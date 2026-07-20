---
title: "How do I align bilingual documents with LF Aligner?"
description: "You have source and target documents and want a translation memory or parallel corpus."
category: "CAT tools"
difficulty: "intermediate"
time: "30–60 min"
tags: [alignment, translation memory, LF Aligner, parallel corpus]
---

# How do I align bilingual documents with LF Aligner?

<div class="answer-meta" markdown>
<span>CAT tools</span>
<span>intermediate</span>
<span>30–60 min</span>
</div>

## What you are trying to do

You have source and target documents and want a translation memory or parallel corpus.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Source document
- Target document
- Language pair

## Tools

- [LF Aligner](https://sourceforge.net/projects/aligner)

## Workflow

1. Prepare clean source and target text.
2. Run LF Aligner and choose the correct language pair.
3. Inspect proposed sentence alignments.
4. Fix splits, joins, omissions, and reordered sections.
5. Export TMX or aligned text.

## Output

`aligned.tmx` or sentence-aligned parallel text.

## Check yourself

- Are headings and boilerplate handled?
- Do sentence counts roughly match?
- Are one-to-many alignments documented?

## Common traps

- Assuming alignment is automatic truth.
- Forgetting to remove footers or page numbers.
- Exporting without spot-checking.

## Practice task

Give groups the same bilingual text pair and compare the alignment errors they find.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
