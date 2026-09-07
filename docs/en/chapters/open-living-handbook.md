---
title: "The living open handbook"
description: "How reviewed editions, continuing correction, shared maintenance and preservation support accountable scholarly publication."
tags: [open-education, versioning, peer-review, contribution, publishing]
status: draft
---

# The living open handbook

!!! warning "Editorial status"
    This expanded chapter is a machine-assisted draft awaiting continuous scholarly and competent human Slovene-language review. Its examples describe publication decisions, not completed releases or assigned identifiers.

## Learning outcomes

After this chapter, you should be able to:

- distinguish source history, a generated edition, a release package and a scholarly publication record;
- state what a review covers and what a version number does not establish;
- trace a correction from evidence through publication to later citation;
- prepare a release manifest with review, translation, rights and accessibility status;
- separate student assessment, consent to publication and contributor credit;
- plan preservation, maintenance and succession within realistic resources.

## Before you begin

How can a reader criticize an interpretation if its evidence and wording change between reading and citation? Conversely, what responsibility does an editor have when a widely cited teaching resource contains an error? These questions connect textual scholarship with the practical organization of digital publishing. A living publication must make change intelligible without presenting yesterday's claim as today's knowledge.

Recall a digital edition or teaching site you used. Could you identify its authors, version, last substantive review and preservation arrangement? Distinguish what the page disclosed from what you inferred from its institutional logo. You need basic familiarity with source files and the distinction between evidence and interpretation; publishing permissions are unnecessary for the exercises. The inputs are a small publication inventory and a correction scenario. The outputs are documentary records that another editor can assess.

## Two tempos and a bounded claim to authority

A reviewed edition establishes a bounded scholarly object: these chapters, in these languages, with these examples, were reviewed at this revision. The living edition provides a continuing place for corrections and developing work. Their relationship is editorial, not merely chronological. A recent workflow may be useful but provisionally tested; an older reviewed chapter may retain conceptual value despite an obsolete interface illustration. Neither recency nor a version number substitutes for evidence about review scope.

This handbook places its slowly changing chapters and learning paths beside a faster workflow library. The default branch, `main`, supports the living edition; numbered releases are intended as frozen, reviewed snapshots. A release manifest must specify which practical pages belong to the reviewed edition and which remain companion material. English fallback in the Slovene workflow library provides access, but it is not a completed translation. A claim that the entire repository has been reviewed or fully translated would exceed such a bounded manifest.

The distinction also makes openness assessable. UNESCO's 2019 OER Recommendation connects open licensing with capacity, inclusion and sustainable provision. For this handbook, the editorial implication is to budget review and maintenance alongside new content, and to provide a stable reading copy when continuing development is unaffordable.[^living-oer]

## Sources, editions and publication artefacts

Editable source contains arguments, examples, metadata, licences and build instructions. Generated HTML or a review manuscript presents that source to particular readers. Distributed artefacts, such as a source ZIP or static-site archive, are specific byte sequences. They may omit live services, remotely hosted media or externally retrieved data. Before promising offline use, extract a package on another machine, disconnect it from the network and inspect its essential reading paths.

A source commit identifies a revision and its history links. A Git tag names a point in that history; an annotated tag can carry a message and attribution. Tags can be replaced or deleted when permissions permit. A GitHub release associates a tag with notes and assets; it is a separate platform object. GitHub's documented immutable-release option protects associated tags and assets when enabled, while release notes remain editable. These properties were checked on 7 September 2026; this chapter does not claim that the option is enabled here.[^living-git][^living-github]

A scholarly identifier serves another purpose. A DOI or repository identifier connects a publication object to maintained metadata and a landing record; an ISBN belongs to the publisher's bibliographic arrangements. None is a checksum or proof of peer review. Decide with the publisher and deposit institution which object each identifier describes, whether language editions share a record and how versions relate. Zenodo distinguishes using an existing DOI from registering another one; an available registration button is not a reason to create a competing edition record.[^living-zenodo]

Four distinctions from [AI, ethics and reproducibility](ai-ethics-reproducibility.md) remain useful. Technical repeatability asks whether an operation can be repeated under specified conditions. Computational reproducibility asks whether preserved source, code, data and environment support reconstruction. Evidential auditability asks whether a claim can be followed to sources and corrections. Interpretive accountability asks why the editor selected those sources and which alternative readings remain defensible. Identical bytes do not answer that last question. An archived PDF may remain auditable without preserving an executable environment.

