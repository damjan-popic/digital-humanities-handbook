# Case-study metadata and critical-content contract

This framework implements phase 1 of issue #27, not the eight showcase additions or the final browsing interface. The catalogue currently retains every legacy case. `showcase-v1` is a content standard, not a release name or a claim of human scholarly approval.

## One source for each kind of fact

- Edit descriptive records in `data/case-studies.yml` (`schema_version: 2`, `cases:` list). Do not author either connection field there.
- Edit conceptual chapter/workflow relationships only in `intertextuality.yml`. Its existing untyped model remains authoritative; issue #28 owns typed relation semantics.
- Record dated primary-source observations and remediation in `release/case-study-audit.md`.
- `scripts/build_case_study_index.py` validates the source, then writes `data/case-studies-index.json` and both case-study indexes. Never edit these three outputs manually.
- `data/case-study-schema.json` is the JSON Schema 2020-12 contract. Its enums and `x-labels` contain the canonical codes and English/Slovene catalogue labels; this guide documents their scope.

Ordering is deterministic: records by `case_id`, JSON keys in schema-property order (including nested rights records), unordered facet lists including `inspection_modes` lexicographically, rights components in the fixed order code/data/documentation/source-material/images/interface-content, and conceptual links in the authoritative map's authored order. Writers emit UTF-8/LF with a final newline; there are no generated current timestamps or network-dependent results.

## Fields

| Field | Meaning and constraint |
| --- | --- |
| `case_id` | Stable case identifier (CASE- plus a lowercase slug-like identifier); never reused for another scholarly object. |
| `slug` | Stable lowercase hyphenated page stem; unique across the catalogue. |
| `title_en` | Exact English page frontmatter title; null only when the English page is absent. |
| `title_sl` | Exact Slovene page title, not a translated catalogue substitute; null when no Slovene case page exists. |
| `page_en` | Repository-relative docs/en/case-studies/SLUG.md; null only for an explicitly Slovene-only or deferred catalogue-only record. |
| `page_sl` | Matching docs/sl/case-studies/SLUG.md; null when absent. A generated fallback URL is not a page. |
| `project_url` | Public project homepage, or the repository landing page if no separate project site was verified. HTTP(S) syntax is checked offline. |
| `repository_url` | Public source repository location; null when none is known. A repository is not required for an interface/documentation case. |
| `method_domains` | One or more controlled methodological facets; facets are not quality scores. |
| `source_types` | One or more controlled source-object facets; not filenames or rights assertions. |
| `inspection_modes` | One or more actual inspection modes, with no rank or opaque mixed value. Documentation and repository inspection remain separately filterable; a local run must never be inferred. |
| `languages_regions` | One or more controlled language/context facets; not a claim of representative coverage. |
| `code_availability` | Public inspectability of implementation code; publicly-inspectable says nothing about an open-source licence, permission or successful execution. |
| `reusable_data_availability` | An evidenced data-access/reuse path; public filenames or repository visibility do not establish permission. |
| `rights_status` | Verification summary deterministically checked against rights_components using the rules below. Unknown does not suppress a project declaration. |
| `rights_components` | Exactly six component records, one for each controlled component, with declaration/verification status, terms, scope and a real case-specific audit locator. No top-level licence can stand in for these records. |
| `translation_status` | Presence and review state of actual case pages. Eleven existing English-only cases use english-fallback. |
| `lifecycle_status` | Dated factual state of the external project/resource: current, maintenance-unclear, archived or unavailable. Never an editorial deferral or recommendation. |
| `editorial_disposition` | The handbook's controlled decision/recommendation for the case, distinct from external project lifecycle and content maturity; the audit explains its scope. |
| `evidence_status` | Neutral basis of handbook assertions. Source-evidence-inspected does not imply an independent reviewer; multiple inspection modes are recorded separately. |
| `repository_relationship` | Repository location or documented fork/collaboration, not inferred intellectual, project or institutional ownership. The audit states which fact was observed. |
| `last_checked` | Quoted ISO calendar date YYYY-MM-DD, valid and not in the future. Manual dated observation, not a CI link ping. |
| `content_standard` | Critical-content maturity. Legacy and deferred pages never become v1-complete just by migrating metadata. |
| `audit_record` | Local release/case-study-audit.md#case-SLUG anchor; section must identify this case and matching check date. |
| `short_summary_en` | Plain-text cautious English catalogue summary; null only when its language page is absent. |
| `short_summary_sl` | Plain-text Slovene summary for an actual paired page; null for English fallback. Localized facet labels do not imply translated case content. |
| `chapter_connections` | GENERATED from intertextuality.yml case_studies entry, preserving map order; no second authored list. |
| `workflow_connections` | GENERATED from the same authoritative entry, preserving map order. |
| `connection_remediation` | Null when both relation lists are populated; otherwise an explicit substantive note also present verbatim in the audit. This exception is unavailable to showcase-v1. |

