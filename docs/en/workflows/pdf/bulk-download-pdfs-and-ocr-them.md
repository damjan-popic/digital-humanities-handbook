---
title: "How do I bulk-download PDFs and OCR them?"
description: "You have many scanned PDFs and need searchable text."
category: "PDF & OCR"
difficulty: "intermediate"
time: "60–120 min"
tags: [PDF, OCR, Tesseract, archives, corpus]
---

# How do I bulk-download PDFs and OCR them?

<div class="answer-meta" markdown>
<span>PDF & OCR</span>
<span>intermediate</span>
<span>60–120 min</span>
</div>

## What you are trying to do

You have many scanned PDFs and need searchable text.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- CSV or text file of PDF URLs
- Language(s) for OCR

## Tools

- [wget](https://www.gnu.org/software/wget/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Poppler](https://poppler.freedesktop.org)

## Workflow

1. Confirm that you may download and process the files.
2. Download PDFs into a dedicated folder.
3. Convert pages to images if needed.
4. Run OCR with the appropriate language model.
5. Store text, original PDF, and processing log together.

## Output

`ocr_text/*.txt` plus OCR logs.

## Check yourself

- Are page numbers preserved?
- Are diacritics recognized?
- Is OCR quality good enough for the intended analysis?

## Common traps

- Assuming searchable PDF equals clean text.
- Ignoring columns, tables, and footnotes.
- Not recording OCR settings.

## Practice task

Use one difficult page, compare OCR settings, and write an honest error report rather than only reporting the prettiest output.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
