---
title: "The living open handbook"
description: "How a reviewed scholarly edition and a continuously maintained teaching resource can coexist without confusing authority, authorship or citation."
tags: [open-education, versioning, peer-review, contribution, publishing]
status: draft
---

# The living open handbook

## Learning outcomes

After this chapter, you should be able to:

- distinguish a living edition from a stable reviewed release;
- cite a versioned digital publication correctly;
- design contribution, review and translation workflows;
- explain how Git, GitHub Pages and an archive serve different publication functions;
- evaluate whether an update requires a patch, minor or major release.

## Before you begin

A printed software tutorial can be obsolete before students open it. A constantly changing website can be impossible to cite or review. The solution is not to choose between permanence and change. It is to give each a defined layer.

## Two editions, one publication

This handbook separates:

1. the **living edition** on the default branch, where corrections, new workflows and translations are developed; and
2. a **stable release**, identified by a version tag, date and archived snapshot.

The living edition supports teaching and maintenance. The stable release is the object of formal review, citation and preservation. Readers can always see which edition they are using.

This model is common in software and data publishing, but it also suits fields whose methods and interfaces change rapidly. The conceptual chapters should change slowly; practical workflows can be updated more frequently.

## Roles of the publication infrastructure

Different components have different jobs:

- **Git repository:** source files, history, issues, review and contributions;
- **GitHub Pages:** readable public web edition;
- **tagged release:** frozen set of files representing an edition;
- **archival repository:** long-term record and persistent identifier;
- **publisher record:** peer review, metadata, cataloguing and institutional recognition;
- **optional PDF snapshot:** offline, deposit and review format, not the editorial master.

No single platform should carry every responsibility. A URL to a branch is not an archive, and a PDF is not a maintainable source.

## Version numbers communicate meaning

A practical semantic scheme is:

- **patch** release, such as 1.0.1: corrections that do not materially change method or learning outcomes;
- **minor** release, such as 1.1.0: new workflows, translations or backward-compatible additions;
- **major** release, such as 2.0.0: substantial reorganization, changed methodological recommendations or a newly reviewed edition.

Every release should include a changelog, citation metadata and a statement of review status. Do not silently rewrite an archived edition.

## Citation and review status

The site should display:

- current version or development status;
- publication and last-updated dates;
- preferred citation;
- DOI or archival identifier when assigned;
- editorial and peer-review statement;
- licences for text, code and data;
- link to the exact source revision.

A reader citing a research claim should cite the stable version used. A classroom may use the living edition and record the commit or semester release.

## Contribution is not unmoderated editing

Openness means that people can propose and inspect changes, not that every change is published automatically. A contribution workflow should require:

1. a defined problem and intended audience;
2. source and rights checks;
3. a reproducible minimal example;
4. expected output and failure modes;
5. editorial and technical review;
6. language review where relevant;
7. disclosure of contributor role and licence agreement;
8. automated checks before merge.

Students can be genuine contributors. Their work should be credited, reviewed and licensed with informed agreement. Assessment and publication decisions must be separated so that students are not coerced into public authorship.

## Bilingual publication is editorial work

A language switch is a technical feature; a bilingual handbook requires editorial equivalence.

Each language version needs:

- idiomatic terminology rather than mechanical word replacement;
- aligned learning outcomes and examples;
- a way to mark missing or outdated translations;
- reviewers competent in the relevant language and field;
- translation provenance and date;
- a policy for changes that affect only one language.

The versions need not be identical sentence by sentence. They should support equivalent learning and make differences visible. The default language may temporarily provide fallback pages, but missing translations must not masquerade as complete coverage.

## Governance prevents the bus-factor problem

A living resource should not depend on one person's memory. Record:

- editor and maintainer roles;
- who can approve content, translation and technical changes;
- review intervals for software-dependent pages;
- labels for tested, outdated or archived workflows;
- correction and takedown procedures;
- succession and repository ownership arrangements;
- how conflicts of interest are handled.

Governance makes openness durable. It also lets a publisher recognize a changing project without assuming that every commit has undergone formal peer review.

## A release workflow

A formal release can follow these steps:

1. declare a content freeze and release candidate;
2. run automated link, structure and code checks;
3. complete scholarly and didactic review of the stable core;
4. resolve required changes and record reviewer approval;
5. complete language and accessibility checks;
6. tag the source and build the web/PDF artifacts;
7. archive the release and mint or register its persistent identifier;
8. publish citation metadata and release notes;
9. reopen the living edition for development.

This preserves both accountability and momentum.

## Worked example: a student contribution

A student proposes a workflow for mapping places in oral-history transcripts.

- The student submits a small anonymized sample, method, output and limitations.
- A peer reproduces the steps.
- An editor reviews privacy, geocoding uncertainty and terminology.
- The contribution is revised and credited.
- It enters the living edition as a reviewed workflow.
- At the next minor release it becomes part of a stable archived edition.

The student's work is real scholarly communication, not disposable homework, while the editorial process protects readers and participants.

## Practice

Take one digital teaching resource and draft its publication architecture. Identify the living source, stable release, archive, citation, editorial roles, contribution route, translation policy and criteria for a major new edition.

## Reflection

- What exactly has been peer reviewed: every page, the core chapters or one release?
- How will a reader know that a software-dependent workflow is still current?
- Who owns and can maintain the project if the original editor leaves?

## Summary

A living handbook can be open and academically citable when development and publication are separated clearly. Git supports history and contribution, a web site supports reading, tagged releases support review, and an archive supports preservation. Versioning, governance, bilingual editorial policy and explicit review status turn continuous change from a weakness into a documented scholarly method.
