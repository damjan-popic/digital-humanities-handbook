# Text and NLP validation teaching packet

Research question: how do linguistic and text-analytic conclusions differ
across two small synthetic contemporary examples and two textual realizations
of one historical passage—a reference transcription and corresponding provider
OCR?

This bilingual packet connects handbook chapters 9–11 to inspectable evidence.
It contains twelve short, handbook-authored contemporary documents; declared
extractions from the existing archival-friction packet; a machine-assisted
reference-annotation draft pending human review; frozen CLASSLA output; a small
frequency, document-frequency and dispersion exercise; and bounded topic and
emotion exercises.
The contemporary documents are synthetic teaching material, not evidence about
real institutions or events.

## Layers

| Layer | Role | Rule |
| --- | --- | --- |
| `source/` | Authored teaching corpus and extraction registry | Preserve; the registry points to archival material rather than copying it here |
| `reference/` | Machine-assisted annotation, codebooks and interpretation drafts | Treat as pending human review, never as unmediated truth |
| `raw/` | Deterministic extracted inputs | Rebuild; do not hand-edit |
| `interim/` | Frozen CLASSLA and NMF model outputs | Preserve as run evidence; refresh only with the optional model command and review |
| `output/` | Layer metrics, error log, concordances and analytic tables | Rebuild with the standard library |
| `validation/` | Expected values and SHA-256 manifest | Rebuild after an approved source or model change |
| `known-problems/` | Deliberately open limits | Extend when a new limit is found |

## Student route

1. Read `rights-and-provenance.md` and `data-dictionary.md`.
2. Compare the three strata in `raw/annotation-samples.csv` with the draft
   reference and frozen CLASSLA tables.
3. Recalculate one layer-specific denominator in
   `output/classla-evaluation.csv`, then trace two errors to
   `output/classla-error-log.csv` and the source text.
4. Use `output/frequency-dispersion.csv` and `output/concordance.csv` to explain
   why total frequency, document frequency and dispersion answer different
   questions.
5. Inspect topic matches across seeds and component counts before reading the
   deliberately cautious interpretation table.
6. Compare the transparent emotion-word baseline with the contextual draft
   labels pending human review. Identify the experiencer, target, quotation,
   negation and irony.

The student exercise needs no model download. Download
`text-nlp-validation-v1.zip` from the handbook page or inspect this source tree.

## Maintainer commands

Ordinary validation uses only Python's standard library and the committed model
outputs:

```bash
make text-nlp-validation
make check
```

Model regeneration is intentionally separate because it downloads large
resources:

```bash
python3.12 -m venv .venv-text-nlp
source .venv-text-nlp/bin/activate
python -m pip install -r teaching-data/text-nlp-validation/requirements-text-nlp.txt
make text-nlp-validation-models
```

The model command writes candidates to a new `.cache/` directory and refuses to
overwrite committed evidence. Compare candidate bytes and metadata, review every
changed annotation or topic, and only then replace the frozen files in a separate
editorial commit. Never commit the model cache.

The frozen runs point to `interim/model-environment.json` and its complete
`pip freeze --all` lock. CLASSLA resource acquisition is recorded separately in
`interim/classla/resource-acquisition.json`: the file manifest is known, while
the original acquisition time remains explicitly `unknown`.

## Interpretation boundary

The annotation sample is purposive and tiny; it diagnoses errors but estimates
neither CLASSLA's general performance nor a population parameter. The topic
models operate on twelve short synthetic documents and are a stability
demonstration, not evidence that the themes exist in a historical corpus. The
emotion lexicon is an original miniature teaching baseline, not a Slovene
emotion resource. Human methodological and Slovene-language review remain
pending.
