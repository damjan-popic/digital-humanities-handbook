#!/usr/bin/env python3
"""Build issue #24 text/NLP teaching outputs and deterministic download."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import itertools
import json
import re
import sys
import tempfile
import unicodedata
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

from scholarly_work_package_utils import deterministic_zip


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "teaching-data" / "text-nlp-validation"
ARCHIVE = ROOT / "docs" / "assets" / "downloads" / "text-nlp-validation-v1.zip"
DIGEST = ARCHIVE.with_suffix(ARCHIVE.suffix + ".sha256")
PREFIX = "text-nlp-validation-v1/"
THEMES = ("archives", "museums", "language", "press")
TOPIC_STABILITY_THRESHOLD = 0.30
TOKEN_RE = re.compile(r"(?u)\b[^\W\d_][^\W_]+\b")
REFERENCE_DRAFT_STATUS = "machine-assisted reference draft; pending human review"
CAUSAL_DRAFT_STATUS = "machine-assisted causal draft; pending human review"
HUMAN_REVIEWED_STATUS = "human-reviewed"

OUTPUT_FILES = (
    "raw/annotation-samples.csv",
    "output/document-summary.csv",
    "output/frequency-dispersion.csv",
    "output/concordance.csv",
    "output/frequency-sensitivity.csv",
    "output/classla-evaluation.csv",
    "output/classla-error-log.csv",
    "output/downstream-consequences.csv",
    "output/topic-stability.csv",
    "output/topic-count-sensitivity.csv",
    "output/emotion-baseline.csv",
    "output/emotion-sensitivity.csv",
    "output/emotion-method-comparison.csv",
    "validation/expected-values.json",
)


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def csv_bytes(rows: list[dict[str, object]], fields: list[str] | None = None) -> bytes:
    if not rows and fields is None:
        raise ValueError("CSV fields are required for an empty table")
    fields = fields or list(rows[0])
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def simple_frontmatter(path: Path) -> dict[str, str]:
    """Read the packet's scalar frontmatter without adding a YAML dependency."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.S)
    if match is None:
        raise ValueError(f"Missing frontmatter: {path}")
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, separator, value = line.partition(":")
        if not separator:
            raise ValueError(f"Unsupported frontmatter line in {path}: {line}")
        result[key.strip()] = value.strip().strip('"\'')
    return result


def validate_review_state(
    record: dict[str, str],
    *,
    status_field: str,
    draft_status: str,
    context: str,
    reviewer_field: str = "reviewer",
    date_field: str = "reviewed_on",
    scope_field: str = "review_scope",
) -> None:
    """Accept the declared draft or a fully documented human-reviewed state."""
    status = record.get(status_field, "")
    if status == draft_status:
        return
    if status != HUMAN_REVIEWED_STATUS:
        raise ValueError(f"{context}: unsupported review status {status!r}")
    reviewer = record.get(reviewer_field, "").strip()
    reviewed_on = record.get(date_field, "").strip()
    review_scope = record.get(scope_field, "").strip()
    try:
        if "T" in reviewed_on:
            datetime.fromisoformat(reviewed_on.replace("Z", "+00:00"))
        else:
            date.fromisoformat(reviewed_on)
        valid_date = True
    except ValueError:
        valid_date = False
    if not reviewer or not review_scope or not valid_date:
        raise ValueError(
            f"{context}: human-reviewed records require a named reviewer, ISO date and review scope"
        )


def normalized(text: str) -> str:
    return unicodedata.normalize("NFC", text).strip()


def split_sentences(text: str) -> list[str]:
    """Split the packet's declared synthetic prose while retaining terminal quotes."""
    text = normalized(text)
    matches = [
        normalized(match.group(0))
        for match in re.finditer(r".*?[.!?](?:[«»”\"])?(?=\s+|$)", text)
    ]
    if not matches or normalized(" ".join(matches)) != text:
        raise ValueError("Sentence splitter could not account for the complete source text")
    return matches


def extract_sentence(text: str, selector: str) -> str:
    text = normalized(text)
    if selector.startswith("sentence_prefix:"):
        prefix = selector.split(":", 1)[1]
        start = text.index(prefix)
        return normalized(text[start:].splitlines()[0])
    if selector.startswith("sentence_index:"):
        index = int(selector.split(":", 1)[1]) - 1
        return split_sentences(text)[index]
    raise ValueError(f"Unsupported selector: {selector}")


def annotation_samples() -> tuple[list[dict[str, object]], dict[str, dict[str, object]]]:
    registry = json.loads((PACKET / "source/extraction-registry.json").read_text(encoding="utf-8"))
    documents = {row["doc_id"]: row for row in csv_rows(PACKET / "source/contemporary-sample.csv")}
    model_meta = json.loads((PACKET / "interim/classla/model-run.json").read_text(encoding="utf-8"))
    result: list[dict[str, object]] = []
    by_id: dict[str, dict[str, object]] = {}
    for entry in registry["extractions"]:
        path = ROOT / entry["source_path"]
        if entry["source_path"].endswith("contemporary-sample.csv"):
            source_text = documents[entry["source_record_id"]]["text"]
        else:
            source_text = path.read_text(encoding="utf-8")
        text = extract_sentence(source_text, entry["selector"])
        text_digest = sha256_bytes(text.encode("utf-8"))
        expected_digest = model_meta["sample_text_sha256"][entry["sample_id"]]
        if text_digest != expected_digest:
            raise ValueError(f"Frozen CLASSLA input hash mismatch: {entry['sample_id']}")
        row = {
            "sample_id": entry["sample_id"],
            "stratum": entry["stratum"],
            "source_path": entry["source_path"],
            "source_record_id": entry["source_record_id"],
            "selector": entry["selector"],
            "synthetic": str(entry["synthetic"]).lower(),
            "normalization": registry["normalization"],
            "text": text,
            "text_sha256": text_digest,
            "source_sha256": sha256(path),
        }
        result.append(row)
        by_id[entry["sample_id"]] = row
    return result, by_id


