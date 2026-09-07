---
title: "How do I compare AI output across prompts, models and runs?"
description: "Test whether a bounded source-based conclusion survives controlled changes, and classify differences that affect the argument."
category: "AI"
category_id: AI
difficulty: "intermediate"
time: "90–150 min"
tags: [AI, robustness, evaluation, source-criticism, uncertainty]
status: draft
---

# How do I compare AI output across prompts, models and runs?

## What you are trying to do

You want to know whether a summary preserves who makes a historical claim when
its prompt, source order or model changes. This is a bounded robustness
exercise, not a ranking of universally best models. Follow
[AI, ethics and reproducibility](../../chapters/ai-ethics-reproducibility.md)
and first complete the
[source and run audit](document-and-audit-a-source-grounded-ai-analysis.md).

This machine-assisted workflow awaits human review. It proposes eight model
calls but reports **zero actual runs**. Its alternative offline exercise uses
authored simulations and cannot establish model performance.

## You need

- The [text/NLP packet](../../../assets/downloads/text-nlp-validation-v1.zip)
  and [archival-friction packet](../../../assets/downloads/archival-friction-v1.zip),
  with rights and provenance records.
- Three passage IDs: `TNLP-CLEAN-02` (synthetic control), `TNLP-AF-REF` and
  `TNLP-AF-OCR` (two representations of one historical sentence).
- An audit table, a source register and time for source reading. Use only
  approved services if you elect to run models; no account is needed offline.

The question is how the introductory paragraph constructs political unity.
The historical locator is `AF-OCR-P1-INTRO`, PDF page 1 below the title,
sentence beginning `Tudi danes`. A manual baseline should extract the speaker,
the claim of unity, the evidence offered and the qualification needed. Prepare
it before reading candidate AI summaries to reduce anchoring. The baseline
is a proposed task, not a completed human-reviewed reference.

## Workflow

1. **Freeze the comparison.** Retain the same source versions, passage IDs,
   task and output format. P0 asks: “For each passage, identify the speaker,
   summarize its claim, give the passage ID, and state what the source does
   not establish. Do not add evidence.” P1 changes only the first instruction
   to “For each passage, distinguish the publication's assertion from a
   finding about its audience”, preserving the remaining requirements.
2. **Declare conditions.** C0 uses P0, M1 and the original passage order; C1
   changes only to P1; C2 changes only to reversed passage order; C3 changes
   only to M2. M1/M2 are placeholders for recorded model identifiers, not
   products. Fix parameters where supported and record unavailable settings.
   Use fresh contexts, not a conversation that retains prior answers.
3. **Plan two repetitions per condition.** Each call receives all three
   passages, clearly labelled, and returns separate records for them. Four
   conditions times two repetitions mean eight planned calls. Log time,
   model identifier, configuration and output for each actual call, including
   refusals and failures. A second model may require a different provider;
   review its data arrangement before sending anything. If unavailable,
   mark C3 `not_run` and reduce the claim, not the documentation.
4. **Review without model labels.** Assign output IDs and hide condition
   names during the first reading where practical. Compare every consequential
   claim with the source and manual baseline. Keep the synthetic control and
   historical text separate; the two historical representations are paired,
   not independent observations for statistical inference. Because the
   reference and OCR are visible together, this tests use of paired evidence,
   not performance on OCR alone. A test with isolated inputs needs a separately
   declared plan and budget.
5. **Classify differences.** Use the taxonomy below. A changed adjective is
   not automatically a research difference; an adjective that changes certainty
   may be. Compare original Slovene with English paraphrase rather than treating
   fluent English as the reference. Inspect omissions and refusals as well as
   generated statements.
6. **Adjudicate and decide.** Preserve independent reviewer judgements when
   possible, their reasons, final decision and unresolved cases. Count errors
   and reviewed claims separately in each stratum. Report raw counts, coverage
   and missing conditions. Two repetitions cannot estimate a stable performance
   distribution or support statistical significance claims.
7. **Report the boundary.** State which changes altered the historical argument
   and whether the method met the acceptance rule. Do not choose a winning
   prompt after seeing results and call that an independent test. A revised
   prompt requires a new held-out evaluation sample for performance claims.

## Comparison plan

Copy the record and retain its machine keys in either language. The proposed
budget is a classroom ceiling, not permission to incur charges. Obtain an
appropriate permitted arrangement before optional paid calls; otherwise use
the offline route. Every actual run needs the full provenance record from the
companion workflow. `unknown`, `redacted` with explanation and `not_run` must
remain distinguishable. Human-review fields require real names, ISO dates and
scope before a human-reviewed state can be claimed.

