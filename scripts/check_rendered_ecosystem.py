#!/usr/bin/env python3
"""Smoke-test the rendered HTML produced by the intertextuality hook."""
from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


class TextCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        cleaned = " ".join(data.split())
        if cleaned:
            self.parts.append(cleaned)

    @property
    def text(self) -> str:
        return " ".join(self.parts)


def inspect_page(
    relative_path: str,
    expected_text: tuple[str, ...],
    expected_html: tuple[str, ...],
    failures: list[str],
) -> None:
    path = SITE / relative_path
    if not path.exists():
        failures.append(f"Missing rendered page: {path.relative_to(ROOT)}")
        return

    html = path.read_text(encoding="utf-8")
    parser = TextCollector()
    parser.feed(html)
    text = parser.text

    for needle in expected_text:
        if needle not in text:
            failures.append(
                f"{path.relative_to(ROOT)}: missing rendered text {needle!r}"
            )
    for needle in expected_html:
        if needle not in html:
            failures.append(
                f"{path.relative_to(ROOT)}: missing rendered HTML fragment {needle!r}"
            )

    if "handbook-ecosystem-map" in html:
        failures.append(f"{path.relative_to(ROOT)}: unresolved ecosystem marker")


def main() -> int:
    failures: list[str] = []

    inspect_page(
        "ecosystem/index.html",
        (
            "Handbook ecosystem",
            "From chapters to practice",
            "Connections work in both directions",
        ),
        (
            "analyse-emotion-with-a-lexicon-and-manual-check/",
            "medieval-ner/",
        ),
        failures,
    )
    inspect_page(
        "sl/ecosystem/index.html",
        (
            "Ekosistem priročnika",
            "Od poglavij k praksi",
            "angleška nadomestna stran",
        ),
        (
            "analyse-emotion-with-a-lexicon-and-manual-check/",
            "medieval-ner/",
        ),
        failures,
    )
    inspect_page(
        "chapters/what-is-digital-humanities/index.html",
        (
            "Continue through the ecosystem",
            "Try a workflow",
            "Inspect a case study",
        ),
        (
            "make-a-tiny-digital-edition-of-a-historical-text/",
            "ladakh-relations/",
        ),
        failures,
    )
    inspect_page(
        "workflows/text-analysis/analyse-emotion-with-a-lexicon-and-manual-check/index.html",
        (
            "Where this workflow fits",
            "Conceptual chapters",
        ),
        (
            "topics-emotions-classification/",
        ),
        failures,
    )
    inspect_page(
        "case-studies/medieval-ner/index.html",
        (
            "Read this case across the handbook",
            "Executable workflows",
        ),
        (
            "models-evidence-interpretation/",
            "map-places-mentioned-in-a-text/",
        ),
        failures,
    )

    if failures:
        print("Rendered ecosystem check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "OK: rendered ecosystem overview, chapter, workflow, and case-study pages contain reciprocal links; the Slovene overview exposes fallback labels."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
