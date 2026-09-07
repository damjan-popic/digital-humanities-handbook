#!/usr/bin/env python3
"""Query a generated dossier read-only, returning source-qualified CSV."""
import argparse
import csv
from datetime import date, datetime
from pathlib import Path
import sqlite3
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database', required=True, type=Path)
    parser.add_argument('--subject', default='SYN-A')
    parser.add_argument('--as-of', default='1910-06-15')
    parser.add_argument('--known-at', default='2026-09-03T00:00:00Z')
    parser.add_argument('--conflicts', action='store_true')
    args = parser.parse_args()
    date.fromisoformat(args.as_of)
    datetime.strptime(args.known_at, '%Y-%m-%dT%H:%M:%SZ')
    query = 'conflicts.sql' if args.conflicts else 'at-date.sql'
    connection = sqlite3.connect(args.database.resolve().as_uri() + '?mode=ro', uri=True)
    try:
        cursor = connection.execute((Path(__file__).parent / 'queries' / query).read_text(encoding='utf-8'),
                                    {'subject': args.subject, 'as_of': args.as_of, 'known_at': args.known_at})
        writer = csv.writer(sys.stdout, lineterminator='\n')
        writer.writerow(column[0] for column in cursor.description)
        writer.writerows(cursor)
    finally:
        connection.close()


if __name__ == '__main__':
    main()
