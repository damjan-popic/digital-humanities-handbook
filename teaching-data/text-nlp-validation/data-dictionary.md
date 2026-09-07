# Data dictionary

The packet uses UTF-8, Unicode NFC and LF line endings. CSV files have one
header row and RFC 4180-style quoting. Stable identifiers begin `TNLP-`.
Generated tables use a documented deterministic ordering appropriate to their
contents: for example, error records follow their identifiers, while frequency
output is ordered by descending frequency, with terms in ascending order to
break ties.

The meaning of an empty value is field-specific: it can mean “not applicable”,
an undefined measure (such as a rate with denominator zero), or pending
human-review metadata (reviewer, date or scope). An empty field must never be
interpreted automatically as numeric zero.

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
| `alignment_unit` | Sentence text, word FORM or typed entity span used for accounting |
| `reference_item_count` / `predicted_item_count` | Total items on each side before alignment/exclusion |
| `aligned_reference_items` / `aligned_predicted_items` | Items admitted by the declared prerequisite alignment |
| `substitutions` / `insertions` / `deletions` | Explicit alignment operations in the named unit |
| `excluded_reference_items` / `excluded_predicted_items` | Side-specific items excluded from downstream scoring |
| `exclusion_rule` | Reason those items do not enter the layer score |
| `alignment_status` | `equal_form` (exact word-form match), `substitution`, `insertion`, `deletion` or `aligned_span` (entity-span alignment), where applicable; the applicable values depend on the alignment unit or layer |
| `reference_value` / `predicted_value` | Compared labels or structures |
| `error_family` | `segmentation`, `lexical`, `morphosyntactic`, `dependency`, `entity` or `ambiguity` |
| `input_stratum` | Source condition; never treated as a causal conclusion by itself |
| `immediate_disagreement` | Direct alignment/label contrast before causal interpretation |
| `likely_causal_origin` | Machine-assisted causal draft from the explicit decision table |
| `also_occurs_in_reference_transcription` | Whether the same form/layer disagreement is present without provider OCR |
| `review_status` | Current provenance state of the causal/reference decision |
| `reviewer` / `reviewed_on` / `review_scope` | Blank while review is pending; required name, ISO date and scope for a future `human-reviewed` state |
| `interpretive_risk` | Research consequence that could follow if the error is ignored |

The reference files are a machine-assisted draft pending competent human review.
Their annotation policy, causal-decision table and documented disagreements are
part of the data and must travel with the scores. `validation/expected-values.json`
also carries the current status and the reviewer/date/scope fields required for
any later `human-reviewed` state.

## Text-analysis, topic and emotion fields

`frequency-dispersion.csv` records token frequency, document frequency, the
share of all documents and Gries's DP across four authored theme groups. The
groups contain 83, 68, 66 and 113 eligible tokens, so each row publishes those
part sizes and its per-part term counts. For total frequency (F>0), part token
total (N_i), corpus total (N), and part term count (f_i):

```text
DP = 0.5 * sum_i(abs(f_i / F - N_i / N))
```

DP is undefined when `F=0`; lower values indicate a distribution closer to the
part-size expectation and larger values greater concentration. `concordance.csv`
records bounded left and right context, not a replacement for reading the
document.

Topic files identify `component_count`, `seed`, `topic_id`, ranked `top_terms`,
top documents, a matched baseline topic, Jaccard overlap and a stability
decision. Topic numbers have no identity across runs until the matching step.
Interpretations use stable sentence IDs such as `TNLP-C11.s1`; the builder
requires each ID and every high-weight/contradictory document to resolve to the
source corpus.

Emotion annotations identify a source sentence only by `doc_id` and
`sentence_index`; generated output resolves and carries the exact source text so
a duplicate cannot drift. They distinguish whether emotion is contextually represented,
its category, experiencer, target, voice, negation, irony and uncertainty. The
baseline reports exact-form lexicon hits; it does not infer a person's mental
state. See `reference/emotion-codebook.md` for the decision rules.

`interim/model-environment.json` and `model-environment.lock.txt` identify the
actual optional-run environment. `interim/classla/resource-acquisition.json`
keeps the resource-file inventory separate from the inference timestamp and
uses `unknown` because the former runner did not preserve a recoverable
acquisition time.
