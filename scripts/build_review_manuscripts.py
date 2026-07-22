#!/usr/bin/env python3
"""Build deterministic review manuscripts from the stable bilingual core."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = [
    "what-is-digital-humanities.md",
    "history-of-digital-humanities.md",
    "models-evidence-interpretation.md",
    "research-design.md",
    "data-metadata-models.md",
    "texts-corpora-ocr.md",
    "linguistic-annotation-classla.md",
    "text-analysis.md",
    "topics-emotions-classification.md",
    "databases-sql.md",
    "gis-spatial-humanities.md",
    "networks-visualization.md",
    "ai-ethics-reproducibility.md",
    "open-living-handbook.md",
]
PATHS = [
    "pismenost-za-informacijsko-druzbo.md",
    "digitalna-slovenistika.md",
]
META = {
    "en": {
        "title": "Digital Humanities Handbook",
        "subtitle": "Stable core and course pathways — development review snapshot",
        "part1": "Part I: Handbook chapters",
        "part2": "Part II: Course pathways",
        "note": "This file is generated from the version-controlled source. The public web edition is canonical for navigation and interactive material.",
    },
    "sl": {
        "title": "Priročnik za digitalno humanistiko",
        "subtitle": "Stabilno jedro in učni poti — razvojni recenzijski posnetek",
        "part1": "I. del: Poglavja priročnika",
        "part2": "II. del: Učni poti",
        "note": "Datoteka je samodejno sestavljena iz verzioniranega izvornega besedila. Za navigacijo in interaktivno gradivo je merodajna spletna izdaja.",
    },
}


def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        _, _, rest = text.partition("\n---\n")
        return rest.lstrip()
    return text


def demote_title(text: str) -> str:
    # Preserve the page title as an H2 inside the combined manuscript.
    return re.sub(r"(?m)^# ", "## ", text, count=1)


def build(locale: str) -> None:
    meta = META[locale]
    out = [
        f"# {meta['title']}",
        "",
        f"**{meta['subtitle']}**",
        "",
        "**Version:** 0.1.0-dev  ",
        "**Date:** 2026-07-20  ",
        "**Author/editor:** Damjan Popič",
        "",
        f"> {meta['note']}",
        "",
        "---",
        "",
        f"# {meta['part1']}",
        "",
    ]
    for filename in CHAPTERS:
        p = ROOT / "docs" / locale / "chapters" / filename
        out.extend([demote_title(strip_front_matter(p.read_text(encoding="utf-8"))).rstrip(), "", "---", ""])
    out.extend([f"# {meta['part2']}", ""])
    for filename in PATHS:
        p = ROOT / "docs" / locale / "learning-paths" / filename
        out.extend([demote_title(strip_front_matter(p.read_text(encoding="utf-8"))).rstrip(), "", "---", ""])
    target = ROOT / "release" / f"review-manuscript-{locale}.md"
    target.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {target.relative_to(ROOT)}")


if __name__ == "__main__":
    for lang in ("en", "sl"):
        build(lang)
