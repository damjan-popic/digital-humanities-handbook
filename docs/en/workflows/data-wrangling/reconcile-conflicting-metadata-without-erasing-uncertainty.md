---
title: "How do I reconcile conflicting metadata without erasing uncertainty?"
description: "Compare source statements, provider records and authority candidates, then preserve evidence and a documented decision."
category: "Data wrangling"
category_id: "data-wrangling"
difficulty: "beginner"
time: "60–90 min"
tags: [metadata, provenance, authority control, uncertainty, reconciliation]
---

# How do I reconcile conflicting metadata without erasing uncertainty?

<div class="answer-meta" markdown>
<span>Data wrangling</span><span>beginner</span><span>60–90 min</span>
</div>

## What you are trying to do

A printed caption, repository catalogue, OCR text and authority file disagree about a name or date. The first provider-only result is inadequate: selecting its value, or the neatest alternative, would hide what the evidence actually supports.

Reconciliation is not majority voting. It is a documented comparison of claims made by sources with different purposes, proximity and authority. Your clean record should preserve the source forms, state the normalized value only as precisely as warranted, and leave an identity unresolved when the evidence is insufficient.

## You need

- the original item or faithful image and a precise locator;
- every provider record or export you intend to compare;
- stable links to any authority records consulted;
- a spreadsheet or text editor; and
- optionally, download the [Archival Friction teaching packet ZIP](../../../assets/downloads/archival-friction-v1.zip) and use `raw/messy-records.csv`, `reference/observations.csv` and `cleaned/decisions.csv`; maintainers can inspect the [packet source tree](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction).

Record source and rights information before beginning. Keep provider exports unchanged.

## Workflow

### 1. State what is in conflict

Give the record and field stable identifiers. Copy each value exactly and classify its source:

- visible evidence transcribed from the item;
- provider-supplied descriptive metadata;
- provider OCR or HTR;
- your derivation from another supported value;
- an external authority candidate; or
- a deliberately synthetic teaching disturbance.

Do not combine these into one “name” or “date” column. The same string can be a transcription in one source and an inferred identity in another.

### 2. Build an evidence matrix

Create one row per claim-source pair:

| Field | Example purpose |
| --- | --- |
| `claim_id` | stable identifier for this assertion |
| `record_id` | object or observation being described |
| `field` | name, date, place, title or relation |
| `value` | the exact claimed value |
| `source_type` | facsimile, catalogue, OCR, derivation, authority |
| `source_locator` | page, region, record URL or identifier |
| `accessed` | when a mutable record was checked |
| `evidence_scope` | what the source directly establishes |
| `notes` | ambiguity, damage, mismatch or caveat |

A facsimile may establish the spelling in print but not the person's modern authority identity. An authority file may establish an individual's dates but not prove that the image depicts that person. Evaluate scope, not prestige alone.

### 3. Test record identity before field values

Confirm that the compared records describe the same object, manifestation or person. Compare stable identifiers, title, issue, page, creator, date, physical description and source lineage. Similar names are not enough.

Classify relationships explicitly: `same_as` only when supported; `duplicate_of` for a duplicated record; `reprint_of` for repeated publication; `version_of` for a changed manifestation; and `possible_match` for an unconfirmed candidate. Keep the evidence for each relation.

### 4. Apply field-specific rules

Write the rule before choosing a value. Examples:

- **transcription:** prefer the visible form when legible; preserve unresolved characters rather than modernizing them;
- **provider metadata:** retain it as a provider claim even when the object contradicts it;
- **date:** retain the printed expression, define what the date describes, and distinguish exact, rule-derived, unknown and not-applicable values from a separate issue-context date;
- **person:** require corroborating place, role, event, date or relationship before linking an authority identifier;
- **title:** distinguish the title printed on the item from a repository-supplied title; and
- **language or genre:** state the vocabulary and whose classification it represents.

Do not use the number of agreeing sources as the rule unless their independence and relevance are established. Several catalogues may all copy one earlier error.

### 5. Record the decision without deleting alternatives

Add a decision row containing the record, field, raw value, accepted value, action, evidence, decision maker, date and rule version. Use a controlled action such as `correct_from_facsimile`, `retain_provider_variant`, `derive_date`, `accept_authority_match`, `reject_authority_match` or `leave_unresolved`.

For *Ilustrirani Slovenec*, the image prints “Mr. Meker.” One synthetic teaching change silently rewrites it as “Mr. Meeker”; another sets the tested Ezra Meeker authority candidate to `accepted`. Similarity of name, age and public role is insufficient evidence. The defensible clean record restores the printed form, models the unit as `one_person`, retains Ezra Meeker as an audited candidate, and assigns `candidate_rejected` rather than confusing a printed label with an external authority link.

### 6. Preserve precision, negative decisions and unresolved cases

Do not turn an issue date into a feature's creation date. Keep fields such as `date_scope`, `printed_date`, `date_normalized`, `date_status`, `issue_context_date` and the derivation evidence. In the packet the riverbed photograph remains blank/`unknown`; 1925-02-07 is publication context only. For an unsuccessful authority check, retain the rejected candidate and reason so someone does not repeat the same search without new evidence.

Use `unknown` when no value is known, `unresolved` when evidence conflicts, and `not_applicable` when the field does not describe that record. Empty strings alone erase those differences.

### 7. Run automated checks after manual reconciliation

Manual reconciliation determines evidential scope and identity. Automated checks can then confirm that every accepted value has evidence or an explicit rule; every correction has a decision; every authority identifier resolves; precision has not increased without justification; and unresolved candidates remain visible in the audit layer.

After treating duplicates, verify the exact identifiers retained and row counts before and after. Exact duplicate rows may be removed under a documented rule. If candidates differ, apply a deterministic priority or retain/exclude rule; do not trust their visible sort order.

## Output

Produce an evidence matrix, reconciled record table, relation table where needed, decision log and known-problems note. Include the rule version and access date for mutable catalogues and authority services.

Validation passes when another reader can recover every competing value, see why one was accepted or why none was, follow the source locator, and reproduce the final record count. A useful unresolved result is better than a confident false match.

## Check yourself

- Have you separated the printed form, provider claim, normalized value and authority identity?
- Does each source actually support the scope you assign to it?
- Could apparently independent records derive from the same catalogue?
- Have you retained rejected candidates and reasons?
- Did any normalized date become more precise than its evidence?
- Can you verify the retained identifiers and row counts?

## Common traps

- Choosing the most common spelling by vote.
- Treating OCR as the item's wording.
- Treating an authority candidate as a confirmed identity.
- Silently replacing a provider field instead of preserving both claims.
- Converting approximate or derived dates into false precision.
- Calling reprints duplicates and deleting evidence of circulation.
- Relying on current spreadsheet order to select among differing rows.

## Practice task

Use records `AF-P1-001`, `AF-P1-002`, `AF-P1-003`, `AF-P2-001` and `AF-P2-003` from the packet. For each one, separate the printed label, entity structure, provider value, date scope and status, external authority candidate, authority-link status and evidence. Write one decision row per conflict. Then compare your table with `cleaned/decisions.csv` and explain what evidence would be needed to replace the rejected authority candidate or date the riverbed photograph.

Continue with [turning messy notes into reusable data](turn-messy-humanities-notes-into-a-reusable-dataset.md) for the complete layered process. [Data, metadata and models](../../chapters/data-metadata-models.md) explains why these decisions are acts of modelling rather than neutral cleanup.
