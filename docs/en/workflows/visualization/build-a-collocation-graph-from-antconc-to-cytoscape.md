---
title: "How do I build a collocation graph from AntConc to Cytoscape?"
description: "You want to show lexical relationships as a network rather than a table."
category: "Visualization"
difficulty: "intermediate"
time: "45–90 min"
tags: [collocation, network, AntConc, Cytoscape, visualization]
---

# How do I build a collocation graph from AntConc to Cytoscape?

<div class="answer-meta" markdown>
<span>Visualization</span>
<span>intermediate</span>
<span>45–90 min</span>
</div>

## What you are trying to do

You want to show lexical relationships as a network rather than a table.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Plain-text corpus
- Collocation settings

## Tools

- [AntConc](https://www.laurenceanthony.net/software/antconc)
- [Cytoscape](https://cytoscape.org)

## Workflow

1. Generate collocates in AntConc for selected keywords.
2. Export collocation table with association scores.
3. Filter weak or noisy edges.
4. Import nodes and edges into Cytoscape.
5. Style by frequency, score, or semantic group.

## Output

Interactive collocation network.

## Check yourself

- Do edges represent a clear statistical relationship?
- Are labels readable?
- Does the graph answer a question beyond looking cool?

## Common traps

- Making a hairball network.
- Forgetting to explain edge weights.
- Choosing a threshold after the graph “looks nice”.

## Practice task

Use the same collocation table with two different filtering thresholds, then justify which one better fits the research question.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
