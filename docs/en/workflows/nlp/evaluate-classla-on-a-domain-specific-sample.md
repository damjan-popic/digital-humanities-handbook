---
title: "How do I evaluate CLASSLA on a domain-specific sample?"
description: "Audit sentence, token, lemma, morphology, dependency and entity predictions against a documented Slovene reference sample."
category: "NLP"
difficulty: "intermediate"
time: "60–90 min"
tags: [CLASSLA, Slovene, validation, CoNLL-U, error-analysis]
status: draft
---

# How do I evaluate CLASSLA on a domain-specific sample?

<div class="answer-meta" markdown>
<span>NLP</span><span>intermediate</span><span>60–90 min</span>
</div>

## What you are trying to do

You want to know whether linguistic annotation is usable for one humanities
question, not whether a pipeline has a good reputation in general. You will
compare one frozen CLASSLA run with a machine-assisted Slovene reference draft
that is pending human review, across
clean contemporary text, a historical transcription and provider OCR. You will
report a separate denominator for each layer and connect errors to their likely
effect on interpretation.

!!! quote "One-sentence version"
    Evaluate the exact layer your claim uses, on material that represents its
    difficulty, and read the errors before trusting the score.

This is a diagnostic exercise. Four selected sentences cannot estimate general
CLASSLA performance.

## You need

- the repository checkout or the
  [text and NLP validation packet](../../../assets/downloads/text-nlp-validation-v1.zip);
- Python 3.12 for rebuilding deterministic tables;
- a spreadsheet viewer or text editor;
- familiarity with the layers in
  [Linguistic annotation and CLASSLA](../../chapters/linguistic-annotation-classla.md).

You do **not** need to install CLASSLA or download its models. The packet includes
frozen output and exact run metadata.

## Inputs and outputs

| Role | File | Why it matters |
| --- | --- | --- |
| extraction rules | `source/extraction-registry.json` | identifies source layer, record and sentence selector |
| research inputs | `raw/annotation-samples.csv` | records normalized text and source/input hashes |
| reference draft | `reference/classla/*.conllu` | states contestable machine-assisted decisions pending human review |
| causal decisions | `reference/classla-causal-decisions.csv` | separates immediate disagreement from likely causal origin across source layers |
| model predictions | `interim/classla/*.conllu` | preserves the frozen run unchanged |
| run identity | `interim/classla/model-run.json` | names package, processors, environment, resources and hashes |
| measures | `output/classla-evaluation.csv` | exposes numerator, denominator and eligible set per layer |
| disagreements | `output/classla-error-log.csv` | connects label differences to error family and risk |

Read `rights-and-provenance.md`, `data-dictionary.md` and
`reference/classla-reference-policy.md` before interpreting the tables.

## Workflow

### 0. Write a stratified sample and decision plan

Before opening model output, define the research operation, required layers,
sampling frame and likely difficulty strata. State target counts for genre,
period, source condition, code-switching, non-standard language, abbreviations
and names where relevant. Define how references are reviewed, how disagreement
and unresolved cases are stored, and which downstream count will be recalculated.

Pre-register a pass, conditional-pass or fail rule tied to the claim. For
example, a speaker-retrieval study might fail if any sampled subject error changes
group ranking, pass conditionally if every candidate is manually reviewed, and
pass for exploratory retrieval if recall is adequate under a declared threshold.
Do not invent a universal CLASSLA threshold.

### 1. Rebuild without downloading models

From the repository root, run:

```bash
make text-nlp-validation
```

The command uses the Python standard library. It extracts declared passages,
checks frozen hashes, calculates outputs, packages the student ZIP and verifies
the checksum. A changed source, model artifact or expected value should make the
command fail visibly rather than update evidence silently.

### 2. Audit the source contrast

Open `raw/annotation-samples.csv`. Confirm that the two contemporary rows are
marked synthetic. The historical transcription and provider OCR point to two
different files but share the archival record identifier. They are two textual
layers of one newspaper passage, not two documents.

Compare the historical texts character by character. Record the joined form
`narodain`, the damaged forms `stavovske` and `kultrunega`, and relative `i` in
the OCR. Do not correct the raw row. The reference policy explains which FORM
values remain observed and which word boundary or lemma is annotated according
to the checked transcription.

### 3. Identify the frozen run

Open `interim/classla/model-run.json` and answer:

- Which CLASSLA and Python versions produced the files?
- Which processors ran, and was a GPU used?
- Which hashes identify the normalized inputs and outputs?
- Which hashes and byte counts identify local model resources, and when was the
  resource manifest recorded?
- Which environment snapshot identifies Python, Torch, NumPy, SciPy,
  scikit-learn, CLASSLA, Stanza and Obeliks?

The metadata identifies one run. It does not turn a model prediction into a
reference label or prove that future installations behave identically.

### 4. Inspect one sentence before calculating

Place `reference/classla/TNLP-AF-OCR.conllu` beside
`interim/classla/TNLP-AF-OCR.conllu`. Ignore comment lines temporarily and read
the ten CoNLL-U columns. Find the reference multiword token `27-28 narodain` and
its components. Then find `i`: compare FORM, LEMMA, UPOS, HEAD and DEPREL.

