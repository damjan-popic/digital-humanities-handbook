---
title: "How do I make a custom stop-word list for spaCy?"
description: "Default stop-word lists remove too little, too much, or the wrong words for your corpus."
category: "Automation"
difficulty: "intermediate"
time: "25–50 min"
tags: [spaCy, preprocessing, stop words, NLP]
---

# How do I make a custom stop-word list for spaCy?

<div class="answer-meta" markdown>
<span>Automation</span>
<span>intermediate</span>
<span>25–50 min</span>
</div>

## What you are trying to do

Default stop-word lists remove too little, too much, or the wrong words for your corpus.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Corpus
- Frequency list
- A clear analysis goal

## Tools

- [spaCy](https://spacy.io)

## Workflow

1. Generate a frequency list from your corpus.
2. Mark words that are unhelpful for your specific task.
3. Keep a separate domain stop-word file.
4. Load the list into spaCy or your preprocessing script.
5. Document why unusual words were added or removed.

## Output

`stopwords.json` or similar reusable list.

## Check yourself

- Does the list remove noise without deleting meaningful terms?
- Are language and domain documented?
- Can someone reproduce the list?

## Common traps

- Using stop words because “everyone does”.
- Removing negation words such as `not` when sentiment matters.
- Hard-coding lists inside scripts.

## Practice task

Users build different stop-word lists for literary, legal, and social-media texts, then compare choices.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
