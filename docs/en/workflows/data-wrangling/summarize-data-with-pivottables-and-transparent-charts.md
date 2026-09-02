---
title: "How do I summarize data with PivotTables and transparent charts?"
description: "Answer a bounded question with a checked PivotTable and one restrained chart whose source, unit, denominator, and missing values are explicit."
category: "Data wrangling"
category_id: "data-wrangling"
difficulty: "beginner"
time: "60–90 min"
tags: [excel, pivottable, chart, denominator, validation]
---

# How do I summarize data with PivotTables and transparent charts?

<div class="answer-meta" markdown>
<span>Data wrangling</span><span>beginner</span><span>60–90 min</span>
</div>

## What you are trying to do

How are catalogue records distributed across documented categories, and what can that distribution support? A PivotTable answers a specified aggregation question. A chart presents selected values. Neither chooses a valid denominator nor interprets the historical meaning for you.

Begin from tidy, checked data: one row per observational unit, one variable per column, stable identifiers, explicit missingness, and no merged cells inside the table.

## You need

- a cleaned Excel table and its data dictionary;
- a written question naming the population, grouping variable, measure, and exclusions;
- the raw-to-clean log and known missing categories;
- the [sample ZIP](../../../assets/downloads/scholarly-work-foundations-v1.zip), whose workbook, pivot summary, chart data, and manual checks form one inspectable chain.

## Workflow

1. **Write the aggregation question.** Distinguish `How many rows?`, `What is the sum of a numeric measure?`, `What is the average among non-missing observations?`, and `How many distinct documents?` A repeated document can make row count differ from distinct-document count.

2. **Choose the denominator and missing rule.** State whether the population is all imported rows, accepted cleaned records, records with known dates, or another subset. Decide whether `unknown` appears as a visible category, is excluded from a percentage with a note, or belongs in the denominator. Do not let the PivotTable's default blank handling decide silently.

3. **Insert the PivotTable.** Select a cell in the named cleaned table and use *Insert → PivotTable*. Confirm the table/range and place the result on a new `Pivot Check` sheet. Keep the source table unchanged.

4. **Assign fields deliberately.** Put the grouping field in *Rows* and the measure in *Values*. Open *Value Field Settings* and choose Count, Sum, or Average according to the written question. For distinct-document counts, use *Distinct Count* when the Excel version and Data Model support it; otherwise make a deduplicated check table and document the fallback.

5. **Expose missing categories.** Inspect filters and row labels. Confirm that blanks, unknowns, and not-applicable values are treated according to the rule. Show counts alongside percentages when a small denominator could mislead.

6. **Refresh after source changes.** If the source is an Excel table or query result, use *Refresh* after an added row or query update. Confirm the PivotTable source still covers the intended data and that filters did not preserve an obsolete category state.

7. **Perform a manual subset check.** Select a small category with five or fewer source rows. Filter the source table, list the included IDs, and manually count or calculate the measure. Compare the result with the PivotTable. Record pass/fail and resolve any difference before charting.

8. **Prepare a chart-source table.** Copy or link only the categories and checked values required for the stated message. Keep the helper table traceable to the PivotTable or source. Do not paste unexplained values into a disconnected chart.

9. **Choose one restrained chart.** A sorted bar or column chart suits a small category comparison; a line chart suits an ordered time series. Avoid 3-D effects, gradients, decorative icons, and colour that has no meaning. A table may be clearer when exact values are the main point.

10. **Label the evidence.** Give the chart a descriptive title and visible units. Add axis titles only where needed. Beneath it, write a full caption with source file/version, observational unit, measure, denominator, exclusions, missing-value rule, transformation reference, and manual-check result. Provide meaningful alternative text and do not encode categories by colour alone.

11. **Write interpretation separately.** First describe what the checked chart shows. Then identify the evidence and choices that produce it. Only then offer an interpretation and limitation. A polished chart is not an interpretation, and an association among catalogue categories does not prove a historical cause.

## Output

Produce one refreshed PivotTable, a manual subset check, a linked chart-source table, one restrained chart, complete caption and alternative text, and a paragraph separating description, evidence, interpretation, and limitation.

The workflow passes when the chosen aggregation answers the written question, the denominator and missing rule are explicit, a manual subset matches the PivotTable, and every plotted value traces to the cleaned table.

## Check yourself

- Is the Values field using Count, Sum, Average, or Distinct Count for a stated reason?
- Can you name the denominator and all exclusions?
- Did refresh change the expected controlled row?
- Does the manual subset reproduce the PivotTable result?
- Does the caption allow a reader to identify source, unit, measure, and missingness?
- Is the interpretive claim weaker than or equal to what the evidence supports?

## Common traps

- Reporting a row count as a count of unique documents.
- Averaging a field without inspecting missing and non-numeric values.
- Leaving blanks hidden by PivotTable defaults.
- Editing a PivotTable result instead of correcting and refreshing the source.
- Using a chart title as the only source or unit note.
- Treating visual polish, correlation, or a large bar as a historical explanation.

## Sources and interface status

Sources checked **2 September 2026**: Microsoft Support on [creating a PivotTable](https://support.microsoft.com/en-us/excel/get-started/create-a-pivottable-to-analyze-worksheet-data), [refreshing PivotTable data](https://support.microsoft.com/en-us/office/refresh-pivottable-data), [creating charts](https://support.microsoft.com/en-us/excel/get-started/create-a-chart-from-start-to-finish), [chart and axis titles](https://support.microsoft.com/en-us/office/excelexp/add-or-remove-titles-in-a-chart), and [accessible Excel workbooks](https://support.microsoft.com/en-us/accessibility/excel/make-your-excel-documents-accessible-to-people-with-disabilities). PivotTable interfaces, Distinct Count availability, and chart controls differ by platform and release.

## Practice task

Create a category count from the sample cleaned table, show the unknown category, manually check one category, refresh after the supplied row is added, and create one chart with a caption that names the denominator and missing-value rule.
