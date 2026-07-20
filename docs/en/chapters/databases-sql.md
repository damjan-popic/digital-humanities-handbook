---
title: "Databases and SQL"
description: "How relational modelling turns people, texts, places and events into queryable humanities data without erasing uncertainty."
tags: [database, SQL, relational-model, identifiers, provenance]
status: draft
---

# Databases and SQL

## Learning outcomes

After this chapter, you should be able to:

- distinguish a spreadsheet from a relational database;
- identify entities, attributes, relationships, keys and cardinalities;
- design a normalized schema for a small humanities project;
- write basic SQL queries that filter, join, group and count records;
- represent uncertainty, provenance and changing interpretations explicitly.

## Before you begin

Imagine a table with columns `author_1`, `author_2`, `author_3`, `place_1`, `place_2` and several cells containing comma-separated names. It may look convenient, but how would you reliably ask which authors published in the same place, or correct one person's name everywhere? The structure determines which questions remain possible.

## A database is an argument about the world

A database does more than store facts. Its schema states what kinds of things exist in the project and how they relate. For a literary history project, we might model people, works, editions, publishers, places and events. Choosing *work* and *edition* as separate entities is already an interpretive decision.

Relational modelling asks:

- What is one identifiable thing?
- Which properties belong to it?
- Can one thing have many values of this property?
- Which relationships connect entities?
- What evidence supports each assertion?

The schema should follow research needs while remaining explicit enough to revise.

## Tables, rows, columns and keys

A relational database stores records in tables:

- a **row** represents one record;
- a **column** represents one defined attribute;
- a **primary key** uniquely identifies a row;
- a **foreign key** refers to a row in another table.

Use stable internal identifiers rather than names as keys. Names change, collide and vary in spelling. `person_id = 1042` can remain stable while the database stores several name forms and their sources.

## Relationships and cardinality

Common relationships include:

- one-to-many: one newspaper has many issues;
- many-to-many: many people contribute to many works;
- one-to-one: rare and often a sign that two tables could be combined.

A many-to-many relationship needs a junction table. Instead of columns `author_1`, `author_2` and `author_3`, use a `contribution` table with `person_id`, `work_id`, role, order and evidence. The relationship itself can then carry historically meaningful information.

## Normalization without dogma

Normalization reduces duplication and contradictory updates. A useful basic rule is: one cell, one value; one table, one kind of entity; each fact stored in the place where it belongs.

Do not repeat a publisher address in every edition row. Store the publisher once and link editions to it. Do not store a person's birth year both in the person table and every authorship record.

Yet humanities data are not always tidy. An uncertain date such as “between 1848 and 1851” should not be forced into one exact year. Model earliest date, latest date, display text and certainty separately, or create a date assertion table with evidence.

## Provenance and assertions

A value may be quoted from an archive, inferred by an editor, imported from Wikidata or proposed by a student. Store provenance at the level required by the claim.

For contested information, model **assertions** rather than overwriting one value:

| assertion_id | subject | property | value | source | certainty | contributor |
|---:|---|---|---|---|---|---|
| 81 | person_1042 | birth_place | place_17 | archive_A_52 | probable | dp |

This makes disagreement queryable and preserves the history of editorial decisions.

## SQL as a research language

Structured Query Language expresses questions about tables. A few core patterns go far:

```sql
SELECT title, year
FROM work
WHERE year BETWEEN 1900 AND 1918
ORDER BY year;
```

A join follows relationships:

```sql
SELECT p.preferred_name, COUNT(*) AS works
FROM person AS p
JOIN contribution AS c ON c.person_id = p.person_id
WHERE c.role = 'author'
GROUP BY p.person_id
ORDER BY works DESC;
```

Queries should be saved as project files, not reconstructed manually for each publication. A query is part of the analytical method.

## Integrity and validation

Databases can enforce useful constraints:

- keys must be unique;
- required fields cannot be empty;
- foreign keys must point to existing records;
- categories can be restricted to controlled values;
- dates or numerical ranges can be checked.

Constraints prevent accidental inconsistency, but they cannot decide whether the underlying historical claim is correct. Validation also requires source review, duplicate detection, authority control and documented editorial policy.

## SQLite for small humanities projects

SQLite stores a complete relational database in one portable file and supports standard SQL without a server. It is an excellent step beyond spreadsheets for teaching, prototypes and many research datasets.

Keep alongside it:

- a schema file that can recreate the database;
- import scripts or documented procedures;
- controlled vocabularies;
- data dictionaries and field definitions;
- saved analytical queries;
- versioned exports in open formats such as CSV.

The database file is convenient; the documented process is what makes it reproducible.

## Worked example: correspondence network

To study correspondence, create tables for persons, letters, places and participation. A letter has a date, repository identifier and perhaps uncertainty. A participation table links a person to a letter with a role such as sender, recipient, mentioned person or editor. A place link can specify origin, destination or place mentioned.

This structure supports questions about exchange, mobility and mediation without collapsing every relationship into a single edge. It also makes explicit which relationships come from document metadata and which are extracted from letter text.

## Practice

Design a schema for one project: a bibliography, oral-history archive, literary corpus, cultural-heritage inventory or correspondence collection. Draw entities and relationships, assign keys, identify one many-to-many relationship and show how uncertainty and provenance will be recorded.

## Reflection

- Which categories in your schema are analytical interpretations rather than source facts?
- What information would be lost by exporting the database to one flat table?
- Which query would reveal the strongest weakness in your data coverage?

## Summary

A relational database is a formal, revisable model of entities and relationships. Keys and normalized tables reduce ambiguity; junction tables express many-to-many relations; SQL makes analytical steps explicit. Humanities databases become trustworthy when they also preserve uncertainty, provenance, contested assertions, editorial rules and recreatable structure.
