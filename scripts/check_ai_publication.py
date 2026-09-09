#!/usr/bin/env python3
"""Check paired Part IV chapters and the documentary contracts in five workflows.

These checks validate completeness and structural parity, not ethical approval,
source interpretation, legal permission, or a claim that a model run took place.
"""
from __future__ import annotations

import csv
import re
import sys
import unicodedata
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

import yaml
from markdown import markdown

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
        "research_question source_documents passage_ids baseline prompt_registry model_registry "
        "conditions repetitions_per_condition planned_runs "
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

# Explicit operational values, not translated explanations. '*' visits every
# list item (in order) or mapping entry. Unknown/missing paths fail closed.
INVARIANT_PATHS = {
    "ai-analysis-audit": (
        "provider model_identifier model_version_or_snapshot run_time_utc interface "
        "system_instructions user_instructions parameters retrieval_configuration "
        "source_documents passage_ids truncation output_path correction_log "
        "validation_sample environment cost nondeterminism unavailable_details "
        "review_status reviewer review_date"
    ),
    "ai-robustness-plan": (
        "source_documents passage_ids prompt_registry model_registry conditions "
        "repetitions_per_condition planned_runs actual_runs run_records "
        "consequential_difference_taxonomy validation_strata validation_sample budget "
        "results_status review_status reviewer review_date"
    ),
    "scholarly-release-plan": (
        "candidate_version source_commit manifest.*.path manifest.*.language "
        "manifest.*.content_type manifest.*.review_status manifest.*.licence "
        "manifest.*.source_sha256 manifest.*.inclusion_status "
        "manifest.*.external_dependencies identifiers.doi identifiers.isbn "
        "identifiers.status artefacts.*.path artefacts.*.sha256 archive.deposit_status"
    ),
    "publication-correction": (
        "correction_id affected_release affected_objects category "
        "release_classification.level release_classification.target_version"
    ),
    "maintenance-succession-plan": "services.*.owner_role",
}
STATUS_CODES = {
    "not_run", "unknown", "redacted", "pending", "template", "not_selected",
    "pending_human_review", "pending-human-review", "human-reviewed",
    "pending-agreement", "not-deposited", "proposed-reviewed-edition",
}
REVIEW_PLACEHOLDERS = {
    "pending", "unknown", "not run", "redacted", "tbd", "todo", "null", "none",
    "nil", "n a", "na", "nan", "not applicable", "unavailable", "withheld",
    "undetermined", "unassigned", "not reviewed", "not selected", "placeholder",
    "to be determined", "to be reviewed", "to be assigned", "fill in",
    "v čakanju", "na čakanju", "čaka", "čakajo", "čakajoč", "čakajoča", "čakajoče",
    "v teku", "neznano", "neznan", "neznana", "ni znano", "ni podatka",
    "ni podatkov", "ni določeno", "ni navedeno", "ni izvedeno", "ni pregledano",
    "neizvedeno", "neizveden", "neizvedena", "zakrito", "zakrit", "zakrita",
    "zaupno", "anonimno", "brez pregleda", "za pregled", "nedoločeno",
    "neopredeljeno", "manjkajoče", "izpolnite", "dopolnite", "ni relevantno", "se ne uporablja",
    "ni na voljo", "ne velja", "čakanje", "v pripravi", "zadržano",
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


def validate_chapter_length(count: int) -> None:
    require(count >= 2300, f"{count} words; scholarly-completeness minimum is 2300")


class AnswerMetaParser(HTMLParser):
    """Read the standard visible card, not a fenced or commented example."""

    def __init__(self) -> None:
        super().__init__()
        self.cards: list[list[str]] = []
        self.current: list[str] | None = None
        self.span: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "div" and "answer-meta" in (attributes.get("class") or "").split():
            require(self.current is None, "answer-meta: nested card")
            require("markdown" in attributes, "answer-meta: missing markdown attribute")
            self.current = []
        elif self.current is not None:
            require(tag == "span" and self.span is None, "answer-meta: expected plain spans")
            self.span = []

    def handle_data(self, data: str) -> None:
        if self.span is not None:
            self.span.append(data)
        elif self.current is not None:
            require(not data.strip(), "answer-meta: values must be inside spans")

    def handle_endtag(self, tag: str) -> None:
        if self.current is None:
            return
        if tag == "span":
            require(self.span is not None, "answer-meta: unbalanced span")
            self.current.append(" ".join("".join(self.span).split()))
            self.span = None
        else:
            require(tag == "div" and self.span is None, "answer-meta: unbalanced card")
            self.cards.append(self.current)
            self.current = None


def validate_answer_meta(text: str, meta: dict, locale: str) -> None:
    parser = AnswerMetaParser()
    # Let the handbook's Markdown parser distinguish real HTML from inline,
    # indented and fenced code. Without md_in_html the source's required
    # 'markdown' attribute remains inspectable on the raw card element.
    parser.feed(markdown(text, extensions=["fenced_code"]))
    require(parser.current is None and len(parser.cards) == 1,
            "answer-meta: require exactly one complete metadata card")
    expected = [meta.get(field) for field in ("category", "difficulty", "time")]
    require(all(isinstance(value, str) and value.strip() for value in expected),
            "answer-meta: category, difficulty and time must be nonempty")
    require(parser.cards[0] == expected,
            "answer-meta: three category/difficulty/time values must match localized metadata")
    categories = {"en": {"AI", "Publishing & FAIR data"},
                  "sl": {"UI", "Objavljanje in podatki FAIR"}}
    difficulties = {"en": {"beginner", "intermediate", "advanced"},
                    "sl": {"začetno", "srednje zahtevno", "zahtevno"}}
    require(meta["category"] in categories[locale] and meta["difficulty"] in difficulties[locale],
            "answer-meta: category and difficulty must be localized")


def is_review_placeholder(value: object) -> bool:
    if not isinstance(value, str) or not value.strip():
        return True
    normalized = unicodedata.normalize("NFKC", value).casefold()
    normalized = " ".join(re.sub(r"[^\w]+|_", " ", normalized).split())
    if not normalized:
        return True
    # Reject padded/composed sentinels, not only a truthy exact 'pending'.
    # 'na' is also a common Slovene preposition (and can occur in a name).
    # Null-like NA/N/A is a sentinel only when it is the whole field.
    exact_only = {"na", "n a"}
    return normalized in exact_only or any(
        f" {sentinel} " in f" {normalized} " for sentinel in REVIEW_PLACEHOLDERS - exact_only
    )


def validate_review_metadata(reviewer: object, review_date: object,
                            review_scope: object, context: str) -> None:
    require(not is_review_placeholder(reviewer), f"{context}: reviewer must not be a placeholder")
    name_words = re.findall(r"[^\W\d_]+", reviewer)
    role_words = {
        "name", "named", "first", "last", "reviewer", "human", "subject", "matter",
        "language", "scholarly", "competent", "assigned", "confirmed", "review",
        "ime", "priimek", "in", "pregledovalec", "strokovni", "jezikovni", "človeški",
        "usposobljeni", "recenzent", "imenovani", "potrjen", "dr", "prof", "mr", "ms",
    }
    require(len(name_words) >= 2 and not all(word.casefold() in role_words for word in name_words),
            f"{context}: require a named reviewer, not an unnamed role")
    date_text = str(review_date)
    require(re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_text) is not None,
            f"{context}: review_date must be a valid ISO date (YYYY-MM-DD)")
    try:
        date.fromisoformat(date_text)
    except ValueError as error:
        raise ValueError(f"{context}: review_date must be a valid ISO date") from error
    require(not is_review_placeholder(review_scope), f"{context}: review_scope must not be a placeholder")
    require(len(review_scope.strip()) >= 20 and len(re.findall(r"[^\W_]+", review_scope)) >= 4,
            f"{context}: review_scope must describe a substantive review scope")
    # These structural checks do not authenticate an identity or prove review.


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


