#!/usr/bin/env python3
"""Validate issue #24 chapters, workflows, packet, metrics and ecosystem links."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
from zipfile import ZipFile

import yaml

from scholarly_work_package_utils import FIXED_ZIP_DATE
from build_text_nlp_validation import gries_dp, indexed_source_sentences


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "teaching-data" / "text-nlp-validation"
ARCHIVE = ROOT / "docs" / "assets" / "downloads" / "text-nlp-validation-v1.zip"
DIGEST = ARCHIVE.with_suffix(ARCHIVE.suffix + ".sha256")
PREFIX = "text-nlp-validation-v1/"
CHAPTERS = ("linguistic-annotation-classla.md", "text-analysis.md", "topics-emotions-classification.md")
WORKFLOWS = (
    "nlp/evaluate-classla-on-a-domain-specific-sample.md",
    "text-analysis/compare-frequency-document-frequency-and-dispersion.md",
    "text-analysis/test-topic-model-stability-and-interpretability.md",
    "text-analysis/analyse-emotion-with-a-lexicon-and-manual-check.md",
)
EXPECTED = {
    "packet_version": 1,
    "annotation_samples": 4,
    "contemporary_documents": 12,
    "all_contemporary_documents_synthetic": True,
    "classla_evaluation_rows": 48,
    "classla_error_rows": 24,
    "downstream_consequence_rows": 4,
    "total_tokens": 330,
    "part_tokens_archives": 83,
    "part_tokens_museums": 68,
    "part_tokens_language": 66,
    "part_tokens_press": 113,
    "frequency_svoboda": 9,
    "df_svoboda": 1,
    "frequency_arhiv": 5,
    "df_arhiv": 2,
    "frequency_raziskovalci": 2,
    "df_raziskovalci": 2,
    "frequency_korpus": 2,
    "df_korpus": 1,
    "gries_dp_svoboda": 0.657576,
    "gries_dp_arhiv": 0.748485,
    "gries_dp_raziskovalci": 0.548485,
    "gries_dp_korpus": 0.8,
    "topic_stability_rows": 18,
    "unstable_topic_matches": 13,
    "unmatched_count_topics": 1,
    "emotion_examples": 8,
    "emotion_zero_matches": 1,
    "emotion_baseline_tp": 4,
    "emotion_baseline_fp": 3,
    "emotion_baseline_tn": 0,
    "emotion_baseline_fn": 1,
    "emotion_extended_tp": 5,
    "emotion_extended_fp": 3,
    "emotion_extended_tn": 0,
    "emotion_extended_fn": 0,
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def review_state(
    record: dict[str, object],
    *,
    status_field: str,
    draft_status: str,
    context: str,
    reviewer_field: str = "reviewer",
    date_field: str = "reviewed_on",
    scope_field: str = "review_scope",
) -> None:
    """Permit the current draft or a fully documented future human review."""
    status = str(record.get(status_field, ""))
    if status == draft_status:
        return
    require(status == "human-reviewed", f"{context}: unsupported review status {status!r}")
    require(bool(record.get(reviewer_field)), f"{context}: human-reviewed state lacks a named reviewer")
    reviewed_on = str(record.get(date_field, ""))
    try:
        if "T" in reviewed_on:
            datetime.fromisoformat(reviewed_on.replace("Z", "+00:00"))
        else:
            date.fromisoformat(reviewed_on)
        valid_date = True
    except ValueError:
        valid_date = False
    require(
        valid_date,
        f"{context}: human-reviewed state lacks an ISO review date",
    )
    require(bool(record.get(scope_field)), f"{context}: human-reviewed state lacks review scope")


def conllu_comments(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# ") and " = " in line:
            key, value = line[2:].split(" = ", 1)
            result[key] = value
    return result


def rows(relative: str) -> list[dict[str, str]]:
    with (PACKET / relative).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def frontmatter(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.S)
    require(match is not None, f"{path.relative_to(ROOT)}: missing frontmatter")
    return yaml.safe_load(match.group(1)) or {}, text


def translation_metadata(path: Path, metadata: dict[str, object], text: str) -> None:
    status = metadata.get("translation_status")
    if status == "machine-assisted draft; requires human language review":
        require("strojno" in text.lower(), f"{path.relative_to(ROOT)}: visible machine-assisted notice missing")
    elif status == "human-reviewed":
        for field in ("translation_reviewed_by", "translation_reviewed_on", "translation_review_scope"):
            require(metadata.get(field), f"{path.relative_to(ROOT)}: human-reviewed metadata missing {field}")
        require(re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(metadata["translation_reviewed_on"])) is not None, f"{path.relative_to(ROOT)}: review date must be YYYY-MM-DD")
    else:
        raise AssertionError(f"{path.relative_to(ROOT)}: unsupported translation_status {status!r}")


def word_count(text: str, lang: str) -> int:
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^\n)]+\)", r"\1", text)
    return len(re.findall(r"[^\W_]+(?:[’'-][^\W_]+)*", text, re.UNICODE))


def executable_blocks(text: str) -> list[str]:
    return re.findall(r"```(?:bash|python|sql)\n(.*?)```", text, flags=re.S)


def check_pages() -> dict[str, int]:
    counts = {}
    requirements = {
        "linguistic-annotation-classla.md": (
            "sentence segmentation", "multiword token", "XPOS", "UAS", "LAS",
            "code-switching", "historical spelling", "custom lexicon", "source offsets",
            "reference", "precision", "recall", "F1", "50/52", "43/46", "42/46",
        ),
        "text-analysis.md": (
            "token", "type", "analytical unit", "document frequency", "range",
            "dispersion", "Gries", "DP", "concordance", "keyness", "effect size",
            "multiple-comparison", "collocation", "n-grams", "OCR",
        ),
        "topics-emotions-classification.md": (
            "topic modelling", "clustering", "supervised", "bag-of-words",
            "random seed", "initialization", "Jaccard", "calibration", "domain shift",
            "experiencer", "target", "quoted speech", "negation", "modality", "irony",
        ),
    }
    for chapter in CHAPTERS:
        pair = []
        for lang in ("en", "sl"):
            path = ROOT / "docs" / lang / "chapters" / chapter
            metadata, text = frontmatter(path)
            pair.append(text)
            require(metadata.get("status") == "draft", f"{path.relative_to(ROOT)}: status must remain draft")
            if lang == "sl":
                translation_metadata(path, metadata, text)
            count = word_count(text, lang)
            require(count >= 2100, f"{path.relative_to(ROOT)}: {count} words below completeness minimum 2100")
            counts[f"{lang}/{chapter}"] = count
            require("text-nlp-validation-v1.zip" in text, f"{path.relative_to(ROOT)}: missing packet link")
        lower = pair[0].lower()
        for phrase in requirements[chapter]:
            require(phrase.lower() in lower, f"docs/en/chapters/{chapter}: missing {phrase!r}")
        require(executable_blocks(pair[0]) == executable_blocks(pair[1]), f"{chapter}: bilingual executable blocks differ")
        en_dois = set(re.findall(r"https://doi.org/[^)\s]+", pair[0]))
        sl_dois = set(re.findall(r"https://doi.org/[^)\s]+", pair[1]))
        require(en_dois == sl_dois, f"{chapter}: DOI sets differ by language")
    all_workflow_text = []
    for workflow in WORKFLOWS:
        pair = []
        for lang in ("en", "sl"):
            path = ROOT / "docs" / lang / "workflows" / workflow
            metadata, text = frontmatter(path)
            pair.append(text)
            require(metadata.get("status") == "draft", f"{path.relative_to(ROOT)}: status must remain draft")
            require("text-nlp-validation-v1.zip" in text, f"{path.relative_to(ROOT)}: missing packet link")
            require('<div class="answer-meta" markdown>' in text and text.count("<span>") >= 3, f"{path.relative_to(ROOT)}: answer summary missing")
            if lang == "sl":
                translation_metadata(path, metadata, text)
        require(executable_blocks(pair[0]) == executable_blocks(pair[1]), f"{workflow}: bilingual executable blocks differ")
        all_workflow_text.extend(pair)
    joined = "\n".join(all_workflow_text).lower()
    for required in ("stratified", "pass", "unresolved", "document frequency", "gries", "random seed", "unmatched", "false positive", "false negative", "quoted", "negation", "irony", "zero match"):
        require(required in joined, f"new workflows: missing required difficult concept {required!r}")
    require("gold" not in "\n".join((ROOT / "docs" / lang / "chapters" / chapter).read_text(encoding="utf-8").lower() for lang in ("en", "sl") for chapter in CHAPTERS), "core chapters use prohibited gold terminology")
    return counts


def check_packet_structure() -> None:
    for directory in ("source", "reference", "raw", "interim", "output", "validation", "known-problems"):
        require((PACKET / directory).is_dir(), f"packet layer missing: {directory}")
    for english, slovene in (
        ("README.md", "README.sl.md"),
        ("rights-and-provenance.md", "rights-and-provenance.sl.md"),
        ("data-dictionary.md", "data-dictionary.sl.md"),
        ("RIGHTS.md", "RIGHTS.sl.md"),
        ("known-problems/README.md", "known-problems/README.sl.md"),
        ("reference/classla-reference-policy.md", "reference/classla-reference-policy.sl.md"),
        ("reference/emotion-codebook.md", "reference/emotion-codebook.sl.md"),
        ("reference/topic-interpretation.csv", "reference/topic-interpretation.sl.csv"),
    ):
        require((PACKET / english).is_file() and (PACKET / slovene).is_file(), f"missing paired packet documentation: {english}")
    source_text = (PACKET / "source/contemporary-sample.csv").read_text(encoding="utf-8")
    require("synthetic" in source_text and "CC BY 4.0" in source_text, "synthetic source or rights declaration missing")
    rights = (PACKET / "rights-and-provenance.md").read_text(encoding="utf-8")
    for token in ("URN:NBN:SI:doc-YPI8OFSU", "provider-ocr.txt", "reference-transcription.txt", "NRC", "redistribution"):
        require(token in rights, f"rights/provenance record missing {token}")
    sample_rows = rows("raw/annotation-samples.csv")
    ids = [row["sample_id"] for row in sample_rows]
    require(len(ids) == 4 and len(set(ids)) == 4 and all(ids), "annotation sample IDs are not stable and unique")
    require(all(row["source_path"] and row["source_record_id"] and row["selector"] and row["source_sha256"] for row in sample_rows), "source locators or hashes missing")
    require({row["stratum"] for row in sample_rows} == {"contemporary_clean", "historical_reference", "provider_ocr"}, "annotation strata changed")

    policy_meta, policy_text = frontmatter(PACKET / "reference/classla-reference-policy.md")
    review_state(
        policy_meta,
        status_field="reference_status",
        draft_status="machine-assisted reference draft; pending human review",
        context="CLASSLA reference policy",
        reviewer_field="human_reviewer",
        date_field="human_reviewed_on",
        scope_field="human_review_scope",
    )
    status_documents = (
        "docs/en/chapters/linguistic-annotation-classla.md",
        "docs/sl/chapters/linguistic-annotation-classla.md",
        "docs/en/chapters/topics-emotions-classification.md",
        "docs/sl/chapters/topics-emotions-classification.md",
        "docs/en/workflows/nlp/evaluate-classla-on-a-domain-specific-sample.md",
        "docs/sl/workflows/nlp/evaluate-classla-on-a-domain-specific-sample.md",
        "docs/en/workflows/text-analysis/analyse-emotion-with-a-lexicon-and-manual-check.md",
        "docs/sl/workflows/text-analysis/analyse-emotion-with-a-lexicon-and-manual-check.md",
        "docs/en/workflows/text-analysis/test-topic-model-stability-and-interpretability.md",
        "docs/sl/workflows/text-analysis/test-topic-model-stability-and-interpretability.md",
        "teaching-data/text-nlp-validation/README.md",
        "teaching-data/text-nlp-validation/README.sl.md",
        "teaching-data/text-nlp-validation/data-dictionary.md",
        "teaching-data/text-nlp-validation/data-dictionary.sl.md",
    )
    status_texts = {relative: (ROOT / relative).read_text(encoding="utf-8").lower() for relative in status_documents}
    if policy_meta["reference_status"] == "machine-assisted reference draft; pending human review":
        for relative, text in status_texts.items():
            marker = "human review" if "/en/" in relative or relative.endswith(("README.md", "data-dictionary.md")) else "človešk"
            require(marker in text, f"{relative}: pending human-review status not disclosed")
        prohibited = ("manually reviewed teaching reference", "one maintainer reviewed", "ročno pregledana referenca", "negotovost; en pregledovalec")
        require(all(term not in "\n".join(status_texts.values()) for term in prohibited), "unsupported completed-review claim returned")
    else:
        require(all("human-reviewed" in text for text in status_texts.values()), "human-reviewed policy is not reflected across teaching materials")
    for token in ("named reviewer", "ISO", "review scope", "TNLP-CLEAN-01", "TNLP-CLEAN-02", "TNLP-AF-REF", "TNLP-AF-OCR", "Unresolved"):
        require(token.lower() in policy_text.lower(), f"reference policy lacks future-review or inspection detail: {token}")

    emotion_codebook_statuses = []
    for relative in ("reference/emotion-codebook.md", "reference/emotion-codebook.sl.md"):
        metadata, _ = frontmatter(PACKET / relative)
        emotion_codebook_statuses.append(metadata["reference_status"])
        review_state(
            metadata,
            status_field="reference_status",
            draft_status="machine-assisted reference draft; pending human review",
            context=relative,
            reviewer_field="human_reviewer",
            date_field="human_reviewed_on",
            scope_field="human_review_scope",
        )
    require(len(set(emotion_codebook_statuses)) == 1, "bilingual emotion-codebook review status differs")

    for sample_id in ids:
        path = PACKET / "reference/classla" / f"{sample_id}.conllu"
        comments = conllu_comments(path)
        review_state(
            comments,
            status_field="reference_status",
            draft_status="machine-assisted reference draft; pending human review",
            context=f"reference/{path.name}",
            reviewer_field="human_reviewer",
            date_field="human_reviewed_on",
            scope_field="human_review_scope",
        )
        require(comments["reference_status"] == policy_meta["reference_status"], f"{path.name}: status differs from reference policy")
        require(comments.get("reference_policy", "").startswith("TNLP-REF-2;"), f"{path.name}: reference version drift")

    def conllu_word(path: Path, token_id: int) -> list[str]:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith(f"{token_id}\t"):
                fields = line.split("\t")
                require(len(fields) == 10, f"{path.name}: malformed CoNLL-U token {token_id}")
                return fields
        raise AssertionError(f"{path.name}: token {token_id} missing")

    ref_stranko = conllu_word(PACKET / "reference/classla/TNLP-AF-REF.conllu", 43)
    ocr_stranko = conllu_word(PACKET / "reference/classla/TNLP-AF-OCR.conllu", 42)
    require((ref_stranko[1], ref_stranko[6], ref_stranko[7]) == ("stranko", "34", "obl"), "TNLP-AF-REF stranko correction drift")
    require((ocr_stranko[1], ocr_stranko[6], ocr_stranko[7]) == ("stranko", "33", "obl"), "TNLP-AF-OCR stranko correction drift")

    require((PACKET / "reference/classla-causal-decisions.csv").is_file(), "causal-decision table missing")
    for row in rows("reference/classla-causal-decisions.csv"):
        review_state(
            row,
            status_field="review_status",
            draft_status="machine-assisted causal draft; pending human review",
            context=f"causal decision {row['causal_rule_id']}",
        )
    for relative, draft_status in (
        ("reference/emotion-annotations.csv", "machine-assisted reference draft; pending human review"),
        ("reference/topic-interpretation.csv", "machine-assisted interpretation draft; pending human review"),
        ("reference/topic-interpretation.sl.csv", "machine-assisted interpretation draft; pending human review"),
    ):
        for row in rows(relative):
            review_state(row, status_field="review_status", draft_status=draft_status, context=f"{relative} row")
            if relative == "reference/emotion-annotations.csv":
                require(row["review_status"] == emotion_codebook_statuses[0], "emotion annotation/codebook review status differs")


def check_model_metadata() -> None:
    classla = json.loads((PACKET / "interim/classla/model-run.json").read_text(encoding="utf-8"))
    require(classla["classla_version"] == "2.2.1", "CLASSLA version drift")
    require(classla["python_version"] == "3.12.3", "CLASSLA Python version drift")
    require(classla["processors"] == ["tokenize", "pos", "lemma", "depparse", "ner"], "CLASSLA processors drift")
    require(classla["use_gpu"] is False, "CLASSLA device metadata missing")
    require("resource_download_date" not in classla, "unverifiable CLASSLA resource download date returned")
    require(re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", classla["run_timestamp_utc"]) is not None, "CLASSLA UTC run timestamp missing")
    require(classla["obeliks_version"] == "1.1.6", "Obeliks version drift")
    require(classla["resource_files"] and all(item["bytes"] > 0 and re.fullmatch(r"[0-9a-f]{64}", item["sha256"]) for item in classla["resource_files"]), "CLASSLA resource inventory incomplete")
    require(".cache/text-nlp-validation-models-v2" in classla["command"], "exact CLASSLA run command missing")

    environment_path = PACKET / "interim/model-environment.json"
    lock_path = PACKET / "interim/model-environment.lock.txt"
    environment = json.loads(environment_path.read_text(encoding="utf-8"))
    require(classla["environment_snapshot"]["path"] == "../model-environment.json", "CLASSLA environment locator drift")
    require(classla["environment_snapshot"]["sha256"] == hashlib.sha256(environment_path.read_bytes()).hexdigest(), "CLASSLA environment snapshot hash mismatch")
    require(environment["lock_sha256"] == hashlib.sha256(lock_path.read_bytes()).hexdigest(), "environment lock hash mismatch")
    require(re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", environment["captured_at_utc"]) is not None, "environment capture timestamp missing")
    required_packages = {"classla", "torch_distribution", "torch_runtime", "numpy", "scipy", "scikit-learn", "stanza", "obeliks"}
    require(required_packages <= set(environment["packages"]) and all(environment["packages"][name] for name in required_packages), "model environment package inventory incomplete")

    acquisition_path = PACKET / "interim/classla/resource-acquisition.json"
    acquisition = json.loads(acquisition_path.read_text(encoding="utf-8"))
    require(classla["resource_acquisition_manifest"]["path"] == "resource-acquisition.json", "CLASSLA acquisition manifest locator drift")
    require(classla["resource_acquisition_manifest"]["sha256"] == hashlib.sha256(acquisition_path.read_bytes()).hexdigest(), "CLASSLA acquisition manifest hash mismatch")
    require(acquisition["acquisition_timestamp_utc"] == "unknown" and acquisition["acquisition_status"] == "unknown", "unverifiable CLASSLA acquisition time must remain explicit")
    require(acquisition["resource_files"] == classla["resource_files"], "CLASSLA resource inventory differs from acquisition manifest")
    for name, digest in classla["output_sha256"].items():
        require(hashlib.sha256((PACKET / "interim/classla" / name).read_bytes()).hexdigest() == digest, f"frozen CLASSLA hash mismatch: {name}")

    topics = json.loads((PACKET / "interim/topics/model-run.json").read_text(encoding="utf-8"))
    require(topics["documents"] == topics["synthetic_documents"] == 12, "topic corpus size drift")
    require(topics["nmf"]["component_counts"] == [2, 3, 4] and topics["nmf"]["seeds"] == [7, 19, 31], "topic run grid drift")
    require(topics["scipy_version"] == environment["packages"]["scipy"], "topic SciPy version/environment mismatch")
    require(topics["environment_snapshot"] == classla["environment_snapshot"], "topic and CLASSLA environment snapshots differ")
    vectorizer = topics["vectorizer"]["effective_parameters"]
    vectorizer_fields = {"analyzer", "binary", "decode_error", "dtype", "encoding", "input", "lowercase", "max_df", "max_features", "min_df", "ngram_range", "norm", "preprocessor", "smooth_idf", "stop_words", "strip_accents", "sublinear_tf", "token_pattern", "tokenizer", "use_idf", "vocabulary"}
    require(set(vectorizer) == vectorizer_fields and vectorizer["min_df"] == 1 and vectorizer["ngram_range"] == [1, 1], "full TF-IDF parameter record drift")
    nmf_runs = topics["nmf"]["effective_parameters_by_run"]
    nmf_fields = {"alpha_H", "alpha_W", "beta_loss", "init", "l1_ratio", "max_iter", "n_components", "random_state", "shuffle", "solver", "tol", "verbose"}
    require(len(nmf_runs) == 9 and all(set(run) == nmf_fields for run in nmf_runs), "full NMF effective parameter grid missing")
    require({(run["n_components"], run["random_state"]) for run in nmf_runs} == {(count, seed) for count in (2, 3, 4) for seed in (7, 19, 31)}, "NMF parameter grid drift")
    require(all(run["init"] == "random" and run["solver"] == "mu" and run["beta_loss"] == "kullback-leibler" for run in nmf_runs), "NMF initialization/solver drift")
    require(hashlib.sha256((PACKET / "source/contemporary-sample.csv").read_bytes()).hexdigest() == topics["corpus_sha256"], "topic corpus hash mismatch")
    for name, digest in topics["output_sha256"].items():
        require(hashlib.sha256((PACKET / "interim/topics" / name).read_bytes()).hexdigest() == digest, f"frozen topic hash mismatch: {name}")


def check_metrics() -> None:
    expected = json.loads((PACKET / "validation/expected-values.json").read_text(encoding="utf-8"))
    reference_review = expected.pop("reference_review")
    review_state(
        reference_review,
        status_field="status",
        draft_status="machine-assisted reference draft; pending human review",
        context="validation/expected-values.json reference review",
    )
    require(expected == EXPECTED, f"expected-value regression: {expected}")
    evaluation = rows("output/classla-evaluation.csv")
    errors = rows("output/classla-error-log.csv")
    accounting_fields = (
        "reference_item_count", "predicted_item_count", "aligned_reference_items",
        "aligned_predicted_items", "substitutions", "insertions", "deletions",
        "excluded_reference_items", "excluded_predicted_items",
    )
    for row in evaluation:
        numerator, denominator = int(row["numerator"]), int(row["denominator"])
        require(denominator >= 0 and numerator >= 0, f"negative CLASSLA count: {row}")
        if denominator == 0:
            require(numerator == 0 and row["value"] == "", f"undefined CLASSLA rate must remain empty: {row}")
        else:
            require(row["value"] == f"{numerator / denominator:.6f}", f"CLASSLA rate/count mismatch: {row}")
        require(row["eligible_rule"] and row["alignment_unit"] and row["exclusion_rule"], f"CLASSLA accounting rule missing: {row}")
        counts = {field: int(row[field]) for field in accounting_fields}
        require(all(value >= 0 for value in counts.values()), f"negative alignment count: {row}")
        require(
            counts["reference_item_count"] == counts["aligned_reference_items"] + counts["excluded_reference_items"],
            f"reference-side alignment accounting does not reconcile: {row}",
        )
        require(
            counts["predicted_item_count"] == counts["aligned_predicted_items"] + counts["excluded_predicted_items"],
            f"prediction-side alignment accounting does not reconcile: {row}",
        )
        if row["layer"] == "sentence_boundary" and row["metric"] == "precision":
            require(denominator == counts["predicted_item_count"], f"sentence precision denominator drift: {row}")
        elif row["layer"] == "sentence_boundary" and row["metric"] == "recall":
            require(denominator == counts["reference_item_count"], f"sentence recall denominator drift: {row}")
        elif row["layer"] == "sentence_boundary" and row["metric"] == "f1":
            require(denominator == counts["reference_item_count"] + counts["predicted_item_count"], f"sentence F1 denominator drift: {row}")
        elif row["layer"] == "tokenization":
            require(denominator == counts["reference_item_count"], f"token denominator is not the complete reference side: {row}")
        elif row["layer"] in {"lemma", "upos", "morphology", "dependency"}:
            require(denominator == counts["aligned_reference_items"], f"downstream label denominator does not match admitted aligned items: {row}")
        elif row["layer"] == "ner" and row["metric"] == "strict_span_precision":
            require(denominator == counts["predicted_item_count"], f"NER precision denominator drift: {row}")
        elif row["layer"] == "ner" and row["metric"] == "strict_span_recall":
            require(denominator == counts["reference_item_count"], f"NER recall denominator drift: {row}")
        elif row["layer"] == "ner" and row["metric"] == "strict_span_f1":
            require(denominator == counts["reference_item_count"] + counts["predicted_item_count"], f"NER F1 denominator drift: {row}")
    error_counts = Counter((row["sample_id"], row["layer"]) for row in errors)
    metric_to_error = {
        ("tokenization", "reference_token_agreement"): "tokenization",
        ("lemma", "accuracy"): "lemma",
        ("upos", "accuracy"): "upos",
        ("morphology", "exact_feature_set_accuracy"): "morphology",
        ("dependency", "UAS"): "dependency_uas",
        ("dependency", "LAS"): "dependency_las",
    }
    for row in evaluation:
        key = (row["layer"], row["metric"])
        if key in metric_to_error:
            require(int(row["denominator"]) - int(row["numerator"]) == error_counts[(row["sample_id"], metric_to_error[key])], f"aggregate/error-log disagreement: {row}")
    require({row["error_family"] for row in errors} <= {"segmentation", "lexical", "morphosyntactic", "dependency", "entity", "ambiguity"}, "unknown CLASSLA error family")
    causal_fields = ("input_stratum", "immediate_disagreement", "likely_causal_origin", "also_occurs_in_reference_transcription", "review_status")
    require(all(row["source_locator"] and row["interpretive_risk"] and all(row[field] for field in causal_fields) for row in errors), "CLASSLA error or causal detail incomplete")
    cross_layer = [row for row in errors if row["likely_causal_origin"] == "cross_layer_model_reference_disagreement"]
    require(len(cross_layer) == 14 and all(row["also_occurs_in_reference_transcription"] == "true" and row["causal_rule_id"] for row in cross_layer), "cross-layer causal classification regression")
    require(sum(row["likely_causal_origin"] == "provider_ocr_conditioned" for row in errors) == 10, "provider-OCR-conditioned error count regression")
    for form, layers in (("vse", {"lemma", "upos", "morphology", "dependency_uas", "dependency_las"}), ("stranko", {"dependency_uas", "dependency_las"})):
        matching = [row for row in cross_layer if row["form"] == form]
        require({row["input_stratum"] for row in matching} == {"historical_reference", "provider_ocr"}, f"{form}: cross-layer strata missing")
        require(Counter(row["layer"] for row in matching) == Counter({layer: 2 for layer in layers}), f"{form}: cross-layer field regression")
    consequences = rows("output/downstream-consequences.csv")
    require([(row["consequence_id"], row["delta_reference_minus_automatic"]) for row in consequences] == [("TNLP-DOWN-01", "2"), ("TNLP-DOWN-02", "1"), ("TNLP-DOWN-03", "0"), ("TNLP-DOWN-04", "2")], "downstream consequence regression")

    frequencies = {row["term"]: row for row in rows("output/frequency-dispersion.csv")}
    concordances = rows("output/concordance.csv")
    concordance_counts = Counter(row["term"] for row in concordances)
    selected_dp = {
        "svoboda": 0.657576,
        "arhiv": 0.748485,
        "raziskovalci": 0.548485,
        "korpus": 0.800000,
    }
    for term, frequency, document_frequency in (("svoboda", 9, 1), ("arhiv", 5, 2), ("raziskovalci", 2, 2), ("korpus", 2, 1)):
        row = frequencies[term]
        require(int(row["frequency"]) == frequency and int(row["document_frequency"]) == document_frequency, f"frequency/DF regression: {term}")
        require(concordance_counts[term] == frequency, f"concordance/frequency disagreement: {term}")
        part_sizes = [int(row[f"{theme}_eligible_tokens"]) for theme in ("archives", "museums", "language", "press")]
        part_counts = [int(row[f"{theme}_term_count"]) for theme in ("archives", "museums", "language", "press")]
        require(part_sizes == [83, 68, 66, 113] and sum(part_sizes) == 330, f"dispersion part sizes drift: {term}")
        require(sum(part_counts) == frequency, f"dispersion term counts do not reconcile: {term}")
        calculated = gries_dp(part_counts, part_sizes)
        require(calculated is not None and row["gries_dp"] == f"{calculated:.6f}" == f"{selected_dp[term]:.6f}", f"Gries DP regression: {term}")
        require("0 = proportional" in row["dispersion_direction"] and "unequal" in row["dispersion_partition"], f"Gries DP interpretation metadata missing: {term}")
    require(gries_dp([0, 0, 0, 0], [83, 68, 66, 113]) is None, "Gries DP must remain undefined for F=0")
    require("Juilland" not in (PACKET / "output/frequency-dispersion.csv").read_text(encoding="utf-8"), "obsolete Juilland dispersion returned")
    sensitivity = {(row["setting"], row["term"]): row for row in rows("output/frequency-sensitivity.csv")}
    require(sensitivity[("raw_token_frequency", "svoboda")]["rank"] == "1" and sensitivity[("document_frequency", "svoboda")]["rank"] == "4", "frequency/DF ranking contrast lost")
    require(sensitivity[("document_frequency", "raziskovalci")]["rank"] == "2", "distributed lower-frequency example lost")

    emotion = rows("output/emotion-baseline.csv")
    annotation_path = PACKET / "reference/emotion-annotations.csv"
    with annotation_path.open(encoding="utf-8", newline="") as handle:
        annotation_reader = csv.DictReader(handle)
        require("text" not in (annotation_reader.fieldnames or []), "emotion reference duplicates mutable source text")
        annotations = {row["annotation_id"]: row for row in annotation_reader}
    source_sentences = indexed_source_sentences(rows("source/contemporary-sample.csv"))
    for row in emotion:
        sentence_id = f"{row['doc_id']}.s{row['sentence_index']}"
        require(row["sentence_id"] == sentence_id and row["source_text"] == source_sentences[sentence_id], f"emotion source locator/text drift: {row['annotation_id']}")
        require(row["source_locator"] == f"source/contemporary-sample.csv#{sentence_id}", f"emotion stable source locator drift: {row['annotation_id']}")
        require(row["reference_review_status"] == annotations[row["annotation_id"]]["review_status"], f"emotion review status drift: {row['annotation_id']}")
    emotion_by_id = {row["annotation_id"]: row for row in emotion}
    require(emotion_by_id["TNLP-E06"]["source_text"] == source_sentences["TNLP-C10.s1"] and emotion_by_id["TNLP-E07"]["source_text"] == source_sentences["TNLP-C12.s1"], "E06/E07 source punctuation drift")
    require(any(not row["lexicon_matches"] and row["binary_outcome"] == "FN" for row in emotion), "zero-match false negative missing")
    require(any(row["binary_outcome"] == "FP" for row in emotion), "emotion false positive missing")
    require(any(row["quotation"] == "true" and row["voice"] == "quoted_speech" and row["experiencer"] != "unresolved" for row in emotion), "quoted attributed emotion missing")
    require(any(row["negation"] == "true" for row in emotion) and any(row["irony"] == "true" and row["uncertain"] == "true" for row in emotion), "negation or unresolved irony missing")
    sensitivity_rows = rows("output/emotion-sensitivity.csv")
    require(sensitivity_rows[0]["FN"] == "1" and sensitivity_rows[1]["FN"] == "0" and sensitivity_rows[1]["development_note"], "emotion sensitivity result drift")

    stability = rows("output/topic-stability.csv")
    require(len(stability) == 18 and {row["comparison_seed"] for row in stability} == {"19", "31"}, "topic stability grid incomplete")
    require(sum(row["status"] == "unstable" for row in stability) == 13, "unstable topic rows were lost")
    count_rows = rows("output/topic-count-sensitivity.csv")
    require({row["comparison_count"] for row in count_rows} == {"2", "4"} and any(row["relation_status"] == "unmatched_comparison_topic" for row in count_rows), "topic-count sensitivity/unmatched rows missing")
    top_documents: dict[tuple[int, int, int], list[str]] = defaultdict(list)
    for row in sorted(rows("interim/topics/topic-documents.csv"), key=lambda item: (int(item["component_count"]), int(item["seed"]), int(item["topic_id"]), int(item["rank"]))):
        top_documents[(int(row["component_count"]), int(row["seed"]), int(row["topic_id"]))].append(row["doc_id"])
    interpretation_pairs = []
    for relative in ("reference/topic-interpretation.csv", "reference/topic-interpretation.sl.csv"):
        inspected = rows(relative)
        interpretation_pairs.append(inspected)
        require(len(inspected) == 3, f"{relative}: interpretation row count drift")
        for row in inspected:
            key = (int(row["component_count"]), int(row["seed"]), int(row["topic_id"]))
            declared_documents = row["high_weight_documents"].split("|")
            inspected_ids = row["inspected_sentence_ids"].split("|")
            require(declared_documents == top_documents[key], f"{relative}: high-weight document IDs drift for {key}")
            require(all(sentence_id in source_sentences for sentence_id in inspected_ids), f"{relative}: inspected sentence ID does not resolve for {key}")
            require({sentence_id.split(".s", 1)[0] for sentence_id in inspected_ids} == set(declared_documents), f"{relative}: high-weight documents lack source sentences for {key}")
            require(row["contradictory_sentence_id"] in source_sentences and row["contradictory_sentence_id"].startswith(f"{row['contradictory_document']}.s"), f"{relative}: contradictory source locator drift for {key}")
            require(row["interpretive_judgement"], f"{relative}: interpretive judgement missing for {key}")
            review_state(row, status_field="review_status", draft_status="machine-assisted interpretation draft; pending human review", context=f"{relative}: {key}")
    structural_fields = ("component_count", "seed", "topic_id", "high_weight_documents", "inspected_sentence_ids", "contradictory_document", "contradictory_sentence_id", "review_status", "reviewer", "reviewed_on", "review_scope")
    require(
        [tuple(row[field] for field in structural_fields) for row in interpretation_pairs[0]]
        == [tuple(row[field] for field in structural_fields) for row in interpretation_pairs[1]],
        "bilingual topic interpretation structure/status drift",
    )


def check_archive() -> None:
    require(ARCHIVE.is_file() and DIGEST.is_file(), "student ZIP or digest missing")
    digest = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
    require(DIGEST.read_text(encoding="ascii") == f"{digest}  {ARCHIVE.name}\n", "student ZIP digest stale")
    manifest_path = PACKET / "validation/SHA256SUMS.txt"
    manifest = {}
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        value, relative = line.split("  ", 1)
        manifest[relative] = value
        require((PACKET / relative).is_file(), f"manifest target missing: {relative}")
        require(hashlib.sha256((PACKET / relative).read_bytes()).hexdigest() == value, f"manifest digest mismatch: {relative}")
    with ZipFile(ARCHIVE) as archive:
        infos = archive.infolist()
        require(archive.testzip() is None, "student ZIP CRC failure")
        require(all(info.date_time == FIXED_ZIP_DATE for info in infos), "student ZIP timestamps are not deterministic")
        names = {info.filename for info in infos}
        expected_names = {PREFIX + name for name in manifest} | {PREFIX + "validation/SHA256SUMS.txt", PREFIX + "LICENSE.md"}
        require(names == expected_names, "student ZIP member set differs from manifest")
        for relative, value in manifest.items():
            require(hashlib.sha256(archive.read(PREFIX + relative)).hexdigest() == value, f"student ZIP content mismatch: {relative}")


def check_ecosystem_and_generated() -> None:
    mapping = yaml.safe_load((ROOT / "intertextuality.yml").read_text(encoding="utf-8"))
    relative_workflows = tuple(f"workflows/{path}" for path in WORKFLOWS[:3])
    for workflow in relative_workflows:
        require(workflow in mapping["workflows"], f"explicit ecosystem mapping missing: {workflow}")
    chapter_expectations = {
        "chapters/linguistic-annotation-classla.md": relative_workflows[0],
        "chapters/text-analysis.md": relative_workflows[1],
        "chapters/topics-emotions-classification.md": relative_workflows[2],
    }
    for chapter, workflow in chapter_expectations.items():
        require(workflow in mapping["chapters"][chapter]["workflows"], f"chapter ecosystem trail missing {workflow}")
    for locale, marker in (("en", "Linguistic annotation and CLASSLA"), ("sl", "Jezikoslovna anotacija in CLASSLA")):
        manuscript = (ROOT / "release" / f"review-manuscript-{locale}.md").read_text(encoding="utf-8")
        require(marker in manuscript and "text-nlp-validation-v1.zip" in manuscript, f"{locale} review manuscript stale")
        catalogue = (ROOT / "docs" / locale / "workflows/index.md").read_text(encoding="utf-8")
        for workflow in WORKFLOWS:
            title = frontmatter(ROOT / "docs" / locale / "workflows" / workflow)[0]["title"]
            require(str(title) in catalogue, f"{locale} workflow catalogue missing {title}")
    coverage = (ROOT / "release/translation-coverage.md").read_text(encoding="utf-8")
    for workflow in WORKFLOWS:
        require(workflow not in coverage, f"paired workflow incorrectly listed as translation fallback: {workflow}")


def main() -> int:
    try:
        counts = check_pages()
        check_packet_structure()
        check_model_metadata()
        check_metrics()
        check_archive()
        check_ecosystem_and_generated()
    except (AssertionError, KeyError, OSError, ValueError, yaml.YAMLError) as error:
        print(f"Text/NLP validation check failed:\n\n- {error}")
        return 1
    print("Text/NLP chapter word counts (metadata and fenced code excluded):")
    for name, count in counts.items():
        print(f"  {name}: {count}")
    print("OK: text/NLP sources, frozen models, metrics, teaching download, translations and ecosystem links are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
