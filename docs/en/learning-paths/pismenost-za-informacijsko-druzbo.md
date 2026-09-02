---
title: "Information Society Literacy"
description: "A low-threshold course path from questions and sources to structured writing, verified citations, checked spreadsheet evidence, and responsible submission."
tags: [course, information-literacy, scholarly-writing, reference-management, data-literacy, AI-literacy]
status: draft
---

# Information Society Literacy

## Purpose

This path is designed for first-year and non-technical humanities students who need one coherent route from a research question to a structured, cited, and inspectable submission. It combines scholarly writing, source evaluation, reference management, word processing, spreadsheet data work, basic text and spatial methods, and responsible use of artificial intelligence.

The course should not be reduced to software menus. Interfaces change. The durable outcome is the ability to define a question, distinguish evidence from interpretation, preserve source and data lineage, check output, revise a claim, and communicate limits.

Start with the paired [scholarly-work foundations route](../foundations/scholarly-work.md), which connects writing, Zotero, Word or LibreOffice Writer, and Excel in one research cycle.

## Prior knowledge and access

No programming experience is required. You should be able to use a web browser, create and organize files, and prepare a basic written assignment.

No WSL, Bash, Git or Python is required to pass this course. You can complete the assessed route with graphical tools. A stable ZIP or dated snapshot is acceptable where version control is not taught. The [technical workspace route](../foundations/technical-workspace.md) is an optional extension, not a hidden prerequisite.

Because Word, LibreOffice, Zotero, Excel, and Power Query differ by platform and release, instructors should publish the tested platform and an equivalent fallback before each assignment. The learning outcome is the documented scholarly operation, not reproduction of one ribbon layout.

## Learning outcomes

By the end of the path, you should be able to:

- turn a research question into a structured and revisable scholarly text for a named audience and genre;
- distinguish a source, bibliographic record, attachment, note, citation, bibliography, and stable identifier;
- build and verify a small Zotero library, identify the required citation system and guidelines, select the corresponding style, and audit five varied records;
- insert citations with appropriate locators and generate and refresh a bibliography in Word or LibreOffice Writer;
- use real heading styles, contents, captions, cross-references, comments, and tracked changes;
- import, clean, and summarize a small Excel dataset without silently changing identifiers or types;
- document a raw-to-clean transformation and distinguish a repeatable query from one-off cell editing;
- connect every table or figure to a source, observational unit, measure, denominator, missing-value rule, check, and interpretive claim;
- distinguish text, image, OCR, annotation, and derived data and perform a basic text or spatial exploration;
- assess provenance, privacy, copyright, licensing, accessibility, and the limits of AI assistance;
- package a scholarly dossier that a peer can inspect without requiring public publication.

## Suggested 14-module sequence

### 1. Digital literacy in historical and social context

Read [What is digital humanities?](../chapters/what-is-digital-humanities.md) and selected sections of [Histories and genealogies of digital humanities](../chapters/history-of-digital-humanities.md). Map a familiar assignment from source discovery to submission. Identify where an institution, format, platform, interface, or inherited convention shapes what becomes visible.

**Output:** a one-page process map with one access or power question.

### 2. Questions, models, evidence and research design

Use [Models, evidence and interpretation](../chapters/models-evidence-interpretation.md), [Infrastructures of digital humanities](../chapters/critical-infrastructures.md), and [From question to method](../chapters/research-design.md). Turn a broad topic into one bounded research question. Define the object, scope, possible evidence, provisional model, alternative explanation, and one infrastructural limit.

Use the [Archival Friction teaching packet](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction) to test a plausible question against the actual sampling frame, source rights, dates and record units. Narrow or reformulate the claim when the two-page source cannot support it.

**Output:** a question-and-evidence brief that distinguishes description, evidence, interpretation, and recommendation.

### 3. Scholarly writing and structured documents

First [turn the research question into a scholarly paper plan](../workflows/scholarly-writing/turn-a-research-question-into-a-scientific-paper-plan.md): name the audience and genre, draft a working claim, map sections, connect sources to claims, and revise one paragraph. Then [structure the long document with styles, captions, and cross-references](../workflows/scholarly-writing/structure-a-long-document-with-styles-captions-and-cross-references.md). Use real headings, an automatic contents page, fields, notes, comments, tracked changes, and meaningful alternative text. Begin a [revision log](../workflows/scholarly-writing/revise-claims-evidence-and-paragraphs.md).

**Output:** a one-page argument plan, source-to-claim table, revised paragraph, and structured `.docx` or `.odt` draft.

### 4. Search, source evaluation and the Slovenian resource ecosystem

