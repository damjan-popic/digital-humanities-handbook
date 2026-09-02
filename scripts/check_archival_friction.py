#!/usr/bin/env python3
"""Validate the paired archival-friction route required by issue #23."""

from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "teaching-data" / "archival-friction"
PDF_SHA256 = "e7b4b9f27f2043f2a3861b6cf05e1b4d8e1053e16eb81bf05f96d21385b5ad79"
REQUIRED_PACKET_FILES = {
    "README.md",
    "rights-and-provenance.md",
    "data-dictionary.md",
    "metadata-raw.csv",
    "metadata-clean.csv",
    "correction-log.csv",
    "unresolved-cases.csv",
    "expected-observations.md",
    "source/commons-source.json",
    "source/ilustrirani-slovenec-1925-02-07.pdf",
    "source/source-records.csv",
    "source/synthetic-perturbations.csv",
    "source/provider-ocr.txt",
    "source/gold-transcription.txt",
    "raw/messy-records.csv",
    "raw/provider-ocr.txt",
    "interim/reconciliation-candidates.csv",
    "cleaned/records.csv",
    "cleaned/gold-transcription.txt",
    "cleaned/decisions.csv",
    "output/ocr-evaluation.csv",
    "output/record-summary.csv",
    "validation/expected-results.json",
    "validation/SHA256SUMS.txt",
    "known-problems/README.md",
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


def fail(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def rows(relative: str) -> list[dict[str, str]]:
    with (PACKET / relative).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def unique_ids(
    records: list[dict[str, str]], field: str, label: str, failures: list[str]
) -> set[str]:
    values = [row.get(field, "") for row in records]
    fail(all(values), f"{label}: blank {field}", failures)
    fail(len(values) == len(set(values)), f"{label}: duplicate {field}", failures)
    return set(values)


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
        fail(
            listed[relative] == actual[relative],
            f"packet manifest digest mismatch: {relative}",
            failures,
        )


def check_packet(failures: list[str]) -> None:
    actual_files = {
        path.relative_to(PACKET).as_posix()
        for path in PACKET.rglob("*")
        if path.is_file()
    }
    for relative in sorted(REQUIRED_PACKET_FILES - actual_files):
        failures.append(f"missing packet file: {relative}")
    if REQUIRED_PACKET_FILES - actual_files:
        return

    rights = (PACKET / "rights-and-provenance.md").read_text(encoding="utf-8")
    for required in (
        "public domain",
        "Digital Library of Slovenia",
        "Wikimedia Commons",
        "2 September 2026",
        PDF_SHA256,
        "AF-SYN-001",
        "not historical text",
    ):
        fail(required in rights, f"rights audit is missing {required!r}", failures)

    pdf = PACKET / "source/ilustrirani-slovenec-1925-02-07.pdf"
    fail(hashlib.sha256(pdf.read_bytes()).hexdigest() == PDF_SHA256, "source PDF digest changed", failures)

    source = rows("source/source-records.csv")
    raw = rows("metadata-raw.csv")
    clean = rows("metadata-clean.csv")
    perturbations = rows("source/synthetic-perturbations.csv")
    corrections = rows("correction-log.csv")
    unresolved = rows("unresolved-cases.csv")
    candidates = rows("interim/reconciliation-candidates.csv")

    source_ids = unique_ids(source, "record_id", "source records", failures)
    raw_ids = unique_ids(raw, "record_id", "raw records", failures)
    clean_ids = unique_ids(clean, "record_id", "clean records", failures)
    perturbation_ids = unique_ids(perturbations, "perturbation_id", "perturbations", failures)
    correction_ids = unique_ids(corrections, "decision_id", "correction log", failures)
    candidate_ids = unique_ids(candidates, "candidate_id", "interim candidates", failures)
    unresolved_ids = unique_ids(unresolved, "case_id", "unresolved cases", failures)

    fail(len(source) == 8, "source table must contain eight records", failures)
    fail(len(raw) == 9, "raw table must contain nine records", failures)
    fail(len(clean) == 8, "clean table must contain eight records", failures)
    fail(source_ids == clean_ids, "clean stable IDs differ from the authentic source IDs", failures)
    fail(source_ids < raw_ids, "raw IDs must contain all source IDs plus a synthetic row", failures)
    fail(raw_ids - source_ids == {"AF-P1-002-DUP"}, "unexpected extra raw record IDs", failures)
    fail(perturbation_ids == correction_ids == candidate_ids, "synthetic, interim and decision IDs differ", failures)
    fail(len(perturbations) == 4, "expected four declared synthetic perturbations", failures)
    fail(len(unresolved_ids) == 6, "expected six explicit unresolved cases", failures)
    fail(
        {row["record_id"] for row in unresolved} <= clean_ids,
        "unresolved cases reference a missing clean record",
        failures,
    )
    fail(all(row["synthetic"] == "false" for row in source), "source layer contains synthetic rows", failures)
    fail(all(row["synthetic"] == "false" for row in clean), "clean layer contains synthetic rows", failures)
    fail(all(row["synthetic"] == "true" for row in corrections), "correction log does not label synthetic changes", failures)
    fail(all(row["synthetic"] == "true" for row in candidates), "interim queue does not label synthetic candidates", failures)
    fail(
        (PACKET / "metadata-raw.csv").read_bytes()
        == (PACKET / "raw/messy-records.csv").read_bytes(),
        "top-level and layered raw metadata differ",
        failures,
    )
    fail(
        (PACKET / "metadata-clean.csv").read_bytes()
        == (PACKET / "cleaned/records.csv").read_bytes(),
        "top-level and layered clean metadata differ",
        failures,
    )

    required_correction_fields = {
        "decision_id",
        "record_id",
        "field",
        "source_value",
        "transformed_value",
        "responsible",
        "decision_date",
        "reason",
        "confidence",
        "reversible",
        "source_provenance",
    }
    fail(
        bool(corrections) and required_correction_fields <= set(corrections[0]),
        "correction log is missing required intervention fields",
        failures,
    )

    expected = json.loads((PACKET / "validation/expected-results.json").read_text(encoding="utf-8"))
    evaluation = rows("output/ocr-evaluation.csv")
    fail(len(evaluation) == 1, "OCR evaluation must contain one sample", failures)
    if evaluation:
        result = evaluation[0]
        for key, value in {
            "sample_id": "AF-OCR-P1-INTRO",
            "gold_characters": "591",
            "character_edits": "15",
            "cer": "0.025381",
            "gold_words": "93",
            "word_edits": "9",
            "wer": "0.096774",
        }.items():
            fail(result.get(key) == value, f"OCR evaluation has unexpected {key}", failures)
    fail(expected.get("unresolved_case_count") == 6, "expected-results unresolved count is stale", failures)
    check_manifest(failures)


def check_paired_content(failures: list[str]) -> None:
    workflow_terms = {
        "en": ("rights", "provenance", "first", "automated", "manual", "unresolved", "valid", "claim", "raw/"),
        "sl": ("pravic", "provenien", "prvi", "samodejn", "ročn", "nerešen", "prever", "trdit", "raw/"),
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
    for locale, expected_chapters in chapter_markers.items():
        for chapter, markers in expected_chapters.items():
            path = ROOT / "docs" / locale / chapter
            fail(path.exists(), f"missing paired chapter: docs/{locale}/{chapter}", failures)
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8").lower()
            words = len(text.split())
            fail(2000 <= words <= 3000, f"docs/{locale}/{chapter}: word count {words} is outside 2000–3000", failures)
            for marker in markers:
                fail(marker in text, f"docs/{locale}/{chapter}: missing required section concept {marker!r}", failures)


def check_ecosystem_and_generated(failures: list[str]) -> None:
    data = yaml.safe_load((ROOT / "intertextuality.yml").read_text(encoding="utf-8"))
    overrides = data.get("workflows", {})
    chapters = data.get("chapters", {})
    for workflow in WORKFLOWS:
        fail(workflow in overrides, f"ecosystem lacks curated override for {workflow}", failures)
    fail(
        WORKFLOWS[1] in chapters["chapters/data-metadata-models.md"]["workflows"],
        "metadata chapter does not feature reconciliation workflow",
        failures,
    )
    fail(
        WORKFLOWS[2] in chapters["chapters/texts-corpora-ocr.md"]["workflows"],
        "text chapter does not feature OCR/HTR evaluation workflow",
        failures,
    )

    for locale in ("en", "sl"):
        catalogue = (ROOT / "docs" / locale / "workflows/index.md").read_text(encoding="utf-8")
        for workflow in WORKFLOWS:
            relative = workflow.removeprefix("workflows/")
            fail(relative in catalogue, f"docs/{locale}/workflows/index.md is stale for {relative}", failures)
        manuscript = (ROOT / "release" / f"review-manuscript-{locale}.md").read_text(encoding="utf-8").lower()
        required = "where the first pipeline fails" if locale == "en" else "kje prvi postopek odpove"
        fail(required in manuscript, f"review-manuscript-{locale}.md is stale", failures)

    coverage = (ROOT / "release/translation-coverage.md").read_text(encoding="utf-8")
    fail(
        "workflows/pdf/evaluate-ocr-or-htr-against-a-reference-sample.md" not in coverage,
        "translation coverage incorrectly reports the paired OCR/HTR workflow as missing",
        failures,
    )


def main() -> int:
    failures: list[str] = []
    if not PACKET.is_dir():
        print("Archival-friction check failed:\n\n- missing teaching-data/archival-friction")
        return 1
    check_packet(failures)
    check_paired_content(failures)
    check_ecosystem_and_generated(failures)
    if failures:
        print("Archival-friction check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(
        "OK: archival-friction packet has 8 authentic records, 4 declared synthetic "
        "perturbations, 6 unresolved cases, 3 paired workflows, 6 formal-review "
        "chapters, a current manifest, and curated ecosystem links."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
