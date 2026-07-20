---
title: "Learner-corpus lexical analysis"
description: "A Šolar-focused pipeline for safe reannotation, lexical richness, syntactic measures, collocations, and reports."
tags: [projects, learner-corpus, CLASSLA, lexical-diversity, Slovene]
---

# Learner-corpus lexical analysis

<div class="answer-meta" markdown>
<span>learner corpus</span>
<span>lexical analysis</span>
<span>CLASSLA</span>
</div>

## What this project does

This example shows a project-specific learner-corpus analysis pipeline. It reannotates Šolar CoNLL-U data with CLASSLA while preserving IDs, sentence boundaries, token forms, and metadata linkage, then calculates lexical diversity, lexical density, lexical sophistication, syntactic diversity, collocation candidates, statistics, plots, and reports.

[:octicons-mark-github-16: Open the source repository](https://github.com/damjan-popic/korpus-solar-analysis)

## Use this when

- you need to preserve metadata linkage during reannotation.
- you want to connect NLP output to corpus-linguistic measures.
- you need a realistic example of analysis outputs rather than only annotation.
- you want users to see why generated IDs and broken metadata joins are serious problems.

## What to inspect in the code

- `configs/` — reproducible analysis settings.
- `src/solar3_lexical_analysis/` — core analysis code.
- `scripts/` — command-line wrappers.
- `data/metadata/solar-meta.tsv` — metadata join target.
- `analysis/` and `reports/` — generated tables, plots, validation, and summary outputs.
- `pyproject.toml` and `requirements.txt` — dependency model.

## Minimal run path

Treat this as a project-specific pipeline. The minimal pattern to copy is:

```text
raw CoNLL-U + metadata → safe reannotation → validation → analysis tables → report
```

For a small local exercise, create a three-document CoNLL-U sample and verify that original sentence IDs survive every step.

## Relevant handbook workflows

- [How do I annotate a small text with CLASSLA?](../workflows/nlp/annotate-a-small-text-with-classla.md)
- [How do I export CLASSLA results to CSV?](../workflows/nlp/export-classla-results-to-csv.md)
- [How do I write a README for a humanities dataset?](../workflows/publishing/write-a-readme-for-a-humanities-dataset.md)
- [How do I visualise a frequency list with Voyant?](../workflows/visualization/visualise-a-frequency-list-with-voyant.md)

## Practice use

Ask users to design a validation checklist for a reannotation pipeline: what must stay unchanged, what may change, and what would make downstream analysis invalid.

## Limits and cautions

- The pipeline is deliberately specific to the Šolar corpus and its metadata model.
- Lexical-diversity metrics are sensitive to text length and preprocessing.
- Reannotation can improve consistency while still introducing model errors.
- Generated reports should be interpreted with corpus design and metadata imbalance in mind.