Build a search strategy with concepts, synonyms, language variants, Boolean combinations, and source filters. Compare a library catalogue, bibliographic database, institutional repository, and general search engine. Profile one relevant resource from [Digital humanities in Slovenia](../chapters/digital-humanities-in-slovenia.md). Record search strings, dates, selection criteria, exclusions, and access conditions.

**Output:** a search and source-selection log with three different source environments.

### 5. Zotero, citation systems, styles and bibliography management

Complete all three reference workflows. [Build and clean a small Zotero library](../workflows/reference-management/build-and-clean-a-zotero-library.md), including identifier, catalogue, Connector, and manual-entry routes. [Choose, apply, and audit the required citation style](../workflows/reference-management/choose-apply-and-audit-a-citation-style.md): record its authority and version, then test five source types. Finally [insert citations with Zotero in Word or LibreOffice](../workflows/reference-management/cite-with-zotero-in-word-or-libreoffice.md), add appropriate locators, create a multiple-source citation, generate and refresh the bibliography, and correct metadata in Zotero.

Explain one source or metadata case that the style does not handle cleanly. Do not maintain the same document with both Zotero and Word's built-in citation manager. Keep the document with active Zotero fields as the master; follow the venue's delivery requirements and unlink only a separately named, backed-up final submission copy when static text is required. Never unlink the working master merely to repair formatting.

**Output:** five verified Zotero records, a linked document with citations and generated bibliography, and a short `citation-style-audit/` recording authority, tests, corrections, deviations, and unresolved cases.

### 6. Files, formats, folders, README and backup

Create a project folder with `sources`, `notes`, `data/raw`, `data/cleaned`, `outputs`, `validation`, and `known-problems`. Compare `.docx`, `.odt`, `.pdf`, `.txt`, `.csv`, `.xlsx`, image, RIS, and ZIP files. Use [Data, metadata and models](../chapters/data-metadata-models.md) to write a README, file-naming rule, backup rule, and rights note.

A stable ZIP or dated snapshot is sufficient for assessment. If you choose the optional technical extension, you may use the [technical workspace route](../foundations/technical-workspace.md) for Git and command-line versioning, but the course does not require it.

**Output:** a recoverable project package whose raw and working layers are visibly distinct.

### 7. Excel data structure and cleaning

Define one row and one variable before editing. Use the [messy-notes workflow](../workflows/data-wrangling/turn-messy-humanities-notes-into-a-reusable-dataset.md) and [reconcile conflicting metadata without erasing uncertainty](../workflows/data-wrangling/reconcile-conflicting-metadata-without-erasing-uncertainty.md), then [import and clean the small dataset in Excel](../workflows/data-wrangling/import-and-clean-a-small-dataset-in-excel.md). Inspect delimiter, encoding, decimal/date locale, and types; protect leading-zero identifiers as text; define missingness; use an Excel table, filters, frozen headings, formulas where appropriate, and a validation list. Preserve source, raw, interim, modelled, decision and unresolved layers.

**Output:** raw and cleaned files, data dictionary, validation list, transformation log, and five-row manual check.

### 8. Repeatable spreadsheet analysis and visual communication

[Record repeatable transformations in Excel Power Query](../workflows/data-wrangling/make-repeatable-transformations-with-excel-power-query.md): rename and type columns, trim/clean and split text, filter by a stated rule, replace documented categories, merge a lookup, and refresh after a source change. Remove exact duplicate rows directly; when candidate rows differ, use an explicit priority, grouping/index, or retain/exclude rule rather than trusting visible sort order. Verify retained identifiers and row counts. Inspect Applied Steps and diagnose one broken step. If Power Query authoring is unavailable, complete the documented fallback and have the steps run once on a supported platform.

Then [summarize the cleaned data with a PivotTable and one transparent chart](../workflows/data-wrangling/summarize-data-with-pivottables-and-transparent-charts.md). Distinguish row count, distinct documents, sum, and average; expose missing categories and denominator; refresh; and manually verify a small subset.

**Output:** repeatable raw-to-clean procedure, refreshed result, checked PivotTable, one restrained chart, complete caption, alternative text, and interpretation with a limitation.

### 9. Documents, OCR and corpus basics

Read [Texts, corpora and OCR](../chapters/texts-corpora-ocr.md), then [evaluate OCR or HTR against a reference sample](../workflows/pdf/evaluate-ocr-or-htr-against-a-reference-sample.md). Compare a scan and machine text, declare transcription and sampling rules, calculate CER and WER, classify errors that change names, dates, negation or word boundaries, and test one search or count on both versions. Keep the image, layout, provider, reference, normalized and annotation layers distinct.

