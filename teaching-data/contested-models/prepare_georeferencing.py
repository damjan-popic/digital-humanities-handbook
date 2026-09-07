#!/usr/bin/env python3
"""Regenerate cached EPSG:3794 landmark coordinates; no network access."""
from __future__ import annotations

import argparse
import csv
import io
from pathlib import Path

from pyproj import Transformer


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    transformer = Transformer.from_crs('EPSG:4326', 'EPSG:3794', always_xy=True)
    with (root / 'input/landmarks.csv').open(encoding='utf-8', newline='') as stream:
        rows = list(csv.DictReader(stream))
    buffer = io.StringIO(newline='')
    writer = csv.DictWriter(buffer, fieldnames=[*rows[0], 'target_e_m', 'target_n_m'], lineterminator='\n')
    writer.writeheader()
    for row in rows:
        easting, northing = transformer.transform(float(row['longitude']), float(row['latitude']))
        writer.writerow({**row, 'target_e_m': f'{easting:.3f}', 'target_n_m': f'{northing:.3f}'})
    target = root / 'input/gcps.csv'
    expected = buffer.getvalue()
    if args.check:
        if not target.exists() or target.read_text(encoding='utf-8') != expected:
            raise SystemExit('Stale projected control coordinates')
        print('OK: cached EPSG:3794 coordinates match pyproj transformation.')
    else:
        target.write_text(expected, encoding='utf-8', newline='\n')
        print('Generated input/gcps.csv with EPSG:4326 -> EPSG:3794, always_xy=True.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
