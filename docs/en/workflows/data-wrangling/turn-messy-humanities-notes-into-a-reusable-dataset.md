---
title: "How do I turn messy humanities notes into a reusable dataset?"
description: "You have notes, archive lists, genealogy, bibliography, or fieldwork data and want structured rows without erasing uncertainty."
category: "Data wrangling"
difficulty: "beginner"
time: "45–90 min"
tags: [data modeling, metadata, messy data, humanities]
---

# How do I turn messy humanities notes into a reusable dataset?

<div class="answer-meta" markdown>
<span>Data wrangling</span>
<span>beginner</span>
<span>45–90 min</span>
</div>

## What you are trying to do

You have notes, archive lists, genealogy, bibliography, or fieldwork data and want structured rows without erasing uncertainty.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Messy notes or document excerpt
- A research question

## Tools

- [OpenRefine](https://openrefine.org)
- [Google Sheets](https://www.google.com/sheets/about/)
- [Excel](https://www.microsoft.com/microsoft-365/excel)

## Workflow

1. Underline entities: people, places, dates, events, sources.
2. Decide the unit of one row: person, event, object, or source.
3. Create columns for certainty and provenance, not only “facts”.
4. Enter a small sample and test whether the schema works.
5. Revise column names before scaling up.

## Output

CSV with clear fields, uncertainty notes, and source references.

## Check yourself

- Can every claim be traced to a source?
- Are uncertain values marked rather than silently fixed?
- Does one row mean one thing?

## Common traps

- Mixing events and people in the same row.
- Deleting ambiguity to make data look cleaner.
- Using comments instead of columns.

## Worked examples

- [Slovene Wikisource corpus build pipeline](../../case-studies/wikivir.md) shows metadata normalization for a large, messy Slovene Wikisource corpus.
- [static knowledge graph, map, and corpus index example](../../case-studies/ladakh-relations.md) shows how cleaned entities and relations can become a graph, map, and corpus index.
- [dialogue corpus tabulation and lexical-diversity example](../../case-studies/pracomul.md) shows how dialogue-corpus exports can become tidy token, turn, speaker, and aggregate tables.

## Practice task

Use one page of chaotic notes and design two different schemas; compare what each schema makes visible.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
