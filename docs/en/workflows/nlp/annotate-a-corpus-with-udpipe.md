---
title: "How do I annotate a corpus with UDPipe?"
description: "You need tokens, lemmas, POS tags, or dependency parses for a corpus."
category: "NLP"
difficulty: "intermediate"
time: "30–60 min"
tags: [UDPipe, POS tagging, lemmatization, dependency parsing, CoNLL-U]
---

# How do I annotate a corpus with UDPipe?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>intermediate</span>
<span>30–60 min</span>
</div>

## What you are trying to do

You need tokens, lemmas, POS tags, or dependency parses for a corpus.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Plain text corpus
- Language model for UDPipe

## Tools

- [UDPipe](https://ufal.mff.cuni.cz/udpipe)

## Workflow

1. Download or select the correct language model.
2. Run tokenization, tagging, and parsing on a small sample first.
3. Inspect errors on names, dialect, old spelling, or punctuation.
4. Process the full corpus.
5. Save output in CoNLL-U format.

## Output

`out.conllu` with linguistic annotation.

## Check yourself

- Does the model match the language and text type?
- Are sentence boundaries plausible?
- Are lemmas useful for your question?

## Common traps

- Using a modern-language model on historical text without checking.
- Treating automatic annotation as gold standard.
- Processing huge files without chunking.

## Worked examples

- [corpus conversion and CLASSLA annotation example](../../case-studies/corpus-augmenter.md) shows a CLASSLA-based pipeline for converting and enriching corpus annotation layers.
- [Šolar lexical analysis](../../case-studies/korpus-solar-analysis.md) shows how to reannotate while preserving source IDs and metadata links.

## Practice task

Annotate five sentences with unusual punctuation or old spelling, then diagnose the parser mistakes.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
