---
title: "How do I validate a TBX file before publishing it?"
description: "You have a TBX file and want to catch broken XML or schema problems before sharing it."
category: "Terminology"
difficulty: "beginner"
time: "10–20 min"
tags: [terminology, TBX, XML, validation]
---

# How do I validate a TBX file before publishing it?

<div class="answer-meta" markdown>
<span>Terminology</span>
<span>beginner</span>
<span>10–20 min</span>
</div>

## What you are trying to do

You have a TBX file and want to catch broken XML or schema problems before sharing it.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- `*.tbx` file
- The intended TBX profile, if known

## Tools

- [TBXChecker](https://github.com/LTAC-Global/tbxchecker)

## Workflow

1. Open the TBX file in TBXChecker.
2. Select the relevant TBX profile.
3. Run validation.
4. Separate critical XML errors from softer data-quality warnings.
5. Fix the source data if possible, not only the exported TBX.

## Output

A validation log and a corrected TBX file.

## Check yourself

- Does the file open in a CAT tool?
- Are all languages represented consistently?
- Do IDs remain stable after correction?

## Common traps

- Treating all warnings as equally urgent.
- Fixing exported XML while leaving the spreadsheet broken.
- Ignoring character-encoding errors.

## Practice task

Users exchange TBX files and produce a friendly bug report: error, likely cause, suggested fix.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
