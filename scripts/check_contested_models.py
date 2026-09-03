#!/usr/bin/env python3
"""Regression checks for issue #25's paired chapters, workflows and source models."""
from __future__ import annotations

from datetime import date
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import subprocess
import sys
import tempfile
from zipfile import ZipFile

import yaml

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / 'teaching-data/contested-models'
sys.path.insert(0, str(PACKET))
import network_analysis as networks
import spatial_analysis as spatial
import run as runner

CHAPTERS = ('databases-sql', 'gis-spatial-humanities', 'networks-visualization')
WORKFLOWS = (
    'data/model-changing-names-statuses-and-boundaries-in-sqlite.md',
    'mapping/georeference-and-check-a-historical-map-in-qgis.md',
    'mapping/model-changing-place-names-and-boundaries.md',
    'networks/compare-bipartite-and-projected-networks.md',
    'networks/audit-a-network-claim-against-source-records.md',
)
MAP_HASH = 'd3c6c0475a6976c69c99065b7b9df1ae57a5fe6416a9acc858ef0cf75aebf21c'


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def word_count(text, lang):
    """Count visible prose/table tokens; exclude metadata, fences, notes and references."""
    text = re.sub(r'\A---\n.*?\n---\n', '', text, flags=re.S)
    text = text.split('## Further reading' if lang == 'en' else '## Nadaljnje branje')[0]
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    text = re.sub(r'^\[\^[^\]]+\]:.*(?:\n[ \t]+.*)*', '', text, flags=re.M)
    text = re.sub(r'\[([^\]]+)\]\([^\n)]+\)', r'\1', text)
    text = re.sub(r'<[^>]+>', '', text)
    return len(re.findall(r"[^\W_]+(?:[’'-][^\W_]+)*", text, re.UNICODE))


def executable_blocks(text):
    return re.findall(r'```(?:bash|sql|python)\n(.*?)```', text, flags=re.S)


def check_pages():
    counts = {}
    required = {
        'en': ('Learning outcomes', 'Before you begin', 'Practice', 'Reflection', 'Summary', 'Further reading', 'Hybrid modelling'),
        'sl': ('Učni cilji', 'Pred začetkom', 'Vaja', 'Refleksija', 'Povzetek', 'Nadaljnje branje', 'Hibridno modeliranje'),
    }
    mapping = yaml.safe_load((ROOT / 'intertextuality.yml').read_text(encoding='utf-8'))
    for chapter in CHAPTERS:
        pair = []
        for lang in ('en', 'sl'):
            path = ROOT / f'docs/{lang}/chapters/{chapter}.md'
            text = path.read_text(encoding='utf-8')
            pair.append(text)
            for heading in required[lang]:
                require(f'## {heading}\n' in text, f'{path}: missing {heading}')
            count = word_count(text, lang)
            require(2300 <= count <= 3300, f'{path}: {count} words outside target')
            counts[f'{lang}/{chapter}'] = count
            require('contested-models-v1.zip' in text, f'{path}: missing reproducible packet')
            require('| ' in text, f'{path}: missing non-visual comparison table')
            require('status: draft' in text, f'{path}: review status lost')
            if lang == 'sl':
                require('translation_status: machine-assisted draft; requires human language review' in text,
                        f'{path}: translation review status lost')
        require(executable_blocks(pair[0]) == executable_blocks(pair[1]), f'{chapter}: executable bilingual divergence')
        dois = [set(re.findall(r'https://doi.org/[^)\s]+', text)) for text in pair]
        require(dois[0] == dois[1], f'{chapter}: paired scholarly references differ')
    for workflow in WORKFLOWS:
        pair = [(ROOT / f'docs/{lang}/workflows/{workflow}').read_text(encoding='utf-8') for lang in ('en', 'sl')]
        require(executable_blocks(pair[0]) == executable_blocks(pair[1]), f'{workflow}: executable bilingual divergence')
        require(all('contested-models-v1.zip' in text for text in pair), f'{workflow}: missing download')
        require('workflows/' + workflow in mapping['workflows'], f'{workflow}: missing explicit mapping')
        if workflow.startswith(('mapping/', 'networks/')):
            require(all('|' in text or 'table' in text.lower() or 'tabel' in text.lower() for text in pair),
                    f'{workflow}: missing non-visual route')
    print('Word counts (visible prose/table tokens, excluding references/metadata/fenced code):')
    for name, count in counts.items():
        print(f'  {name}: {count}')
    return counts


def rejected(connection, sql, parameters=()):
    connection.execute('SAVEPOINT negative_test')
    try:
        try:
            connection.execute(sql, parameters)
        except sqlite3.IntegrityError:
            return
        raise AssertionError('Invalid database mutation was accepted: ' + sql)
    finally:
        connection.execute('ROLLBACK TO negative_test')
        connection.execute('RELEASE negative_test')


