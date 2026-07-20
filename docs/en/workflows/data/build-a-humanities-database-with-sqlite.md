---
title: "How do I build a small humanities database with SQLite?"
description: "Turn people, works and contributions into linked tables with keys, provenance and saved research queries."
category: "Data"
difficulty: "intermediate"
time: "90–180 min"
tags: [SQLite, SQL, database, provenance]
---

# How do I build a small humanities database with SQLite?

<div class="answer-meta" markdown>
<span>Data</span><span>intermediate</span><span>90–180 min</span>
</div>

## What you are trying to do

You have repeated people, works and roles in a spreadsheet and need a structure that supports reliable correction and queries. SQLite stores linked tables in one portable file.

!!! quote "One-sentence version"
    Model entities and relationships first, create the database from a saved schema, then keep every analytical question as a SQL file.

## You need

- a small cleaned CSV sample;
- SQLite or Python's built-in `sqlite3` module;
- an entity-relationship sketch;
- stable project identifiers and source references.

## Workflow

### Step 1: define the schema

Create `schema.sql`:

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE person (
  person_id TEXT PRIMARY KEY,
  preferred_name TEXT NOT NULL,
  source_note TEXT
);

CREATE TABLE work (
  work_id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  year_start INTEGER,
  year_end INTEGER,
  date_note TEXT
);

CREATE TABLE contribution (
  person_id TEXT NOT NULL REFERENCES person(person_id),
  work_id TEXT NOT NULL REFERENCES work(work_id),
  role TEXT NOT NULL,
  source_id TEXT NOT NULL,
  certainty TEXT NOT NULL DEFAULT 'certain',
  PRIMARY KEY (person_id, work_id, role, source_id)
);
```

### Step 2: create the database

```bash
sqlite3 data/project.sqlite < schema.sql
```

Or use Python if the command is unavailable.

### Step 3: import a tiny sample

Import people and works before relationship rows. Turn on foreign-key checks and stop on invalid identifiers rather than creating orphan records.

### Step 4: save research queries

Create `queries/works-per-person.sql`:

```sql
SELECT p.preferred_name, COUNT(DISTINCT c.work_id) AS work_count
FROM person AS p
LEFT JOIN contribution AS c USING (person_id)
GROUP BY p.person_id
ORDER BY work_count DESC, p.preferred_name;
```

Run it with:

```bash
sqlite3 -header -csv data/project.sqlite < queries/works-per-person.sql \
  > output/works-per-person.csv
```

### Step 5: validate

Check duplicate names, empty sources, impossible date ranges, orphan keys and category spelling. Compare a random sample with the original sources.

## Output

A recreatable SQLite database, `schema.sql`, import procedure, saved queries, data dictionary and open-format exports.

## Check yourself

- Can the database be rebuilt from files in the repository?
- Does every relationship carry evidence?
- Are uncertain dates represented without invented precision?
- Do identifiers remain stable when names are corrected?
- Does a left join reveal records with no relationships?

## Common traps

- editing the database manually without recording changes;
- using names as primary keys;
- storing several people in one cell;
- importing relationships before checking entities;
- publishing only the `.sqlite` file with no schema or data dictionary.

## Practice task

Create three tables with at least ten people, ten works and fifteen contributions. Write one query that answers a substantive question and another that diagnoses missing data.
