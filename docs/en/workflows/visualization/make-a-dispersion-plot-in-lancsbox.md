---
title: "How do I make a dispersion plot in LancsBox?"
description: "You need to show where a word or phrase appears across a text or corpus."
category: "Visualization"
difficulty: "beginner"
time: "20–40 min"
tags: [LancsBox, dispersion plot, corpus, visualization]
---

# How do I make a dispersion plot in LancsBox?

<div class="answer-meta" markdown>
<span>Visualization</span>
<span>beginner</span>
<span>20–40 min</span>
</div>

## What you are trying to do

You need to show where a word or phrase appears across a text or corpus.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Text file or corpus
- Target word/phrase

## Tools

- [LancsBox](https://corpora.lancs.ac.uk/lancsbox)

## Workflow

1. Load the corpus into LancsBox.
2. Search for the target item.
3. Generate a dispersion plot.
4. Normalize or segment texts if comparing documents.
5. Export image and explain what distribution means.

## Output

PNG/SVG dispersion plot.

## Check yourself

- Are texts comparable in length?
- Is the target lemmatized or exact-form only?
- Does the plot reveal clustering or spread?

## Common traps

- Comparing raw positions across unequal texts.
- Ignoring inflected forms.
- Treating one plot as proof without examples.

## Practice task

Users predict where a motif appears in a text, then compare prediction with the dispersion plot.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