def teaching_sample_ids() -> set[str]:
    with (ROOT / "teaching-data/text-nlp-validation/raw/annotation-samples.csv").open(encoding="utf-8", newline="") as handle:
        return {row["sample_id"] for row in csv.DictReader(handle)}


def validate_robustness_plan(record: dict) -> None:
    context = "ai-robustness-plan"
    mapping_fields(record, "prompt_registry model_registry passage_ids conditions "
                   "repetitions_per_condition planned_runs actual_runs run_records "
                   "validation_strata validation_sample budget results_status", context)
    passages = record["passage_ids"]
    require(isinstance(passages, list) and bool(passages)
            and all(isinstance(item, str) for item in passages), "passage_ids must be a nonempty ID list")
    require(len(set(passages)) == len(passages) and set(passages) <= teaching_sample_ids(),
            "passage_ids must be unique and resolve to preserved passages")
    prompts, models = record["prompt_registry"], record["model_registry"]
    require(isinstance(prompts, dict) and set(prompts) == {"P0", "P1"},
            "prompt_registry must define P0 and P1")
    require(all(isinstance(text, str) and text.strip() for text in prompts.values()),
            "prompt_registry must preserve exact nonempty instructions")
    require(prompts["P0"] != prompts["P1"], "P0 and P1 must contain different instructions")
    require(isinstance(models, dict) and set(models) == {"M1", "M2"},
            "model_registry must define M1 and M2")
    for model_id, model in models.items():
        mapping_fields(model, "model_identifier model_version_or_snapshot status", f"model_registry.{model_id}")
        require(model["status"] == "not_selected"
                and model["model_identifier"] is None and model["model_version_or_snapshot"] is None,
                f"model_registry.{model_id}: this unperformed teaching plan must keep selection explicitly pending")
    conditions = record["conditions"]
    require(isinstance(conditions, list) and bool(conditions), "conditions must be a nonempty list")
    factors = ("prompt", "model", "passage_order")
    ids = []
    for condition in conditions:
        required = {"condition_id", "changed_factor", *factors}
        require(isinstance(condition, dict) and set(condition) == required,
                "condition fields must declare IDs, prompt, model, passage_order and changed_factor only")
        condition_id = condition["condition_id"]
        require(isinstance(condition_id, str), "condition_id must be a string")
        ids.append(condition_id)
        require(isinstance(condition["prompt"], str) and condition["prompt"] in prompts,
                f"{condition_id}: prompt ID does not resolve")
        require(isinstance(condition["model"], str) and condition["model"] in models,
                f"{condition_id}: model ID does not resolve")
        order = condition["passage_order"]
        require(isinstance(order, list) and all(isinstance(item, str) for item in order)
                and len(order) == len(passages) and set(order) == set(passages),
                f"{condition_id}: passage_order must contain each declared passage exactly once")
    require(len(set(ids)) == len(ids), "condition IDs must be unique")
    require(ids == ["C0", "C1", "C2", "C3"], "conditions must preserve C0–C3 in declared order")
    baseline = conditions[0]
    require(baseline["changed_factor"] is None, "C0 changed_factor must be null")
    require(baseline["prompt"] == "P0" and baseline["model"] == "M1"
            and baseline["passage_order"] == passages, "C0 must use P0, M1 and the declared passage order")
    for condition, factor in zip(conditions[1:], ("prompt", "passage_order", "model"), strict=True):
        changed = [key for key in factors if condition[key] != baseline[key]]
        require(condition["changed_factor"] == factor and changed == [factor],
                f"{condition['condition_id']}: must differ from C0 only in its declared changed_factor ({factor})")
    require(conditions[2]["passage_order"] == list(reversed(passages)), "C2 must reverse the baseline passage order")
    repetitions, planned, actual = (record[key] for key in
                                    ("repetitions_per_condition", "planned_runs", "actual_runs"))
    require(type(repetitions) is int and repetitions == 2, "repetitions_per_condition must be 2")
    require(type(planned) is int and planned == len(conditions) * repetitions,
            "planned_runs must equal number_of_conditions × repetitions_per_condition")
    require(isinstance(record["run_records"], list), "run_records must be a list")
    require(type(actual) is int and actual == len(record["run_records"]),
            "actual_runs must equal len(run_records)")
    require(actual == 0, "teaching template must retain actual_runs: 0; no model experiment is reported")
    require(record["results_status"] == "not_run", "results_status must remain not_run for the unperformed teaching plan")
    mapping_fields(record["budget"], "maximum_model_calls maximum_paid_cost_eur maximum_review_minutes", "budget")
    maximum = record["budget"]["maximum_model_calls"]
    require(type(maximum) is int and maximum >= planned, "budget maximum_model_calls must permit planned_runs")
    for field in ("maximum_paid_cost_eur", "maximum_review_minutes"):
        value = record["budget"][field]
        require(type(value) in {int, float} and value >= 0, f"budget {field} must be nonnegative")
    strata = record["validation_strata"]
    require(isinstance(strata, list) and bool(strata), "validation_strata must be a nonempty list")
    groups = [record["validation_sample"]]
    for stratum in strata:
        mapping_fields(stratum, "stratum passage_ids", "validation_strata")
        groups.append(stratum["passage_ids"])
    for group in groups:
        require(isinstance(group, list) and bool(group) and all(isinstance(item, str) for item in group)
                and set(group) <= set(passages), "validation passage IDs must resolve to declared passages")


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
        sample_ids = teaching_sample_ids()
        require(isinstance(record["passage_ids"], list) and bool(record["passage_ids"]),
                f"{record_type}: passage_ids must identify the teaching passages")
        require(set(record["passage_ids"]) <= sample_ids,
                f"{record_type}: passage ID does not resolve to the preserved sample")
        if record["review_status"] == "pending_human_review":
            require(all(record[field] is None for field in ("reviewer", "review_date", "review_scope")),
                    f"{record_type}: unfinished reviewer, review_date and review_scope must be null")
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
        validate_review_metadata(record["reviewer"], record["review_date"], record["review_scope"], record_type)
    if record_type == "ai-robustness-plan":
        validate_robustness_plan(record)


