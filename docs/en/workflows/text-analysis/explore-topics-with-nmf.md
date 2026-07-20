---
title: "How do I explore recurring themes with NMF?"
description: "Build an interpretable document-term model, inspect representative texts and test whether the themes survive parameter changes."
category: "Text analysis"
difficulty: "intermediate"
time: "90–150 min"
tags: [NMF, topic analysis, TF-IDF, validation]
---

# How do I explore recurring themes with NMF?

<div class="answer-meta" markdown>
<span>Text analysis</span><span>intermediate</span><span>90–150 min</span>
</div>

## What you are trying to do

You want an exploratory overview of recurring lexical patterns across documents. Non-negative matrix factorization (NMF) decomposes a TF-IDF document-term matrix into components that researchers may interpret as themes.

!!! quote "One-sentence version"
    Fit several small NMF models, inspect top words and whole documents, and report stable patterns rather than treating one run as discovered truth.

## You need

- a CSV with `doc_id`, `text` and useful metadata;
- at least dozens of documents, preferably more;
- Python with `pandas` and `scikit-learn`;
- a documented stop-word and normalization policy.

## Workflow

### Step 1: inspect corpus balance

Count documents and words by period, source and genre. Remove exact duplicates and decide whether very short documents should be combined or excluded.

### Step 2: build a baseline model

```python
import pandas as pd
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer

frame = pd.read_csv("data/documents.csv")

vectorizer = TfidfVectorizer(
    lowercase=True,
    min_df=3,
    max_df=0.85,
    ngram_range=(1, 2),
    max_features=8000,
)
X = vectorizer.fit_transform(frame["text"].fillna(""))

model = NMF(n_components=8, init="nndsvda", random_state=42, max_iter=500)
W = model.fit_transform(X)
H = model.components_
terms = vectorizer.get_feature_names_out()

for topic_id, weights in enumerate(H):
    top = weights.argsort()[-12:][::-1]
    print(topic_id, ", ".join(terms[top]))
```

### Step 3: inspect documents, not only words

For each component, list the documents with the largest weights and read them. Record a provisional label only after identifying what unites and contradicts those documents.

```python
for topic_id in range(W.shape[1]):
    top_docs = W[:, topic_id].argsort()[-5:][::-1]
    print("TOPIC", topic_id, frame.loc[top_docs, ["doc_id", "title"]])
```

### Step 4: test sensitivity

Repeat with different component counts, vocabulary rules and random seeds. Note which themes persist, split, merge or disappear. Compare with a simple keyword or metadata analysis.

### Step 5: create an interpretation table

For each reported component, save the top terms, representative documents, contradictory documents, prevalence by metadata, label, confidence and notes.

## Output

A versioned table of model settings and interpreted components, plus links to source documents and a sensitivity note.

## Check yourself

- Are components driven by OCR artefacts, boilerplate or one publication?
- Did you inspect full documents rather than label from ten words?
- Does the pattern survive another reasonable setting?
- Is the label narrower than the evidence?

## Common traps

- selecting the number of components only because the output looks tidy;
- treating coherence or reconstruction error as a humanistic verdict;
- removing all frequent words before checking whether they carry genre or historical meaning;
- plotting prevalence without document-level uncertainty;
- calling components “topics people discussed” when they are lexical patterns in a sampled corpus.

## Practice task

Fit models with 6, 8 and 10 components. Choose one recurring pattern and write a 300-word interpretation supported by three documents and one counterexample.
