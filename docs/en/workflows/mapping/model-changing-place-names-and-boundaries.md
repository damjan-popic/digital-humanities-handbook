---
title: "How do I model changing place names and boundaries?"
description: "Preserve multilingual place names, unresolved candidates and dated boundaries in a time-qualified spatial model."
category: "Mapping"
category_id: "Mapping"
difficulty: "intermediate"
time: "60–90 min"
tags: [historical-GIS, toponyms, boundaries, temporal-data, uncertainty]
status: draft
---

# How do I model changing place names and boundaries?

<div class="answer-meta" markdown>
<span>Mapping</span><span>intermediate</span><span>60–90 min</span>
</div>

## What you are trying to do

Determine whether a changed territorial label indicates movement, an administrative change or an uncertain identification. Preserve multilingual source names and unresolved candidates instead of replacing them with one modern coordinate. Read [GIS and spatial humanities](../../chapters/gis-spatial-humanities.md) and [Databases and SQL](../../chapters/databases-sql.md).

## You need

Unpack the [companion ZIP](../../../assets/downloads/contested-models-v1.zip). Use Python 3.10+ and a CSV viewer or text editor. The boundary geometry and “St. Peter” candidates are explicitly synthetic; they are not traced from the authentic map. No GIS software is necessary for the tabular route.

## Workflow

### 1. Separate the objects

Read `input/dossier.md`, `candidates.csv`, `places.csv`, `boundaries.csv` and `assertions.csv` inside `input/`. The source mention belongs to a workplace description, not a residence change. Keep the wording “St. Peter”, both candidate IDs, source identifier, date and unresolved decision.

For a new historical source, add one row per multilingual name assertion with language, context, valid interval and source. Do not infer historical name validity from today's preferred gazetteer label. The two current exercise candidates share a name; neither is automatically accepted.

### 2. State temporal and geometric rules

The local engineering square runs from 0 to 1,000 m on both axes. Its divider is x=500 before 1920 and x=600 afterwards. West means x below the divider; east includes the divider. Intervals are half-open. These local coordinates are not EPSG:3794 and must not be placed on a geographic basemap.

Keep source publication time separate from the period represented. A's stable residence is a stipulated assertion covering 1910–1925; the changing boundary is another assertion. Actual research would require independent sources for both.

### 3. Reproduce centre and uncertainty joins

```bash
python run.py --output output-first
python query.py --database output-first/dossier.sqlite --subject SYN-L1 --as-of 1920-01-01
```

Open `output-first/membership.csv`.

| Place | Centre x | Before 1920 | From 1920 | With ±75 m |
|---|---:|---|---|---|
| SYN-L1 | 550 | east | west | both memberships possible in both periods |
| SYN-L2 | 800 | east | east | east only |

The ±75 m range is a sensitivity assumption, not a probability distribution. Geometry-based possible membership does not overwrite the source's asserted membership. Explain their difference.

### 4. Preserve ambiguity in an output view

Inspect `candidate-places.csv`. Each row keeps the mention source and event window,
the boundary-validity interval and the toponym-validity interval in different
fields. `comparison_interval_start` and `_end` are their true boundary/name
intersection; the scope label says this is candidate-place history, not mention
duration. Confirm that the 1917 `SYN-L1` name change appears within the still-active
1910 boundary. Count the unresolved mention once, not as two workplaces or two
residents. Record what new evidence could distinguish the candidates: a dated
street description, surrounding names or a source-specific itinerary.

If you draw a diagram, label it synthetic and include the table. A real GeoPackage adaptation should retain separate dated boundary features and identifiers linked to the assertion table. Do not overwrite the old polygon with the new one.

### 5. Test a different assumption

In a copy of the packet, change L1's uncertainty to zero and rerun into a new directory. Its membership becomes unique in each period, while the centre-based change remains. Restore the original and explain why this does not prove the real-world location to be exact. Test 1919-12-31 and 1920-01-01 separately to check interval endpoints.

## Output

Submit the time-qualified table, candidate-decision log, source-date versus represented-date note and sensitivity comparison. A non-visual table is a complete result; a geographic-looking map of these engineering coordinates would be misleading.

## Check yourself

Are both candidates still visible? Did a workplace become a residence without evidence? Are old boundaries recoverable? Is uncertainty a stated assumption rather than an invented measurement? Could a reader identify the exact join rule?

## Common traps

Silently accepting the first gazetteer result, calling the boundary change migration, counting candidate rows as people, and treating map publication date as the date of every depicted feature.

## Practice task

Write a 150-word answer to “Did A move?” Distinguish the stipulated residence, changing centre membership, positional uncertainty and unresolved workplace mention. Name one distinction kept queryable and one retained in prose.
