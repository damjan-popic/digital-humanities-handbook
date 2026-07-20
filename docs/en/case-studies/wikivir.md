---
title: "Slovene Wikisource corpus build pipeline"
description: "A reproducible pattern for turning messy Wikisource material into an annotated research corpus."
tags: [projects, Wikisource, corpus, CLASSLA, topic-modeling]
---

# Slovene Wikisource corpus build pipeline

<div class="answer-meta" markdown>
<span>large corpus</span>
<span>metadata normalization</span>
<span>Slovene</span>
</div>

## What this project does

This example is a build-and-analysis toolkit for a Slovene Wikisource corpus. It normalizes messy document headers, maps metadata tokens, enriches author and genre information, runs linguistic annotation, and prepares the corpus for downstream linguistic and digital-humanities analysis.

[:octicons-mark-github-16: Open the source repository](https://github.com/damjan-popic/wikivir)

## Use this when

- you want a full example of messy source material becoming a reusable corpus.
- you need a case study in metadata normalization.
- you want to compare manual curation, automatic mapping, and validation.
- you want users to see why corpus pipelines need both scripts and human decisions.

## What to inspect in the code

- `header_map.csv` — the master token-to-field mapping.
- `apply_header_map.py` — applies curated metadata mappings to corpus headers.
- `tools/header_curator.py` — interactive one-key metadata curation.
- `tools/validate_header_map.py` — sanity checks.
- `tools/run_classla_xml.py` — stream annotation with CLASSLA.
- `tools/topic_model.py` — topic-modelling entry point.
- `stats/` — generated frequency and coverage outputs.

## Minimal run path

This is not a tiny toy workflow. Treat it as a reference architecture first. For a small teaching version, replicate the pattern on ten documents:

1. collect messy headers;
2. extract header tokens;
3. create a token-to-field map;
4. validate unmapped tokens;
5. rewrite clean metadata;
6. annotate or analyse only after metadata is stable.

## Relevant handbook workflows

- [How do I turn messy humanities notes into a reusable dataset?](../workflows/data-wrangling/turn-messy-humanities-notes-into-a-reusable-dataset.md)
- [How do I package a corpus with FAIR metadata?](../workflows/publishing/package-a-corpus-with-fair-metadata.md)
- [How do I visualise uncertainty in humanities data?](../workflows/visualization/visualise-uncertainty-in-humanities-data.md)
- [How do I automate a linguistic workflow with a Makefile?](../workflows/automation/automate-a-linguistic-workflow-with-a-makefile.md)

## Practice use

Give users twenty messy document headers. Ask them to design a `header_map.csv` with fields such as author, genre, period, source, and uncertainty. Then require a validation step that identifies unmapped or contradictory tokens.

## Limits and cautions

- Large-corpus workflows are hard to reproduce without the same source dump and environment.
- Topic models and embeddings depend on preprocessing choices.
- Metadata normalization can erase ambiguity unless uncertainty is explicitly tracked.
- Public reuse depends on source licensing and attribution requirements.
