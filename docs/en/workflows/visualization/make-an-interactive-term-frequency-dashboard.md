---
title: "How do I make an interactive term-frequency dashboard?"
description: "You want stakeholders to filter and explore term counts without opening a spreadsheet."
category: "Visualization"
difficulty: "intermediate"
time: "45–90 min"
tags: [dashboard, terminology, Observable, visualization]
---

# How do I make an interactive term-frequency dashboard?

<div class="answer-meta" markdown>
<span>Visualization</span>
<span>intermediate</span>
<span>45–90 min</span>
</div>

## What you are trying to do

You want stakeholders to filter and explore term counts without opening a spreadsheet.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- `term_count.csv` with term and count columns

## Tools

- [Observable Plot](https://observablehq.com/plot)

## Workflow

1. Prepare a tidy CSV with one row per term.
2. Create a basic bar chart.
3. Add filters for language, domain, or source.
4. Document how counts were produced.
5. Share a read-only dashboard link.

## Output

Interactive dashboard or notebook.

## Check yourself

- Are axes labeled?
- Can viewers filter without breaking the view?
- Is data provenance visible?

## Common traps

- Dashboarding dirty data.
- Using interactivity to hide unclear assumptions.
- Leaving stakeholders without export options.

## Practice task

Users turn a frequency table into a one-screen dashboard and write the caption first, then the chart.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