def parse_conllu(path: Path) -> dict[str, object]:
    comments: dict[str, list[str]] = defaultdict(list)
    words: list[dict[str, str | int]] = []
    multiword_tokens: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# ") and " = " in line:
            key, value = line[2:].split(" = ", 1)
            comments[key].append(value)
        elif line and not line.startswith("#"):
            fields = line.split("\t")
            if len(fields) != 10:
                raise ValueError(f"Malformed CoNLL-U row in {path}: {line}")
            if "-" in fields[0]:
                multiword_tokens.append(fields[0])
                continue
            if "." in fields[0]:
                continue
            words.append(
                {
                    "id": int(fields[0]),
                    "form": fields[1],
                    "lemma": fields[2],
                    "upos": fields[3],
                    "xpos": fields[4],
                    "feats": fields[5],
                    "head": int(fields[6]),
                    "deprel": fields[7],
                    "deps": fields[8],
                    "misc": fields[9],
                }
            )
    ids = [int(word["id"]) for word in words]
    if ids != list(range(1, len(ids) + 1)):
        raise ValueError(f"Non-contiguous CoNLL-U word IDs in {path}")
    if any(int(word["head"]) not in {0, *ids} for word in words):
        raise ValueError(f"Invalid CoNLL-U head in {path}")
    return {"comments": comments, "words": words, "multiword_tokens": multiword_tokens}


def align_words(reference: list[dict[str, object]], predicted: list[dict[str, object]]) -> list[tuple[str, int | None, int | None]]:
    rows, columns = len(reference) + 1, len(predicted) + 1
    costs = [[0] * columns for _ in range(rows)]
    moves = [[""] * columns for _ in range(rows)]
    for row in range(1, rows):
        costs[row][0], moves[row][0] = row, "deletion"
    for column in range(1, columns):
        costs[0][column], moves[0][column] = column, "insertion"
    priority = {"substitution": 0, "deletion": 1, "insertion": 2}
    for row in range(1, rows):
        for column in range(1, columns):
            if reference[row - 1]["form"] == predicted[column - 1]["form"]:
                costs[row][column], moves[row][column] = costs[row - 1][column - 1], "equal"
            else:
                candidates = (
                    (costs[row - 1][column - 1] + 1, "substitution"),
                    (costs[row - 1][column] + 1, "deletion"),
                    (costs[row][column - 1] + 1, "insertion"),
                )
                costs[row][column], moves[row][column] = min(
                    candidates, key=lambda item: (item[0], priority[item[1]])
                )
    result: list[tuple[str, int | None, int | None]] = []
    row, column = len(reference), len(predicted)
    while row or column:
        operation = moves[row][column]
        if operation in {"equal", "substitution"}:
            result.append((operation, row - 1, column - 1))
            row -= 1
            column -= 1
        elif operation == "deletion":
            result.append((operation, row - 1, None))
            row -= 1
        elif operation == "insertion":
            result.append((operation, None, column - 1))
            column -= 1
        else:
            raise ValueError("Undefined alignment backtrace")
    result.reverse()
    return result


def ner_spans(words: list[dict[str, object]]) -> set[tuple[int, int, str]]:
    spans: set[tuple[int, int, str]] = set()
    start = end = None
    entity_type = ""
    for word in words + [{"id": -1, "misc": "NER=O"}]:
        match = re.search(r"(?:^|\|)NER=([^|]+)", str(word["misc"]))
        tag = match.group(1) if match else "O"
        if tag.startswith("B-") or tag == "O" or (tag.startswith("I-") and tag[2:] != entity_type):
            if start is not None:
                spans.add((start, end, entity_type))
            start = end = None
            entity_type = ""
        if tag.startswith("B-") or (tag.startswith("I-") and start is None):
            start = end = int(word["id"])
            entity_type = tag[2:]
        elif tag.startswith("I-") and start is not None:
            end = int(word["id"])
    return spans


def rate(numerator: int, denominator: int) -> str:
    return f"{numerator / denominator:.6f}" if denominator else ""


def gries_dp(term_counts: list[int], part_token_counts: list[int]) -> float | None:
    """Return Gries's DP; zero means proportional spread, larger means concentration."""
    frequency = sum(term_counts)
    total_tokens = sum(part_token_counts)
    if frequency == 0:
        return None
    if total_tokens == 0 or len(term_counts) != len(part_token_counts):
        raise ValueError("DP requires matching non-empty corpus-part denominators")
    observed = [count / frequency for count in term_counts]
    expected = [count / total_tokens for count in part_token_counts]
    return 0.5 * sum(abs(observed_value - expected_value) for observed_value, expected_value in zip(observed, expected))


