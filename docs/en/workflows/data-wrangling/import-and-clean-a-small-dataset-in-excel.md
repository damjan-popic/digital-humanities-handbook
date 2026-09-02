---
title: "How do I import and clean a small dataset in Excel?"
description: "Import CSV data with deliberate types, preserve identifiers, clean a copied layer, and document every change."
category: "Data wrangling"
category_id: "data-wrangling"
difficulty: "beginner"
time: "60–90 min"
tags: [excel, csv, data-types, tidy-data, validation, provenance]
---

# How do I import and clean a small dataset in Excel?

<div class="answer-meta" markdown>
<span>Data wrangling</span><span>beginner</span><span>60–90 min</span>
</div>

## What you are trying to do

How can you turn a small export or catalogue table into research data without silently changing identifiers, dates, decimals, or uncertainty? Excel displays a value after interpreting it. Double-clicking a CSV can accept system defaults before you inspect the delimiter, encoding, locale, and column types.

Preserve the raw file and create a documented cleaned layer. A research dataset uses rows as observational units and columns as variables; a decorative table designed for reading may merge cells, use colour as meaning, and place multiple facts in one cell, but it is not automatically reusable data.

## You need

- a small CSV or delimited text file and a clear definition of one row;
- the source's delimiter, encoding, decimal mark, date convention, missing-value codes, and rights conditions;
- desktop Excel with *Data → From Text/CSV* or the equivalent import interface;
- the [sample ZIP](../../../assets/downloads/scholarly-work-foundations-v1.zip), which includes raw, lookup, cleaned, workbook, output, validation, and known-problem layers.

## Workflow

1. **Copy and describe the raw source.** Keep `postcards-messy.csv` unchanged. Record creator, source, date received/accessed, licence or restriction, file checksum if available, delimiter, encoding, and known problems. Do not “fix” the only copy.

2. **Define the observational unit.** Write a sentence such as `One row represents one catalogue record for one postcard.` Give every variable one column and every observation one row. Put units in headers or a data dictionary, not mixed with values. Do not merge cells inside the data region.

3. **Import through the data interface.** Use *Data → From Text/CSV* (or *Get Data → Text/CSV*). Inspect the preview. Set the correct delimiter and file origin/encoding, normally UTF-8 for the sample. If decimal or date interpretation depends on locale, set or document the intended locale before loading. Prefer *Transform Data* when types need correction.

4. **Protect identifiers as text.** Set catalogue IDs, shelfmarks, postal codes, and long numeric-looking identifiers to Text before they are converted. Confirm that `00127` remains five characters and that values resembling dates or scientific notation remain literal when they are identifiers.

5. **Inspect dates and numbers as values, not appearances.** A displayed date can hide a different underlying date serial, and decimal commas may be split or read as text under another locale. Test a known row. Keep ambiguous source dates as text plus a normalized date and precision field rather than inventing a day.

6. **Load a working layer and make it an Excel table.** Keep a `Raw` sheet or external raw file read-only and perform corrections in `Cleaned`. Convert the cleaned region to a named Excel table with one header row. Use filters and freeze the header row. Do not use blank rows, subtotal lines, footnotes, or merged titles inside the table.

7. **Define missingness.** Decide how blank, unknown, not applicable, illegible, and not yet checked differ. Prefer a status field such as `date_status` over several undocumented symbols. Never replace all missing values with zero: zero is an observed value.

8. **Run cleaning checks.** Check duplicated stable IDs, leading/trailing and repeated whitespace, inconsistent categories such as `Photograph`, `photo`, and `foto`, mixed data types, impossible dates, and unexpected blanks. Preserve `source_value` where normalization changes meaning. Record each correction rule and affected row count.

9. **Constrain future entry.** Put approved categories in a separate lookup table and apply *Data Validation → List* to editable cells. Add an explicit error message. Validation reduces new variants; it does not correct existing values or prove the category is conceptually sound.

10. **Export deliberately.** Save the working workbook as `.xlsx` to preserve tables, types, formulas, validation, comments, and multiple sheets. Export a cleaned `.csv` only when a plain interoperable table is needed. CSV stores values, not multiple sheets, cell formatting, formulas as formulas, validation, charts, or a reliable type schema. State encoding, delimiter, line endings, and date format beside the export.

## Output

Produce an unchanged raw file, a cleaned table, a data dictionary, a transformation log, a validation report, and a known-problems note. The cleaned CSV should contain the same stable identifiers as the accepted raw observations unless a documented duplicate rule explains a difference.

The workflow passes when all sample IDs retain leading zeros, UTF-8 characters display correctly, every cleaned change has a rule, no merged cell occurs in the data table, and a manual comparison of five rows finds no silent type conversion.

## Check yourself

- Is one row one declared observational unit and one column one variable?
- Are identifiers stored as text even when they contain only digits?
- Can you distinguish blank, unknown, and not applicable?
- Are normalized values traceable to source values?
- Does the exported CSV document what it cannot preserve?

## Common traps

- Double-clicking a CSV and saving after silent date or identifier conversion.
- Formatting an identifier with leading zeros after its original digits were already lost.
- Using colour, comments, or merged cells as the only data encoding.
- Correcting the raw layer or deleting a suspicious row without a reason.
- Assuming data validation fixes existing categories.
- Treating CSV as a complete workbook archive.

## Sources and interface status

Sources checked **2 September 2026**: Microsoft Support on [importing or exporting text/CSV files](https://support.microsoft.com/en-us/excel/get-started/import-or-export-text-txt-or-csv-files), the [Text Import Wizard](https://support.microsoft.com/en-us/excel/text-import-wizard), [importing data with Power Query](https://support.microsoft.com/en-us/excel/import-data-from-data-sources-power-query), [Excel tables](https://support.microsoft.com/en-us/office/overview-of-excel-tables), [data validation](https://support.microsoft.com/en-us/office/apply-data-validation-to-cells), and [data import and analysis options](https://support.microsoft.com/en-us/excel/data-import-and-analysis-options-in-excel). Import labels and automatic-conversion controls differ across Windows, macOS, web, subscription, and perpetual releases.

## Practice task

Import the raw sample without double-clicking. Preserve the IDs, normalize the documented categories in a copied layer, define missingness, apply one validation list, export a cleaned CSV, and compare five rows with the raw text in a plain-text viewer.
