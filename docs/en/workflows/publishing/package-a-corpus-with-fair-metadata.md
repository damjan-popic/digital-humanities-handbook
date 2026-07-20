---
title: "How do I package a corpus with FAIR metadata?"
description: "You want other people to understand, cite, and reuse your corpus."
category: "Publishing & FAIR data"
difficulty: "intermediate"
time: "60–120 min"
tags: [FAIR, metadata, corpus, Zenodo, publishing]
---

# How do I package a corpus with FAIR metadata?

<div class="answer-meta" markdown>
<span>Publishing & FAIR data</span>
<span>intermediate</span>
<span>60–120 min</span>
</div>

## What you are trying to do

You want other people to understand, cite, and reuse your corpus.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Clean corpus files
- Metadata about sources, rights, language, dates, and processing

## Tools

- [JSON Schema](https://json-schema.org)
- [Zenodo](https://zenodo.org)

## Workflow

1. Write a README before packaging.
2. Compute basic corpus statistics.
3. Create metadata with creators, license, language, source, and processing notes.
4. Add checksums for files.
5. Deposit or archive according to rights.

## Output

Corpus ZIP with README, metadata, and checksums.

## Check yourself

- Can someone cite the dataset?
- Are rights and restrictions explicit?
- Can processing be reproduced?

## Common traps

- Publishing text you do not have rights to publish.
- Leaving out negative information, e.g. known OCR errors.
- Treating metadata as admin fluff.

## Worked examples

- [Slovene Wikisource corpus build pipeline](../../case-studies/wikivir.md) shows metadata normalization, validation, and corpus-level documentation for a large text collection.
- [corpus conversion and CLASSLA annotation example](../../case-studies/corpus-augmenter.md) shows how conversion and annotation outputs should preserve metadata for traceability.
- [website crawler and chatbot corpus builder](../../case-studies/fifi.md) shows document and chunk metadata for retrieval-ready website corpora.

## Practice task

Users write a README for a tiny fake corpus and peer-review only the reuse instructions.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