def classla_outputs(samples: dict[str, dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    metadata = json.loads((PACKET / "interim/classla/model-run.json").read_text(encoding="utf-8"))
    for name, expected in metadata["output_sha256"].items():
        if sha256(PACKET / "interim/classla" / name) != expected:
            raise ValueError(f"Frozen CLASSLA output changed without metadata: {name}")
    evaluations: list[dict[str, object]] = []
    errors: list[dict[str, object]] = []
    parsed: dict[str, dict[str, object]] = {}

    causal_rules = csv_rows(PACKET / "reference/classla-causal-decisions.csv")
    causal_lookup: dict[tuple[str, str, str], dict[str, str]] = {}
    for causal_rule in causal_rules:
        validate_review_state(
            causal_rule,
            status_field="review_status",
            draft_status=CAUSAL_DRAFT_STATUS,
            context=f"causal decision {causal_rule['causal_rule_id']}",
        )
        for causal_sample_id in causal_rule["sample_ids"].split("|"):
            for causal_layer in causal_rule["layers"].split("|"):
                key = (causal_sample_id, causal_rule["form"], causal_layer)
                if key in causal_lookup:
                    raise ValueError(f"Duplicate causal decision for {key}")
                causal_lookup[key] = causal_rule

    def add_metric(
        sample_id: str,
        stratum: str,
        layer: str,
        metric: str,
        numerator: int,
        denominator: int,
        rule: str,
        *,
        alignment_unit: str,
        reference_item_count: int,
        predicted_item_count: int,
        aligned_reference_items: int,
        aligned_predicted_items: int,
        substitutions: int,
        insertions: int,
        deletions: int,
        excluded_reference_items: int,
        excluded_predicted_items: int,
        exclusion_rule: str,
    ) -> None:
        evaluations.append(
            {
                "sample_id": sample_id,
                "stratum": stratum,
                "layer": layer,
                "metric": metric,
                "numerator": numerator,
                "denominator": denominator,
                "value": rate(numerator, denominator),
                "eligible_rule": rule,
                "alignment_unit": alignment_unit,
                "reference_item_count": reference_item_count,
                "predicted_item_count": predicted_item_count,
                "aligned_reference_items": aligned_reference_items,
                "aligned_predicted_items": aligned_predicted_items,
                "substitutions": substitutions,
                "insertions": insertions,
                "deletions": deletions,
                "excluded_reference_items": excluded_reference_items,
                "excluded_predicted_items": excluded_predicted_items,
                "exclusion_rule": exclusion_rule,
            }
        )

    def risk(layer: str) -> str:
        return {
            "tokenization": "Token counts, word lookup and every later word-indexed layer can diverge.",
            "lemma": "Lemma queries and lexical frequency can omit or misgroup the occurrence.",
            "upos": "A grammatical-category filter can include or exclude the occurrence.",
            "morphology": "A feature query can assign the wrong grammatical role or comparison group.",
            "dependency_uas": "A relation query can attach the occurrence to the wrong governor.",
            "dependency_las": "A construction query can assign the wrong head or relation.",
            "ner": "Entity counts or linking candidates can change.",
        }[layer]

    def add_error(sample_id: str, stratum: str, locator: str, layer: str, operation: str, ref: dict[str, object] | None, pred: dict[str, object] | None, reference_value: str, predicted_value: str) -> None:
        form = str((ref or pred or {}).get("form", ""))
        ambiguous = form == "vse"
        causal_rule = causal_lookup.get((sample_id, form, layer))
        if causal_rule:
            causal_rule_id = causal_rule["causal_rule_id"]
            likely_origin = causal_rule["likely_causal_origin"]
            also_in_reference = causal_rule["also_occurs_in_reference_transcription"]
            review_status = causal_rule["review_status"]
        else:
            causal_rule_id = ""
            likely_origin = (
                "provider_ocr_conditioned"
                if stratum == "provider_ocr"
                else "model_reference_disagreement"
            )
            also_in_reference = "false"
            review_status = CAUSAL_DRAFT_STATUS
        errors.append(
            {
                "error_id": f"TNLP-ERR-{len(errors) + 1:03d}",
                "sample_id": sample_id,
                "input_stratum": stratum,
                "source_locator": locator,
                "reference_token_id": "" if ref is None else ref["id"],
                "predicted_token_id": "" if pred is None else pred["id"],
                "form": form,
                "layer": layer,
                "alignment_status": operation,
                "immediate_disagreement": f"{operation}: reference={reference_value}; prediction={predicted_value}",
                "reference_value": reference_value,
                "predicted_value": predicted_value,
                "error_family": "ambiguity" if ambiguous else ("segmentation" if layer == "tokenization" else {"lemma": "lexical", "upos": "morphosyntactic", "morphology": "morphosyntactic", "dependency_uas": "dependency", "dependency_las": "dependency", "ner": "entity"}[layer]),
                "causal_rule_id": causal_rule_id,
                "likely_causal_origin": likely_origin,
                "also_occurs_in_reference_transcription": also_in_reference,
                "interpretive_risk": risk(layer),
                "review_status": review_status,
            }
        )

    for sample_id, sample in samples.items():
        stratum = str(sample["stratum"])
        locator = f"{sample['source_path']}#{sample['source_record_id']}:{sample['selector']}"
        reference_doc = parse_conllu(PACKET / "reference/classla" / f"{sample_id}.conllu")
        predicted_doc = parse_conllu(PACKET / "interim/classla" / f"{sample_id}.conllu")
        reference_comments = {
            key: values[0] if values else ""
            for key, values in reference_doc["comments"].items()
        }
        validate_review_state(
            reference_comments,
            status_field="reference_status",
            draft_status=REFERENCE_DRAFT_STATUS,
            context=f"CLASSLA reference {sample_id}",
            reviewer_field="human_reviewer",
            date_field="human_reviewed_on",
            scope_field="human_review_scope",
        )
        reference = reference_doc["words"]
        predicted = predicted_doc["words"]
        alignment = align_words(reference, predicted)
        equal = [(ri, pi) for op, ri, pi in alignment if op == "equal" and ri is not None and pi is not None]
        operations = Counter(op for op, _, _ in alignment)
        mapping = {int(reference[ri]["id"]): int(predicted[pi]["id"]) for ri, pi in equal}

        reference_sentences = reference_doc["comments"].get("text", [])
        predicted_sentences = predicted_doc["comments"].get("text", [])
        correct_sentences = len(reference_sentences) if reference_sentences == predicted_sentences else 0
        sentence_substitutions = min(len(reference_sentences), len(predicted_sentences)) - correct_sentences
        sentence_accounting = {
            "alignment_unit": "exact sentence text",
            "reference_item_count": len(reference_sentences),
            "predicted_item_count": len(predicted_sentences),
            "aligned_reference_items": correct_sentences,
            "aligned_predicted_items": correct_sentences,
            "substitutions": sentence_substitutions,
            "insertions": max(0, len(predicted_sentences) - len(reference_sentences)),
            "deletions": max(0, len(reference_sentences) - len(predicted_sentences)),
            "excluded_reference_items": len(reference_sentences) - correct_sentences,
            "excluded_predicted_items": len(predicted_sentences) - correct_sentences,
            "exclusion_rule": "non-identical sentence texts are excluded from exact-span matches",
        }
        add_metric(sample_id, stratum, "sentence_boundary", "precision", correct_sentences, len(predicted_sentences), "exact sentence spans; denominator is predicted sentences", **sentence_accounting)
        add_metric(sample_id, stratum, "sentence_boundary", "recall", correct_sentences, len(reference_sentences), "exact sentence spans; denominator is reference sentences", **sentence_accounting)
        add_metric(sample_id, stratum, "sentence_boundary", "f1", 2 * correct_sentences, len(predicted_sentences) + len(reference_sentences), "2 × exact spans / (predicted + reference sentences)", **sentence_accounting)

        word_accounting = {
            "alignment_unit": "word FORM",
            "reference_item_count": len(reference),
            "predicted_item_count": len(predicted),
            "aligned_reference_items": len(equal),
            "aligned_predicted_items": len(equal),
            "substitutions": operations["substitution"],
            "insertions": operations["insertion"],
            "deletions": operations["deletion"],
            "excluded_reference_items": operations["substitution"] + operations["deletion"],
            "excluded_predicted_items": operations["substitution"] + operations["insertion"],
            "exclusion_rule": "non-identical FORM alignments are excluded from downstream label scoring",
        }
        add_metric(sample_id, stratum, "tokenization", "reference_token_agreement", len(equal), len(reference), "identical one-to-one word FORM alignments / reference word tokens", **word_accounting)
        for operation, ri, pi in alignment:
            if operation == "equal":
                continue
            ref = reference[ri] if ri is not None else None
            pred = predicted[pi] if pi is not None else None
            add_error(sample_id, stratum, locator, "tokenization", operation, ref, pred, "<missing>" if ref is None else str(ref["form"]), "<missing>" if pred is None else str(pred["form"]))

        for field, layer in (("lemma", "lemma"), ("upos", "upos"), ("feats", "morphology")):
            correct = 0
            for ri, pi in equal:
                ref, pred = reference[ri], predicted[pi]
                if ref[field] == pred[field]:
                    correct += 1
                else:
                    add_error(sample_id, stratum, locator, layer, "equal_form", ref, pred, str(ref[field]), str(pred[field]))
            metric = "exact_feature_set_accuracy" if field == "feats" else "accuracy"
            add_metric(sample_id, stratum, layer, metric, correct, len(equal), "exact label on identical one-to-one FORM alignments", **word_accounting)

        eligible_dependencies = []
        uas = las = 0
        for ri, pi in equal:
            ref, pred = reference[ri], predicted[pi]
            if ref["upos"] == "PUNCT":
                continue
            ref_head = int(ref["head"])
            if ref_head != 0 and ref_head not in mapping:
                continue
            eligible_dependencies.append((ref, pred))
            expected_head = 0 if ref_head == 0 else mapping[ref_head]
            head_correct = int(pred["head"]) == expected_head
            label_correct = head_correct and pred["deprel"] == ref["deprel"]
            uas += int(head_correct)
            las += int(label_correct)
            if not head_correct:
                add_error(sample_id, stratum, locator, "dependency_uas", "equal_form", ref, pred, str(expected_head), str(pred["head"]))
            if not label_correct:
                add_error(sample_id, stratum, locator, "dependency_las", "equal_form", ref, pred, f"{expected_head}:{ref['deprel']}", f"{pred['head']}:{pred['deprel']}")
        dependency_rule = "aligned non-punctuation words whose reference head is root or has an identical-FORM alignment"
        reference_non_punct = sum(word["upos"] != "PUNCT" for word in reference)
        predicted_non_punct = sum(word["upos"] != "PUNCT" for word in predicted)
        dependency_accounting = word_accounting | {
            "reference_item_count": reference_non_punct,
            "predicted_item_count": predicted_non_punct,
            "aligned_reference_items": len(eligible_dependencies),
            "aligned_predicted_items": len(eligible_dependencies),
            "excluded_reference_items": reference_non_punct - len(eligible_dependencies),
            "excluded_predicted_items": predicted_non_punct - len(eligible_dependencies),
            "exclusion_rule": "punctuation, non-identical FORM alignments and words whose reference head cannot be aligned are excluded",
        }
        add_metric(sample_id, stratum, "dependency", "UAS", uas, len(eligible_dependencies), dependency_rule, **dependency_accounting)
        add_metric(sample_id, stratum, "dependency", "LAS", las, len(eligible_dependencies), dependency_rule, **dependency_accounting)

        reference_spans = ner_spans(reference)
        predicted_spans = ner_spans(predicted)
        mapped_spans = set()
        for start, end, kind in reference_spans:
            ids = list(range(start, end + 1))
            if all(item in mapping for item in ids):
                mapped = [mapping[item] for item in ids]
                if mapped == list(range(mapped[0], mapped[-1] + 1)):
                    mapped_spans.add((mapped[0], mapped[-1], kind))
        correct_spans = len(mapped_spans & predicted_spans)
        ner_accounting = {
            "alignment_unit": "exact typed entity span after word-FORM alignment",
            "reference_item_count": len(reference_spans),
            "predicted_item_count": len(predicted_spans),
            "aligned_reference_items": len(mapped_spans),
            "aligned_predicted_items": len(predicted_spans),
            "substitutions": 0,
            "insertions": len(predicted_spans - mapped_spans),
            "deletions": len(mapped_spans - predicted_spans),
            "excluded_reference_items": len(reference_spans) - len(mapped_spans),
            "excluded_predicted_items": 0,
            "exclusion_rule": "reference spans crossing non-identical word-FORM alignments cannot enter strict span scoring",
        }
        add_metric(sample_id, stratum, "ner", "strict_span_precision", correct_spans, len(predicted_spans), "exact aligned word span and entity type / predicted spans", **ner_accounting)
        add_metric(sample_id, stratum, "ner", "strict_span_recall", correct_spans, len(reference_spans), "exact aligned word span and entity type / reference spans", **ner_accounting)
        add_metric(sample_id, stratum, "ner", "strict_span_f1", 2 * correct_spans, len(predicted_spans) + len(reference_spans), "2 × exact typed spans / (predicted + reference spans)", **ner_accounting)
        for span in sorted(mapped_spans - predicted_spans):
            add_error(sample_id, stratum, locator, "ner", "aligned_span", None, None, f"{span[0]}-{span[1]}:{span[2]}", "<missing>")
        for span in sorted(predicted_spans - mapped_spans):
            add_error(sample_id, stratum, locator, "ner", "aligned_span", None, None, "<missing>", f"{span[0]}-{span[1]}:{span[2]}")
        parsed[sample_id] = {"reference": reference, "predicted": predicted, "reference_spans": reference_spans, "predicted_spans": predicted_spans}

    consequences = []
    historical = ("TNLP-AF-REF", "TNLP-AF-OCR")
    ref_pronoun_subject = sum(word["form"] == "vse" and word["upos"] == "PRON" and word["deprel"] == "nsubj" for sample_id in historical for word in parsed[sample_id]["reference"])
    pred_pronoun_subject = sum(word["form"] == "vse" and word["upos"] == "PRON" and word["deprel"] == "nsubj" for sample_id in historical for word in parsed[sample_id]["predicted"])
    ref_acl = sum(word["deprel"] == "acl" for word in parsed["TNLP-AF-OCR"]["reference"])
    pred_acl = sum(word["deprel"] == "acl" for word in parsed["TNLP-AF-OCR"]["predicted"])
    ref_entities = sum(len(parsed[sample_id]["reference_spans"]) for sample_id in parsed)
    pred_entities = sum(len(parsed[sample_id]["predicted_spans"]) for sample_id in parsed)
    ref_stranko_oblique = sum(
        word["form"] == "stranko" and word["deprel"] == "obl"
        for sample_id in historical
        for word in parsed[sample_id]["reference"]
    )
    pred_stranko_oblique = sum(
        word["form"] == "stranko" and word["deprel"] == "obl"
        for sample_id in historical
        for word in parsed[sample_id]["predicted"]
    )
    for consequence_id, operation, layer, automatic, reference_value, interpretation in (
        ("TNLP-DOWN-01", "count vse as a pronominal subject in the two historical layers", "UPOS+dependency", pred_pronoun_subject, ref_pronoun_subject, "The automatic query omits both draft-reference subject readings."),
        ("TNLP-DOWN-02", "count relative acl relations in the provider-OCR sentence", "dependency", pred_acl, ref_acl, "OCR damage to ki changes the clause attachment in this sentence."),
        ("TNLP-DOWN-03", "count exact typed entity spans across all four samples", "NER", pred_entities, ref_entities, "The entity-span conclusion survives the draft-reference corrections in this tiny sample."),
        ("TNLP-DOWN-04", "count instrumental stranko as an oblique in the two historical layers", "dependency", pred_stranko_oblique, ref_stranko_oblique, "The frozen parser attaches stranko to naziranja in both layers and misses both draft-reference clause-level obliques."),
    ):
        consequences.append({"consequence_id": consequence_id, "operation": operation, "layer": layer, "automatic_count": automatic, "reference_count": reference_value, "delta_reference_minus_automatic": reference_value - automatic, "interpretation": interpretation, "scope": "four purposive teaching sentences; no population inference"})
    return evaluations, errors, consequences


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(normalized(text).lower())


def indexed_source_sentences(documents: list[dict[str, str]]) -> dict[str, str]:
    result: dict[str, str] = {}
    for document in documents:
        doc_id = document["doc_id"]
        for index, sentence in enumerate(split_sentences(document["text"]), start=1):
            sentence_id = f"{doc_id}.s{index}"
            if sentence_id in result:
                raise ValueError(f"Duplicate source sentence ID: {sentence_id}")
            result[sentence_id] = sentence
    return result


def text_analysis_outputs() -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], dict[str, int]]:
    documents = csv_rows(PACKET / "source/contemporary-sample.csv")
    if len(documents) != 12 or any(row["synthetic"] != "true" for row in documents):
        raise ValueError("The contemporary teaching corpus must contain twelve declared synthetic documents")
    by_document = {row["doc_id"]: tokenize(row["text"]) for row in documents}
    total_tokens = sum(map(len, by_document.values()))
    summaries = [
        {"doc_id": row["doc_id"], "title": row["title"], "theme": row["theme"], "eligible_tokens": len(by_document[row["doc_id"]]), "synthetic": row["synthetic"], "rights_status": row["rights_status"]}
        for row in documents
    ]
    all_terms = sorted({token for tokens in by_document.values() for token in tokens})
    frequency_rows: list[dict[str, object]] = []
    concordances: list[dict[str, object]] = []
    doc_theme = {row["doc_id"]: row["theme"] for row in documents}
    doc_title = {row["doc_id"]: row["title"] for row in documents}
    part_token_counts = [
        sum(len(tokens) for doc_id, tokens in by_document.items() if doc_theme[doc_id] == theme)
        for theme in THEMES
    ]
    term_counts: dict[str, int] = {}
    term_df: dict[str, int] = {}
    for term in all_terms:
        counts = {doc_id: tokens.count(term) for doc_id, tokens in by_document.items()}
        frequency = sum(counts.values())
        document_frequency = sum(value > 0 for value in counts.values())
        group_counts = [sum(value for doc_id, value in counts.items() if doc_theme[doc_id] == theme) for theme in THEMES]
        dispersion = gries_dp(group_counts, part_token_counts)
        term_counts[term], term_df[term] = frequency, document_frequency
        frequency_rows.append(
            {
                "term": term,
                "frequency": frequency,
                "eligible_token_denominator": total_tokens,
                "normalized_per_10000": f"{frequency / total_tokens * 10000:.6f}",
                "document_frequency": document_frequency,
                "document_denominator": len(documents),
                "document_share": f"{document_frequency / len(documents):.6f}",
                "gries_dp": "" if dispersion is None else f"{dispersion:.6f}",
                "dispersion_formula": "0.5 * sum_i(abs(term_count_i/frequency - part_tokens_i/total_tokens))",
                "dispersion_direction": "0 = proportional to corpus-part sizes; larger = more concentrated",
                "dispersion_partition": "four authored theme groups; unequal eligible-token totals",
                **{
                    key: value
                    for theme, part_tokens, count in zip(THEMES, part_token_counts, group_counts)
                    for key, value in (
                        (f"{theme}_eligible_tokens", part_tokens),
                        (f"{theme}_term_count", count),
                    )
                },
            }
        )
        occurrence = 0
        for row in documents:
            tokens = by_document[row["doc_id"]]
            for index, token in enumerate(tokens):
                if token != term:
                    continue
                occurrence += 1
                concordances.append(
                    {
                        "term": term,
                        "occurrence_id": f"{term}-{occurrence:03d}",
                        "doc_id": row["doc_id"],
                        "title": row["title"],
                        "theme": row["theme"],
                        "token_index": index + 1,
                        "left_context": " ".join(tokens[max(0, index - 5):index]),
                        "match": token,
                        "right_context": " ".join(tokens[index + 1:index + 6]),
                        "source_locator": f"source/contemporary-sample.csv#{row['doc_id']}",
                    }
                )
    frequency_rows.sort(key=lambda row: (-int(row["frequency"]), str(row["term"])))
    concordances.sort(key=lambda row: (str(row["term"]), str(row["doc_id"]), int(row["token_index"])))

    selected = ("svoboda", "arhiv", "raziskovalci", "korpus")
    sensitivity: list[dict[str, object]] = []
    for setting, values, denominator, note in (
        ("raw_token_frequency", term_counts, total_tokens, "counts every exact lower-case surface-form token"),
        ("document_frequency", term_df, len(documents), "counts each document at most once"),
    ):
        ordered = sorted(selected, key=lambda term: (-values[term], term))
        for rank, term in enumerate(ordered, start=1):
            sensitivity.append({"setting": setting, "term": term, "numerator": values[term], "denominator": denominator, "value": f"{values[term] / denominator:.6f}", "rank": rank, "tie_rule": "descending numerator, then Unicode term", "interpretation": note})
    selected_dispersion = {
        term: gries_dp(
            [
                sum(
                    by_document[doc_id].count(term)
                    for doc_id in by_document
                    if doc_theme[doc_id] == theme
                )
                for theme in THEMES
            ],
            part_token_counts,
        )
        for term in selected
    }
    return summaries, frequency_rows, concordances, sensitivity, {
        "total_tokens": total_tokens,
        **{f"part_tokens_{theme}": count for theme, count in zip(THEMES, part_token_counts)},
        **{f"frequency_{term}": term_counts[term] for term in selected},
        **{f"df_{term}": term_df[term] for term in selected},
        **{f"gries_dp_{term}": round(float(selected_dispersion[term]), 6) for term in selected},
    }


