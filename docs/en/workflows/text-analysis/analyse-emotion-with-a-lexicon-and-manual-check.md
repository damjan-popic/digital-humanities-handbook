---
title: "How do I analyse emotion with a lexicon and a manual check?"
description: "Compare transparent word associations with contextual labels for experiencer, target, voice, negation and irony."
category: "Text analysis"
difficulty: "intermediate"
time: "75–120 min"
tags: [emotion, lexicon, attribution, quotation, negation, irony, validation]
status: draft
---

# How do I analyse emotion with a lexicon and a manual check?

<div class="answer-meta" markdown>
<span>Text analysis</span><span>intermediate</span><span>75–120 min</span>
</div>

## What you are trying to do

You want to compare an inspectable lexical signal with a contextual claim about
emotion. You will preserve who is represented as experiencing emotion, what it
targets, whose voice carries the words, and whether negation or irony blocks the
literal reading. You will keep zero matches, false positives, false negatives and
unresolved cases visible.

!!! quote "One-sentence version"
    A word can be associated with emotion without proving that the author,
    speaker, narrator or anyone else experiences it.

## You need

- the repository checkout or the
  [text and NLP validation packet](../../../assets/downloads/text-nlp-validation-v1.zip);
- a spreadsheet viewer and optionally Python 3.12;
- the distinctions in
  [Topics, sentiment and emotion](../../chapters/topics-emotions-classification.md).

All eight sentences are synthetic and link to stable `doc_id` and
`sentence_index` values in `source/contemporary-sample.csv`. They are designed to
expose method behavior, not to represent historical emotion.

## Lexicon provenance and rights

`reference/teaching-emotion-lexicon.csv` contains eight exact Slovene surface
forms written for this handbook under its CC BY 4.0 text licence. It is a
deliberately incomplete teaching rule set, not a language resource. It does not
copy NRC or another third-party lexicon. The packet therefore redistributes no
external lexicon whose terms forbid redistribution.

The category `fear` deliberately groups worry and fear for the exercise. Each row
is marked synthetic and carries a scope and note. Reuse must retain this
provenance and must not advertise the list as validated Slovene coverage.

## Inputs and outputs

| File | Role |
| --- | --- |
| `reference/teaching-emotion-lexicon.csv` | original exact-form baseline |
| `reference/emotion-sensitivity-additions.csv` | one documented post-baseline form for sensitivity analysis |
| `reference/emotion-annotations.csv` | machine-assisted contextual reference draft, pending human review, with source locators |
| `reference/emotion-codebook.md` | rules for presence, experiencer, target, voice and uncertainty |
| `output/emotion-baseline.csv` | matches, draft reference label and TP/FP/TN/FN outcome per sentence |
| `output/emotion-sensitivity.csv` | baseline versus one-entry extension comparison |
| `output/emotion-method-comparison.csv` | unit, representation, evidence and claim boundaries |

## Workflow

### 1. Define the claim before matching

Choose one unit and target. This exercise asks whether a sentence contextually
represents a coarse emotion for a recoverable experiencer. It does not classify
general polarity, narrator stance or reader response. A sentence can perform
negative evaluation while receiving `emotion_present=false`.

Read `reference/emotion-codebook.md`. Note that `uncertain=true` preserves a
judgement rather than forcing confidence. The labels are a machine-assisted
reference draft pending human review; no named reviewer, completed review date,
review scope or inter-annotator agreement estimate is available.

### 2. Rebuild the transparent baseline

Run:

```bash
make text-nlp-validation
```

The standard-library builder uses Unicode NFC, lower-cases for lookup and matches
declared surface forms exactly. It records every matched form and category. One
or more matches predict `emotion_present=true`; zero matches predict false. The
rule neither lemmatizes nor resolves negation, voice or irony.

### 3. Trace source-linked examples

Open `reference/emotion-annotations.csv` and locate these stable records:

- `TNLP-E03` → `TNLP-C06`, sentence 1: fear is attributed to *obiskovalci*
  inside quoted speech; it is not the reporter’s emotion.
- `TNLP-E05` → `TNLP-C06`, sentence 3: *jeza* is a metalinguistic mention, and
  negation rejects the inference that it belongs to the report’s author.
- `TNLP-E07` → `TNLP-C12`, sentence 1: sadness is negated while worry is
  attributed to the editor and targeted at a missing source.
