#!/usr/bin/env python3
"""Regression checks for consequential omissions in the teaching records."""
from __future__ import annotations

import copy
import re
import unittest
from markdown import markdown

from check_ai_publication import (
    RECORDS,
    ROOT,
    frontmatter,
    record_from_markdown,
    structure,
    validate_answer_meta,
    validate_bilingual_invariants,
    validate_chapter_length,
    validate_record,
    validate_review_metadata,
    validate_robustness_plan,
    validate_translation,
)


AUDIT_PATH = "ai/document-and-audit-a-source-grounded-ai-analysis.md"
ROBUSTNESS_PATH = "ai/compare-ai-output-across-prompts-models-and-runs.md"
RELEASE_PATH = "publishing/create-a-versioned-scholarly-release.md"
CORRECTION_PATH = "publishing/correct-a-published-digital-resource-without-erasing-history.md"
MAINTENANCE_PATH = "publishing/prepare-a-maintenance-and-succession-plan.md"

# Invented metadata confined to automated TEST FIXTURES. These values are not
# evidence that any person reviewed the handbook, its language or its sources.
TEST_REVIEWER = "Mira Novak (TEST FIXTURE)"
TEST_REVIEW_DATE = "2026-09-08"
TEST_REVIEW_SCOPE = "TEST FIXTURE ONLY: checked source attribution and Slovene terminology."
REVIEW_SENTINELS = (
    None, "", "   ", "pending", "PENDING", "unknown", "not_run", "not reviewed",
    "fill", "TBD", "n/a", "NA", "null", "None", "~", "v čakanju", "čaka",
    "neznano", "ni izvedeno", "ni pregledano", "dopolnite",
)


def replace_at(record: dict, path: tuple, value: object) -> None:
    target = record
    for component in path[:-1]:
        target = target[component]
    target[path[-1]] = value


