---
title: "How do I create a sentence-similarity heat map?"
description: "You want to see whether sentences, paragraphs, or documents cluster semantically."
category: "Visualization"
difficulty: "advanced"
time: "60–120 min"
tags: [sentence-transformers, heat map, semantic similarity, Python]
---

# How do I create a sentence-similarity heat map?

<div class="answer-meta" markdown>
<span>Visualization</span>
<span>advanced</span>
<span>60–120 min</span>
</div>

## What you are trying to do

You want to see whether sentences, paragraphs, or documents cluster semantically.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- List of sentences or short documents

## Tools

- [sentence-transformers](https://www.sbert.net)
- [Matplotlib](https://matplotlib.org)

## Workflow

1. Choose a sentence embedding model suitable for the language.
2. Encode all sentences.
3. Compute pairwise cosine similarities.
4. Plot the similarity matrix as a heat map.
5. Cluster or reorder rows only if you explain the method.

## Output

`heatmap.png` plus similarity table.

## Check yourself

- Are labels readable?
- Does the model support the language?
- Are high-similarity pairs inspected manually?

## Common traps

- Overinterpreting colour gradients.
- Comparing long and short texts without thought.
- Forgetting that embeddings compress meaning.

## Practice task

Users predict which texts should cluster, then compare predictions to the heat map.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
