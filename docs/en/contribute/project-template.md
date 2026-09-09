---
title: "Critical case-study template"
description: "A fifteen-section template for investigating a public humanities project through sources, inspected evidence, modelling decisions, rights and limits."
tags: [template, case-studies, evidence, source-criticism]
status: draft
---

# Critical case-study template

Use this template to explain what a humanities project makes knowable and what
its interface, data or code cannot establish. Start from a scholarly question,
not a promotional description. A responsible case can inspect an interface,
dataset or documentation without running code. State the inspection actually
performed and its limits.

Create the paired pages under `docs/en/case-studies/` and
`docs/sl/case-studies/` using the same filename. Retain the fifteen headings
below and replace the prompts with a connected, evidence-supported account.
This is a writing template, not an inspected case or a record of human approval.

Prepare the authored catalogue record in `data/case-studies.yml`, following
`data/case-study-schema.json` and `data/case-study-metadata.md`. The case's
`case_id`, localized `title`, `content_standard`, `translation_status` and `audit_record` in
frontmatter must agree with that record. For a new paired showcase draft,
start with the following skeleton and replace all explicit placeholders:

```yaml
---
case_id: "REPLACE_WITH_REGISTERED_CASE_ID"
title: "REPLACE_WITH_ENGLISH_CASE_TITLE"
description: "State the scholarly question and what this case makes inspectable."
tags: [case-study]
status: draft
content_standard: showcase-v1
translation_status: paired-draft
audit_record: "release/case-study-audit.md#REPLACE_WITH_CASE_ANCHOR"
---
```

`showcase-v1` identifies the required content structure, not completed peer
review. Do not relabel a `legacy-audited` case as complete merely by adding
headings; remedy its recorded gaps in a bounded content change. A `deferred`
case requires an explicit audit explanation. Keep machine-assisted drafts
visibly identified until appropriate human review is recorded.

The generator derives `data/case-studies-index.json` and both catalogues from
the authored records and canonical relationships. Do not hand-edit those
outputs. Current availability and licence claims need dated evidence in
`release/case-study-audit.md`; ordinary validation does not revisit external
services or prove that they are still available.

## Research question and scholarly object

State what the project seeks to know, represent, publish or enable. Identify
the scholarly object: for example, a collection, edition, historical relation
or description practice. Explain the question that this case study investigates
and distinguish it from the project's own stated ambitions. Name the inspected
version and establish the scope of the argument.

## Intended users or communities

Identify the intended readers, researchers, learners or communities and the
evidence for that identification. Distinguish an institution's proposed audience
from observed use; do not invent usage figures or infer community endorsement.
Discuss who can contribute, challenge a description or request restriction,
and whose language, access needs or expertise the design may exclude.

## Sources and coverage

Describe included and excluded materials, period, geography, language, genre
and known gaps. Name the selection unit and explain the relationship between
the small inspected sample and the wider collection. Preserve source
identifiers and provenance. An interface's search results are not necessarily
a complete inventory; say which coverage claims you could verify.

## Rights and access

Separate access to the interface from permission to download, process,
redistribute or send material to a third-party service. Inspect the relevant
licence, access statement or agreement and record its location, scope and date.
Distinguish code, source documents, derived data, images and documentation.
Identify personal or sensitive information, community authority and mediated
access. If permission is unresolved, select a lawful inspection route and state
what you cannot examine or share.

## Data and modelling choices

Explain the units, identifiers, schema, categories and standards that turn
sources into data. Trace one inspected source item into its representation.
Show how the model handles uncertainty, missingness, conflicting names or
changing dates, and where it simplifies meaningful distinctions. Do not infer
implemented validation from a schema filename or a README promise; inspect
the relevant fields, rules or documented examples.

## Technical and institutional architecture

Describe the public interface, repository if available, data formats,
downloads or APIs, important dependencies and responsible institutions.
Distinguish what is public, restricted, generated, hosted or locally
reconstructible. Identify who maintains the system and what evidence supports
that account. A repository can expose only one component of a larger service;
do not equate its presence with a complete reproducible installation.

## Evidence inspected

Include the following evidence table. Use separate rows for distinct
observations, with exact source locations, access dates and versions or
commit identifiers where available. Replace the prompts; they do not report
completed inspection. If an evidence type is absent, say so and explain why.

