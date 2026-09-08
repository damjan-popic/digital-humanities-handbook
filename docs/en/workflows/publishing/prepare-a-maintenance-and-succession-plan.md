---
title: "How do I prepare a maintenance and succession plan?"
description: "Assign responsibility for a scholarly resource, test recovery and document transfer before its founding maintainer leaves."
category: "Publishing & FAIR data"
category_id: "Publishing & FAIR data"
difficulty: "intermediate"
time: "90–150 min"
tags: [maintenance, preservation, governance, succession, accessibility]
status: draft
---

# How do I prepare a maintenance and succession plan?

<div class="answer-meta" markdown="span">
<span>Publishing & FAIR data</span><span>intermediate</span><span>90–150 min</span>
</div>

!!! warning "Draft and exercise scope"
    This machine-assisted workflow awaits human scholarly and Slovene-language review. Names of roles and services below are a planning template, not evidence of existing assignments. Do not publish credentials or transfer accounts during the exercise.

## What you are trying to do

Who can correct a cited digital edition after its founding editor leaves? Build a plan that another person can execute, including continued care or a responsible end to active maintenance. Use [The living open handbook](../../chapters/open-living-handbook.md) to distinguish hosting, editorial ownership and preservation.

## You need

- An inventory of the publication, repositories, domains, external services and data dependencies.
- Existing role assignments, renewal responsibilities and a realistic maintenance budget.
- A rights-cleared sample backup and a separate local recovery workspace.
- A person able to rehearse the documented procedure without the founder's private knowledge.

## Workflow

1. Name the organizational owner, editor, technical maintainer and intended successor. Separate decision authority from access privileges. Confirm acceptance of real roles privately; do not infer responsibility from someone's institutional affiliation.
2. Inventory dependencies and services: runtime and build tools, external datasets/APIs, repository, domain, hosting, deposit and citation records. For each, record a version source or dated terms check, review trigger, owner and renewal obligation. Link to an approved credential manager entry by a non-sensitive reference, never its secret contents.
3. Choose review intervals based on consequence and budget. Include broken-link meaning checks, dependency/security notices, teaching-example reruns, translation drift, accessibility and deposit retrieval. Record a last completed check and next due date when available; a planned cadence is not a completed audit.
4. Define backup scope, locations, retention and who can restore. A copy of the Git repository may omit issues, release assets, permissions, external data or domain records. Separate authorized restricted records from public source, and minimize personal data in backups.
5. Rehearse recovery in an isolated workspace. Compare checksums, build a reading copy, inspect bilingual navigation and one worked example, and record missing services. Log date, operator, result and unresolved failures. Do not overwrite the running site in a test.
6. Rehearse editorial succession too: give a successor a bounded correction and require them to locate its sources, review route, licence and citation impact. List approvals for actual transfer, recovery contacts, access revocation and credential rotation after authorized handover.
7. Agree an exit plan if transfer fails. Freeze an identified final edition, arrange deposit, display the end of maintenance and the support limits, close new submissions, and retain an appropriate correction contact. Do not leave unsupported instructions labelled current.

## Documentary record

This classroom template describes a hypothetical project. Replace role placeholders with confirmed assignments in a real plan; keep private contacts and recovery details in approved restricted storage. Shared EN/SL machine keys allow comparison without translating identifiers.

```yaml
record_type: maintenance-succession-plan
record_status: template
project: "Hypothetical bilingual source-counting resource"
owner: "Department or institution; acceptance pending"
editor: "Role pending confirmed appointment"
technical_maintainer: "Role pending confirmed appointment"
successor: "Role pending acceptance and rehearsal"
dependencies:
  - name: "Runtime and site builder"
    version_record: "Version lock and environment record; to be inventoried"
    review_trigger: "Security notice, failed build, or quarterly review"
  - name: "External historical-source links"
    version_record: "Source locator, authority and last verification date"
    review_trigger: "Reported failure or before each teaching term"
services:
  - name: "Git repository and hosting"
    owner_role: technical_maintainer
    credential_reference: "Approved vault item reference; no secret value"
    renewal: "Confirm account ownership, billing and recovery arrangements"
  - name: "Domain"
    owner_role: owner
    credential_reference: "Approved registrar vault reference; no secret value"
    renewal: "Record expiry date, payer and deputy after confirmation"
  - name: "Institutional deposit"
    owner_role: editor
    credential_reference: "Approved deposit-access reference; no secret value"
    renewal: "Confirm contact and deposit responsibilities annually"
backups:
  scope: "Sources, reading files, assets, metadata and permitted review records"
  locations: "Two independently controlled approved locations; confirmation pending"
  retention: "Institutional schedule; restrict private records and document exceptions"
restore_test: "Pending date/operator/checksums/build/offline reading/result/follow-up"
review_cadence: "Monthly triage (2 hours); quarterly dependencies/accessibility; termly examples/translations; annual recovery"
transfer_procedure:
  - "Confirm successor authority and available maintenance time"
  - "Rehearse recovery and a bilingual correction in an isolated workspace"
  - "Approve repository/domain/deposit transfer through responsible organizations"
  - "Verify successor access; rotate credentials and remove obsolete access"
  - "Update public contacts and record completed handover date"
exit_plan: "If no successor: identify final edition, deposit, announce end of maintenance and correction route"
```

## Output

A responsibility and dependency register, backup/restore evidence, a dated review schedule, transfer procedure and exit plan. The public version contains roles and safe references; restricted operational records hold only necessary private details. Do not call the plan tested until the rehearsal has occurred.

## Check yourself

- Can someone other than the founder locate every required source and permission?
- Does each service have a confirmed owner and a recovery route?
- Does the recovery test restore reading functionality as well as files?
- Are translation and accessibility maintenance assigned time and responsibility?
- Can the project end active maintenance without losing the last citable edition?

## Common traps

- Treating a personal account password as a succession strategy.
- Calling an untested backup a recovery plan.
- Retaining sensitive records everywhere under a blanket “preserve everything” rule.
- Promising weekly manual review without allocating staff time.

## Practice task

Exchange plans and assume the founder is unavailable for a month. Introduce an expired domain or missing build dependency. In a local rehearsal, identify the steps that can proceed and the ones that require authorized staff. Revise the plan and its budget; record actual results separately from recommendations.

## Sources and service check

Checked **7 September 2026**: Digital Preservation Coalition, [Fixity and checksums](https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums) and [File formats and standards](https://www.dpconline.org/handbook/technical-solutions-and-tools/file-formats-and-standards); UNESCO, [Recommendation on Open Educational Resources (OER)](https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer). The intervals and role assignments above are proposed exercise decisions, not requirements attributed to these sources.
