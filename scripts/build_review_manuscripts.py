#!/usr/bin/env python3
"""Build deterministic review manuscripts from the stable bilingual core."""
from __future__ import annotations

import re
from pathlib import Path

from handbook_structure import COURSE_PATHS, PARTS, SECTION_LABELS
from intertextuality import inject_connections, inject_ecosystem

ROOT = Path(__file__).resolve().parents[1]
META = {
    "en": {
        "title": "Digital Humanities Handbook",
        "subtitle": "Stable core and course pathways — development review snapshot",
        "note": "This file is generated from the version-controlled source. The public web edition is canonical for navigation and interactive material.",
        "version_label": "Version",
        "date_label": "Date",
        "author_editor_label": "Author/editor",
    },
    "sl": {
        "title": "Priročnik za digitalno humanistiko",
        "subtitle": "Stabilno jedro in učni poti — razvojni recenzijski posnetek",
        "note": "Datoteka je samodejno sestavljena iz verzioniranega izvornega besedila. Za navigacijo in interaktivno gradivo je merodajna spletna izdaja.",
        "version_label": "Različica",
        "date_label": "Datum",
        "author_editor_label": "Avtor/urednik",
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


def append_page(
    out: list[str],
    path: Path,
    locale: str,
    relative_path: str,
) -> None:
    text = strip_front_matter(path.read_text(encoding="utf-8"))
    if relative_path == "ecosystem.md":
        text = inject_ecosystem(text, locale, link_mode="absolute")
    elif relative_path.startswith("chapters/") and relative_path != "chapters/index.md":
        text = inject_connections(
            text,
            relative_path,
            locale,
            link_mode="absolute",
        )
    out.extend([demote_title(text).rstrip(), "", "---", ""])


def build(locale: str) -> None:
    meta = META[locale]
    labels = SECTION_LABELS[locale]
    out = [
        f"# {meta['title']}",
        "",
        f"**{meta['subtitle']}**",
        "",
        f"**{meta['version_label']}:** 0.1.0-dev<br>",
        f"**{meta['date_label']}:** 2026-07-23<br>",
        f"**{meta['author_editor_label']}:** Damjan Popič",
        "",
        f"> {meta['note']}",
        "",
        "---",
        "",
        f"# {labels['orientation']}",
        "",
    ]
    append_page(
        out,
        ROOT / "docs" / locale / "chapters" / "index.md",
        locale,
        "chapters/index.md",
    )
    append_page(
        out,
        ROOT / "docs" / locale / "ecosystem.md",
        locale,
        "ecosystem.md",
    )
    for heading, filenames in zip(labels["parts"], PARTS, strict=True):
        out.extend([f"# {heading}", ""])
        for filename in filenames:
            append_page(
                out,
                ROOT / "docs" / locale / "chapters" / filename,
                locale,
                f"chapters/{filename}",
            )
    out.extend([f"# {labels['course_pathways']}", ""])
    for filename in COURSE_PATHS:
        append_page(
            out,
            ROOT / "docs" / locale / "learning-paths" / filename,
            locale,
            f"learning-paths/{filename}",
        )
    target = ROOT / "release" / f"review-manuscript-{locale}.md"
    target.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {target.relative_to(ROOT)}")


if __name__ == "__main__":
    for lang in ("en", "sl"):
        build(lang)