## Component-level rights

Every case has one record for each of `code`, `data`, `documentation`, `source-material`, `images` and `interface-content`. These are bounded evidence records, not a claim that every project has every component. A component not inspected, not distributed or lacking identified terms normally remains `unknown`; use `not-applicable` only with a specific reason why it is outside this case's declared inspection/reuse scope.

| Component-record field | Meaning and constraint |
| --- | --- |
| `component` | Controlled component code; every code appears exactly once. |
| `status` | Controlled declaration/verification status. A project declaration is not a verified grant. |
| `licence_or_terms` | Exact licence identifier or a faithful, attributed account of declared terms/restrictions. Null for unknown/not-applicable; nonempty for project-declared/verified-open/verified-restricted. Do not replace a known declaration with null merely because its scope remains unverified. |
| `scope_note` | Substantive component-specific explanation of material covered, evidence limits and unresolved applicability (at least 20 characters and four words). A short structural minimum cannot establish rights. |
| `audit_locator` | `release/case-study-audit.md#rights-SLUG-COMPONENT`; a unique real anchor inside this case's audit section. The linked row supplies the dated observation and precise source locator. |

Declarations are not propagated automatically across components: a code manifest saying MIT does not license source texts, documentation, images or interface content. Pracomul's code MIT declaration and unnamed non-commercial transcript terms are recorded separately; its derived tables do not inherit a licence by assumption. Vejice's package-manifest MIT declarations retain their unverified scope. Jezikovni svetovalec's private-course and no-redistribution warnings are declarations of restrictions, **not grants of permission**.

The catalogue shows all six component statuses and any recorded terms, with component audit links. Licence identifiers are preserved unchanged. Recorded terms may be faithful editorial summaries, not verbatim source quotations; they remain in the language of the metadata record, which is not necessarily the language of the underlying source. The Slovene catalogue explicitly labels this text as untranslated. Localized labels do not claim a Slovene translation of a case or an authoritative legal translation.

### Deterministic rights summary

`rights_status` remains explicit in authored metadata but must equal this calculation; inconsistent summaries fail validation rather than being silently repaired:

1. Ignore components marked `not-applicable`.
2. If no components remain, the summary is `not-applicable`.
3. If none of the remaining components is verified-open or verified-restricted, the summary is `unknown`. This includes project-declared terms whose scope is unverified.
4. If every remaining component is verified-open, the summary is `verified-open`; if every one is verified-restricted, it is `verified-restricted`.
5. Otherwise at least one component is verified and the statuses differ: the summary is `mixed`. Inspect the actual component records, including unknown or project-declared ones.

The summary reports verification coverage/status, not a universal licence. Different licence identifiers and scopes remain distinct even when their verification status is the same. CI checks record coherence and local evidence locators; it cannot authenticate permission, reviewers or legal applicability.

## Lifecycle, disposition and repository relationship

