---
title: "How do I turn an Excel glossary into TBX?"
description: "You have a spreadsheet of terms and need a standards-friendly termbase that CAT tools can import."
category: "Terminology"
difficulty: "beginner"
time: "15–25 min"
tags: [terminology, TBX, glossary, Excel, beginner]
---

# How do I turn an Excel glossary into TBX?

<div class="answer-meta" markdown>
<span>Terminology</span>
<span>beginner</span>
<span>15–25 min</span>
</div>

## What you are trying to do

You have a spreadsheet of terms and need a standards-friendly termbase that CAT tools can import.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- `glossary.xlsx` with at least one term column and one language column
- Optional columns: definition, context, source, domain, status, note

## Tools

- [Glossary Converter](https://www.glossaryconverter.com)

## Workflow

1. Clean obvious duplicates and empty rows before conversion.
2. Open Glossary Converter and drop the spreadsheet onto the app.
3. Map each column to a language or metadata field.
4. Choose **TBX-Basic** or the lightest TBX profile your tool supports.
5. Convert, then open the result in a text editor to check that diacritics survived.

## Output

`glossary.tbx` ready for import or validation.

## Check yourself

- Can another person identify the languages without guessing?
- Are forbidden/deprecated terms marked as such rather than deleted?
- Do special characters display correctly?

## Common traps

- Mixing multiple concepts in one row.
- Using colour as metadata; export will lose it.
- Forgetting source/provenance columns.

## Practice task

Use a deliberately messy glossary. Clean it, convert it to TBX, then try importing the result in a terminology tool.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
