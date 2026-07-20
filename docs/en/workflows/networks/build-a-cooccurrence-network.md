---
title: "How do I build a source-linked co-occurrence network?"
description: "Create edges from shared units while preserving the scenes, documents or events that justify every connection."
category: "Networks"
difficulty: "intermediate"
time: "90–150 min"
tags: [network, co-occurrence, bipartite, NetworkX]
---

# How do I build a source-linked co-occurrence network?

<div class="answer-meta" markdown>
<span>Networks</span><span>intermediate</span><span>90–150 min</span>
</div>

## What you are trying to do

You have entities linked to shared units—characters in scenes, people in letters, places in documents—and want a network. Preserve the entity-unit table first; the projected edge list is a derived view.

## You need

- a CSV with `unit_id` and `entity_id`, one pair per row;
- a clear definition of the shared unit;
- Python with `pandas` and `networkx`;
- source references for every unit.

## Workflow

```python
from itertools import combinations
from collections import Counter
import pandas as pd

memberships = pd.read_csv("data/entity_unit.csv")
edges = Counter()

evidence = {}
for unit_id, group in memberships.groupby("unit_id"):
    entities = sorted(set(group["entity_id"]))
    for left, right in combinations(entities, 2):
        edges[(left, right)] += 1
        evidence.setdefault((left, right), []).append(unit_id)

rows = [
    {"source": a, "target": b, "weight": weight,
     "evidence_units": "|".join(evidence[(a, b)])}
    for (a, b), weight in edges.items()
]
pd.DataFrame(rows).to_csv("output/edges.csv", index=False)
```

Then load the edge list into NetworkX, Gephi or Cytoscape. Calculate degree only after checking the distribution of unit sizes; one large scene creates many projected edges.

## Output

The original bipartite entity-unit table, a derived edge list with evidence IDs and a visualization whose threshold is documented.

## Check yourself

- Does sharing a unit actually mean the relationship claimed?
- Are aliases and duplicate entities resolved?
- Do large units dominate the projection?
- Can every edge be opened back to source evidence?
- What happens when uncertain memberships are removed?

## Common traps

- throwing away the bipartite table after projection;
- treating edge weight as relationship strength without interpretation;
- excluding isolated entities from the published data;
- choosing a threshold only to make the graph attractive;
- reading a force-directed layout as geography or chronology.

## Practice task

Build the network twice: once with all shared units and once excluding units above the 90th percentile in size. Explain which centralities change and what that says about the edge rule.