def jaccard(left: set[str], right: set[str]) -> tuple[int, int, float]:
    intersection, union = len(left & right), len(left | right)
    return intersection, union, intersection / union if union else 1.0


def topic_outputs() -> tuple[list[dict[str, object]], list[dict[str, object]], dict[str, int]]:
    metadata = json.loads((PACKET / "interim/topics/model-run.json").read_text(encoding="utf-8"))
    for name, expected in metadata["output_sha256"].items():
        if sha256(PACKET / "interim/topics" / name) != expected:
            raise ValueError(f"Frozen NMF output changed without metadata: {name}")
    rows = csv_rows(PACKET / "interim/topics/topic-components.csv")
    topic_documents = csv_rows(PACKET / "interim/topics/topic-documents.csv")
    source_documents = csv_rows(PACKET / "source/contemporary-sample.csv")
    source_document_ids = {row["doc_id"] for row in source_documents}
    source_sentences = indexed_source_sentences(source_documents)
    top_documents: dict[tuple[int, int, int], list[str]] = defaultdict(list)
    for row in sorted(topic_documents, key=lambda item: (int(item["component_count"]), int(item["seed"]), int(item["topic_id"]), int(item["rank"]))):
        if row["doc_id"] not in source_document_ids:
            raise ValueError(f"Frozen topic document is absent from the source corpus: {row['doc_id']}")
        top_documents[(int(row["component_count"]), int(row["seed"]), int(row["topic_id"]))].append(row["doc_id"])

    paired_interpretations = []
    for path in (
        PACKET / "reference/topic-interpretation.csv",
        PACKET / "reference/topic-interpretation.sl.csv",
    ):
        interpretation_rows = csv_rows(path)
        paired_interpretations.append(interpretation_rows)
        for row in interpretation_rows:
            key = (int(row["component_count"]), int(row["seed"]), int(row["topic_id"]))
            declared_documents = row["high_weight_documents"].split("|")
            if declared_documents != top_documents[key]:
                raise ValueError(f"{path.name}: high-weight document IDs drifted for {key}")
            inspected_ids = row["inspected_sentence_ids"].split("|")
            if any(sentence_id not in source_sentences for sentence_id in inspected_ids):
                raise ValueError(f"{path.name}: inspected sentence ID does not resolve for {key}")
            if {sentence_id.split(".s", 1)[0] for sentence_id in inspected_ids} != set(declared_documents):
                raise ValueError(f"{path.name}: each high-weight document needs an inspected source sentence for {key}")
            contradictory_document = row["contradictory_document"]
            contradictory_sentence = row["contradictory_sentence_id"]
            if contradictory_document not in source_document_ids or contradictory_sentence not in source_sentences:
                raise ValueError(f"{path.name}: contradictory source locator does not resolve for {key}")
            if not contradictory_sentence.startswith(f"{contradictory_document}.s"):
                raise ValueError(f"{path.name}: contradictory document/sentence mismatch for {key}")
            validate_review_state(
                row,
                status_field="review_status",
                draft_status="machine-assisted interpretation draft; pending human review",
                context=f"{path.name}: interpretation {key}",
            )
    structural_fields = (
        "component_count",
        "seed",
        "topic_id",
        "high_weight_documents",
        "inspected_sentence_ids",
        "contradictory_document",
        "contradictory_sentence_id",
        "review_status",
        "reviewer",
        "reviewed_on",
        "review_scope",
    )
    if [tuple(row[field] for field in structural_fields) for row in paired_interpretations[0]] != [tuple(row[field] for field in structural_fields) for row in paired_interpretations[1]]:
        raise ValueError("English and Slovene topic-interpretation locators or status differ")

    topics = {
        (int(row["component_count"]), int(row["seed"]), int(row["topic_id"])): set(row["top_terms"].split("|"))
        for row in rows
    }
    stability: list[dict[str, object]] = []
    unstable = 0
    for count in metadata["nmf"]["component_counts"]:
        reference_ids = list(range(1, count + 1))
        for comparison_seed in metadata["nmf"]["seeds"]:
            if comparison_seed == 7:
                continue
            candidates = []
            for permutation in itertools.permutations(reference_ids):
                overlaps = [jaccard(topics[(count, 7, ref_id)], topics[(count, comparison_seed, comp_id)])[2] for ref_id, comp_id in zip(reference_ids, permutation)]
                candidates.append((sum(overlaps), permutation, overlaps))
            best_score = max(item[0] for item in candidates)
            best = min((item for item in candidates if abs(item[0] - best_score) < 1e-12), key=lambda item: item[1])
            for ref_id, comp_id, overlap in zip(reference_ids, best[1], best[2]):
                intersection, union, _ = jaccard(topics[(count, 7, ref_id)], topics[(count, comparison_seed, comp_id)])
                status = "stable_at_teaching_threshold" if overlap >= TOPIC_STABILITY_THRESHOLD else "unstable"
                unstable += status == "unstable"
                stability.append(
                    {
                        "component_count": count,
                        "reference_seed": 7,
                        "reference_topic": ref_id,
                        "comparison_seed": comparison_seed,
                        "comparison_topic": comp_id,
                        "intersection_count": intersection,
                        "union_count": union,
                        "jaccard": f"{overlap:.6f}",
                        "threshold": f"{TOPIC_STABILITY_THRESHOLD:.2f}",
                        "status": status,
                        "reference_terms": "|".join(sorted(topics[(count, 7, ref_id)])),
                        "comparison_terms": "|".join(sorted(topics[(count, comparison_seed, comp_id)])),
                        "matching_rule": "maximum-total one-to-one Jaccard assignment; lexicographic topic-ID tie break",
                    }
                )

    count_sensitivity: list[dict[str, object]] = []
    unmatched = 0
    for target_count in (2, 4):
        selected_targets = set()
        for ref_id in (1, 2, 3):
            candidates = []
            for target_id in range(1, target_count + 1):
                intersection, union, overlap = jaccard(topics[(3, 7, ref_id)], topics[(target_count, 7, target_id)])
                candidates.append((overlap, target_id, intersection, union))
            overlap, target_id, intersection, union = max(candidates, key=lambda item: (item[0], -item[1]))
            selected_targets.add(target_id)
            count_sensitivity.append(
                {"reference_count": 3, "reference_topic": ref_id, "comparison_count": target_count, "comparison_topic": target_id, "intersection_count": intersection, "union_count": union, "jaccard": f"{overlap:.6f}", "relation_status": "best_overlap_not_topic_identity", "reference_terms": "|".join(sorted(topics[(3, 7, ref_id)])), "comparison_terms": "|".join(sorted(topics[(target_count, 7, target_id)])), "matching_rule": "independent best top-term Jaccard; lower comparison ID breaks ties"}
            )
        for target_id in sorted(set(range(1, target_count + 1)) - selected_targets):
            unmatched += 1
            count_sensitivity.append(
                {"reference_count": 3, "reference_topic": "", "comparison_count": target_count, "comparison_topic": target_id, "intersection_count": 0, "union_count": len(topics[(target_count, 7, target_id)]), "jaccard": "", "relation_status": "unmatched_comparison_topic", "reference_terms": "", "comparison_terms": "|".join(sorted(topics[(target_count, 7, target_id)])), "matching_rule": "retained because no three-component source selected this destination"}
            )
    return stability, count_sensitivity, {"topic_stability_rows": len(stability), "unstable_topic_matches": unstable, "unmatched_count_topics": unmatched}


