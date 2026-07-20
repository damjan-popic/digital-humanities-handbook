---
title: "How do I filter a corpus by language with fastText?"
description: "Your corpus contains mixed-language noise and you need mostly one language."
category: "Corpora"
difficulty: "intermediate"
time: "30–60 min"
tags: [language identification, fastText, corpus cleaning, preprocessing]
---

# How do I filter a corpus by language with fastText?

<div class="answer-meta" markdown>
<span>Corpora</span>
<span>intermediate</span>
<span>30–60 min</span>
</div>

## What you are trying to do

Your corpus contains mixed-language noise and you need mostly one language.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Raw text lines or documents
- Target language code

## Tools

- [fastText](https://fasttext.cc)

## Workflow

1. Run language identification on lines or documents.
2. Save predicted language and confidence score.
3. Set a confidence threshold based on sample inspection.
4. Keep, reject, or review uncertain cases.
5. Document the threshold and sample errors.

## Output

Language-filtered corpus and a rejected/uncertain set.

## Check yourself

- Does the model handle short texts?
- Are code-switching and named entities creating false positives?
- Is the threshold defensible?

## Common traps

- Throwing away multilingual material that matters.
- Assuming confidence score is correctness.
- Filtering before deciding what “language” means for the project.

## Worked examples

- [web text harvesting example](../../case-studies/text-harvester.md) includes a lightweight language-detection step for harvested web texts.
- [website crawler and chatbot corpus builder](../../case-studies/fifi.md) keeps language and source metadata in document records and retrieval chunks.

## Practice task

Users inspect 50 borderline lines and argue whether “wrong language” is a technical or interpretive category.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
