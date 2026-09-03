#!/usr/bin/env python3
"""Build deterministic derived files and the download for issue #23."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import shutil
import tempfile
import unicodedata
from decimal import Decimal, ROUND_HALF_EVEN
from pathlib import Path
from zipfile import ZipFile

from scholarly_work_package_utils import FIXED_ZIP_DATE, deterministic_zip


ARCHIVE_NAME = "archival-friction-v1.zip"
ARCHIVE_PREFIX = "archival-friction-v1/"
PROVIDER_EXPORT_SHA256 = "ab4e9e5464eb349d4c27b3b895c2b98b3a6509f3ce4be76f387b739a1fcee456"
RATE_QUANTIZER = Decimal("0.000001")
DEPRECATED_PACKET_FILES = (
    "source/source-records.csv",
    "source/synthetic-perturbations.csv",
    "source/gold-transcription.txt",
    "source/transcription-note.md",
    "cleaned/gold-transcription.txt",
)
GENERATED_PACKET_FILES = (
    "metadata-raw.csv",
    "metadata-clean.csv",
    "correction-log.csv",
    "unresolved-cases.csv",
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
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def csv_bytes(rows: list[dict[str, str]], fields: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def normalized_text(path: Path) -> str:
    return unicodedata.normalize("NFC", path.read_text(encoding="utf-8")).strip()


def provider_comparison_excerpt(path: Path) -> str:
    """Derive the declared three-line comparison sample from the dLib TXT export."""
    source_lines = path.read_bytes().decode("windows-1250").splitlines()
    if len(source_lines) < 4:
        raise ValueError("The dLib TXT export no longer contains the selected first four lines")
    selected_lines = (
        f"{source_lines[0]} {source_lines[1]}",
        source_lines[2],
        source_lines[3],
    )
    normalized_lines = (
        " ".join(unicodedata.normalize("NFC", line).split())
        for line in selected_lines
    )
    return "\n".join(normalized_lines)


def rounded_rate(edits: int, denominator: int) -> str:
    return format(
        (Decimal(edits) / Decimal(denominator)).quantize(
            RATE_QUANTIZER, rounding=ROUND_HALF_EVEN
        ),
        ".6f",
    )


def align(
    reference: list[str] | str, provider: list[str] | str
) -> list[tuple[str, str, str]]:
    """Return one minimum alignment with substitution > deletion > insertion ties."""
    rows = len(reference) + 1
    columns = len(provider) + 1
    costs = [[0] * columns for _ in range(rows)]
    moves = [[""] * columns for _ in range(rows)]
    for index in range(1, rows):
        costs[index][0] = index
        moves[index][0] = "deletion"
    for index in range(1, columns):
        costs[0][index] = index
        moves[0][index] = "insertion"
    priority = {"substitution": 0, "deletion": 1, "insertion": 2}
    for row in range(1, rows):
        for column in range(1, columns):
            if reference[row - 1] == provider[column - 1]:
                costs[row][column] = costs[row - 1][column - 1]
                moves[row][column] = "equal"
                continue
            candidates = (
                (costs[row - 1][column - 1] + 1, "substitution"),
                (costs[row - 1][column] + 1, "deletion"),
                (costs[row][column - 1] + 1, "insertion"),
            )
            costs[row][column], moves[row][column] = min(
                candidates, key=lambda item: (item[0], priority[item[1]])
            )

    operations: list[tuple[str, str, str]] = []
    row, column = len(reference), len(provider)
    while row or column:
        operation = moves[row][column]
        if operation in {"equal", "substitution"}:
            operations.append((operation, reference[row - 1], provider[column - 1]))
            row -= 1
            column -= 1
        elif operation == "deletion":
            operations.append((operation, reference[row - 1], ""))
            row -= 1
        elif operation == "insertion":
            operations.append((operation, "", provider[column - 1]))
            column -= 1
        else:
            raise ValueError("Alignment backtrace reached an undefined move")
    operations.reverse()
    return operations


def operation_counts(operations: list[tuple[str, str, str]]) -> dict[str, int]:
    return {
        operation: sum(item[0] == operation for item in operations)
        for operation in ("substitution", "deletion", "insertion")
    }


def word_audit(
    operations: list[tuple[str, str, str]],
) -> list[dict[str, str]]:
    classifications = {
        ("substitution", "„Slovenca“", '„Slovenca"'): (
            "punctuation recognition",
            "recognition_error",
            "Phrase search and quotation normalization can diverge.",
        ),
        ("substitution", "30.", "30,"): (
            "punctuation recognition",
            "recognition_error",
            "Issue numbering may be parsed incorrectly.",
        ),
        ("substitution", "bori", "obri"): (
            "letter order",
            "recognition_error",
            "Keyword retrieval for the verb fails.",
        ),
        ("deletion", "ne", ""): (
            "omitted word",
            "recognition_error",
            "Negation is lost and the sentence meaning changes.",
        ),
        ("substitution", "stanovske", "stavovske"): (
            "character substitution",
            "recognition_error",
            "A politically meaningful term becomes an out-of-vocabulary form.",
        ),
        ("deletion", "naroda", ""): (
            "word-boundary merge",
            "recognition_error",
            "The reference token is lost when two words merge in the provider text.",
        ),
        ("substitution", "in", "narodain"): (
            "word-boundary merge",
            "recognition_error",
            "The conjunction aligns to a merged provider token, distorting both searches.",
        ),
        ("substitution", "kulturnega", "kultrunega"): (
            "letter order",
            "recognition_error",
            "Keyword retrieval and frequency counts diverge.",
        ),
        ("substitution", "ki", "i"): (
            "initial-letter deletion",
            "recognition_error",
            "The relative clause is tokenized with a non-word form.",
        ),
    }
    audited = []
    for operation, reference, provider in operations:
        if operation == "equal":
            continue
        key = (operation, reference, provider)
        if key not in classifications:
            raise ValueError(f"Unclassified OCR word operation: {key!r}")
        category, error_type, consequence = classifications[key]
        audited.append(
            {
                "audit_id": f"AF-OCR-A{len(audited) + 1:03d}",
                "sample_id": "AF-OCR-P1-INTRO",
                "source_locator": "PDF page 1, masthead/title/introductory paragraph",
                "reference_form": reference,
                "provider_form": provider,
                "operation": operation,
                "error_category": category,
                "policy_or_recognition": error_type,
                "probable_downstream_consequence": consequence,
                "review_status": "manually reviewed against facsimile",
                "aggregate_relation": (
                    "Included in word S/D/I totals; character S/D/I use a separate "
                    "whole-string alignment and are not allocated to word rows."
                ),
            }
        )
    return audited


def expected_outputs(packet: Path) -> dict[str, bytes]:
    reference_rows = read_csv(packet / "reference/observations.csv")
    fields = list(reference_rows[0])
    clean_rows = [dict(row) for row in reference_rows]
    messy_rows = [dict(row) for row in reference_rows]
    source_grounded_decisions = read_csv(packet / "reference/editorial-decisions.csv")
    perturbations = read_csv(packet / "teaching/synthetic-perturbations.csv")
    synthetic_decisions: list[dict[str, str]] = []
    candidates: list[dict[str, str]] = []
    action_by_id = {
        "AF-SYN-001": "restore_reference_capitalization",
        "AF-SYN-002": "restore_printed_person_label",
        "AF-SYN-003": "reject_unsupported_authority_acceptance",
        "AF-SYN-004": "exclude_declared_synthetic_duplicate",
    }

    for item in perturbations:
        target_id = item["target_record_id"]
        target = next(row for row in messy_rows if row["record_id"] == target_id)
        if item["operation"] == "set":
            reference_value = target[item["field"]]
            target[item["field"]] = item["synthetic_value"]
            target["synthetic"] = "true"
            affected_id = target_id
            input_value = item["synthetic_value"]
            result_value = reference_value
        elif item["operation"] == "duplicate":
            duplicate = dict(target)
            duplicate["record_id"] = item["new_record_id"]
            duplicate["synthetic"] = "true"
            duplicate["evidence_note"] = "Declared synthetic duplicate teaching row; do not cite."
            messy_rows.append(duplicate)
            affected_id = item["new_record_id"]
            input_value = item["new_record_id"]
            result_value = target_id
        else:
            raise ValueError(f"Unsupported perturbation operation: {item['operation']}")
        synthetic_decisions.append(
            {
                "decision_id": item["perturbation_id"],
                "record_id": affected_id,
                "field": item["field"] or "record_id",
                "input_value": input_value,
                "result_value": result_value,
                "action": action_by_id[item["perturbation_id"]],
                "source_locator": target["source_locator"],
                "evidence": item["teaching_reason"],
                "responsible_process": "deterministic packet builder",
                "decision_date": "2026-09-03",
                "rule_version": "AF-v1.1",
                "confidence": "high",
                "reversible": "true",
                "synthetic": "true",
            }
        )
        candidates.append(
            {
                "candidate_id": item["perturbation_id"],
                "record_id": affected_id,
                "field": item["field"] or "record_id",
                "candidate_value": input_value,
                "reference_value": result_value,
                "review_status": "requires_source_or_reference_review",
                "synthetic": "true",
            }
        )

    decision_fields = list(source_grounded_decisions[0])
    decisions = source_grounded_decisions + synthetic_decisions
    unresolved = [
        {
            "case_id": "AF-U-001",
            "record_id": "AF-P1-002",
            "field": "creation_date",
            "status": "unknown",
            "current_value": "",
            "current_evidence": "No creation date is printed; 1925-02-07 is only the issue context.",
            "reason": "The issue date cannot be inherited as a photograph-creation date.",
            "evidence_needed": "Item-level dating evidence or a documented derivation rule supported by the source.",
        },
        {
            "case_id": "AF-U-002",
            "record_id": "AF-P2-003",
            "field": "authority_link",
            "status": "candidate_rejected",
            "current_value": "Ezra Meeker",
            "current_evidence": "The printed form is Meker; name and age resemblance alone do not establish identity.",
            "reason": "The tested external candidate is not supported strongly enough for acceptance.",
            "evidence_needed": "Independent biographical or event evidence connecting the pictured speaker to an authority record.",
        },
    ]

    provider = provider_comparison_excerpt(packet / "source/provider-ocr.txt")
    reference = normalized_text(packet / "reference/reference-transcription.txt")
    character_operations = align(reference, provider)
    word_operations = align(reference.split(), provider.split())
    character_counts = operation_counts(character_operations)
    word_counts = operation_counts(word_operations)
    character_edits = sum(character_counts.values())
    word_edits = sum(word_counts.values())
    reference_character_count = len(reference)
    reference_word_count = len(reference.split())
    cer = rounded_rate(character_edits, reference_character_count)
    wer = rounded_rate(word_edits, reference_word_count)
    evaluation = [
        {
            "sample_id": "AF-OCR-P1-INTRO",
            "normalization": (
                "dLib TXT decoded as Windows-1250; source lines 1-4 selected; "
                "header lines joined; Unicode NFC; whitespace runs collapsed "
                "within three comparison lines"
            ),
            "character_tokenization": "Unicode code points including internal whitespace",
            "word_tokenization": "Unicode whitespace",
            "tie_breaking": "equal, then substitution, deletion, insertion",
            "reference_characters": str(reference_character_count),
            "character_substitutions": str(character_counts["substitution"]),
            "character_deletions": str(character_counts["deletion"]),
            "character_insertions": str(character_counts["insertion"]),
            "character_edits": str(character_edits),
            "cer": cer,
            "reference_words": str(reference_word_count),
            "word_substitutions": str(word_counts["substitution"]),
            "word_deletions": str(word_counts["deletion"]),
            "word_insertions": str(word_counts["insertion"]),
            "word_edits": str(word_edits),
            "wer": wer,
            "rate_rounding": "round half even to six decimal places",
        }
    ]
    audit = word_audit(word_operations)

    summary: list[dict[str, str]] = []

    def add_summary(dimension: str, category: str, count: int, notes: str) -> None:
        summary.append(
            {
                "dimension": dimension,
                "category": category,
                "count": str(count),
                "notes": notes,
            }
        )

    add_summary("inventory", "authentic_historical_object", 1, "One two-page PDF.")
    add_summary("inventory", "reference_observation", len(reference_rows), "Handbook-created and source-grounded.")
    add_summary("inventory", "issue_record", 1, "Issue-level reference observation.")
    add_summary("inventory", "feature_record", 7, "Feature-level reference observations.")
    add_summary("inventory", "synthetic_perturbation", len(perturbations), "Declared teaching disturbances.")
    add_summary("inventory", "raw_row", len(messy_rows), "Eight reference rows plus one duplicate.")
    add_summary("inventory", "clean_row", len(clean_rows), "Synthetic changes removed.")
    add_summary("inventory", "unresolved_case", len(unresolved), "Field-specific open cases.")
    for dimension, field in (
        ("record_kind", "record_kind"),
        ("date_status", "date_status"),
        ("entity_structure", "entity_structure"),
        ("authority_link_status", "authority_link_status"),
    ):
        for category in sorted({row[field] for row in clean_rows}):
            add_summary(
                dimension,
                category,
                sum(row[field] == category for row in clean_rows),
                "Derived from cleaned/records.csv.",
            )

    expected_json = {
        "authentic_historical_object_count": 1,
        "clean_record_count": len(clean_rows),
        "feature_record_count": 7,
        "issue_record_count": 1,
        "ocr": {
            "cer": cer,
            "character_deletions": character_counts["deletion"],
            "character_edits": character_edits,
            "character_insertions": character_counts["insertion"],
            "character_substitutions": character_counts["substitution"],
            "reference_characters": reference_character_count,
            "reference_words": reference_word_count,
            "sample_id": "AF-OCR-P1-INTRO",
            "wer": wer,
            "word_deletions": word_counts["deletion"],
            "word_edits": word_edits,
            "word_insertions": word_counts["insertion"],
            "word_substitutions": word_counts["substitution"],
        },
        "packet_version": 1,
        "raw_record_count": len(messy_rows),
        "reference_observation_count": len(reference_rows),
        "source_grounded_decision_count": len(source_grounded_decisions),
        "source_provider_export_sha256": PROVIDER_EXPORT_SHA256,
        "source_pdf_sha256": "e7b4b9f27f2043f2a3861b6cf05e1b4d8e1053e16eb81bf05f96d21385b5ad79",
        "synthetic_perturbation_count": len(perturbations),
        "unresolved_case_count": len(unresolved),
    }

    unresolved_fields = list(unresolved[0])
    candidate_fields = list(candidates[0])
    return {
        "metadata-raw.csv": csv_bytes(messy_rows, fields),
        "metadata-clean.csv": csv_bytes(clean_rows, fields),
        "correction-log.csv": csv_bytes(decisions, decision_fields),
        "unresolved-cases.csv": csv_bytes(unresolved, unresolved_fields),
        "raw/messy-records.csv": csv_bytes(messy_rows, fields),
        "raw/provider-ocr.txt": (provider + "\n").encode("utf-8"),
        "interim/reconciliation-candidates.csv": csv_bytes(candidates, candidate_fields),
        "cleaned/records.csv": csv_bytes(clean_rows, fields),
        "cleaned/reference-transcription.txt": (reference + "\n").encode("utf-8"),
        "cleaned/decisions.csv": csv_bytes(decisions, decision_fields),
        "output/ocr-evaluation.csv": csv_bytes(evaluation, list(evaluation[0])),
        "output/ocr-error-audit.csv": csv_bytes(audit, list(audit[0])),
        "output/record-summary.csv": csv_bytes(summary, list(summary[0])),
        "validation/expected-results.json": (
            json.dumps(expected_json, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        ).encode("utf-8"),
    }


def write_archive(packet: Path, archive: Path, digest_path: Path) -> None:
    members = [
        (ARCHIVE_PREFIX + path.relative_to(packet).as_posix(), path.read_bytes())
        for path in packet.rglob("*")
        if path.is_file()
    ]
    deterministic_zip(archive, members)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    digest_path.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")


def build(packet: Path, archive: Path, digest_path: Path) -> None:
    for relative in DEPRECATED_PACKET_FILES:
        path = packet / relative
        if path.exists():
            path.unlink()
    outputs = expected_outputs(packet)
    for relative, content in outputs.items():
        destination = packet / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)

    manifest_lines = []
    for path in sorted(item for item in packet.rglob("*") if item.is_file()):
        relative = path.relative_to(packet).as_posix()
        if relative == "validation/SHA256SUMS.txt":
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        manifest_lines.append(f"{digest}  {relative}")
    manifest = packet / "validation/SHA256SUMS.txt"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
    write_archive(packet, archive, digest_path)


def compare_directories(actual: Path, expected: Path) -> list[str]:
    actual_files = {
        path.relative_to(actual).as_posix(): path
        for path in actual.rglob("*")
        if path.is_file()
    }
    expected_files = {
        path.relative_to(expected).as_posix(): path
        for path in expected.rglob("*")
        if path.is_file()
    }
    problems = []
    for relative in sorted(actual_files.keys() | expected_files.keys()):
        if relative not in actual_files:
            problems.append(f"missing generated packet file: {relative}")
        elif relative not in expected_files:
            problems.append(f"unexpected packet file: {relative}")
        elif actual_files[relative].read_bytes() != expected_files[relative].read_bytes():
            problems.append(f"stale packet file: {relative}")
    return problems


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    packet = repo_root / "teaching-data/archival-friction"
    archive = repo_root / "docs/assets/downloads" / ARCHIVE_NAME
    digest_path = archive.with_suffix(archive.suffix + ".sha256")
    if not packet.is_dir():
        raise SystemExit(f"packet directory not found: {packet}")

    if args.check:
        with tempfile.TemporaryDirectory(prefix="archival-friction-") as temp_dir:
            temporary = Path(temp_dir)
            expected_packet = temporary / "archival-friction"
            expected_archive = temporary / ARCHIVE_NAME
            expected_digest = temporary / f"{ARCHIVE_NAME}.sha256"
            shutil.copytree(packet, expected_packet)
            build(expected_packet, expected_archive, expected_digest)
            problems = compare_directories(packet, expected_packet)
            if not archive.exists() or archive.read_bytes() != expected_archive.read_bytes():
                problems.append(f"stale download: docs/assets/downloads/{ARCHIVE_NAME}")
            if not digest_path.exists() or digest_path.read_bytes() != expected_digest.read_bytes():
                problems.append(f"stale download digest: docs/assets/downloads/{ARCHIVE_NAME}.sha256")
        if problems:
            for problem in problems:
                print(f"ERROR: {problem}")
            return 1
        with ZipFile(archive) as archived:
            if any(info.date_time != FIXED_ZIP_DATE for info in archived.infolist()):
                print("ERROR: download contains a non-deterministic timestamp")
                return 1
        print("Archival-friction packet, deterministic ZIP, and digest are reproducible and current.")
        return 0

    build(packet, archive, digest_path)
    print(
        f"Rebuilt {len(GENERATED_PACKET_FILES)} packet files plus {ARCHIVE_NAME} and its digest."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