def structure(value: object) -> object:
    """Compare machine keys, collection topology and scalar types, not translation."""
    if isinstance(value, dict):
        return {key: structure(item) for key, item in sorted(value.items())}
    if isinstance(value, list):
        return [structure(item) for item in value]
    return type(value).__name__


def values_at_path(value: object, path: str) -> dict[str, object]:
    found = {}

    def visit(item: object, parts: list[str], prefix: str) -> None:
        if not parts:
            found[prefix] = item
        elif parts[0] == "*":
            require(isinstance(item, (dict, list)), f"invariant path {path}: expected collection")
            entries = enumerate(item) if isinstance(item, list) else sorted(item.items())
            for key, child in entries:
                visit(child, parts[1:], f"{prefix}.{key}".lstrip("."))
        else:
            require(isinstance(item, dict) and parts[0] in item, f"missing invariant path {path}")
            visit(item[parts[0]], parts[1:], f"{prefix}.{parts[0]}".lstrip("."))

    visit(value, path.split("."), "")
    return found


def record_leaves(value: object, prefix: str = "") -> dict[str, object]:
    if isinstance(value, dict):
        entries = value.items()
    elif isinstance(value, list):
        entries = enumerate(value)
    else:
        return {prefix: value}
    result = {}
    for key, item in entries:
        result.update(record_leaves(item, f"{prefix}.{key}".lstrip(".")))
    return result


