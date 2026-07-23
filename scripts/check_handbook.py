#!/usr/bin/env python3
"""Validate the bilingual stable core and course paths."""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

import yaml

from handbook_structure import CHAPTERS, COURSE_PATHS, ORIENTATION, PARTS, SECTION_LABELS

ROOT = Path(__file__).resolve().parents[1]
HEADINGS = {
    "en": ["## Learning outcomes", "## Before you begin", "## Practice", "## Reflection", "## Summary"],
    "sl": ["## Učni cilji", "## Pred začetkom", "## Vaja", "## Refleksija", "## Povzetek"],
}


class MkDocsLoader(yaml.SafeLoader):
    """Load trusted MkDocs YAML while treating Python-name tags as strings."""


MkDocsLoader.add_multi_constructor(
    "tag:yaml.org,2002:python/name:",
    lambda _loader, suffix, _node: suffix,
)


def page_title(path: Path) -> str:
    if not path.exists():
        raise ValueError(f"{path.relative_to(ROOT)}: missing page")
    match = re.search(r"(?m)^# (.+)$", path.read_text(encoding="utf-8"))
    if not match:
        raise ValueError(f"{path.relative_to(ROOT)}: missing page title")
    return match.group(1)


def localized_nav(config: dict, locale: str) -> list[dict]:
    if locale == "en":
        return config["nav"]
    for plugin in config["plugins"]:
        if not isinstance(plugin, dict) or "i18n" not in plugin:
            continue
        for language in plugin["i18n"]["languages"]:
            if language["locale"] == locale:
                return language["nav"]
    raise ValueError(f"mkdocs.yml: missing navigation for locale '{locale}'")


def named_group(nav: list[dict], label: str) -> list[dict]:
    matches = [entry[label] for entry in nav if isinstance(entry, dict) and label in entry]
    if len(matches) != 1:
        raise ValueError(f"navigation must contain exactly one '{label}' group")
    if not isinstance(matches[0], list):
        raise ValueError(f"navigation group '{label}' must contain nested pages")
    return matches[0]


def flatten_pages(entries: list[dict]) -> list[tuple[str, str]]:
    pages: list[tuple[str, str]] = []
    for entry in entries:
        label, value = next(iter(entry.items()))
        if isinstance(value, list):
            pages.extend(flatten_pages(value))
        else:
            pages.append((label, value))
    return pages


def check_navigation(config: dict, locale: str, failures: list[str]) -> None:
    labels = SECTION_LABELS[locale]
    expected_paths = ["chapters/index.md", *(f"chapters/{name}" for name in CHAPTERS)]
    try:
        handbook = named_group(localized_nav(config, locale), labels["handbook"])
    except (KeyError, TypeError, ValueError) as error:
        failures.append(f"mkdocs.yml ({locale}): {error}")
        return

    actual_groups = [next(iter(entry)) for entry in handbook]
    expected_groups = [labels["orientation"], *labels["parts"]]
    if actual_groups != expected_groups:
        failures.append(
            f"mkdocs.yml ({locale}): handbook groups are {actual_groups}; expected {expected_groups}"
        )

    expected_group_paths = [
        (labels["orientation"], ["chapters/index.md"]),
        *(
            (label, [f"chapters/{name}" for name in filenames])
            for label, filenames in zip(labels["parts"], PARTS, strict=True)
        ),
    ]
    for group_label, expected in expected_group_paths:
        matches = [
            entry[group_label]
            for entry in handbook
            if isinstance(entry, dict) and group_label in entry
        ]
        valid_group = len(matches) == 1 and isinstance(matches[0], list)
        actual: list[str] = []
        for match in matches:
            if isinstance(match, list):
                actual.extend(path for _, path in flatten_pages(match))
            elif isinstance(match, str):
                actual.append(match)
        if not valid_group or actual != expected:
            failures.append(
                f"mkdocs.yml ({locale}): navigation group '{group_label}' has "
                f"actual paths {actual}; expected paths {expected}"
            )

    pages = flatten_pages(handbook)
    actual_paths = [path for _, path in pages]
    counts = Counter(actual_paths)
    for path in expected_paths:
        if counts[path] == 0:
            failures.append(f"mkdocs.yml ({locale}): missing handbook page '{path}'")
        elif counts[path] > 1:
            failures.append(
                f"mkdocs.yml ({locale}): handbook page '{path}' appears {counts[path]} times"
            )
    unexpected = [path for path in actual_paths if path not in expected_paths]
    if unexpected:
        failures.append(f"mkdocs.yml ({locale}): unexpected handbook pages {unexpected}")
    if actual_paths != expected_paths:
        failures.append(
            f"mkdocs.yml ({locale}): handbook page order differs from the canonical 16-chapter order"
        )

    try:
        expected_titles = [
            page_title(ROOT / "docs" / locale / "chapters" / ORIENTATION),
            *(page_title(ROOT / "docs" / locale / "chapters" / name) for name in CHAPTERS),
        ]
    except ValueError as error:
        failures.append(str(error))
    else:
        actual_titles = [title for title, _ in pages]
        if actual_titles != expected_titles:
            failures.append(
                f"mkdocs.yml ({locale}): navigation labels do not match the established page titles"
            )


