---
title: "How do I filter Common Crawl with CC-Net?"
description: "You need a very large monolingual corpus and can handle computational overhead."
category: "Corpora"
difficulty: "advanced"
time: "half day+"
tags: [Common Crawl, CC-Net, large corpora, web data]
---

# How do I filter Common Crawl with CC-Net?

<div class="answer-meta" markdown>
<span>Corpora</span>
<span>advanced</span>
<span>half day+</span>
</div>

## What you are trying to do

You need a very large monolingual corpus and can handle computational overhead.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Common Crawl dump list
- Language ID model
- Filtering criteria

## Tools

- [CC-Net](https://github.com/facebookresearch/cc_net)
- [fastText](https://fasttext.cc)

## Workflow

1. Start with a tiny sample; do not begin with the full web.
2. Download selected Common Crawl shards.
3. Apply language identification and deduplication.
4. Filter by length, quality, and boilerplate indicators.
5. Save JSONL with metadata and checksums.

## Output

Deduplicated JSONL corpus.

## Check yourself

- Is language ID accurate for your target language?
- How much text was filtered out and why?
- Can the pipeline be rerun?

## Common traps

- Underestimating storage and time.
- Creating a giant corpus with unclear quality.
- Ignoring legal and ethical constraints.

## Practice task

Use this as a design exercise before a full run: plan the filters and estimate likely failure modes.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
