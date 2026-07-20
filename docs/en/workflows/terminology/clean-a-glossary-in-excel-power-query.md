---
title: "How do I clean a glossary in Excel Power Query?"
description: "You need repeatable cleaning rather than one-off spreadsheet surgery."
category: "Terminology"
difficulty: "beginner"
time: "20–40 min"
tags: [terminology, Excel, Power Query, data cleaning]
---

# How do I clean a glossary in Excel Power Query?

<div class="answer-meta" markdown>
<span>Terminology</span>
<span>beginner</span>
<span>20–40 min</span>
</div>

## What you are trying to do

You need repeatable cleaning rather than one-off spreadsheet surgery.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- `glossary.xlsx` or `.csv` with inconsistent spacing, casing, duplicates, or blank rows

## Tools

- [Excel Power Query](https://support.microsoft.com/excel)

## Workflow

1. Load the table with **Data → Get Data**.
2. Apply **Trim** and **Clean** to term columns.
3. Normalize casing only if your domain allows it.
4. Remove duplicate rows, then separately inspect near-duplicates.
5. Close and load the cleaned table; save the query steps.

## Output

A cleaned sheet that can be refreshed when new data arrives.

## Check yourself

- Can you re-run the cleaning on a new version?
- Did you keep an untouched original sheet?
- Do cleaned terms still preserve intended capitalization?

## Common traps

- Accidentally lowercasing named entities.
- Deleting “duplicates” that are actually different concepts.
- Doing manual edits after Power Query and then losing them on refresh.

## Practice task

Run a “before/after autopsy”: groups document three cleaning decisions and one decision they are not sure about.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
