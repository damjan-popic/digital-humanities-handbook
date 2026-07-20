#!/usr/bin/env python3
"""Validate English and Slovene workflow pages with localized conventions."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_META = {"title", "description", "category", "difficulty", "time", "tags"}
REQUIRED_HEADINGS = {
    "en": [
        "## What you are trying to do",
        "## Output",
        "## Check yourself",
        "## Common traps",
    ],
    "sl": [
        "## Kaj želite doseči",
        "## Rezultat",
        "## Preverite se",
        "## Pogoste pasti",
    ],
}
PROCESS_HEADINGS = {
    "en": ["## Workflow", "## Procedure"],
    "sl": ["## Postopek"],
}


def read_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    meta: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    return meta


def main() -> int:
    failures: list[str] = []
    checked = 0
    for lang in ("en", "sl"):
        root = ROOT / "docs" / lang / "workflows"
        files = sorted(p for p in root.rglob("*.md") if p.name != "index.md")
        if not files:
            failures.append(f"No workflow pages found under {root.relative_to(ROOT)}")
            continue
        for path in files:
            checked += 1
            text = path.read_text(encoding="utf-8")
            rel = path.relative_to(ROOT)
            meta = read_frontmatter(text)
            missing = REQUIRED_META - meta.keys()
            for key in sorted(missing):
                failures.append(f"{rel}: missing frontmatter key '{key}'")
            title = meta.get("title", "").strip('"')
            if lang == "en" and title and not re.match(r"How do I .+\?$", title):
                failures.append(f"{rel}: English title should be 'How do I ...?'")
            if lang == "sl" and title and not re.match(r"Kako .+\?$", title):
                failures.append(f"{rel}: Slovene title should be a 'Kako ...?' question")
            for heading in REQUIRED_HEADINGS[lang]:
                if heading not in text:
                    failures.append(f"{rel}: missing heading '{heading}'")
            if not any(h in text for h in PROCESS_HEADINGS[lang]):
                failures.append(f"{rel}: missing workflow/procedure heading")

    if failures:
        print("Workflow check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"OK: checked {checked} workflow pages in English and Slovene.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
