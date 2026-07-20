---
title: "How do I automate a linguistic workflow with a Makefile?"
description: "You want one command to rebuild outputs from raw data."
category: "Automation"
difficulty: "intermediate"
time: "45–90 min"
tags: [Makefile, automation, reproducibility, workflow]
---

# How do I automate a linguistic workflow with a Makefile?

<div class="answer-meta" markdown>
<span>Automation</span>
<span>intermediate</span>
<span>45–90 min</span>
</div>

## What you are trying to do

You want one command to rebuild outputs from raw data.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Raw data
- Scripts or command-line steps
- Desired output

## Tools

- [GNU Make](https://www.gnu.org/software/make)

## Workflow

1. List outputs and the inputs they depend on.
2. Create targets such as `clean`, `tokenize`, `align`, and `report`.
3. Run each target independently.
4. Add `.PHONY` for command targets.
5. Document `make all` in the README.

## Output

Reproducible workflow controlled by `make`.

## Check yourself

- Does `make all` work from a fresh clone?
- Are intermediate files created predictably?
- Can a failed step be rerun?

## Common traps

- Automating before understanding the steps.
- Using absolute paths tied to one computer.
- Not separating generated files from source files.

## Worked examples

- [this MkDocs publishing workflow](../../contribute/index.md) shows a documentation workflow with validation and GitHub Pages deployment.
- [Šolar lexical analysis](../../case-studies/korpus-solar-analysis.md) shows a multi-step corpus pipeline with scripts, configs, reports, and outputs.

## Practice task

Manually perform three steps, convert them into a Makefile, and then test what happens when a dependency changes.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
