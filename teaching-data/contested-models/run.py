#!/usr/bin/env python3
"""Reproduce the issue #25 comparisons using only Python's standard library."""
from __future__ import annotations

import argparse
import csv
from datetime import date, datetime
from itertools import combinations
import json
from pathlib import Path
import sqlite3

import network_analysis
import spatial_analysis

ROOT = Path(__file__).resolve().parent


def read_csv(path):
    with path.open(encoding='utf-8', newline='') as stream:
        return list(csv.DictReader(stream))


def write_csv(path, rows, fields=None):
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields or list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def build_database(path):
    validate_inputs()
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.executescript((ROOT / 'schema.sql').read_text(encoding='utf-8'))
    for row in read_csv(ROOT / 'input/entities.csv'):
        connection.execute('INSERT INTO entity VALUES (?,?,?,?)', tuple(row.values()))
    for row in read_csv(ROOT / 'input/documents.csv'):
        connection.execute('INSERT INTO source VALUES (?,?,?)',
                           (row['document_id'], row['source_locator'], 'true'))
    for source in ('SYN-N1', 'SYN-N2', 'SYN-BORDER', 'SYN-NAMES'):
        connection.execute('INSERT INTO source VALUES (?,?,?)',
                           (source, 'input/dossier.md: ' + source, 'true'))
    for row in read_csv(ROOT / 'input/assertions.csv'):
        values = tuple(value or None for value in row.values())
        connection.execute('INSERT INTO assertion VALUES (' + ','.join('?' for _ in values) + ')', values)
    connection.commit()
    return connection


def validate_interval(start, end):
    if date.fromisoformat(start).isoformat() != start or date.fromisoformat(end).isoformat() != end:
        raise ValueError('Use canonical Gregorian YYYY-MM-DD dates')
    if start >= end:
        raise ValueError('Half-open intervals require start < end')


def validate_inputs():
    for name in ('assertions', 'boundaries', 'toponyms', 'documents'):
        rows = read_csv(ROOT / 'input' / f'{name}.csv')
        start, end = ('date_start', 'date_end') if name == 'documents' else ('valid_start', 'valid_end')
        for row in rows:
            validate_interval(row[start], row[end])
            if row.get('synthetic') != 'true':
                raise ValueError(f'{name}: synthetic records must be labelled')
            if 'recorded_at' in row:
                timestamp = row['recorded_at']
                if datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%dT%H:%M:%SZ') != timestamp:
                    raise ValueError('Use canonical UTC record timestamps')
    people = {row['entity_id'] for row in read_csv(ROOT / 'input/entities.csv') if row['kind'] == 'person'}
    documents = {row['document_id'] for row in read_csv(ROOT / 'input/documents.csv')}
    seen = set()
    for row in read_csv(ROOT / 'input/participation.csv'):
        pair = (row['person_id'], row['document_id'])
        if pair in seen or pair[0] not in people or pair[1] not in documents:
            raise ValueError('Participation must be unique and reference known people/documents')
        seen.add(pair)


def run(output):
    output.mkdir(parents=True, exist_ok=False)
    connection = build_database(output / 'dossier.sqlite')
    at_date = (ROOT / 'queries/at-date.sql').read_text(encoding='utf-8')
    conflicts = [dict(row) for row in connection.execute((ROOT / 'queries/conflicts.sql').read_text(encoding='utf-8'))]
    write_csv(output / 'status-conflicts.csv', conflicts)
    snapshots = {}
    for label, as_of, known_at in [('1910_early', '1910-06-15', '2026-09-01T23:59:59Z'),
                                 ('1910_corrected', '1910-06-15', '2026-09-03T00:00:00Z'),
                                 ('1925', '1925-01-25', '2026-09-03T00:00:00Z')]:
        snapshots[label] = [dict(row) for row in connection.execute(at_date,
                           {'subject': 'SYN-A', 'as_of': as_of, 'known_at': known_at})]
        write_csv(output / f'assertions-{label}.csv', snapshots[label])
    current_count = connection.execute('SELECT count(*) FROM current_assertion').fetchone()[0]
    assertion_count = connection.execute('SELECT count(*) FROM assertion').fetchone()[0]
    integrity = connection.execute('PRAGMA integrity_check').fetchone()[0]
    foreign_keys = list(connection.execute('PRAGMA foreign_key_check'))
    connection.close()
    archival_path = ROOT.parent / 'archival-friction/reference/observations.csv'
    if not archival_path.exists():
        archival_path = ROOT / 'source/archival-observations.csv'
    archival = read_csv(archival_path)
    individuals = [row for row in archival if row['entity_structure'] == 'one_person']
    archival_edges = [{'observation_a': a['record_id'], 'observation_b': b['record_id'],
                       'source_id': 'AF-ISSUE-001', 'rule': 'same_issue_not_interaction',
                       'source_locator_a': a['source_locator'], 'source_locator_b': b['source_locator']}
                      for a, b in combinations(individuals, 2)]
    write_csv(output / 'authentic-issue-cooccurrence.csv', archival_edges)
    result = {'database': {'assertion_count': assertion_count, 'current_assertion_count': current_count,
                           'conflicts': conflicts, 'snapshots': snapshots, 'integrity_check': integrity,
                           'foreign_key_errors': len(foreign_keys)},
              'authentic': {'reference_observations': len(archival), 'individually_labelled_people': len(individuals),
                            'same_issue_edges': len(archival_edges), 'correspondence_edges_evidenced': 0},
              'networks': network_analysis.compare(ROOT, output, read_csv, write_csv),
              'gis': spatial_analysis.compare(ROOT, output, read_csv, write_csv)}
    (output / 'results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'database_current_assertions': current_count, 'authentic_issue_edges': len(archival_edges),
                      'graph_edges': {name: graph['edge_count'] for name, graph in result['networks'].items()},
                      'fit_rmse_m': result['gis']['fit_rmse_m'],
                      'independent_check_rmse_m': result['gis']['independent_check_rmse_m']}, ensure_ascii=False))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path, help='New output directory; existing directories are never overwritten')
    args = parser.parse_args()
    run(args.output)
