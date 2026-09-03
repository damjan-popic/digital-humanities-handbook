---
title: "How do I compare bipartite and projected networks?"
description: "compare bipartite and projected networks with explicit sources, checks and uncertainty."
category: "Networks"
category_id: "Networks"
difficulty: "intermediate"
time: "60–90 min"
tags: [modelling, provenance, uncertainty]
status: draft
---

# How do I compare bipartite and projected networks?

## What you are trying to do

Test how a shared-document rule changes what “connected” means. Preserve the person–document evidence while comparing projections, thresholds and source-qualified correspondence. [Networks and visualization](../../chapters/networks-visualization.md) supplies definitions and interpretation.

## You need

Unpack the [companion ZIP](../../../assets/downloads/contested-models-v1.zip). Use Python 3.10+ and a CSV viewer. No graph library or drawing application is required. Read `input/dossier.md`; all six people and six network documents are synthetic. The authentic newspaper comparison remains separately labelled.

## Workflow

### 1. Fix the population and selection

Inspect `input/participation.csv` and `input/documents.csv`. There are six people, six documents and 18 participation rows. A person is counted once per document. Preserve sender/recipient roles and source locators. Separate notes SYN-N1 and SYN-N2 belong to the database exercise, not this network selection.

### 2. Generate all views

```bash
python run.py --output output-first
```

The bipartite graph connects people only to documents. The projected graph links pairs sharing a document, with weight equal to distinct shared documents. The correspondence graph uses only letter records with explicit sender and recipient roles.

Open `bipartite-edges.csv`, `projection-evidence.csv` and `correspondence-edges.csv`. A projected pair retains every supporting document; it does not become a new independent source.

### 3. Compare thresholds and rankings

| Rule | Edges | Highest person degree |
|---|---:|---|
| Bipartite | 18 | E, 4 documents |
| Projection ≥1 document | 15 | all six, 5 people |
| Projection ≥2 documents | 7 | C, 4 people |
| Projection ≥3 documents | 2 | A, B, D, E, 1 person |
| Correspondence | 3 | E, total degree 2 |

Compare the corresponding `*-metrics.csv` files. Keep isolated people in the denominator. Bipartite degree counts documents; projected degree counts people. The code uses unweighted unit-length paths after thresholding, raw betweenness and normalized outgoing harmonic closeness. Weight is support, not distance.

### 4. Explain projection inflation

SYN-D5 lists six people and creates fifteen possible pairs. Inspect AB, supported by D1, D2 and D5, and CE, supported by D3 and D5. Repeated co-documentation does not establish friendship.

Inspect `fractional-weights.csv` and `results.json`. Giving each document contribution 1/(k−1) per pair and requiring weight ≥1 retains AB, DE and EF. Removing D5 at ordinary threshold 1 instead retains seven pairs. Explain why these alternatives differ.

### 5. Check communities and missing records

In `results.json`, the threshold-2 optimum is ABC | DEF, whereas threshold 1 puts everyone together. The code exhaustively tests unweighted undirected modularity at resolution 1 and retains all ties; it is intended only for six-person examples. Correspondence communities discard direction explicitly.

Withhold D6 before threshold 2: EF disappears and E's raw betweenness falls from 4 to 0. Compare `missing_D6-metrics.csv`. This targeted loss scenario is not an estimate of random archival survival.

## Output

Submit the three-model comparison, two or more thresholds, node metrics, provenance table and one sensitivity interpretation. A drawing is optional. Provide a prose description of components and isolates so all results are available without seeing a plot.

## Check yourself

Can every pair be traced to its supporting documents? Did you compare the same six people? Have you named units, direction and normalization? Did an algorithmic partition become a historical faction without corroboration?

## Common traps

Treating a six-person list as fifteen independent testimonies; comparing degrees with different units; hiding isolates; using support counts as path lengths; and reporting only the threshold that confirms an expected ranking.

## Practice task

State a claim that remains valid and one that fails across constructions. Audit AB and CE using the [source-record workflow](audit-a-network-claim-against-source-records.md). Preserve the construction rule in the final sentence.
