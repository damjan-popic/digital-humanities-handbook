# Data dictionary

The packet uses UTF-8, Unicode NFC and LF line endings. CSV files have one
header row and RFC 4180-style quoting. Stable identifiers begin `TNLP-`.
Generated files are sorted by their identifier fields; empty cells mean “not
applicable”, never an inferred zero.

## Source and extraction fields

| Field | Meaning |
| --- | --- |
| `doc_id` | Stable synthetic-document identifier |
| `title` | Handbook-authored display title |
| `theme` | Authored grouping used only for the dispersion exercise |
| `text` | Complete synthetic teaching document |
| `synthetic` | Literal `true` for every contemporary record |
| `rights_status` | Rights statement carried with the record |
| `sample_id` | Stable annotation-sample identifier |
| `stratum` | `contemporary_clean`, `historical_reference` or `provider_ocr` |
| `source_path` | Repository-relative path to the selected source layer |
| `source_record_id` | Stable identifier in the source packet |
| `selector` | Reproducible sentence selection rule |
| `source_sha256` | SHA-256 of the complete selected source file |
| `text_sha256` | SHA-256 of the normalized extracted text |

## CLASSLA evaluation fields

Reference and prediction files use CoNLL-U. `NER=B-PER` and related values are
stored in the MISC column because that is CLASSLA's serialized representation.
Multiword-token rows are retained in the reference, but syntactic metrics use
integer-ID word rows only.

| Field | Meaning |
| --- | --- |
| `layer` | Sentence, tokenization, lemma, UPOS, morphology, dependency or NER layer |
| `numerator` / `denominator` | Exact counts used to compute the reported measure |
| `metric` | Measure name; never compare percentages without its denominator |
| `value` | Decimal measure rounded to six places |
| `eligible_rule` | Which reference items entered the denominator |
| `alignment_status` | Exact token match, substitution, insertion or deletion |
| `reference_value` / `predicted_value` | Compared labels or structures |
| `error_family` | `source`, `segmentation`, `lexical`, `morphosyntactic`, `dependency`, `entity` or `ambiguity` |
| `interpretive_risk` | Research consequence that could follow if the error is ignored |

The manual files are a reviewed teaching reference. Their annotation policy and
documented disagreements are part of the data and must travel with the scores.

## Text-analysis, topic and emotion fields

`frequency-dispersion.csv` records token frequency, document frequency, the
share of all documents, Juilland's D across four equal authored theme groups,
and per-group counts. `concordance.csv` records bounded left and right context,
not a replacement for reading the document.

Topic files identify `component_count`, `seed`, `topic_id`, ranked `top_terms`,
top documents, a matched baseline topic, Jaccard overlap and a stability
decision. Topic numbers have no identity across runs until the matching step.

Emotion annotations distinguish whether emotion is contextually represented,
its category, experiencer, target, voice, negation, irony and uncertainty. The
baseline reports exact-form lexicon hits; it does not infer a person's mental
state. See `reference/emotion-codebook.md` for the decision rules.
