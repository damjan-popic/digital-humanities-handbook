#!/usr/bin/env python3
"""Validate the bilingual stable core and course paths."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = [
    "what-is-digital-humanities.md",
    "history-of-digital-humanities.md",
    "models-evidence-interpretation.md",
    "critical-infrastructures.md",
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
PATHS = ["pismenost-za-informacijsko-druzbo.md", "digitalna-slovenistika.md"]
HEADINGS = {
    "en": ["## Learning outcomes", "## Before you begin", "## Practice", "## Reflection", "## Summary"],
    "sl": ["## Učni cilji", "## Pred začetkom", "## Vaja", "## Refleksija", "## Povzetek"],
}


def main() -> int:
    failures: list[str] = []
    for lang in ("en", "sl"):
        for filename in CHAPTERS:
            path = ROOT / "docs" / lang / "chapters" / filename
            if not path.exists():
                failures.append(f"Missing paired chapter: {path.relative_to(ROOT)}")
                continue
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---\n"):
                failures.append(f"{path.relative_to(ROOT)}: missing frontmatter")
            for heading in HEADINGS[lang]:
                if heading not in text:
                    failures.append(f"{path.relative_to(ROOT)}: missing '{heading}'")
        for filename in PATHS:
            path = ROOT / "docs" / lang / "learning-paths" / filename
            if not path.exists():
                failures.append(f"Missing course path: {path.relative_to(ROOT)}")
            elif "## Learning outcomes" not in path.read_text(encoding="utf-8") and "## Učni izidi" not in path.read_text(encoding="utf-8"):
                failures.append(f"{path.relative_to(ROOT)}: missing learning outcomes")
    if failures:
        print("Handbook core check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"OK: bilingual stable core has {len(CHAPTERS)} paired chapters and {len(PATHS)} paired learning paths.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
