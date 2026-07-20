---
title: "How do I query a corpus with CQPweb?"
description: "You need advanced pattern queries, KWIC output, and frequency tables."
category: "Corpora"
difficulty: "advanced"
time: "45–90 min"
tags: [CQPweb, corpus query, KWIC, CQP]
---

# How do I query a corpus with CQPweb?

<div class="answer-meta" markdown>
<span>Corpora</span>
<span>advanced</span>
<span>45–90 min</span>
</div>

## What you are trying to do

You need advanced pattern queries, KWIC output, and frequency tables.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Indexed corpus or vertical file
- Query question

## Tools

- [CQPweb](https://cwb.sourceforge.io/cqpweb.php)

## Workflow

1. Prepare or select an indexed corpus.
2. Start with simple word or lemma queries.
3. Add POS or structural constraints gradually.
4. Save useful query patterns.
5. Export KWIC and frequency tables for interpretation.

## Output

KWIC lines, frequency tables, and reusable CQP queries.

## Check yourself

- Does the query return examples that match your intended phenomenon?
- Are false positives counted?
- Is corpus size considered when comparing frequencies?

## Common traps

- Writing a fancy query before defining the linguistic question.
- Comparing raw counts across unequal subcorpora.
- Forgetting that annotation errors affect results.

## Practice task

Users compete to write the shortest correct query for a small phenomenon, then explain false positives.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
