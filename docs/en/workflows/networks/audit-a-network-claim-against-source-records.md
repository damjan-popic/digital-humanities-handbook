---
title: "How do I audit a network claim against source records?"
description: "audit a network claim against source records with explicit sources, checks and uncertainty."
category: "Networks"
category_id: "Networks"
difficulty: "intermediate"
time: "45–60 min"
tags: [modelling, provenance, uncertainty]
status: draft
---

# How do I audit a network claim against source records?

## What you are trying to do

Check whether a claim such as “C led the group” or “E brokered communication” follows from the selected records. Return from a metric or picture to identity decisions, edge semantics and source passages. Read [Networks and visualization](../../chapters/networks-visualization.md) first.

## You need

Unpack the [companion ZIP](../../../assets/downloads/contested-models-v1.zip), read `input/dossier.md` and run the standard-library Python script. A text editor and CSV viewer are sufficient. The synthetic dossier permits controlled testing; the authentic newspaper observations remain a separate source-level counterexample.

## Workflow

### 1. Write a falsifiable claim

Record the exact graph, population, date selection, edge rule and metric. Replace “most important” with a measurable statement before testing it. For example: “C has the highest degree among the six retained people in the shared-document projection at threshold 2.” Do not substitute historical leadership for this limited result.

### 2. Reproduce and choose an audit sample

```bash
python run.py --output output-first
```

Inspect `projection_t2-metrics.csv` and `correspondence-metrics.csv`. Select a prominent node, an unexpected isolate and edges with different support. Use this minimum audit:

| Object | Supporting record | What it supports |
|---|---|---|
| AB | SYN-D1, SYN-D2, SYN-D5 | shared documents; D2 also asserts A → B |
| CE | SYN-D3, SYN-D5 | shared lists, not correspondence |
| E → F | SYN-D6 | asserted letter with probable recipient and February event window |
| Authentic issue pairs | AF observation locators | same-issue co-occurrence, not letters |

Keep full identifiers when recording decisions. Open the dossier section named by the supporting document, not merely the derived edge table.

### 3. Audit identity and time

The dossier stipulates A's identity across name variants. Explain what additional evidence a real project would require. Check whether merging two uncertain identities could combine their neighbours into a false bridge.

For D6, retain the half-open February interval and probable recipient. Do not turn the interval into a month-long relationship. The aggregate graph spans 1910 and 1925; it does not establish that every path was available simultaneously.

### 4. Test competing edge rules

Compare `projection-evidence.csv` with `correspondence-edges.csv`: CE disappears under the correspondence rule. Compare all recipients with certain recipients only: E→F disappears. Under the threshold-2 missing-D6 scenario, E's raw betweenness becomes zero instead of four. Record these changes rather than selecting the most persuasive picture.

Open `authentic-issue-cooccurrence.csv` and the packet's original-observation extract. Four individually labelled people generate six pairs solely because the issue is treated as one container. These observations evidence zero correspondence edges, not the absence of all real-world correspondence.

### 5. Audit the visual inference

If you have a plot, list each claim derived from position, proximity, colour or size. A force-directed cluster does not establish shared ideology. Test whether rotating or relaying out the unchanged graph would alter the verbal argument. Record unsupported interpretations as unsupported, not as errors in the historical source.

## Output

Submit a claim ledger with claim, model, metric, source locator, evidence scope, alternative rule and verdict: supported within model, requires external evidence, or unsupported. Include node/edge tables and a text summary; no visual inspection is required to complete the source audit.

## Check yourself

Does the source assert the relation drawn? Is confidence attached to the correct assertion? Can the reader recover the rejected interpretation? Are sensitive identities or inferred ties appropriate to publish?

## Common traps

Reading a layout as geography; turning co-occurrence into friendship; treating unknown dates as simultaneous; calling an isolate socially isolated; and describing a mathematical community as a documented faction.

## Practice task

Rewrite “E was the network's indispensable intermediary” in 150 words. Report which graph gives E betweenness, what happens without D6, and which additional historical evidence would be needed to argue actual mediation. Keep the failed claim in the audit log.
