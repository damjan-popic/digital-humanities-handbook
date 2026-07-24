#!/usr/bin/env python3
"""Validate the canonical links among chapters, workflows, and case studies."""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

from handbook_structure import CHAPTERS
from intertextuality import (
    ECOSYSTEM_MARKER,
    ROOT,
    connections_for,
    inject_ecosystem,
    load_map,
    workflow_category,
)


def relative_files(directory: Path, prefix: str) -> set[str]:
    return {
        f"{prefix}/{path.relative_to(directory).as_posix()}"
        for path in directory.rglob("*.md")
        if path.name != "index.md"
    }


def duplicates(values: list[str]) -> list[str]:
    return sorted(value for value, count in Counter(values).items() if count > 1)


def check_targets(
    owner: str,
    relation: str,
    targets: list[str],
    expected_prefix: str,
    failures: list[str],
) -> None:
    repeated = duplicates(targets)
    if repeated:
        failures.append(f"{owner}: duplicate {relation} targets {repeated}")
    for target in targets:
        if target == owner:
            failures.append(f"{owner}: self-link in {relation}")
        if not target.startswith(expected_prefix):
            failures.append(
                f"{owner}: {relation} target '{target}' must start with '{expected_prefix}'"
            )
        if not (ROOT / "docs" / "en" / target).exists():
            failures.append(f"{owner}: missing {relation} target '{target}'")


def main() -> int:
    failures: list[str] = []
    data = load_map()

    expected_chapters = {f"chapters/{name}" for name in CHAPTERS}
    actual_chapters = set(data.get("chapters", {}))
    if actual_chapters != expected_chapters:
        failures.append(
            "intertextuality.yml: chapter keys differ from the stable core; "
            f"missing={sorted(expected_chapters - actual_chapters)}, "
            f"unexpected={sorted(actual_chapters - expected_chapters)}"
        )

    workflow_root = ROOT / "docs" / "en" / "workflows"
    case_root = ROOT / "docs" / "en" / "case-studies"
    workflow_paths = relative_files(workflow_root, "workflows")
    case_paths = relative_files(case_root, "case-studies")

    category_map = data.get("workflow_categories", {})
    used_categories: set[str] = set()
    for path in sorted(workflow_paths):
        try:
            category = workflow_category(path)
        except (OSError, ValueError) as error:
            failures.append(str(error))
            continue
        used_categories.add(category)
        if category not in category_map:
            failures.append(f"{path}: unmapped workflow category '{category}'")
            continue
        chapters = list(category_map[category].get("chapters", []))
        if not chapters:
            failures.append(f"workflow category '{category}' has no chapter connection")
        check_targets(path, "chapter", chapters, "chapters/", failures)
        resolved = connections_for(path, category)
        if not resolved.get("chapters"):
            failures.append(f"{path}: no rendered chapter connection")

    unused_categories = set(category_map) - used_categories
    if unused_categories:
        failures.append(
            f"intertextuality.yml: unused workflow categories {sorted(unused_categories)}"
        )

    workflow_overrides = data.get("workflows", {})
    unexpected_overrides = set(workflow_overrides) - workflow_paths
    if unexpected_overrides:
        failures.append(
            "intertextuality.yml: workflow overrides reference missing workflows "
            f"{sorted(unexpected_overrides)}"
        )
    for path, entry in workflow_overrides.items():
        chapters = list(entry.get("chapters", []))
        if not chapters:
            failures.append(f"{path}: workflow override has no chapter connection")
        check_targets(path, "chapter", chapters, "chapters/", failures)

    actual_cases = set(data.get("case_studies", {}))
    if actual_cases != case_paths:
        failures.append(
            "intertextuality.yml: case-study keys differ from the catalogue; "
            f"missing={sorted(case_paths - actual_cases)}, "
            f"unexpected={sorted(actual_cases - case_paths)}"
        )

    for chapter, entry in data.get("chapters", {}).items():
        workflows = list(entry.get("workflows", []))
        cases = list(entry.get("case_studies", []))
        if not workflows:
            failures.append(f"{chapter}: no featured workflow")
        if not cases:
            failures.append(f"{chapter}: no featured case study")
        check_targets(chapter, "workflow", workflows, "workflows/", failures)
        check_targets(chapter, "case study", cases, "case-studies/", failures)

    for case, entry in data.get("case_studies", {}).items():
        chapters = list(entry.get("chapters", []))
        workflows = list(entry.get("workflows", []))
        if not chapters:
            failures.append(f"{case}: no chapter connection")
        if not workflows:
            failures.append(f"{case}: no workflow connection")
        check_targets(case, "chapter", chapters, "chapters/", failures)
        check_targets(case, "workflow", workflows, "workflows/", failures)
        resolved = connections_for(case)
        if not resolved.get("chapters") or not resolved.get("workflows"):
            failures.append(f"{case}: incomplete rendered connections")

    for locale in ("en", "sl"):
        path = ROOT / "docs" / locale / "ecosystem.md"
        if not path.exists():
            failures.append(f"Missing ecosystem page: {path.relative_to(ROOT)}")
            continue
        source = path.read_text(encoding="utf-8")
        if source.count(ECOSYSTEM_MARKER) != 1:
            failures.append(
                f"{path.relative_to(ROOT)}: expected exactly one ecosystem-map marker"
            )
            continue
        try:
            rendered = inject_ecosystem(source, locale, link_mode="relative")
        except (OSError, ValueError) as error:
            failures.append(f"{path.relative_to(ROOT)}: {error}")
            continue
        if ECOSYSTEM_MARKER in rendered or rendered.count("| ") < len(CHAPTERS):
            failures.append(f"{path.relative_to(ROOT)}: ecosystem table did not render")

    if failures:
        print("Intertextuality check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "OK: connected "
        f"{len(expected_chapters)} chapters, {len(workflow_paths)} workflows, "
        f"and {len(case_paths)} case studies through one validated ecosystem map."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