| Evidence type | Exact item, version and locator | Date and action performed | Finding and limit |
| --- | --- | --- | --- |
| Project or institutional claim | Identify the official statement and section | Record when you read it | Attribute the claim; say whether independently checked |
| Observed interface behaviour | Identify the page, control, query and relevant state | Record the interaction and access date | Describe the observed response, not unseen backend behaviour |
| Inspected repository/file evidence | Identify the file and commit, release or checksum | Record what you read or compared | Explain what the bytes support and what remains untested |
| Locally executed result | Identify the permitted input, command, environment and output | Record the actual execution date, or state that nothing was run | Report the result, failure or refusal to execute and its reason |
| Editorial inference | Identify the evidence rows on which the inference depends | Record the reasoning and any review undertaken | Label the interpretation and a plausible alternative |

A project claim and an observed result can disagree. Preserve that disagreement
and its consequence for the case. Screenshots require rights and accessible
descriptions; a screenshot alone is not proof of complete system behaviour.

## Minimal lawful inspection or run path

Give a bounded route with prerequisites, permitted inputs, exact actions,
expected inspectable output, a check and a stopping condition. Set a sample
size and approximate time. One documented interface query, a comparison of two
data records or a reading of a versioned schema may be sufficient.

Code execution is optional. Where it is appropriate, supply the tested command,
dependency versions and smallest lawful input; distinguish an actual local
result from an untested project instruction. When execution requires missing
data, infrastructure, credentials or permission, explain the barrier and offer
a non-executing inspection. Do not bypass access controls, start an unrestricted
crawl or imply full reproducibility from a successful small demonstration.

## Where the workflow breaks

Document at least one observed or demonstrable failure, edge case, ambiguous
record, missing dependency or inaccessible component. Identify the input and
evidence, expected behaviour, actual observation and consequence for the
research question. If reproducing a failure would be inappropriate, explain
the evidence you can lawfully inspect. Label a teaching simulation explicitly;
never present an invented failure as an observed defect in the project.

## Manual intervention and unresolved questions

Explain what people must correct, adjudicate, interpret or leave open. Trace
one decision from evidence through alternatives to its consequence. Preserve
disagreement instead of treating consensus as proof. Name any actual reviewer,
date and scope; leave unfinished review clearly pending. State which questions
need a project maintainer, domain specialist, community representative or
rights holder rather than an unsupported editorial guess.

## Reuse potential and exact licence conditions

Identify reusable ideas, code, schemas, data or teaching patterns separately.
For each proposed reuse, cite the inspected licence text or permission and its
scope, version, attribution requirements and restrictions. Distinguish an open
licence from public visibility, a downloadable sample or mediated access.
Record an unverified licence as unknown with the reason; do not interpret a
missing licence as permission. Explain what the classroom exercise may inspect
without claiming that all project material can be republished.

## Claims supported and not supported

State the strongest claim warranted by the inspected evidence and one
tempting claim it does not support. Connect the limit to source coverage,
modelling choices or inspection depth. Distinguish technical functioning,
performance on a bounded sample and scholarly interpretation. Explain how a
plausible alternative selection or modelling decision could change the result.

## Maintenance and preservation

Date the status assessment and identify the version, responsible body,
available maintenance evidence and unresolved dependencies. Distinguish a
reachable site, an active maintainer and a preserved scholarly object.
Describe version records, exports, persistent references, backups or deposit
arrangements only where inspected evidence supports them. Record an unclear,
archived or unavailable state visibly; a recent page response alone does not
establish long-term preservation.

## Connections across the handbook

Explain why at least one chapter and one practical workflow help a reader
understand this case. Author the conceptual relationship lists only in
`intertextuality.yml`; the generated catalogue derives `chapter_connections`
and `workflow_connections` from that map. Do not maintain competing connection
lists in metadata or page frontmatter. Use this section for the rationale and
the handbook's generated connection block for the current links. If a legacy
or deferred case lacks a suitable connection, record the remediation in its
audit rather than attaching a vaguely relevant page.

## A bounded classroom task

Set one question, a small lawful input or inspectable item, a time limit and a
specific student output. Include a source check, one difficult decision and a
reflection on what cannot be concluded. Offer an accessible non-executing
alternative where an account, cost, unavailable dependency or restricted data
would prevent participation. Assess the quality of evidence and reasoning,
not whether students can reproduce the whole project.

Before submitting, confirm English/Slovene parity, complete the dated audit
and metadata record, regenerate the catalogues and run `make check` and
`git diff --check`. A passing build checks structure and consistency, not
source accuracy, ethical permission or completed human review.
