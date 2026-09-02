---
title: "How do I turn messy humanities notes into a reusable dataset?"
description: "Move from source-grounded notes to documented decisions, clean records and validation without erasing uncertainty."
category: "Data wrangling"
category_id: "data-wrangling"
difficulty: "beginner"
time: "60–90 min"
tags: [data modeling, metadata, messy data, provenance, validation]
---

# How do I turn messy humanities notes into a reusable dataset?

<div class="answer-meta" markdown>
<span>Data wrangling</span><span>beginner</span><span>60–90 min</span>
</div>

## What you are trying to do

You have archive notes, a bibliography, a genealogy, catalogue exports or field observations. You want a table that supports comparison without turning ambiguous evidence into tidy-looking fact.

This workflow uses a **source → raw note → decision → clean record → output → validation** chain. Each layer has a different purpose. You can complete it in Excel, LibreOffice Calc or another spreadsheet; programming is optional.

!!! quote "One-sentence version"
    Preserve what the source and provider say, record every interpretive decision separately, and test identifiers, counts and provenance before using the clean table.

## You need

- a research question and a sentence defining the unit of one row;
- your original notes or source export, plus locators back to the evidence;
- a spreadsheet application or CSV-capable editor;
- a statement about rights, privacy and redistribution; and
- optionally, the open [Archival Friction teaching packet](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction), especially `raw/messy-records.csv`.

Make a working copy. Do not edit the only copy of your notes or the packet's `source/` and `raw/` layers.

## Workflow

### 1. Define the question and the row

Write the question above the table. Then finish: “One row represents one …” A source document, person, event, statement and image caption are different units. If one caption names eight people, either keep the caption as the row and use a linked people table, or make one person-caption relation per row. Do not squeeze several kinds of entity into one cell.

Give every record a stable identifier that does not depend on a name you may later correct. Keep the source locator—page, folio, image region, shelfmark or URL—in its own field.

### 2. Freeze and describe the source layer

Preserve the received file or notes unchanged. Record repository, collection, creator, source identifier, access date, rights statement, file name and checksum when available. If you transcribed a value, distinguish it from provider metadata and later inference.

Stop if you cannot identify the source or determine whether your planned use is allowed. A clean table without source identity is not reusable evidence.

### 3. Make a raw working table

Copy the relevant values into `raw` without silently correcting spelling, dates or names. Useful columns include:

| Field | Purpose |
| --- | --- |
| `record_id` | stable identifier for the row |
| `source_locator` | exact route back to the document |
| `value_as_printed` | transcription of visible evidence |
| `provider_value` | catalogue or OCR value, if different |
| `normalized_value` | later research-ready form |
| `certainty` | exact, derived, approximate, unresolved or not applicable |
| `evidence_note` | reason and supporting location |
| `synthetic` | whether a teaching disturbance was deliberately added |

Use explicit status fields for unknown, illegible, not applicable and not yet checked. A blank alone cannot tell readers which one you mean. Do not use cell colour or comments as the only data carrier.

### 4. Inspect the first inadequate result

The first raw table is deliberately inadequate, not a failed final product. Filter and sort a copy to find missing identifiers, conflicting spellings, mixed date formats, repeated records, several values in one cell and implausible authority matches. Inspect the source for each candidate. A majority of catalogue records does not automatically outweigh the closest evidence.

Classify the problem before choosing an action: transcription error, provider difference, normalization, uncertain identification, exact file duplicate, repeated intellectual content, reprint, version or deliberately synthetic disturbance.

### 5. Separate automated actions from manual decisions

Automation may flag exact duplicate bytes, invalid formats, missing IDs and values outside a controlled list. It cannot decide whether a reprint matters, identify a person from resemblance or determine what an archive's silence means. Review each flag against the source. For every material change, add a decision row with:

```text
decision_id, record_id, field, raw_value, clean_value,
action, evidence, decision_by, decision_date, rule_version
```

Choose among actions such as `correct_from_facsimile`, `normalize_with_rule`, `retain_variant`, `leave_unresolved`, `link_authority`, `reject_authority_candidate` and `exclude_declared_synthetic_duplicate`. Do not resolve an identity because a search result seems plausible. Retain the printed form, candidate identifier, evidence and status separately.