def check_database(path):
    con = runner.build_database(path)
    try:
        require(con.execute('PRAGMA foreign_keys').fetchone()[0] == 1, 'Foreign keys disabled')
        original = dict(con.execute("SELECT * FROM assertion WHERE assertion_id='SYN-A05'").fetchone())
        for changes in ({'assertion_id': 'BAD', 'subject_id': 'MISSING'},
                        {'assertion_id': 'BAD', 'source_id': 'MISSING'},
                        {'assertion_id': 'BAD', 'object_id': 'SYN-L1'},
                        {'assertion_id': 'BAD', 'valid_end': '1900-01-01'},
                        {'assertion_id': 'BAD', 'supersedes': 'SYN-A01'},
                        {'assertion_id': 'BAD', 'supersedes': 'SYN-A05'},
                        {'assertion_id': 'BAD', 'value_text': None},
                        {}):
            row = original | changes
            rejected(con, 'INSERT INTO assertion VALUES (' + ','.join('?' for _ in row) + ')', tuple(row.values()))
        rejected(con, "UPDATE assertion SET value_text='erased' WHERE assertion_id='SYN-A05'")
        rejected(con, "DELETE FROM assertion WHERE assertion_id='SYN-A05'")
        query = (PACKET / 'queries/at-date.sql').read_text(encoding='utf-8')
        def at(subject, day, known='2026-09-03T00:00:00Z'):
            return [dict(row) for row in con.execute(query, {'subject': subject, 'as_of': day, 'known_at': known})]
        require([row['object_id'] for row in at('SYN-L1', '1919-12-31')] == ['SYN-EAST'], 'Old boundary endpoint')
        require([row['object_id'] for row in at('SYN-L1', '1920-01-01')] == ['SYN-W'], 'New boundary endpoint')
        before = at('SYN-A', '1910-06-15', '2026-09-01T23:59:59Z')
        after = at('SYN-A', '1910-06-15')
        require(any(row['value_text'] == 'Ana Kovać' for row in before), 'Earlier editorial state lost')
        require(any(row['value_text'] == 'Ana Kovač' for row in after), 'Correction absent')
        require(not any(row['value_text'] == 'Ana Kovać' for row in after), 'Superseded value leaks')
        statuses = [row for row in after if row['predicate'] == 'status']
        require(len(statuses) == 2, 'Source disagreement collapsed')
        require(sum(row['context'] == 'municipal_register' for row in statuses) == 1, 'Status sensitivity mismatch')
        require(at('SYN-A', '1910-06-15', '2026-08-31T00:00:00Z') == [], 'Future editorial record leaks')
        require(not any(row['predicate'] == 'name' for row in at('SYN-A', '1910-06-16')), 'Event upper bound included')
    finally:
        con.close()
    for start, end in [('1910-02-30', '1911-01-01'), ('19100101', '1911-01-01'),
                       ('1910-01-01', '1910-01-01')]:
        try:
            runner.validate_interval(start, end)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid date interval accepted')


def check_math():
    chain = networks.graph_metrics(['a', 'b', 'c', 'z'], [('a', 'b'), ('b', 'c')])
    b = next(row for row in chain['metrics'] if row['node'] == 'b')
    require(b['degree'] == 2 and b['betweenness_raw'] == 1, 'Undirected path benchmark')
    require(b['harmonic_closeness'] == 0.666667, 'Disconnected harmonic convention')
    directed = networks.graph_metrics(['a', 'b', 'c'], [('a', 'b'), ('b', 'c')], directed=True)
    require(directed['metrics'][0]['harmonic_closeness'] == 0.75, 'Directed harmonic benchmark')
    require(directed['metrics'][1]['betweenness_raw'] == 1, 'Directed betweenness benchmark')
    require(networks.graph_metrics(['a', 'b'], [('a', 'b'), ('b', 'a')])['edge_count'] == 1,
            'Duplicate undirected endpoints inflate metrics')
    require(len(list(networks.partitions(tuple('abcdef')))) == 203, 'Partition enumeration')
    complete = [(u, v) for u in 'abc' for v in 'abc' if u < v]
    optimum = networks.communities(list('abc'), complete)
    require(optimum['modularity'] == 0 and len(optimum['partitions']) == 1, 'Complete graph modularity')
    points = [{'source_x_px': x, 'source_y_px': y, 'target_e_m': 10 + 2*x + 3*y,
               'target_n_m': 20 - x + 4*y} for x, y in [(0, 0), (100, 0), (0, 100), (100, 100)]]
    fit = spatial.fit_affine(points)
    require(all(spatial.residual(row, fit) < 1e-8 for row in points), 'Known affine transform')
    try:
        spatial.fit_affine([points[0]] * 3)
    except ValueError:
        pass
    else:
        raise AssertionError('Singular affine controls accepted')


