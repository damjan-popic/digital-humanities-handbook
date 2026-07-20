---
title: "Dialogue corpus tabulation and lexical-diversity analysis"
description: "A pipeline for turning dialogue-corpus exports into token, turn, speaker, and aggregate tables."
tags: [projects, dialogue, lexical-diversity, pandas, Spanish]
---

# Dialogue corpus tabulation and lexical-diversity analysis

<div class="answer-meta" markdown>
<span>dialogue corpus</span>
<span>lexical diversity</span>
<span>tables</span>
</div>

## What this project does

This example turns an SLC-style dialogue-corpus export into tidy data frames and precomputed aggregate tables. It recognizes speaker turns, normalizes transcription artefacts, attaches speaker metadata, computes lexical-diversity and sentence-level diagnostics, and exports CSV outputs.

[:octicons-mark-github-16: Open the source repository](https://github.com/damjan-popic/pracomul)

## Use this when

- you have conversational corpus data and need analysis-ready tables.
- you want to teach corpus grain: document, speaker, turn, token, aggregate.
- you need an example of lexical-diversity metrics in practice.
- you want users to see why a data dictionary matters.

## What to inspect in the code

- `analyze_slc.py` — the main pipeline script.
- `data/` — input corpus material.
- `results/` — output tables.
- `slc_column_dictionary.xlsx` — column dictionary.
- notebooks — exploratory analysis and checks.

## Minimal run path

```bash
python analyze_slc.py data/corpus.txt results
```

Expected outputs include token tables, turn tables, speaker-centered tables, aggregate summaries, and lexical-diversity measures.

## Relevant handbook workflows

- [How do I turn messy humanities notes into a reusable dataset?](../workflows/data-wrangling/turn-messy-humanities-notes-into-a-reusable-dataset.md)
- [How do I visualise a frequency list with Voyant?](../workflows/visualization/visualise-a-frequency-list-with-voyant.md)
- [How do I make an interactive term-frequency dashboard?](../workflows/visualization/make-an-interactive-term-frequency-dashboard.md)
- [How do I write a README for a humanities dataset?](../workflows/publishing/write-a-readme-for-a-humanities-dataset.md)

## Practice use

Ask users to draw the data model: corpus → document → speaker → turn → token → aggregate. Then have them decide which research questions require each level.

## Limits and cautions

- Dialogue transcription conventions shape the output.
- Sentence boundaries in conversational data are approximate.
- Lexical-diversity metrics are sensitive to text length and preprocessing.
- Original transcripts may have non-commercial or restricted-use licensing.
