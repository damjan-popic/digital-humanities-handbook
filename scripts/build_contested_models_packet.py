#!/usr/bin/env python3
"""Reproduce the issue #25 expected outputs and deterministic download."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile

from scholarly_work_package_utils import deterministic_zip

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / 'teaching-data/contested-models'
ARCHIVE = ROOT / 'docs/assets/downloads/contested-models-v1.zip'
PREFIX = 'contested-models-v1/'
EXPECTED = ('results.json', 'membership.csv', 'candidate-places.csv',
            'gcp-residuals.csv', 'gcp-leave-one-out.csv', 'projection-evidence.csv',
            'projection-singletons.csv')


def build(check=False):
    with tempfile.TemporaryDirectory(prefix='contested-models-build-') as temporary:
        staging = Path(temporary)
        output = staging / 'output'
        result = subprocess.run([sys.executable, str(PACKET / 'run.py'), '--output', str(output)],
                                check=True, capture_output=True, text=True)
        generated = {PACKET / 'expected' / name: (output / name).read_bytes() for name in EXPECTED}
        members = []
        for path in sorted(PACKET.rglob('*')):
            relative = path.relative_to(PACKET)
            if not path.is_file() or any(part in ('expected', '__pycache__') for part in relative.parts):
                continue
            if path.suffix not in ('.py', '.md', '.sql', '.csv', '.json', '.txt', '.jpg'):
                continue
            members.append((PREFIX + relative.as_posix(), path.read_bytes()))
        members.extend((PREFIX + 'expected/' + name, generated[PACKET / 'expected' / name]) for name in EXPECTED)
        archival = ROOT / 'teaching-data/archival-friction'
        extras = {'source/archival-observations.csv': archival / 'reference/observations.csv',
                  'LICENSE.md': ROOT / 'LICENSE.md'}
        for name in ('rights-and-provenance.md', 'rights-and-provenance.sl.md',
                     'RIGHTS.md', 'RIGHTS.sl.md', 'SOURCE_CITATION.md', 'SOURCE_CITATION.sl.md'):
            extras['source/archival-' + name] = archival / name
        members.extend((PREFIX + name, path.read_bytes()) for name, path in extras.items())
        manifest = ''.join(f'{hashlib.sha256(payload).hexdigest()}  {name.removeprefix(PREFIX)}\n'
                           for name, payload in sorted(members)).encode('utf-8')
        members.append((PREFIX + 'SHA256SUMS.txt', manifest))
        packaged = staging / ARCHIVE.name
        deterministic_zip(packaged, members)
        generated[ARCHIVE] = packaged.read_bytes()
        generated[ARCHIVE.with_suffix('.zip.sha256')] = (
            hashlib.sha256(generated[ARCHIVE]).hexdigest() + '  ' + ARCHIVE.name + '\n').encode('ascii')
        stale = []
        for path, payload in generated.items():
            if check:
                if not path.exists() or path.read_bytes() != payload:
                    stale.append(str(path.relative_to(ROOT)))
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(payload)
        if stale:
            raise SystemExit('Stale contested-models artifacts: ' + ', '.join(stale))
        print(result.stdout.strip())
        print(f'OK: {"verified" if check else "generated"} {len(generated)} artifacts; '
              f'{len(members)} deterministic archive members.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    build(parser.parse_args().check)