class DocumentationContractTests(unittest.TestCase):
    def record(self, path: str, locale: str = "en") -> tuple[dict, str, str]:
        record_type, fields = RECORDS[path]
        text = (ROOT / "docs" / locale / "workflows" / path).read_text(encoding="utf-8")
        return record_from_markdown(text, record_type), record_type, fields

    def test_audit_cannot_omit_truncation_or_validation_protocol(self) -> None:
        record, record_type, fields = self.record("ai/document-and-audit-a-source-grounded-ai-analysis.md")
        for field in ("truncation", "validation_protocol", "unavailable_details"):
            with self.subTest(field=field):
                damaged = copy.deepcopy(record)
                del damaged[field]
                with self.assertRaisesRegex(ValueError, field):
                    validate_record(damaged, record_type, fields)

    def test_release_cannot_silently_assign_a_teaching_identifier(self) -> None:
        record, record_type, fields = self.record("publishing/create-a-versioned-scholarly-release.md")
        record["identifiers"]["doi"] = "invented-placeholder"
        with self.assertRaisesRegex(ValueError, "unassigned DOI/ISBN"):
            validate_record(record, record_type, fields)

    def test_audit_passage_must_resolve_to_a_preserved_sample(self) -> None:
        record, record_type, fields = self.record("ai/document-and-audit-a-source-grounded-ai-analysis.md")
        record["passage_ids"] = ["TNLP-NONEXISTENT"]
        with self.assertRaisesRegex(ValueError, "does not resolve"):
            validate_record(record, record_type, fields)

    def test_release_manifest_requires_translation_and_rights(self) -> None:
        record, record_type, fields = self.record("publishing/create-a-versioned-scholarly-release.md")
        for field in ("translation_status", "licence", "accessibility"):
            with self.subTest(field=field):
                damaged = copy.deepcopy(record)
                del damaged["manifest"][0][field]
                with self.assertRaisesRegex(ValueError, field):
                    validate_record(damaged, record_type, fields)

    def test_maintenance_record_requires_credential_custody(self) -> None:
        record, record_type, fields = self.record("publishing/prepare-a-maintenance-and-succession-plan.md")
        del record["services"][0]["credential_reference"]
        with self.assertRaisesRegex(ValueError, "credential_reference"):
            validate_record(record, record_type, fields)

    def test_schema_comparison_detects_nested_translation_drift(self) -> None:
        path = "publishing/create-a-versioned-scholarly-release.md"
        english, _, _ = self.record(path, "en")
        slovene, _, _ = self.record(path, "sl")
        self.assertEqual(structure(english), structure(slovene))
        del slovene["manifest"][0]["review_scope"]
        self.assertNotEqual(structure(english), structure(slovene))

    def test_all_published_teaching_records_satisfy_the_contract(self) -> None:
        for path in RECORDS:
            for locale in ("en", "sl"):
                with self.subTest(path=path, locale=locale):
                    record, record_type, fields = self.record(path, locale)
                    validate_record(record, record_type, fields)

    def test_chapter_depth_has_a_minimum_but_no_automatic_maximum(self) -> None:
        for count in (0, 2299):
            with self.subTest(count=count), self.assertRaises(ValueError):
                validate_chapter_length(count)
        for count in (2300, 3300, 3501, 10000):
            with self.subTest(count=count):
                validate_chapter_length(count)

    def test_completed_review_accepts_explicit_test_fixture_metadata(self) -> None:
        validate_review_metadata(TEST_REVIEWER, TEST_REVIEW_DATE, TEST_REVIEW_SCOPE, "TEST FIXTURE")

    def test_substantive_slovene_review_scope_can_contain_the_preposition_na(self) -> None:
        validate_review_metadata(
            "Mira Novak", TEST_REVIEW_DATE,
            "TEST FIXTURE: preverjena navezava trditev na vire in slovenska terminologija.",
            "TEST FIXTURE ONLY: invented reviewer metadata, not a handbook review",
        )

    def test_unnamed_review_roles_remain_invalid_when_punctuated_or_padded(self) -> None:
        for reviewer in ("named reviewer", "named reviewer.", "human reviewer (assigned)",
                         "ime / priimek", "strokovni pregledovalec."):
            with self.subTest(reviewer=reviewer), self.assertRaisesRegex(ValueError, "reviewer"):
                validate_review_metadata(reviewer, TEST_REVIEW_DATE, TEST_REVIEW_SCOPE, "TEST FIXTURE")

    def test_completed_review_rejects_english_slovene_and_null_like_sentinels(self) -> None:
        for field in ("reviewer", "review_date", "review_scope"):
            for sentinel in REVIEW_SENTINELS:
                with self.subTest(field=field, sentinel=sentinel), self.assertRaises(ValueError):
                    values = dict(reviewer=TEST_REVIEWER, review_date=TEST_REVIEW_DATE,
                                  review_scope=TEST_REVIEW_SCOPE)
                    values[field] = sentinel
                    validate_review_metadata(**values, context="TEST FIXTURE")

    def test_completed_review_requires_strict_valid_iso_calendar_date(self) -> None:
        for invalid in ("20260908", "2026-9-8", "2026-02-30", "2025-02-29",
                        "2026-13-01", "08.09.2026", "2026-09-08T00:00:00Z", " 2026-09-08 "):
            with self.subTest(date=invalid), self.assertRaises(ValueError):
                validate_review_metadata(TEST_REVIEWER, invalid, TEST_REVIEW_SCOPE, "TEST FIXTURE")

    def test_completed_review_requires_substantive_scope(self) -> None:
        for scope in ("Reviewed", "Language checked", "Historical attribution reviewed", "a b c d"):
            with self.subTest(scope=scope), self.assertRaises(ValueError):
                validate_review_metadata(TEST_REVIEWER, TEST_REVIEW_DATE, scope, "TEST FIXTURE")

    def test_human_reviewed_translation_uses_the_same_review_contract(self) -> None:
        metadata = {
            "translation_status": "human-reviewed",
            "translation_reviewed_by": TEST_REVIEWER,
            "translation_reviewed_on": TEST_REVIEW_DATE,
            "translation_review_scope": TEST_REVIEW_SCOPE,
        }
        validate_translation(metadata, "TEST FIXTURE ONLY: no publication review is claimed.")
        fields = ("translation_reviewed_by", "translation_reviewed_on", "translation_review_scope")
        for field in fields:
            for invalid in (None, "pending", "v čakanju", "null"):
                with self.subTest(field=field, value=invalid), self.assertRaises(ValueError):
                    damaged = {**metadata, field: invalid}
                    validate_translation(damaged, "TEST FIXTURE ONLY")
        for invalid in ("20260908", "2026-02-30"):
            with self.subTest(date=invalid), self.assertRaises(ValueError):
                validate_translation({**metadata, "translation_reviewed_on": invalid}, "TEST FIXTURE ONLY")
        with self.assertRaises(ValueError):
            validate_translation({**metadata, "translation_review_scope": "Language checked"}, "TEST FIXTURE ONLY")

    def test_machine_assisted_translation_still_requires_visible_notice(self) -> None:
        metadata = {"translation_status": "machine-assisted draft; requires human language review"}
        validate_translation(metadata, "TEST FIXTURE: strojno podprti osnutek čaka na pregled.")
        with self.assertRaises(ValueError):
            validate_translation(metadata, "TEST FIXTURE without a visible translation notice.")

    def test_unfinished_translation_cannot_carry_nonnull_completed_review_metadata(self) -> None:
        metadata = {"translation_status": "machine-assisted draft; requires human language review"}
        for field in ("translation_reviewed_by", "translation_reviewed_on", "translation_review_scope"):
            for value in ("pending", "null", TEST_REVIEW_SCOPE):
                with self.subTest(field=field, value=value), self.assertRaisesRegex(ValueError, "metadata"):
                    validate_translation({**metadata, field: value}, "TEST FIXTURE: strojno podprti osnutek.")

    def test_pending_ai_review_fields_must_be_actual_null_values(self) -> None:
        for path in (AUDIT_PATH, ROBUSTNESS_PATH):
            record, record_type, fields = self.record(path)
            for field in ("reviewer", "review_date", "review_scope"):
                for invalid in ("pending", "v čakanju", "null", "", TEST_REVIEW_SCOPE):
                    with self.subTest(path=path, field=field, value=invalid), self.assertRaises(ValueError):
                        damaged = copy.deepcopy(record)
                        damaged[field] = invalid
                        validate_record(damaged, record_type, fields)

    def test_completed_ai_record_uses_strict_review_metadata(self) -> None:
        for path in (AUDIT_PATH, ROBUSTNESS_PATH):
            record, record_type, fields = self.record(path)
            record.update(review_status="human-reviewed", reviewer=TEST_REVIEWER,
                          review_date=TEST_REVIEW_DATE, review_scope=TEST_REVIEW_SCOPE)
            validate_record(record, record_type, fields)
            for field, invalid in (("reviewer", "pending"), ("reviewer", "v čakanju"),
                                   ("review_date", "20260908"), ("review_scope", "Checked")):
                with self.subTest(path=path, field=field), self.assertRaises(ValueError):
                    damaged = copy.deepcopy(record)
                    damaged[field] = invalid
                    validate_record(damaged, record_type, fields)

    def test_localized_answer_cards_match_frontmatter(self) -> None:
        for locale, category, difficulty in (
            ("en", "Publishing & FAIR data", "intermediate"),
            ("sl", "Objavljanje in podatki FAIR", "srednje zahtevno"),
        ):
            metadata = {"category": category, "difficulty": difficulty, "time": "90–150 min"}
            card = '<div class="answer-meta" markdown>\n' + "".join(
                f"<span>{metadata[field]}</span>" for field in ("category", "difficulty", "time")
            ) + "\n</div>"
            with self.subTest(locale=locale):
                validate_answer_meta(card, metadata, locale)
            for field in ("category", "difficulty", "time"):
                for damaged in (
                    card.replace(f"<span>{metadata[field]}</span>", ""),
                    card.replace(f"<span>{metadata[field]}</span>", "<span>wrong value</span>"),
                ):
                    with self.subTest(locale=locale, field=field), self.assertRaises(ValueError):
                        validate_answer_meta(damaged, metadata, locale)
            for damaged in ("", card + card, card.replace("answer-meta", "different-card")):
                with self.subTest(locale=locale, malformed=damaged), self.assertRaises(ValueError):
                    validate_answer_meta(damaged, metadata, locale)

    def test_every_actual_workflow_has_a_matching_localized_answer_card(self) -> None:
        for path in RECORDS:
            for locale in ("en", "sl"):
                with self.subTest(path=path, locale=locale):
                    text = (ROOT / "docs" / locale / "workflows" / path).read_text(encoding="utf-8")
                    validate_answer_meta(text, frontmatter(text), locale)

    def test_rendered_metadata_spans_are_direct_flex_children(self) -> None:
        # md_in_html's default block mode inserts a paragraph: inline chips
        # then split words at mobile width instead of wrapping as flex items.
        for path in RECORDS:
            for locale in ("en", "sl"):
                with self.subTest(path=path, locale=locale):
                    text = (ROOT / "docs" / locale / "workflows" / path).read_text(encoding="utf-8")
                    rendered = markdown(text, extensions=["fenced_code", "md_in_html"])
                    cards = re.findall(r'<div class="answer-meta">(.*?)</div>', rendered, re.S)
                    self.assertEqual(len(cards), 1)
                    self.assertEqual(cards[0].count("<span>"), 3)
                    self.assertNotIn("<p>", cards[0])

    def test_answer_card_in_code_or_comment_does_not_count_as_a_visible_card(self) -> None:
        metadata = {"category": "AI", "difficulty": "intermediate", "time": "90–150 min"}
        card = ('<div class="answer-meta" markdown><span>AI</span>'
                '<span>intermediate</span><span>90–150 min</span></div>')
        examples = {
            "backtick fence": "```html\n" + card + "\n```\n",
            "tilde fence": "~~~html\n" + card + "\n~~~\n",
            "inline code": "`" + card + "`",
            "indented code": "    " + card + "\n",
            "HTML comment": "<!--" + card + "-->",
        }
        for kind, example in examples.items():
            with self.subTest(kind=kind), self.assertRaisesRegex(ValueError, "answer-meta"):
                validate_answer_meta(example, metadata, "en")

    def test_all_five_records_retain_structure_and_operational_parity(self) -> None:
        for path in RECORDS:
            with self.subTest(path=path):
                english, record_type, _ = self.record(path, "en")
                slovene, _, _ = self.record(path, "sl")
                self.assertEqual(structure(english), structure(slovene))
                validate_bilingual_invariants(english, slovene, record_type)

    def test_bilingual_operational_drift_is_not_hidden_by_equal_scalar_types(self) -> None:
        mutations = {
            AUDIT_PATH: (
                (("source_documents", 0), "teaching-data/other/source.csv"),
                (("passage_ids", 0), "TNLP-OTHER-ID"),
                (("model_version_or_snapshot",), "different-model-version"),
                (("output_path",), "output/other.tsv"),
                (("review_status",), "human-reviewed"),
            ),
            ROBUSTNESS_PATH: (
                (("planned_runs",), 80),
                (("conditions", 0, "condition_id"), "C99"),
                (("conditions", 2, "passage_order"), ["TNLP-CLEAN-02", "TNLP-AF-REF", "TNLP-AF-OCR"]),
                (("prompt_registry", "P0"), "TEST FIXTURE: a substantively different prompt"),
                (("budget", "maximum_paid_cost_eur"), 50),
                (("results_status",), "completed"),
            ),
            RELEASE_PATH: (
                (("candidate_version",), "2.0.0"),
                (("manifest", 0, "path"), "docs/en/different-source.md"),
                (("manifest", 0, "review_status"), "human-reviewed"),
                (("manifest", 0, "licence"), "CC0-1.0"),
                (("identifiers", "status"), "assigned"),
                (("artefacts", 0, "path"), "different-release.zip"),
            ),
            CORRECTION_PATH: (
                (("correction_id",), "EX-ERR-002"),
                (("release_classification", "level"), "patch"),
                (("release_classification", "target_version"), "1.0.1"),
                (("affected_objects", 2), "LETTER-COUNT-02"),
            ),
            MAINTENANCE_PATH: (
                (("services", 1, "owner_role"), "technical_maintainer"),
            ),
        }
        for path, changes in mutations.items():
            english, record_type, _ = self.record(path, "en")
            slovene, _, _ = self.record(path, "sl")
            for field_path, value in changes:
                with self.subTest(path=path, field=field_path):
                    damaged = copy.deepcopy(slovene)
                    replace_at(damaged, field_path, value)
                    self.assertNotEqual(damaged, slovene, "Regression mutation must actually change its fixture")
                    self.assertEqual(structure(english), structure(damaged))
                    with self.assertRaises(ValueError):
                        validate_bilingual_invariants(english, damaged, record_type)

    def test_bilingual_numeric_budget_in_translated_maintenance_prose_is_invariant(self) -> None:
        english, record_type, _ = self.record(MAINTENANCE_PATH, "en")
        slovene, _, _ = self.record(MAINTENANCE_PATH, "sl")
        slovene["review_cadence"] = re.sub(r"\b2\b", "20", slovene["review_cadence"])
        self.assertIn("20", slovene["review_cadence"])
        with self.assertRaises(ValueError):
            validate_bilingual_invariants(english, slovene, record_type)

    def test_bilingual_human_prose_can_differ_without_changing_operations(self) -> None:
        prose = {
            AUDIT_PATH: ("research_question", "Kako uvod oblikuje politično enotnost?"),
            ROBUSTNESS_PATH: ("research_question", "Ali povzetek ohrani pripisovanje in negotovost?"),
            RELEASE_PATH: ("project", "Izmišljena dvojezična učna izdaja za preizkus"),
            CORRECTION_PATH: ("claim_before", "Tabela naj bi opisovala 40 različnih zgodovinskih pisem."),
            MAINTENANCE_PATH: ("owner", "Ustanova prevzame odgovornost po pisni potrditvi."),
        }
        for path, (field, value) in prose.items():
            with self.subTest(path=path):
                english, record_type, _ = self.record(path, "en")
                slovene, _, _ = self.record(path, "sl")
                slovene[field] = value
                validate_bilingual_invariants(english, slovene, record_type)