The three fields answer different questions. `lifecycle_status` records a dated observation about the external resource. `editorial_disposition` records what the handbook proposes to do with its case. `content_standard` records whether the written case is legacy, showcase-v1 or deferred content. An accessible project can have unclear maintenance while its source-dependent classroom use is deferred; a recommendation to archive a handbook case does not make the external project archived.

All eleven existing project lifecycles remain `maintenance-unclear` on the original inspection evidence. The existing recommendations become five retain-and-upgrade, five retain-as-legacy and one defer. Jezikovni svetovalec retains legacy-audited content; its disposition alone records the deferral.

A repository on the editor's account is not necessarily the editor's intellectual or institutional project. The documented-fork-or-collaboration category takes precedence where that relationship is evidenced, and the audit must say whether it is a fork, collaboration or both. Vejice is a documented fork; collaboration is not inferred from that fact. The other ten records describe repository location only. Unknown and not-applicable relationships support cases without an established repository route.

## Controlled vocabulary

Codes stay identical across editions. Labels are localized; booleans/nulls and licence identifiers are not translated. No code below establishes legal clearance, independent scholarly review, project ownership, exhaustive inspection or guaranteed future availability.

### method_domains

| Code | Meaning; what it does not claim |
| --- | --- |
| `corpus-building` | Collecting and preparing a bounded corpus, not evidence that collection is representative. |
| `linguistic-annotation` | Assigning linguistic labels; not a guarantee of annotation accuracy. |
| `text-analysis` | Comparing textual features; not interpretation without source reading. |
| `data-modelling` | Representing units and relations; not a neutral or exhaustive model. |
| `gis` | Spatial representation or analysis; not verified coordinates or boundaries. |
| `networks` | Constructing or inspecting relations; not proof of historical connection. |
| `ai-retrieval` | AI-assisted or retrieval workflows; not validated generated claims. |
| `scholarly-publishing` | Publication infrastructure; not a reviewed or preserved edition. |
| `writing-support` | Tools supporting writing; not validated language advice. |
| `digital-editions` | Editorial representation of sources; not an authoritative edition by default. |
| `ocr-htr` | Text recognition; not checked transcription. |
| `accessibility` | Accessibility as a subject; not certified conformance. |
| `public-engagement` | Work with publics; not proof of consent or community authority. |
| `relational-databases` | Representing and querying relational tables, keys and joins; not generic modelling or proof of data validity. |
| `reference-management` | Organizing references, citation metadata and identifiers; not verified bibliographic accuracy. |
| `scholarly-writing` | Developing scholarly arguments, evidence and drafts; not generic writing assistance or completed peer review. |

### source_types

| Code | Meaning; what it does not claim |
| --- | --- |
| `web-pages` | Web documents; public access does not grant redistribution. |
| `corpus-text` | Text grouped as a corpus; representativeness remains a question. |
| `learner-writing` | Learner-produced material; consent and privacy require separate evidence. |
| `dialogue-transcripts` | Transcribed interaction, shaped by transcription choices. |
| `historical-documents` | Historical records; not automatically public domain in every form. |
| `metadata` | Descriptions and identifiers; potentially sensitive and fallible. |
| `structured-records` | Tables or graph records; not verified relationships. |
| `scholarly-text` | Research/reference prose with source-specific rights. |
| `office-documents` | Document-application inputs; may contain private text. |
| `interaction-transcripts` | User/system exchanges; publication does not establish participant permission. |
| `images` | Visual source objects; licences must be checked separately. |
| `maps` | Cartographic sources; georeferencing is an interpretation. |
| `audio` | Recorded sound; speaker and performance rights remain relevant. |

### inspection_modes

