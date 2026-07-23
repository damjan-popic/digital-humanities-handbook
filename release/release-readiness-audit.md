# Release-readiness audit

**Snapshot:** 2026-07-23  
**Audited target:** a future formally reviewed `v1.0`  
**Current verdict:** **strong development release and credible review candidate; not yet ready to be labelled the formally reviewed `v1.0` edition.**

This audit treats the public web edition, version-controlled source, generated review manuscripts, course paths, workflows, case studies and release policy as one publication system.

## Ready now

| Area | Finding | Evidence |
| --- | --- | --- |
| Stable core | Sixteen English–Slovene chapter pairs exist in one canonical four-part order. | [`scripts/handbook_structure.py`](../scripts/handbook_structure.py), [`scripts/check_handbook.py`](../scripts/check_handbook.py) |
| Course use | Two paired fourteen-module learning paths connect the core to *Pismenost za informacijsko družbo* and *Digitalna slovenistika*. | [`docs/en/learning-paths/`](../docs/en/learning-paths/), [`docs/sl/learning-paths/`](../docs/sl/learning-paths/) |
| Build reproducibility | Dependencies are pinned or bounded, CI uses Python 3.12, generated catalogues are checked, and the site is built with strict MkDocs validation. | [`requirements.txt`](../requirements.txt), [`Makefile`](../Makefile), [Pages workflow](../.github/workflows/pages.yml) |
| Bilingual architecture | The stable chapters and course paths are paired; language switching and English fallback are explicit. | [`release/translation-coverage.md`](translation-coverage.md), [`TRANSLATION_POLICY.md`](../TRANSLATION_POLICY.md) |
| Rights and reuse | Original prose is CC BY 4.0, code is MIT, and contributors must identify third-party material. | [`LICENSE.md`](../LICENSE.md), [`CONTRIBUTING.md`](../CONTRIBUTING.md) |
| Citation and editions | Citation metadata, semantic versioning rules, a changelog and deterministic review manuscripts are present. | [`CITATION.cff`](../CITATION.cff), [`VERSIONING.md`](../VERSIONING.md), [`CHANGELOG.md`](../CHANGELOG.md) |
| Intertextuality | One validated map connects chapters, workflows and case studies; the web edition and review manuscripts render the same conceptual-to-practical trails. | [`intertextuality.yml`](../intertextuality.yml), [`scripts/check_intertextuality.py`](../scripts/check_intertextuality.py), [ecosystem page](../docs/en/ecosystem.md) |
| Repository hygiene | Merged-branch cleanup is automated and future merged branches are configured for deletion. | [branch-hygiene workflow](../.github/workflows/branch-hygiene.yml) |

## Blockers before a formal `v1.0`

### 1. Formal scholarly review is not complete

The current site is a development edition. Stable pages retain development/draft status until the promised external and editorial review has been completed. A formal release needs:

- named reviewers and a documented review scope;
- an editorial response record;
- confirmation that blocking review comments were resolved;
- a release note that distinguishes reviewed stable chapters from the more rapidly changing practical library.

### 2. Release artefacts still need to be frozen

The repository defines the required release model, but a `v1.0` package still needs:

- a frozen release manifest listing included pages and translation status;
- a `v1.0` Git tag and GitHub release;
- final `CITATION.cff` version/date metadata;
- archived review manuscripts and, where useful, PDF/EPUB snapshots;
- checksums for deposited release files.

### 3. Persistent preservation is not yet confirmed

A formal edition should be deposited in an appropriate long-term repository and receive a persistent identifier where possible. GitHub and GitHub Pages remain the development and reading infrastructure, not the sole preservation plan.

### 4. Publisher and licence compatibility must be settled in writing

Before a publishing agreement is signed, confirm that the publisher accepts:

- the web edition as the primary publication;
- continued public development of `main`;
- the existing CC BY 4.0 and MIT licensing model;
- a non-exclusive or otherwise compatible rights arrangement;
- a frozen, citable release as the formally reviewed edition.

### 5. Whole-book language and terminology review remains necessary

Individual chapters have received focused Slovene passes, but `v1.0` still needs a continuous whole-book copy-edit. The review should normalize terminology, register, punctuation, institutional names, translated technical terms and cross-chapter repetition without flattening genuine disciplinary disagreement.

### 6. Bibliographic and time-sensitive facts need a final release-date audit

Before freezing `v1.0`:

- normalize bibliography style across all chapters;
- recheck mutable institutional descriptions, organizer lists, service versions and access dates;
- verify every DOI and persistent identifier;
- record any intentionally unresolved metadata discrepancy in the release notes.

### 7. External links need a release audit

Strict MkDocs validation protects internal links and navigation, not the continued availability or redirected meaning of every external source. Run and document a final external-link audit, treating rights-controlled, institutional and versioned resources carefully rather than automatically rewriting URLs.

### 8. The practical library needs an explicit translation decision

The stable core is bilingual, but the repository-wide report currently records **46 Slovene counterparts among 127 English Markdown pages (36.2%)**, with 81 English fallback pages. This is acceptable for a transparently bilingual core with a growing practical library only if the release statement says so clearly. Otherwise, define a smaller required Slovene subset for `v1.0` and complete it before release.

## Ready after editorial review, but not release blockers by themselves

- Final glossary alignment across the sixteen chapters.
- A consistency pass on chapter summaries, learning outcomes and exercise labels.
- A documented usability test of Slovene search, because the current search stack does not provide a dedicated Slovene Lunr language configuration.
- Manual accessibility checks with keyboard navigation, zoom, dark mode and at least one screen reader.
- A final responsive inspection of large tables and the generated ecosystem map.

## Deferred improvements

- Translate additional workflows and case studies according to teaching priority rather than raw page count.
- Add an optional PDF/EPUB production pipeline after the web edition is stable.
- Add automated external-link and accessibility regression checks if they can be made reliable enough not to punish maintainers with noisy failures.
- Add more public case studies only when their purpose, run path, rights, licence and limits can be documented responsibly.

## Repository-hygiene record

Before this audit, two stale branches from already merged pull requests were still reachable:

- `chore/codex-editorial-workflow`;
- `codex/issue-3-dh-histories`.

The merged-branch hygiene workflow introduced by this audit enables GitHub's automatic branch deletion and removes remaining same-repository branches whose pull requests are already merged. Its workflow summary is the authoritative deletion record. It never deletes the default branch, a protected branch or an unmerged branch.

## Recommendation

Use the current edition for teaching, piloting and publisher discussion. Present it as a **development release and review candidate**, not yet as the formally reviewed `v1.0`. Begin formal review only after the ecosystem and audit pull request has passed CI and been visually inspected; freeze `v1.0` only after the eight blockers above have owners, evidence and completion dates.
