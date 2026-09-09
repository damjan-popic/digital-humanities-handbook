#!/usr/bin/env python3
"""Check that generated review manuscripts contain the ecosystem layer."""
from __future__ import annotations

import sys

from build_review_manuscripts import manuscripts
from handbook_structure import CHAPTERS
from intertextuality import ECOSYSTEM_MARKER, ROOT, START_MARKER
from review_links import REPOSITORY_URL, ReviewSource, rewrite_links


def main() -> int:
    failures: list[str] = []
    try:
        source = ReviewSource.load()
        expected = manuscripts(source)
    except (OSError, ValueError) as error:
        print(f"Review-manuscript source check failed:\n{error}")
        return 1
    for locale in ("en", "sl"):
        path = ROOT / "release" / f"review-manuscript-{locale}.md"
        if not path.exists():
            failures.append(f"Missing review manuscript: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        if text != expected[locale]:
            failures.append(f"{path.relative_to(ROOT)}: manuscript differs from its verified source; run make manuscripts")
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
        destinations: list[str] = []
        rewrite_links(text, lambda destination: destinations.append(destination) or destination)
        prefix = f"{REPOSITORY_URL}/blob/{source.source_commit}/docs/"
        if not any(destination.startswith(prefix) for destination in destinations):
            failures.append(f"{path.relative_to(ROOT)}: missing versioned absolute source links")

    if failures:
        print("Review-manuscript ecosystem check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        f"OK: both review manuscripts include the ecosystem overview, {len(CHAPTERS)} chapter connection blocks, "
        "and absolute links to verified source commit " + source.source_commit + "."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