def emotion_outputs() -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], dict[str, int]]:
    annotations = csv_rows(PACKET / "reference/emotion-annotations.csv")
    lexicon = csv_rows(PACKET / "reference/teaching-emotion-lexicon.csv")
    additions = csv_rows(PACKET / "reference/emotion-sensitivity-additions.csv")
    documents = csv_rows(PACKET / "source/contemporary-sample.csv")
    source_sentences = indexed_source_sentences(documents)

    def evaluate(entries: list[dict[str, str]]) -> tuple[list[dict[str, object]], Counter[str]]:
        lookup: dict[str, list[str]] = defaultdict(list)
        for entry in entries:
            lookup[entry["form"].lower()].append(entry["emotion"])
        result = []
        outcomes: Counter[str] = Counter()
        for row in annotations:
            sentence_id = f"{row['doc_id']}.s{row['sentence_index']}"
            if sentence_id not in source_sentences:
                raise ValueError(f"Emotion annotation source sentence does not resolve: {sentence_id}")
            validate_review_state(
                row,
                status_field="review_status",
                draft_status=REFERENCE_DRAFT_STATUS,
                context=f"emotion annotation {row['annotation_id']}",
            )
            source_text = source_sentences[sentence_id]
            matches = [(token, emotion) for token in tokenize(source_text) for emotion in lookup.get(token, [])]
            predicted = bool(matches)
            reference_present = row["emotion_present"] == "true"
            outcome = "TP" if predicted and reference_present else "FP" if predicted else "FN" if reference_present else "TN"
            outcomes[outcome] += 1
            result.append(
                {
                    "annotation_id": row["annotation_id"],
                    "doc_id": row["doc_id"],
                    "sentence_index": row["sentence_index"],
                    "sentence_id": sentence_id,
                    "source_text": source_text,
                    "source_locator": f"source/contemporary-sample.csv#{sentence_id}",
                    "lexicon_matches": "|".join(f"{form}:{emotion}" for form, emotion in matches),
                    "match_count": len(matches),
                    "predicted_emotion_present": str(predicted).lower(),
                    "draft_reference_emotion_present": row["emotion_present"],
                    "draft_reference_emotion": row["emotion"],
                    "reference_review_status": row["review_status"],
                    "reviewer": row["reviewer"],
                    "reviewed_on": row["reviewed_on"],
                    "review_scope": row["review_scope"],
                    "experiencer": row["experiencer"],
                    "target": row["target"],
                    "voice": row["voice"],
                    "quotation": row["quotation"],
                    "negation": row["negation"],
                    "irony": row["irony"],
                    "uncertain": row["uncertain"],
                    "binary_outcome": outcome,
                    "rationale": row["rationale"],
                }
            )
        return result, outcomes

    baseline, baseline_counts = evaluate(lexicon)
    sensitivity = []
    variant_counts = {}
    for variant, entries, note in (
        ("baseline_exact_form", lexicon, "predeclared eight-form teaching baseline"),
        ("add_documented_bali_form", lexicon + additions, "development variant designed after observing the baseline false negative; requires new-data evaluation"),
    ):
        _, counts = evaluate(entries)
        variant_counts[variant] = counts
        precision_den = counts["TP"] + counts["FP"]
        recall_den = counts["TP"] + counts["FN"]
        f1_num = 2 * counts["TP"]
        f1_den = 2 * counts["TP"] + counts["FP"] + counts["FN"]
        sensitivity.append(
            {
                "variant": variant,
                "lexicon_entries": len(entries),
                "TP": counts["TP"], "FP": counts["FP"], "TN": counts["TN"], "FN": counts["FN"],
                "precision_numerator": counts["TP"], "precision_denominator": precision_den, "precision": rate(counts["TP"], precision_den),
                "recall_numerator": counts["TP"], "recall_denominator": recall_den, "recall": rate(counts["TP"], recall_den),
                "f1_numerator": f1_num, "f1_denominator": f1_den, "f1": rate(f1_num, f1_den),
                "zero_match_sentences": sum(not row["lexicon_matches"] for row in evaluate(entries)[0]),
                "development_note": note,
            }
        )
    method_comparison = [
        {"method": "exact-form teaching lexicon", "unit": "sentence", "input_representation": "Unicode-NFC lower-case source forms", "output": "declared form/category matches and binary presence", "validation_evidence": "eight machine-assisted draft cases; TP/FP/TN/FN and exact counts; human review pending", "supported_claim": "which declared forms match in this sample", "unsupported_claim": "who actually experiences emotion", "gain": "transparent and reproducible", "loss": "inflection and context", "known_failure": "quoted, negated, metalinguistic and ironic uses"},
        {"method": "draft contextual annotation", "unit": "source sentence with document context", "input_representation": "sentence resolved by stable ID plus codebook", "output": "presence, category, experiencer, target, voice, negation, irony and uncertainty", "validation_evidence": "one machine-assisted reference draft; no competent human review or agreement estimate", "supported_claim": "how the draft codebook was applied", "unsupported_claim": "objective psychological state or population prevalence", "gain": "roles, source identity and context remain visible", "loss": "labour and reviewer dependence", "known_failure": "reasonable disagreement and unresolved irony"},
        {"method": "supervised classifier", "unit": "not fitted", "input_representation": "would require labelled train/validation/test units", "output": "deliberately omitted", "validation_evidence": "eight purpose-built cases are inadequate", "supported_claim": "none for this packet", "unsupported_claim": "predictive performance", "gain": "omission prevents leakage and decorative modelling", "loss": "no automated contextual baseline", "known_failure": "a fitted toy model would memorize wording or source"},
    ]
    return baseline, sensitivity, method_comparison, {"emotion_examples": len(annotations), "emotion_zero_matches": sum(not row["lexicon_matches"] for row in baseline), **{f"emotion_baseline_{key.lower()}": baseline_counts[key] for key in ("TP", "FP", "TN", "FN")}, **{f"emotion_extended_{key.lower()}": variant_counts["add_documented_bali_form"][key] for key in ("TP", "FP", "TN", "FN")}}


