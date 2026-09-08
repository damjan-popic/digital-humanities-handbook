---
title: "How do I document and audit a source-grounded AI analysis?"
description: "Preserve sources, configuration, outputs and human decisions while distinguishing reproducibility from a traceable claim."
category: "AI"
category_id: AI
difficulty: "intermediate"
time: "90–120 min"
tags: [AI, provenance, source-criticism, validation, reproducibility]
status: draft
---

# How do I document and audit a source-grounded AI analysis?

<div class="answer-meta" markdown="span">
<span>AI</span>
<span>intermediate</span>
<span>90–120 min</span>
</div>

## What you are trying to do

You want to explain how a newspaper constructs political unity without turning
its rhetoric into a finding about public opinion. Preserve enough evidence for
another reader to inspect every consequential claim, even if the model later
becomes unavailable. This workflow accompanies
[AI, ethics and reproducibility](../../chapters/ai-ethics-reproducibility.md).

This is a machine-assisted documentation draft pending human review. The
chapter's faulty outputs are authored teaching simulations. The template below
records no completed AI run or human validation.

## You need

- The [text/NLP packet](../../../assets/downloads/text-nlp-validation-v1.zip)
  and [archival-friction packet](../../../assets/downloads/archival-friction-v1.zip),
  including their rights, transcription and provenance records.
- A text editor or accessible table editor, a PDF reader, and a place to retain
  original and corrected outputs separately.
- A research question, a short claim-review codebook, and an agreed disclosure
  and access plan. No paid account or external model is required.

Use `TNLP-CLEAN-02` as the synthetic clean control and `TNLP-AF-REF` /
`TNLP-AF-OCR` as two representations of the same historical sentence, not
independent historical sources. Their exact selections and hashes are in
`raw/annotation-samples.csv`. The historical locator is `AF-OCR-P1-INTRO`,
PDF page 1 beneath the title, sentence beginning `Tudi danes`.

## Workflow

1. **Set the boundary.** State the question and forbid unsupported inference
   about population opinion. Read the rights records; identify any restricted
   material before selecting a service. If procurement, privacy or reuse terms
   remain unresolved, complete the offline audit with the authored simulation.
2. **Freeze the input.** Preserve the source files and their hashes. Record
   passage IDs, surrounding context, normalization, translations and omissions.
   For retrieval, preserve the index and embedding-model versions, query,
   chunking, filters, ranking, selection count and supplied passage order.
3. **Record the event.** Fill every applicable field below before and during
   an optional run. Save actual UTC time and returned model identifier; do not
   substitute a product name for a missing version. Preserve instructions and
   history when permitted. Record hidden or unavailable settings explicitly.
4. **Preserve the candidate.** Save the complete unedited response or clearly
   labelled teaching simulation. Give it a stable output ID. Keep errors,
   refusals and truncated outputs. Do not overwrite it with the edited text.
5. **Audit claims and omissions.** Verify quotations character by character
   against the appropriate text layer and then the scan. Verify speaker,
   locator, date, scope and counterevidence separately. A real quotation may
   still be misattributed. Inspect translation against the Slovene original.
6. **Review decisions.** For this tiny exercise inspect every claim. Have a
   second reader independently review them if available; retain both decisions
   and reasons before adjudication. For a larger study specify a random sample
   plus strata for language, OCR condition and genre, with IDs and denominators.
   Mark pending review honestly when a second reader is unavailable.
7. **Correct and report.** Keep a correction log, narrowed scholarly claim and
   assistance statement. Report what can be rerun and what can only be audited.
   A prompt and frozen output alone do not reconstruct a retired hosted model.
   Link the packet to the exact publication version that uses it.

## Documentation record

Copy and complete this YAML record. Machine keys remain identical across
languages. Replace `not_run` only after execution; use `unknown` for unavailable
information and `redacted` with a reason and authorized access route for
withheld material. Empty metadata never silently means zero. Keep `reviewer`,
`review_date` and `review_scope` as YAML `null` while human review is pending.
Before claiming completed review, replace them with the reviewer's name, an
ISO date (`YYYY-MM-DD`) and a substantive account of the material and checks
covered. Never publish credentials.

```yaml
record_type: ai-analysis-audit
record_status: template
research_question: How does the introductory paragraph construct political unity?
provider: not_run
model_identifier: not_run
model_version_or_snapshot: not_run
run_time_utc: not_run
interface: not_run
system_instructions: not_run
user_instructions: not_run
parameters: not_run
retrieval_configuration: not_run
source_documents:
  - teaching-data/text-nlp-validation/raw/annotation-samples.csv
  - teaching-data/archival-friction/source/ilustrirani-slovenec-1925-02-07.pdf
passage_ids: [TNLP-CLEAN-02, TNLP-AF-REF, TNLP-AF-OCR]
preprocessing: Copy the declared extraction and hash records before running.
truncation: not_run
output_path: not_run
correction_log: not_run
validation_sample: [TNLP-CLEAN-02, TNLP-AF-REF, TNLP-AF-OCR]
validation_protocol: Inspect all claims; preserve independent decisions and adjudication.
environment: not_run
cost: not_run
nondeterminism: unknown
unavailable_details: unknown
disclosure: This template records no model experiment; after execution, disclose the task, run record, affected material, checks and responsible people.
review_status: pending_human_review
reviewer: null
review_date: null
review_scope: null
```

`source_documents` identifies selected inputs, not a licence grant. Add hashes,
source versions and access conditions to the accompanying source register.
For an actual run, `cost` should include currency and amount, and `environment`
the relevant software, packages, hardware and elapsed time. A remote provider's
unavailable environment remains unknown. Redaction limits public auditability;
document that limit instead of promising unrestricted reproduction.

Use one row per claim or consequential omission:

| claim_id | original_output_id | claim_or_omission | source_id_and_locator | verdict | correction | consequence_for_argument | reviewer_and_date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fill | fill | fill | fill | pending | pending | pending | pending |

Suggested verdicts are `supported`, `partly_supported`, `unsupported_claim`,
`misattribution`, `quotation_error`, `locator_error`, `omission`, `unverifiable`.
Define them in the codebook and allow multiple error tags. Preserve original
reviewer disagreements rather than replacing them with only the final verdict.

## Output

A source register, run record or explicitly unperformed-run record, preserved
candidate, claim audit, correction log, validation sample and assistance
statement. The corrected interpretation should attribute the unity claim to
the newspaper and withdraw the invented survey. These are expected teaching
decisions, not measured model-performance results.

## Check yourself

- Can another reader locate every source passage and distinguish OCR from the
  reference transcription and synthetic control?
- Can you reconstruct the supplied context, or have you marked what is unknown?
- Have you checked attribution and omissions as well as exact quotations?
- Are actual human review, planned review and machine assistance distinguishable?
- Do reported rates identify their denominator and leave zero-denominator
  measures undefined?

## Common traps

- Asking a model to verify itself without giving a reviewer the source.
- Treating a source locator or a fluent translation as proof of support.
- Replacing original output, prompt history or initial reviewer decisions.
- Claiming reproducibility when only traceability has been preserved.
- Publishing private source content in the audit to demonstrate transparency.

## Practice task

Audit the chapter's A01–A04 simulation and write an 80-word corrected
interpretation. Record one disagreement with a partner or explain why review
is pending. Identify one field that would remain unknown for a hosted service
and the resulting limit on your reproducibility claim. Then use the
[bounded comparison workflow](compare-ai-output-across-prompts-models-and-runs.md)
to design the next test.
