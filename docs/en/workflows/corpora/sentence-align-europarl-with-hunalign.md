---
title: "How do I sentence-align EuroParl with hunalign?"
description: "You need sentence-aligned data for translation analysis or MT experiments."
category: "Corpora"
difficulty: "advanced"
time: "60–120 min"
tags: [alignment, EuroParl, hunalign, parallel corpus]
---

# How do I sentence-align EuroParl with hunalign?

<div class="answer-meta" markdown>
<span>Corpora</span>
<span>advanced</span>
<span>60–120 min</span>
</div>

## What you are trying to do

You need sentence-aligned data for translation analysis or MT experiments.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- EuroParl source and target texts
- Optional bilingual dictionary

## Tools

- [hunalign](https://github.com/danielvarga/hunalign)
- [EuroParl](https://www.statmt.org/europarl/)

## Workflow

1. Extract or strip XML into clean text.
2. Ensure source and target documents correspond.
3. Run hunalign with a dictionary if available.
4. Inspect alignment scores and suspicious gaps.
5. Export aligned text or TMX.

## Output

Sentence-aligned parallel file.

## Check yourself

- Are document boundaries preserved?
- Do alignment scores identify weak pairs?
- Are one-to-many pairs handled?

## Common traps

- Aligning mismatched editions.
- Ignoring deleted or added paragraphs.
- Using aligned data for training without quality sampling.

## Practice task

Users hand-align ten sentence pairs, then compare with automatic alignment and discuss why aligners fail.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
