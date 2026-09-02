# Data dictionary

All CSV files use UTF-8, comma delimiters, a single header row and `\n` line
endings. Stable source-record identifiers begin with `AF-`; declared
synthetic interventions begin with `AF-SYN-`; unresolved-case identifiers
begin with `AF-U-`.

## Core metadata fields

These fields occur in `source/source-records.csv`, `metadata-raw.csv`,
`raw/messy-records.csv`, `metadata-clean.csv` and `cleaned/records.csv`.

| Field | Meaning and allowed values |
| --- | --- |
| `record_id` | Stable packet identifier for one issue or captioned feature. |
| `record_kind` | Modelled unit: `issue`, `captioned_feature`, `portrait` or `group_portrait`. |
| `page` | PDF page number or span, stored as text. |
| `label_transcribed` | Human transcription of the printed label under the packet policy. |
| `label_provider_ocr` | Corresponding wording in the embedded machine text layer. |
| `printed_date` | Date expression visible in the source; blank if none is printed. |
| `date_normalized` | ISO-like normalized value no more precise than the evidence. |
| `date_certainty` | `exact`, `derived_from_relative_date`, `approximate` or `unknown`. |
| `person_as_printed` | Name form visible in the selected caption. |
| `authority_candidate` | External identity candidate; blank when none is defensible. |
| `identity_status` | `unresolved`, `multiple_people` or `not_applicable` in this sample. |
| `source_locator` | Human-readable page and region within the committed PDF. |
| `evidence_note` | Reason for the normalized value, status or limitation. |
| `synthetic` | `true` only when a declared teaching perturbation affects the raw row. |

The source and clean tables contain the eight source-grounded records. The
raw table contains one additional synthetic duplicate and three synthetic
field changes. `metadata-raw.csv` is byte-identical to
`raw/messy-records.csv`; `metadata-clean.csv` is byte-identical to
`cleaned/records.csv`. The top-level copies provide the stable student-facing
names required by the lesson; the nested copies demonstrate layer roles.

## Synthetic perturbation fields

`source/synthetic-perturbations.csv` declares, but does not disguise, every
teaching change.

| Field | Meaning |
| --- | --- |
| `perturbation_id` | Stable `AF-SYN-` identifier. |
| `operation` | `set` for a field change or `duplicate` for an added row. |
| `target_record_id` | Authentic source-grounded record used by the exercise. |
| `new_record_id` | Identifier of the synthetic duplicate, otherwise blank. |
| `field` | Changed field for a `set` operation. |
| `synthetic_value` | Artificial value inserted into the raw layer. |
| `teaching_reason` | Why the disturbance is pedagogically useful. |

## Interim and decision fields

`interim/reconciliation-candidates.csv` is a generated review queue, not a
source of historical facts. It contains `candidate_id`, `record_id`, `field`,
`candidate_value`, `source_value`, `review_status` and `synthetic`.

`correction-log.csv` records `decision_id`, `record_id`, `field`,
`source_value`, `transformed_value`, `action`, `responsible`,
`decision_date`, `reason`, `confidence`, `reversible`, `source_provenance`
and `synthetic`. The compact compatibility file `cleaned/decisions.csv`
contains the same four decisions as `raw_value`, `clean_value`, `action` and
`evidence`.

`unresolved-cases.csv` contains `case_id`, `record_id`, `field`, `status`,
`current_value`, `reason` and `evidence_needed`. An unresolved case is an
auditable result, not an error to fill automatically.

## OCR evaluation fields

`output/ocr-evaluation.csv` has one row identified by `sample_id` and records
the normalization and tokenization rules, reference-character and reference-
word denominators, edit counts, CER and WER. Rates are decimal fractions,
not percentages.

`output/record-summary.csv` contains `measure` and `value` pairs derived from
the clean and raw tables. `validation/expected-results.json` stores the
expected counts and source digest in machine-readable form.
