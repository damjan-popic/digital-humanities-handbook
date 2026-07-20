---
title: "How do I extract named entities with spaCy?"
description: "You need a first pass at people, places, organizations, or other named entities in texts."
category: "NLP"
difficulty: "intermediate"
time: "30–60 min"
tags: [spaCy, NER, named entities, Python]
---

# How do I extract named entities with spaCy?

<div class="answer-meta" markdown>
<span>NLP</span>
<span>intermediate</span>
<span>30–60 min</span>
</div>

## What you are trying to do

You need a first pass at people, places, organizations, or other named entities in texts.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Plain-text files
- Language model for spaCy

## Tools

- [spaCy](https://spacy.io)
- [pandas](https://pandas.pydata.org)

## Workflow

1. Install or load the correct spaCy model.
2. Run NER on a small sample first.
3. Export entity text, label, document ID, and context.
4. Manually inspect errors.
5. Filter or normalize entities before visualization.

## Output

`entities.csv` with entity mentions.

## Check yourself

- Are entities mentions or unique entities?
- Does the model work for your language/domain?
- Are false positives labeled?

## Common traps

- Treating NER as authority.
- Forgetting that “Paris” may be a person or place.
- Counting mentions as people.

## Worked example

- [medieval notarial NER workflow](../../case-studies/medieval-ner.md) shows why historical named-entity extraction often needs a domain-specific annotation schema, a baseline, and a manual error typology.

## Practice task

Users compare human and spaCy entity extraction on the same paragraph and build an error typology.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
