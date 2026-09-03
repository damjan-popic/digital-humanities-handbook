# Issue #25: temporal, spatial and relational modelling review

Governing issue: https://github.com/damjan-popic/digital-humanities-handbook/issues/25

Status: implementation complete; **draft review only**. Methodological and competent
Slovene-language review are mandatory before marking ready.

## Contract recorded before editing

Objective: deepen the three stable analytical chapters without turning them into
software manuals. Preserve titles and paths; provide substantive bilingual parity,
source-supported arguments, clean and difficult examples, explicit modelling loss,
manual checks, sensitivity analyses and executable practice.

Affected files: six chapter pages; ten new workflow pages; the curated entries in
`intertextuality.yml`; generated bilingual catalogues, review manuscripts and
translation coverage; `Makefile`; a bounded companion teaching packet and its
builder/checker; this review record. Existing navigation titles/order are retained.

Exclusions: no theme redesign, no rewrites of other stable chapters, no changes to
the preserved archival-friction source or its declared inventory, no new case-study
catalogue. Issue #27 remains responsible for verified historical-database, GIS and
network showcase cases; existing curated cases remain linked without new claims.

Acceptance: 2,300–3,300 prose words per chapter/language (excluding references,
footnotes and executable blocks); paired required sections/workflows; reproducible
SQL, GIS and graph results; source/rights audit; non-visual tables; strict
`make check` and `git diff --check`; committed clean worktree; draft PR.

## Scenario decision

The original archival packet contains one authentic issue, not a longitudinal
biography. Its four individually labelled people can be joined by issue-level
co-occurrence, but it cannot substantiate invented correspondence. Keep that
source-grounded example and add an explicitly synthetic, source-readable dossier
for controlled temporal and network tests. The dossier is never used to augment
the authentic archival inventory. Use a separately sourced 1910 Ljubljana plan
for real georeferencing, with synthetic boundaries only in the sensitivity exercise.

## Before/after completeness

| Requirement | Before | Implemented draft |
|---|---|---|
| Chapter depth | approximately 900 words per chapter/language; concepts introductory | 2,519–2,655 counted words per page; difficult examples, losses, manual checks, sensitivity and readings |
| Shared evidence | isolated sketches | authentic newspaper observation counterexample plus clearly separated synthetic longitudinal dossier |
| Database | timeless-attribute risks noted briefly | entity/relation/assertion/event distinction; context-qualified names, statuses and languages; valid/record time; intervals, supersession, hierarchy, false merges and export loss |
| GIS | geocoding, CRS and map caution | candidate preservation, dated boundaries, affine georeferencing with independent failure, scale/accuracy, missingness, MAUP, route assumptions, sensitive sites |
| Networks | graph basics | four evidential relation levels; direction, sign, weight, layers, time and bipartite structure; projection inflation, thresholds, centrality conventions, tied communities and missingness |
| Practice | one prompt per chapter | five paired source-linked procedures plus a deterministic ZIP and non-visual output tables |
| Automated assurance | generic paired/build checks | specific SQL negative/temporal tests, independent graph and affine benchmarks, provenance hashes, standalone archive reproduction and paired executable-block/reference checks |

The established chapter titles, paths and both navigation trees are unchanged. The
existing curated cases remain; issue #27 owns the planned balanced case expansion.

## Schema and model representations

```text
entity 1 -- many assertion many -- 1 source
entity 1 -- many assertion.object_id       (entity-valued claims)
assertion 1 -- many assertion.supersedes   (append-only correction)
person many -- participation -- many document
place 1 -- many dated name / membership -- many territory versions
```

| Model | Enables | Documented loss/cost |
|---|---|---|
| Flat person row | sorting and a declared snapshot | collapses sources, contexts, time and relation semantics |
| Normalized entity/relationship model | reusable identity and many-to-many joins | still hides disagreement if relations are unqualified |
| Assertion/event model | historical and editorial snapshots with provenance | more joins; generic types; facsimile layout and tone remain elsewhere |
| GIS view | containment and approximate display | geometry cannot settle place meaning or administrative self-identification |
| Graph view | relational summaries under one rule | document context, multiple roles and unsupported relations disappear |

The SQLite fixture has 13 stored assertions and 12 current assertions. Constraints
reject orphan subjects/sources/objects, invalid value/object combinations, reversed
intervals, invalid self/context supersession, updates and deletion. The Python
importer additionally rejects non-canonical calendar dates and duplicate or orphan
participation. The tests emphasize that these are consistency checks, not truth tests.

## Source and rights audit

