---
title: "How do I evaluate OCR or HTR against a reference sample?"
description: "Build a checked sample, calculate CER and WER, classify errors and test whether they alter a humanities claim."
category: "PDF & OCR"
category_id: "pdf"
difficulty: "beginner"
time: "60–90 min"
tags: [OCR, HTR, CER, WER, transcription, evaluation]
---

# How do I evaluate OCR or HTR against a reference sample?

<div class="answer-meta" markdown>
<span>PDF & OCR</span><span>beginner</span><span>60–90 min</span>
</div>

## What you are trying to do

You have OCR for print or HTR for handwriting and want to know whether it is usable. A few visually impressive lines or one overall confidence score cannot answer that. Compare a declared sample with a human-checked reference, measure edit distance, classify the failures and test the research task that depends on the text.

No programming is required. The supplied teaching packet includes a tiny candidate/reference pair and computed results. You can inspect and explain them with a text editor and spreadsheet; the reproducibility command is an optional maintainer extension.

## You need

- the page images and an unchanged recognition export;
- a written transcription policy;
- a human-checked reference transcription for a declared sample;
- a spreadsheet or an edit-distance tool that reports substitutions, deletions and insertions; and
- optionally, the open [Archival Friction teaching packet](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction): `raw/provider-ocr.txt`, `cleaned/gold-transcription.txt`, `source/transcription-note.md` and `output/ocr-evaluation.csv`.

Check the source, rights and provenance record before copying images or text. Keep the candidate and reference in separate files.

## Workflow

### 1. Define the intended claim

Write one use case: finding a person's name, counting a word, comparing lexical frequencies, extracting dates or quoting a passage. List the text features it depends on. This makes “good enough” testable: a score adequate for broad search may still be inadequate for exact quotation.

### 2. Declare the evaluation population and sample

State what collection, titles, dates, document types and recognition route you intend the result to describe. Then select pages or lines across relevant strata such as typeface or hand, scan quality, layout, language, captions, tables and proper names.

Keep a random or systematic component. Report a purposive challenge set separately. Record the selection rule and the numbers of pages, lines, reference characters and reference words. A convenient clean passage can teach the calculation but cannot estimate a collection.

### 3. Freeze and diagnose the first inadequate result

Treat the first OCR or HTR output as an inadequate candidate until tested, then save it exactly as delivered. Record provider, service or software, version or access date, model identifier, language and layout settings, export format and run date. Interfaces and hosted models change, so preserve the export that you actually evaluate.

Give the candidate a sample identifier and connect it to exact page coordinates or a stable image locator. Do not correct this file.

### 4. Prepare the reference under explicit rules

Have a person transcribe and check the same region against the image. Beforehand decide:

- reading order and included regions;
- treatment of line breaks and line-end hyphenation;
- historical spelling, ligatures, abbreviations, capitalization and punctuation;
- Unicode normalization and spaces;
- notation for illegible or missing text; and
- whether corrections and normalized forms are represented separately.

Record the transcriber, checker, dates and policy version. Resolve disagreements through the written policy or mark them unresolved. Do not quietly make the reference resemble the candidate.

### 5. Normalize only what the test excludes

Apply exactly the same declared preprocessing to candidate and reference. If case does not matter, fold case in both; if punctuation matters, retain it in both. The packet strips surrounding whitespace and uses Unicode NFC but otherwise retains character differences. For WER it uses whitespace-delimited words.

Save the normalization and tokenization rules with the result. A CER without them is ambiguous.

### 6. Run automated alignment and calculate

Use minimum edit distance to count substitutions \(S\), deletions \(D\) and insertions \(I\) against \(N\) reference units:

\[
\mathrm{error\ rate}=\frac{S+D+I}{N}
\]

Calculate once with characters for CER and once with your defined word tokens for WER. Record the counts as well as the rates. Do not call \(1-\mathrm{CER}\) “accuracy” without defining it; insertions can make an error rate greater than 1.

The packet's sample `AF-OCR-P1-INTRO` contains 591 reference characters, 15 character edits, 93 reference words and 9 word edits. Therefore:

- CER = `15 / 591 = 0.025381` (about 2.54%);
- WER = `9 / 93 = 0.096774` (about 9.68%).

Enter the numerators and denominators in separate spreadsheet cells, calculate the divisions, and compare them byte-for-byte with `output/ocr-evaluation.csv` rather than rounding first.

### 7. Make manual decisions about consequential errors

Make one audit row per aligned difference with the sample and page locator, reference string, candidate string, edit type, category and likely consequence. Include character confusion, diacritic, split/join, line-end hyphenation, punctuation, name, number, omitted region, duplicated region, reading order and transcription-policy difference.

Inspect omissions at the image level. Plain-text alignment cannot score a caption that neither file includes. Report error counts by stratum when the sample is large enough.

### 8. Test the downstream task

Run the use case from step 1 on both versions. For search, compare true and missed hits. For word counts, list changed forms and totals. For entity extraction, compare correct, missed and false entities. For quotation, verify every character directly against the image.

Write a decision:

- **proceed** when measured errors do not materially change the narrow claim;
- **revise** when targeted correction, a different model, better segmentation or a narrower claim may solve the problem; or
- **stop** when missing pages, incompatible policy, uncheckable reference or systematic error invalidates the comparison.

### 9. Preserve unresolved cases, the result and its limits

Keep image, candidate, reference, policy, metrics, audit table and decision as linked but separate objects. Add checksums and a known-problems note. State exactly which population and strata the estimate covers, which it omits and whether the evaluation was random, systematic or purposive.

## Output

Deliver a sample manifest, frozen candidate, checked reference, transcription policy, CER/WER table, error audit, downstream comparison and proceed/revise/stop decision.

The workflow passes when another person can recover the same sample, apply the stated normalization, reproduce the numerators and denominators, locate at least five errors on the image and understand why the conclusion is limited. Matching the packet's values without explaining their scope is not enough.

## Check yourself

- Does the sample include the layouts and text features central to the claim?
- Are candidate and reference distinct, frozen files?
- Did you apply identical, documented normalization?
- Can you explain every denominator and edit count?
- Did you inspect region omission and reading order, not only character substitutions?
- Have you compared the actual downstream result?

## Common traps

- Evaluating only a clean or convenient page.
- Calling a human transcription neutral “truth” without a policy.
- Correcting the candidate before preserving it.
- Comparing files with different line-break, case or Unicode conventions.
- Treating one aggregate CER as a universal quality threshold.
- Ignoring names, captions or tables because ordinary prose scores well.
- Generalizing one passage to a publication, platform or model.

## Practice task

Use the packet to verify the reported CER and WER. Classify five differences and test a search for one proper name in the provider and reference files. Write a two-sentence result: first the measured finding for sample `AF-OCR-P1-INTRO`, then the boundary beyond which it cannot be generalized.

For the underlying concepts and references, read [Texts, corpora and OCR](../../chapters/texts-corpora-ocr.md). Current technical definitions are in the [OCR-D quality-assurance documentation](https://ocr-d.de/en/spec/ocrd_eval.html) and [Ground Truth Guidelines](https://ocr-d.de/en/gt-guidelines/trans/) (living documentation; accessed 2 September 2026).