class RobustnessPlanTests(unittest.TestCase):
    def setUp(self) -> None:
        # Every negative test starts from a independently validated plan. A
        # missing base field must fail the suite, not make all negatives pass.
        validate_robustness_plan(self.plan())

    def plan(self) -> dict:
        passages = ["TNLP-CLEAN-02", "TNLP-AF-REF", "TNLP-AF-OCR"]
        return {
            "record_type": "ai-robustness-plan", "record_status": "template",
            "passage_ids": passages,
            "prompt_registry": {
                "P0": "TEST FIXTURE ONLY: identify the speaker and preserve uncertainty.",
                "P1": "TEST FIXTURE ONLY: distinguish the publication's assertion from a finding.",
            },
            "model_registry": {
                alias: {"model_identifier": None, "model_version_or_snapshot": None, "status": "not_selected"}
                for alias in ("M1", "M2")
            },
            "repetitions_per_condition": 2,
            "conditions": [
                {"condition_id": "C0", "prompt": "P0", "model": "M1", "passage_order": passages[:], "changed_factor": None},
                {"condition_id": "C1", "prompt": "P1", "model": "M1", "passage_order": passages[:], "changed_factor": "prompt"},
                {"condition_id": "C2", "prompt": "P0", "model": "M1", "passage_order": passages[::-1], "changed_factor": "passage_order"},
                {"condition_id": "C3", "prompt": "P0", "model": "M2", "passage_order": passages[:], "changed_factor": "model"},
            ],
            "planned_runs": 8, "actual_runs": 0, "run_records": [],
            "validation_sample": passages[:],
            "validation_strata": [
                {"stratum": "synthetic_clean", "passage_ids": ["TNLP-CLEAN-02"]},
                {"stratum": "historical_reference", "passage_ids": ["TNLP-AF-REF"]},
                {"stratum": "historical_ocr", "passage_ids": ["TNLP-AF-OCR"]},
            ],
            "budget": {"maximum_model_calls": 8, "maximum_paid_cost_eur": 5, "maximum_review_minutes": 120,
                       "actual_cost": "not_run", "energy_measurement": "unknown"},
            "results_status": "not_run",
        }

    def test_declared_four_condition_two_repetition_plan_is_valid(self) -> None:
        validate_robustness_plan(self.plan())

    def test_planned_run_count_must_equal_conditions_times_repetitions(self) -> None:
        for field, value in (("planned_runs", 80), ("repetitions_per_condition", 3),
                             ("repetitions_per_condition", 0), ("repetitions_per_condition", True)):
            with self.subTest(field=field, value=value), self.assertRaisesRegex(ValueError, field):
                plan = self.plan()
                plan[field] = value
                validate_robustness_plan(plan)

    def test_actual_runs_match_records_and_template_claims_no_runs(self) -> None:
        for actual, records in ((1, []), (0, [{"run_id": "TEST-RUN-01"}]),
                                (1, [{"run_id": "TEST-RUN-01"}])):
            with self.subTest(actual=actual, records=records), self.assertRaisesRegex(ValueError, "actual_runs"):
                plan = self.plan()
                plan.update(actual_runs=actual, run_records=records)
                validate_robustness_plan(plan)

    def test_condition_identifiers_and_baseline_are_unambiguous(self) -> None:
        for index, identifier in ((1, "C0"), (0, "missing-baseline")):
            with self.subTest(index=index, identifier=identifier), self.assertRaisesRegex(ValueError, "condition"):
                plan = self.plan()
                plan["conditions"][index]["condition_id"] = identifier
                validate_robustness_plan(plan)

    def test_condition_prompt_model_and_passages_resolve(self) -> None:
        for field, value in (("prompt", "P-MISSING"), ("model", "M-MISSING"),
                             ("passage_order", ["TNLP-NONEXISTENT", "TNLP-AF-REF", "TNLP-AF-OCR"]),
                             ("passage_order", ["TNLP-CLEAN-02", "TNLP-CLEAN-02", "TNLP-AF-OCR"]),
                             ("passage_order", ["TNLP-CLEAN-02", "TNLP-AF-REF"])):
            with self.subTest(field=field, value=value), self.assertRaisesRegex(ValueError, field):
                plan = self.plan()
                plan["conditions"][1][field] = value
                validate_robustness_plan(plan)

    def test_prompt_registry_requires_complete_nonempty_prompt_strings(self) -> None:
        for invalid in (None, "", {}, []):
            with self.subTest(value=invalid), self.assertRaisesRegex(ValueError, "prompt_registry"):
                plan = self.plan()
                plan["prompt_registry"]["P1"] = invalid
                validate_robustness_plan(plan)
        plan = self.plan()
        plan["prompt_registry"]["P1"] = plan["prompt_registry"]["P0"]
        with self.assertRaisesRegex(ValueError, "different instructions"):
            validate_robustness_plan(plan)

    def test_model_aliases_are_documented_but_not_claimed_as_selected(self) -> None:
        for field, invalid in (("model_identifier", "TEST-MODEL"),
                               ("model_version_or_snapshot", "TEST-VERSION"), ("status", "selected")):
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "model_registry"):
                plan = self.plan()
                plan["model_registry"]["M1"][field] = invalid
                validate_robustness_plan(plan)
        plan = self.plan()
        del plan["model_registry"]["M1"]["model_version_or_snapshot"]
        with self.assertRaisesRegex(ValueError, "model_version_or_snapshot"):
            validate_robustness_plan(plan)

    def test_each_condition_changes_exactly_its_declared_factor(self) -> None:
        changes = (
            (0, "changed_factor", "prompt"),
            (1, "changed_factor", "model"),
            (1, "prompt", "P0"),
            (1, "model", "M2"),
            (2, "passage_order", ["TNLP-CLEAN-02", "TNLP-AF-REF", "TNLP-AF-OCR"]),
            (3, "model", "M1"),
        )
        for index, field, value in changes:
            with self.subTest(condition=index, field=field), self.assertRaisesRegex(ValueError, "changed_factor"):
                plan = self.plan()
                plan["conditions"][index][field] = value
                validate_robustness_plan(plan)

    def test_budget_must_cover_the_declared_number_of_calls(self) -> None:
        plan = self.plan()
        plan["budget"]["maximum_model_calls"] = 7
        with self.assertRaisesRegex(ValueError, "maximum_model_calls"):
            validate_robustness_plan(plan)

    def test_validation_sample_and_stratum_passages_must_resolve(self) -> None:
        for path in (("validation_sample",), ("validation_strata", 0, "passage_ids")):
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, "validation passage IDs"):
                plan = self.plan()
                replace_at(plan, path, ["TNLP-NONEXISTENT"])
                validate_robustness_plan(plan)

    def test_legacy_source_order_cannot_replace_or_override_explicit_passage_order(self) -> None:
        plan = self.plan()
        plan["conditions"][0]["source_order"] = "original"
        with self.assertRaisesRegex(ValueError, "condition fields"):
            validate_robustness_plan(plan)

    def test_zero_run_teaching_plan_cannot_claim_completed_results(self) -> None:
        plan = self.plan()
        plan["results_status"] = "completed"
        with self.assertRaisesRegex(ValueError, "results_status"):
            validate_robustness_plan(plan)


if __name__ == "__main__":
    unittest.main()
