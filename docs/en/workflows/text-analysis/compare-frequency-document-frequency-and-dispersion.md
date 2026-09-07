---
title: "How do I compare frequency, document frequency and dispersion?"
description: "Use an uneven Slovene teaching corpus to distinguish repetition, document reach and distribution across corpus parts."
category: "Text analysis"
difficulty: "beginner"
time: "45–75 min"
tags: [frequency, document-frequency, dispersion, concordance, Slovene]
status: draft
---

# How do I compare frequency, document frequency and dispersion?

<div class="answer-meta" markdown>
<span>Text analysis</span><span>beginner</span><span>45–75 min</span>
</div>

## What you are trying to do

You have several documents and want to distinguish three claims: how often a
term occurs, how many documents use it, and how evenly it is distributed across
meaningful corpus parts. You will audit concordances before interpreting the
numbers.

!!! quote "One-sentence version"
    Frequency measures repetition, document frequency measures reach, and
    dispersion measures concentration under a declared partition.

## You need

- the repository checkout or the
  [text and NLP validation packet](../../../assets/downloads/text-nlp-validation-v1.zip);
- Python 3.12 if you rebuild the supplied tables;
- a spreadsheet viewer or text editor; and
- the concepts in [Text analysis](../../chapters/text-analysis.md).

The twelve documents are synthetic teaching texts. They are intentionally
uneven and are not evidence about real institutions, genres or Slovene usage.

## Inputs and outputs

| File | Role |
| --- | --- |
| `source/contemporary-sample.csv` | twelve source documents with stable IDs, authored theme and rights status |
| `output/document-summary.csv` | eligible token totals by document |
| `output/frequency-dispersion.csv` | frequency, DF, document share, Juilland’s D and four group counts |
| `output/concordance.csv` | every matched occurrence with bounded context |
| `validation/expected-values.json` | selected invariant counts used by the checker |

The deterministic builder lower-cases Unicode-NFC text and extracts sequences of
letters of length two or more. It does not lemmatize. The four authored theme
groups—archives, museums, language and press—each contain three documents, so
the classroom Juilland calculation uses equal parts.

## Workflow

### 1. Rebuild the tables

From the repository root, run:

```bash
make text-nlp-validation
```

This command checks inputs and frozen artifacts before writing generated tables.
No NLP model is installed or downloaded.

### 2. Inspect the documents before the aggregate

Open `source/contemporary-sample.csv` and `output/document-summary.csv`. Confirm
that every row has a stable `doc_id`, a theme, `synthetic=true`, a rights
statement and a token denominator. Sort by token count. Ask whether the longest
document could dominate a raw count.

Document boundaries here are authored for the exercise. In your research they
might be articles, letters, books, issues or speeches; changing the boundary
changes DF even when the characters stay identical.

### 3. Compare three contrasting terms

In `output/frequency-dispersion.csv`, locate `arhiv`, `korpus` and `svoboda`.
For each term, record:

- total frequency;
- normalized frequency per 10,000 eligible tokens;
- document frequency and document share;
- counts in the four theme groups; and
- Juilland’s D.

Do not rank the terms by a single column. State the question each column answers.
A repeated word can have high frequency but low DF; a term can reach several
documents yet remain confined to one theme group.

### 4. Verify frequency and DF manually

Filter `output/concordance.csv` to one term. Count rows to reproduce token
frequency. Count distinct `doc_id` values to reproduce DF. Then verify:

```text
document_share = document_frequency / 12
normalized_frequency = frequency / all_eligible_tokens * 10,000
```

The two formulas have different denominators. Writing “the term occurs in 16.7%
of the corpus” is ambiguous: it might mean documents, tokens or bytes. Name the
unit.

### 5. Recalculate dispersion

Take the four theme counts for one non-zero term. Calculate their mean and
population standard deviation, then:

```text
D = 1 - (population_standard_deviation / mean) / sqrt(4 - 1)
```

Compare your value with the six-decimal value in the table. If all occurrences
are in one theme, D is 0. If group counts are equal, D is 1. A middle value has
meaning only together with the four counts.

Do not reuse this simple formula when corpus parts differ in size. Choose a
measure that accounts for part size or calculate document-level distributions.

### 6. Read every concordance line

For the three terms, inspect `left_context`, `match` and `right_context`. Open the
complete document if speaker, negation or argument extends beyond the window.
Classify each occurrence as relevant, ambiguous or irrelevant to a question you
define. Your classification is a new annotation layer; document its rule.

Check whether repeated uses come from a deliberate contrast, a list, a title or
formulaic language. Frequency alone cannot tell you.

### 7. Test one alternative

Repeat the reasoning under one changed choice: exact case instead of lower-case,
lemma instead of form, document instead of theme dispersion, or one occurrence
per document. You need not recalculate the entire packet. Predict which values
would change and verify a small sample.

The aim is to locate sensitivity. Do not choose the transformation that makes
your preferred narrative look strongest.

## Output

Write a short evidence note containing:

- corpus and tokenization definition;
- term, query form and source layer;
- raw and normalized frequency with denominator;
- DF and document denominator;
- named dispersion measure, partition and per-part counts;
- one concordance-supported interpretation;
- one contradictory or ambiguous context; and
- one limit on generalization.

## Check yourself

- Can another reader reconstruct each denominator?
- Does frequency equal the number of concordance rows?
- Does DF equal the number of distinct document IDs?
- Is D accompanied by the partition and group counts?
- Did you describe only the synthetic dataset rather than Slovene discourse?

## Common traps

- Calling a frequent term widespread without checking DF.
- Calling a high-DF term evenly dispersed without inspecting group counts.
- Comparing normalized rates that use different eligible-token rules.
- Treating an arbitrary file boundary as a historical document boundary.
- Reading a KWIC window as if it contained the whole argument.
- Applying equal-part Juilland’s D to strongly unequal corpus parts.

## Practice task

Choose two additional terms from the table with similar frequency but different
DF or dispersion. Explain the difference with concordances. Then design a
comparable real-corpus sample and list the metadata, OCR checks and rights review
required before repeating the calculation.
