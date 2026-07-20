---
title: "How do I evaluate machine translation with COMET?"
description: "You need a reference-based automatic MT evaluation score alongside human inspection."
category: "MT evaluation"
difficulty: "advanced"
time: "45–120 min"
tags: [machine translation, COMET, evaluation, metrics]
---

# How do I evaluate machine translation with COMET?

<div class="answer-meta" markdown>
<span>MT evaluation</span>
<span>advanced</span>
<span>45–120 min</span>
</div>

## What you are trying to do

You need a reference-based automatic MT evaluation score alongside human inspection.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Source file
- MT output file
- Reference translation file

## Tools

- [COMET](https://github.com/Unbabel/COMET)

## Workflow

1. Prepare aligned `src`, `mt`, and `ref` files with identical line counts.
2. Run COMET evaluation.
3. Export segment-level and system-level scores.
4. Inspect low-scoring segments manually.
5. Report metric version and model name.

## Output

`comet_scores.csv` and summary score.

## Check yourself

- Do all files have matching line counts?
- Are scores interpreted with examples?
- Is metric version documented?

## Common traps

- Reporting one metric as final truth.
- Ignoring domain and language-pair limitations.
- Mixing segment order.

## Practice task

Users rank three MT outputs manually, then compare their rankings with COMET and debate disagreements.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