Return to the sentence text. Explain in prose how a recognition error becomes a
lexical and dependency disagreement. This step prevents a metric from becoming
detached from the source.

### 5. Recalculate one layer denominator

Open `output/classla-evaluation.csv`. Select one sample and layer. Verify:

```text
value = numerator / denominator
```

Use the `eligible_rule` column to explain what entered the denominator. Lemma,
UPOS and morphology use one-to-one aligned word tokens. Dependency scores use
aligned syntactic words whose reference heads can also be aligned. NER precision
and recall deliberately use different denominators. Token insertions and
deletions are not allowed to disappear inside another layer’s percentage.
Use the explicit reference, predicted, aligned, substituted, inserted, deleted
and excluded counts to reconcile the denominator. `excluded` is never a generic
remainder: each side and its exclusion rule are reported separately.

The corrected dependency rows should read:

| Sample | UAS | LAS |
| --- | ---: | ---: |
| `TNLP-CLEAN-01` | 11/11 | 11/11 |
| `TNLP-CLEAN-02` | 9/9 | 9/9 |
| `TNLP-AF-REF` | 50/52 | 50/52 |
| `TNLP-AF-OCR` | 43/46 | 42/46 |

Treat these as agreement with the current machine-assisted draft, not an
accuracy estimate against a human-adjudicated reference.

### 6. Read the error log by family

Filter `output/classla-error-log.csv` by `sample_id`, then by `error_family`.
For two rows, write a four-part note:

1. source form and layer;
2. reference and predicted values;
3. immediate model/reference disagreement;
4. likely causal origin, including whether it also occurs in the reference
   transcription; and
5. research operation that could change.

Distinguish a source-recognition error from the tagger’s response to it. If your
claim concerns only exact location spans, a lemma disagreement may be irrelevant.
If it concerns clause subjects, the same passage’s dependency disagreement is
central.
Use `reference/classla-causal-decisions.csv` to verify recurring cases across
the transcription and OCR strata. A disagreement that appears in both layers,
such as the five `vse` fields in each historical sample, is not caused by OCR.
The regenerated log contains 24 disagreements: 14 matched cross-layer cases
(ten `vse` fields and four `stranko` dependency fields) and ten cases conditioned
by the provider OCR.

### 7. Compare strata without overclaiming

Group the evaluation rows by `stratum`. You may describe which disagreements
occur in these selected clean, historical and OCR samples. You may not infer an
average error rate for contemporary or historical Slovene. The sample is small,
purposive and partly selected to reveal failure.

Formulate a bounded decision such as: “For this query, manually review all
subject relations in provider OCR before aggregation.” Name the validation that
would be required to generalize it.

### 8. Apply the planned decision and retain unresolved cases

Use `output/downstream-consequences.csv` to compare one automatic and reference
count, then apply the rule from step 0. Record `pass`, `conditional_pass` or
`fail`, the observed counts, required intervention and scope. Add an unresolved
table with sample ID, source locator, layer, competing analyses, evidence needed
and whether the case is excluded, reviewed manually or carried into uncertainty.
A small denominator or genuine linguistic disagreement is not converted to a
confident label simply to complete the exercise.

## Optional maintainer-only model refresh

Model regeneration is separate from the lesson because it downloads large
resources and can change across releases:

```bash
python3.12 -m venv .venv-text-nlp
source .venv-text-nlp/bin/activate
python -m pip install -r teaching-data/text-nlp-validation/requirements-text-nlp.txt
make text-nlp-validation-models
```

The command writes a new candidate under `.cache/` and refuses to overwrite the
committed run. A maintainer must compare metadata and annotations, review every
change, and update expected values deliberately. Ordinary CI never downloads
models.

## Output

Produce a short validation note containing the stratified sample plan, frozen
run identifier, one verified layer denominator, two source-linked error analyses,
the recalculated downstream consequence, the pass/conditional-pass/fail decision
and an unresolved-cases table. End with one bounded claim and the conditions
under which it must be reviewed again. Keep the packet outputs unchanged unless
you are performing a documented maintainer refresh.

## Check yourself

You have completed the workflow when you can:

- trace every sample to a source path and SHA-256 value;
- state why the machine-assisted reference draft remains contestable and pending
  human review;
- recompute one reported value from its explicit counts;
- explain why dependency and NER denominators differ;
- connect two errors to concrete interpretive risks; and
- state a conclusion that remains inside the sample’s limits.

## Common traps

- Comparing percentages while ignoring unequal or tiny denominators.
- Calling OCR damage a CLASSLA error, or ignoring how the model propagates it.
- Scoring only tokens that align easily without reporting exclusions.
- Treating token-level `O` labels as evidence of strong entity recognition.
- Replacing the frozen run during an ordinary lesson or CI job.
- Correcting the source layer silently instead of recording another text layer.
- Generalizing from four purposive sentences to a language, period or genre.

## Practice task

Design a 30-sentence reference sample for your own question. Specify strata,
sampling rule, required annotation layers, reviewer guidance, disagreement
procedure, metrics, denominators and the decision each result would trigger.
Write one ethical or licensing limit and one reason the sample could still be
unrepresentative.
