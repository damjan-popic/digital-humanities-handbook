---
title: "How do I run forbidden-term QA in a CAT tool?"
description: "A client, institution, or style guide bans certain terms and you need automatic checks."
category: "Terminology"
difficulty: "intermediate"
time: "20–40 min"
tags: [terminology, QA, CAT tools, controlled language]
---

# How do I run forbidden-term QA in a CAT tool?

<div class="answer-meta" markdown>
<span>Terminology</span>
<span>intermediate</span>
<span>20–40 min</span>
</div>

## What you are trying to do

A client, institution, or style guide bans certain terms and you need automatic checks.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Translation project
- Term list with accepted and forbidden terms

## Tools

- [memoQ QA](https://help.memoq.com)
- [RWS Trados QA Checker](https://docs.rws.com)

## Workflow

1. Create term entries with clear status: preferred, admitted, deprecated, forbidden.
2. Attach the termbase to the project.
3. Enable terminology checks in QA settings.
4. Run QA before delivery.
5. Review every hit; some “violations” may be legitimate quoted text.

## Output

QA report showing forbidden-term hits.

## Check yourself

- Are false positives documented?
- Are critical terms set to block delivery?
- Does the report identify segment numbers?

## Common traps

- Using only a plain forbidden-word list without context.
- Failing to distinguish source quotes from translator choices.
- Treating QA as a substitute for review.

## Practice task

Users build a micro style guide for one domain, then test whether QA catches violations in a short translation.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