## Versioning requires an editorial judgement

Semantic Versioning defines major, minor and patch changes against a software interface contract. A humanities argument has no equivalent automatic compatibility test. Borrow the communication convention cautiously, state the local policy and justify each decision.[^living-semver]

Under this handbook's policy, a patch repairs a typo, broken instruction or metadata error without changing the teaching argument. A minor release adds substantial reviewed material within the existing architecture. A major release marks a substantially revised method, reorganized argument or newly reviewed edition. A one-word change from “supports” to “contradicts” may need more scrutiny than a hundred corrected links. Count the consequence for readers, not changed lines. A correction that alters the teaching argument must not be called a patch merely because it is small.

Dates also need defined meanings: source revision, review completion, release publication and later metadata repair may occur separately. A manifest should record the source commit and included paths, languages, translation status, review scope, licences, source hashes, external dependencies and accessibility findings. Record the build environment and distributed artefact checksums separately. Unassigned identifiers remain explicitly pending; a successful build cannot fill them. Publication must wait wherever the chosen edition requires unresolved review or publisher approval.

For a numbered edition, record the author or editor, publication title, edition version and date, chapter or workflow locator, and the assigned identifier or stable access route for that edition. Use the version you actually read, even if a newer one exists. When your object is deliberately the living `main` branch, say “living edition”, record the full source commit, exact page and access date, and provide a commit-specific source link alongside the reading URL. An access date alone cannot identify which of several same-day revisions supported the claim. Classroom citations can follow the same principle without pretending that a semester snapshot is formally peer reviewed.

## What this handbook currently implements

At the repository inspection for this chapter on 7 September 2026, paired Markdown sources, editorial policies, translation reporting, generated review manuscripts and strict site checks were present. The tag-triggered workflow builds source and site archives, copies manuscripts and translation coverage, computes checksums and uploads an Actions artefact. That workflow alone does not demonstrate permanent deposit, attachment of files to a public GitHub release, publisher approval or DOI/ISBN assignment. Citation metadata is not proof that every file received formal review.