| Code | Meaning; what it does not claim |
| --- | --- |
| `interface-inspected` | Specific visible interface elements were inspected, not its hidden implementation. |
| `documentation-inspected` | Documentation was read; its claims are not independently executed results. |
| `repository-inspected` | Named source files were read; their execution or advertised correctness is not established. |
| `data-inspected` | Named data records or exports were inspected, not the whole collection. |
| `locally-run` | A dated bounded path was executed with recorded inputs/environment/results; not full reproducibility. |

### languages_regions

| Code | Meaning; what it does not claim |
| --- | --- |
| `slovene` | Slovene is materially relevant; not a coverage claim. |
| `slovenia` | Slovenian context; not national representativeness. |
| `spanish` | Spanish-language material or documented scope. |
| `spain` | Spanish regional scope where documented. |
| `latin` | Latin-language material or documented scope. |
| `adriatic` | Adriatic historical scope where documented. |
| `ladakh` | Ladakh-related material; not community authorization. |
| `himalaya` | Himalayan scope where documented. |
| `multilingual` | More than one language is materially in scope; not universal language support. |
| `not-specified` | Inspected evidence does not establish language/region coverage. |

### code_availability

| Code | Meaning; what it does not claim |
| --- | --- |
| `publicly-inspectable` | The core source is publicly readable. This states access, not an open-source licence, verified reuse permission or a successful run. |
| `partial` | Some implementation is public but a consequential part is missing. |
| `unavailable` | A required implementation could not be accessed on the audit date. |
| `not-applicable` | The lawful inspection does not depend on project code; not a completeness failure. |
| `unknown` | Evidence was insufficient to classify source availability. |

### reusable_data_availability

| Code | Meaning; what it does not claim |
| --- | --- |
| `open-download` | An inspected public download has documented reuse conditions; not necessarily unrestricted or complete. |
| `mediated-access` | A documented request/access process exists; access has not necessarily been granted. |
| `sample-only` | Only a bounded sample has an evidenced reuse path; not the full dataset. |
| `metadata-only` | Only descriptive/derived records have an evidenced reuse path, not source texts. |
| `unavailable` | No usable authorized data path was verified; public-looking files do not resolve rights. |
| `not-applicable` | The case does not require a distributed dataset. |
| `unknown` | Access or reuse conditions could not be established. |

### rights_status

| Code | Meaning; what it does not claim |
| --- | --- |
| `verified-open` | All applicable component records are verified-open within their documented scopes; not a universal grant for dependencies or other material. |
| `verified-restricted` | All applicable component records have verified restricted terms within their scopes; this is not legal clearance. |
| `mixed` | At least one component is verified, but applicable component statuses differ. Consult each record; no single licence covers the whole case. |
| `unknown` | No applicable component has verified terms. Project-declared licences or warnings may still be recorded and must not be discarded. |
| `not-applicable` | All six components are explicitly outside the documented inspection/reuse scope; not a general exemption from rights. |

### rights_component

| Code | Meaning; what it does not claim |
| --- | --- |
| `code` | Implementation source and scripts; does not automatically include dependencies or other components. |
| `data` | Project datasets, annotations or derived outputs in the stated scope; does not silently inherit code or source-material terms. |
| `documentation` | README, manuals and explanatory prose; a code declaration need not license documentation. |
| `source-material` | Underlying texts, transcripts, documents or other sources; access, consent and edition rights remain distinct. |
| `images` | Visual material, scans and illustrations where relevant; neither subject age nor web access establishes permission. |
| `interface-content` | Interface text, displayed content and assets in the stated scope; not automatically covered by implementation-code terms. |

### rights_component_status

| Code | Meaning; what it does not claim |
| --- | --- |
| `unknown` | No licence/terms declaration or applicable grant was established for this component and scope. Absence or non-inspection is explained in scope_note. |
| `project-declared` | A project source declares a licence, terms or restriction warning, but applicability and scope have not been established beyond that declaration. Not a verified reuse grant. |
| `verified-open` | Applicable open terms were checked against the exact component and scope named in the audit; not all project materials. |
| `verified-restricted` | Applicable restricted terms were checked for the stated component and scope; not automatic authorization to use restricted material. |
| `not-applicable` | The component is explicitly outside the bounded case inspection/reuse scope, with a rationale. This does not assert that the project contains no such material. |

