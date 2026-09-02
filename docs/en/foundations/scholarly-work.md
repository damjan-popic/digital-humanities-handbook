---
title: "Scholarly work: writing, references, documents, and spreadsheets"
description: "A low-threshold route from a research question to a structured, cited, checked, and revisable scholarly dossier."
---

# Scholarly work: writing, references, documents, and spreadsheets

## The research problem

How can a reader tell where a scholarly claim came from, how a table was changed, and whether a document will remain coherent after revision? A polished submission is not enough. Scholarly work must connect questions to evidence and preserve the links among sources, notes, citations, document structure, data transformations, figures, and interpretation.

This route follows one connected cycle:

```text
question → search → source record → reading note → claim → citation → structured document
         → small dataset → checked table/figure → interpretation → revision → submission
```

The arrows are not a command to work only from left to right. A counterexample may change the claim; a metadata error may change a citation; a denominator check may require a new table; revision may narrow the question. The cycle is inspectable when each change leaves evidence.

## Learning outcomes

After completing the route, you should be able to:

- turn a research question into a section-level argument plan and a source-to-claim table;
- structure and revise a scholarly text without treating one genre as universal;
- build and quality-check a small Zotero library;
- identify the required citation system and guidelines, select the corresponding citation style, insert citations with locators, and audit the generated output;
- use real heading styles, captions, cross-references, fields, comments, and tracked changes;
- import, clean, and summarize a small Excel dataset without silently changing identifiers or types;
- distinguish a repeatable transformation from an undocumented edit;
- connect every table or figure to a source, unit, denominator, check, and interpretive claim.

## What the objects are

| Object | What it records | What it is not |
| --- | --- | --- |
| **Source** | The text, object, recording, dataset, software, archival unit, or other evidence used in research. | The metadata row that describes it. |
| **Bibliographic record** | Structured metadata about a source: creators, title, container, date, identifiers, and other fields. | Proof that the imported metadata are correct. |
| **Attachment** | A PDF, snapshot, image, or other file attached to a Zotero item. | The bibliographic item itself or permission to redistribute the file. |
| **Reading note** | Your traceable record of a source passage, locator, paraphrase, question, and possible use. | A citation or a copy of prose ready to paste. |
| **Citation** | A formatted pointer in the text, a note, or an endnote that connects a claim to a source record. | A complete bibliography entry in every citation system. |
| **Bibliography** | A formatted list produced with a defined citation style under the governing citation guidelines. | A substitute for checking individual claims and locators. |
| **Stable identifier** | A managed identifier such as a DOI, ISBN, Handle, ARK, or archival signature. | Any URL copied from a browser address bar. |

## From a question to a document

A **research question** defines the uncertainty you will investigate. A **working claim** is a provisional answer that can change. **Evidence** is the source material or observation offered in support; **interpretation** is the reasoning that explains why it supports, complicates, or limits the claim. A **paragraph** develops one local move in that reasoning. A **section** coordinates several moves for a larger purpose. The document structure should therefore expose the argument, not merely divide a word count.

Use **styles** to mark structural roles such as Heading 1, Heading 2, body text, and caption. Direct formatting—selecting a line and making it bold and large—changes appearance without reliably identifying its role. A real **caption** is a numbered field attached to a table or figure, not a typed label such as “Figure 3.” A **cross-reference** points to that field and can update after material moves; copied text cannot.

## From a table to evidence

A spreadsheet cell has both an **underlying value** and a **display**. The display `01/02/03` might conceal a date interpretation, while `00127` may have been converted from an identifier to the number `127`. Inspect types and values before formatting.

A **one-off edit** changes a cell with no reusable record. A **documented transformation** states the source, operation, reason, and result and can be repeated after the source changes. A **research dataset** has a defined observational unit, variables, provenance, missing-value rules, and checks. A decorative table arranged for presentation may be useful, but it is not automatically a research dataset.

## The complete route

### Plan and revise the argument