The complete audit is in
`teaching-data/contested-models/rights-and-provenance.md` and its Slovene pair.
The authentic map is Koch's *Ljubljana* (1910), from dLib.si; the provider catalogue
links a Public Domain Mark statement. The unchanged 5747 × 7287 JPEG is pinned by
SHA256 `d3c6c0475a6976c69c99065b7b9df1ae57a5fe6416a9acc858ef0cf75aebf21c`.
Current P625 landmark coordinates are cached from six named Wikidata revisions
under CC0. No remote tiles, external photographs or sensitive personal coordinates
were added. Pixel selections are handbook-created, unapproved first-pass candidates.

The original archival-friction observations are copied byte-for-byte into the
download with their existing rights and citation notes. The full newspaper PDF is
not duplicated. All invented records carry `SYN-` identifiers and `synthetic=true`;
they are CC BY 4.0 teaching content, never attributed to the authentic people, map
or institutions. Original scripts remain MIT-licensed.

## GIS and network sensitivity results

| Check | Baseline | Alternative | Result |
|---|---:|---:|---|
| Affine control RMSE | four fitted points: 15.231 m | two withheld points: 220.063 m | approximately 15 m accuracy claim fails |
| Spatial distribution | four controls | withhold western G4: 1,090.241 m | weak extrapolation exposed |
| L1 centre membership | east before 1920 | west from 1920 | change without stipulated movement |
| L1 ±75 m assumption | centre assigns one side | either side in both periods | unique geometry-based membership fails |
| Projection threshold | t1: 15 edges | t2: 7; t3: 2 | ranking/components depend on threshold |
| Projection rule | remove large list: 7 edges | fractional ≥1: 3 | two inflation controls differ |
| Missing selected document | E betweenness 4 at t2 | omit D6: E betweenness 0 | intermediary claim is sensitive |
| Relation semantics | six authentic same-issue pairs | zero evidenced letters | co-occurrence cannot become correspondence |

All map/network findings have CSV tables. Graph weights count supporting documents
but shortest paths use unit lengths. The community comparison exhaustively evaluates
203 partitions for only six persons, retains ties and discards correspondence
direction for communities only. No layout is used as evidence.

## Word counts

The checker counts visible prose and table tokens, excluding YAML metadata,
footnotes, fenced executable blocks and further-reading sections:

| Page | Words |
|---|---:|
| English databases | 2,632 |
| Slovene databases | 2,561 |
| English GIS | 2,603 |
| Slovene GIS | 2,532 |
| English networks | 2,655 |
| Slovene networks | 2,519 |

## Validation and rendered review

Exact captured output is in `release/issue-25-validation.txt`. Commands:

```bash
PATH="$PWD/.venv/bin:$PATH" make check
.venv/bin/python teaching-data/contested-models/prepare_georeferencing.py --check
git diff --check
```

All returned exit 0; `git diff --check` produced no text. The optional projection
check uses the separately installed, packet-pinned pyproj 3.7.2; the main packet
and its tests use only Python's standard library. The deterministic archive has
43 members and matches its committed digest byte-for-byte.

Rendered inspection covered all six chapter pages and all ten workflow pages in
English and Slovene at 360, 768 and 1280 px, default/light and slate/dark schemes:
96 states total, with zero document-level horizontal overflow, broken in-page
anchors, missing paired-language links or content-boundary violations by page
actions. Tables are horizontally contained. Three after screenshots and two
English before screenshots are in `release/issue-25-screenshots/`; no CSS or theme
change was made. The browser check data are preserved as
`release/issue-25-screenshots/browser-checks.json`.

## Remaining review and uncertainty

This PR must remain draft. It requires:

- methodological review of the schema, graph semantics, interval conventions,
  community calculation and interpretations;
- manual QGIS 3.40-or-compatible execution, visual comparison and re-selection of
  controls. The numerical baseline intentionally fails independent checking and
  no approved georeferenced raster is claimed;
- review of whether current Wikidata entity coordinates and historical-map
  features name the same spatial referents;
- idiomatic Slovene language and field-terminology review. Every new Slovene page
  and paired packet document is visibly marked as a machine-assisted draft;
- accessibility review with assistive technology. Automated width, anchor,
  language-link and light/dark checks plus non-visual alternatives have passed,
  but no screen-reader user test is claimed; and
- jurisdiction-specific rights review where reuse exceeds the documented provider
  Public Domain Mark assessment or the inherited newspaper terms.

No named historical person is identified from the synthetic dossier. The boundary,
gazetteer dates and biographies are teaching stipulations, not historical claims.
