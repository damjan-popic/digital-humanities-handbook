#!/usr/bin/env python3
"""Build deterministic review manuscripts from the stable bilingual core."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from handbook_structure import COURSE_PATHS, PARTS, SECTION_LABELS
from intertextuality import inject_connections, inject_ecosystem
from review_links import REPOSITORY_URL, ReviewSource

ROOT = Path(__file__).resolve().parents[1]
META = {
    "en": {
        "title": "Digital Humanities Handbook",
        "subtitle": "Stable core and course pathways — development review snapshot",
        "note": "This development review snapshot is not a numbered edition. Repository links identify the recorded source commit; the public web edition remains the living edition.",
        "version_label": "Version",
        "date_label": "Source snapshot date (UTC)",
        "source_label": "Source commit",
        "author_editor_label": "Author/editor",
    },
    "sl": {
        "title": "Priročnik za digitalno humanistiko",
        "subtitle": "Stabilno jedro in učni poti — razvojni recenzijski posnetek",
        "note": "Ta razvojni recenzijski posnetek ni oštevilčena izdaja. Povezave v repozitorij vodijo do zapisanega izvornega commita; spletna izdaja ostaja sproti posodabljana živa izdaja.",
        "version_label": "Različica",
        "date_label": "Datum izvornega posnetka (UTC)",
        "source_label": "Izvorni commit",
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
    source: ReviewSource,
) -> None:
    text = strip_front_matter(path.read_text(encoding="utf-8"))
    if relative_path == "ecosystem.md":
        text = inject_ecosystem(text, locale)
    elif relative_path.startswith("chapters/") and relative_path != "chapters/index.md":
        text = inject_connections(
            text,
            relative_path,
            locale,
        )
    text = source.rewrite(text, path)
    out.extend([demote_title(text).rstrip(), "", "---", ""])


def build(locale: str, source: ReviewSource) -> str:
    meta = META[locale]
    labels = SECTION_LABELS[locale]
    out = [
        f"# {meta['title']}",
        "",
        f"**{meta['subtitle']}**",
        "",
        f"**{meta['version_label']}:** 0.1.0-dev<br>",
        f"**{meta['date_label']}:** {source.source_date}<br>",
        f"**{meta['source_label']}:** [{source.source_commit}]({REPOSITORY_URL}/commit/{source.source_commit})<br>",
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
        source,
    )
    append_page(
        out,
        ROOT / "docs" / locale / "ecosystem.md",
        locale,
        "ecosystem.md",
        source,
    )
    for heading, filenames in zip(labels["parts"], PARTS, strict=True):
        out.extend([f"# {heading}", ""])
        for filename in filenames:
            append_page(
                out,
                ROOT / "docs" / locale / "chapters" / filename,
                locale,
                f"chapters/{filename}",
                source,
            )
    out.extend([f"# {labels['course_pathways']}", ""])
    for filename in COURSE_PATHS:
        append_page(
            out,
            ROOT / "docs" / locale / "learning-paths" / filename,
            locale,
            f"learning-paths/{filename}",
            source,
        )
    return "\n".join(out).rstrip() + "\n"


def manuscripts(source: ReviewSource) -> dict[str, str]:
    for relative in (
        ".gitattributes",
        "intertextuality.yml",
        "scripts/handbook_structure.py",
        "scripts/intertextuality.py",
        "scripts/build_review_manuscripts.py",
        "scripts/review_links.py",
    ):
        source.require_path(ROOT / relative)
    result = {locale: build(locale, source) for locale in ("en", "sl")}
    source.verify()
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--record-source", metavar="COMMIT",
        help="Verify this full source commit ID and record its date and dependency digests",
    )
    arguments = parser.parse_args()
    source = (
        ReviewSource.from_commit(ROOT, arguments.record_source)
        if arguments.record_source else ReviewSource.load()
    )
    generated = manuscripts(source)
    if arguments.record_source:
        metadata_path = ROOT / "release" / "review-source.json"
        metadata_path.write_text(
            json.dumps(source.metadata(), indent=2, ensure_ascii=False, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        print(f"Recorded {metadata_path.relative_to(ROOT)} from {source.source_commit}")
    for locale, text in generated.items():
        target = ROOT / "release" / f"review-manuscript-{locale}.md"
        target.write_text(text, encoding="utf-8", newline="\n")
        print(f"Wrote {target.relative_to(ROOT)}")
