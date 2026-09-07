#!/usr/bin/env python3
"""Check paired Part IV chapters and the documentary contracts in five workflows.

These checks validate completeness and structural parity, not ethical approval,
source interpretation, legal permission, or a claim that a model run took place.
"""
from __future__ import annotations

import csv
import re
import sys
from datetime import date
from pathlib import Path

import yaml

from intertextuality import connections_for, load_map

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ("ai-ethics-reproducibility.md", "open-living-handbook.md")
RECORDS = {
    "ai/document-and-audit-a-source-grounded-ai-analysis.md": (
        "ai-analysis-audit",
        "research_question provider model_identifier model_version_or_snapshot "
        "run_time_utc interface system_instructions user_instructions parameters "
        "retrieval_configuration source_documents passage_ids preprocessing truncation "
        "output_path correction_log validation_sample validation_protocol environment "
        "cost nondeterminism unavailable_details disclosure review_status reviewer "
        "review_date review_scope",
    ),
    "ai/compare-ai-output-across-prompts-models-and-runs.md": (
        "ai-robustness-plan",
        "research_question source_documents passage_ids baseline conditions planned_runs "
        "actual_runs run_records consequential_difference_taxonomy validation_strata "
        "validation_sample adjudication acceptance_rule stop_rule budget results_status "
        "review_status reviewer review_date review_scope",
    ),
    "publishing/create-a-versioned-scholarly-release.md": (
        "scholarly-release-plan",
        "project candidate_version source_commit manifest changelog citation_metadata "
        "identifiers artefacts archive build_environment approval",
    ),
    "publishing/correct-a-published-digital-resource-without-erasing-history.md": (
        "publication-correction",
        "correction_id affected_release affected_objects evidence category claim_before "
        "claim_after release_classification source_change changelog erratum release_notes "
        "prior_version_access supersession later_citation review privacy_action",
    ),
    "publishing/prepare-a-maintenance-and-succession-plan.md": (
        "maintenance-succession-plan",
        "project owner editor technical_maintainer successor dependencies services "
        "backups restore_test review_cadence transfer_procedure exit_plan",
    ),
}
NESTED_FIELDS = {
    "scholarly-release-plan": {
        "manifest[]": "path title language content_type review_status review_scope "
        "translation_status licence source_sha256 inclusion_status external_dependencies accessibility",
        "identifiers": "doi isbn assignment_authority status",
        "artefacts[]": "path sha256",
        "archive": "repository deposit_status verification",
    },
    "publication-correction": {
        "release_classification": "level target_version rationale",
    },
    "maintenance-succession-plan": {
        "dependencies[]": "name version_record review_trigger",
        "services[]": "name owner_role credential_reference renewal",
        "backups": "scope locations retention",
    },
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def frontmatter(text: str) -> dict:
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.S)
    require(match is not None, "missing YAML frontmatter")
    result = yaml.safe_load(match.group(1))
    require(isinstance(result, dict), "frontmatter must be a mapping")
    return result


def word_count(text: str) -> int:
    """Visible prose, headings and tables, excluding metadata/code/references/notes."""
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.split(r"(?m)^## (?:Further reading|References|Nadaljnje branje|Literatura)\s*$", text)[0]
    text = re.sub(r"(?m)^\[\^[^]]+\]:.*(?:\n(?:[ \t]+.*|\s*$))*", "", text)
    text = re.sub(r"\[\^[^]]+\]", "", text)
    text = re.sub(r"(?ms)^```.*?^```\s*$", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^\n)]+\)", r"\1", text)
    return len(re.findall(r"[^\W_]+(?:[’'-][^\W_]+)*", text, re.UNICODE))


def record_from_markdown(text: str, record_type: str) -> dict:
    matches = []
    for block in re.findall(r"(?ms)^```yaml\s*\n(.*?)^```\s*$", text):
        value = yaml.safe_load(block)
        if isinstance(value, dict) and value.get("record_type") == record_type:
            matches.append(value)
    require(len(matches) == 1, f"expected one {record_type!r} YAML record, found {len(matches)}")
    return matches[0]


def mapping_fields(value: object, required: str, context: str) -> None:
    require(isinstance(value, dict), f"{context}: expected a mapping")
    missing = set(required.split()) - value.keys()
    require(not missing, f"{context}: missing documentation fields {sorted(missing)}")


