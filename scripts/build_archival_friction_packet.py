#!/usr/bin/env python3
"""Build deterministic derived files for the archival-friction packet."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import shutil
import tempfile
import unicodedata
from pathlib import Path


GENERATED = (
    "raw/messy-records.csv",
    "raw/provider-ocr.txt",
    "cleaned/records.csv",
    "cleaned/gold-transcription.txt",
    "cleaned/decisions.csv",
    "output/ocr-evaluation.csv",
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


def edit_distance(left: list[str] | str, right: list[str] | str) -> int:
    previous = list(range(len(right) + 1))
    for index, left_item in enumerate(left, start=1):
        current = [index]
        for offset, right_item in enumerate(right, start=1):
            current.append(
                min(
                    current[-1] + 1,
                    previous[offset] + 1,
                    previous[offset - 1] + (left_item != right_item),
                )
            )
        previous = current
    return previous[-1]


def expected_outputs(packet: Path) -> dict[str, bytes]:
    source_rows = read_csv(packet / "source/source-records.csv")
    fields = list(source_rows[0])
    messy_rows = [dict(row) for row in source_rows]
    decisions: list[dict[str, str]] = []

    for item in read_csv(packet / "source/synthetic-perturbations.csv"):
        operation = item["operation"]
        target_id = item["target_record_id"]
        if operation == "set":
            target = next(row for row in messy_rows if row["record_id"] == target_id)
            previous = target[item["field"]]
            target[item["field"]] = item["synthetic_value"]
            target["synthetic"] = "true"
            decisions.append(
                {
                    "decision_id": item["perturbation_id"],
                    "record_id": target_id,
                    "field": item["field"],
                    "raw_value": item["synthetic_value"],
                    "clean_value": previous,
                    "action": "restore_from_facsimile_or_leave_unresolved",
                    "evidence": "source/source-records.csv and the cited PDF locator",
                }
            )
        elif operation == "duplicate":
            target = next(row for row in messy_rows if row["record_id"] == target_id)
            duplicate = dict(target)
            duplicate["record_id"] = item["new_record_id"]
            duplicate["synthetic"] = "true"
            duplicate["evidence_note"] = "Synthetic duplicate teaching row; do not cite."
            messy_rows.append(duplicate)
            decisions.append(
                {
                    "decision_id": item["perturbation_id"],
                    "record_id": item["new_record_id"],
                    "field": "record_id",
                    "raw_value": item["new_record_id"],
                    "clean_value": target_id,
                    "action": "exclude_declared_synthetic_duplicate",
                    "evidence": "source/synthetic-perturbations.csv",
                }
            )
        else:
            raise ValueError(f"Unsupported perturbation operation: {operation}")

    decision_fields = [
        "decision_id",
        "record_id",
        "field",
        "raw_value",
        "clean_value",
        "action",
        "evidence",
    ]
    provider = normalized_text(packet / "source/provider-ocr.txt")
    gold = normalized_text(packet / "source/gold-transcription.txt")
    char_edits = edit_distance(provider, gold)
    word_edits = edit_distance(provider.split(), gold.split())
    cer = char_edits / len(gold)
    wer = word_edits / len(gold.split())
    evaluation = [
        {
            "sample_id": "AF-OCR-P1-INTRO",
            "normalization": "Unicode NFC; surrounding whitespace stripped",
            "tokenization": "Unicode whitespace",
            "gold_characters": str(len(gold)),
            "character_edits": str(char_edits),
            "cer": f"{cer:.6f}",
            "gold_words": str(len(gold.split())),
            "word_edits": str(word_edits),
            "wer": f"{wer:.6f}",
        }
    ]
    evaluation_fields = list(evaluation[0])
    summary = [
        {"measure": "source_records", "value": str(len(source_rows))},
        {"measure": "raw_records", "value": str(len(messy_rows))},
        {
            "measure": "synthetic_perturbations",
            "value": str(len(decisions)),
        },
        {
            "measure": "clean_records",
            "value": str(len(source_rows)),
        },
        {
            "measure": "unresolved_or_unknown_identity_records",
            "value": str(
                sum(
                    row["identity_status"] in {"unresolved", "multiple_people"}
                    for row in source_rows
                )
            ),
        },
    ]
    expected_json = {
        "clean_record_count": len(source_rows),
        "ocr": {
            "cer": round(cer, 6),
            "character_edits": char_edits,
            "gold_characters": len(gold),
            "gold_words": len(gold.split()),
            "sample_id": "AF-OCR-P1-INTRO",
            "wer": round(wer, 6),
            "word_edits": word_edits,
        },
        "packet_version": 1,
        "raw_record_count": len(messy_rows),
        "source_pdf_sha256": "e7b4b9f27f2043f2a3861b6cf05e1b4d8e1053e16eb81bf05f96d21385b5ad79",
        "source_record_count": len(source_rows),
        "synthetic_perturbation_count": len(decisions),
    }

    return {
        "raw/messy-records.csv": csv_bytes(messy_rows, fields),
        "raw/provider-ocr.txt": (provider + "\n").encode("utf-8"),
        "cleaned/records.csv": csv_bytes(source_rows, fields),
        "cleaned/gold-transcription.txt": (gold + "\n").encode("utf-8"),
        "cleaned/decisions.csv": csv_bytes(decisions, decision_fields),
        "output/ocr-evaluation.csv": csv_bytes(evaluation, evaluation_fields),
        "output/record-summary.csv": csv_bytes(summary, ["measure", "value"]),
        "validation/expected-results.json": (
            json.dumps(expected_json, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        ).encode("utf-8"),
    }


def build(packet: Path) -> None:
    outputs = expected_outputs(packet)
    for relative, content in outputs.items():
        destination = packet / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)

    manifest_lines = []
    for path in sorted(p for p in packet.rglob("*") if p.is_file()):
        relative = path.relative_to(packet).as_posix()
        if relative == "validation/SHA256SUMS.txt":
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        manifest_lines.append(f"{digest}  {relative}")
    manifest = packet / "validation/SHA256SUMS.txt"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")


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
    if not packet.is_dir():
        raise SystemExit(f"packet directory not found: {packet}")

    if args.check:
        with tempfile.TemporaryDirectory(prefix="archival-friction-") as temp_dir:
            expected = Path(temp_dir) / "archival-friction"
            shutil.copytree(packet, expected)
            build(expected)
            problems = compare_directories(packet, expected)
        if problems:
            for problem in problems:
                print(f"ERROR: {problem}")
            return 1
        print("Archival-friction packet is reproducible and current.")
        return 0

    build(packet)
    print(f"Rebuilt {len(GENERATED)} archival-friction packet files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
