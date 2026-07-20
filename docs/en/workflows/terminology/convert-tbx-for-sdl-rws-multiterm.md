---
title: "How do I convert TBX for SDL/RWS MultiTerm?"
description: "You need to share terminology with colleagues working in Trados/MultiTerm."
category: "Terminology"
difficulty: "intermediate"
time: "20–45 min"
tags: [terminology, TBX, MultiTerm, CAT tools]
---

# How do I convert TBX for SDL/RWS MultiTerm?

<div class="answer-meta" markdown>
<span>Terminology</span>
<span>intermediate</span>
<span>20–45 min</span>
</div>

## What you are trying to do

You need to share terminology with colleagues working in Trados/MultiTerm.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- `glossary.tbx` or a clean spreadsheet
- Language codes and field names agreed in advance

## Tools

- [RWS MultiTerm Convert](https://docs.rws.com)

## Workflow

1. Back up the original TBX.
2. Open MultiTerm Convert and choose a TBX import workflow.
3. Map language and descriptive fields carefully.
4. Export the MultiTerm-compatible termbase.
5. Run a spot check on 10 random entries.

## Output

A MultiTerm termbase package for Trados users.

## Check yourself

- Can Trados recognize terms while translating?
- Are definitions, examples, and statuses still present?
- Are language labels correct?

## Common traps

- Assuming every TBX field maps cleanly.
- Dropping administrative fields such as source or reliability.
- Sending a termbase without usage notes.

## Practice task

One group plays “vendor”, one “client”; the client rejects unclear mappings until the vendor documents them.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
