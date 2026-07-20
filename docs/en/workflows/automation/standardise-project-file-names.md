---
title: "How do I standardise project file names?"
description: "Your project folder is chaos and you need machine-readable names."
category: "Automation"
difficulty: "beginner"
time: "15–30 min"
tags: [file management, automation, reproducibility, naming]
---

# How do I standardise project file names?

<div class="answer-meta" markdown>
<span>Automation</span>
<span>beginner</span>
<span>15–30 min</span>
</div>

## What you are trying to do

Your project folder is chaos and you need machine-readable names.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Mixed project files
- A naming convention

## Tools

- [Bulk Rename Utility](https://www.bulkrenameutility.co.uk)
- [Python pathlib](https://docs.python.org/3/library/pathlib.html)

## Workflow

1. Define a pattern before renaming: `project_lang_version.ext` is a good start.
2. Write down allowed values for language, date, version, and format.
3. Test on a copy of the folder.
4. Run a batch rename tool or small script.
5. Add the naming convention to the project README.

## Output

Consistent file names that support sorting and automation.

## Check yourself

- Can someone infer file purpose from the name?
- Do names avoid spaces and fragile punctuation?
- Are dates sortable, e.g. `YYYY-MM-DD`?

## Common traps

- Renaming without a backup.
- Encoding too much information in the file name.
- Changing names after scripts already depend on them.

## Practice task

Use a messy folder listing, invent a naming scheme, and document the trade-offs.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
