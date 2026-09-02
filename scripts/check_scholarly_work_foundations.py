#!/usr/bin/env python3
"""Validate the paired scholarly-work foundations route required by issue #20."""
from __future__ import annotations

import posixpath
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
HUB = "foundations/scholarly-work.md"
WORKFLOWS = {
    "workflows/reference-management/build-and-clean-a-zotero-library.md": "reference-management",
    "workflows/reference-management/cite-with-zotero-in-word-or-libreoffice.md": "reference-management",
    "workflows/reference-management/choose-apply-and-audit-a-citation-style.md": "reference-management",
    "workflows/scholarly-writing/turn-a-research-question-into-a-scientific-paper-plan.md": "scholarly-writing",
    "workflows/scholarly-writing/structure-a-long-document-with-styles-captions-and-cross-references.md": "scholarly-writing",
    "workflows/scholarly-writing/revise-claims-evidence-and-paragraphs.md": "scholarly-writing",
    "workflows/data-wrangling/import-and-clean-a-small-dataset-in-excel.md": "data-wrangling",
    "workflows/data-wrangling/make-repeatable-transformations-with-excel-power-query.md": "data-wrangling",
    "workflows/data-wrangling/summarize-data-with-pivottables-and-transparent-charts.md": "data-wrangling",
}
META = {
    "en": {
        "hub_title": "Scholarly work: writing, references, documents, and spreadsheets",
        "nav_group": "Foundations",
        "technical_title": "Technical workspace: terminal, WSL, Bash, Git, and Python",
        "category": {
            "reference-management": "Reference management",
            "scholarly-writing": "Scholarly writing",
            "data-wrangling": "Data wrangling",
        },
        "access_date": "2 September 2026",
        "low_threshold": "No WSL, Bash, Git or Python is required to pass",
    },
    "sl": {
        "hub_title": "Znanstveno delo: pisanje, viri, dokumenti in preglednice",
        "nav_group": "Osnove",
        "technical_title": "Tehnično delovno okolje: terminal, WSL, Bash, Git in Python",
        "category": {
            "reference-management": "Upravljanje virov",
            "scholarly-writing": "Znanstveno pisanje",
            "data-wrangling": "Urejanje podatkov",
        },
        "access_date": "2. septembra 2026",
        "low_threshold": "Za uspešen zaključek ne potrebujete WSL, lupine Bash, Gita ali Pythona",
    },
}
SAMPLE_ROOT = ROOT / "examples" / "scholarly-work-foundations"
SAMPLE_FILES = {
    "MANIFEST.sha256",
    "README.md",
    "RIGHTS.md",
    "source/identifier-exercise.md",
    "source/reading-notes.md",
    "source/zotero-five-records.ris",
    "raw/postcards-messy.csv",
    "raw/place-lookup.csv",
    "cleaned/postcards-clean.csv",
    "output/argument-plan.md",
    "output/source-to-claim.csv",
    "output/revised-paragraph.md",
    "output/structured-paper.docx",
    "output/structured-paper.odt",
    "output/scholarly-data-workbook.xlsx",
    "output/pivot-summary.csv",
    "output/chart-data.csv",
    "output/revision-log.md",
    "validation/manual-checks.md",
    "known-problems/patchwritten-paragraph.md",
    "known-problems/data-known-problems.md",
    "citation-style-audit/style-and-version.md",
    "citation-style-audit/five-test-records.md",
    "citation-style-audit/generated-bibliography.docx",
    "citation-style-audit/comparison-and-corrections.md",
    "citation-style-audit/unresolved-cases.md",
}
ZIP_PATH = ROOT / "docs" / "assets" / "downloads" / "scholarly-work-foundations-v1.zip"


class MkDocsLoader(yaml.SafeLoader):
    """Treat trusted MkDocs Python-name tags as inert strings."""


MkDocsLoader.add_multi_constructor(
    "tag:yaml.org,2002:python/name:",
    lambda _loader, suffix, _node: suffix,
)


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return {}
    raw = text[4 : text.index("\n---\n", 4)]
    return yaml.safe_load(raw) or {}


def markdown_links(text: str) -> list[str]:
    return re.findall(r"!?(?:\[[^\]]*\])\(([^)]+)\)", text)


def localized_nav(config: dict, locale: str) -> list[dict]:
    if locale == "en":
        return config["nav"]
    for plugin in config["plugins"]:
        if isinstance(plugin, dict) and "i18n" in plugin:
            for language in plugin["i18n"]["languages"]:
                if language["locale"] == locale:
                    return language["nav"]
    raise ValueError(f"mkdocs.yml: missing navigation for locale '{locale}'")


def check_hub(locale: str, failures: list[str]) -> None:
    path = ROOT / "docs" / locale / HUB
    if not path.exists():
        failures.append(f"Missing scholarly-work hub: {path.relative_to(ROOT)}")
        return
    text = path.read_text(encoding="utf-8")
    if f"# {META[locale]['hub_title']}" not in text:
        failures.append(f"{path.relative_to(ROOT)}: missing required displayed title")
    if META[locale]["low_threshold"] not in text:
        failures.append(f"{path.relative_to(ROOT)}: low-threshold course boundary is missing")

    resolved: set[str] = set()
    for raw_target in markdown_links(text):
        target = raw_target.strip().strip("<>")
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, flags=re.IGNORECASE):
            continue
        path_part = unquote(target.split("#", 1)[0])
        if not path_part:
            continue
        relative = posixpath.normpath(posixpath.join(posixpath.dirname(HUB), path_part))
        resolved.add(relative)
        target_path = ROOT / "docs" / locale / relative
        if not target_path.exists():
            failures.append(f"{path.relative_to(ROOT)}: missing linked page '{relative}'")
    missing = set(WORKFLOWS) - resolved
    if missing:
        failures.append(f"{path.relative_to(ROOT)}: missing route links {sorted(missing)}")