- `TNLP-E08` → `TNLP-C12`, sentence 2: quoted *čudovito* is ironic negative
  evaluation; a discrete emotion remains unresolved.

For each, find the same sentence in `source/contemporary-sample.csv`. Confirm the
experiencer, target, `voice`, `quotation`, `negation`, `irony`, `uncertain` and
rationale fields. Do not infer an author’s psychology from these authored lines.

### 4. Find a zero match and false negative

In `output/emotion-baseline.csv`, find `TNLP-E06`. The sentence represents fear
attributed to townspeople with the surface form *bali*, but the exact-form
lexicon includes *bojijo*, not *bali*. It therefore has zero matches and becomes
a false negative under the binary presence rule.

This is evidence about the matching policy. It does not show that *bali* is
emotionally unambiguous in every context or that adding a lemma solves the task.

### 5. Read false positives

Inspect at least these rows:

- `TNLP-E04`: *čudovita* matches joy, but the sentence is ironic and does not
  safely license a discrete emotion.
- `TNLP-E05`: two occurrences of *jeza* match anger, but the sentence discusses
  attribution and explicitly blocks the author inference.
- `TNLP-E08`: quoted *čudovito* matches joy, while the draft reference label
  leaves emotion absent and the ironic reading uncertain.

A binary confusion outcome simplifies richer disagreements. Retain match lists,
draft-reference rationale and uncertainty beside TP/FP/TN/FN rather than treating the
acronym as a complete interpretation.

### 6. Compare expressed and attributed emotion

Contrast `TNLP-E02`, where the narrator explicitly describes the curator as
enthusiastic, with `TNLP-E03` and `TNLP-E06`, where reporting constructions
attribute fear to visitors or townspeople. Identify the grammatical or discourse
cue that recovers the experiencer. Then identify the target: a restored poster,
closure of a collection or change.

Do not transfer emotion from quoted speaker to reporter, from character to author
or from lexical item to reader response. If the experiencer or target cannot be
supported, use `unresolved`.

### 7. Run the sensitivity comparison

`reference/emotion-sensitivity-additions.csv` adds only the surface form *bali*
to the baseline. Compare `output/emotion-sensitivity.csv` for
`baseline_exact_form` and `add_documented_bali_form`.

The added form repairs the known false negative in this sample. It does not fix
false positives from negation, metalinguistic mention or irony. This is the gain
and loss of one lexicon change: recall can improve while contextual validity does
not. A true lemma-based variant would require documented lemmatization and its
own error audit.

Because the addition was designed after examining the baseline errors, the
improved value is development evidence. It must be tested on new material before
being reported as expected performance.

### 8. Write a bounded method comparison

Use `output/emotion-method-comparison.csv`. For lexical matching and contextual
reference annotation, report unit, input representation, output, validation evidence,
supported and unsupported claim, gain, loss and known failure. The packet does
not fit a supervised classifier: eight purpose-built cases cannot support
train/validation/test separation. That omission is a methodological decision,
not missing decoration.

## Output

Prepare an evidence note containing lexicon provenance and rights, exact matching
rule, confusion counts with denominators, one zero match, one false positive, one
false negative, one quoted or attributed case, one negated case, an unresolved
irony, source IDs, sensitivity result and a supported claim. End with an
unsupported claim about inner state or population prevalence.

## Check yourself

- Can you trace every label to a stable document and sentence?
- Did you name the experiencer, target and voice separately?
- Are quotation, negation and irony explicit fields rather than impressions?
- Are zero-match, FP and FN cases retained?
- Did you preserve the micro-lexicon’s original rights and limited purpose?
- Did you avoid claiming supervised performance from eight sentences?

## Common traps

- Calling every lexical association an expressed emotion.
- Assigning quoted fear to the reporter or author.
- Allowing negated sadness to count as experienced sadness.
- Converting ironic negative evaluation into an invented discrete emotion.
- Improving the lexicon on evaluation examples and reporting the same cases as a
  fair test.
- Copying a third-party lexicon without checking redistribution terms.

## Practice task

Write four new synthetic sentences: one explicit emotion, one attribution, one
negation and one unresolved irony. Add stable IDs and provenance. Have another
reader apply the codebook without seeing your intended labels, retain the
disagreement, and test both lexicon variants. Explain which error would matter
most for your own research question.
