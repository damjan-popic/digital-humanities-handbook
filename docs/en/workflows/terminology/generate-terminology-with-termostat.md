---
title: "How do I generate terminology with Termostat?"
description: "You want terms that are characteristic of a specialized corpus compared with general language."
category: "Terminology"
difficulty: "intermediate"
time: "30–60 min"
tags: [Termostat, terminology, contrastive corpus, keywords]
---

# How do I generate terminology with Termostat?

<div class="answer-meta" markdown>
<span>Terminology</span>
<span>intermediate</span>
<span>30–60 min</span>
</div>

## What you are trying to do

You want terms that are characteristic of a specialized corpus compared with general language.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Specialized corpus
- Reference corpus

## Tools

- [Termostat](https://termostat.tsr.cesnet.cz)

## Workflow

1. Prepare both corpora in comparable formats.
2. Upload or select corpora.
3. Compute candidate terms using contrastive statistics.
4. Inspect high-ranked terms in context.
5. Export results and add human judgement.

## Output

Ranked contrastive term list.

## Check yourself

- Is the reference corpus appropriate?
- Are candidates actual terms or just topic words?
- Can the selected terms be explained as domain-relevant rather than merely frequent?

## Common traps

- Using a tiny or mismatched reference corpus.
- Keeping all statistically salient words.
- Forgetting domain expert review.

## Practice task

Compare a medical mini-corpus with a legal mini-corpus and document how “termhood” differs by domain.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