def check_navigation(locale: str, config: dict, failures: list[str]) -> None:
    label = META[locale]["nav_group"]
    matches = [entry[label] for entry in localized_nav(config, locale) if isinstance(entry, dict) and label in entry]
    expected = [
        {META[locale]["technical_title"]: "foundations/technical-workspace.md"},
        {META[locale]["hub_title"]: HUB},
    ]
    if matches != [expected]:
        failures.append(f"mkdocs.yml ({locale}): '{label}' group is {matches!r}; expected {[expected]!r}")


def check_course(locale: str, failures: list[str]) -> None:
    path = ROOT / "docs" / locale / "learning-paths/pismenost-za-informacijsko-druzbo.md"
    text = path.read_text(encoding="utf-8")
    modules = [int(number) for number in re.findall(r"(?m)^### (\d+)\. ", text)]
    if modules != list(range(1, 15)):
        failures.append(f"{path.relative_to(ROOT)}: module sequence is {modules}; expected 1 through 14")
    for workflow in WORKFLOWS:
        target = f"../{workflow}"
        if target not in text:
            failures.append(f"{path.relative_to(ROOT)}: missing course workflow link {target!r}")
    for token in (
        "../foundations/scholarly-work.md",
        "../foundations/technical-workspace.md",
        "citation-style-audit",
        "pet" if locale == "sl" else "five",
        "ZIP",
        META[locale]["low_threshold"],
    ):
        if token not in text:
            failures.append(f"{path.relative_to(ROOT)}: missing route requirement {token!r}")

    overview = ROOT / "docs" / locale / "learning-paths/index.md"
    if "../foundations/scholarly-work.md" not in overview.read_text(encoding="utf-8"):
        failures.append(f"{overview.relative_to(ROOT)}: missing prominent scholarly-work hub link")


def check_samples(failures: list[str]) -> None:
    actual = {
        path.relative_to(SAMPLE_ROOT).as_posix()
        for path in SAMPLE_ROOT.rglob("*")
        if path.is_file()
    } if SAMPLE_ROOT.exists() else set()
    missing = SAMPLE_FILES - actual
    if missing:
        failures.append(f"Sample package is missing {sorted(missing)}")
    if not ZIP_PATH.exists():
        failures.append(f"Missing stable sample ZIP: {ZIP_PATH.relative_to(ROOT)}")
        return
    with zipfile.ZipFile(ZIP_PATH) as archive:
        members = {name.removeprefix("scholarly-work-foundations/") for name in archive.namelist() if not name.endswith("/")}
    zip_missing = SAMPLE_FILES - members
    if zip_missing:
        failures.append(f"Stable sample ZIP is missing {sorted(zip_missing)}")


def main() -> int:
    failures: list[str] = []
    config = yaml.load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"), Loader=MkDocsLoader)
    ecosystem = yaml.safe_load((ROOT / "intertextuality.yml").read_text(encoding="utf-8"))

    for locale in ("en", "sl"):
        check_hub(locale, failures)
        check_navigation(locale, config, failures)
        check_course(locale, failures)
        for relative_path, category_id in WORKFLOWS.items():
            path = ROOT / "docs" / locale / relative_path
            if not path.exists():
                failures.append(f"Missing paired scholarly workflow: {path.relative_to(ROOT)}")
                continue
            metadata = front_matter(path)
            if metadata.get("category_id") != category_id:
                failures.append(f"{path.relative_to(ROOT)}: category_id must be {category_id!r}")
            expected_category = META[locale]["category"][category_id]
            if metadata.get("category") != expected_category:
                failures.append(f"{path.relative_to(ROOT)}: category is {metadata.get('category')!r}; expected {expected_category!r}")
            text = path.read_text(encoding="utf-8")
            if META[locale]["access_date"] not in text:
                failures.append(f"{path.relative_to(ROOT)}: missing source access date")
            if "![" in text:
                failures.append(f"{path.relative_to(ROOT)}: screenshots/images require an explicit rights review")

    category_map = ecosystem.get("workflow_categories", {})
    for category_id in set(WORKFLOWS.values()):
        if not category_map.get(category_id, {}).get("chapters"):
            failures.append(f"intertextuality.yml: category {category_id!r} lacks a chapter mapping")
    overrides = ecosystem.get("workflows", {})
    for workflow in WORKFLOWS:
        if not overrides.get(workflow, {}).get("chapters"):
            failures.append(f"intertextuality.yml: workflow {workflow!r} lacks a curated mapping")

    template_en = (ROOT / "docs/en/contribute/student-workflow-template.md").read_text(encoding="utf-8")
    template_sl = (ROOT / "docs/sl/contribute/student-workflow-template.md").read_text(encoding="utf-8")
    if "Assessment and publication are separate" not in template_en or "Ocenjevanje in objava sta ločena postopka" not in template_sl:
        failures.append("Student contribution templates no longer separate assessment from publication")

    check_samples(failures)
    if failures:
        print("Scholarly-work foundations check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(
        "OK: paired scholarly-work route has 2 hubs, 9 paired workflows, localized stable categories, "
        "two aligned 14-module low-threshold paths, curated ecosystem mappings, and a complete stable sample ZIP."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
