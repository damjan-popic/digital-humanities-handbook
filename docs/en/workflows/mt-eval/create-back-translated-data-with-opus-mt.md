---
title: "How do I create back-translated data with OPUS-MT?"
description: "You need synthetic parallel data for low-resource MT experiments."
category: "MT evaluation"
difficulty: "advanced"
time: "60–180 min"
tags: [machine translation, back-translation, OPUS-MT, data augmentation]
---

# How do I create back-translated data with OPUS-MT?

<div class="answer-meta" markdown>
<span>MT evaluation</span>
<span>advanced</span>
<span>60–180 min</span>
</div>

## What you are trying to do

You need synthetic parallel data for low-resource MT experiments.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Monolingual target-language text
- Translation model in the reverse direction

## Tools

- [Marian NMT](https://marian-nmt.github.io)
- [OPUS-MT models](https://huggingface.co/Helsinki-NLP)

## Workflow

1. Clean and segment monolingual target text.
2. Translate it backward into the source language.
3. Tag synthetic lines, e.g. `__BT__`.
4. Mix synthetic and authentic parallel data deliberately.
5. Evaluate whether synthetic data helps or harms.

## Output

Synthetic source text paired with original target text.

## Check yourself

- Are synthetic lines labeled?
- Is domain mismatch controlled?
- Did downstream evaluation improve?

## Common traps

- Confusing synthetic data with human translations.
- Adding huge noisy data without validation.
- Training and testing on overlapping material.

## Practice task

Use a toy example: back-translate five sentences and mark where the synthetic wording looks unnatural.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
