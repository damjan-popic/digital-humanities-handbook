---
title: "Data, metadata and models"
description: "How humanities materials become structured data without losing provenance, uncertainty and context."
tags: [data, metadata, modelling, provenance]
status: draft
---

# Data, metadata and models

## Learning outcomes

After this chapter, you should be able to:

- distinguish data, metadata and documentation;
- design stable identifiers and a simple tabular data model;
- represent provenance, uncertainty and missingness explicitly;
- recognize when a spreadsheet should become a relational database;
- evaluate whether a schema reflects the research question or merely the available source format.

## Before you begin

Open a table you have used for research. Can you tell, without asking its creator, what one row represents, which columns are required, what blank cells mean, where the values came from and which version you are looking at? If not, the problem is not “messy data” alone; it is missing semantics.

## Data, metadata and documentation

In humanities research, **data** are recorded observations or representations used as evidence. **Metadata** describe the objects, records or processes: title, date, creator, source, language, rights, collection, coordinates, transcription status or annotation version. **Documentation** explains how the data and metadata were produced and how they should be interpreted.

The distinction depends on the question. A publication date may be metadata in a corpus search but become analysed data in a study of publishing history.

A robust project keeps all three layers:

- the source or a stable reference to it;
- structured records used in analysis;
- documentation of transformations and decisions.

## What does one row mean?

The most important table-design question is the **observation unit**. One row should represent one clearly defined thing: one document, person, place, event, sentence, annotation or relationship.

Mixing levels creates errors. A table with one row per author but multiple book titles squeezed into cells cannot answer book-level questions reliably. A table with one row per newspaper issue but article-level topics in comma-separated lists cannot be filtered or counted without ambiguity.

A useful test is to complete the sentence:

> Each row represents exactly one ________.

If several answers are possible, split the data into related tables.

## Identifiers before names

Names are labels, not stable identifiers. People change names; places have historical and multilingual variants; titles are repeated; spelling varies. Assign each entity a stable internal ID such as `person_0042` or `place_0187`, and store names as attributes or aliases.

Identifiers should be:

- unique within the project;
- persistent across revisions;
- free of sensitive meaning where possible;
- never silently recycled;
- mapped to external identifiers such as Wikidata, VIAF or GeoNames when appropriate, without treating external reconciliation as infallible.

## Missing, unknown and not applicable

A blank cell is dangerously ambiguous. It might mean:

- the value is unknown;
- the value was not recorded;
- the field does not apply;
- the source is illegible;
- the value is being withheld;
- the work has not yet been completed.

Choose an explicit policy. In analysis tables, a machine-readable missing value may be appropriate, but preserve a separate status or note when different forms of uncertainty matter historically.

Do not replace unknown values with zero unless zero is a real observed value. “No recorded letters” is not the same as “zero letters were written.”

## Controlled vocabularies and open text

Controlled vocabularies make comparison possible: `novel`, `poetry`, `essay` rather than dozens of spelling variants. But fixed categories can erase ambiguity and impose modern distinctions.

A practical pattern is to keep:

- a controlled field for analysis;
- the original source wording;
- a note or confidence field;
- a vocabulary document defining each category and its revisions.

Categories should be few enough to use consistently and rich enough to support the research question. “Other” is often necessary, but it should be inspected rather than treated as a bin for discomfort.

## Provenance and transformation

Every derived value should be traceable. Record at least:

- source identifier and location;
- date of acquisition;
- method or script used;
- software/model version where relevant;
- person or process responsible;
- manual corrections;
- relationship between raw, cleaned and analysed files.

A common folder structure separates `data/raw`, `data/interim`, `data/processed` and `output`. Raw data should be read-only whenever possible. Corrections belong in a documented transformation or correction table, not in silent overwriting.

## When a spreadsheet stops being enough

A spreadsheet is excellent for inspection and small flat datasets. Consider a relational database when:

- one person has many works and one work has many persons;
- records need stable relationships across tables;
- repeated text values create inconsistency;
- several people edit or query the data;
- integrity rules matter;
- the project needs reusable queries.

The decision is not about prestige. A database is useful when relationships and constraints are part of the evidence.

## Worked example: correspondence data

A correspondence project might use four tables:

- `persons(person_id, preferred_name, birth_year, ...)`
- `letters(letter_id, date_text, date_start, date_end, source_id, ...)`
- `letter_participants(letter_id, person_id, role)`
- `places(place_id, preferred_name, latitude, longitude, ...)`

The participant table allows several senders, recipients, copied persons or uncertain roles without adding columns such as `recipient_2` and `recipient_3`. The date is represented both as the original string and as a computable interval, preserving uncertainty such as “spring 1898.”

## Practice

Take a small humanities collection and create:

1. a data dictionary with field name, definition, type, allowed values and missing-value policy;
2. five example records;
3. a provenance note explaining one transformation;
4. a list of entities that need stable identifiers.

## Reflection

- Which categories come from the historical source, and which come from your research design?
- Could another researcher reconstruct a derived value from your records?
- What does a blank cell mean in each field?

## Summary

Data structure is interpretation made operational. Clear observation units, stable identifiers, explicit missingness, documented vocabularies and provenance make analysis possible without pretending that cultural evidence is cleaner or more certain than it is. Use a database when relationships and constraints matter, not simply because the dataset is “serious.”
