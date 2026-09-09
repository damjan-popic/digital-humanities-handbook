---
title: "How do I create a versioned scholarly release?"
description: "Prepare an inspectable edition plan with a manifest, review scope, citation metadata, rights, checksums and a conditional deposit route."
category: "Publishing & FAIR data"
category_id: "Publishing & FAIR data"
difficulty: "intermediate"
time: "90–150 min"
tags: [publishing, versioning, preservation, review, metadata]
status: draft
---

# How do I create a versioned scholarly release?

<div class="answer-meta" markdown="span">
<span>Publishing & FAIR data</span><span>intermediate</span><span>90–150 min</span>
</div>

!!! warning "Draft and exercise scope"
    This machine-assisted workflow awaits human scholarly and Slovene-language review. It prepares a release plan; it does not publish a release, register an identifier or confirm a publisher agreement.

## What you are trying to do

A reader needs to know exactly which bilingual teaching material supports a cited argument. Prepare a package whose contents, evidence of review, rights and citation agree. Use [The living open handbook](../../chapters/open-living-handbook.md) to distinguish a reviewed edition from the continually maintained source.

## You need

- A small rights-cleared teaching project, its source revision and build instructions.
- A list of included and excluded pages, with paired-language status.
- Available review records and written publisher/deposit requirements, if confirmed.
- A local workspace and checksum utility; no repository administration rights are needed.

## Workflow

1. State the edition's scholarly claim and audience. Select a candidate revision and inventory every included object. Separate reviewed content from living-library companions; a page outside the manifest cannot inherit the edition's review claim.
2. Record review scope, names where publication is permitted, dates and revision reviewed. Check translations by meaning and instruction, and mark draft or fallback honestly. List accessibility checks and remaining exceptions separately for each reading format.
3. Choose a version under the editorial policy and explain its significance in a changelog. Reconcile the proposed tag, citation metadata, manifest, release notes and package filenames. A tag, GitHub release and scholarly identifier describe different objects.
4. Build from the selected source in a documented environment. Inspect both language editions, links, source locators, tables and offline reading. Produce a source archive and suitable reading copies, including licences and contributor records. Compute SHA-256 after finalizing each file; an edited ZIP requires a new digest.
5. Complete the record below. `null` means not yet obtained in this template, never an assigned value or a successful check. Replace it with the observed commit or checksum only after verification. Repeat manifest and artefact entries for the complete inventory.
6. Agree identifier responsibilities and deposit conditions with the publisher/institution. Leave DOI/ISBN conditional. Verify deposited bytes and the landing record when an authorized deposit actually occurs. GitHub Actions artefacts alone are not a preservation arrangement.
7. Ask another editor to reconcile all records. Record unresolved blockers and stop at a candidate if required review, rights, accessibility or publisher decisions remain pending.

## Documentary record

This is a classroom template for a hypothetical bilingual source-counting edition. Paths belong to the exercise, not to this repository. EN/SL templates share machine keys. Empty values here are explicitly pending; they do not establish completeness.

```yaml
record_type: scholarly-release-plan
record_status: template
project: "Hypothetical source-counting teaching edition"
candidate_version: "1.0.0-rc.1"
source_commit: null
manifest:
  - path: "docs/en/source-counting.md"
    title: "Counting historical sources"
    language: en
    content_type: stable-chapter
    review_status: pending-human-review
    review_scope: "Subject, method, pedagogy; reviewer/date/revision pending"
    translation_status: "Paired Slovene draft; equivalence review pending"
    licence: CC-BY-4.0
    source_sha256: null
    inclusion_status: proposed-reviewed-edition
    external_dependencies: []
    accessibility: "Heading, table and keyboard review pending"
  - path: "docs/sl/source-counting.md"
    title: "Štetje zgodovinskih virov"
    language: sl
    content_type: stable-chapter
    review_status: pending-human-review
    review_scope: "Slovene language and subject; reviewer/date/revision pending"
    translation_status: "Machine-assisted draft paired with English"
    licence: CC-BY-4.0
    source_sha256: null
    inclusion_status: proposed-reviewed-edition
    external_dependencies: []
    accessibility: "Heading, table and keyboard review pending"
changelog: "Draft entry for 1.0.0-rc.1; not a publication date"
citation_metadata: "Draft author/title/version/locator record; reconcile before publication"
identifiers:
  doi: null
  isbn: null
  assignment_authority: "Publisher and institutional repository; confirmation pending"
  status: pending-agreement
artefacts:
  - path: "source-counting-1.0.0-rc.1-source.zip"
    sha256: null
  - path: "source-counting-1.0.0-rc.1-reading.zip"
    sha256: null
archive:
  repository: "Institutional repository; acceptance pending"
  deposit_status: not-deposited
  verification: "Pending retrieval, checksum comparison and landing-record inspection"
build_environment: "Record OS, runtime, dependencies, command and observed result"
approval: "Pending named editor, review record and required publisher approval"
```

## Output

A candidate package plus manifest, changelog, citation draft, licences, contributor/review records and checksums. Distinguish prepared files from a completed deposit. For this handbook, actual publisher-coordinated release operations belong to [issue #30](https://github.com/damjan-popic/digital-humanities-handbook/issues/30).

## Check yourself

- Can another person identify the exact source and every included object?
- Do review and translation claims match the actual records in both languages?
- Can the package be extracted and its principal content read offline?
- Do recalculated checksums match, and are missing dependencies disclosed?
- Is every unassigned identifier explicitly pending with an identified authority?

## Common traps

- Treating CI success as peer review or a tag as permanent preservation.
- Relicensing external data through a blanket repository licence.
- Citing an undated `main` page after using a numbered edition.
- Assuming accessible HTML proves an accessible PDF.

## Practice task

Exchange candidate plans. Introduce a missing Slovene page, an unlicensed image and a changed ZIP. Identify which claims must be withdrawn and which files must be regenerated. Submit a corrected plan and a short decision about whether publication can proceed.

## Sources and service check

Checked **7 September 2026**: [GitHub: About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases), [Zenodo: Digital Object Identifier (DOI)](https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/), and [Digital Preservation Coalition: Fixity and checksums](https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums). Recheck the selected service and institutional requirements before acting.
