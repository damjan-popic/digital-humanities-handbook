---
title: "How do I analyse emotion with a lexicon and a manual check?"
description: "Create a transparent baseline for emotion language, then measure where words, context and human labels disagree."
category: "Text analysis"
difficulty: "intermediate"
time: "90–150 min"
tags: [emotion, lexicon, validation, annotation]
---

# How do I analyse emotion with a lexicon and a manual check?

<div class="answer-meta" markdown>
<span>Text analysis</span><span>intermediate</span><span>90–150 min</span>
</div>

## What you are trying to do

You want to estimate where a corpus uses language associated with categories such as joy, fear, anger or sadness. A lexicon offers a transparent baseline, but it does not reveal a writer's inner state and it fails on negation, irony, quotation, polysemy and genre.

!!! quote "One-sentence version"
    Count documented emotion associations, annotate a sample in context, and report the gap between lexical signal and interpretive category.

## You need

- a document or sentence table with stable IDs;
- a licensed emotion lexicon suitable for the language or a documented adaptation;
- lemmas where inflection would otherwise fragment matching;
- a codebook for the human category;
- Python or a spreadsheet for joining and counting.

## Workflow

### Step 1: define the target

State whether you measure emotion words, emotion attributed to a person, narrator stance, emotional framing or reader response. Use one unit—sentence, paragraph or document—and define mixed and uncertain cases.

### Step 2: inspect the lexicon

Record its language, source, categories, annotation procedure, licence and known domain. For a translated lexicon, manually inspect culturally or morphologically difficult entries. Remove or flag ambiguous words rather than silently trusting every match.

### Step 3: create a lexical baseline

```python
import pandas as pd

texts = pd.read_csv("data/sentences.csv")      # sentence_id, text, lemmas
lexicon = pd.read_csv("data/emotion_lexicon.csv")  # lemma, emotion

rows = []
for row in texts.itertuples():
    lemmas = str(row.lemmas).split()
    matches = lexicon[lexicon["lemma"].isin(lemmas)]
    counts = matches["emotion"].value_counts().to_dict()
    rows.append({"sentence_id": row.sentence_id, **counts})

pd.DataFrame(rows).fillna(0).to_csv("output/lexicon_counts.csv", index=False)
```

### Step 4: annotate a stratified sample

Sample examples with high scores, no matches, different genres and expected difficult phenomena. Have two people label at least part of the sample using the codebook. Preserve disagreement and reasoning.

### Step 5: compare signal and judgement

Create a confusion table for a decision rule or correlate counts with human labels where categories allow it. Read false positives and false negatives. Adjust only with an explicit rule and test the adjustment on another sample.

### Step 6: aggregate responsibly

Normalize by words or relevant units, report document distributions and show uncertainty. Separate quoted speech from narrator or author language when the claim requires it.

## Output

A lexicon provenance note, codebook, sentence-level count table, human-labelled validation sample and error analysis.

## Check yourself

- What exactly does one match claim?
- Are scores driven by one common ambiguous word?
- Does negation or quotation reverse the interpretation?
- Do translated categories fit the historical and cultural setting?
- Can you trace every aggregate result to passages?

## Common traps

- calling polarity “emotion” without defining either;
- interpreting a character's words as the author's feelings;
- using a consumer-review lexicon on poetry without validation;
- hiding zero-match documents;
- revising the lexicon on the same examples used to report performance.

## Practice task

Manually label 50 sentences, compare them with a lexical rule and classify the ten most informative errors. Write one paragraph on what the lexicon measures well and one on what it cannot measure.