def validate_bilingual_invariants(english: dict, slovene: dict, record_type: str) -> None:
    require(structure(english) == structure(slovene), f"{record_type}: bilingual schemas differ")
    for path in ("record_type record_status " + INVARIANT_PATHS[record_type]).split():
        require(values_at_path(english, path) == values_at_path(slovene, path),
                f"{record_type}: bilingual invariant differs at {path}")
    en_leaves, sl_leaves = record_leaves(english), record_leaves(slovene)
    for path, value in en_leaves.items():
        translated = sl_leaves[path]
        if value is None or type(value) in {bool, int, float} or (
            isinstance(value, str) and (value in STATUS_CODES or translated in STATUS_CODES)
        ):
            require(value == translated, f"{record_type}: bilingual scalar/status invariant differs at {path}")
        elif isinstance(value, str):
            # A prose explanation may be translated, but embedded quantities,
            # versions and conventional record IDs must not silently change.
            tokens = r"(?<!\w)\d+(?:[.-]\d+)*(?!\w)|\b[A-Z][A-Z0-9]*(?:[-_][A-Z0-9]+)+\b"
            require(re.findall(tokens, value) == re.findall(tokens, translated),
                    f"{record_type}: bilingual numeric/ID invariant differs at {path}")


def validate_translation(meta: dict, text: str) -> None:
    status = meta.get("translation_status")
    if status == "human-reviewed":
        validate_review_metadata(meta.get("translation_reviewed_by"), meta.get("translation_reviewed_on"),
                                 meta.get("translation_review_scope"), "human-reviewed translation")
    else:
        require(status == "machine-assisted draft; requires human language review",
                "translation must declare its review state")
        require("strojno" in text.lower(), "machine-assisted translation needs a visible review notice")
        require(all(meta.get(field) is None for field in
                    ("translation_reviewed_by", "translation_reviewed_on", "translation_review_scope")),
                "unfinished translation-review metadata must be absent or null")


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
                validate_chapter_length(count)
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
                validate_answer_meta(text, meta, locale)
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
            else:
                try:
                    validate_bilingual_invariants(paired_records[("en", path)], paired_records[("sl", path)], RECORDS[path][0])
                except ValueError as error:
                    failures.append(f"{path}: {error}")
    for filename in CHAPTERS:
        if all((locale, filename) in paired_sources for locale in ("en", "sl")):
            if paired_sources[("en", filename)] != paired_sources[("sl", filename)]:
                failures.append(f"{filename}: English/Slovene external references differ")
    print("Part IV chapter words (minimum 2300; no hard maximum; editorial guidance 2300–3300; references, footnotes, metadata and fenced code excluded):")
    for path, count in counts.items():
        print(f"  {path}: {count}")
    if failures:
        print("Part IV validation failed:\n" + "\n".join(f"- {item}" for item in failures))
        return 1
    print("OK: 2 paired Part IV chapters, 5 paired workflows, 10 localized answer-meta cards, documentary fields, bilingual invariant values, placeholder-free review states, conditional identifiers and reciprocal ecosystem links.")
    print("OK: EN/SL robustness plans: 4 unique conditions × 2 repetitions = 8 planned calls; 0 actual runs = 0 run records; prompt/model/passage IDs resolve; C1–C3 change only the declared factor; 8-call budget permits the plan.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