1. [Turn a research question into a scholarly paper plan](../workflows/scholarly-writing/turn-a-research-question-into-a-scientific-paper-plan.md).
2. [Structure a long document with styles, captions, and cross-references](../workflows/scholarly-writing/structure-a-long-document-with-styles-captions-and-cross-references.md).
3. [Revise claims, evidence, and paragraphs](../workflows/scholarly-writing/revise-claims-evidence-and-paragraphs.md).

### Manage and cite sources

4. [Build and clean a Zotero library](../workflows/reference-management/build-and-clean-a-zotero-library.md).
5. [Choose, apply, and audit a citation style](../workflows/reference-management/choose-apply-and-audit-a-citation-style.md).
6. [Cite with Zotero in Word or LibreOffice](../workflows/reference-management/cite-with-zotero-in-word-or-libreoffice.md).

### Clean, transform, and present small data

7. [Import and clean a small dataset in Excel](../workflows/data-wrangling/import-and-clean-a-small-dataset-in-excel.md).
8. [Make repeatable transformations with Excel Power Query](../workflows/data-wrangling/make-repeatable-transformations-with-excel-power-query.md).
9. [Summarize data with PivotTables and transparent charts](../workflows/data-wrangling/summarize-data-with-pivottables-and-transparent-charts.md).

Download the [version 1 scholarly-work sample ZIP](../../assets/downloads/scholarly-work-foundations-v1.zip). It contains original or bibliographic-fact-only teaching material organized into source, raw, cleaned, output, validation, known-problem, and citation-audit layers. Its `RIGHTS.md` records provenance and reuse conditions.

## A low technical threshold

No WSL, Bash, Git or Python is required to pass this route or the Information Society Literacy course. Work can be completed with Zotero, Word or LibreOffice Writer, and Excel. A stable ZIP or dated snapshot is acceptable when version control is not taught, provided that the README identifies the version and the raw material remains unchanged.

The [technical workspace route](technical-workspace.md) is an optional extension for students who want command-line, Git, or Python practice. It is not a hidden prerequisite for scholarly writing, reference management, or spreadsheet assessment.

## Submission check

Before submission, make a backed-up delivery copy and verify:

- the question, intended audience, genre, working claim, limitation, and section purposes are explicit;
- every quotation matches the source and has an appropriate locator;
- Zotero metadata were corrected in the library and refreshed in the document;
- the required citation-style version and any justified local deviations are recorded;
- real headings generate the contents page, and captions and cross-references update;
- raw data remain unchanged and cleaning steps are documented;
- the table or figure states its source, unit, denominator, missing-value rule, and check;
- comments and tracked changes have been reviewed rather than blindly accepted;
- AI assistance, if any, is disclosed and its outputs are verified;
- rights, privacy, accessibility, and platform limitations are stated.

Always keep the working document with active Zotero fields as the master. Follow the venue or publisher's delivery requirements. When preparing a static final submission, use Zotero's irreversible **Unlink Citations** command only in a separately named and backed-up delivery copy. Never unlink the working master merely to repair formatting.

## Interface and source boundary

Software interfaces are mutable. The workflows name the conceptual operation first and then give recognizable labels for current desktop interfaces. Labels may differ by operating system, subscription, language pack, or release. The source audit was checked on **2 September 2026** against current official Zotero, Microsoft Support, and LibreOffice Help pages; live behaviour on every Office, LibreOffice, and Zotero platform was not claimed.

The writing route also draws on the Harvard College Writing Center's guidance on [theses](https://writingcenter.fas.harvard.edu/thesis), [organizing an essay](https://writingcenter.fas.harvard.edu/tips-organizing-your-essay), [body paragraphs](https://writingcenter.fas.harvard.edu/anatomy-body-paragraph), and [counterargument](https://writingcenter.fas.harvard.edu/counterargument), and on Eric Hayot's *[The Elements of Academic Style: Writing for the Humanities](https://cup.columbia.edu/book/the-elements-of-academic-style/9780231537414/)*. These sources support planning and revision without treating IMRaD or the five-paragraph essay as a universal humanities form.
