---
title: "Texts, corpora and OCR"
description: "How to build interpretable text collections from born-digital, scanned and historically variable sources."
tags: [text, corpus, OCR, sampling]
status: draft
---

# Texts, corpora and OCR

## Learning outcomes

After this chapter, you should be able to:

- distinguish document images, OCR text, corrected text, linguistic annotation and metadata;
- design a corpus around a question rather than around convenience;
- assess representativeness, balance and comparability;
- choose a normalization policy appropriate to historical or non-standard language;
- measure OCR quality and explain its effect on later analysis.

## Before you begin

Open a scanned historical page and its OCR transcription. Find five differences. Which errors would prevent search? Which would change a word frequency? Which would mislead a named-entity recognizer? Not every error has the same research cost.

Digitization, OCR and corpus delivery depend on institutional choices as well as software. Use [Infrastructures of digital humanities](critical-infrastructures.md) to examine selection, access and maintenance, and [Digital humanities in Slovenia](digital-humanities-in-slovenia.md) for a local example of the steps between a library scan and a deposited corpus.

## A digital text has layers

A single document can have several related representations:

1. **image** — the scan or photograph;
2. **layout description** — regions, columns, lines, marginalia;
3. **diplomatic transcription** — a close record of visible characters and structure;
4. **normalized text** — standardized spelling, punctuation or encoding;
5. **linguistic annotation** — tokens, lemmas, part-of-speech tags, entities or syntax;
6. **metadata** — source, date, author, genre, rights and processing history.

These layers should not silently overwrite one another. The image remains evidence when OCR is uncertain. The diplomatic text preserves historical form. A normalized version may support search, but it is an interpretation and should be linked to the original.

## Corpus design begins with inclusion rules

A corpus is a purposive collection of texts, not simply a folder containing many files. Its boundaries must be justified.

Specify:

- target population: what larger body of texts the corpus is intended to represent;
- sampling frame: which materials were actually available for selection;
- inclusion and exclusion criteria;
- time, genre, region, language and authorship coverage;
- unit of sampling and unit of analysis;
- known gaps, duplication and rights restrictions.

A million web pages may be less useful than one thousand well-documented documents if the research requires period, genre or authorship comparisons.

## Representativeness is a claim

No corpus represents “language” or “culture” in the abstract. It represents a defined population under a set of choices. Web corpora overrepresent material that is public, crawlable and search-engine visible. Newspaper archives reflect survival, licensing and digitization priorities. Literary corpora often overrepresent canonical, public-domain works.

Use metadata tables and distribution plots to inspect balance. Count documents and words by year, genre, source, author and other relevant strata. Large word counts do not compensate for a missing category.

## OCR as measurement

Optical character recognition predicts text from images. It is not neutral transcription. Quality depends on print, script, language model, scan resolution, layout, hyphenation, page damage and historical spelling.

Two common measures are:

- **character error rate (CER):** substitutions, insertions and deletions relative to reference characters;
- **word error rate (WER):** the same logic at word level.

A global score can hide unequal failure. Proper names, diacritics, small type, tables or minority-language passages may be much worse than ordinary prose. Evaluate a stratified sample that includes difficult pages and the text features central to the research.

## The downstream cost of OCR errors

OCR affects methods differently:

- full-text search loses recall when target words are misspelled;
- frequency lists fragment one word into many erroneous forms;
- lemmatizers and taggers may fail on corrupted tokens;
- named-entity recognition is especially vulnerable to unusual names;
- topic models may create noise topics around repeated OCR artefacts;
- quotations and editions require much higher fidelity than aggregate trends.

The right correction effort therefore depends on the claim. A rough trend analysis may tolerate errors that a scholarly edition cannot.

## Normalization and historical variation

Normalization can improve comparability but erase evidence. Keep the original and normalized forms separately. Document rules for:

- Unicode and character encoding;
- line-break hyphenation;
- historical characters and diacritics;
- spelling variants;
- punctuation and quotation marks;
- boilerplate, headers and page numbers;
- language mixing and code-switching.

Automatic normalization should be reversible or at least auditable. A correction list with source form, replacement, context and reason is preferable to undocumented search-and-replace.

## Deduplication and document identity

Digital collections often contain duplicates: mirrored web pages, syndicated news, revised editions, OCR exports of the same scan or documents quoted inside other documents. Duplicates can dominate frequencies and falsely increase confidence.

Assign document IDs, calculate exact hashes for identical files and use similarity methods for near-duplicates. Do not delete blindly: duplicated circulation may itself be historically meaningful. Mark relationships such as `duplicate_of`, `reprint_of` or `version_of` and decide which level the analysis needs.

## Worked example: a historical newspaper corpus

A defensible workflow might be:

1. select newspaper titles and years according to the question;
2. record issue-level and article-level metadata;
3. retain page images and OCR separately;
4. sample pages across titles, years and layout types for OCR evaluation;
5. correct high-impact systematic errors;
6. segment articles and preserve links to page coordinates;
7. document missing issues and changes in publication frequency;
8. compare word and document distributions before analysis;
9. keep an error register and cite the corpus release.

## Practice

Create a corpus card for a collection you could realistically build. Include target population, sampling frame, inclusion rules, exclusion rules, metadata fields, expected OCR or extraction errors, duplicate policy and the strongest comparison the corpus can support.

## Reflection

- Which missing texts are invisible because they were never digitized?
- Would normalization remove a feature your interpretation might later need?
- Which OCR errors matter most for your planned method?

## Summary

A text corpus is a documented research instrument. It consists of linked layers, explicit boundaries, metadata and measured transformations. OCR and normalization create useful text but also new uncertainty. Corpus quality is not the number of tokens; it is the fit between selection, representation, error profile and research claim.
