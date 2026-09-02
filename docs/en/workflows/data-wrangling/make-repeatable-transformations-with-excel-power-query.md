---
title: "How do I make repeatable transformations with Excel Power Query?"
description: "Record a small raw-to-clean pipeline in Power Query, refresh it after source changes, and diagnose a broken Applied Step."
category: "Data wrangling"
category_id: "data-wrangling"
difficulty: "beginner"
time: "60–90 min"
tags: [excel, power-query, transformation, refresh, provenance]
---

# How do I make repeatable transformations with Excel Power Query?

<div class="answer-meta" markdown>
<span>Data wrangling</span><span>beginner</span><span>60–90 min</span>
</div>

## What you are trying to do

How can you repeat the same cleaning decisions when a source file changes? Repeated cell editing records the final state but not the procedure. Power Query stores ordered transformation steps and reruns them on refresh while leaving the source file unchanged.

Keep three layers distinct: the **source** file, the **query** that records operations, and the **loaded result** placed in Excel. The result is not a second raw source, and typing into it is not a reliable way to change the query.

## You need

- one small CSV or workbook and a separate place-name lookup table;
- a written data dictionary and duplicate rule;
- an Excel version that exposes Power Query/*Get & Transform* for the required connectors;
- the [sample ZIP](../../../assets/downloads/scholarly-work-foundations-v1.zip). Its workbook shows the intended layers and step log, while the exercise asks you to create the live query on your platform.

## Workflow

1. **Record the source boundary.** Copy the raw files to a stable exercise folder and do not edit them during the query. Note the file names, encoding, delimiter, locale, and source rights. A moved or renamed source can break the first query step.

2. **Connect rather than open.** Use *Data → Get Data → From File → From Text/CSV* or *From Workbook*. In the preview, confirm the file origin and delimiter, then choose *Transform Data* to open Power Query Editor. Name the query `Postcards_Clean`.

3. **Inspect Applied Steps.** Identify *Source*, *Navigation* when present, and automatically inserted *Promoted Headers* or *Changed Type*. Delete or revise an automatic step if it interpreted identifiers or dates incorrectly. Each later step depends on the state produced before it.

4. **Rename columns and set types.** Use stable, concise names. Set `record_id` to Text before any numeric conversion; set normalized dates to Date only after locale and ambiguity are resolved; set actual measurements to suitable numeric types. Renaming in Power Query does not rename the source column.

5. **Clean text visibly.** Select relevant text columns and apply *Format → Trim* to remove leading/trailing whitespace and *Clean* to remove non-printing characters. These do not resolve spelling variants or conceptual categories; record separate replacement rules for those.

6. **Split only with a stated rule.** Split a compound column by a delimiter or fixed position only if the delimiter is structurally reliable. Preserve the original column until the split passes a manual check. Count rows before and after to detect accidental expansion or loss.

7. **Filter and replace with reasons.** Filter rows only according to an inclusion rule, such as excluding a documented test row. Replace values through a small mapping, not ad hoc memory. Record `foto → photograph` as a terminology decision, including affected row count and whether case matters.

8. **Merge the lookup table.** Import `place-lookup.csv` as a separate query. Use *Merge Queries* on the exact source key, inspect match rates, and expand only needed normalized fields. Keep unmatched values visible for review; do not let a fuzzy or many-to-many join silently multiply rows.

9. **Remove only justified duplicates.** Define the key and rationale before *Remove Duplicates*. Sort order can affect which row is retained, so first decide which record should survive and whether two similar records are actually editions, versions, or separate observations. Compare row counts and IDs before and after.

10. **Load the result separately.** Use *Close & Load To* and load as a table on a named `Query Result` sheet or as a connection when appropriate. Do not overwrite the raw source. Add a README or workbook sheet that translates each Applied Step into a research reason.

11. **Refresh after a controlled change.** Add the supplied new row to a copy of the source, then use *Data → Refresh All*. Confirm that the row passes through each rule, the lookup merge behaves as expected, and row-count checks update. Refresh reruns the query; it does not validate the interpretation.

12. **Diagnose a broken step.** Rename a source column in a disposable copy and refresh. In Power Query Editor, click Applied Steps from top to bottom to locate the first error. Repair that step only after deciding whether the source schema legitimately changed. Check all later steps because column references can cascade.

## Platform fallback exercise

Power Query availability, connectors, authoring, and refresh differ across Windows, macOS, Excel for the web, licence, and release. If your assigned platform cannot author the query, complete the same research decisions in a copied `Cleaned` sheet and maintain a numbered transformation log with input count, operation, column, rule, output count, and manual check. Then exchange files with a classmate or instructor who can run the live query. The fallback meets the low-threshold learning outcome when it documents a genuinely repeatable procedure; it does not claim that manual edits are Power Query.

## Output

Produce the unchanged source, lookup table, workbook with `Query Result`, exported cleaned CSV, Applied Steps inventory, refresh test, row-count reconciliation, and one broken-step diagnosis.

The workflow passes when refresh after an added source row reproduces all documented transformations, identifiers remain text, the merge does not multiply observations, duplicate removal matches the written rule, and the first broken step can be identified.

## Check yourself

- Can you point separately to source, query, and loaded result?
- Does every Applied Step have a research reason, not merely a button name?
- Do row counts reconcile after filters, joins, and duplicate removal?
- Does refresh incorporate a new source row without hand editing the result?
- Can an unmatched lookup value remain visible rather than being forced?

## Common traps

- Accepting an automatic *Changed Type* step that strips leading zeros.
- Editing the loaded result and expecting the change to survive refresh.
- Replacing categories without a mapping or case rule.
- Merging on non-unique keys and multiplying rows.
- Removing duplicates without defining which record is retained.
- Repairing the last error instead of locating the first broken dependency.

## Sources and interface status

Sources checked **2 September 2026**: Microsoft Support on [Power Query in Excel](https://support.microsoft.com/en-us/excel/about-power-query-in-excel), [creating, loading, or editing a query](https://support.microsoft.com/en-us/excel/create-load-or-edit-a-query-in-excel-power-query), [importing data sources](https://support.microsoft.com/en-us/excel/import-data-from-data-sources-power-query), [renaming columns and diagnosing later steps](https://support.microsoft.com/en-us/excel/rename-a-column-power-query), [merging queries](https://support.microsoft.com/en-us/office/merge-queries-power-query), and [Power Query availability by Excel version](https://support.microsoft.com/en-us/office/power-query-data-sources-in-excel-versions). Verify the current feature matrix for your platform before assessment.

## Practice task

Build the sample query, refresh it after adding the supplied row, then break a source column name in a disposable copy. Record the first failing step, repair it, and reconcile input, unmatched, duplicate, excluded, and output counts.
