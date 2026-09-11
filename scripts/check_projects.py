#!/usr/bin/env python3
"""Validate critical case metadata, audited legacy debt and deterministic catalogues."""
from __future__ import annotations

import json
import sys

import yaml

from build_case_study_index import check_generated
from case_studies import INDEX, ROOT, load_records, validate_records


def main() -> int:
    try:
        records = load_records()
        validate_records(records)
        # Validate committed JSON too; same-type drift is not silently ignored.
        validate_records(json.loads((ROOT / INDEX).read_text(encoding="utf-8")))
        check_generated(records)
    except (OSError, ValueError, KeyError, yaml.YAMLError) as error:
        print(f"Case-study check failed: {error}")
        return 1
    legacy = sum(record["content_standard"] == "legacy-audited" for record in records)
    showcase = sum(record["content_standard"] == "showcase-v1" for record in records)
    print(f"OK: {len(records)} case records; {legacy} legacy-audited, {showcase} showcase-v1; "
          "schema, separate lifecycle/editorial disposition, inspection modes, six component rights records and their summary, "
          "dated audit anchors, page/translation declarations, canonical connections and 3 generated outputs agree. No external network checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
