---
title: "How do I build a translation memory with OmegaT?"
description: "You want a free, cross-platform way to manage translation memory."
category: "CAT tools"
difficulty: "beginner"
time: "30–60 min"
tags: [OmegaT, translation memory, CAT tools]
---

# How do I build a translation memory with OmegaT?

<div class="answer-meta" markdown>
<span>CAT tools</span>
<span>beginner</span>
<span>30–60 min</span>
</div>

## What you are trying to do

You want a free, cross-platform way to manage translation memory.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Source files
- Existing target files or translated segments

## Tools

- [OmegaT](https://omegat.org)

## Workflow

1. Create a new OmegaT project.
2. Set source and target languages.
3. Add source files to the project.
4. Import or create translation memory entries.
5. Export the project TMX after review.

## Output

Translation memory file such as `project_save.tmx`.

## Check yourself

- Do matches appear when translating similar segments?
- Are language codes correct?
- Are old and new TMs separated by domain?

## Common traps

- Mixing unrelated domains in one huge TM.
- Keeping unreviewed machine translations as clean TM.
- Ignoring segmentation rules.

## Practice task

Users translate a repeated-text mini document and watch how TM suggestions change after the first pass.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
