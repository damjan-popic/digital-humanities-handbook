---
title: "How do I version-control a termbase with Git?"
description: "Several people edit terminology and you need a history of who changed what."
category: "Terminology"
difficulty: "intermediate"
time: "30–60 min"
tags: [terminology, Git, version control, collaboration]
---

# How do I version-control a termbase with Git?

<div class="answer-meta" markdown>
<span>Terminology</span>
<span>intermediate</span>
<span>30–60 min</span>
</div>

## What you are trying to do

Several people edit terminology and you need a history of who changed what.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Text-based termbase such as TBX, TSV, CSV, or JSON
- A Git repository

## Tools

- [Git](https://git-scm.com)
- [Git LFS](https://git-lfs.com)

## Workflow

1. Prefer plain text formats when possible.
2. Commit a clean initial version.
3. Use small commits with meaningful messages, e.g. `add climate terms`.
4. Review diffs before merging changes.
5. Use Git LFS only for large binary files.

## Output

A termbase with a transparent edit history.

## Check yourself

- Can you see a meaningful diff?
- Are changes grouped by topic?
- Can a previous version be restored?

## Common traps

- Putting huge `.xlsx` files in normal Git history.
- Committing generated files that change on every export.
- Merging terminology without editorial review.

## Practice task

Introduce a controlled bad edit, commit it, and then recover the previous version using Git history.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
