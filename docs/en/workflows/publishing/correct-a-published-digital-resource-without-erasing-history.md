---
title: "How do I correct a published digital resource without erasing history?"
description: "Document an error, its scholarly consequence, the corrected edition and the continuing citation route."
category: "Publishing & FAIR data"
category_id: "Publishing & FAIR data"
difficulty: "intermediate"
time: "60–100 min"
tags: [corrections, publishing, versioning, ethics, citation]
status: draft
---

# How do I correct a published digital resource without erasing history?

!!! warning "Draft and exercise scope"
    This machine-assisted workflow awaits human scholarly and Slovene-language review. The release numbers and letter counts below are hypothetical. Prepare records locally; no actual release or removal is required.

## What you are trying to do

How should a later reader learn that an earlier edition counted the same historical letter twice? Make the change and its evidential consequence visible in a source correction, public notice and citation route. Follow the distinctions in [The living open handbook](../../chapters/open-living-handbook.md).

## You need

- An identifiable earlier edition and exact affected section/table locators.
- Evidence that permits independent checking, including lawful source access.
- Both language versions, generated outputs and any existing correction policy.
- An editor responsible for deciding the scope of correction and review.

## Workflow

1. Reproduce the reported discrepancy before classifying it. Identify affected releases, language versions, figures, data and calculations. Record uncertain scope explicitly; a correction to a table may require revising prose that cites it.
2. Decide whether the issue is a limited correction, substantive correction, deprecation, supersession or retraction. An erratum is the notice, not a substitute for classifying the problem. Serious unreliability requires an editorial process; distinguish uncertainty under investigation from an established finding.
3. Assess release consequence under the local policy. Use a patch only if the teaching argument remains unchanged. Substantial corrected material within the existing architecture may warrant a minor release; a changed method or architecture may warrant a major reviewed edition. Explain the decision.
4. Draft the paired source correction and revision of dependent outputs. Preserve an error identifier across the changelog, erratum and release notes. Record what was wrong, how it was verified, what changes and what still holds.
5. Keep ordinarily cited earlier artefacts identifiable. Add a visible correction/supersession link to their landing record; put corrected files in the successor edition. Document edits to mutable landing metadata without claiming the original bytes changed.
6. Handle privacy/security exposure separately through responsible institutional channels. Restrict or remove harmful content where required, including history/deposits/caches where feasible. Retain only an authorized restricted evidential record; publish a non-sensitive notice. Do not reproduce the exposed data in the issue or promise complete deletion of other people's copies.
7. Have a reviewer check the complete chain and both languages. Rebuild affected outputs, compare claims and checksums, test links from the older landing record, and prepare citation guidance. Notify known course maintainers or repositories through approved routes when the consequence warrants it.

## Documentary record

The classroom example removes four duplicate representations from 40 rows, leaving 36 distinct letters. The release judgement is specific to this example, not a universal rule for numerical corrections. Shared machine keys let EN/SL records be compared; each record is a template, not evidence of completed human review.

```yaml
record_type: publication-correction
record_status: template
correction_id: EX-ERR-001
affected_release: "1.0.0 (hypothetical)"
affected_objects:
  - "en/source-counting#worked-example"
  - "sl/source-counting#razdelan-primer"
  - "table LETTER-COUNT-01 and generated reading copies"
evidence: "Compare duplicate source IDs in rows 37–40 with their earlier entries"
category: substantive-correction
claim_before: "The table represents 40 distinct historical letters"
claim_after: "The 40 rows represent 36 distinct historical letters"
release_classification:
  level: minor
  target_version: "1.1.0 (hypothetical)"
  rationale: "Corrected teaching conclusion within the existing architecture; not a patch"
source_change: "Paired correction and recalculation; source commit pending"
changelog: "EX-ERR-001 identifies affected 1.0.0 section and planned 1.1.0"
erratum: "Draft dated notice: evidence, wrong denominator, consequence, replacement"
release_notes: "Link EX-ERR-001; describe review scope and all regenerated outputs"
prior_version_access: "Preserve ordinary 1.0.0 files; link erratum from landing record"
supersession: "1.1.0 replaces the affected teaching example; keep earlier identity"
later_citation: "Cite corrected 1.1.0 section; for history cite 1.0.0 plus EX-ERR-001"
review: "Pending named subject and Slovene reviewers, date and revision"
privacy_action: "No personal data in this hypothetical example; reassess each real case"
```

## Output

A correction dossier containing source changes, evidence, release classification, erratum, revised metadata, review scope and later citation instructions. It must distinguish a proposed action from an executed one. A reader should understand the consequence without knowing Git.

## Check yourself

- Does a reader of the earlier edition encounter a visible correction route?
- Are unchanged files distinguishable from regenerated successor files?
- Does the erratum explain whether the interpretation changes?
- Do both language records name the same error and successor?
- Does the privacy variant avoid copying sensitive evidence into public history?

## Common traps

- Replacing an archived ZIP under the same filename and silently changing its digest.
- Calling an altered conclusion a typo because only one sentence changes.
- Treating deprecation as proof that the old historical analysis was false.
- Preserving a harmful public disclosure in the name of transparency.

## Practice task

Exchange dossiers. Replace the numerical fault with a broken link that still has an authoritative successor, then with disclosed participant data. Explain why the actions and release classification differ. A defensible answer identifies uncertainties and responsible decision-makers instead of inventing completed approvals.

## Sources and service check

Checked **7 September 2026**: COPE, [Retraction guidelines](https://doi.org/10.24318/cope.2019.1.4), version 3 (2025), and [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html). These inform the distinctions; the publication's editorial policy determines its release decisions. For a successor package, use [Create a versioned scholarly release](create-a-versioned-scholarly-release.md).