def validate_record(record: dict, record_type: str, required: str) -> None:
    mapping_fields(record, f"record_type record_status {required}", record_type)
    require(record["record_type"] == record_type, "incorrect record_type")
    require(record["record_status"] == "template", f"{record_type}: teaching template must identify itself")
    if record_type in {"ai-analysis-audit", "ai-robustness-plan"}:
        require(record["review_status"] in {"pending_human_review", "human-reviewed"},
                f"{record_type}: unknown human-review status")
        require(isinstance(record["source_documents"], list) and bool(record["source_documents"]),
                f"{record_type}: source_documents must list preserved source files")
        for relative in record["source_documents"]:
            path = (ROOT / relative).resolve()
            require(path.is_relative_to(ROOT) and path.is_file(), f"{record_type}: missing source file {relative}")
        with (ROOT / "teaching-data/text-nlp-validation/raw/annotation-samples.csv").open(encoding="utf-8", newline="") as handle:
            sample_ids = {row["sample_id"] for row in csv.DictReader(handle)}
        require(isinstance(record["passage_ids"], list) and bool(record["passage_ids"]),
                f"{record_type}: passage_ids must identify the teaching passages")
        require(set(record["passage_ids"]) <= sample_ids,
                f"{record_type}: passage ID does not resolve to the preserved sample")
    for field, fields in NESTED_FIELDS.get(record_type, {}).items():
        if field.endswith("[]"):
            items = record[field[:-2]]
            require(isinstance(items, list) and bool(items), f"{record_type}.{field}: include a record to fill")
            for index, item in enumerate(items):
                mapping_fields(item, fields, f"{record_type}.{field}[{index}]")
        else:
            mapping_fields(record[field], fields, f"{record_type}.{field}")
    if record_type == "scholarly-release-plan":
        identifiers = record["identifiers"]
        require(identifiers["doi"] is None and identifiers["isbn"] is None,
                "release teaching template must leave unassigned DOI/ISBN null")
        require(bool(identifiers["assignment_authority"]) and bool(identifiers["status"]),
                "release identifier responsibility and pending state must be explicit")
        for item in record["manifest"]:
            require(isinstance(item["external_dependencies"], list),
                    "manifest external_dependencies must be a list, including when empty")
    if record.get("review_status") == "human-reviewed":
        for key in ("reviewer", "review_scope"):
            require(bool(record[key]), f"{record_type}: human-reviewed state requires {key}")
        date.fromisoformat(str(record["review_date"]))


def structure(value: object) -> object:
    """Compare machine keys, collection topology and scalar types, not translation."""
    if isinstance(value, dict):
        return {key: structure(item) for key, item in sorted(value.items())}
    if isinstance(value, list):
        return [structure(item) for item in value]
    return type(value).__name__


def validate_translation(meta: dict, text: str) -> None:
    status = meta.get("translation_status")
    if status == "human-reviewed":
        for field in ("translation_reviewed_by", "translation_reviewed_on", "translation_review_scope"):
            require(bool(meta.get(field)), f"human-reviewed translation requires {field}")
        date.fromisoformat(str(meta["translation_reviewed_on"]))
    else:
        require(status == "machine-assisted draft; requires human language review",
                "translation must declare its review state")
        require("strojno" in text.lower(), "machine-assisted translation needs a visible review notice")


def main() -> int:
    failures = []
    counts = {}
    paired_records = {}
    paired_sources = {}
    ecosystem = load_map()
    for locale in ("en", "sl"):
        for filename in CHAPTERS:
            relative = f"docs/{locale}/chapters/{filename}"
            try:
                text = (ROOT / relative).read_text(encoding="utf-8")
                meta = frontmatter(text)
                if locale == "sl":
                    validate_translation(meta, text)
                count = word_count(text)
                counts[f"{locale}/{filename}"] = count
                require(2300 <= count <= 3500, f"{count} words; expected formal-review depth near 2300–3300")
                reading_heading = "## Further reading" if locale == "en" else "## Nadaljnje branje"
                require(reading_heading in text, "missing compact further reading section")
                paired_sources[(locale, filename)] = set(re.findall(r"\]\((https?://[^\s)]+)\)", text))
                definitions = re.findall(r"(?m)^\[\^([^]]+)\]:", text)
                require(len(definitions) == len(set(definitions)), "duplicate footnote definition")
                other_definitions = set()
                for other in (ROOT / "docs" / locale / "chapters").glob("*.md"):
                    if other.name != filename:
                        other_definitions.update(re.findall(r"(?m)^\[\^([^]]+)\]:", other.read_text(encoding="utf-8")))
                require(not set(definitions) & other_definitions,
                        "footnote IDs collide with another chapter in the combined manuscript")
            except (OSError, ValueError, yaml.YAMLError) as error:
                failures.append(f"{relative}: {error}")
        for path, (record_type, fields) in RECORDS.items():
            relative = f"docs/{locale}/workflows/{path}"
            try:
                text = (ROOT / relative).read_text(encoding="utf-8")
                meta = frontmatter(text)
                expected_category = "AI" if path.startswith("ai/") else "Publishing & FAIR data"
                require(meta.get("category_id") == expected_category, "missing stable category_id")
                if locale == "sl":
                    validate_translation(meta, text)
                record = record_from_markdown(text, record_type)
                validate_record(record, record_type, fields)
                paired_records[(locale, path)] = record
                chapter = "chapters/" + CHAPTERS[0 if path.startswith("ai/") else 1]
                require(f"workflows/{path}" in ecosystem["chapters"][chapter]["workflows"],
                        f"not selected in {chapter}'s ecosystem trail")
                require(chapter in connections_for(f"workflows/{path}")["chapters"],
                        f"missing reciprocal connection to {chapter}")
            except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as error:
                failures.append(f"{relative}: {error}")
    for path in RECORDS:
        if all((locale, path) in paired_records for locale in ("en", "sl")):
            if structure(paired_records[("en", path)]) != structure(paired_records[("sl", path)]):
                failures.append(f"{path}: English/Slovene documentary record schemas differ")
    for filename in CHAPTERS:
        if all((locale, filename) in paired_sources for locale in ("en", "sl")):
            if paired_sources[("en", filename)] != paired_sources[("sl", filename)]:
                failures.append(f"{filename}: English/Slovene external references differ")
    print("Part IV chapter words (references, footnotes, metadata and fenced code excluded):")
    for path, count in counts.items():
        print(f"  {path}: {count}")
    if failures:
        print("Part IV validation failed:\n" + "\n".join(f"- {item}" for item in failures))
        return 1
    print("OK: 2 paired Part IV chapters, 5 paired workflows, documentary fields, conditional identifiers, translation states and reciprocal ecosystem links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
