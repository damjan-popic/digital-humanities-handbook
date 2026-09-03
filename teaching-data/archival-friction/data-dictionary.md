# Data dictionary

All CSV files use UTF-8, comma delimiters, one header row and `\n` line
endings. Stable observations begin `AF-`; source-grounded editorial decisions
begin `AF-ED-`; synthetic interventions begin `AF-SYN-`; unresolved cases
begin `AF-U-`; OCR audit rows begin `AF-OCR-A`.

## Layers and exercises

`source/` contains preserved provider material: the unchanged historical PDF,
captured dLib and Commons records, and the byte-preserved dLib TXT export.
The export retains its original CRLF bytes and is decoded as Windows-1250 by
the builder. `reference/` contains
handbook-created source-grounded observations, editorial decisions,
reference transcription and policy. `teaching/` declares synthetic
disturbances. `raw/` preserves their deliberately awkward result and the
derived three-line provider excerpt after declared selection, decoding,
Unicode NFC and whitespace normalization;
`interim/` holds review candidates; `cleaned/` holds the audited result;
`output/` contains derived metrics and summaries; `validation/` contains
expected values and digests; `known-problems/` records limits.

The metadata exercise compares `raw/messy-records.csv` with
`reference/observations.csv` and records decisions before consulting
`cleaned/records.csv`. The OCR exercise compares provider and reference text,
then audits the exact numeric result in `output/`.

## Observation fields

These stable fields occur in `reference/observations.csv`, both top-level
metadata tables, and the layered raw and cleaned tables.

| Field | Meaning and allowed values |
| --- | --- |
| `record_id` | Stable identifier for an issue or feature observation. |
| `record_kind` | `issue`, `captioned_feature`, `portrait`, or `group_portrait`. |
| `page` | PDF page or span as text. |
| `label_transcribed` | Handbook transcription of the printed label under the declared policy. |
| `label_provider_ocr` | Corresponding provider-OCR wording. |
| `date_scope` | What the date describes: `issue_publication`, `depicted_event`, `referenced_event`, `photograph_creation`, or `not_modelled`. |
| `printed_date` | Date expression visible in the source; blank when none is printed. |
| `date_normalized` | Normalized date supported by evidence; blank when unknown or not modelled. |
| `date_status` | `exact`, `derived_from_relative_date`, `unknown`, or `not_applicable`. |
| `issue_context_date` | Publication context for a feature, kept separate from its own date. |
| `printed_person_or_group` | Local person or group label exactly as printed. |
| `entity_structure` | `zero_people`, `one_person`, or `multiple_people`; this is not an authority result. |
| `authority_candidate` | External authority candidate tested during reconciliation. |
| `authority_link_status` | `not_attempted`, `not_reconciled`, `candidate_rejected`, `accepted`, `unresolved`, or `not_applicable`. |
| `authority_evidence` | Evidence for the authority-link status or reason it does not apply. |
| `source_locator` | Page and region in the committed PDF. |
| `evidence_note` | Explanation of a transcription, date, model or limitation. |
| `synthetic` | `true` only when a declared teaching disturbance affects the raw row; otherwise `false`. |

The printed label, entity structure and authority link are separate. A clear
printed name without an external URI may be `one_person` and
`not_attempted`; it is not automatically an unresolved identity. A group
portrait is `multiple_people`, not one unresolved person. AF-P1-002 has
`date_scope=photograph_creation`, blank `date_normalized`,
`date_status=unknown`, and a separate `issue_context_date=1925-02-07`.

## Teaching and review fields

`teaching/synthetic-perturbations.csv` records `perturbation_id`, `operation`
(`set` or `duplicate`), `target_record_id`, optional `new_record_id`, changed
`field`, `synthetic_value`, and `teaching_reason`. These are declared
exercise devices, never historical facts.

`interim/reconciliation-candidates.csv` records `candidate_id`, `record_id`,
`field`, `candidate_value`, `reference_value`, `review_status`, and
`synthetic`. Its rows require review; they do not authorize silent changes.

`correction-log.csv` and `cleaned/decisions.csv` record `decision_id`,
`record_id`, `field`, `input_value`, `result_value`, specific `action`,
`source_locator`, `evidence`, `responsible_process`, `decision_date`,
`rule_version`, `confidence`, `reversible`, and `synthetic`. Nine
`synthetic=false` rows document source-grounded editorial work—including the
provider-excerpt extraction and normalization—while four
`synthetic=true` rows reverse the declared disturbances.

`unresolved-cases.csv` records `case_id`, `record_id`, field-specific `field`,
`status`, `current_value`, `current_evidence`, `reason`, and
`evidence_needed`. An unknown or rejected result is an auditable outcome,
not a blank to fill automatically.

## OCR output fields

`output/ocr-evaluation.csv` reports separate character and word
substitutions, deletions and insertions, reference denominators, total edits,
CER and WER. Character alignment uses Unicode code points including internal
whitespace; word alignment splits on Unicode whitespace. Ties prefer match,
then substitution, deletion and insertion. Rates use
`edits / reference denominator` and are rounded to six decimal places with
round-half-even. These comparisons begin with `raw/provider-ocr.txt`, after
the declared excerpt selection and whitespace normalization; they do not
measure omitted layout-whitespace behaviour in the rest of the dLib export.

`output/ocr-error-audit.csv` gives `audit_id`, `sample_id`, `source_locator`,
`reference_form`, `provider_form`, `operation`, `error_category`,
`policy_or_recognition`, `probable_downstream_consequence`, `review_status`
and `aggregate_relation`. Its nine rows are every non-matching word operation
and sum to the word S/D/I totals. Character S/D/I is a separate whole-string
alignment, so those operations are deliberately not allocated to word rows.

`output/record-summary.csv` uses `dimension`, `category`, `count` and `notes`
to report the inventory, record kinds, date statuses, entity structures and
authority-link statuses. `validation/expected-results.json` stores the same
key counts and OCR results in machine-readable form.
