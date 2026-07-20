---
title: "Medieval notarial NER workflow"
description: "A hybrid baseline and supervised-training pattern for named-entity recognition in medieval notarial material."
tags: [projects, NER, medieval, historical-NLP, annotation]
---

# Medieval notarial NER workflow

<div class="answer-meta" markdown>
<span>historical NLP</span>
<span>NER</span>
<span>annotation schema</span>
</div>

## What this project does

This example shows how to approach named-entity recognition in medieval notarial material. It combines a hybrid extractor baseline with a planned supervised fine-tuning workflow, using explicit person-span annotation as the safest first target.

[:octicons-mark-github-16: Open the source repository](https://github.com/damjan-popic/medieval-ner)

## Use this when

- you need a historical-NLP example where generic NER is not enough.
- you want to teach annotation guidelines and span boundaries.
- you need a realistic baseline plus model-training architecture.
- you want users to inspect domain-specific failure modes.

## What to inspect in the code

- `process_ner.py` — current hybrid inference pipeline.
- `Rules.md` — extraction expectations.
- `annotation_guidelines.md` — annotation instructions.
- `train_ner.py` — fine-tuning entry point.
- `evaluate_ner.py` — token-label and span evaluation.
- `prepare_training_data.py` — converts annotations into token-classification records.
- `data/annotation_schema.md` — annotation standard.

## Minimal run path

Treat this as a design pattern rather than a push-button solution. The useful minimum path is:

```text
source text → annotation schema → baseline extractor → error typology → gold spans → model training → evaluation
```

Start with ten short passages and evaluate span boundaries manually before training anything.

## Relevant handbook workflows

- [How do I extract named entities with spaCy?](../workflows/nlp/extract-named-entities-with-spacy.md)
- [How do I audit AI output against source documents?](../workflows/ai/audit-ai-output-against-source-documents.md)
- [How do I make a tiny digital edition of a historical text?](../workflows/editions/make-a-tiny-digital-edition-of-a-historical-text.md)
- [How do I visualise uncertainty in humanities data?](../workflows/visualization/visualise-uncertainty-in-humanities-data.md)

## Practice use

Give users five medieval or historical passages. Ask them to mark person spans, compare disagreements, and write two rules that would help a baseline extractor without pretending the rules solve the whole problem.

## Limits and cautions

- Historical names, titles, patronymics, abbreviations, and formulaic references are difficult for generic NER models.
- A historical index is not automatically a complete gold standard.
- Rules and models solve different problems and should be evaluated separately.
- Entity extraction can expose people, places, and community knowledge in ways that need contextual review.
