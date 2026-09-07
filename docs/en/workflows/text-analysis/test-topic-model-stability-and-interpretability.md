---
title: "How do I test topic-model stability and interpretability?"
description: "Match NMF components across seeds and topic counts, retain instability, and verify every label against documents."
category: "Text analysis"
difficulty: "intermediate"
time: "75–120 min"
tags: [NMF, topic-modeling, stability, Jaccard, interpretation]
status: draft
---

# How do I test topic-model stability and interpretability?

<div class="answer-meta" markdown>
<span>Text analysis</span><span>intermediate</span><span>75–120 min</span>
</div>

## What you are trying to do

You have a set of NMF components that look interpretable. You want to know
whether related lexical patterns persist across random seeds and component
counts—and whether the documents support the labels you are tempted to assign.

!!! warning "Teaching boundary"
    Twelve short synthetic documents cannot establish general thematic
    structure. This deliberately unstable example teaches comparison and refusal,
    not substantive topic inference.

## You need

- the repository checkout or the
  [text and NLP validation packet](../../../assets/downloads/text-nlp-validation-v1.zip);
- a spreadsheet viewer or a Python environment for optional exploration;
- the conceptual distinctions in
  [Topics, sentiment and emotion](../../chapters/topics-emotions-classification.md).

Ordinary work uses frozen output. You do not need scikit-learn to complete the
lesson.

## Frozen design

The model run uses all twelve handbook-authored synthetic documents. The
TF-IDF vectorizer lower-cases text, uses the declared Slovene stop list, keeps
letter sequences of two or more characters, and sets `min_df=1`, `max_df=1.0`.
NMF uses random initialization, multiplicative updates, Kullback–Leibler loss,
up to 1,000 iterations, component counts 2, 3 and 4, and seeds 7, 19 and 31.
Eight top terms and three high-weight documents are retained per component.
Exact versions, corpus and stop-list hashes are in
`interim/topics/model-run.json`.

These permissive vocabulary settings are defensible only for showing instability
in a tiny dataset. A substantive study would require more documents, justified
frequency thresholds, segmentation tests and held-out interpretation.

## Inputs and outputs

| File | Role |
| --- | --- |
| `interim/topics/topic-components.csv` | terms, convergence and reconstruction information for every run |
| `interim/topics/topic-documents.csv` | three high-weight documents per component |
| `output/topic-stability.csv` | one-to-one topic matches across seeds within a component count |
| `output/topic-count-sensitivity.csv` | best-overlap links showing split/merge sensitivity across 2, 3 and 4 components |
| `reference/topic-interpretation.csv` | manually inspected passages, provisional labels and contradictions |

## Workflow

### 1. Verify the run grid

Run `make text-nlp-validation`, then group `topic-components.csv` by
`component_count` and `seed`. Confirm that every combination has exactly the
declared number of components. Do not compare component IDs across runs yet;
their numbering is arbitrary.

### 2. Match seeds under a fixed component count

For each count, the packet treats seed 7 as a reference run for alignment—not as
the true solution. It converts each component’s eight top terms to a set and
calculates Jaccard overlap with every component from seed 19 or 31:

```text
J(A, B) = |A ∩ B| / |A ∪ B|
```

It tests every one-to-one assignment and retains the assignment with the largest
total overlap; lexicographically smaller topic-ID sequences break exact ties.
Open `output/topic-stability.csv` and verify one intersection and union manually.
A row below the declared teaching threshold remains in the table as `unstable`.

### 3. Compare component counts

Topic counts are not commensurate one-to-one: a pattern can split or merge. The
count-sensitivity table therefore records the best top-term overlap from each
three-component, seed-7 component to every component in the two- and
four-component seed-7 runs. Multiple source components may select the same
destination. This is evidence of a merge, not a row to deduplicate.

List one apparent split, merge or disappearance. Check high-weight documents as
well as words. Lower reconstruction error at a larger count does not establish a
more valid humanistic interpretation.

### 4. Inspect documents and passages

Open `reference/topic-interpretation.csv`. For each three-component baseline,
read the named high-weight documents in `source/contemporary-sample.csv`, then
read the contradictory document. Compare the provisional label with the actual
passages.

The reference review deliberately refuses a clean authored-theme label because
components mix archive, museum, language, press and emotion cues. You may propose
another label, but cite document IDs and a contradictory passage. Do not label
from eight words alone.

### 5. Separate numerical and interpretive decisions

Create a short table with one row per reported pattern and these fields:

| Field | Question |
| --- | --- |
| overlap evidence | Do term sets and high-weight documents recur? |
| count sensitivity | Does the pattern split, merge or vanish? |
| source evidence | Which exact passages support the provisional label? |
| contradiction | Which passage weakens or changes it? |
| decision | report, report as unstable, or withhold |

A high overlap can preserve an uninterpretable component. A low overlap may
still expose a useful retrieval path. Neither condition names a historical
theme without reading.

### 6. Test one modelling choice

Predict what would happen if you changed segmentation, stop words, lemmatization,
`min_df`, or OCR correction. If you run a new model, save it as a candidate with
new metadata; do not overwrite the frozen run. Compare the full grid again rather
than reporting only the most attractive output.

## Optional model reproduction

Maintainers can install the pinned environment and run
`make text-nlp-validation-models`. The command writes to a new `.cache/`
directory and refuses replacement. Model generation is excluded from ordinary
CI; only reviewed frozen outputs and deterministic summaries are validated.

## Output

Write a stability note naming corpus, segmentation, vectorization, NMF settings,
seeds, counts, matching rule, overlap evidence, inspected document IDs,
contradictory passage and decision. Include unstable or unmatched patterns and
state that the tiny synthetic corpus cannot establish thematic structure.

## Check yourself

- Did you compare at least three seeds and three component counts?
- Did you match topics rather than compare their arbitrary IDs?
- Are low-overlap and duplicate destination matches still visible?
- Did you read complete synthetic documents and a contradiction?
- Did you keep numerical recurrence separate from interpretive validity?

## Common traps

- Calling a fixed seed evidence of stability.
- Selecting the component count from reconstruction error alone.
- Matching each source topic greedily and creating impossible duplicate matches
  within an equal-count run.
- Deleting unstable topics from the report.
- Treating authored theme metadata as a hidden answer key.
- Generalizing from a synthetic miniature to historical discourse.

## Practice task

Choose one baseline component. Trace its matches across both alternative seeds
and component counts, then write a 250-word interpretation that cites two
supporting passages and one contradiction. End with a report/unstable/withhold
decision and the additional corpus evidence needed to change it.
