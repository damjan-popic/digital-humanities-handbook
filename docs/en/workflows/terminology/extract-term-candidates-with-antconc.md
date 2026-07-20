---
title: "How do I extract term candidates with AntConc?"
description: "You need a first list of candidate terms from a domain corpus."
category: "Terminology"
difficulty: "beginner"
time: "25–45 min"
tags: [AntConc, terminology, corpus, keywords]
---

# How do I extract term candidates with AntConc?

<div class="answer-meta" markdown>
<span>Terminology</span>
<span>beginner</span>
<span>25–45 min</span>
</div>

## What you are trying to do

You need a first list of candidate terms from a domain corpus.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Plain-text corpus
- Optional stopword list

## Tools

- [AntConc](https://www.laurenceanthony.net/software/antconc)

## Workflow

1. Load corpus files into AntConc.
2. Generate word, cluster, and n-gram lists.
3. Set a minimum frequency threshold.
4. Export candidate lists.
5. Manually classify candidates: keep, reject, maybe.

## Output

`terms.csv` with ranked term candidates.

## Check yourself

- Are high-frequency function words removed?
- Do multi-word terms survive?
- Can each accepted term be justified with corpus examples?

## Common traps

- Equating frequency with terminological importance.
- Ignoring spelling variants.
- Exporting lists with no context examples.

## Practice task

Users build term lists from two mini corpora and compare which terms are domain-specific.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
