---
title: "How do I build a simple cultural heritage map?"
description: "You want to turn cultural objects, monuments, texts, or institutions into an explorable map."
category: "Mapping"
difficulty: "beginner"
time: "60–120 min"
tags: [mapping, heritage, metadata, public history]
---

# How do I build a simple cultural heritage map?

<div class="answer-meta" markdown>
<span>Mapping</span>
<span>beginner</span>
<span>60–120 min</span>
</div>

## What you are trying to do

You want to turn cultural objects, monuments, texts, or institutions into an explorable map.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- List of items
- Coordinates or place descriptions
- Metadata fields

## Tools

- [uMap](https://umap.openstreetmap.fr)
- [Wikidata](https://www.wikidata.org)
- [QGIS](https://qgis.org)

## Workflow

1. Define what counts as an item.
2. Create a metadata table: title, type, date, place, source, note, rights.
3. Find coordinates and mark uncertain ones.
4. Import the table into a mapping tool.
5. Write a public-facing description for each point.

## Output

Interactive heritage map with metadata.

## Check yourself

- Are sources linked?
- Are categories meaningful?
- Does the map avoid overclaiming precise locations?

## Common traps

- Creating a pin dump with no interpretation.
- Forgetting rights for images.
- Mapping only famous or easy-to-find objects.

## Worked example

- [static knowledge graph, map, and corpus index example](../../case-studies/ladakh-relations.md) shows a static cultural-heritage graph and map with coordinate review and corpus links.

## Practice task

Create a five-point sample map, then audit whose heritage the map includes or excludes.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
