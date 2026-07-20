---
title: "How do I map places mentioned in a text?"
description: "You want a spatial overview of places mentioned in a text, archive, or interview."
category: "Mapping"
difficulty: "beginner"
time: "45–90 min"
tags: [mapping, geocoding, literary geography, places]
---

# How do I map places mentioned in a text?

<div class="answer-meta" markdown>
<span>Mapping</span>
<span>beginner</span>
<span>45–90 min</span>
</div>

## What you are trying to do

You want a spatial overview of places mentioned in a text, archive, or interview.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Text with place mentions
- Gazetteer or coordinates

## Tools

- [QGIS](https://qgis.org)
- [uMap](https://umap.openstreetmap.fr)
- [Wikidata](https://www.wikidata.org)

## Workflow

1. Extract place mentions manually or with NER.
2. Classify places as real, fictional, vague, historical, or uncertain.
3. Find coordinates from a gazetteer.
4. Map only places whose coordinates make sense.
5. Write an interpretation of omissions and uncertainty.

## Output

Map with notes on place certainty.

## Check yourself

- Are historical place names handled?
- Are ambiguous places disambiguated?
- Is “not mapped” documented?

## Common traps

- Pretending every place has one stable coordinate.
- Mapping vague places too confidently.
- Forgetting that frequency is not importance.

## Worked example

- [static knowledge graph, map, and corpus index example](../../case-studies/ladakh-relations.md) shows how place entities, map views, and source references can be connected in a static DH site.

## Practice task

Users map five places only. The constraint keeps the task interpretive rather than cartographic busywork.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
