#!/usr/bin/env python3
"""Validate the paired archival-friction route required by issue #23."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
import unicodedata
from decimal import Decimal, ROUND_HALF_EVEN
from pathlib import Path
from zipfile import ZipFile

import yaml

from scholarly_work_package_utils import FIXED_ZIP_DATE


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "teaching-data" / "archival-friction"
ARCHIVE = ROOT / "docs/assets/downloads/archival-friction-v1.zip"
DIGEST = ARCHIVE.with_suffix(ARCHIVE.suffix + ".sha256")
ARCHIVE_PREFIX = "archival-friction-v1/"
PDF_SHA256 = "e7b4b9f27f2043f2a3861b6cf05e1b4d8e1053e16eb81bf05f96d21385b5ad79"
PROVIDER_EXPORT_SHA256 = "ab4e9e5464eb349d4c27b3b895c2b98b3a6509f3ce4be76f387b739a1fcee456"
SOURCE_TREE_URL = (
    "https://github.com/damjan-popic/digital-humanities-handbook/"
    "tree/main/teaching-data/archival-friction"
)
DOCUMENT_PAIRS = (
    ("README.md", "README.sl.md"),
    ("rights-and-provenance.md", "rights-and-provenance.sl.md"),
    ("SOURCE_CITATION.md", "SOURCE_CITATION.sl.md"),
    ("data-dictionary.md", "data-dictionary.sl.md"),
    ("expected-observations.md", "expected-observations.sl.md"),
    ("known-problems/README.md", "known-problems/README.sl.md"),
    ("RIGHTS.md", "RIGHTS.sl.md"),
    ("reference/transcription-policy.md", "reference/transcription-policy.sl.md"),
)
REQUIRED_PACKET_FILES = {
    name for pair in DOCUMENT_PAIRS for name in pair
} | {
    "metadata-raw.csv",
    "metadata-clean.csv",
    "correction-log.csv",
    "unresolved-cases.csv",
    "source/commons-source.json",
    "source/dlib-source.json",
    "source/ilustrirani-slovenec-1925-02-07.pdf",
    "source/provider-ocr.txt",
    "reference/observations.csv",
    "reference/editorial-decisions.csv",
    "reference/reference-transcription.txt",
    "teaching/synthetic-perturbations.csv",
    "raw/messy-records.csv",
    "raw/provider-ocr.txt",
    "interim/reconciliation-candidates.csv",
    "cleaned/records.csv",
    "cleaned/reference-transcription.txt",
    "cleaned/decisions.csv",
    "output/ocr-evaluation.csv",
    "output/ocr-error-audit.csv",
    "output/record-summary.csv",
    "validation/expected-results.json",
    "validation/SHA256SUMS.txt",
}
WORKFLOWS = (
    "workflows/data-wrangling/turn-messy-humanities-notes-into-a-reusable-dataset.md",
    "workflows/data-wrangling/reconcile-conflicting-metadata-without-erasing-uncertainty.md",
    "workflows/pdf/evaluate-ocr-or-htr-against-a-reference-sample.md",
)
CHAPTERS = (
    "chapters/research-design.md",
    "chapters/data-metadata-models.md",
    "chapters/texts-corpora-ocr.md",
)
DOWNLOAD_LINK_PAGES = (
    "foundations/scholarly-work.md",
    "learning-paths/pismenost-za-informacijsko-druzbo.md",
    *WORKFLOWS,
    *CHAPTERS,
)
AUTHORITY_STATUSES = {
    "not_attempted",
    "not_reconciled",
    "candidate_rejected",
    "accepted",
    "unresolved",
    "not_applicable",
}
OBSERVATION_FIELDS = {
    "record_id",
    "record_kind",
    "page",
    "label_transcribed",
    "label_provider_ocr",
    "date_scope",
    "printed_date",
    "date_normalized",
    "date_status",
    "issue_context_date",
    "printed_person_or_group",
    "entity_structure",
    "authority_candidate",
    "authority_link_status",
    "authority_evidence",
    "source_locator",
    "evidence_note",
    "synthetic",
}


def fail(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def rows(relative: str) -> list[dict[str, str]]:
    with (PACKET / relative).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def expected_provider_excerpt() -> str:
    source_lines = (PACKET / "source/provider-ocr.txt").read_bytes().decode(
        "windows-1250"
    ).splitlines()
    if len(source_lines) < 4:
        return ""
    selected_lines = (
        f"{source_lines[0]} {source_lines[1]}",
        source_lines[2],
        source_lines[3],
    )
    return "\n".join(
        " ".join(unicodedata.normalize("NFC", line).split())
        for line in selected_lines
    )


def unique_ids(
    records: list[dict[str, str]], field: str, label: str, failures: list[str]
) -> set[str]:
    values = [row.get(field, "") for row in records]
    fail(all(values), f"{label}: blank {field}", failures)
    fail(len(values) == len(set(values)), f"{label}: duplicate {field}", failures)
    return set(values)


def check_bilingual_packet_docs(failures: list[str]) -> None:
    shared_tokens = {
        "README.md": {
            "source/",
            "reference/",
            "teaching/",
            "raw/",
            "interim/",
            "cleaned/",
            "output/",
            "validation/",
            "known-problems/",
            "entity_structure",
            "authority_candidate",
            "authority_link_status",
        },
        "rights-and-provenance.md": {
            PDF_SHA256,
            PROVIDER_EXPORT_SHA256,
            "URN:NBN:SI:doc-YPI8OFSU",
            "source/dlib-source.json",
            "source/commons-source.json",
            "CC BY 4.0",
            "MIT",
            "v1.0",
            "AF-SYN-001",
            "AF-SYN-004",
        },
        "SOURCE_CITATION.md": {
            "URN:NBN:SI:doc-YPI8OFSU",
            "reference/observations.csv",
            "teaching/synthetic-perturbations.csv",
        },
        "data-dictionary.md": OBSERVATION_FIELDS
        | AUTHORITY_STATUSES
        | {
            "zero_people",
            "one_person",
            "multiple_people",
            "exact",
            "derived_from_relative_date",
            "unknown",
            "not_applicable",
            "output/ocr-evaluation.csv",
            "output/ocr-error-audit.csv",
            "output/record-summary.csv",
        },
        "expected-observations.md": {
            "date_normalized",
            "date_status",
            "unknown",
            "issue_context_date",
            "multiple_people",
            "candidate_rejected",
            "correction-log.csv",
            "output/record-summary.csv",
        },
        "known-problems/README.md": {
            "AF-P1-002",
            "AF-P2-001",
            "AF-P2-003",
        },
        "RIGHTS.md": {"rights-and-provenance.md", "rights-and-provenance.sl.md"},
        "reference/transcription-policy.md": {
            "source/provider-ocr.txt",
            "raw/provider-ocr.txt",
            "reference/reference-transcription.txt",
        },
    }
    for english, slovene in DOCUMENT_PAIRS:
        english_path = PACKET / english
        slovene_path = PACKET / slovene
        fail(english_path.exists(), f"missing English packet document: {english}", failures)
        fail(slovene_path.exists(), f"missing Slovene packet document: {slovene}", failures)
        if not english_path.exists() or not slovene_path.exists():
            continue
        english_text = english_path.read_text(encoding="utf-8")
        slovene_text = slovene_path.read_text(encoding="utf-8")
        fail(len(english_text.split()) >= 20, f"packet document is unexpectedly short: {english}", failures)
        fail(len(slovene_text.split()) >= 20, f"packet document is unexpectedly short: {slovene}", failures)
        for token in sorted(shared_tokens[english]):
            fail(token in english_text, f"{english}: missing paired concept {token!r}", failures)
            fail(token in slovene_text, f"{slovene}: missing paired concept {token!r}", failures)


def check_manifest(failures: list[str]) -> None:
    path = PACKET / "validation/SHA256SUMS.txt"
    if not path.exists():
        return
    listed: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            digest, relative = line.split("  ", 1)
        except ValueError:
            failures.append("validation/SHA256SUMS.txt: malformed line")
            continue
        listed[relative] = digest
    actual = {
        path.relative_to(PACKET).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in PACKET.rglob("*")
        if path.is_file() and path.name != "SHA256SUMS.txt"
    }
    fail(set(listed) == set(actual), "packet manifest member list is stale", failures)
    for relative in sorted(set(listed) & set(actual)):
        fail(listed[relative] == actual[relative], f"packet manifest digest mismatch: {relative}", failures)


def check_archive(failures: list[str]) -> None:
    fail(ARCHIVE.exists(), "missing archival-friction-v1.zip", failures)
    fail(DIGEST.exists(), "missing archival-friction-v1.zip.sha256", failures)
    if not ARCHIVE.exists() or not DIGEST.exists():
        return
    digest = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
    fail(
        DIGEST.read_text(encoding="utf-8") == f"{digest}  {ARCHIVE.name}\n",
        "download SHA-256 file is stale",
        failures,
    )
    packet_files = {
        path.relative_to(PACKET).as_posix(): path
        for path in PACKET.rglob("*")
        if path.is_file()
    }
    with ZipFile(ARCHIVE) as archive:
        infos = archive.infolist()
        names = {info.filename for info in infos}
        expected_names = {ARCHIVE_PREFIX + relative for relative in packet_files}
        fail(names == expected_names, "download member list differs from the packet", failures)
        fail(all(info.date_time == FIXED_ZIP_DATE for info in infos), "download timestamps are not deterministic", failures)
        for relative, path in packet_files.items():
            name = ARCHIVE_PREFIX + relative
            if name in names:
                fail(archive.read(name) == path.read_bytes(), f"download member differs: {relative}", failures)


def check_source_and_rights(failures: list[str]) -> None:
    source_files = {
        path.relative_to(PACKET / "source").as_posix()
        for path in (PACKET / "source").rglob("*")
        if path.is_file()
    }
    fail(
        source_files
        == {
            "commons-source.json",
            "dlib-source.json",
            "ilustrirani-slovenec-1925-02-07.pdf",
            "provider-ocr.txt",
        },
        "source/ must contain only preserved provider material and captured records",
        failures,
    )
    pdf = PACKET / "source/ilustrirani-slovenec-1925-02-07.pdf"
    fail(hashlib.sha256(pdf.read_bytes()).hexdigest() == PDF_SHA256, "source PDF digest changed", failures)
    dlib = json.loads((PACKET / "source/dlib-source.json").read_text(encoding="utf-8"))
    commons = json.loads((PACKET / "source/commons-source.json").read_text(encoding="utf-8"))
    fail(dlib.get("stable_urn") == "URN:NBN:SI:doc-YPI8OFSU", "dLib URN is missing", failures)
    fail("NUK" in dlib.get("provider", ""), "dLib record does not name NUK", failures)
    fail(dlib.get("availability_at_access") == {"pdf": True, "txt": True}, "dLib PDF/TXT availability is stale", failures)
    fail(dlib.get("displayed_pdf_size_kb") == 1185 and dlib.get("displayed_txt_size_kb") == 7, "dLib displayed file sizes are stale", failures)
    fail(dlib.get("displayed_rights_field") == "blank", "dLib rights-field audit is stale", failures)
    provider_export = PACKET / "source/provider-ocr.txt"
    export_capture = dlib.get("txt_export_capture", {})
    fail(hashlib.sha256(provider_export.read_bytes()).hexdigest() == PROVIDER_EXPORT_SHA256, "preserved dLib TXT export digest changed", failures)
    fail(export_capture.get("sha256") == PROVIDER_EXPORT_SHA256, "dLib TXT capture digest is stale", failures)
    fail(export_capture.get("byte_size") == provider_export.stat().st_size == 5710, "dLib TXT capture byte size is stale", failures)
    fail(export_capture.get("decoding_used") == "Windows-1250", "dLib TXT decoding record is stale", failures)
    fail(export_capture.get("line_endings") == "CRLF", "dLib TXT line-ending record is stale", failures)
    fail(export_capture.get("content_type_header") == "text/plain", "dLib TXT content type is stale", failures)
    expected_excerpt = expected_provider_excerpt()
    fail(bool(expected_excerpt), "dLib TXT export cannot supply the declared four-line selection", failures)
    fail(
        (PACKET / "raw/provider-ocr.txt").read_bytes()
        == (expected_excerpt + "\n").encode("utf-8"),
        "raw provider excerpt does not match the declared extraction and whitespace normalization",
        failures,
    )
    fail(commons.get("rights_label_applied_by") == "Wikimedia Commons file page", "Commons rights attribution is unclear", failures)
    fail(commons.get("provider_credit") == "Digital Library of Slovenia", "Commons-to-dLib source credit is missing", failures)
    fail("United States public domain tag" in commons.get("us_public_domain_tag_notice", ""), "Commons US-tag notice is missing", failures)


def check_records_and_decisions(failures: list[str]) -> None:
    reference = rows("reference/observations.csv")
    raw = rows("metadata-raw.csv")
    clean = rows("metadata-clean.csv")
    perturbations = rows("teaching/synthetic-perturbations.csv")
    decisions = rows("correction-log.csv")
    unresolved = rows("unresolved-cases.csv")
    candidates = rows("interim/reconciliation-candidates.csv")

    reference_ids = unique_ids(reference, "record_id", "reference observations", failures)
    raw_ids = unique_ids(raw, "record_id", "raw rows", failures)
    clean_ids = unique_ids(clean, "record_id", "clean rows", failures)
    perturbation_ids = unique_ids(perturbations, "perturbation_id", "perturbations", failures)
    decision_ids = unique_ids(decisions, "decision_id", "decisions", failures)
    candidate_ids = unique_ids(candidates, "candidate_id", "interim candidates", failures)
    unresolved_ids = unique_ids(unresolved, "case_id", "unresolved cases", failures)

    fail(bool(reference) and set(reference[0]) == OBSERVATION_FIELDS, "observation schema is stale", failures)
    fail(len(reference) == 8, "expected eight handbook reference observations", failures)
    fail(sum(row["record_kind"] == "issue" for row in reference) == 1, "expected one issue observation", failures)
    fail(sum(row["record_kind"] != "issue" for row in reference) == 7, "expected seven feature observations", failures)
    fail(len(raw) == 9, "raw table must contain nine rows", failures)
    fail(len(clean) == 8, "clean table must contain eight observations", failures)
    fail(reference_ids == clean_ids, "clean IDs differ from reference observation IDs", failures)
    fail(reference_ids < raw_ids, "raw IDs must contain all reference IDs plus a synthetic duplicate", failures)
    fail(raw_ids - reference_ids == {"AF-P1-002-DUP"}, "unexpected extra raw record IDs", failures)
    fail(perturbation_ids == {f"AF-SYN-{number:03d}" for number in range(1, 5)}, "expected four stable synthetic perturbations", failures)
    fail(candidate_ids == perturbation_ids, "interim candidate IDs differ from perturbations", failures)
    fail(unresolved_ids == {"AF-U-001", "AF-U-002"}, "expected two field-specific unresolved cases", failures)
    fail(all(row["synthetic"] == "false" for row in reference), "reference observations contain synthetic rows", failures)
    fail(all(row["synthetic"] == "false" for row in clean), "clean observations contain synthetic rows", failures)
    fail((PACKET / "metadata-raw.csv").read_bytes() == (PACKET / "raw/messy-records.csv").read_bytes(), "top-level and layered raw metadata differ", failures)
    fail((PACKET / "metadata-clean.csv").read_bytes() == (PACKET / "cleaned/records.csv").read_bytes(), "top-level and layered clean metadata differ", failures)
    fail((PACKET / "correction-log.csv").read_bytes() == (PACKET / "cleaned/decisions.csv").read_bytes(), "decision copies differ", failures)
    fail((PACKET / "reference/reference-transcription.txt").read_bytes() == (PACKET / "cleaned/reference-transcription.txt").read_bytes(), "reference-transcription copies differ", failures)

    by_id = {row["record_id"]: row for row in clean}
    riverbed = by_id["AF-P1-002"]
    fail(riverbed["date_scope"] == "photograph_creation", "AF-P1-002 date scope is stale", failures)
    fail(riverbed["date_normalized"] == "", "AF-P1-002 must have no normalized creation date", failures)
    fail(riverbed["date_status"] == "unknown", "AF-P1-002 creation-date status must be unknown", failures)
    fail(riverbed["issue_context_date"] == "1925-02-07", "AF-P1-002 issue context is missing", failures)
    source_grounded_decisions = [
        row for row in decisions if row["synthetic"] == "false"
    ]
    for row in clean:
        inherited = (
            row["record_kind"] != "issue"
            and not row["printed_date"]
            and row["date_normalized"]
            and row["date_normalized"] == row["issue_context_date"]
        )
        explicit_rule = any(
            decision["record_id"] == row["record_id"]
            and decision["field"] == "date_normalized"
            and decision["action"] == "derive_undated_feature_date_from_evidence"
            for decision in source_grounded_decisions
        )
        fail(not inherited or explicit_rule, f"{row['record_id']} inherits issue date without an evidential rule", failures)

    fail({row["authority_link_status"] for row in clean} <= AUTHORITY_STATUSES, "unknown authority-link status", failures)
    fail({row["entity_structure"] for row in clean} <= {"zero_people", "one_person", "multiple_people"}, "unknown entity structure", failures)
    fail(by_id["AF-P2-001"]["entity_structure"] == "multiple_people", "group portrait is not modelled as multiple people", failures)
    fail(by_id["AF-P2-003"]["printed_person_or_group"] == "Mr. Meker", "printed Meker form was not retained", failures)
    fail(by_id["AF-P2-003"]["authority_link_status"] == "candidate_rejected", "Meker authority candidate must remain rejected", failures)
    for row in clean:
        if row["authority_link_status"] == "accepted":
            supported = bool(row["authority_candidate"] and row["authority_evidence"]) and any(
                decision["record_id"] == row["record_id"]
                and decision["field"] == "authority_link_status"
                and decision["result_value"] == "accepted"
                and decision["evidence"]
                and decision["synthetic"] == "false"
                for decision in decisions
            )
            fail(supported, f"{row['record_id']} accepts an authority candidate without evidence", failures)

    unresolved_by_id = {row["case_id"]: row for row in unresolved}
    fail(unresolved_by_id["AF-U-001"]["field"] == "creation_date", "AF-U-001 references the wrong field", failures)
    fail(unresolved_by_id["AF-U-002"]["field"] == "authority_link", "AF-U-002 references the wrong field", failures)
    for case in unresolved:
        record = by_id.get(case["record_id"])
        fail(record is not None, f"{case['case_id']} references a missing record", failures)
        if record is None:
            continue
        fail(bool(case["current_evidence"] and case["reason"] and case["evidence_needed"]), f"{case['case_id']} lacks field-specific evidence", failures)
        if case["field"] == "creation_date":
            fail(record["date_status"] == "unknown", f"{case['case_id']} does not match date status", failures)
        elif case["field"] == "authority_link":
            fail(not re.search(r"\bdate\b", case["reason"].lower()), f"{case['case_id']} attaches a date reason to authority work", failures)
            fail(record["entity_structure"] == "one_person", f"{case['case_id']} treats a non-person or group as one unresolved identity", failures)
            fail(record["authority_link_status"] in {"candidate_rejected", "unresolved"}, f"{case['case_id']} does not match authority status", failures)
        else:
            failures.append(f"{case['case_id']} references unsupported unresolved field {case['field']!r}")
        fail(not (record["entity_structure"] == "multiple_people" and case["field"] == "authority_link"), f"{case['case_id']} counts multiple_people as one unresolved identity", failures)

    required_decision_fields = {
        "decision_id",
        "record_id",
        "field",
        "input_value",
        "result_value",
        "action",
        "source_locator",
        "evidence",
        "responsible_process",
        "decision_date",
        "rule_version",
        "confidence",
        "reversible",
        "synthetic",
    }
    fail(bool(decisions) and set(decisions[0]) == required_decision_fields, "decision log schema is incomplete", failures)
    fail(len(source_grounded_decisions) == 9, "expected nine source-grounded editorial decisions", failures)
    fail(
        {row["decision_id"] for row in source_grounded_decisions}
        == {f"AF-ED-{number:03d}" for number in range(1, 10)},
        "source-grounded editorial decision IDs are incomplete",
        failures,
    )
    fail({row["decision_id"] for row in decisions if row["synthetic"] == "true"} == perturbation_ids, "synthetic decision IDs differ from perturbations", failures)
    fail(all(row["source_locator"] and row["evidence"] and row["responsible_process"] and row["decision_date"] and row["rule_version"] and row["confidence"] and row["reversible"] for row in decisions), "a decision lacks required provenance", failures)
    fail(all(row["action"] != "restore_from_facsimile_or_leave_unresolved" for row in decisions), "generic decision action remains", failures)
    required_actions = {
        "derive_relative_date",
        "correct_provider_ocr_from_facsimile",
        "retain_printed_form",
        "reject_authority_candidate",
        "model_group_as_multiple_people",
        "leave_creation_date_unknown",
        "select_decode_and_normalize_provider_excerpt",
    }
    fail(
        required_actions <= {row["action"] for row in source_grounded_decisions},
        "source-grounded editorial action inventory is incomplete",
        failures,
    )

    observation_decisions = [
        row for row in source_grounded_decisions if row["field"] in OBSERVATION_FIELDS
    ]
    for decision in observation_decisions:
        observation = by_id.get(decision["record_id"])
        fail(
            observation is not None,
            f"{decision['decision_id']} targets a missing cleaned observation",
            failures,
        )
        if observation is not None:
            fail(
                decision["result_value"] == observation[decision["field"]],
                f"{decision['decision_id']} result does not match cleaned {decision['field']}",
                failures,
            )

    transcription_decisions = [
        row
        for row in source_grounded_decisions
        if row["field"] == "reference_transcription"
    ]
    fail(
        {row["decision_id"] for row in transcription_decisions}
        == {"AF-ED-003", "AF-ED-004"},
        "reference-transcription decisions are incomplete",
        failures,
    )
    provider_excerpt = (PACKET / "raw/provider-ocr.txt").read_text(encoding="utf-8")
    reference_transcription = (
        PACKET / "reference/reference-transcription.txt"
    ).read_text(encoding="utf-8")
    for decision in transcription_decisions:
        fail(
            decision["input_value"] in provider_excerpt,
            f"{decision['decision_id']} input is absent from the normalized provider excerpt",
            failures,
        )
        fail(
            decision["result_value"] in reference_transcription,
            f"{decision['decision_id']} result is absent from the reference transcription",
            failures,
        )

    extraction_decisions = [
        row for row in source_grounded_decisions if row["field"] == "raw_provider_ocr"
    ]
    fail(
        len(extraction_decisions) == 1
        and extraction_decisions[0]["decision_id"] == "AF-ED-009"
        and extraction_decisions[0]["input_value"] == "source/provider-ocr.txt"
        and extraction_decisions[0]["result_value"] == "raw/provider-ocr.txt",
        "provider-excerpt extraction decision is missing or inconsistent",
        failures,
    )
    known_decision_fields = OBSERVATION_FIELDS | {
        "reference_transcription",
        "raw_provider_ocr",
    }
    fail(
        all(row["field"] in known_decision_fields for row in source_grounded_decisions),
        "a source-grounded decision targets an unsupported field",
        failures,
    )

    authority_decision = next(
        (row for row in source_grounded_decisions if row["decision_id"] == "AF-ED-006"),
        {},
    )
    fail(
        authority_decision.get("field") == "authority_link_status"
        and authority_decision.get("input_value") == "not_reconciled"
        and authority_decision.get("result_value") == "candidate_rejected"
        and by_id["AF-P2-003"]["authority_candidate"] == "Ezra Meeker",
        "AF-ED-006 does not separate the authority candidate from the status transition",
        failures,
    )
    riverbed_decision = next(
        (row for row in source_grounded_decisions if row["decision_id"] == "AF-ED-008"),
        {},
    )
    fail(
        riverbed_decision.get("field") == "date_status"
        and riverbed_decision.get("result_value") == "unknown"
        and by_id["AF-P1-002"]["date_normalized"] == "",
        "AF-ED-008 does not agree with the cleaned riverbed date fields",
        failures,
    )
    fail(decision_ids == {row["decision_id"] for row in decisions}, "decision ID set is inconsistent", failures)


def check_ocr_and_summary(failures: list[str]) -> None:
    expected = json.loads((PACKET / "validation/expected-results.json").read_text(encoding="utf-8"))
    evaluation = rows("output/ocr-evaluation.csv")
    audit = rows("output/ocr-error-audit.csv")
    summary = rows("output/record-summary.csv")
    fail(len(evaluation) == 1, "OCR evaluation must contain one sample", failures)
    if evaluation:
        result = evaluation[0]
        expected_values = {
            "sample_id": "AF-OCR-P1-INTRO",
            "normalization": (
                "dLib TXT decoded as Windows-1250; source lines 1-4 selected; "
                "header lines joined; Unicode NFC; whitespace runs collapsed "
                "within three comparison lines"
            ),
            "reference_characters": "591",
            "character_substitutions": "7",
            "character_deletions": "5",
            "character_insertions": "0",
            "character_edits": "12",
            "cer": "0.020305",
            "reference_words": "93",
            "word_substitutions": "7",
            "word_deletions": "2",
            "word_insertions": "0",
            "word_edits": "9",
            "wer": "0.096774",
            "rate_rounding": "round half even to six decimal places",
        }
        for key, value in expected_values.items():
            fail(result.get(key) == value, f"OCR evaluation has unexpected {key}", failures)
        quantizer = Decimal("0.000001")
        calculated_cer = (Decimal(result["character_edits"]) / Decimal(result["reference_characters"])).quantize(quantizer, rounding=ROUND_HALF_EVEN)
        calculated_wer = (Decimal(result["word_edits"]) / Decimal(result["reference_words"])).quantize(quantizer, rounding=ROUND_HALF_EVEN)
        fail(result["cer"] == f"{calculated_cer:.6f}", "CER does not match the declared numeric rule", failures)
        fail(result["wer"] == f"{calculated_wer:.6f}", "WER does not match the declared numeric rule", failures)
        for key in (
            "reference_characters",
            "character_substitutions",
            "character_deletions",
            "character_insertions",
            "character_edits",
            "cer",
            "reference_words",
            "word_substitutions",
            "word_deletions",
            "word_insertions",
            "word_edits",
            "wer",
        ):
            fail(
                str(expected.get("ocr", {}).get(key, "")) == result[key],
                f"expected-results OCR value differs for {key}",
                failures,
            )
        for unit in ("character", "word"):
            total = sum(int(result[f"{unit}_{kind}"]) for kind in ("substitutions", "deletions", "insertions"))
            fail(total == int(result[f"{unit}_edits"]), f"{unit} S/D/I does not sum to edits", failures)
    unique_ids(audit, "audit_id", "OCR audit", failures)
    fail(len(audit) == 9, "OCR error audit must cover all nine word edits", failures)
    if evaluation:
        operation_counts = {
            operation: sum(row["operation"] == operation for row in audit)
            for operation in ("substitution", "deletion", "insertion")
        }
        for operation, plural in (("substitution", "substitutions"), ("deletion", "deletions"), ("insertion", "insertions")):
            fail(operation_counts[operation] == int(evaluation[0][f"word_{plural}"]), f"OCR audit {operation} count differs from aggregate", failures)
    fail(all(row["review_status"] == "manually reviewed against facsimile" for row in audit), "OCR audit contains an unreviewed row", failures)
    fail(all("character S/D/I" in row["aggregate_relation"] for row in audit), "OCR audit does not explain character-alignment scope", failures)
    stanovske_audit = next(
        (
            row
            for row in audit
            if row["reference_form"] == "stanovske"
            and row["provider_form"] == "stavovske"
        ),
        {},
    )
    fail(
        stanovske_audit.get("operation") == "substitution"
        and stanovske_audit.get("error_category") == "character substitution",
        "stanovske → stavovske is not classified as a character substitution",
        failures,
    )
    fail(expected.get("unresolved_case_count") == 2, "expected-results unresolved count is stale", failures)
    fail(expected.get("authentic_historical_object_count") == 1, "expected-results authentic-object count is stale", failures)
    fail(expected.get("reference_observation_count") == 8, "expected-results reference count is stale", failures)
    fail(expected.get("source_grounded_decision_count") == 9, "expected-results decision count is stale", failures)
    fail(expected.get("source_provider_export_sha256") == PROVIDER_EXPORT_SHA256, "expected-results provider-export digest is stale", failures)
    summary_keys = {(row["dimension"], row["category"]): row["count"] for row in summary}
    expected_summary = {
        ("inventory", "authentic_historical_object"): "1",
        ("inventory", "reference_observation"): "8",
        ("inventory", "issue_record"): "1",
        ("inventory", "feature_record"): "7",
        ("inventory", "synthetic_perturbation"): "4",
        ("record_kind", "group_portrait"): "1",
        ("date_status", "unknown"): "1",
        ("entity_structure", "multiple_people"): "1",
        ("authority_link_status", "candidate_rejected"): "1",
    }
    for key, value in expected_summary.items():
        fail(summary_keys.get(key) == value, f"record summary is missing {key}", failures)


def check_paired_content(failures: list[str]) -> dict[str, int]:
    workflow_terms = {
        "en": ("rights", "provenance", "manual", "unresolved", "raw/", "reference/"),
        "sl": ("pravic", "provenien", "ročn", "nerešen", "raw/", "reference/"),
    }
    for workflow in WORKFLOWS:
        for locale in ("en", "sl"):
            path = ROOT / "docs" / locale / workflow
            fail(path.exists(), f"missing paired workflow: docs/{locale}/{workflow}", failures)
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8").lower()
            for term in workflow_terms[locale]:
                fail(term in text, f"docs/{locale}/{workflow}: missing route concept {term!r}", failures)

    chapter_markers = {
        "en": {
            "chapters/research-design.md": ("target population", "sampling frame", "stopping rule", "sensitivity"),
            "chapters/data-metadata-models.md": ("source/raw layer", "interim layer", "processed/modelled layer", "decision layer"),
            "chapters/texts-corpora-ocr.md": (
                "### where the first pipeline fails",
                "### manual intervention",
                "### what remains uncertain",
                "### effect on the downstream claim",
                "confidence score",
                "multiple hands",
            ),
        },
        "sl": {
            "chapters/research-design.md": ("ciljna populacija", "vzorčni okvir", "pravilo za ustavitev", "občutljivost"),
            "chapters/data-metadata-models.md": ("izvorno oziroma surovo plast", "vmesno plast", "modelirano plast", "odločitveno"),
            "chapters/texts-corpora-ocr.md": (
                "### kje prvi postopek odpove",
                "### ročni poseg",
                "### kaj ostane negotovo",
                "### vpliv na nadaljnjo trditev",
                "ocena zaupanja",
                "več pisav oziroma rokopisnih rok",
            ),
        },
    }
    counts: dict[str, int] = {}
    for locale, expected_chapters in chapter_markers.items():
        for chapter, markers in expected_chapters.items():
            path = ROOT / "docs" / locale / chapter
            fail(path.exists(), f"missing paired chapter: docs/{locale}/{chapter}", failures)
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8").lower()
            words = len(re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE))
            counts[f"{locale}/{chapter}"] = words
            fail(words >= 2000, f"docs/{locale}/{chapter}: word count {words} is below the completeness minimum", failures)
            for marker in markers:
                fail(marker in text, f"docs/{locale}/{chapter}: missing required section concept {marker!r}", failures)

    for locale in ("en", "sl"):
        for relative in DOWNLOAD_LINK_PAGES:
            path = ROOT / "docs" / locale / relative
            text = path.read_text(encoding="utf-8") if path.exists() else ""
            fail("archival-friction-v1.zip" in text, f"docs/{locale}/{relative}: missing student ZIP link", failures)
            fail(SOURCE_TREE_URL in text, f"docs/{locale}/{relative}: missing source-tree link", failures)
    return counts


def check_ecosystem_and_generated(failures: list[str]) -> None:
    data = yaml.safe_load((ROOT / "intertextuality.yml").read_text(encoding="utf-8"))
    overrides = data.get("workflows", {})
    chapters = data.get("chapters", {})
    for workflow in WORKFLOWS:
        fail(workflow in overrides, f"ecosystem lacks curated override for {workflow}", failures)
    fail(WORKFLOWS[1] in chapters["chapters/data-metadata-models.md"]["workflows"], "metadata chapter does not feature reconciliation workflow", failures)
    fail(WORKFLOWS[2] in chapters["chapters/texts-corpora-ocr.md"]["workflows"], "text chapter does not feature OCR/HTR evaluation workflow", failures)

    for locale in ("en", "sl"):
        catalogue = (ROOT / "docs" / locale / "workflows/index.md").read_text(encoding="utf-8")
        for workflow in WORKFLOWS:
            relative = workflow.removeprefix("workflows/")
            fail(relative in catalogue, f"docs/{locale}/workflows/index.md is stale for {relative}", failures)
        manuscript = (ROOT / "release" / f"review-manuscript-{locale}.md").read_text(encoding="utf-8").lower()
        required = "where the first pipeline fails" if locale == "en" else "kje prvi postopek odpove"
        fail(required in manuscript, f"review-manuscript-{locale}.md is stale", failures)
    coverage = (ROOT / "release/translation-coverage.md").read_text(encoding="utf-8")
    fail("workflows/pdf/evaluate-ocr-or-htr-against-a-reference-sample.md" not in coverage, "translation coverage reports the paired OCR/HTR workflow as missing", failures)


def main() -> int:
    failures: list[str] = []
    if not PACKET.is_dir():
        print("Archival-friction check failed:\n\n- missing teaching-data/archival-friction")
        return 1
    actual_files = {
        path.relative_to(PACKET).as_posix()
        for path in PACKET.rglob("*")
        if path.is_file()
    }
    for relative in sorted(REQUIRED_PACKET_FILES - actual_files):
        failures.append(f"missing packet file: {relative}")
    if REQUIRED_PACKET_FILES - actual_files:
        for failure in failures:
            print(f"- {failure}")
        return 1

    check_bilingual_packet_docs(failures)
    check_source_and_rights(failures)
    check_records_and_decisions(failures)
    check_ocr_and_summary(failures)
    check_manifest(failures)
    check_archive(failures)
    word_counts = check_paired_content(failures)
    check_ecosystem_and_generated(failures)
    if failures:
        print("Archival-friction check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1
    count_report = ", ".join(f"{name}={count}" for name, count in sorted(word_counts.items()))
    print(
        "OK: archival-friction packet has 1 authentic two-page object, 8 handbook "
        "reference observations (1 issue + 7 features), 4 declared synthetic "
        "perturbations, 9 source-grounded editorial decisions, 2 field-specific open "
        "cases, a complete OCR S/D/I audit, paired packet documentation, a "
        "byte-checked deterministic ZIP, 3 paired workflows, 6 formal-review "
        "chapters, and curated ecosystem links."
    )
    print(f"Chapter word counts (minimum 2000; no hard maximum): {count_report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