def generated_outputs() -> dict[Path, bytes]:
    samples, sample_map = annotation_samples()
    evaluations, errors, consequences = classla_outputs(sample_map)
    document_summary, frequencies, concordances, frequency_sensitivity, text_expected = text_analysis_outputs()
    topic_stability, topic_count_sensitivity, topic_expected = topic_outputs()
    emotion_baseline, emotion_sensitivity, method_comparison, emotion_expected = emotion_outputs()
    reference_metadata = simple_frontmatter(PACKET / "reference/classla-reference-policy.md")
    validate_review_state(
        reference_metadata,
        status_field="reference_status",
        draft_status=REFERENCE_DRAFT_STATUS,
        context="CLASSLA reference policy",
        reviewer_field="human_reviewer",
        date_field="human_reviewed_on",
        scope_field="human_review_scope",
    )
    expected = {
        "packet_version": 1,
        "reference_review": {
            "status": reference_metadata["reference_status"],
            "reviewer": reference_metadata.get("human_reviewer", ""),
            "reviewed_on": reference_metadata.get("human_reviewed_on", ""),
            "review_scope": reference_metadata.get("human_review_scope", ""),
        },
        "annotation_samples": len(samples),
        "contemporary_documents": len(document_summary),
        "all_contemporary_documents_synthetic": all(row["synthetic"] == "true" for row in document_summary),
        "classla_evaluation_rows": len(evaluations),
        "classla_error_rows": len(errors),
        "downstream_consequence_rows": len(consequences),
        **text_expected,
        **topic_expected,
        **emotion_expected,
    }
    return {
        PACKET / "raw/annotation-samples.csv": csv_bytes(samples),
        PACKET / "output/document-summary.csv": csv_bytes(document_summary),
        PACKET / "output/frequency-dispersion.csv": csv_bytes(frequencies),
        PACKET / "output/concordance.csv": csv_bytes(concordances),
        PACKET / "output/frequency-sensitivity.csv": csv_bytes(frequency_sensitivity),
        PACKET / "output/classla-evaluation.csv": csv_bytes(evaluations),
        PACKET / "output/classla-error-log.csv": csv_bytes(errors),
        PACKET / "output/downstream-consequences.csv": csv_bytes(consequences),
        PACKET / "output/topic-stability.csv": csv_bytes(topic_stability),
        PACKET / "output/topic-count-sensitivity.csv": csv_bytes(topic_count_sensitivity),
        PACKET / "output/emotion-baseline.csv": csv_bytes(emotion_baseline),
        PACKET / "output/emotion-sensitivity.csv": csv_bytes(emotion_sensitivity),
        PACKET / "output/emotion-method-comparison.csv": csv_bytes(method_comparison),
        PACKET / "validation/expected-values.json": json_bytes(expected),
    }