### translation_status

| Code | Meaning; what it does not claim |
| --- | --- |
| `paired-draft` | Both case pages exist; human language approval is not claimed. |
| `paired-human-reviewed` | Both pages and named dated human translation-review metadata exist; CI cannot authenticate a review. |
| `english-fallback` | No Slovene case page; translated catalogue labels do not count as a translation. |
| `slovene-only` | A Slovene case page exists without an English page; requires explicit editorial scope approval. |
| `not-applicable` | Reserved for an explicitly deferred catalogue-only record with no case page; not a translation shortcut. |

### lifecycle_status

| Code | Meaning; what it does not claim |
| --- | --- |
| `current` | Dated evidence supports active maintenance; not a service-level commitment. |
| `maintenance-unclear` | Resource may be reachable but sustained maintenance/responsibility is not established. |
| `archived` | Project declares archival/read-only status; not proof of preservation. |
| `unavailable` | Expected public resource was inaccessible on the audit date; not proof it no longer exists. |

### editorial_disposition

| Code | Meaning; what it does not claim |
| --- | --- |
| `retain-and-upgrade` | Retain this handbook case and recommend later critical-content work; not completed upgrade or project maintenance. |
| `retain-as-legacy` | Keep the audited legacy case visible pending prerequisites; not a permanent scholarly exemption. |
| `defer` | Defer the handbook use identified in the audit pending prerequisites; not a project lifecycle state or deletion. |
| `archive` | Recommend archiving the handbook case; does not say that the external project is archived. |
| `replace` | Recommend a later replacement of the handbook case; the current audited record stays visible until an explicit editorial change. |

### evidence_status

| Code | Meaning; what it does not claim |
| --- | --- |
| `project-description-only` | Only project self-description supports the case; no source-evidence inspection beyond that description is claimed. |
| `source-evidence-inspected` | Named source evidence was inspected beyond repeating a description. This makes no claim of reviewer independence, ownership or scholarly approval. |
| `locally-tested` | A dated bounded local result supports a claim; not universal functionality, independent review or exhaustive reproduction. |

### repository_relationship

| Code | Meaning; what it does not claim |
| --- | --- |
| `editor-account` | The inspected repository is located on the handbook editor's account. This does not establish intellectual, project or institutional ownership. |
| `documented-fork-or-collaboration` | A source records a fork relationship or collaboration; the audit specifies which. A fork alone does not establish collaboration or project ownership. |
| `external-repository` | The inspected repository is outside the editor's account and no collaboration is documented in the audit; not an assertion of independence or ownership. |
| `unknown` | Evidence does not establish a repository relationship; no project role is inferred. |
| `not-applicable` | No repository is part of this case's declared inspection route; not a defect in a responsible interface/documentation case. |

### content_standard

| Code | Meaning; what it does not claim |
| --- | --- |
| `legacy-audited` | Existing page has a dated audit and explicit remediation; it is not a completed showcase. |
| `showcase-v1` | All required critical-case sections and paired page declarations are validated; not a numbered release or human scholarly approval. |
| `deferred` | Content is retained/deferred with an audit record; not a completed showcase. |

## Version 2 migration

This is a breaking metadata-semantic migration within the draft phase-1 PR, before any new showcase batch. Authored `schema_version: 2` is required; obsolete fields/codes fail rather than being accepted as aliases.