**Output:** an OCR/HTR validation sample, error audit, downstream comparison and corpus inclusion note.

### 10. Search, concordance and frequency

Read the opening of [Text analysis](../chapters/text-analysis.md). In a corpus interface or desktop tool, search a word, inspect concordance context, and compare token frequency with document frequency. Record corpus version, query, date, filters, and denominator. Treat frequency as a description that still requires interpretation.

**Output:** one query log, checked frequency table, and a bounded interpretive paragraph.

### 11. Places and maps

Read the introduction to [GIS and spatial humanities](../chapters/gis-spatial-humanities.md). Create a place table with source form, normalized name, source locator, coordinates, coordinate source, and uncertainty. Produce a basic map or inspect the table when mapping software is unavailable. Do not convert uncertain place references into false precision.

**Output:** a small place table, map or equivalent spatial check, and uncertainty note.

### 12. Generative AI with evidence

Read [AI, ethics and reproducibility](../chapters/ai-ethics-reproducibility.md). Ask an approved system to work only with supplied material, require passage identifiers, and verify every factual statement, quotation, locator, citation, and calculation. Record model, version or access date, prompt, supplied material, output, corrections, and any data that could not be shared.

**Output:** an AI-use statement and claim-level audit. If you do not use AI, submit a brief non-use statement; use is not required.

### 13. Rights, privacy, access, accessibility and responsible publication

Apply the [ethics checklist](../resources/ethics-checklist.md) to the dossier. Decide what may be submitted, shared with peers, made public, restricted, anonymized, generalized, or omitted. Verify licences for text, data, images, PDFs, software, and attachments. Check heading navigation, table headers, meaningful links, alternative text, contrast, and a non-visual account of every figure.

**Output:** a component-level rights, privacy, access, and accessibility register.

### 14. Reproducible scholarly dossier, versioning and peer review

Assemble the final dossier from the source, writing, citation, spreadsheet, validation, known-problem, and rights layers. Use [the revision workflow](../workflows/scholarly-writing/revise-claims-evidence-and-paragraphs.md) in substantive, structural, paragraph, sentence, and proofreading passes. Create a stable ZIP or dated snapshot and record the handbook and software guidance versions used.

Exchange dossiers. Without oral help, a peer should locate the sources, inspect five Zotero records and the citation-style audit, follow the raw-to-clean decision trail, manually verify one table or figure value, identify the main limitation, and return a structured review. Revise and log the response.

**Output:** the final dossier, stable snapshot, peer review, response, and closed revision log.

## Assessment model

A balanced model can combine:

- **weekly practice portfolio (30%)** — short writing, source, document, and data checks;
- **citation and evidence audit (20%)** — five-source citation-style audit plus one table/figure check;
- **scholarly dossier (40%)** — connected question, structured text, verified references, data transformation, interpretation, and documentation;
- **peer reproducibility review (10%)** — evidence-based inspection of another dossier.

Assessment rewards documented judgement, not merely successful clicking. Honest diagnosis of a method's failure may show more competence than polished but unverified output.

!!! important "Assessment and public publication are separate"
    Completing or exchanging the dossier does not authorize publication in the handbook or elsewhere. Public student work requires a separate choice, editorial review, attribution, rights clearance, and licence consent. Choosing assessment only must not affect the grade.

## Final dossier specification

Submit:

1. a focused question, intended audience, disciplinary genre, working claim, counterexample, and limitation;
2. a search/source-selection log and source-to-claim table;
3. a structured `.docx` or `.odt` using real heading styles, automatic contents, captions, and cross-references;
4. at least five verified Zotero records with metadata-correction notes;
5. active citations with appropriate locators and a generated, refreshed bibliography;
6. a short citation-style audit naming the authority/version, five varied test records, corrections, justified deviations, and unresolved cases;
7. one documented raw-to-clean spreadsheet transformation with raw file, cleaned output, data dictionary, and validation log;
8. one checked table or figure with a full caption naming source, unit, measure, denominator, missing-value rule, transformation, and manual check;
9. a 700–1,000 word interpretation that distinguishes description, evidence, interpretation, and recommendation;
10. a revision log and peer-review response;
11. an AI-use or non-use statement, plus ethics, rights, privacy, access, accessibility, and platform-limit notes;
12. a README and stable ZIP or dated snapshot that let a peer reproduce one result without WSL, Bash, Git, or Python.

## Course versioning

At the start of the semester, record the handbook release or commit used by the syllabus and publish a stable ZIP or snapshot of graded instructions. Corrections may be consulted in the living edition, but requirements should not shift silently during the course. Record the tested Word/LibreOffice, Zotero, and Excel platform; offer an equivalent route where institutional access differs.