def check_results(result):
    expected_edges = {'bipartite': 18, 'projection_t1': 15, 'projection_t2': 7,
                      'projection_t3': 2, 'without_press_list': 7, 'fractional_ge_1': 3,
                      'correspondence': 3, 'correspondence_certain': 2, 'missing_D6': 6}
    for name, edges in expected_edges.items():
        require(result['networks'][name]['edge_count'] == edges, f'{name}: edge regression')
    def metric(graph, node, field):
        return next(row[field] for row in result['networks'][graph]['metrics'] if row['node'] == node)
    require(metric('projection_t2', 'SYN-C', 'betweenness_raw') == 6, 'C betweenness')
    require(metric('projection_t2', 'SYN-E', 'betweenness_raw') == 4, 'E betweenness')
    require(metric('missing_D6', 'SYN-E', 'betweenness_raw') == 0, 'Missingness sensitivity')
    require(len(result['networks']['projection_t3']['communities']['partitions']) == 10, 'Tied partitions lost')
    require(result['authentic']['same_issue_edges'] == 6 and result['authentic']['correspondence_edges_evidenced'] == 0,
            'Authentic and synthetic evidence conflated')
    gis = result['gis']
    require(gis['fit_rmse_m'] == 15.231 and gis['independent_check_rmse_m'] == 220.063, 'GIS residual regression')
    l1 = [row for row in gis['memberships'] if row['place_id'] == 'SYN-L1']
    require([row['centre_membership'] for row in l1] == ['SYN-EAST', 'SYN-W'], 'Fixed place/boundary change')
    require(all(row['possible_memberships'] == 'SYN-W|SYN-EAST' for row in l1), 'Uncertainty hidden')
    require(len(gis['candidate_places']) == 4, 'Unresolved candidates dropped')


def check_provenance():
    require(hashlib.sha256((PACKET / 'source/ljubljana-1910.jpg').read_bytes()).hexdigest() == MAP_HASH, 'Source map changed')
    dossier = (PACKET / 'input/dossier.md').read_text(encoding='utf-8')
    for row in runner.read_csv(PACKET / 'input/documents.csv'):
        file, anchor = row['source_locator'].split('#')
        require((PACKET / file).exists() and f'id="{anchor}"' in dossier, 'Broken source locator')
    for name in ('README', 'rights-and-provenance', 'data-dictionary'):
        require(all((PACKET / f'{name}{suffix}.md').is_file() for suffix in ('', '.sl')), 'Missing paired packet document')
        require('strojno' in (PACKET / f'{name}.sl.md').read_text(encoding='utf-8').lower(),
                f'{name}.sl.md: translation-review marker missing')
    require('strojno' in (PACKET / 'input/dossier.sl.md').read_text(encoding='utf-8').lower(),
            'dossier.sl.md: translation-review marker missing')
    for row in runner.read_csv(PACKET / 'input/candidates.csv'):
        require(row['review_status'] == 'unresolved' and row['synthetic'] == 'true', 'Candidate promoted without evidence')


def check_download():
    archive = ROOT / 'docs/assets/downloads/contested-models-v1.zip'
    prefix = 'contested-models-v1/'
    with ZipFile(archive) as zipped, tempfile.TemporaryDirectory(prefix='contested-models-download-') as temp:
        require(zipped.testzip() is None, 'Corrupt ZIP')
        for line in zipped.read(prefix + 'SHA256SUMS.txt').decode('utf-8').splitlines():
            digest, name = line.split('  ', 1)
            require(hashlib.sha256(zipped.read(prefix + name)).hexdigest() == digest, 'Manifest mismatch: ' + name)
        require(zipped.read(prefix + 'source/archival-observations.csv') ==
                (ROOT / 'teaching-data/archival-friction/reference/observations.csv').read_bytes(), 'Observation extract changed')
        # Reject unsafe members before extracting the locally built teaching archive.
        require(all(not Path(name).is_absolute() and '..' not in Path(name).parts for name in zipped.namelist()), 'Unsafe archive path')
        zipped.extractall(temp)
        unpacked = Path(temp) / prefix
        subprocess.run([sys.executable, str(unpacked / 'run.py'), '--output', str(unpacked / 'output')],
                       check=True, capture_output=True)
        downloaded_result = json.loads((unpacked / 'output/results.json').read_text(encoding='utf-8'))
        check_results(downloaded_result)
        # A second run must refuse to overwrite the user's first output.
        rerun = subprocess.run([sys.executable, str(unpacked / 'run.py'), '--output', str(unpacked / 'output')],
                               capture_output=True)
        require(rerun.returncode != 0, 'Output directory was silently overwritten')
        query = subprocess.run([sys.executable, str(unpacked / 'query.py'), '--database',
                                str(unpacked / 'output/dossier.sqlite'), '--as-of', '1910-06-15'],
                               check=True, capture_output=True, text=True, encoding='utf-8')
        require('Ana Kovač' in query.stdout and 'Ana Kovać' not in query.stdout, 'Download query mismatch')


def main():
    counts = check_pages()
    check_math()
    check_provenance()
    with tempfile.TemporaryDirectory(prefix='contested-models-check-') as temp:
        check_database(Path(temp) / 'negative.sqlite')
        result = runner.run(Path(temp) / 'output')
        check_results(result)
    check_download()
    print('OK: 6 chapters, 10 workflows; paired prose/code/references; SQL negative and temporal tests; '
          'graph/affine benchmarks; source provenance; standalone ZIP and query checks.')
    return counts


if __name__ == '__main__':
    main()
