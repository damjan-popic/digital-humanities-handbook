#!/usr/bin/env python3
"""Hermetic regression tests for case metadata, content and generated catalogues.

All projects, pages, audits and review metadata below are invented TEST FIXTURES.
Only the local schema is copied from the repository; no real case is inspected,
no model or project code runs, and no URL is requested by this suite.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import yaml

from build_case_study_index import catalogue, check_generated, generated
from case_studies import (
    CONNECTION_FIELDS,
    EVIDENCE_TYPES,
    INDEX,
    ROOT,
    SCHEMA,
    SHOWCASE_HEADINGS,
    SOURCE,
    frontmatter,
    headings,
    load_records,
    schema,
    validate_records,
    validate_schema,
)
from handbook_structure import CHAPTERS


TEST_DATE = "2000-01-15"
TEST_SECTION = "INVENTED TEST FIXTURE ONLY: no inspection or project execution was performed."
TEST_COMPONENTS = ("code", "data", "documentation", "source-material", "images", "interface-content")
TEST_EVIDENCE = {
    "en": ("Project or institutional claim", "Observed interface behaviour",
           "Inspected repository/file evidence", "Locally executed result", "Editorial inference"),
    "sl": ("Trditev projekta ali ustanove", "Opaženo delovanje vmesnika",
           "Pregledano dokazno gradivo iz repozitorija ali datoteke", "Rezultat lokalnega zagona", "Uredniški sklep"),
}
TEST_REVIEW = {
    "translation_reviewed_by": "Mira Novak (INVENTED TEST FIXTURE)",
    "translation_reviewed_on": TEST_DATE,
    "translation_review_scope": (
        "INVENTED TEST FIXTURE ONLY: checked Slovene terminology and source attribution."
    ),
}


def case_record(slug: str = "alpha", *, paired: bool = False,
                showcase: bool = False) -> dict:
    """A complete minimal record, never evidence about an actual project."""
    return {
        "case_id": f"CASE-{slug}",
        "slug": slug,
        "title_en": f"TEST FIXTURE {slug}",
        "title_sl": f"PREIZKUSNI PRIMER {slug}" if paired else None,
        "page_en": f"docs/en/case-studies/{slug}.md",
        "page_sl": f"docs/sl/case-studies/{slug}.md" if paired else None,
        "project_url": f"https://project.invalid/{slug}",
        "repository_url": f"https://repository.invalid/{slug}",
        "method_domains": ["text-analysis"],
        "source_types": ["historical-documents"],
        "inspection_modes": ["documentation-inspected"],
        "languages_regions": ["slovene"],
        "code_availability": "unknown",
        "reusable_data_availability": "unknown",
        "rights_status": "unknown",
        "rights_components": [{
            "component": component,
            "status": "unknown",
            "licence_or_terms": None,
            "scope_note": "INVENTED TEST FIXTURE: component rights have not been verified.",
            "audit_locator": f"release/case-study-audit.md#rights-{slug}-{component}",
        } for component in TEST_COMPONENTS],
        "translation_status": "paired-draft" if paired else "english-fallback",
        "lifecycle_status": "maintenance-unclear",
        "editorial_disposition": "retain-as-legacy",
        "evidence_status": "project-description-only",
        "repository_relationship": "external-repository",
        "last_checked": TEST_DATE,
        "content_standard": "showcase-v1" if showcase else "legacy-audited",
        "audit_record": f"release/case-study-audit.md#case-{slug}",
        "short_summary_en": "Invented test fixture; no project was inspected.",
        "short_summary_sl": "Izmišljeni preizkusni primer; projekt ni bil pregledan." if paired else None,
        "chapter_connections": ["chapters/" + CHAPTERS[0]],
        "workflow_connections": ["workflows/test/test-method.md"],
        "connection_remediation": None,
    }


class CaseStudyContractTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="case-study-tests-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.write(SCHEMA, (ROOT / SCHEMA).read_text(encoding="utf-8"))
        self.record = case_record()
        # An added required schema field must prompt an explicit fixture update.
        self.assertEqual(set(self.record), set(schema(self.root)["$defs"]["case"]["required"]))
        self.write_fixture([self.record])

    def write(self, relative: str, text: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")

    def write_yaml(self, relative: str, value: object) -> None:
        self.write(relative, yaml.safe_dump(value, allow_unicode=True, sort_keys=False))

    def write_source(self, records: list[dict]) -> None:
        authored = [{key: value for key, value in record.items() if key not in CONNECTION_FIELDS}
                    for record in records]
        self.write_yaml(SOURCE, {"schema_version": 2, "cases": authored})

    def write_page(self, record: dict, locale: str, *, metadata: dict | None = None,
                   body: str | None = None) -> None:
        if metadata is None:
            metadata = {"title": record[f"title_{locale}"], **{
                field: record[field]
                for field in ("case_id", "content_standard", "translation_status", "audit_record")
            }}
        if body is None:
            body = "# TEST FIXTURE ONLY\n\nNo real project or source was inspected.\n\n"
            if locale == "sl":
                body += "Strojno podprti osnutek; potreben je človeški jezikovni pregled.\n\n"
            if record["content_standard"] == "showcase-v1":
                for index, heading in enumerate(SHOWCASE_HEADINGS[locale]):
                    body += f"## {heading}\n\n{TEST_SECTION}\n\n"
                    if index == 6:
                        body += ("| Type | Locator | Action | Limit |\n| --- | --- | --- | --- |\n"
                                 + "\n".join(f"| {kind} | TEST FIXTURE | Not inspected | No real evidence claimed |"
                                             for kind in TEST_EVIDENCE[locale]) + "\n\n")
        self.write(record[f"page_{locale}"], "---\n" + yaml.safe_dump(
            metadata, allow_unicode=True, sort_keys=False) + "---\n\n" + body)

    def write_fixture(self, records: list[dict]) -> None:
        """Build only temporary local pages, an audit and the authoritative map."""
        fixture_schema = schema(self.root)
        # Substitute a tiny invented baseline in the TEMPORARY schema only.
        fixture_schema["x-legacy-case-ids"] = [record["case_id"] for record in records]
        self.write(SCHEMA, json.dumps(fixture_schema, ensure_ascii=False, indent=2) + "\n")
        self.write_source(records)
        mapping = {"case_studies": {}}
        audits = ["# INVENTED TEST FIXTURES — not a publication audit\n"]
        for record in records:
            mapping["case_studies"][f"case-studies/{record['slug']}.md"] = {
                "chapters": record["chapter_connections"],
                "workflows": record["workflow_connections"],
            }
            anchor = record["audit_record"].split("#", 1)[1]
            audits.append(f'<a id="{anchor}"></a>\n\n{record["case_id"]}; {record["last_checked"]}.\n')
            if record["connection_remediation"]:
                audits.append(record["connection_remediation"] + "\n")
            for component in record["rights_components"]:
                rights_anchor = component["audit_locator"].split("#", 1)[1]
                audits.append(f'<a id="{rights_anchor}"></a>\n\n{component["scope_note"]}\n')
            for field in CONNECTION_FIELDS:
                for target in record[field]:
                    self.write("docs/en/" + target, "# INVENTED TEST FIXTURE ONLY\n")
            for locale in ("en", "sl"):
                if record[f"page_{locale}"]:
                    self.write_page(record, locale)
        self.write_yaml("intertextuality.yml", mapping)
        self.write("release/case-study-audit.md", "\n".join(audits))

    def checked_records(self) -> list[dict]:
        records = load_records(self.root)
        validate_records(records, self.root)
        return records

    def write_generated(self, records: list[dict]) -> dict[str, str]:
        outputs = generated(records, self.root)
        for relative, text in outputs.items():
            self.write(relative, text)
        return outputs

    def test_minimal_audited_legacy_fixture_passes_without_code_or_data(self) -> None:
        self.assertEqual(self.checked_records(), [self.record])

    def test_duplicate_case_ids_slugs_and_page_paths_are_rejected(self) -> None:
        other = case_record("beta")
        self.write_fixture([self.record, other])
        fixture_schema = schema(self.root)
        fixture_schema["x-legacy-case-ids"] = [self.record["case_id"]]
        self.write(SCHEMA, json.dumps(fixture_schema))
        for field, message in (("case_id", "Duplicate case_id"), ("slug", "Duplicate slug"),
                               ("page_en", "Duplicate local page path")):
            with self.subTest(field=field):
                damaged = copy.deepcopy([self.record, other])
                damaged[1][field] = damaged[0][field]
                with self.assertRaisesRegex(ValueError, message):
                    validate_records(damaged, self.root)

    def test_case_id_must_identify_its_slug(self) -> None:
        fixture_schema = schema(self.root)
        fixture_schema["x-legacy-case-ids"] = ["CASE-other"]
        self.write(SCHEMA, json.dumps(fixture_schema))
        with self.assertRaisesRegex(ValueError, "ID and slug must agree"):
            validate_records([{**self.record, "case_id": "CASE-other"}], self.root)

    def test_audit_anchor_must_identify_its_case_and_cannot_be_shared(self) -> None:
        with self.assertRaisesRegex(ValueError, "audit anchor must identify this case"):
            validate_records([{**self.record, "audit_record": "release/case-study-audit.md#case-other"}], self.root)
        other = {**case_record("beta"), "audit_record": self.record["audit_record"]}
        with self.assertRaisesRegex(ValueError, "Duplicate audit_record"):
            validate_records([self.record, other], self.root)

    def test_new_cases_cannot_use_the_frozen_legacy_exemption(self) -> None:
        new_case = case_record("new-case")
        self.write_fixture([self.record, new_case])
        fixture_schema = schema(self.root)
        fixture_schema["x-legacy-case-ids"] = [self.record["case_id"]]
        self.write(SCHEMA, json.dumps(fixture_schema))
        with self.assertRaisesRegex(ValueError, "new cases cannot claim the legacy exemption"):
            self.checked_records()

    def test_original_legacy_inventory_cannot_disappear(self) -> None:
        self.write_fixture([self.record, case_record("beta")])
        with self.assertRaisesRegex(ValueError, "Original legacy inventory cannot disappear"):
            validate_records([self.record], self.root)

    def test_every_controlled_vocabulary_rejects_unknown_values(self) -> None:
        definitions = schema(self.root)["$defs"]
        for field, definition in definitions.items():
            if "enum" not in definition or field not in self.record:
                continue
            with self.subTest(field=field):
                damaged = copy.deepcopy(self.record)
                damaged[field] = ["invented-invalid-enum"] if isinstance(damaged[field], list) else "invented-invalid-enum"
                with self.assertRaisesRegex(ValueError, field):
                    validate_schema([damaged], self.root)

    def test_all_required_machine_fields_are_required(self) -> None:
        for field in self.record:
            with self.subTest(field=field):
                damaged = copy.deepcopy(self.record)
                del damaged[field]
                with self.assertRaisesRegex(ValueError, field):
                    validate_schema([damaged], self.root)

    def test_last_checked_requires_strict_iso_calendar_date(self) -> None:
        for invalid in ("20000115", "2000-1-15", "2000-01-5", "2000-02-30", "2001-02-29",
                        "2000-13-01", "15.01.2000", "2000-01-15T00:00:00Z", " 2000-01-15 ", None):
            with self.subTest(value=invalid), self.assertRaisesRegex(ValueError, "last_checked"):
                validate_schema([{**self.record, "last_checked": invalid}], self.root)

    def test_last_checked_cannot_claim_a_future_inspection(self) -> None:
        future = {**self.record, "last_checked": "9999-12-31"}
        self.write_fixture([future])
        with self.assertRaisesRegex(ValueError, "future last_checked"):
            self.checked_records()

    def test_top_level_licence_cannot_replace_component_rights(self) -> None:
        with self.assertRaisesRegex(ValueError, "licence"):
            validate_schema([{**self.record, "licence": "CC BY 4.0"}], self.root)

    def test_unknown_components_cannot_be_promoted_to_verified_summary(self) -> None:
        with self.assertRaisesRegex(ValueError, "rights_status"):
            validate_records([{**self.record, "rights_status": "verified-open"}], self.root)

    def test_retired_metadata_keys_and_codes_are_rejected(self) -> None:
        for change in (
            {"inspection_depth": "repository-inspected"},
            {"editor_relationship": "editor-owned"},
            {"licence": "MIT"},
            {"code_availability": "open"},
            {"evidence_status": "independently-inspected"},
            {"evidence_status": "mixed"},
            {"lifecycle_status": "deferred"},
            {"repository_relationship": "editor-owned"},
            {"repository_relationship": "collaborative"},
            {"repository_relationship": "external"},
        ):
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_schema([{**self.record, **change}], self.root)

    def test_inspection_modes_require_a_nonempty_unique_list_of_explicit_modes(self) -> None:
        for modes in ("repository-inspected", [], ["mixed"], ["unknown"],
                      ["repository-inspected", "repository-inspected"], [None]):
            with self.subTest(modes=modes), self.assertRaises(ValueError):
                validate_schema([{**self.record, "inspection_modes": modes}], self.root)

    def test_all_five_inspection_modes_and_neutral_evidence_state_are_supported(self) -> None:
        modes = ["interface-inspected", "documentation-inspected", "repository-inspected",
                 "data-inspected", "locally-run"]
        record = {**self.record, "inspection_modes": modes, "evidence_status": "source-evidence-inspected"}
        self.write_fixture([record])
        self.assertEqual(set(self.checked_records()[0]["inspection_modes"]), set(modes))

    def test_new_method_domains_are_valid_without_changing_the_case_inventory(self) -> None:
        record = {**self.record, "method_domains": ["relational-databases", "reference-management", "scholarly-writing"]}
        self.write_fixture([record])
        self.assertEqual(len(self.checked_records()), 1)
        for locale in ("en", "sl"):
            definitions = schema(self.root)["$defs"]
            rendered = catalogue(self.checked_records(), locale, definitions)
            for value in record["method_domains"]:
                self.assertIn(definitions["method_domains"]["x-labels"][value][locale], rendered)

    def test_project_lifecycle_and_editorial_disposition_are_independent_fields(self) -> None:
        for lifecycle, disposition in (("current", "defer"), ("archived", "retain-and-upgrade"),
                                       ("maintenance-unclear", "archive"), ("unavailable", "replace")):
            with self.subTest(lifecycle=lifecycle, disposition=disposition):
                record = {**self.record, "lifecycle_status": lifecycle, "editorial_disposition": disposition}
                self.write_fixture([record])
                checked = self.checked_records()
                definitions = schema(self.root)["$defs"]
                for locale in ("en", "sl"):
                    rendered = catalogue(checked, locale, definitions)
                    self.assertIn(definitions["lifecycle_status"]["x-labels"][lifecycle][locale], rendered)
                    self.assertIn(definitions["editorial_disposition"]["x-labels"][disposition][locale], rendered)

    def test_catalogue_repository_relationship_is_neutral_not_an_ownership_claim(self) -> None:
        definitions = schema(self.root)["$defs"]
        for relationship in ("editor-account", "documented-fork-or-collaboration", "external-repository",
                             "unknown", "not-applicable"):
            with self.subTest(relationship=relationship):
                record = {**self.record, "repository_relationship": relationship}
                self.write_fixture([record])
                for locale in ("en", "sl"):
                    rendered = catalogue(self.checked_records(), locale, definitions)
                    self.assertIn(definitions["repository_relationship"]["x-labels"][relationship][locale], rendered)
                    self.assertNotIn("Editor-owned", rendered)
                    self.assertNotIn("V urednikovi lasti", rendered)
                    self.assertNotIn("Urednikov projekt", rendered)
                self.assertIn("Repository relationship", catalogue(self.checked_records(), "en", definitions))

    def test_factual_repository_relationship_requires_a_repository_url(self) -> None:
        for relationship in ("editor-account", "documented-fork-or-collaboration", "external-repository"):
            with self.subTest(relationship=relationship):
                record = {**self.record, "repository_relationship": relationship, "repository_url": None}
                self.write_fixture([record])
                with self.assertRaisesRegex(ValueError, "factual repository relationship requires repository_url"):
                    self.checked_records()

    def test_unknown_or_inapplicable_repository_relationship_supports_interface_only_cases(self) -> None:
        for relationship in ("unknown", "not-applicable"):
            with self.subTest(relationship=relationship):
                record = {**self.record, "repository_relationship": relationship, "repository_url": None,
                          "inspection_modes": ["interface-inspected"]}
                self.write_fixture([record])
                checked = self.checked_records()
                self.assertIsNone(checked[0]["repository_url"])
                self.assertEqual(checked[0]["repository_relationship"], relationship)
                self.assertEqual(checked[0]["inspection_modes"], ["interface-inspected"])

    def test_publicly_inspectable_code_does_not_imply_verified_reuse_rights(self) -> None:
        record = {**self.record, "code_availability": "publicly-inspectable"}
        self.write_fixture([record])
        checked = self.checked_records()
        self.assertEqual(checked[0]["rights_status"], "unknown")
        for component in checked[0]["rights_components"]:
            self.assertEqual(component["status"], "unknown")

    def test_all_six_distinct_rights_components_are_required(self) -> None:
        for index, component in enumerate(TEST_COMPONENTS):
            with self.subTest(missing=component):
                damaged = copy.deepcopy(self.record)
                damaged["rights_components"].pop(index)
                with self.assertRaises(ValueError):
                    validate_records([damaged], self.root)
                self.write_source([damaged])
                with self.assertRaises(ValueError):
                    load_records(self.root)

    def test_duplicate_component_names_fail_even_with_different_scope_or_locator(self) -> None:
        damaged = copy.deepcopy(self.record)
        damaged["rights_components"][-1].update(
            component="code", scope_note="INVENTED TEST FIXTURE: a different code rights note.")
        with self.assertRaises(ValueError):
            validate_records([damaged], self.root)
        self.write_source([damaged])
        with self.assertRaises(ValueError):
            load_records(self.root)

    def test_rights_component_shape_and_vocabularies_are_closed(self) -> None:
        for change in ({"component": "other"}, {"status": "mixed"}, {"status": "open"}, {"extra": True}):
            with self.subTest(change=change):
                damaged = copy.deepcopy(self.record)
                damaged["rights_components"][0].update(change)
                with self.assertRaises(ValueError):
                    validate_schema([damaged], self.root)
        for field in self.record["rights_components"][0]:
            with self.subTest(missing_field=field):
                damaged = copy.deepcopy(self.record)
                del damaged["rights_components"][0][field]
                with self.assertRaises(ValueError):
                    validate_schema([damaged], self.root)

    def test_unknown_or_inapplicable_components_require_actual_null_terms(self) -> None:
        for status in ("unknown", "not-applicable"):
            for terms in ("MIT", "unknown", "null", "", " "):
                with self.subTest(status=status, terms=terms):
                    damaged = copy.deepcopy(self.record)
                    damaged["rights_components"][0].update(status=status, licence_or_terms=terms)
                    with self.assertRaises(ValueError):
                        validate_schema([damaged], self.root)

    def test_declared_or_verified_components_require_nonempty_terms(self) -> None:
        for status in ("project-declared", "verified-open", "verified-restricted"):
            for terms in (None, "", " ", "\n\t"):
                with self.subTest(status=status, terms=terms):
                    damaged = copy.deepcopy(self.record)
                    damaged["rights_components"][0].update(status=status, licence_or_terms=terms)
                    with self.assertRaises(ValueError):
                        validate_schema([damaged], self.root)

    def test_component_scope_requires_a_substantive_explanation(self) -> None:
        for scope in (None, "", "TODO", "Not verified", "<!-- four words hidden here -->"):
            with self.subTest(scope=scope):
                damaged = copy.deepcopy(self.record)
                damaged["rights_components"][0]["scope_note"] = scope
                with self.assertRaises(ValueError):
                    validate_records([damaged], self.root)

    def test_project_declared_mit_is_preserved_without_promoting_unknown_summary(self) -> None:
        record = copy.deepcopy(self.record)
        record["rights_components"][0].update(status="project-declared", licence_or_terms="MIT")
        self.write_fixture([record])
        checked = self.checked_records()
        exported = json.loads(generated(checked, self.root)[INDEX])[0]
        self.assertEqual(exported["rights_status"], "unknown")
        self.assertEqual(exported["rights_components"][0]["licence_or_terms"], "MIT")
        self.assertEqual(exported["rights_components"][0]["status"], "project-declared")
        definitions = schema(self.root)["$defs"]
        for locale in ("en", "sl"):
            rendered = catalogue(checked, locale, definitions)
            self.assertIn("MIT", rendered)
            for component in record["rights_components"]:
                self.assertIn(component["audit_locator"], rendered)
        self.assertIn("licence identifier or recorded terms", catalogue(checked, "en", definitions))
        self.assertIn("zapis pogojev (neprevedeno)", catalogue(checked, "sl", definitions))
        self.assertNotIn("original-language", catalogue(checked, "en", definitions))
        self.assertNotIn("v izvirnem jeziku", catalogue(checked, "sl", definitions))

    def test_project_declared_terms_cannot_be_promoted_to_verified_rights(self) -> None:
        for summary in ("verified-open", "verified-restricted", "mixed", "not-applicable"):
            with self.subTest(summary=summary):
                record = copy.deepcopy(self.record)
                record["rights_components"][0].update(status="project-declared", licence_or_terms="MIT")
                record["rights_status"] = summary
                self.write_fixture([record])
                with self.assertRaisesRegex(ValueError, "rights_status"):
                    self.checked_records()

    def test_rights_summary_uses_verified_components_and_ignores_inapplicable_ones(self) -> None:
        for statuses, expected in (
            (["not-applicable"] * 6, "not-applicable"),
            (["unknown"] * 6, "unknown"),
            (["project-declared"] * 6, "unknown"),
            (["verified-open"] * 6, "verified-open"),
            (["verified-restricted"] * 6, "verified-restricted"),
            (["verified-open"] + ["not-applicable"] * 5, "verified-open"),
            (["verified-restricted"] + ["not-applicable"] * 5, "verified-restricted"),
            (["verified-open"] + ["unknown"] * 5, "mixed"),
            (["verified-restricted"] + ["project-declared"] * 5, "mixed"),
            (["verified-open", "verified-restricted"] + ["not-applicable"] * 4, "mixed"),
        ):
            with self.subTest(statuses=statuses, expected=expected):
                record = copy.deepcopy(self.record)
                for component, status in zip(record["rights_components"], statuses):
                    component.update(status=status, licence_or_terms=(
                        None if status in ("unknown", "not-applicable") else "INVENTED TEST FIXTURE terms"))
                record["rights_status"] = expected
                self.write_fixture([record])
                self.assertEqual(self.checked_records()[0]["rights_status"], expected)
                for incorrect in {"unknown", "verified-open", "verified-restricted", "mixed", "not-applicable"} - {expected}:
                    with self.assertRaisesRegex(ValueError, "rights_status"):
                        validate_records([{**record, "rights_status": incorrect}], self.root)

    def test_component_audit_locator_requires_its_exact_local_case_and_component(self) -> None:
        for locator in ("https://example.invalid/#rights-alpha-code", "release/other-audit.md#rights-alpha-code",
                        "release/case-study-audit.md#case-alpha", "release/case-study-audit.md#rights-beta-code",
                        "release/case-study-audit.md#rights-alpha-data"):
            with self.subTest(locator=locator):
                damaged = copy.deepcopy(self.record)
                damaged["rights_components"][0]["audit_locator"] = locator
                with self.assertRaises(ValueError):
                    validate_records([damaged], self.root)

    def test_component_audit_anchor_must_exist_once(self) -> None:
        original = (self.root / "release/case-study-audit.md").read_text(encoding="utf-8")
        marker = '<a id="rights-alpha-code"></a>'
        for text in (original.replace(marker, ""), original.replace(marker, marker + "\n" + marker)):
            with self.subTest(text=text):
                self.write("release/case-study-audit.md", text)
                with self.assertRaises(ValueError):
                    self.checked_records()

    def test_rights_anchor_in_another_case_section_cannot_supply_evidence(self) -> None:
        self.write_fixture([self.record, case_record("beta")])
        audit = (self.root / "release/case-study-audit.md").read_text(encoding="utf-8")
        marker = '<a id="rights-alpha-code"></a>'
        self.write("release/case-study-audit.md", audit.replace(marker, "") + "\n" + marker + "\n")
        with self.assertRaises(ValueError):
            self.checked_records()

    def test_component_locator_in_a_comment_is_not_a_real_audit_anchor(self) -> None:
        audit = (self.root / "release/case-study-audit.md").read_text(encoding="utf-8")
        marker = '<a id="rights-alpha-code"></a>'
        self.write("release/case-study-audit.md", audit.replace(marker, "<!-- " + marker + " -->"))
        with self.assertRaises(ValueError):
            self.checked_records()

    def test_component_status_and_name_labels_are_complete_in_both_languages(self) -> None:
        definitions = schema(self.root)["$defs"]
        self.assertEqual(set(definitions["rights_component"]["enum"]), set(TEST_COMPONENTS))
        self.assertEqual(set(definitions["rights_component_status"]["enum"]), {
            "unknown", "project-declared", "verified-open", "verified-restricted", "not-applicable"})
        for field in ("rights_component", "rights_component_status"):
            for value in definitions[field]["enum"]:
                for locale in ("en", "sl"):
                    with self.subTest(field=field, value=value, locale=locale):
                        self.assertTrue(definitions[field]["x-labels"][value][locale].strip())
        for locale in ("en", "sl"):
            rendered = catalogue(self.checked_records(), locale, definitions)
            for component in TEST_COMPONENTS:
                self.assertIn(definitions["rights_component"]["x-labels"][component][locale], rendered)
            self.assertIn(definitions["rights_component_status"]["x-labels"]["unknown"][locale], rendered)

    def test_missing_audit_file_is_rejected(self) -> None:
        (self.root / "release/case-study-audit.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing local page/file"):
            self.checked_records()

    def test_missing_duplicate_or_unmatched_audit_anchor_is_rejected(self) -> None:
        marker = '<a id="case-alpha"></a>'
        for text in ("No anchor", f"{marker}\n{marker}\nCASE-alpha {TEST_DATE}",
                     f"{marker}\nCASE-beta {TEST_DATE}", f"{marker}\nCASE-alpha 2000-01-16"):
            with self.subTest(text=text):
                self.write("release/case-study-audit.md", text)
                with self.assertRaisesRegex(ValueError, "audit"):
                    self.checked_records()

    def test_another_audit_section_cannot_supply_a_missing_date(self) -> None:
        self.write("release/case-study-audit.md", '<a id="case-alpha"></a>\nCASE-alpha\n'
                   f'<a id="case-beta"></a>\nCASE-beta {TEST_DATE}\n')
        with self.assertRaisesRegex(ValueError, "matching check date"):
            self.checked_records()

    def test_missing_case_page_is_rejected(self) -> None:
        (self.root / self.record["page_en"]).unlink()
        with self.assertRaisesRegex(ValueError, "Case inventory differs"):
            self.checked_records()

    def test_unregistered_case_page_is_rejected(self) -> None:
        self.write("docs/en/case-studies/unregistered.md", "# TEST FIXTURE\n")
        with self.assertRaisesRegex(ValueError, "Case inventory differs"):
            self.checked_records()

    def test_false_paired_status_without_slovene_fields_is_rejected(self) -> None:
        for status in ("paired-draft", "paired-human-reviewed"):
            with self.subTest(status=status), self.assertRaisesRegex(ValueError, "JSON schema"):
                validate_schema([{**self.record, "translation_status": status}], self.root)

    def test_paired_metadata_cannot_claim_a_nonexistent_slovene_page(self) -> None:
        paired = case_record(paired=True)
        self.write_fixture([paired])
        (self.root / paired["page_sl"]).unlink()
        with self.assertRaisesRegex(ValueError, "Case inventory differs"):
            self.checked_records()

    def test_fallback_cannot_hide_an_existing_slovene_page(self) -> None:
        self.write("docs/sl/case-studies/alpha.md", "# PREIZKUSNI PRIMER\n")
        with self.assertRaisesRegex(ValueError, "Case inventory differs"):
            self.checked_records()

    def test_slug_and_page_path_must_agree(self) -> None:
        damaged = {**self.record, "page_en": "docs/en/case-studies/renamed.md"}
        (self.root / self.record["page_en"]).rename(self.root / damaged["page_en"])
        with self.assertRaisesRegex(ValueError, "slug and page path disagree"):
            validate_records([damaged], self.root)

    def test_full_showcase_heading_and_metadata_contract_accepts_fixture(self) -> None:
        self.assertEqual(EVIDENCE_TYPES, TEST_EVIDENCE)
        self.assertEqual({locale: len(values) for locale, values in SHOWCASE_HEADINGS.items()}, {"en": 15, "sl": 15})
        self.write_fixture([case_record(paired=True, showcase=True)])
        self.checked_records()

    def test_showcase_sections_require_visible_content_not_empty_headings(self) -> None:
        record = case_record(paired=True, showcase=True)
        for locale, heading in (("en", "Where the workflow breaks"), ("sl", "Kje postopek odpove")):
            for decoy in ("", f"<!-- {TEST_SECTION} -->", f"```text\n{TEST_SECTION}\n```"):
                with self.subTest(locale=locale, decoy=decoy):
                    self.write_fixture([record])
                    metadata, body = frontmatter(self.root / record[f"page_{locale}"])
                    body = body.replace(f"## {heading}\n\n{TEST_SECTION}\n", f"## {heading}\n\n{decoy}\n")
                    self.write_page(record, locale, metadata=metadata, body=body)
                    with self.assertRaisesRegex(ValueError, "empty showcase-v1 section"):
                        self.checked_records()

    def test_showcase_evidence_table_requires_all_five_types_in_both_languages(self) -> None:
        record = case_record(paired=True, showcase=True)
        for locale in ("en", "sl"):
            for kind in TEST_EVIDENCE[locale]:
                with self.subTest(locale=locale, kind=kind):
                    self.write_fixture([record])
                    metadata, body = frontmatter(self.root / record[f"page_{locale}"])
                    row = f"| {kind} | TEST FIXTURE | Not inspected | No real evidence claimed |\n"
                    self.assertIn(row, body)
                    self.write_page(record, locale, metadata=metadata, body=body.replace(row, ""))
                    with self.assertRaisesRegex(ValueError, "missing evidence-table row"):
                        self.checked_records()

    def test_evidence_table_cells_cannot_be_empty(self) -> None:
        record = case_record(paired=True, showcase=True)
        self.write_fixture([record])
        metadata, body = frontmatter(self.root / record["page_en"])
        kind = TEST_EVIDENCE["en"][0]
        original = [kind, "TEST FIXTURE", "Not inspected", "No real evidence claimed"]
        for index in (1, 2, 3):
            with self.subTest(column=index):
                damaged = original.copy()
                damaged[index] = ""
                changed = body.replace("| " + " | ".join(original) + " |", "| " + " | ".join(damaged) + " |")
                self.write_page(record, "en", metadata=metadata, body=changed)
                with self.assertRaisesRegex(ValueError, "missing evidence-table row"):
                    self.checked_records()

    def test_showcase_requires_real_where_the_workflow_breaks_heading_in_both_languages(self) -> None:
        record = case_record(paired=True, showcase=True)
        for locale, heading in (("en", "Where the workflow breaks"), ("sl", "Kje postopek odpove")):
            for decoy in ("", f"```markdown\n## {heading}\n```", f"<!--\n## {heading}\n-->"):
                with self.subTest(locale=locale, decoy=decoy):
                    self.write_fixture([record])
                    metadata, body = frontmatter(self.root / record[f"page_{locale}"])
                    body = body.replace(f"## {heading}\n", "") + "\n\n" + decoy + "\n"
                    self.write_page(record, locale, metadata=metadata, body=body)
                    with self.assertRaisesRegex(ValueError, "missing showcase-v1 sections"):
                        self.checked_records()

    def test_heading_extractor_ignores_fenced_code_and_html_comments(self) -> None:
        self.assertEqual(headings("## Real section\n\n```markdown\n## Code decoy\n```\n\n"
                                  "<!--\n## Comment decoy\n-->\n\n"
                                  "<!-- <h2>Raw HTML comment decoy</h2> -->\n"), {"Real section"})

    def test_heading_extractor_accepts_visible_inline_formatting(self) -> None:
        self.assertEqual(headings("## Where the **workflow** breaks\n"), {"Where the workflow breaks"})

    def test_showcase_requires_explicit_matching_frontmatter_fields(self) -> None:
        record = case_record(paired=True, showcase=True)
        self.write_fixture([record])
        metadata, body = frontmatter(self.root / record["page_en"])
        for field in ("case_id", "content_standard", "translation_status", "audit_record"):
            with self.subTest(field=field):
                damaged = {key: value for key, value in metadata.items() if key != field}
                self.write_page(record, "en", metadata=damaged, body=body)
                with self.assertRaisesRegex(ValueError, "explicit matching page metadata"):
                    self.checked_records()

    def test_legacy_frontmatter_cannot_claim_v1_completion(self) -> None:
        metadata, body = frontmatter(self.root / self.record["page_en"])
        for change in ({"v1_complete": True}, {"content_standard": "showcase-v1"}):
            with self.subTest(change=change):
                self.write_page(self.record, "en", metadata={**metadata, **change}, body=body)
                with self.assertRaisesRegex(ValueError, "v1-complete|frontmatter content_standard drift"):
                    self.checked_records()

    def test_upgrading_metadata_and_frontmatter_does_not_make_legacy_body_v1_complete(self) -> None:
        legacy = case_record(paired=True)
        self.write_fixture([legacy])
        bodies = {locale: frontmatter(self.root / legacy[f"page_{locale}"])[1] for locale in ("en", "sl")}
        upgraded = {**legacy, "content_standard": "showcase-v1"}
        self.write_source([upgraded])
        for locale in ("en", "sl"):
            self.write_page(upgraded, locale, body=bodies[locale])
        with self.assertRaisesRegex(ValueError, "missing showcase-v1 sections"):
            self.checked_records()

    def test_frontmatter_title_and_identity_drift_is_rejected(self) -> None:
        metadata, body = frontmatter(self.root / self.record["page_en"])
        for field in ("title", "case_id", "translation_status", "audit_record"):
            with self.subTest(field=field):
                self.write_page(self.record, "en", metadata={**metadata, field: "incorrect"}, body=body)
                with self.assertRaisesRegex(ValueError, f"frontmatter {field} drift"):
                    self.checked_records()

    def test_missing_connections_require_a_substantive_note_present_in_the_audit(self) -> None:
        for field in CONNECTION_FIELDS:
            for note in (None, "TODO", "This remediation has enough words but is not in the audit."):
                with self.subTest(field=field, note=note):
                    record = {**self.record, field: [], "connection_remediation": note}
                    self.write_fixture([record])
                    audit = (self.root / "release/case-study-audit.md").read_text(encoding="utf-8")
                    if note:
                        audit = audit.replace(note, "")
                    self.write("release/case-study-audit.md", audit)
                    with self.assertRaisesRegex(ValueError, "explicit audited remediation"):
                        self.checked_records()

    def test_audited_connection_remediation_permits_legacy_gap_but_not_showcase(self) -> None:
        note = "TEST FIXTURE: select a relevant workflow after the evidence audit."
        legacy = {**self.record, "workflow_connections": [], "connection_remediation": note}
        self.write_fixture([legacy])
        self.checked_records()
        showcase = {**case_record(paired=True, showcase=True), "workflow_connections": [],
                    "connection_remediation": note}
        with self.assertRaisesRegex(ValueError, "JSON schema"):
            validate_schema([showcase], self.root)

    def test_resolved_connections_cannot_retain_stale_remediation(self) -> None:
        record = {**self.record, "connection_remediation": "TEST FIXTURE: this gap has already been resolved."}
        self.write_fixture([record])
        with self.assertRaisesRegex(ValueError, "stale connection remediation"):
            self.checked_records()

    def test_connection_targets_must_be_existing_local_pages(self) -> None:
        for field in CONNECTION_FIELDS:
            with self.subTest(field=field):
                self.write_fixture([self.record])
                (self.root / "docs/en" / self.record[field][0]).unlink()
                with self.assertRaisesRegex(ValueError, "Missing local page/file"):
                    self.checked_records()

    def test_connections_cannot_point_to_indexes_or_noncore_chapters(self) -> None:
        for field, target, error in (("chapter_connections", "chapters/index.md", "core chapter"),
                                     ("chapter_connections", "chapters/invented-noncore.md", "core chapter"),
                                     ("workflow_connections", "workflows/test/index.md", "workflow, not an index")):
            with self.subTest(field=field, target=target):
                record = {**self.record, field: [target]}
                self.write_fixture([record])
                with self.assertRaisesRegex(ValueError, error):
                    self.checked_records()

    def test_connections_cannot_be_authored_in_case_metadata_even_when_empty(self) -> None:
        for field in CONNECTION_FIELDS:
            for value in ([], self.record[field]):
                with self.subTest(field=field, value=value):
                    authored = {key: item for key, item in self.record.items() if key not in CONNECTION_FIELDS}
                    authored[field] = value
                    self.write_yaml(SOURCE, {"schema_version": 2, "cases": [authored]})
                    with self.assertRaisesRegex(ValueError, "Author connections only in intertextuality"):
                        load_records(self.root)

    def test_derived_connections_cannot_disagree_with_the_authoritative_map(self) -> None:
        damaged = {**self.record, "chapter_connections": ["chapters/another-concept.md"]}
        with self.assertRaisesRegex(ValueError, "connections differ from authoritative"):
            validate_records([damaged], self.root)

    def test_duplicate_yaml_keys_are_rejected_at_root_and_record_depth(self) -> None:
        original = (self.root / SOURCE).read_text(encoding="utf-8")
        for text in ("schema_version: 2\n" + original,
                     original.replace("  slug: alpha\n", "  slug: alpha\n  slug: beta\n")):
            with self.subTest(text=text):
                self.write(SOURCE, text)
                with self.assertRaisesRegex(ValueError, "Duplicate YAML key"):
                    load_records(self.root)

    def test_duplicate_yaml_keys_in_map_and_frontmatter_are_rejected(self) -> None:
        self.write("intertextuality.yml", "case_studies: {}\ncase_studies: {}\n")
        with self.assertRaisesRegex(ValueError, "Duplicate YAML key"):
            load_records(self.root)
        self.write_fixture([self.record])
        page = (self.root / self.record["page_en"]).read_text(encoding="utf-8")
        self.write(self.record["page_en"], page.replace("---\n", "---\ntitle: duplicate\n", 1))
        with self.assertRaisesRegex(ValueError, "Duplicate YAML key"):
            self.checked_records()

    def test_source_version_and_root_shape_cannot_be_ambiguous(self) -> None:
        for source in ({"schema_version": True, "cases": []}, {"schema_version": "2", "cases": []},
                       {"schema_version": 1, "cases": []}, {"schema_version": 2, "cases": [], "extra": 1}):
            with self.subTest(source=source):
                self.write_yaml(SOURCE, source)
                with self.assertRaisesRegex(ValueError, "schema_version: 2 and cases only"):
                    load_records(self.root)

    def test_completed_translation_review_accepts_only_explicit_fixture_metadata(self) -> None:
        record = {**case_record(paired=True), "translation_status": "paired-human-reviewed"}
        self.write_fixture([record])
        metadata, body = frontmatter(self.root / record["page_sl"])
        self.write_page(record, "sl", metadata={**metadata, **TEST_REVIEW}, body=body)
        self.checked_records()

    def test_completed_translation_review_rejects_null_and_placeholder_fields(self) -> None:
        record = {**case_record(paired=True), "translation_status": "paired-human-reviewed"}
        self.write_fixture([record])
        metadata, body = frontmatter(self.root / record["page_sl"])
        for field in TEST_REVIEW:
            for invalid in (None, "", "pending", "unknown", "TBD", "null", "v čakanju", "dopolnite"):
                with self.subTest(field=field, value=invalid):
                    damaged = {**metadata, **TEST_REVIEW, field: invalid}
                    self.write_page(record, "sl", metadata=damaged, body=body)
                    with self.assertRaises(ValueError):
                        self.checked_records()

    def test_completed_translation_review_requires_a_valid_date_and_substantive_scope(self) -> None:
        record = {**case_record(paired=True), "translation_status": "paired-human-reviewed"}
        self.write_fixture([record])
        metadata, body = frontmatter(self.root / record["page_sl"])
        for change in ({"translation_reviewed_on": "2000-02-30"}, {"translation_reviewed_on": "20000115"},
                       {"translation_review_scope": "Reviewed"}, {"translation_reviewed_by": "human reviewer"}):
            with self.subTest(change=change):
                self.write_page(record, "sl", metadata={**metadata, **TEST_REVIEW, **change}, body=body)
                with self.assertRaises(ValueError):
                    self.checked_records()

    def test_paired_draft_requires_a_visible_language_review_notice(self) -> None:
        record = case_record(paired=True)
        self.write_fixture([record])
        self.write_page(record, "sl", body="# PREIZKUSNI PRIMER\n\nBrez obvestila.\n")
        with self.assertRaisesRegex(ValueError, "visible language-review status"):
            self.checked_records()

    def test_language_review_notice_hidden_in_code_or_comment_does_not_count(self) -> None:
        record = case_record(paired=True)
        self.write_fixture([record])
        notice = "Strojno podprti osnutek; potreben je človeški jezikovni pregled."
        for hidden in (f"<!-- {notice} -->", f"```text\n{notice}\n```", f"<code>{notice}</code>"):
            with self.subTest(hidden=hidden):
                self.write_page(record, "sl", body=f"# PREIZKUSNI PRIMER\n\n{hidden}\n")
                with self.assertRaisesRegex(ValueError, "visible language-review status"):
                    self.checked_records()

    def test_fallback_cards_are_labelled_and_not_counted_as_slovene_case_pages(self) -> None:
        records = self.checked_records()
        definitions = schema(self.root)["$defs"]
        slovene = catalogue(records, "sl", definitions)
        english = catalogue(records, "en", definitions)
        self.assertIn("0 slovenskih strani; 1 angleških nadomestnih strani", slovene)
        self.assertIn("0 Slovene pages; 1 English fallbacks", english)
        self.assertIn("](" + Path(self.record["page_en"]).name + ") — angleška nadomestna stran", slovene)
        self.assertIn(definitions["translation_status"]["x-labels"]["english-fallback"]["sl"], slovene)
        self.assertIsNone(json.loads(generated(records, self.root)[INDEX])[0]["page_sl"])

    def test_paired_and_fallback_counts_do_not_conflate_catalogue_translation_with_case_translation(self) -> None:
        self.write_fixture([self.record, case_record("beta", paired=True)])
        slovene = catalogue(self.checked_records(), "sl", schema(self.root)["$defs"])
        self.assertIn("2 primerov; 2 angleških strani; 1 slovenskih strani; 1 angleških nadomestnih strani", slovene)

    def test_slovene_only_page_has_an_explicit_cross_language_target(self) -> None:
        record = {**case_record(paired=True), "translation_status": "slovene-only",
                  "page_en": None, "title_en": None, "short_summary_en": None}
        (self.root / self.record["page_en"]).unlink()
        self.write_fixture([record])
        records = self.checked_records()
        definitions = schema(self.root)["$defs"]
        english = catalogue(records, "en", definitions)
        slovene = catalogue(records, "sl", definitions)
        self.assertIn("https://damjan-popic.github.io/digital-humanities-handbook/sl/case-studies/alpha/", english)
        self.assertIn(" — Slovene-only page", english)
        self.assertIn("0 English pages; 1 Slovene pages; 0 English fallbacks", english)
        self.assertNotIn(" — angleška nadomestna stran", slovene)

    def test_case_without_a_page_links_to_its_audit_without_a_false_language_fallback(self) -> None:
        record = {**self.record, "translation_status": "not-applicable", "content_standard": "deferred",
                  "editorial_disposition": "defer", "page_en": None, "title_en": None, "short_summary_en": None}
        (self.root / self.record["page_en"]).unlink()
        self.write_fixture([record])
        for locale in ("en", "sl"):
            with self.subTest(locale=locale):
                rendered = catalogue(self.checked_records(), locale, schema(self.root)["$defs"])
                self.assertIn("[CASE-alpha](https://github.com/damjan-popic/digital-humanities-handbook/blob/main/"
                              + record["audit_record"] + ")", rendered)
                self.assertNotIn(" — Slovene-only page", rendered)
                self.assertNotIn(" — angleška nadomestna stran", rendered)

    def test_archived_unavailable_and_deferred_cases_remain_visible_with_status(self) -> None:
        records = []
        for state in ("archived", "unavailable", "deferred"):
            record = {**case_record(state), "lifecycle_status": state if state != "deferred" else "maintenance-unclear"}
            if state == "deferred":
                record.update(page_en=None, title_en=None, short_summary_en=None,
                              translation_status="not-applicable", content_standard="deferred",
                              editorial_disposition="defer")
            records.append(record)
        # Remove the initial default page: this fixture intentionally has a new inventory.
        (self.root / self.record["page_en"]).unlink()
        self.write_fixture(records)
        definitions = schema(self.root)["$defs"]
        checked = self.checked_records()
        self.assertEqual(len(checked), 3)
        for locale in ("en", "sl"):
            rendered = catalogue(checked, locale, definitions)
            for record in records:
                with self.subTest(locale=locale, state=record["lifecycle_status"]):
                    self.assertIn(definitions["lifecycle_status"]["x-labels"][record["lifecycle_status"]][locale], rendered)
                    self.assertIn(definitions["editorial_disposition"]["x-labels"][record["editorial_disposition"]][locale], rendered)
                    self.assertIn(record["audit_record"], rendered)
            self.assertIn("CASE-deferred", rendered)

    def test_generated_json_and_both_catalogues_are_checked_for_missing_or_changed_bytes(self) -> None:
        records = self.checked_records()
        outputs = self.write_generated(records)
        check_generated(records, self.root)
        for relative, expected in outputs.items():
            with self.subTest(path=relative, kind="missing"):
                (self.root / relative).unlink()
                with self.assertRaisesRegex(ValueError, "Metadata/catalogue drift"):
                    check_generated(records, self.root)
                self.write(relative, expected)
            with self.subTest(path=relative, kind="changed"):
                self.write(relative, expected + "\n")
                with self.assertRaisesRegex(ValueError, "Metadata/catalogue drift"):
                    check_generated(records, self.root)
                self.write(relative, expected)

    def test_source_metadata_change_requires_regenerating_all_outputs(self) -> None:
        records = self.checked_records()
        self.write_generated(records)
        self.record["short_summary_en"] = "Changed TEST FIXTURE summary, still not real evidence."
        self.write_source([self.record])
        with self.assertRaisesRegex(ValueError, "Metadata/catalogue drift"):
            check_generated(self.checked_records(), self.root)

    def test_author_order_and_set_like_facet_order_do_not_change_generated_bytes(self) -> None:
        first = copy.deepcopy(self.record)
        first.update(method_domains=["text-analysis", "data-modelling"],
                     source_types=["historical-documents", "corpus-text"],
                     languages_regions=["slovene", "slovenia"],
                     inspection_modes=["repository-inspected", "documentation-inspected"])
        second = case_record("beta")
        self.write_fixture([second, first])
        expected = generated(self.checked_records(), self.root)
        for field in ("method_domains", "source_types", "languages_regions", "inspection_modes"):
            first[field].reverse()
        self.write_fixture([first, second])
        checked = self.checked_records()
        self.assertEqual([record["case_id"] for record in checked], ["CASE-alpha", "CASE-beta"])
        self.assertEqual(generated(checked, self.root), expected)

    def test_component_order_and_nested_key_order_do_not_change_generated_bytes(self) -> None:
        expected = generated(self.checked_records(), self.root)
        reordered = dict(reversed(list(copy.deepcopy(self.record).items())))
        reordered["rights_components"] = [dict(reversed(list(component.items())))
                                           for component in reversed(reordered["rights_components"])]
        self.write_fixture([reordered])
        checked = self.checked_records()
        self.assertEqual(generated(checked, self.root), expected)
        # Direct callers receive the same canonicalization as authored YAML loads.
        self.assertEqual(generated([reordered], self.root), expected)
        exported = json.loads(expected[INDEX])[0]
        self.assertEqual([item["component"] for item in exported["rights_components"]], list(TEST_COMPONENTS))
        for component in exported["rights_components"]:
            self.assertEqual(list(component), ["component", "status", "licence_or_terms", "scope_note", "audit_locator"])

    def test_nested_rights_yaml_cannot_repeat_a_key(self) -> None:
        original = (self.root / SOURCE).read_text(encoding="utf-8")
        self.assertIn("    status: unknown\n", original)
        self.write(SOURCE, original.replace("    status: unknown\n", "    status: unknown\n    status: project-declared\n", 1))
        with self.assertRaisesRegex(ValueError, "Duplicate YAML key"):
            load_records(self.root)

    def test_relation_order_is_preserved_from_the_single_authoritative_map(self) -> None:
        record = {**self.record, "chapter_connections": ["chapters/" + CHAPTERS[1], "chapters/" + CHAPTERS[0]]}
        self.write_fixture([record])
        self.assertEqual(self.checked_records()[0]["chapter_connections"], record["chapter_connections"])

    def test_outputs_are_utf8_lf_deterministic_and_crlf_drift_is_rejected(self) -> None:
        records = self.checked_records()
        outputs = self.write_generated(records)
        self.assertEqual(outputs, generated(records, self.root))
        for relative, text in outputs.items():
            with self.subTest(path=relative):
                self.assertTrue(text.endswith("\n"))
                self.assertNotIn("\r", text)
                self.assertEqual((self.root / relative).read_bytes(), text.encode("utf-8"))
                (self.root / relative).write_bytes(text.replace("\n", "\r\n").encode("utf-8"))
                with self.assertRaisesRegex(ValueError, "Metadata/catalogue drift"):
                    check_generated(records, self.root)
                self.write(relative, text)

    def test_validation_and_generation_have_no_network_dependency(self) -> None:
        forbidden = AssertionError("Network access is forbidden in case-study regression fixtures")
        with mock.patch("socket.socket", side_effect=forbidden), \
                mock.patch("socket.create_connection", side_effect=forbidden), \
                mock.patch("socket.getaddrinfo", side_effect=forbidden), \
                mock.patch("urllib.request.urlopen", side_effect=forbidden):
            records = self.checked_records()
            self.write_generated(records)
            check_generated(records, self.root)


if __name__ == "__main__":
    unittest.main()