If a date is derived from “last Sunday,” keep the printed expression, normalized value, precision or certainty, and derivation note. If only the year is supported, do not invent a month and day.

### 6. Build the clean layer and preserve unresolved cases

Create `cleaned/records.csv` from the raw table plus the decision log. Do not paste over raw values. Keep source wording where it is itself evidence, and place analytical categories in separate fields. When several source rows describe the same entity, use a relation table rather than deleting their distinct locators.

For exact duplicate rows, remove the declared extra row only after you can state why it is exact. When candidates differ, write a deterministic retain/exclude or priority rule before selecting one. A visible sort order is not such a rule. Preserve `duplicate_of`, `reprint_of` or `version_of` when repetition matters historically.

### 7. Produce a question-shaped output

Derive only the table or summary the research question needs: counts by record type, a list of unresolved identities, dates by certainty, or source coverage by page. Keep this output separate from the clean records. A chart or summary is an interpretation of selected fields, not a replacement for them.

In the packet, `output/record-summary.csv` counts the clean record types and uncertainty states. It should be regenerated when decisions change, not corrected by hand.

### 8. Validate the chain

Use a small validation sheet with expected and observed values. Check that:

- record IDs are unique in the clean table;
- every clean row has a source locator;
- every changed value has a decision row;
- accepted source records remain present unless a documented rule excludes one;
- synthetic rows are identified and absent from factual outputs;
- exact, derived, approximate and unresolved values remain distinguishable;
- output totals equal clean-table totals; and
- five sampled rows can be followed back through the decision log to the source.

Recheck retained identifiers and row counts after any duplicate operation. Save the validation result and date. “No errors appeared” is not a test result unless you name the tests.

## Output

Deliver an unchanged source or source reference, raw table, decision log, clean records, a question-shaped output, validation report and known-problems note. Include a small data dictionary defining each field and allowed status.

The workflow passes when another person can explain one row from source to output, reconstruct every material correction, reproduce the row counts, and identify what remains unresolved. The packet's checked result contains eight clean records; the ninth raw row is a separately declared synthetic duplicate.

## Effect on a scholarly claim

Compare one claim before and after cleaning. In the packet, the raw authority candidate could support the false claim that the photographed speaker has been identified. The decision log instead supports a narrower claim: the caption supplies the printed form “Mr. Meker,” while the person's authority identity remains unresolved.

## Check yourself

- Does one row represent the same kind of thing throughout the table?
- Can every transcription, provider value and inference be distinguished?
- Does every normalized value retain its source form and decision?
- Are identifiers stable even when names change?
- Did you verify retained IDs and counts after treating duplicates?
- Could a reader tell which unknowns are evidence rather than unfinished work?

## Common traps

- Correcting the only copy of the source or raw table.
- Treating a provider catalogue field as though it were printed on the object.
- Combining several people, dates or places in one cell.
- Accepting an authority match because it is familiar or highly ranked.
- Converting an approximate year into a falsely exact date.
- Letting a spreadsheet's visible sort determine which differing duplicate remains.
- Deleting repeated publication when circulation is part of the question.
- Hand-editing a summary after the clean table changes.

## Practice task

Open the packet's `raw/messy-records.csv` and the PDF. Without consulting `cleaned/` first, find the four declared synthetic disturbances, record a decision for each, and create a clean table. Compare your result with `cleaned/records.csv` and `cleaned/decisions.csv`. Explain why the tempting authority match for “Mr. Meker” remains unresolved and why the 1925 date on the riverbed image is approximate.

Then design a second schema in which one row represents a person rather than a captioned feature. State which questions become easier and which source relationships require an additional table.

## Related guidance

For the conceptual distinctions behind this procedure, see [Data, metadata and models](../../chapters/data-metadata-models.md) and [Research design](../../chapters/research-design.md). Continue with [reconciling conflicting metadata](reconcile-conflicting-metadata-without-erasing-uncertainty.md) when several sources disagree, or [importing and cleaning a small dataset in Excel](import-and-clean-a-small-dataset-in-excel.md) for interface-specific import checks.
