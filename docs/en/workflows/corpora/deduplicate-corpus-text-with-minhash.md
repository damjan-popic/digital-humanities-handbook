---
title: "How do I deduplicate corpus text with MinHash?"
description: "Your corpus contains near-duplicate documents or sentences and simple exact matching is not enough."
category: "Corpora"
difficulty: "advanced"
time: "45–120 min"
tags: [deduplication, MinHash, corpus cleaning, Python]
---

# How do I deduplicate corpus text with MinHash?

<div class="answer-meta" markdown>
<span>Corpora</span>
<span>advanced</span>
<span>45–120 min</span>
</div>

## What you are trying to do

Your corpus contains near-duplicate documents or sentences and simple exact matching is not enough.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Text files or sentence list
- Similarity threshold

## Tools

- [datasketch](https://ekzhu.github.io/datasketch/)

## Workflow

1. Choose whether you deduplicate documents, paragraphs, or sentences.
2. Tokenize consistently.
3. Create MinHash signatures.
4. Use locality-sensitive hashing to find near-duplicates.
5. Remove or mark duplicates and keep a log.

## Output

Cleaned corpus plus deduplication report.

## Check yourself

- Were formulaic but legitimate texts removed?
- Does the threshold fit the genre?
- Is the original recoverable?

## Common traps

- Using one threshold for every genre.
- Deleting all repeated phrases in poetry or legal text.
- Not reporting how much data was removed.

## Practice task

Users manually judge pairs first, then compare their intuition to MinHash results.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