```yaml
record_type: ai-robustness-plan
record_status: template
research_question: Does the summary preserve attribution and uncertainty?
source_documents:
  - teaching-data/text-nlp-validation/raw/annotation-samples.csv
  - teaching-data/archival-friction/source/ilustrirani-slovenec-1925-02-07.pdf
passage_ids: [TNLP-CLEAN-02, TNLP-AF-REF, TNLP-AF-OCR]
baseline: Manual extraction of speaker, claim, evidence and qualification; pending.
conditions:
  - {condition_id: C0, prompt: P0, model: M1, source_order: original}
  - {condition_id: C1, prompt: P1, model: M1, source_order: original}
  - {condition_id: C2, prompt: P0, model: M1, source_order: reversed}
  - {condition_id: C3, prompt: P0, model: M2, source_order: original}
planned_runs: 8
actual_runs: 0
run_records: []
consequential_difference_taxonomy:
  - attribution
  - evidence
  - uncertainty
  - omission
  - translation
  - abstention
  - style_only
validation_strata:
  - {stratum: synthetic_clean, passage_ids: [TNLP-CLEAN-02]}
  - {stratum: historical_reference, passage_ids: [TNLP-AF-REF]}
  - {stratum: historical_ocr, passage_ids: [TNLP-AF-OCR]}
validation_sample: [TNLP-CLEAN-02, TNLP-AF-REF, TNLP-AF-OCR]
adjudication: Preserve initial decisions, source reasons, final decisions and disagreement.
acceptance_rule: No invented evidence or population claim in any publishable candidate.
stop_rule: Stop at the budget limit or an unresolved privacy or rights problem.
budget:
  maximum_model_calls: 8
  maximum_paid_cost_eur: 5
  maximum_review_minutes: 120
  actual_cost: not_run
  energy_measurement: unknown
results_status: not_run
review_status: pending_human_review
reviewer: pending
review_date: pending
review_scope: pending
```

## Consequential differences

| Category | Compare | Why it matters |
| --- | --- | --- |
| `attribution` | Who asserts or experiences something? | A partisan assertion can become a false population finding |
| `evidence` | Added, altered or absent support; quotation and locator | An invented survey changes the basis of the argument |
| `uncertainty` | Qualifications, certainty and scope | A possible reading can become an unwarranted fact |
| `omission` | Missing counterevidence or context | An apparently accurate sentence can conceal a misleading selection |
| `translation` | Meaning and political voice across languages | A smooth paraphrase can erase the original's stance |
| `abstention` | Refusal, partial answer or explicit unknown | Coverage changes, potentially unevenly across strata |
| `style_only` | Wording with unchanged evidence, attribution and scope | It need not alter the research claim |

Use one comparison row per passage and pair of output IDs:

| passage_id | output_ids | difference_tags | source_locator | consequence | reviewer_decisions | final_treatment |
| --- | --- | --- | --- | --- | --- | --- |
| fill | fill | fill | fill | fill | pending | pending |

## Output

A declared plan, all actual run records, a baseline with its review state,
paired difference table and limited conclusion. Include actual versus planned
calls and missing conditions. Reject or correct any publishable candidate with
invented evidence; that decision does not by itself demonstrate a robust model.
If only simulations were examined, report an audit exercise with no model results.

## Check yourself

- Does each comparison vary only the declared factor?
- Are failed calls and refusals included, with separate error and coverage counts?
- Did each stratum receive source review, including difficult OCR and Slovene?
- Are consequential differences tied to the historical argument?
- Have you avoided treating two related representations as independent sources?
- Are actual costs and inaccessible environment details recorded honestly?

## Common traps

- Comparing different tasks, context lengths and models simultaneously.
- Calling model agreement independent confirmation of a historical claim.
- Reporting only the best response or hiding failed conditions.
- Mistaking two successful repetitions for a reliable population estimate.
- Treating synthetic examples or unfinished human review as a benchmark.

## Practice task

Offline, write three clearly labelled variations of the chapter's simulation:
one changes only style, one removes attribution and one restores uncertainty.
Classify them and explain which scholarly claims change. Record
`actual_runs: 0` and describe the exercise separately; do not insert authored
text into model-run records. With approved model access, complete the planned
calls instead, preserving every outcome. End with one defensible conclusion
and one question the comparison cannot answer.
