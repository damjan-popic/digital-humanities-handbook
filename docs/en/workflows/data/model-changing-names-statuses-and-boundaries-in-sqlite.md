---
title: "How do I model changing names, statuses and boundaries in SQLite?"
description: "Build and query a source-qualified SQLite assertion model without erasing changes or disagreement."
category: "Data"
category_id: "Data"
difficulty: "intermediate"
time: "60–90 min"
tags: [SQLite, SQL, temporal-data, assertions, provenance]
status: draft
---

# How do I model changing names, statuses and boundaries in SQLite?

<div class="answer-meta" markdown>
<span>Data</span><span>intermediate</span><span>60–90 min</span>
</div>

## What you are trying to do

Ask what a particular source says about a person at a particular time, without collapsing multilingual names, competing occupational labels or changing territorial membership into one timeless row. The synthetic dossier makes the loss visible; it does not document real historical residents. Read [Databases and SQL](../../chapters/databases-sql.md) for the comparison with flat and normalized models.

## You need

Download and unpack the [companion ZIP](../../../assets/downloads/contested-models-v1.zip). Use Python 3.10 or later with its standard-library SQLite module, a terminal and a text editor. No package installation or SQLite command-line client is required. Read `README.md`, `input/dossier.md` and `rights-and-provenance.md` first. Work on a copy and keep original inputs unchanged.

## Workflow

### 1. Inspect the assertions

Open `input/sources.csv`, `input/assertions.csv` and `schema.sql`. The source inventory resolves exactly D1–D6, N1, N2, BORDER and NAMES to anchored dossier blocks. An assertion connects a subject to either text or another entity, with source wording, an explicit `exact`, `translation` or `summary` relation, context, validity interval, record time and confidence. Intervals are half-open: the start is included, the end excluded. `event_window` means a possible event date, not continuous duration.

Compare A04 and A05: servant in an institutional vocabulary and seamstress in self-description overlap in 1910. Do not decide by majority vote or replace both with a neutral-looking occupation. A02 and A03 instead represent a corrected transcription; A03 explicitly supersedes A02. The schema retains both. A replacement must preserve the same source, context, historical interval and interval kind, and each assertion can have at most one direct successor.

### 2. Build and inspect

From the unpacked packet directory, run:

```bash
python run.py --output output-first
python query.py --database output-first/dossier.sqlite --subject SYN-A --as-of 1910-06-15 --known-at 2026-09-03T00:00:00Z
python query.py --database output-first/dossier.sqlite --conflicts
```

The build creates 13 assertions, of which 12 are current, and one pair in the status review queue. Check the generated `status-conflicts.csv` and `assertions-1910_corrected.csv`. A constraint passing means internal consistency, not historical truth.

### 3. Change both kinds of time separately

Repeat the entity query with `--known-at 2026-09-01T23:59:59Z`. The June 1910 signature should now read Ana Kovać, the earlier editorial transcription, instead of Ana Kovač. Restore the later record time and change `--as-of` to `1925-01-25`: inspect status and language-use changes.

Review `queries/at-date.sql`: parameters are bound, not inserted into SQL strings. It excludes superseded assertions only if the replacement was already recorded by the selected editorial time. This is a small append-only teaching ledger, not a full database-managed transaction-time system.

### 4. Follow territorial membership

Use `--subject SYN-L1` with historical dates `1919-12-31` and `1920-01-01`. Membership changes from `SYN-EAST` to `SYN-W` at the interval boundary. The fictional residence stays fixed; this is not evidence of migration. The [spatial workflow](../mapping/model-changing-place-names-and-boundaries.md) tests positional uncertainty separately.

### 5. Document the export loss

Compare the assertion table with a one-row person export. List what disappears: source-specific name, status context, language assignment versus use, record history and competing intervals. A convenient analytical CSV is permissible if its selection rule and source IDs remain recoverable.

## Output

Keep the SQLite database, source CSVs, two editorial-time query results, the conflict table and a decision note. Record your Python and SQLite versions, historical date, editorial cutoff and exact command. Do not describe the status review queue as a list of proven contradictions.

## Check yourself

- Are 13 assertions retained and 12 current?
- Does the earlier signature reappear at the earlier record time?
- Is 1920-01-01 in the new membership interval only?
- Can every value be traced to source wording and context?

## Common traps

Overwriting names, treating assigned language as demonstrated competence, using a whole-year event window as continuous activity, and interpreting foreign-key checks as evidence are different errors. Keep their corrections explicit. The packet validates dates before import; the SQL schema alone does not validate every calendar string.

## Practice task

Submit a three-row comparison of flat, normalized and assertion-based representations, then explain one conflict and one supersession. State which distinction must be queryable and which belongs in the source or a prose note.
