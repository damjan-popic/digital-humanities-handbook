---
title: "How do I compare style with function words?"
description: "Build a transparent stylometric baseline and test whether apparent author or genre differences survive document controls."
category: "Text analysis"
difficulty: "intermediate"
time: "90–150 min"
tags: [stylometry, function words, PCA, document features]
---

# How do I compare style with function words?

<div class="answer-meta" markdown>
<span>Text analysis</span><span>intermediate</span><span>90–150 min</span>
</div>

## What you are trying to do

You want to compare writing style using frequent grammatical words that are less topic-dependent than content vocabulary. The goal is a baseline for exploring authorship, genre, translation or period—not an automatic attribution verdict.

## You need

- several documents per group whenever possible;
- comparable text lengths and genres or metadata to control them;
- a documented function-word list appropriate to the language;
- Python with `pandas` and `scikit-learn`.

## Workflow

1. Divide long works into comparable chunks without mixing train and test chunks from the same work.
2. Count the selected words per document and normalize to relative frequencies.
3. Standardize features only after separating any evaluation set.
4. Visualize with PCA and inspect which words drive dimensions.
5. Compare within-author and between-author distances.
6. Repeat after controlling genre, period, OCR quality and translation status.

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

features = pd.read_csv("output/function_word_frequencies.csv", index_col="doc_id")
X = StandardScaler().fit_transform(features)
coords = PCA(n_components=2, random_state=42).fit_transform(X)
pd.DataFrame(coords, index=features.index, columns=["pc1", "pc2"]).to_csv(
    "output/style_pca.csv"
)
```

## Output

A document-feature matrix, documented word list, exploratory coordinates or distances and a sensitivity analysis.

## Check yourself

- Are chunks from the same work leaking across evaluation sets?
- Are groups separated by genre or date before author?
- Does OCR damage change high-frequency short words?
- Does the pattern survive a second feature set or chunk size?

## Common traps

- presenting a PCA plot as a classifier;
- interpreting proximity as literary influence;
- treating every text by one author as independent;
- selecting features after seeing the desired groups;
- omitting documents that weaken the visual story.

## Practice task

Compare at least three documents from two groups. Repeat with two chunk sizes and report one stable and one unstable observation.
