#!/usr/bin/env python3
"""Check that generated review manuscripts contain the ecosystem layer."""
from __future__ import annotations

import sys

from handbook_structure import CHAPTERS
from intertextuality import ECOSYSTEM_MARKER, ROOT, SITE_URL, START_MARKER


def main() -> int:
    failures: list[str] = []
    for locale in ("en", "sl"):
        path = ROOT / "release" / f"review-manuscript-{locale}.md"
        if not path.exists():
            failures.append(f"Missing review manuscript: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        title = "## Ekosistem priročnika" if locale == "sl" else "## Handbook ecosystem"
        if title not in text:
            failures.append(f"{path.relative_to(ROOT)}: missing ecosystem overview")
        block_count = text.count(START_MARKER)
        if block_count != len(CHAPTERS):
            failures.append(
                f"{path.relative_to(ROOT)}: expected {len(CHAPTERS)} chapter ecosystem blocks, "
                f"found {block_count}"
            )
        if ECOSYSTEM_MARKER in text:
            failures.append(f"{path.relative_to(ROOT)}: unresolved ecosystem marker")
        if SITE_URL not in text:
            failures.append(f"{path.relative_to(ROOT)}: missing absolute ecosystem links")

    if failures:
        print("Review-manuscript ecosystem check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        f"OK: both review manuscripts include the ecosystem overview and {len(CHAPTERS)} chapter connection blocks."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
