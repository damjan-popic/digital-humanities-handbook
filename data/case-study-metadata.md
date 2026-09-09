# Case-study metadata and critical-content contract

This framework implements phase 1 of issue #27, not the eight showcase additions or the final browsing interface. The catalogue currently retains every legacy case. `showcase-v1` is a content standard, not a release name or a claim of human scholarly approval.

## One source for each kind of fact

- Edit descriptive records in `data/case-studies.yml` (`schema_version: 1`, `cases:` list). Do not author either connection field there.
- Edit conceptual chapter/workflow relationships only in `intertextuality.yml`. Its existing untyped model remains authoritative; issue #28 owns typed relation semantics.
- Record dated primary-source observations and remediation in `release/case-study-audit.md`.
- `scripts/build_case_study_index.py` validates the source, then writes `data/case-studies-index.json` and both case-study indexes. Never edit these three outputs manually.
- `data/case-study-schema.json` is the JSON Schema 2020-12 contract. Its enums and `x-labels` contain the canonical codes and English/Slovene catalogue labels; this guide documents their scope.

Ordering is deterministic: records by `case_id`, JSON keys in schema-property order, unordered facet lists lexicographically, and conceptual links in the authoritative map's authored order. Writers emit UTF-8/LF with a final newline; there are no generated current timestamps or network-dependent results.

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
| `inspection_depth` | Highest descriptive inspection mode or mixed; scoped by the dated audit, never inferred from a directory. |
| `languages_regions` | One or more controlled language/context facets; not a claim of representative coverage. |
| `code_availability` | Public inspectability of the implementation, separate from permission to reuse it. |
| `reusable_data_availability` | An evidenced data-access/reuse path; public filenames or repository visibility do not establish permission. |
| `rights_status` | The verified extent of permissions/restrictions for the proposed reuse, not legal advice. |
| `licence` | Exact licence identifier/title plus material scope and conditions; null if and only if rights_status is unknown. Partial claims without verifiable applicable terms belong in the audit, not a guessed licence. |
| `translation_status` | Presence and review state of actual case pages. Eleven existing English-only cases use english-fallback. |
| `lifecycle_status` | Dated observed/deferred maintenance status; a recent commit alone is not a service guarantee. |
| `evidence_status` | Basis of handbook assertions; does not certify correctness or human scholarly approval. |
| `editor_relationship` | Editorial ownership/collaboration/external relationship, with provenance disclosed in the audit. |
| `last_checked` | Quoted ISO calendar date YYYY-MM-DD, valid and not in the future. Manual dated observation, not a CI link ping. |
| `content_standard` | Critical-content maturity. Legacy and deferred pages never become v1-complete just by migrating metadata. |
| `audit_record` | Local release/case-study-audit.md#case-SLUG anchor; section must identify this case and matching check date. |
| `short_summary_en` | Plain-text cautious English catalogue summary; null only when its language page is absent. |
| `short_summary_sl` | Plain-text Slovene summary for an actual paired page; null for English fallback. Localized facet labels do not imply translated case content. |
| `chapter_connections` | GENERATED from intertextuality.yml case_studies entry, preserving map order; no second authored list. |
| `workflow_connections` | GENERATED from the same authoritative entry, preserving map order. |
| `connection_remediation` | Null when both relation lists are populated; otherwise an explicit substantive note also present verbatim in the audit. This exception is unavailable to showcase-v1. |

## Controlled vocabulary

The codes below are machine values and stay identical across editions. Labels are localized, while null stays JSON/YAML null. None of these labels implies legal clearance, formal peer review, an exhaustive source audit or guaranteed future availability.

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

### inspection_depth

| Code | Meaning; what it does not claim |
| --- | --- |
| `interface-inspected` | Specific visible interface elements were inspected, not its hidden implementation. |
| `documentation-inspected` | Documentation was read; its claims are not independently executed results. |
| `repository-inspected` | Named source files were read; their execution or advertised correctness is not established. |
| `data-inspected` | Named data records or exports were inspected, not the whole collection. |
| `locally-run` | A dated bounded path was executed with recorded inputs/environment/results; not full reproducibility. |
| `mixed` | More than one inspection mode; the audit names each, without implying a run. |

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
| `open` | The advertised core source is publicly inspectable. Reuse permission is a separate rights/licence field; this does not promise a working run. |
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
| `verified-open` | Explicit open terms cover the material actually proposed for reuse; not all third-party dependencies. |
| `verified-restricted` | Explicit restrictions/access terms are evidenced; this is not legal clearance. |
| `mixed` | Different code/data components have different or incompletely verified terms, described in licence/audit. |
| `unknown` | No applicable licence/permission was verified; absence of a licence is not permission. |

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
| `deferred` | Editorial use is deferred pending the audited prerequisites; not a deleted case. |

### evidence_status

| Code | Meaning; what it does not claim |
| --- | --- |
| `project-description-only` | Only self-description supports the case; no independent inspection is claimed. |
| `independently-inspected` | Specific files/interface/data were checked beyond repeating the description; not independent peer review or absence of editorial involvement. |
| `locally-tested` | A recorded local result supports bounded claims; not universal functionality. |
| `mixed` | More than one evidence basis is used, explicitly separated in the audit. |

### editor_relationship

| Code | Meaning; what it does not claim |
| --- | --- |
| `editor-owned` | Repository/project is owned by the handbook editor; no independent endorsement is implied. |
| `collaborative` | Documented editor participation/fork contribution without sole original ownership. |
| `external` | No editorial ownership/collaboration was found in the inspected evidence; disclose later discoveries. |

### content_standard

| Code | Meaning; what it does not claim |
| --- | --- |
| `legacy-audited` | Existing page has a dated audit and explicit remediation; it is not a completed showcase. |
| `showcase-v1` | All required critical-case sections and paired page declarations are validated; not a numbered release or human scholarly approval. |
| `deferred` | Content is retained/deferred with an audit record; not a completed showcase. |

## Pages, evidence and legacy debt

The [English template](../docs/en/contribute/project-template.md) and [Slovene template](../docs/sl/contribute/project-template.md) define the same 15 required critical sections. New showcase cases must have both actual language pages, matching frontmatter (`case_id`, `title`, `content_standard`, `translation_status`, `audit_record`), every visible H2 section, and at least one chapter and one workflow relationship. Code execution is not mandatory: a bounded lawful interface/data/documentation inspection can support the case. An evidence table must keep project claims, observed interfaces, inspected files, local results and editorial inference separate. Missing/unperformed evidence is recorded explicitly, never fabricated.

`legacy-audited` retains the eleven inherited pages without forcing a disguised content rewrite. Every one has a dated audit anchor, visible catalogue maturity label and documented remediation. A false frontmatter `showcase-v1`/`v1_complete: true` or unsupported metadata promotion fails checks. Adding all headings alone does not constitute scholarly review; editors must assess the actual evidence, claims, rights and classroom task before approving a showcase promotion. The audit's case-specific missing-section lists are the debt register, not a permanent exemption for new showcases.

English fallback requires null `page_sl`, `title_sl` and `short_summary_sl`, plus a visible English-fallback label. A translated card label is never counted as a Slovene case. Future `paired-human-reviewed` cases additionally require named, dated, substantive translation-review metadata using the shared placeholder-rejecting review contract; CI cannot authenticate the person or review. `slovene-only` is reserved for explicit editorial permission, not the default architecture. `not-applicable` is permitted only for a deferred catalogue-only record without either case page.

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
