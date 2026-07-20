---
title: "How do I visualise uncertainty in humanities data?"
description: "Your data contains approximate dates, doubtful identities, conflicting sources, or missing values."
category: "Visualization"
difficulty: "intermediate"
time: "45–90 min"
tags: [uncertainty, visualization, metadata, humanities data]
---

# How do I visualise uncertainty in humanities data?

<div class="answer-meta" markdown>
<span>Visualization</span>
<span>intermediate</span>
<span>45–90 min</span>
</div>

## What you are trying to do

Your data contains approximate dates, doubtful identities, conflicting sources, or missing values.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Dataset with uncertainty notes
- Clear uncertainty categories

## Tools

- [Datawrapper](https://www.datawrapper.de)
- [Flourish](https://flourish.studio)
- [Python Matplotlib](https://matplotlib.org)

## Workflow

1. Separate unknown, approximate, conflicting, and inferred values.
2. Add explicit certainty or evidence columns.
3. Choose visual encodings such as ranges, lighter markers, or annotations.
4. Explain uncertainty in the caption.
5. Keep raw notes accessible.

## Output

Visualization that shows uncertainty instead of flattening it.

## Check yourself

- Can viewers tell what is known and what is inferred?
- Are missing values meaningful or just absent?
- Does the caption explain choices?

## Common traps

- Replacing uncertainty with false precision.
- Using vague labels like “maybe” without categories.
- Making uncertainty visually invisible.

## Practice task

Users convert a fake “messy family history” table into a chart that refuses to lie.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
