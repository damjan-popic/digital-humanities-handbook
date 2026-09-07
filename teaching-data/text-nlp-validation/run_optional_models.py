#!/usr/bin/env python3
"""Regenerate CLASSLA and NMF candidates outside ordinary CI."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import re
import sys
import unicodedata
from pathlib import Path


PACKET = Path(__file__).resolve().parent
ROOT = PACKET.parents[1]
PROCESSORS = "tokenize,pos,lemma,depparse,ner"
NMF_COMPONENTS = (2, 3, 4)
NMF_SEEDS = (7, 19, 31)
TOP_WORDS = 8


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(text: str) -> str:
    return unicodedata.normalize("NFC", text).strip()


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def extract_sentence(text: str, selector: str) -> str:
    text = normalized(text)
    if selector.startswith("sentence_prefix:"):
        prefix = selector.split(":", 1)[1]
        start = text.index(prefix)
        return normalized(text[start:].splitlines()[0])
    if selector.startswith("sentence_index:"):
        index = int(selector.split(":", 1)[1]) - 1
        sentences = re.split(r"(?<=[.!?])\s+(?=[A-ZČŠŽ»„])", text)
        return normalized(sentences[index])
    raise ValueError(f"Unsupported selector: {selector}")


def load_samples() -> list[dict[str, str | bool]]:
    registry = json.loads(
        (PACKET / "source/extraction-registry.json").read_text(encoding="utf-8")
    )
    contemporary = {
        row["doc_id"]: row for row in rows(PACKET / "source/contemporary-sample.csv")
    }
    samples = []
    for entry in registry["extractions"]:
        path = ROOT / entry["source_path"]
        if entry["source_path"].endswith("contemporary-sample.csv"):
            source_text = contemporary[entry["source_record_id"]]["text"]
        else:
            source_text = path.read_text(encoding="utf-8")
        samples.append(entry | {"text": extract_sentence(source_text, entry["selector"])})
    return samples


def model_file_inventory(resource_dir: Path) -> list[dict[str, str | int]]:
    return [
        {
            "path": path.relative_to(resource_dir).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in sorted(resource_dir.rglob("*"))
        if path.is_file()
    ]


def run_classla(output: Path, resource_dir: Path, download: bool) -> None:
    import classla
    import obeliks
    import torch

    if download:
        classla.download("sl", dir=str(resource_dir), type="default")
    if not resource_dir.exists():
        raise SystemExit(
            f"CLASSLA resources are absent at {resource_dir}; rerun with --download"
        )

    destination = output / "classla"
    destination.mkdir(parents=True)
    pipeline = classla.Pipeline(
        "sl",
        dir=str(resource_dir),
        type="default",
        processors=PROCESSORS,
        use_gpu=False,
        logging_level="WARN",
    )
    output_hashes = {}
    sample_hashes = {}
    for sample in load_samples():
        sample_id = str(sample["sample_id"])
        text = str(sample["text"])
        sample_hashes[sample_id] = hashlib.sha256(text.encode("utf-8")).hexdigest()
        path = destination / f"{sample_id}.conllu"
        payload = (
            f"# packet_sample_id = {sample_id}\n"
            f"# packet_stratum = {sample['stratum']}\n"
            f"{pipeline(text).to_conll().rstrip()}\n"
        )
        path.write_text(payload, encoding="utf-8", newline="\n")
        output_hashes[path.name] = sha256(path)

    metadata = {
        "run_date": "2026-09-07",
        "language": "sl",
        "pipeline_type": "default (standard Slovene)",
        "processors": PROCESSORS.split(","),
        "use_gpu": False,
        "classla_version": classla.__version__,
        "obeliks_version": getattr(obeliks, "__version__", "not exposed"),
        "torch_version": torch.__version__,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "command": (
            "python teaching-data/text-nlp-validation/run_optional_models.py "
            "--output .cache/text-nlp-validation-models --resources-dir "
            ".cache/classla-resources --download"
        ),
        "resource_files": model_file_inventory(resource_dir),
        "registry_sha256": sha256(PACKET / "source/extraction-registry.json"),
        "sample_text_sha256": sample_hashes,
        "output_sha256": output_hashes,
        "note": (
            "Frozen prediction evidence, not a benchmark or reference. Model files "
            "are not redistributed; hashes identify the local resources used."
        ),
    }
    (destination / "model-run.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def run_topics(output: Path) -> None:
    import numpy
    import sklearn
    from sklearn.decomposition import NMF
    from sklearn.feature_extraction.text import TfidfVectorizer

    destination = output / "topics"
    destination.mkdir(parents=True)
    documents = rows(PACKET / "source/contemporary-sample.csv")
    stopwords = [
        line.strip()
        for line in (PACKET / "source/stopwords-sl.txt").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    vectorizer = TfidfVectorizer(
        lowercase=True,
        min_df=1,
        max_df=1.0,
        stop_words=stopwords,
        token_pattern=r"(?u)\b[^\W\d_][^\W_]+\b",
    )
    matrix = vectorizer.fit_transform(row["text"] for row in documents)
    terms = vectorizer.get_feature_names_out()
    components_rows = []
    document_rows = []
    for count in NMF_COMPONENTS:
        for seed in NMF_SEEDS:
            model = NMF(
                n_components=count,
                init="random",
                random_state=seed,
                max_iter=1000,
                solver="mu",
                beta_loss="kullback-leibler",
            )
            weights = model.fit_transform(matrix)
            for topic_id, component in enumerate(model.components_, start=1):
                ranked = component.argsort()[::-1][:TOP_WORDS]
                top_docs = weights[:, topic_id - 1].argsort()[::-1][:3]
                components_rows.append(
                    {
                        "component_count": count,
                        "seed": seed,
                        "topic_id": topic_id,
                        "top_terms": "|".join(terms[index] for index in ranked),
                        "reconstruction_error": f"{model.reconstruction_err_:.6f}",
                        "iterations": model.n_iter_,
                    }
                )
                for rank, doc_index in enumerate(top_docs, start=1):
                    document_rows.append(
                        {
                            "component_count": count,
                            "seed": seed,
                            "topic_id": topic_id,
                            "rank": rank,
                            "doc_id": documents[doc_index]["doc_id"],
                            "weight": f"{weights[doc_index, topic_id - 1]:.6f}",
                        }
                    )

    def write_csv(name: str, data: list[dict[str, object]]) -> str:
        path = destination / name
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(data[0]), lineterminator="\n")
            writer.writeheader()
            writer.writerows(data)
        return sha256(path)

    output_hashes = {
        "topic-components.csv": write_csv("topic-components.csv", components_rows),
        "topic-documents.csv": write_csv("topic-documents.csv", document_rows),
    }
    metadata = {
        "run_date": "2026-09-07",
        "scikit_learn_version": sklearn.__version__,
        "numpy_version": numpy.__version__,
        "python_version": platform.python_version(),
        "documents": len(documents),
        "synthetic_documents": len(documents),
        "vectorizer": {
            "lowercase": True,
            "min_df": 1,
            "max_df": 1.0,
            "stopwords_sha256": sha256(PACKET / "source/stopwords-sl.txt"),
            "token_pattern": r"(?u)\b[^\W\d_][^\W_]+\b",
        },
        "nmf": {
            "component_counts": NMF_COMPONENTS,
            "seeds": NMF_SEEDS,
            "init": "random",
            "max_iter": 1000,
            "solver": "mu",
            "beta_loss": "kullback-leibler",
            "top_words": TOP_WORDS,
        },
        "corpus_sha256": sha256(PACKET / "source/contemporary-sample.csv"),
        "output_sha256": output_hashes,
        "warning": (
            "Twelve synthetic documents are too few for substantive topic inference; "
            "these runs exist only to teach matching and sensitivity."
        ),
    }
    (destination / "model-run.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--resources-dir", type=Path, required=True)
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        raise SystemExit(f"Refusing to overwrite existing model output: {output}")
    output.mkdir(parents=True)
    run_classla(output, args.resources_dir.resolve(), args.download)
    run_topics(output)
    print(f"Wrote CLASSLA and NMF candidates to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
