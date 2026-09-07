#!/usr/bin/env python3
"""Regression checks for consequential omissions in the teaching records."""
from __future__ import annotations

import copy
import unittest

from check_ai_publication import RECORDS, ROOT, record_from_markdown, structure, validate_record


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


if __name__ == "__main__":
    unittest.main()
