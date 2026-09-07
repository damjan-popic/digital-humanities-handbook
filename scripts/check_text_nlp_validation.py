#!/usr/bin/env python3
"""Validate issue #24 chapters, workflows, packet, metrics and ecosystem links."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from zipfile import ZipFile

import yaml

from scholarly_work_package_utils import FIXED_ZIP_DATE


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
    "classla_error_rows": 20,
    "downstream_consequence_rows": 3,
    "total_tokens": 330,
    "frequency_svoboda": 9,
    "df_svoboda": 1,
    "frequency_arhiv": 5,
    "df_arhiv": 2,
    "frequency_raziskovalci": 2,
    "df_raziskovalci": 2,
    "frequency_korpus": 2,
    "df_korpus": 1,
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
            "manually reviewed", "precision", "recall", "F1",
        ),
        "text-analysis.md": (
            "token", "type", "analytical unit", "document frequency", "range",
            "dispersion", "Juilland", "concordance", "keyness", "effect size",
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
    for required in ("stratified", "pass", "unresolved", "document frequency", "juilland", "random seed", "unmatched", "false positive", "false negative", "quoted", "negation", "irony", "zero match"):
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


def check_model_metadata() -> None:
    classla = json.loads((PACKET / "interim/classla/model-run.json").read_text(encoding="utf-8"))
    require(classla["classla_version"] == "2.2.1", "CLASSLA version drift")
    require(classla["python_version"] == "3.12.3", "CLASSLA Python version drift")
    require(classla["processors"] == ["tokenize", "pos", "lemma", "depparse", "ner"], "CLASSLA processors drift")
    require(classla["use_gpu"] is False and classla["resource_download_date"] == "2026-09-07", "CLASSLA device/download metadata missing")
    require(classla["resource_files"] and all(item["bytes"] > 0 and re.fullmatch(r"[0-9a-f]{64}", item["sha256"]) for item in classla["resource_files"]), "CLASSLA resource inventory incomplete")
    require(".cache/text-nlp-validation-models-v2" in classla["command"], "exact CLASSLA run command missing")
    for name, digest in classla["output_sha256"].items():
        require(hashlib.sha256((PACKET / "interim/classla" / name).read_bytes()).hexdigest() == digest, f"frozen CLASSLA hash mismatch: {name}")
    topics = json.loads((PACKET / "interim/topics/model-run.json").read_text(encoding="utf-8"))
    require(topics["documents"] == topics["synthetic_documents"] == 12, "topic corpus size drift")
    require(topics["nmf"]["component_counts"] == [2, 3, 4] and topics["nmf"]["seeds"] == [7, 19, 31], "topic run grid drift")
    require(topics["nmf"]["init"] == "random" and topics["vectorizer"]["min_df"] == 1, "topic initialization/vectorizer drift")
    require(hashlib.sha256((PACKET / "source/contemporary-sample.csv").read_bytes()).hexdigest() == topics["corpus_sha256"], "topic corpus hash mismatch")
    for name, digest in topics["output_sha256"].items():
        require(hashlib.sha256((PACKET / "interim/topics" / name).read_bytes()).hexdigest() == digest, f"frozen topic hash mismatch: {name}")


def check_metrics() -> None:
    expected = json.loads((PACKET / "validation/expected-values.json").read_text(encoding="utf-8"))
    require(expected == EXPECTED, f"expected-value regression: {expected}")
    evaluation = rows("output/classla-evaluation.csv")
    errors = rows("output/classla-error-log.csv")
    for row in evaluation:
        numerator, denominator = int(row["numerator"]), int(row["denominator"])
        require(denominator >= 0 and numerator >= 0, f"negative CLASSLA count: {row}")
        if denominator == 0:
            require(numerator == 0 and row["value"] == "", f"undefined CLASSLA rate must remain empty: {row}")
        else:
            require(row["value"] == f"{numerator / denominator:.6f}", f"CLASSLA rate/count mismatch: {row}")
        require(row["eligible_rule"], f"CLASSLA denominator rule missing: {row}")
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
    require(all(row["source_locator"] and row["interpretive_risk"] and row["decision_status"] for row in errors), "CLASSLA error detail incomplete")
    consequences = rows("output/downstream-consequences.csv")
    require([(row["consequence_id"], row["delta_reference_minus_automatic"]) for row in consequences] == [("TNLP-DOWN-01", "2"), ("TNLP-DOWN-02", "1"), ("TNLP-DOWN-03", "0")], "downstream consequence regression")

    frequencies = {row["term"]: row for row in rows("output/frequency-dispersion.csv")}
    concordances = rows("output/concordance.csv")
    concordance_counts = Counter(row["term"] for row in concordances)
    for term, frequency, document_frequency in (("svoboda", 9, 1), ("arhiv", 5, 2), ("raziskovalci", 2, 2), ("korpus", 2, 1)):
        row = frequencies[term]
        require(int(row["frequency"]) == frequency and int(row["document_frequency"]) == document_frequency, f"frequency/DF regression: {term}")
        require(concordance_counts[term] == frequency, f"concordance/frequency disagreement: {term}")
    sensitivity = {(row["setting"], row["term"]): row for row in rows("output/frequency-sensitivity.csv")}
    require(sensitivity[("raw_token_frequency", "svoboda")]["rank"] == "1" and sensitivity[("document_frequency", "svoboda")]["rank"] == "4", "frequency/DF ranking contrast lost")
    require(sensitivity[("document_frequency", "raziskovalci")]["rank"] == "2", "distributed lower-frequency example lost")

    emotion = rows("output/emotion-baseline.csv")
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
    inspected = rows("reference/topic-interpretation.csv")
    require(len(inspected) == 3 and all(row["high_weight_documents"] and row["inspected_passages"] and row["contradictory_passage"] for row in inspected), "manual topic interpretation evidence incomplete")


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