def check_manuscript(locale: str, failures: list[str]) -> None:
    path = ROOT / "release" / f"review-manuscript-{locale}.md"
    if not path.exists():
        failures.append(f"Missing review manuscript: {path.relative_to(ROOT)}")
        return
    text = path.read_text(encoding="utf-8")
    labels = SECTION_LABELS[locale]
    try:
        expected_markers: list[str] = [
            f"# {labels['orientation']}",
            f"## {page_title(ROOT / 'docs' / locale / 'chapters' / ORIENTATION)}",
        ]
        for heading, filenames in zip(labels["parts"], PARTS, strict=True):
            expected_markers.append(f"# {heading}")
            expected_markers.extend(
                f"## {page_title(ROOT / 'docs' / locale / 'chapters' / filename)}"
                for filename in filenames
            )
        expected_markers.append(f"# {labels['course_pathways']}")
        expected_markers.extend(
            f"## {page_title(ROOT / 'docs' / locale / 'learning-paths' / filename)}"
            for filename in COURSE_PATHS
        )
    except ValueError as error:
        failures.append(str(error))
        return

    position = -1
    for marker in expected_markers:
        matches = [match.start() for match in re.finditer(rf"(?m)^{re.escape(marker)}$", text)]
        if len(matches) != 1:
            failures.append(
                f"{path.relative_to(ROOT)}: expected one '{marker}' heading, found {len(matches)}"
            )
            continue
        if matches[0] <= position:
            failures.append(
                f"{path.relative_to(ROOT)}: '{marker}' is out of canonical publication order"
            )
        position = matches[0]


def main() -> int:
    failures: list[str] = []
    try:
        config = yaml.load(
            (ROOT / "mkdocs.yml").read_text(encoding="utf-8"),
            Loader=MkDocsLoader,
        )
    except (OSError, yaml.YAMLError) as error:
        print(f"Handbook core check failed:\n\n- Could not load mkdocs.yml: {error}")
        return 1
    for lang in ("en", "sl"):
        orientation = ROOT / "docs" / lang / "chapters" / ORIENTATION
        if not orientation.exists():
            failures.append(f"Missing orientation page: {orientation.relative_to(ROOT)}")
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
        for filename in COURSE_PATHS:
            path = ROOT / "docs" / lang / "learning-paths" / filename
            if not path.exists():
                failures.append(f"Missing course path: {path.relative_to(ROOT)}")
                continue
            text = path.read_text(encoding="utf-8")
            if "## Learning outcomes" not in text and "## Učni izidi" not in text:
                failures.append(f"{path.relative_to(ROOT)}: missing learning outcomes")
            modules = [int(number) for number in re.findall(r"(?m)^### (\d+)\. ", text)]
            if modules != list(range(1, 15)):
                failures.append(
                    f"{path.relative_to(ROOT)}: module sequence is {modules}; expected 1 through 14"
                )
        check_navigation(config, lang, failures)
        check_manuscript(lang, failures)
    if failures:
        print("Handbook core check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(
        "OK: bilingual stable core has "
        f"{len(CHAPTERS)} paired chapters in canonical navigation/manuscript order "
        f"and {len(COURSE_PATHS)} paired 14-module learning paths."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