def package_members(generated: dict[Path, bytes]) -> list[tuple[str, bytes]]:
    members: dict[str, bytes] = {}
    generated_relatives = {path.relative_to(PACKET).as_posix(): payload for path, payload in generated.items()}
    for path in sorted(PACKET.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(PACKET)
        if any(part in {"__pycache__", "raw", "output", "validation"} for part in relative.parts):
            continue
        members[relative.as_posix()] = path.read_bytes()
    members.update(generated_relatives)
    manifest = "".join(f"{sha256_bytes(payload)}  {name}\n" for name, payload in sorted(members.items())).encode("utf-8")
    members["validation/SHA256SUMS.txt"] = manifest
    members["LICENSE.md"] = (ROOT / "LICENSE.md").read_bytes()
    return [(PREFIX + name, payload) for name, payload in sorted(members.items())]


def build(check: bool = False) -> None:
    generated = generated_outputs()
    members = package_members(generated)
    manifest_payload = next(payload for name, payload in members if name == PREFIX + "validation/SHA256SUMS.txt")
    generated[PACKET / "validation/SHA256SUMS.txt"] = manifest_payload
    with tempfile.TemporaryDirectory(prefix="text-nlp-validation-build-") as temporary:
        archive = Path(temporary) / ARCHIVE.name
        deterministic_zip(archive, members)
        archive_payload = archive.read_bytes()
    generated[ARCHIVE] = archive_payload
    generated[DIGEST] = f"{sha256_bytes(archive_payload)}  {ARCHIVE.name}\n".encode("ascii")
    stale = []
    for path, payload in generated.items():
        if check:
            if not path.exists() or path.read_bytes() != payload:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(payload)
    if stale:
        raise SystemExit("Stale text/NLP artifacts: " + ", ".join(stale))
    mode = "verified" if check else "generated"
    print(f"OK: {mode} {len(generated)} artifacts and {len(members)} deterministic archive members.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    build(parser.parse_args().check)
