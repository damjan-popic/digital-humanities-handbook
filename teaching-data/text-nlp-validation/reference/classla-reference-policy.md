# CLASSLA reference-annotation policy

The four CoNLL-U files are a manually reviewed teaching reference, version
`TNLP-REF-1`. They support an inspectable comparison with one frozen CLASSLA
run; they do not establish universal linguistic truth or population-level
model performance.

## Decisions

1. Preserve the selected sentence, case and punctuation. Do not silently
   replace provider OCR with the reference transcription.
2. For clean and reference-transcription samples, annotate the reading present
   in that layer. For provider OCR, retain observed forms but annotate a
   facsimile-checked research-intended word boundary or lemma when the existing
   archival packet documents an evident recognition error.
3. Record joined OCR `narodain` as the CoNLL-U multiword token `naroda` + `in`.
   Retain `stavovske`, `kultrunega` and `i` as observed FORM values while
   assigning the source-grounded lemmas `stanovski`, `kulturen` and `ki`.
4. Treat substantival `vse` in `zato gre vse` as `PRON`, lemma `ves`, and the
   subject of `gre`. This is an explicit reviewer decision, not a hidden fix.
5. Retain debatable CLASSLA analyses when the sample alone does not justify a
   stronger claim. Dependency and historical-lemma disagreements therefore
   remain possible even after review.

One maintainer performed the review on 7 September 2026. There is no independent
double annotation or adjudication. Reuse must report that limitation and cite
both this policy and the layer-specific denominators.