| Version 1 | Version 2 |
| --- | --- |
| `lifecycle_status: deferred` | Factual lifecycle plus separate `editorial_disposition: defer` |
| `evidence_status: independently-inspected` | `source-evidence-inspected`, with no independence claim |
| `editor_relationship` with editor-owned/collaborative/external | `repository_relationship` describing account location or an evidenced fork/collaboration; no automatic project-ownership inference |
| `code_availability: open` | `publicly-inspectable` |
| Singular `inspection_depth` or opaque mixed inspection/evidence | Nonempty `inspection_modes` list plus a neutral evidence-status code |
| Overall `licence` string/null | Six `rights_components` records; a checked verification summary remains in `rights_status` |

The method vocabulary adds relational-databases, reference-management and scholarly-writing. No existing case acquires these facets merely through an analogous handbook link; their current counts are zero. This revision preserves all eleven cases and the 2026-09-09 source-inspection date. The metadata correction date is not a new external access date.

## Pages, evidence and legacy debt

The [English template](../docs/en/contribute/project-template.md) and [Slovene template](../docs/sl/contribute/project-template.md) define the same 15 required critical sections. New showcase cases must have both actual language pages, matching frontmatter (`case_id`, `title`, `content_standard`, `translation_status`, `audit_record`), every visible H2 section, and at least one chapter and one workflow relationship. Code execution is not mandatory: a bounded lawful interface/data/documentation inspection can support the case. An evidence table must keep project claims, observed interfaces, inspected files, local results and editorial inference separate. Missing/unperformed evidence is recorded explicitly, never fabricated.

`legacy-audited` retains the eleven inherited pages without forcing a disguised content rewrite. Every one has a dated audit anchor, visible catalogue maturity label and documented remediation. A false frontmatter `showcase-v1`/`v1_complete: true` or unsupported metadata promotion fails checks. Adding all headings alone does not constitute scholarly review; editors must assess the actual evidence, claims, rights and classroom task before approving a showcase promotion. The audit's case-specific missing-section lists are the debt register, not a permanent exemption for new showcases.

English fallback requires null `page_sl`, `title_sl` and `short_summary_sl`, plus a visible English-fallback label. A translated card label is never counted as a Slovene case. Future `paired-human-reviewed` cases additionally require named, dated, substantive translation-review metadata using the shared placeholder-rejecting review contract; CI cannot authenticate the person or review. `slovene-only` is reserved for explicit editorial permission, not the default architecture. `not-applicable` translation status is permitted only for a catalogue-only record without either case page, with `content_standard: deferred` and `editorial_disposition: defer`; it does not dictate the external project's lifecycle.

The schema records the eleven original case IDs and their baseline commit in `x-legacy-case-ids` and `x-legacy-baseline`. Every original ID must remain represented, including when archived or deferred. A new ID cannot use `legacy-audited` to avoid the showcase requirements. The checker also binds each `case_id` to its `slug`.

For `showcase-v1`, each required H2 section must contain at least four visible words beyond the heading. The evidence section must include all five evidence types in a four-column table, with no empty cells. Comments and code examples cannot satisfy these content checks. These small structural thresholds catch empty scaffolds; they do not certify scholarly completeness or the truth of any statement.

## Validation and reproducibility

```bash
python scripts/build_case_study_index.py
python scripts/build_case_study_index.py --check
python scripts/check_projects.py
python -m unittest discover -s scripts -p 'test_case_studies.py'
make check
git diff --check
```

`make indexes` also regenerates the case catalogues and translation coverage. The focused checker validates the authored source, committed JSON, real local page inventory, titles/review declarations, audit anchors/dates, canonical connections and exact generated bytes. JSON Schema uses explicit date/URI format checking as well as project-local path checks. External project URLs are never fetched in ordinary CI; repeat observations through a later dated source audit. The implementation uses the [jsonschema validator API](https://python-jsonschema.readthedocs.io/en/stable/validate/) with `Draft202012Validator` and `FormatChecker`.

Any change to a dependency named in `release/review-source.json` follows the source-first/snapshot-second process in [CODEX_WORKFLOW.md](../CODEX_WORKFLOW.md). No snapshot is refreshed solely because a branch or current date changed.
