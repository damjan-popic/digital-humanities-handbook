#!/usr/bin/env python3
"""Validate case-study pages in every language where they exist."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_HEADINGS = {
    "en": [
        "## What this project does",
        "## Use this when",
        "## What to inspect in the code",
        "## Relevant handbook workflows",
        "## Limits and cautions",
    ],
    "sl": [
        "## Kaj projekt počne",
        "## Kdaj ga uporabiti",
        "## Kaj pregledati v kodi",
        "## Povezani postopki priročnika",
        "## Omejitve in opozorila",
    ],
}


def main() -> int:
    failures: list[str] = []
    checked = 0
    for lang in ("en", "sl"):
        root = ROOT / "docs" / lang / "case-studies"
        files = sorted(p for p in root.glob("*.md") if p.name != "index.md") if root.exists() else []
        for path in files:
            checked += 1
            text = path.read_text(encoding="utf-8")
            rel = path.relative_to(ROOT)
            if "github.com" not in text:
                failures.append(f"{rel}: missing source repository link")
            for heading in REQUIRED_HEADINGS[lang]:
                if heading not in text:
                    failures.append(f"{rel}: missing heading '{heading}'")
    if checked == 0:
        failures.append("No case-study pages found.")
    if failures:
        print("Case-study check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"OK: checked {checked} case-study pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
