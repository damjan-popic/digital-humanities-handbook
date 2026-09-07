---
reference_status: machine-assisted reference draft; pending human review
reference_version: TNLP-REF-2
---

# CLASSLA reference-annotation policy

The four CoNLL-U files are a machine-assisted reference draft, version
`TNLP-REF-2`, pending competent human review. They support an inspectable
comparison with one frozen CLASSLA run; they do not establish universal
linguistic truth or population-level model performance.

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
4. In `s Slovensko ljudsko stranko`, attach `stranko` to the second `gre` as
   `obl` (token 34 in `TNLP-AF-REF`; token 33 in `TNLP-AF-OCR`). Attaching it
   to `naziranja` as `nmod` changes the clause-level reading.
5. Treat substantival `vse` in `zato gre vse` as `PRON`, lemma `ves`, and the
   subject of `gre`. This remains a contestable draft decision, not a hidden
   correction or a human-adjudicated label.

## Draft inspection and unresolved analyses

All four files—`TNLP-CLEAN-01`, `TNLP-CLEAN-02`, `TNLP-AF-REF` and
`TNLP-AF-OCR`—were inspected line by line during the machine-assisted editorial
correction that produced `TNLP-REF-2`; none received competent human review.
The clean examples retain contestable analyses of the occupational title plus
personal name (`Kustosinja Maja Kovač`) and shared subject in coordinated verbs.
The historical examples retain open questions about substantival `vse`, the
discourse/syntactic role of `zato`, and the annotation of OCR form `i` as the
source-grounded relative `ki`. These decisions must be checked against the
declared annotation guidelines by a qualified reviewer.

To promote the draft to `human-reviewed`, record a named reviewer, an ISO review
date, the reviewed files/layers as review scope, disagreements and any adjudication.
Until all four fields exist, keep `reference_status` as `machine-assisted
reference draft; pending human review`. Reuse must report this limitation and
cite both this policy and the layer-specific denominators.