The publisher-coordinated release work is separately scoped in [issue #30](https://github.com/damjan-popic/digital-humanities-handbook/issues/30). It must settle written publisher requirements, identifier responsibilities, package contents and deposit verification before a formal edition is claimed. The [release-planning workflow](../workflows/publishing/create-a-versioned-scholarly-release.md) prepares documentary evidence without performing those operations. An existing build script is a useful component; the full publication service remains a responsibility to establish and verify.

## Worked example: a routine contribution with explicit consent

Consider a hypothetical student addition: a bilingual explanation of distinguishing a place-name mention from a person's residence in an oral-history index. Invented interview excerpts avoid exposing participants in the exercise. Its modest claim is that a supplied coding rule separates two relations in these examples, not that all oral histories can be classified automatically.

The student supplies examples, decisions, a counterexample and a credit preference. A peer checks whether the instructions reproduce the expected table. An editor evaluates the historical inference; a Slovene reviewer checks terminology and equivalent instructions; an accessibility reviewer checks headings and reading order. Their records name the revision and scope. A machine-assisted language pass remains a draft contribution to that process, not completed human review.

Assessment evaluates the submitted research work privately. Publication is offered separately, with an equivalent non-public route, an explanation of the licence and public history, and a clear deadline before release. Declining publication must not reduce the grade. A student may request an agreed public credit form, subject to institutional practice. Release requires rights clearance and editorial acceptance as well as the student's agreement. Later deletion cannot reliably recall copies already redistributed under an open licence.

Once these conditions are met, an editor can accept the workflow into the living edition and propose it for a later minor release. The manifest records which review carried forward. Translation, data curation, software and validation deserve recognition alongside prose authorship. CRediT provides terms for several research roles, but the project must also describe editorial and translation labour in terms contributors recognize; a taxonomy does not settle authorship disputes.[^living-credit]

## Difficult example: a correction after citation

This scenario is invented; its numbered releases and counts do not describe an existing handbook edition. Suppose a hypothetical `1.0.0` chapter says that a classroom table contains 40 distinct historical letters. Four entries prove to be duplicate representations, leaving 36 distinct letters. The exercise teaches source counting, so its worked conclusion changes, although the chapter architecture remains usable.

The editor reproduces the discrepancy, identifies affected passages and tables, and checks both language versions and downloads. The classroom comparison is recalculated; the correction states that the denominator was wrong. Here the editor selects a hypothetical minor `1.1.0`, explicitly reasoning that substantive corrected teaching material fits the existing architecture. A correction overturning the method could require a major reviewed edition. The label records a judgement, not the finding itself.

| Publication location | Required visible record in this scenario |
| --- | --- |
| Source change | A reviewed paired change explains the duplicate criterion, changes 40 to 36 and revises the inference. |
| Changelog | An entry identifies the affected `1.0.0` section, substantive correction and planned `1.1.0`. |
| Erratum | A dated notice states the error, evidence, consequence and replacement; its identifier links the records. |
| Release notes | `1.1.0` links the erratum and describes review scope, regenerated tables and bilingual changes. |
| Stable edition | Original `1.0.0` artefacts retain their identity; their landing record points visibly to the erratum and successor. New files belong to `1.1.0`. |
| Later citation | An analysis using the corrected count cites `1.1.0` and the section; a history of the error cites `1.0.0` together with its erratum. |

Readers of downloaded copies may never revisit the website. Where proportionate, notify known course maintainers and deposit services through established channels. A correction notice should explain consequences without requiring readers to reconstruct a Git diff. The [correction workflow](../workflows/publishing/correct-a-published-digital-resource-without-erasing-history.md) turns this chain into an assessable record.

## Correction, withdrawal and the limits of public history

A correction repairs an identified fault. An erratum is the visible notice describing it; its terminology should follow publisher policy. Deprecation warns that a readable workflow is no longer recommended, perhaps because its service changed. Supersession identifies a successor without declaring every earlier claim false. Retraction withdraws reliance on seriously unreliable or otherwise unacceptable work through an editorial process. Avoid collapsing these actions into “updated”. COPE emphasizes the purpose and visibility of retraction notices; apply its journal-oriented guidance cautiously to the relevant digital object.[^living-cope]

Preserving cited versions is the normal scholarly rule, not an instruction to expose private information indefinitely. If identifying interview data or a secret credential is published, stop further dissemination through the responsible institutional process. An innocuous notice can preserve the fact, date and scope of removal without repeating the harmful content. History, caches, deposits and mirrors may require coordinated restriction or removal; a new commit alone is inadequate. Retain necessary evidence only under authorized restricted access and applicable retention rules. Do not promise complete erasure from third-party copies or prescribe a legal outcome without institutional advice.

## Rights and governance are publication infrastructure

The handbook's original prose uses CC BY 4.0 and original code uses MIT. Third-party material retains its own conditions. Distinguish an openly licensed explanation from a reproduced image, quotation or externally obtained dataset. CC BY 4.0 requires attribution and indication of changes; it does not clear privacy, publicity or moral-rights issues. State exceptions at the object, not only in a distant repository file.[^living-cc]

A possible non-exclusive publisher agreement should preserve the agreed ability to maintain and redistribute the open edition while assigning production, deposit and correction duties. Its wording requires agreement; this chapter reports neither a signed contract nor legal approval. Publisher recognition, hosting, copyright ownership and repository administration can belong to different parties. Name who decides scholarly disputes, reviews translations, handles urgent removals and authorizes releases, with a substitute where that person has a conflict of interest.

## Maintenance, preservation and succession

A working site accumulates obligations: dependencies age, links move, credentials expire and examples cease to behave as described. Technical debt includes undocumented editorial exceptions and translation drift as well as code. Prioritize defects by their effect on evidence, access and safety. A changed interface may warrant a dated warning and tested alternative. A broken historical reference requires checking whether a replacement still supports the claim; a successful HTTP response does not establish continuity.

Preservation needs more than another download link. Agree with a repository which files it accepts, what it preserves, who maintains landing metadata and how it handles later versions. Check SHA-256 values after transfer and rehearse retrieval. Checksums detect byte changes against a trusted baseline; they do not establish interpretive correctness. Preserve sources and relevant dependencies alongside reading copies where rights permit. Record missing external components as limitations rather than describing the package as self-contained.[^living-fixity]

Format migration creates another documented transformation. Define what must survive: encoding, footnote targets, headings, table relations and source locators may matter more than matching line breaks. Compare the converted copy with the original, record the environment, retain an appropriate original and calculate new checksums. The Digital Preservation Coalition stresses significant properties and validation when selecting formats and migration routes; a filename extension is no guarantee.[^living-formats]

Accessibility continues after an initial audit. Keyboard access, heading order, text alternatives, language metadata and readable tables can regress when content or tools change. WCAG 2.2 supplies testable criteria, but automated checks cover only part of the assessment. State pages, formats, criteria, assistive technologies and known exceptions tested. Accessible HTML does not prove that a generated PDF has correct reading order.[^living-wcag]

The founding editor's departure should trigger a procedure, not a search through private email. Name an organizational owner, editorial successor and technical contact. Document repository and domain control, renewals, dependency records, protected credential references, backups and a restore test. Never publish passwords in the plan. A successor should rehearse a build and correction before transfer. If no successor or budget is available, close contributions, state the final maintenance date, deposit the last suitable edition and mark unsupported workflows. An honestly closed resource can serve scholarship better than an apparently living site with no responsible maintainer. The [maintenance and succession workflow](../workflows/publishing/prepare-a-maintenance-and-succession-plan.md) makes these commitments testable.

## Practice

In pairs, inventory six objects from a small teaching project: paired chapters, a workflow, a dataset, a generated reading copy and its build instructions. Prepare the three linked workflow records. Keep identifiers and checksums explicitly pending until obtained; do not create public releases. Allocate a realistic two-hour monthly maintenance budget and explain what it cannot cover.

Exchange records. One student plays a reader who downloaded the earlier release; the other introduces the duplicate-letter error or an accidental personal-data disclosure. Trace discovery, review, notice, replacement and citation. Check whether every promised artefact has an owner, every review claim names its scope, and the privacy case avoids repeating the exposure. Submit revised records and a rationale for one disputed decision. Assess reasoning and evidence, not willingness to publish.

## Reflection

- Which publication claims follow from files, and which require institutional commitments?
- When does historical accountability require limiting public access?
- What would a Slovene reader miss if only the English correction appeared?
- Which responsibility becomes ownerless if the maintainer leaves tomorrow?

## Summary

A living scholarly publication makes its changing authority inspectable. Reviewed scope, identifiable editions, correction trails and careful citation connect evidence across time. Governance, consent, rights, accessibility and tested preservation make those records usable. Readers should be able to identify what was published, what changed, why it changed and who can still answer for its care.

## Further reading

- UNESCO. 2019. [Recommendation on Open Educational Resources (OER)](https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer). Read its sustainability provisions alongside the publication budget.
- Digital Preservation Coalition. [Fixity and checksums](https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums) and [File formats and standards](https://www.dpconline.org/handbook/technical-solutions-and-tools/file-formats-and-standards), *Digital Preservation Handbook*. Define verification and migration responsibilities.
- COPE. [Retraction guidelines](https://doi.org/10.24318/cope.2019.1.4), version 3, 2025. Distinguish unreliable findings from a transparently corrected limited error.
- GitHub. [Immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases). Check which objects a protection covers.
- W3C. [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/). Pair automated validation with manual assessment.

All external documentation below was checked on **7 September 2026**. COPE's current guidance was verified through indexed official content; direct page retrieval was unavailable. Recheck service behaviour and institutional arrangements for an actual release.

[^living-oer]: UNESCO, [Recommendation on Open Educational Resources (OER)](https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer), adopted 25 November 2019.
[^living-git]: Scott Chacon and Ben Straub, *Pro Git*, second edition, [Git Basics—Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging).
[^living-github]: GitHub Docs, [About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) and [Immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases).
[^living-zenodo]: Zenodo, [Digital Object Identifier (DOI)](https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/).
[^living-semver]: Tom Preston-Werner, [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).
[^living-credit]: NISO, [CRediT—Contributor Role Taxonomy](https://credit.niso.org/).
[^living-cope]: COPE, [Retraction guidelines](https://doi.org/10.24318/cope.2019.1.4), version 3, August 2025.
[^living-cc]: Creative Commons, [Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).
[^living-fixity]: Digital Preservation Coalition, [Fixity and checksums](https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums).
[^living-formats]: Digital Preservation Coalition, [File formats and standards](https://www.dpconline.org/handbook/technical-solutions-and-tools/file-formats-and-standards).
[^living-wcag]: W3C, [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/).
