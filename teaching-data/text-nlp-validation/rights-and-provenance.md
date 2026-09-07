# Rights and provenance

Provenance record updated: **7 September 2026**. This is not a human-review date
for the reference annotations.

## Handbook-authored contemporary sample

`source/contemporary-sample.csv` contains twelve texts written for this packet.
They are deliberately synthetic and carry `synthetic=true`. They do not report
real events, people or institutional practice. The handbook's original wording,
selection, annotations and documentation are offered under CC BY 4.0; original
code is offered under MIT, in accordance with the repository licence.

## Archival excerpts by reference

`source/extraction-registry.json` points to two files in
`teaching-data/archival-friction/`:

- `reference/reference-transcription.txt`, a handbook-created, manually checked
  transcription of a region in *Ilustrirani Slovenec*, 7 February 1925; and
- `raw/provider-ocr.txt`, the declared UTF-8 derivative of the byte-preserved
  dLib TXT export.

The builder extracts the sentence beginning `Tudi danes` from each file and
records source paths and SHA-256 values. It does not copy either passage into a
new `source/` layer. The generated `raw/annotation-samples.csv` is an exercise
derivative, not a second authentic provider export. Read the archival packet's
`SOURCE_CITATION.md`, `rights-and-provenance.md` and transcription policy before
reuse. Its dLib identifier is `URN:NBN:SI:doc-YPI8OFSU`.

## Model output

Frozen output in `interim/classla/` is generated annotation, not source
evidence. `interim/classla/model-run.json` records the CLASSLA package,
processors, resource manifest and model-file hashes, environment, command,
input hashes and output hashes. CLASSLA is distributed under Apache-2.0; its
models and upstream resources may have distinct licences. The packet does not
redistribute model files. Consult the CLASSLA repository and every downloaded
resource's metadata before redistribution or production use.

Frozen NMF output in `interim/topics/` was produced from the synthetic teaching
documents with scikit-learn, which is distributed under BSD-3-Clause. No
third-party corpus is included.

## Emotion material

`reference/teaching-emotion-lexicon.csv` is a tiny handbook-authored rule set.
It does not reproduce NRC or another external lexicon. This matters because the
NRC resource terms prohibit redistribution; users interested in that resource
must obtain it from its official page and assess the applicable licence.

## Reuse checklist

- Retain `synthetic=true` on all contemporary teaching documents.
- Cite the historical issue and distinguish provider OCR, reference
  transcription, the machine-assisted annotation draft and model output.
- Do not treat the draft annotation as a human-reviewed or neutral ground truth.
- Do not represent the frozen run as current model performance.
- Recheck package, model and external-resource licences before a new release.
