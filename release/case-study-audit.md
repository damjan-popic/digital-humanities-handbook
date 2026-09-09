# Case-study audit — issue #27, phase 1

Audit access date: **2026-09-09**. Baseline handbook: `a728334d2fa2d1f217ffbce20d8a1e5354692806`, including squash-merged PR #35. This machine-assisted editorial/source audit is pending human scholarly and language review; it is not a legal clearance, security certification or a new showcase case.

## Scope and inspection method

All **eleven** existing English case studies are retained. No Slovene case page exists yet; the generated Slovene catalogue visibly labels every English fallback. Localized catalogue labels are not translations of case content. No new showcase was added, and none of these pages is marked v1-complete.

Each repository's public GitHub metadata endpoint was requested **without authentication** and returned HTTP 200 / public visibility on the audit date. Repository trees, commit metadata, README/licence declarations and the named commit-pinned source/documentation files below were inspected. GitHub metadata and a file response establish access to those objects, not successful application behaviour. Some authenticated API requests were used to inspect public tree/version metadata after unauthenticated access was established; private-account access is not the basis of the public-availability claims.

No project code, tests, notebook, add-in, server, model download or crawler was executed. No application interface was exercised beyond repository/documentation access. Potentially sensitive corpus bodies, transcripts, learner metadata, source workbooks, extracted reference-text pages, cached databases and generated record payloads were deliberately not fetched. Tree listings establish presence, not data contents, rights, consent or coverage. No claim of a successful local project result is made.

All repositories are in the editor's GitHub account; ten are classified `editor-owned`, while the Vejice fork is `collaborative` to disclose its upstream inheritance. “Independently inspected” means checking named evidence beyond repeating project self-description, **not independent peer review or freedom from an editorial relationship**. Institutional participation, participant permissions and sustained maintenance commitments were not inferred from account names.

No repository-level licence with verified applicable scope was established for any case. Pracomul's README and Vejice's package manifests declare MIT; those declarations and their limitations are recorded, not erased. The metadata therefore uses `rights_status: unknown` and `licence: null` throughout. This is a bounded verification outcome, not a finding that the projects lack permission or are unlawful. Publicly inspectable code (`open` in the code facet) is deliberately not labelled “open source”; the handbook's own CC BY/MIT licences do not license these linked materials.

## Complete audit summary

All rows were publicly reachable on 2026-09-09, were repository-inspected rather than locally run, and retain `content_standard: legacy-audited`. “Upgrade” below is a later case-content recommendation, not a promotion in this PR.

| Case / current page | Project and repository | Rights / reusable data | Lifecycle | Recommended disposition |
| --- | --- | --- | --- | --- |
| [CASE-corpus-augmenter](#case-corpus-augmenter) · [page](../docs/en/case-studies/corpus-augmenter.md) | [corpus_augmenter](https://github.com/damjan-popic/corpus_augmenter) | Unknown licence; `unavailable` | `maintenance-unclear` | retain and upgrade |
| [CASE-createai](#case-createai) · [page](../docs/en/case-studies/createai.md) | [createai](https://github.com/damjan-popic/createAI) | Unknown licence; `unknown` | `maintenance-unclear` | retain as legacy |
| [CASE-fifi](#case-fifi) · [page](../docs/en/case-studies/fifi.md) | [fifi](https://github.com/damjan-popic/fifi) | Unknown licence; `unavailable` | `maintenance-unclear` | retain as legacy |
| [CASE-jezikovni-svetovalec](#case-jezikovni-svetovalec) · [page](../docs/en/case-studies/jezikovni-svetovalec.md) | [jezikovni-svetovalec](https://github.com/damjan-popic/jezikovni-svetovalec) | Unknown licence; `unknown` | `deferred` | defer |
| [CASE-korpus-solar-analysis](#case-korpus-solar-analysis) · [page](../docs/en/case-studies/korpus-solar-analysis.md) | [korpus-solar-analysis](https://github.com/damjan-popic/korpus-solar-analysis) | Unknown licence; `unknown` | `maintenance-unclear` | retain and upgrade |
| [CASE-ladakh-relations](#case-ladakh-relations) · [page](../docs/en/case-studies/ladakh-relations.md) | [ladakh-relations](https://github.com/damjan-popic/ladakh-relations) | Unknown licence; `unknown` | `maintenance-unclear` | retain and upgrade |
| [CASE-medieval-ner](#case-medieval-ner) · [page](../docs/en/case-studies/medieval-ner.md) | [medieval-ner](https://github.com/damjan-popic/medieval-ner) | Unknown licence; `unknown` | `maintenance-unclear` | retain as legacy |
| [CASE-pracomul](#case-pracomul) · [page](../docs/en/case-studies/pracomul.md) | [pracomul](https://github.com/damjan-popic/pracomul) | Unknown licence; `unknown` | `maintenance-unclear` | retain as legacy |
| [CASE-text-harvester](#case-text-harvester) · [page](../docs/en/case-studies/text-harvester.md) | [text_harvester](https://github.com/damjan-popic/text_harvester) | Unknown licence; `not-applicable` | `maintenance-unclear` | retain and upgrade |
| [CASE-vejice-add-in](#case-vejice-add-in) · [page](../docs/en/case-studies/vejice-add-in.md) | [vejice-add-in](https://github.com/damjan-popic/Vejice_add_in) | Unknown licence; `not-applicable` | `maintenance-unclear` | retain and upgrade |
| [CASE-wikivir](#case-wikivir) · [page](../docs/en/case-studies/wikivir.md) | [wikivir](https://github.com/damjan-popic/wikivir) | Unknown licence; `unknown` | `maintenance-unclear` | retain as legacy |

## Catalogue balance

Counts are facets of the **11** retained records, not quality scores. Method facets are multi-valued, so their counts need not sum to eleven.

| Facet | Controlled value | Count |
| --- | --- | ---: |
| `editor_relationship` | `collaborative` | 1 |
| `editor_relationship` | `editor-owned` | 10 |
| `method_domains` | `ai-retrieval` | 2 |
| `method_domains` | `corpus-building` | 5 |
| `method_domains` | `data-modelling` | 6 |
| `method_domains` | `gis` | 1 |
| `method_domains` | `linguistic-annotation` | 6 |
| `method_domains` | `networks` | 1 |
| `method_domains` | `text-analysis` | 5 |
| `method_domains` | `writing-support` | 2 |
| `lifecycle_status` | `deferred` | 1 |
| `lifecycle_status` | `maintenance-unclear` | 10 |
| `inspection_depth` | `repository-inspected` | 11 |

- Verified reusable code permission: **0/11 established**; publicly inspectable source: **11/11**. This distinction is intentional.
- Reusable data: **7 unknown**, **2 unavailable** (corpus-augmenter, FiFi), **2 not applicable** (TextHarvester, Vejice). No open-download, mediated-access, sample-only or metadata-only reuse claim was verified.
- Translation: **11 English case pages, 0 Slovene case pages, 11 English fallbacks**. The new paired contribution template is not a case.
- Later retain-and-upgrade candidates: TextHarvester, corpus augmenter, Šolar analysis, Ladakh relations and Vejice (**5**).
- Retain as legacy pending prerequisites: Wikivir, Pracomul, medieval NER, FiFi and createAI (**5**).
- Defer source-dependent reuse: Jezikovni svetovalec (**1**). Its architecture remains inspectable; no repository/content deletion is proposed.
- No case is recommended for immediate archive or replacement on reachability evidence alone.

## Missing v1 sections and debt

The old pages use functional headings, not the new 15-section critical template. **None yet has the complete required section set.** Missing a standard heading does not mean every corresponding idea is absent: existing use-case, code-inspection, practice and caution material often supplies partial coverage. The following debt summary and detailed sections name what must be evidenced before a later promotion. Optional execution is not a deficit by itself: a fully documented non-executing inspection can satisfy the new standard.

| Case | Useful existing material | Main unresolved critical-section work |
| --- | --- | --- |
| TextHarvester | Extraction question, use cases, comparison task | Bounded sources/users/rights; versioned evidence; collisions and language denominator; manual decisions; maintenance/preservation |
| Corpus augmenter | Conversion/annotation outline, field-preservation exercise | Corpus/schema coverage and rights; negative-versus-missing labels; failure/evidence/adjudication; exact reuse scope; custody |
| Wikivir | Metadata-normalization pattern, classroom mapping | Verified dump/coverage and rights; stale paths/inputs; field-loss decisions; supported claims; responsible maintenance/preservation |
| Šolar analysis | ID-survival exercise, metric cautions | Learner-source/consent conditions; verified annotation checks; reference choices; manual joins and classification; licences; custody |
| Pracomul | Data grain and lexical-diversity cautions | Source/community/consent; incomplete licence terms; undefined measures versus zero; aggregation decisions; missing documentation/preservation |
| Medieval NER | Annotation policy and manual-span exercise | Edition/coverage/rights; located code; desired versus implemented scoring; offset decisions; bounded evidence; maintenance |
| Ladakh relations | Schema/map/source-boundary teaching | Community authority and sources; exact reuse conditions; unsafe server boundary; manual entities/coordinates; claims and preservation |
| FiFi | Chunk metadata and source-grounding task | Lawful collection scope; safe fixture; output replacement and robots behaviour; evidence/adjudication; licences and custody |
| Jezikovni svetovalec | Source/wiki architecture and cautions | Public/private contradiction; permissions; citation/adjudication evidence; source-safe inspection boundary; maintenance/preservation |
| Vejice | Service-configuration/privacy task | Upstream/reuse scope; observed integration limits; actual providers versus defaults; correction/manual review evidence; custody |
| createAI | Role sections, synthetic-task idea, qualitative caution | Interview provenance/rights; actual script/model path; role validation and evidence; output sensitivity; supported claims; preservation |

## Ecosystem audit and bounded corrections

`intertextuality.yml` remains the only authored relation map. The JSON catalogue's chapter/workflow arrays are generated from it in map order; the prose below is a dated audit of conceptual fit, not a second maintained relation list.

This PR makes only these direct corrections:

- Add `workflows/ethics/decide-whether-a-digitised-source-should-be-public.md` to Ladakh relations, FiFi, Jezikovni svetovalec and createAI. Their inspected source/publication or transcript boundaries justify the link; the first three already explain it in page prose.
- Replace createAI's emotion-lexicon workflow with `workflows/nlp/annotate-a-corpus-with-udpipe.md`, already linked in its page. This is an explicit annotation-comparison/transfer exercise, **not a claim that the Stanza implementation uses UDPipe**. No emotion analysis was inspected.
- No chapter relationships, chapter order, category inheritance or typed relation semantics change. Broader/analogical relations (SQL, networks, geocoding, style, topic analysis and infrastructure history) remain visible audit debt for a later content/issue #28 pass. Conceptual relevance need not mean identical implementation, but it must be explained.

## Tiny current-page corrections

The full critical case rewrites remain deferred. Only demonstrably stale or unsafe wording is changed in seven inherited pages: Wikivir's existing script locations and unverified reproducibility description; medieval NER's `scripts/` locations and set-of-strings evaluator description; createAI's script location and synthetic/authorized-input qualification; Ladakh's all-interface/root-server warning; FiFi's incomplete/unbounded invocation replaced by inspection-first guidance; Vejice's conditional rather than guaranteed mock start; and Jezikovni svetovalec's public/private and source-dependent-reuse warning. These edits report static inspection, not successful execution. Other overstrong claims and methodological gaps remain explicitly recorded below for later remediation.

## Detailed records

<a id="case-corpus-augmenter"></a>

## CASE-corpus-augmenter

Audit access date: **2026-09-09**.

**Page:** `docs/en/case-studies/corpus-augmenter.md`. **Project/repository:** [corpus_augmenter](https://github.com/damjan-popic/corpus_augmenter). **Pinned revision:** [7a245ed85a8341d1d5b6dfa078aad52321032772](https://github.com/damjan-popic/corpus_augmenter/tree/7a245ed85a8341d1d5b6dfa078aad52321032772), committed 2025-09-17. Public HTTP 200, non-fork; checked 2026-09-09.

**Exact inspection.** Read [README](https://github.com/damjan-popic/corpus_augmenter/blob/7a245ed85a8341d1d5b6dfa078aad52321032772/README.md), [continuation notes](https://github.com/damjan-popic/corpus_augmenter/blob/7a245ed85a8341d1d5b6dfa078aad52321032772/CONTINUATION_NOTES.md), complete [`run_classla.py`](https://github.com/damjan-popic/corpus_augmenter/blob/7a245ed85a8341d1d5b6dfa078aad52321032772/run_classla.py), [`tei2conllu.py`](https://github.com/damjan-popic/corpus_augmenter/blob/7a245ed85a8341d1d5b6dfa078aad52321032772/tei2conllu.py), [`xml2conllu.py`](https://github.com/damjan-popic/corpus_augmenter/blob/7a245ed85a8341d1d5b6dfa078aad52321032772/xml2conllu.py) and [`file_compare.py`](https://github.com/damjan-popic/corpus_augmenter/blob/7a245ed85a8341d1d5b6dfa078aad52321032772/file_compare.py). Inspected `vert2conllu.py` CLI defaults/function inventory, not every branch, and the tree listing of `run_classla_shards.py`, not its implementation. Named core functions include `build_argparser`, `needs_layers_for_sentence`, `overlay_token`, `build_pipeline`, `augment_file`, `flow_combine`, TEI `read_sentence_tokens`/`write_header`/`convert_one`, and XML `iter_tokens_with_space`.

| Evidence type | Dated observation and limit |
| --- | --- |
| Project/institutional claim | README says the augmenter never overwrites existing annotations, supports raw annotation and tolerates schema variation. Continuation notes report an earlier wrong column mapping; this is a project-reported failure, not independently observed output. |
| Observed interface behaviour | Public API/raw documentation and source responded; no annotation service or live CLI was exercised. |
| Inspected file/repository evidence | CLI supports only augment/combine; most overlay fields change only when blank/underscore; NER=O is explicitly treated as missing. TEI conversion expects sentence/token elements; simple XML conversion treats each non-empty line as a sentence. |
| Locally executed result | None. No CLASSLA environment, model or corpus was installed/downloaded; no idempotence or alignment test was run. |
| Editorial inference | The code is useful for investigating which “missing” values are permissible to replace, not a verified guarantee that all manual annotation survives. |

**Rights/source availability.** No applicable licence declaration was identified. No corpus or bounded sample appears in the tree; referenced JANES/GOS data and CLASSLA resources are external, with separate rights not inspected here. Recommend code `open`, reusable data `unavailable` (no authorized data path verified in this repository), rights `unknown`, licence `null`; Slovene is documented, broader language support was not tested.

**Minimal inspection and break points.** Read `needs_layers_for_sentence` and `overlay_token` (174–254) against a paper-only example containing human-assigned `NER=O`. The code treats that negative as replaceable and can append another `NER=` entry to existing MISC text. Thus a blanket never-overwrite/idempotence claim is unsupported; source inspection does not establish actual CLASSLA object behaviour. The CLI choices (79) also contradict README's `annotate` mode, and README's `tei2conllu_reannotate.py` does not exist. The handbook's own `run_classla.py --mode augment` syntax matches the parser, but its input directory is not bundled.

TEI conversion writes a note and no sentence rows when `<s>` is absent (99–101), regenerates sentence IDs from filename plus sequence and does not preserve every TEI metadata/NER feature claimed by the README. `file_compare.py` merely counts tokens/sentences at hard-coded input paths; it is not annotation-identity validation. Human decisions must specify trusted layers, distinguish “negative” from “unannotated,” map actual source columns and compare structure/values before accepting output.

**Existing-page claims / missing showcase material.** “Preserving existing annotations where possible” is appropriately weaker than the README, but the recommended use for preserving manual annotation needs the NER caveat. Existing minimal path, exercise and cautions provide a useful functional outline; they do not establish lawful corpus availability, schema coverage, a successful augmentation, reviewer adjudication, exact licences or maintenance/preservation. A research question and intended scholarly users remain generic.

**Maintenance/disposition.** Last available commit is dated above; no release/test/maintenance agreement was found. **Retain and upgrade** as a critical conversion/annotation case, not as a validated turnkey corpus run.

**Ecosystem audit.** Corpus representation, CLASSLA chapter and install/annotate/export workflows fit. AI-ethics is a conceptual accountability connection, not an implemented provenance system. Do not claim all South-Slavic models were evaluated or add links simply because they use annotation.

<a id="case-createai"></a>

## CASE-createai

Audit access date: **2026-09-09**.

- **Current page:** `docs/en/case-studies/createai.md`; English fallback, no Slovene case page.
- **Project/repository:** [damjan-popic/createAI](https://github.com/damjan-popic/createAI); no separate deployed project interface was verified.
- **Availability/version:** unauthenticated API HTTP 200; public, not archived; [ca5b39f90d5a9f25d86b9fc74e7612f9e452f8af](https://github.com/damjan-popic/createAI/commit/ca5b39f90d5a9f25d86b9fc74e7612f9e452f8af), 2026-03-04T21:20:09Z. Complete tree lists 204 files and no releases. Transcript TSV/CSV and generated analysis paths are visible, but their contents were deliberately not fetched or inspected.
- **Licence/data:** no applicable licence file/statement or participant/source permission record was verified; GitHub licence metadata is null. Public interview and token-output filenames establish presence, not lawful redistribution or anonymization. Data reuse is unknown, not open-download. Use original synthetic text for any future classroom execution.
- **Documentation/files inspected:** [README](https://github.com/damjan-popic/createAI/blob/ca5b39f90d5a9f25d86b9fc74e7612f9e452f8af/README.md), [.gitignore](https://github.com/damjan-popic/createAI/blob/ca5b39f90d5a9f25d86b9fc74e7612f9e452f8af/.gitignore), complete file-tree metadata and the full [scripts/stanza_tag_sections.py](https://github.com/damjan-popic/createAI/blob/ca5b39f90d5a9f25d86b9fc74e7612f9e452f8af/scripts/stanza_tag_sections.py), especially `detect_sections`, `stanza_pipeline`, `iter_sections`, `write_df`, `write_workbook_xlsx`, `conllu_for_doc` and `main`.
- **Supported/overstrong claims:** code defines transcript IDs, `u_`/`a_` section selection, token/lemma/section/transcript summaries and optional CoNLL-U output. Existing outputs were not regenerated or checked. Role-labelled columns do not independently establish who authored the text, the interview methodology or representative human/AI differences. Stanza defaults to English in this script; actual corpus language/region was not independently inspected, so do not infer it from a programming language or README language.
- **Demonstrable correction:** the handbook and project README invoke root-level `stanza_tag_sections.py`, but the pinned tree places it under `scripts/`. Correct the handbook path to `python scripts/stanza_tag_sections.py`; this corrects a file location, not a claim that the whole procedure was tested. The sample input should be explicitly original/synthetic or separately authorized, not an invitation to reuse the public interview files.
- **Failure/manual work:** nonconforming `u_`/`a_` labels may select no sections; missing `transcript_id` explicitly raises an error; normalized section names can merge distinctions; models/dependencies are not pinned by the shown `pip install -U` command. Optional full-text/token/CoNLL-U outputs can reproduce sensitive material. Human source/role validation, annotation evaluation and privacy review are required.
- **Minimal lawful inspection:** read `detect_sections`, `iter_sections`, output columns and aggregation code; design a synthetic two-section TSV on paper. No model download, annotation run, transcript inspection or output recomputation was performed.
- **Missing v1 material:** explicit research question/community and interview provenance; source coverage, consent and reuse terms; checked model/environment; local result and known annotation failure; role-label validation/manual adjudication; scope-limited claims; maintenance/preservation responsibility and evidence table. Existing practice task/qualitative-reading caution is useful but incomplete.
- **Maintenance/disposition:** `maintenance-unclear`, editor-owned. **Retain as legacy**, correcting the path and limiting classroom reuse to synthetic/authorized material; later upgrade needs rights and a bounded recorded validation.
- **Ecosystem:** linguistic annotation and corpus-text interpretation are well supported. The canonical emotion-lexicon workflow is overbroad: no sentiment/emotion method was inspected; remove/replace with a relevant annotation workflow if making one justified change. The source-grounded-AI audit is only an analogy for validating output, not this script's method. A privacy/rights workflow is conspicuously missing from the canonical case links and directly fits the interview-data boundary. The prose's pyannote diarization link is an upstream analogy, not evidence that this repository processes audio.

| Evidence type | Inspected evidence and its limit |
| --- | --- |
| Project/institutional claim | README describes transcript section outputs and optional CoNLL-U; it does not establish consent, language coverage or analytical validity. |
| Observed interface behaviour | Repository/API is publicly readable; no application interface or transcript reader was operated. |
| Inspected repository/file evidence | Full annotation script and tree metadata confirm the actual script path, expected fields, English model default and aggregation/output code. |
| Locally executed result | None; no project/model code or corpus was executed, and generated outputs were not examined. |
| Editorial inference | Suitable for a synthetic role/annotation exercise; public transcript paths do not establish reuse rights or valid human/AI comparisons. |

<a id="case-fifi"></a>

## CASE-fifi

Audit access date: **2026-09-09**.

- **Current page:** `docs/en/case-studies/fifi.md`; English fallback, no Slovene case page.
- **Project/repository:** [damjan-popic/fifi](https://github.com/damjan-popic/fifi). The README names the Faculty of Arts website as a crawl target, not a deployment operated or crawled by this audit.
- **Availability/version:** unauthenticated API HTTP 200; public, not archived; [477cfd0b71097676a322006a51c20c10fab21301](https://github.com/damjan-popic/fifi/commit/477cfd0b71097676a322006a51c20c10fab21301), 2026-04-15T11:57:38Z. Nine tracked files; no published releases.
- **Licence/data:** no applicable licence file or statement was verified; GitHub licence null. `.gitignore` excludes crawl data and only `data/.gitkeep` is tracked. There is no supplied reusable crawl dataset or synthetic sample. Website copyright, personal data and server permission require a separate decision; the crawler's existence supplies none.
- **Documentation/files inspected:** [README](https://github.com/damjan-popic/fifi/blob/477cfd0b71097676a322006a51c20c10fab21301/README.md), [requirements](https://github.com/damjan-popic/fifi/blob/477cfd0b71097676a322006a51c20c10fab21301/requirements.txt), [.gitignore](https://github.com/damjan-popic/fifi/blob/477cfd0b71097676a322006a51c20c10fab21301/.gitignore), [CLI wrapper](https://github.com/damjan-popic/fifi/blob/477cfd0b71097676a322006a51c20c10fab21301/scripts/crawl_ff.py), and [crawler.py](https://github.com/damjan-popic/fifi/blob/477cfd0b71097676a322006a51c20c10fab21301/fifi/crawler.py): imports/constants, `is_allowed_by_robots()`, `within_allowed_hosts()`, selected `crawl()` setup/queue branches, output paths and `parse_args()`. The tree's `tests/.gitkeep` is not an implemented test suite.
- **Unsupported/overstrong current claims:** advertised document/chunk/manifest output is supported by writing code, not an observed successful crawl. The handbook's command lacks required `--output-dir`; README also requires a separately installed Playwright Chromium browser. A small allowlisted exercise is not supplied by merely passing `--seed-url`: code adds that URL to the default institutional seeds rather than replacing them.
- **Failure/manual work:** robots handling returns allowed when a parser is missing or raises an exception; this must not be represented as permission-safe enforcement. `crawl()` deletes prior document/chunk JSONL files in its output directory. Default limits allow thousands of items, so the unbounded example is inappropriate as a first classroom action. The wrapper imports `fifi.crawler` without installing the package or adjusting its import path; a fresh-environment launch needs separate verification. These are static observations/inferences, not reported executions.
- **Minimal lawful inspection:** read the seed list, host exclusions, robots branch, chunk construction and schema-like record writers; sketch a synthetic two-page dataset offline. Do not invoke the supplied crawl against the university site in this phase. An executable classroom case needs an explicit isolated target fixture, overwrite protection and tested installation/import/browser setup.
- **Missing v1 material:** bounded research/source coverage; source rights evidence; exact licence; implemented validation/tests; lawful inspected run; demonstrated extraction error and manual adjudication; maintenance/preservation responsibility; evidence/claims table. The existing chunk-metadata classroom prompt is useful but does not establish these.
- **Maintenance/disposition:** `maintenance-unclear`, editor-owned. **Retain as legacy**, with inspection-first qualification; upgrade only after the lawful fixture and execution audit exist.
- **Ecosystem:** corpus-building and source-grounded-AI chapters/workflows are appropriate preparation links, not proof of a working chatbot. Add the digitised-source privacy/rights workflow already present in the prose; the current canonical map omits it. The existing README workflow is suitable. Actual retrieval evaluation should remain a later extension because this code prepares chunks rather than implementing a tested chatbot.

| Evidence type | Inspected evidence and its limit |
| --- | --- |
| Project/institutional claim | README describes a Faculty of Arts chatbot corpus builder and possible later embeddings. No institutional approval or deployed chatbot was verified. |
| Observed interface behaviour | GitHub repository/API is public and reachable; neither the crawl target nor an application was operated. |
| Inspected repository/file evidence | Required CLI output argument, additive seeds, fail-open robots branch, destructive output replacement and placeholder-only tests are visible in code/tree. |
| Locally executed result | None; no crawler, dependency installation or browser download was run. |
| Editorial inference | The code is suitable for critical inspection of collection scope, but not yet a verified bounded classroom crawl. |

<a id="case-jezikovni-svetovalec"></a>

## CASE-jezikovni-svetovalec

Audit access date: **2026-09-09**.

- **Current page:** `docs/en/case-studies/jezikovni-svetovalec.md`; English fallback, no Slovene case page.
- **Project/repository:** [damjan-popic/jezikovni-svetovalec](https://github.com/damjan-popic/jezikovni-svetovalec). No separate application homepage was verified.
- **Availability/version:** unauthenticated API HTTP 200; public, not archived; [e75acc15c5d0d6041f3751fa81649664900ea998](https://github.com/damjan-popic/jezikovni-svetovalec/commit/e75acc15c5d0d6041f3751fa81649664900ea998), 2026-05-11T12:22:35Z. Complete tree lists 1,257 files, including 1,200 page-file paths and `data/index/search.sqlite`; no raw PDF blobs or releases were found. Counts are tree metadata only: extracted texts, index contents and wiki answers were not fetched.
- **Licence/data:** README calls this a private course repository, names SP 2001 and Toporišič's grammar, and warns to keep the corpus private without redistribution rights. The repository is nevertheless publicly accessible. `.gitignore` excludes raw PDFs, not extracted Markdown or the SQLite index. No applicable source/code licence or permission was verified. Public file listings are not evidence of authorized reusable data; classification remains unknown, not open-download.
- **Documentation/files inspected:** [README](https://github.com/damjan-popic/jezikovni-svetovalec/blob/e75acc15c5d0d6041f3751fa81649664900ea998/README.md), [docs index](https://github.com/damjan-popic/jezikovni-svetovalec/blob/e75acc15c5d0d6041f3751fa81649664900ea998/docs/README.md), [pyproject.toml](https://github.com/damjan-popic/jezikovni-svetovalec/blob/e75acc15c5d0d6041f3751fa81649664900ea998/pyproject.toml), [.gitignore](https://github.com/damjan-popic/jezikovni-svetovalec/blob/e75acc15c5d0d6041f3751fa81649664900ea998/.gitignore), [tools/search.py](https://github.com/damjan-popic/jezikovni-svetovalec/blob/e75acc15c5d0d6041f3751fa81649664900ea998/tools/search.py) (`build_query`, `search`, `main`) and [tools/context.py](https://github.com/damjan-popic/jezikovni-svetovalec/blob/e75acc15c5d0d6041f3751fa81649664900ea998/tools/context.py) (`get_rows`, `excerpt`, `main`). Package metadata declares version 0.2.0; this is not a tested or released version claim.
- **Supported/unsupported claims:** SQLite FTS5 queries, AND-to-OR fallback, source/page locators and context extraction are inspectable code. A persistent verified wiki, append-only history, accurate advice and rights-safe deployment are not established by directory names or agent instructions. The current page's “rights-cautious” framing must not conceal the public/private contradiction, and “copy the architecture” must not imply a licence grant for copying code or content.
- **Failure/manual work:** absent or incompatible FTS5 source tables would break the helpers; no index/schema compatibility was executed. Retrieval fallback changes recall and precision; snippets are not source verification. Editors must resolve source permissions, distinguish normative advice from description, verify every citation and clarify custody before any public reuse. No finding of illegality is asserted: permission evidence was not supplied/verified.
- **Minimal lawful inspection:** inspect only the cited code/metadata and diagram an equivalent system using original, rights-cleared sample text. Do not download the corpus/index or run search/context helpers on its contents while rights remain unresolved.
- **Missing v1 material:** verified source rights and coverage limits, lawful data/inspection boundary, real citation-error example, checked wiki maintenance/adjudication records, exact licence terms, measured evaluation, named maintenance/custody and preservation plans. Existing architecture/cautions are not v1 completeness.
- **Maintenance/disposition:** technically reachable, but **defer** source-dependent classroom reuse pending a rights and public/private-boundary review; recommended catalogue lifecycle `deferred`, content still `legacy-audited`. Editor-owned; no deletion of the case or repository is proposed.
- **Ecosystem:** source-grounded AI and Slovenian infrastructure links are appropriate. Add the explicit privacy/rights workflow already linked in prose. FAIR packaging must be framed as a future remediation exercise, not endorsement of redistributing this corpus. The open-handbook relation is useful for wiki correction/custody questions, not proof of a maintained scholarly edition.

| Evidence type | Inspected evidence and its limit |
| --- | --- |
| Project/institutional claim | README describes private course use, source layers and persistent LLM wiki; this is not a rights grant or verified answering performance. |
| Observed interface behaviour | Repository/API is accessible without authentication, contradicting an assumption that the repository itself is private. No language-advice interface was exercised. |
| Inspected repository/file evidence | Tree metadata exposes extracted-page/index paths; `.gitignore` covers raw PDFs only; source-search and context code was read without retrieving source contents. |
| Locally executed result | None; no index, source text, model or wiki tool was run. |
| Editorial inference | Preserve the architecture case but defer source-dependent reuse until rights/custody are resolved; public visibility alone is not clearance. |

<a id="case-korpus-solar-analysis"></a>

## CASE-korpus-solar-analysis

Audit access date: **2026-09-09**.

**Page:** `docs/en/case-studies/korpus-solar-analysis.md`. **Project/repository:** [korpus-solar-analysis](https://github.com/damjan-popic/korpus-solar-analysis). **Pinned revision:** [9a8f6c68559c153e1257be886e027052dda86ce6](https://github.com/damjan-popic/korpus-solar-analysis/tree/9a8f6c68559c153e1257be886e027052dda86ce6), committed 2026-05-25. Public HTTP 200, non-fork; checked 2026-09-09.

**Exact inspection.** Read [README](https://github.com/damjan-popic/korpus-solar-analysis/blob/9a8f6c68559c153e1257be886e027052dda86ce6/README.md), [data dictionary](https://github.com/damjan-popic/korpus-solar-analysis/blob/9a8f6c68559c153e1257be886e027052dda86ce6/docs/data_dictionary.md), [methodology note](https://github.com/damjan-popic/korpus-solar-analysis/blob/9a8f6c68559c153e1257be886e027052dda86ce6/docs/methodology_from_dispozicija.md), [example config](https://github.com/damjan-popic/korpus-solar-analysis/blob/9a8f6c68559c153e1257be886e027052dda86ce6/configs/solar_pipeline.example.json), raw/annotated directory READMEs and [test source](https://github.com/damjan-popic/korpus-solar-analysis/blob/9a8f6c68559c153e1257be886e027052dda86ce6/tests/test_solar_pipeline_basics.py). In [`scripts/solar_reannotate.py`](https://github.com/damjan-popic/korpus-solar-analysis/blob/9a8f6c68559c153e1257be886e027052dda86ce6/scripts/solar_reannotate.py), inspected ID mapping (132–158), pipeline/merge/copy (299–420), quality checks (469–558), CLI and function inventory. In [`scripts/solar_analysis.py`](https://github.com/damjan-popic/korpus-solar-analysis/blob/9a8f6c68559c153e1257be886e027052dda86ce6/scripts/solar_analysis.py), inspected school/contact mapping (273–308), reference handling/fallback (553–658), beginning of document metrics (648–700), CLI/function inventory. Remaining analysis algorithms, shared helper implementation and report builder were not comprehensively reviewed. Corpus body, `solar-meta.tsv`, DOCX and sample-mini contents were not read.

| Evidence type | Dated observation and limit |
| --- | --- |
| Project/institutional claim | README advertises safe CLASSLA reannotation and a thesis-facing lexical/syntactic analysis; methodology describes region/age comparisons and MWE exploration. No empirical thesis finding was checked. |
| Observed interface behaviour | Public API/raw code/docs responded; no report UI or corpus service was exercised. |
| Inspected file/repository evidence | Original IDs/forms are copied and compared, annotation fields deliberately replaced, and structural/metadata checks can fail. External frequency lists are optional; corpus-internal ranks are the fallback. |
| Locally executed result | None. Test source was read, not run; there is no verified CLASSLA output or replicated statistic in this audit. |
| Editorial inference | Useful for separating preservation of linkage from preservation of linguistic labels, and corpus-internal rarity from independently referenced sophistication. |

**Rights/source availability.** The full `data/raw/solar-orig.conllu` required by the config is absent, explicitly acknowledged by README. A tiny sample and a participant-related metadata table are present in the tree but were not inspected or downloaded. Neither their licence nor the original corpus access/consent conditions were established. Generated `analysis/` and `reports/` contain placeholders, not published analytic results. Recommend code `open`, data `unknown`, rights `unknown`, licence `null`; do not label a named public sample reusable without a rights record.

**Minimal inspection / break / manual intervention.** Trace the example config to the missing original corpus, then inspect `copy_with_overwritten_annotation` and `quality_report` without running them. Preservation concerns structure/identifiers; lemma/POS/features/dependency layers and predicted NER are overwritten intentionally. `FORM` or token-count mismatches raise errors. Missing input stops the full path. If no external reference list is supplied, lexical “sophistication” uses the same corpus's frequency ranks; the methodology calls that a debugging fallback, not the preferred thesis basis. Human review must verify ID normalization against metadata, examine mismatched sentences, select a justified external reference and adjudicate MWE candidates.

`infer_contact_zone` is a coarse hard-coded triage mapping, not dialect geography; despite its docstring, unrecognized non-empty region labels fall through to `notranjost` (308), rather than `neznano`. This is a static edge case to resolve or teach, not evidence that any actual participant was misclassified.

**Page claims / missing v1 records.** “Safe reannotation” is a design and checks, not a demonstrated successful run or annotation accuracy. “Produced reports” would be stronger than tree evidence permits; this page currently describes capabilities. The functional page already provides an ID-survival exercise and thoughtful methodological cautions. It still needs sourced learner-population/coverage and privacy conditions, exact licence, dated inspect/run record, failure/manual-review examples, validated measures, institutional authorship/responsibility and preservation.

**Maintenance/disposition.** Recent source compared with other cases and test files do not establish maintenance commitments; no releases or long-term deposit were found. **Retain and upgrade**, with an authorized synthetic/sample route and explicit executed evidence deferred.

**Ecosystem audit.** Data/metadata, CLASSLA and text analysis are close fits. CQPweb query and function-word style links are possible extensions, not inspected implementation. Current page links to CLASSLA annotation/export correspond more directly than some canonical workflow links. Record mismatch for later curated reconciliation; no CQPweb deployment or style experiment was verified.

<a id="case-ladakh-relations"></a>

## CASE-ladakh-relations

Audit access date: **2026-09-09**.

- **Current page:** `docs/en/case-studies/ladakh-relations.md`; English fallback, no Slovene case page.
- **Project/repository:** [damjan-popic/ladakh-relations](https://github.com/damjan-popic/ladakh-relations). No separate homepage is declared in repository metadata; no deployed application was operated.
- **Availability/version:** unauthenticated API HTTP 200; public, not archived; pinned source [0fd91a522e754f3c704820ebc03e4a4f4a574d58](https://github.com/damjan-popic/ladakh-relations/commit/0fd91a522e754f3c704820ebc03e4a4f4a574d58), committed 2026-04-28T07:57:50Z. Complete tree lists 61 files; no release was published at audit time.
- **Licence and data:** no repository-level licence/COPYING file or applicable grant was found in the complete tree or inspected documentation; GitHub licence metadata is null. The tree lists graph/GeoJSON/CSV/GraphML derivatives and a source workbook, but availability is not a reuse grant. Corpus texts are intentionally excluded by `.gitignore`; no corpus, workbook or record payload was opened. Reusable-data rights remain unknown.
- **Documentation/files inspected:** [README](https://github.com/damjan-popic/ladakh-relations/blob/0fd91a522e754f3c704820ebc03e4a4f4a574d58/README.md), [architecture](https://github.com/damjan-popic/ladakh-relations/blob/0fd91a522e754f3c704820ebc03e4a4f4a574d58/docs/ARCHITECTURE.md), [corpus workflow](https://github.com/damjan-popic/ladakh-relations/blob/0fd91a522e754f3c704820ebc03e4a4f4a574d58/docs/CORPUS_AND_ANNOTATION_WORKFLOW.md), `.gitignore`, `schema/README.md`, [text-document schema](https://github.com/damjan-popic/ladakh-relations/blob/0fd91a522e754f3c704820ebc03e4a4f4a574d58/schema/text_document.schema.json), [candidate-link schema](https://github.com/damjan-popic/ladakh-relations/blob/0fd91a522e754f3c704820ebc03e4a4f4a574d58/schema/candidate_link.schema.json), [server helper](https://github.com/damjan-popic/ladakh-relations/blob/0fd91a522e754f3c704820ebc03e4a4f4a574d58/scripts/serve_local.py), and selected functions/branches of [rebuild_all.py](https://github.com/damjan-popic/ladakh-relations/blob/0fd91a522e754f3c704820ebc03e4a4f4a574d58/scripts/rebuild_all.py): `read_corpus_files()`, `main()`, `--include-context`, and the generated-output writes.
- **Supported distinction:** code reads local cleaned/normalized texts and writes derived candidate-link records. The schema separates source/target, method, score, evidence count and review status. README counts and claims of a stable interactive map are self-description, not an independently counted or tested result.
- **Overstrong/unsafe current claims:** the unqualified minimal command runs a server bound to `0.0.0.0` over the repository root. With a private corpus present, this is not a localhost-only boundary. The statement that the project “supports” every advertised interface is not a tested application claim. Full public/private separation is a documented design, not a rights audit.
- **Failure/manual work:** absent local normalized corpus prevents reconstruction of corpus-derived outputs; `--include-context` deliberately adds snippets and needs separate rights review. Entity aliases, co-occurrence candidates and coordinates require source/community judgement. JSON schema presence does not establish that all historical relations are valid.
- **Minimal lawful inspection:** read the pinned schemas, server helper and output-writing branches without running them or opening sensitive records. A future approved static demonstration should use an isolated public-only directory with `python -m http.server 8000 --bind 127.0.0.1 --directory PUBLIC_ONLY_DIRECTORY`; this is a proposed safer route, not a run performed here. Do not serve a directory containing private research sources.
- **Missing v1 material:** explicit research question/community authority, source coverage and exclusions, exact reuse terms, evidence table, observed failure, adjudication record, supported/unsupported claims, responsible maintainer/preservation plan. Existing use-case, architecture, classroom and caution paragraphs only partially cover these requirements; none makes the legacy page showcase-v1 complete.
- **Maintenance/disposition:** reachable but sustained maintenance and institutional custody are unestablished; `maintenance-unclear`. **Retain and upgrade** as a useful graph/source-boundary case after the server correction and rights/source audit. Editor-owned.
- **Ecosystem:** map/network/critical-infrastructure links are justified. SQL is a conceptual transfer exercise, not evidence the project uses SQLite (it publishes JSON/static files). The current FAIR-packaging link must not imply FAIR certification or licence clearance. Missing explicit canonical link worth adding: `workflows/ethics/decide-whether-a-digitised-source-should-be-public.md`, already in the case's prose and directly supported by the public/private design. Avoid broader relation changes until the content upgrade.

| Evidence type | Inspected evidence and its limit |
| --- | --- |
| Project/institutional claim | README reports graph/corpus counts and static research views; counts and usability were not independently validated. |
| Observed interface behaviour | Public GitHub repository/API was reachable unauthenticated; the research graph/map interface was not operated. |
| Inspected repository/file evidence | Explicit server bind, source-reading/output-writing branches and required schema fields were read at the pinned commit. |
| Locally executed result | None. No server, rebuild, geocoding or model task was run. |
| Editorial inference | An inspection-first case can teach schema uncertainty and publication boundaries; scholarly validity and lawful redistribution remain unresolved. |

<a id="case-medieval-ner"></a>

## CASE-medieval-ner

Audit access date: **2026-09-09**.

**Page:** `docs/en/case-studies/medieval-ner.md`. **Project/repository:** [medieval-ner](https://github.com/damjan-popic/medieval-ner). **Pinned revision:** [a940682ad98fe91a085200be685d5d7d421d984d](https://github.com/damjan-popic/medieval-ner/tree/a940682ad98fe91a085200be685d5d7d421d984d), committed 2026-04-15. Public HTTP 200, non-fork; checked 2026-09-09.

**Exact inspection.** Read [README](https://github.com/damjan-popic/medieval-ner/blob/a940682ad98fe91a085200be685d5d7d421d984d/README.md), [Rules.md](https://github.com/damjan-popic/medieval-ner/blob/a940682ad98fe91a085200be685d5d7d421d984d/Rules.md), [annotation guidelines](https://github.com/damjan-popic/medieval-ner/blob/a940682ad98fe91a085200be685d5d7d421d984d/annotation_guidelines.md) and [schema](https://github.com/damjan-popic/medieval-ner/blob/a940682ad98fe91a085200be685d5d7d421d984d/data/annotation_schema.md), complete [training-data converter](https://github.com/damjan-popic/medieval-ner/blob/a940682ad98fe91a085200be685d5d7d421d984d/scripts/prepare_training_data.py), [training script](https://github.com/damjan-popic/medieval-ner/blob/a940682ad98fe91a085200be685d5d7d421d984d/scripts/train_ner.py) and [evaluation script](https://github.com/damjan-popic/medieval-ner/blob/a940682ad98fe91a085200be685d5d7d421d984d/scripts/evaluate_ner.py). In [`scripts/process_ner.py`](https://github.com/damjan-popic/medieval-ner/blob/a940682ad98fe91a085200be685d5d7d421d984d/scripts/process_ner.py), inspected class/function inventory, model initialization (1–43), candidate trimming/building (269–335), reporting/output/default paths (525–691); not every hybrid rule branch. Tree presence only was checked for IN/OUT, annotation records and splits; no source corpus or generated entity file was fetched. Model-host availability/licensing/weights were not inspected.

| Evidence type | Dated observation and limit |
| --- | --- |
| Project/institutional claim | README proposes TEA explicit-person fine-tuning and describes a historical multilingual model as a reasonable starting point; starter splits are expressly placeholders. Suitability and model loading are unverified project claims. |
| Observed interface behaviour | Public repository/source/docs responded; no inference API, model UI or training interface was operated. |
| Inspected file/repository evidence | PER-only schema and exact-span policy coexist with a whitespace BIO converter and an evaluator using sets of mention strings; default extractor input directory is inconsistent with the tree after script relocation. |
| Locally executed result | None. No model, source passage, training job, annotation split or evaluation was run. |
| Editorial inference | A useful incomplete-system case: scholarly annotation aims and implemented evaluation are not equivalent, and filename relocation can invalidate a minimal run path. |

**Rights/source availability.** No applicable repository/data licence was identified. Source text, annotations and derived entity artefacts appear in the tree but were not read; their provenance and reuse permission remain unverified. Medieval subject matter alone does not establish rights to a modern edition/transcription or model. Recommend code `open`, data `unknown`, rights `unknown`, licence `null`. Latin and the TEA/Aquileian Adriatic context are documented; coverage across medieval notarial traditions is not demonstrated.

**Minimal inspection / demonstrable breaks.** Compare the tree with `process_ner.main` (643–665). The script now lives under `scripts/` but sets `project_root = Path(__file__).parent`, so its default input is `scripts/IN`, while the listed corpus is in root `IN/`. It initializes/downloads the external model before checking that directory. The handbook's top-level filenames should be `scripts/process_ner.py`, `scripts/train_ner.py`, `scripts/evaluate_ner.py` and `scripts/prepare_training_data.py`; README commands and many absolute local links are stale too.

Read `score` (56–68) without running: it compares sets of gold/predicted surface strings per record, discarding occurrence multiplicity and offsets. This does **not** implement the README's exact character-span evaluation or a token-F1 evaluation. `convert_record` labels any whitespace token overlapping a supplied character span and emits no offsets, so boundary detail can be lost. Human reviewers must check character offsets, define mention-versus-identity units, handle repeated names and evaluate against held-out source units. Annotation guidelines themselves need offset validation: for example, Category 3 gives `end: 52` for a displayed phrase shorter than that boundary; this is a documentation example problem, not an observed training-corpus error.

**Claims / v1 gaps.** The handbook appropriately calls fine-tuning planned and prioritizes person spans, but an “evaluation entry point” must not imply the desired metric is implemented. README's model suitability and successful loading remain unsupported by this audit; no model improvement is claimed. Existing rules, negative examples, annotation exercise and caution about a historical index already supply strong manual/interpretive material. Still missing are a checked source edition/coverage/rights record, complete bounded lawful input, successful run and results, reproducible split/model identity, mismatch analysis, responsible maintenance and preservation record.

**Maintenance/disposition.** Recent reorganization introduced observable path drift; no model release, project tag or deposit was listed. **Retain as legacy**, explicitly incomplete, until paths, annotation examples, metric semantics and rights are settled. No need to run the model to establish these bounded documentation/code discrepancies.

**Ecosystem audit.** Historical-text representation and models/evidence/interpretation fit directly. The implemented model stack is Hugging Face transformers; spaCy and CLASSLA workflow links are comparators or transferable validation exercises, not the project's implementation. GIS and map-mentioned-places links describe later entity-grounding work: PER spans containing locatives do not supply coordinates, place identities or a GIS model. A topic/emotion chapter link is similarly broader than inspected functionality. Record for phase-appropriate curation rather than silently implying those stages exist.

<a id="case-pracomul"></a>

## CASE-pracomul

Audit access date: **2026-09-09**.

**Page:** `docs/en/case-studies/pracomul.md`. **Project/repository:** [pracomul](https://github.com/damjan-popic/pracomul). **Pinned revision:** [86c778e490f77400182e0776064c715c2902cad5](https://github.com/damjan-popic/pracomul/tree/86c778e490f77400182e0776064c715c2902cad5), committed 2025-09-21. Public HTTP 200, non-fork; checked 2026-09-09.

**Exact inspection.** Read complete [README](https://github.com/damjan-popic/pracomul/blob/86c778e490f77400182e0776064c715c2902cad5/README.md) and [`analyze_slc.py`](https://github.com/damjan-popic/pracomul/blob/86c778e490f77400182e0776064c715c2902cad5/analyze_slc.py), including `Turn`, `TokenRow`, `clean_text`, `lexical_stats`, `sentence_stats`, `process_turns`, `AGG_FUNCS`, `aggregate_and_save`, `read_corpus` and `main`. Inspected tree presence, not contents, of dialogue files, XLSX dictionary, notebooks and `results/` outputs. No transcript, speaker metadata, notebook output or derived row was fetched.

| Evidence type | Dated observation and limit |
| --- | --- |
| Project/institutional claim | README describes an approximately 108,000-token dialogue corpus, byte-identical reruns, MIT code and non-commercial transcript use. Sizes, timings, repeatability and transcript permissions were not independently established. |
| Observed interface behaviour | Public repo/documentation/source access succeeded; no notebook, spreadsheet or dialogue interface was operated. |
| Inspected file/repository evidence | A/B markup and speaker metadata drive tables; spaCy Spanish model is loaded; successive same-speaker blocks merge into turns; most diversity indices are averaged across turns. |
| Locally executed result | None. No dependencies/model/corpus were loaded and no table was regenerated. |
| Editorial inference | Appropriate for examining grain, missingness and aggregation, provided students do not interpret means as pooled diversity or public transcripts as cleared teaching data. |

**Rights/source availability.** README §11 declares MIT for code, but no licence text/copyright notice is bundled in the tree. It describes transcripts only as under their existing non-commercial research licence, without a named licence, rights-holder permission or consent record. This is a project declaration, not verified legal clearance. Recommend rights `unknown`, licence `null`, data reuse `unknown`, code `open`; preserve the README declaration here without implying verified licence scope. Corpus/derived files are publicly listed, but token/turn outputs retain text and demographic fields; the audit deliberately does not inspect their contents. Spanish is documented by model and examples; Slovenian participation/context appears in README. Do not infer Spanish geographic coverage from use of Spanish.

**Minimal inspection / break / intervention.** A lawful inspection can stop at the pinned schema/code. Read `lexical_stats` (141–172): empty/zero-word turns yield 0.0; its `safe` wrapper converts exceptions to 0.0, conflating undefined/error results with numeric values. `AGG_FUNCS` then averages these measures (315–335); a group mean is not a pooled-corpus index. These are static findings, not observed errors in participant data. `process_turns` merges consecutive A/B blocks of one speaker, making “turn” an analytical choice. Human review must decide what constitutes a turn, separate invalid/undefined measures, verify speaker joins, justify aggregation and obtain source permission.

The README advertises `docs/data_dictionary.md` and `docs/methodology.pdf`, neither present in the pinned tree. The XLSX exists but was not opened. `spacy.load("es_core_news_md")` requires an installed model; code does not implement README's claimed automatic first-run caching/download. The script/path in the handbook exists, but the documented ten-second run and byte identity were not checked. README says output CSVs stay out of Git; the tree visibly includes them.

**Claims and v1 gaps.** Current page correctly frames outputs as aids to analysis and cautions about transcripts; “may have” restricted licensing should be replaced in a later upgrade by the actual README declaration plus unresolved permission. Existing grain exercise is valuable, but it lacks a source-population/consent account, specific scholarly/community question, rights record, inspected results, failure/missingness analysis, manual correction example, exact source citation and maintained/preserved version.

**Maintenance/disposition.** No tagged release or environment lock is present; notebook filenames/checkpoints are not evidence of a reviewed reproducible experiment. README citation example contains a placeholder repository and unverified authorship/version details; do not copy it as a verified citation. **Retain as legacy** until rights and missing documentation are resolved; no recommendation to download/run the bundled transcripts.

**Ecosystem audit.** Text analysis and data modelling directly fit. SQL, network/co-occurrence, function-word style and topic/emotion connections are recommendations or analogies, not implemented stages evidenced by the inspected script. A/B metadata does not itself establish an edge model or projection. The page's dataset README and cleaning links are stronger candidates for later curation; avoid adding every plausible table-analysis method.

<a id="case-text-harvester"></a>

## CASE-text-harvester

Audit access date: **2026-09-09**.

**Page:** `docs/en/case-studies/text-harvester.md`. **Project/repository:** [TextHarvester](https://github.com/damjan-popic/text_harvester). **Pinned revision:** [517829419f11c0c6d8bef2595b9909ed8eb74194](https://github.com/damjan-popic/text_harvester/tree/517829419f11c0c6d8bef2595b9909ed8eb74194), committed 2025-11-26. Public HTTP 200, non-fork; checked 2026-09-09.

**Scholarly object and available evidence.** This is a generic collector, not an identified representative corpus or institutional collection. The page's question—what extraction keeps or discards—fits the implementation. The [README](https://github.com/damjan-popic/text_harvester/blob/517829419f11c0c6d8bef2595b9909ed8eb74194/README.md) describes downloading HTML, selecting main text, guessing language, and wrapping each result. The complete [`textharvester.py`](https://github.com/damjan-popic/text_harvester/blob/517829419f11c0c6d8bef2595b9909ed8eb74194/textharvester.py) was inspected: `fetch_html`, `remove_unwanted_tags`, `find_main_content_node`, `extract_clean_text`, `classify_languages_paragraphs`, `harvest`, `url_to_safe_filename`, `to_sketchengine_xml_like`, `save_result_as_txt` and CLI. The tree contains only these two files.

| Evidence type | Dated observation and limit |
| --- | --- |
| Project/institutional claim | README advertises readable extraction and approximate language distributions; its usefulness and language coverage were not benchmarked. |
| Observed interface behaviour | Public API and pinned raw files responded; no target website or harvesting UI was inspected. |
| Inspected file/repository evidence | `requests.get` fetches HTML; tag removal and longest article/main/div fallbacks are explicit; accepted paragraph character counts determine shares; XML-like export is escaped. |
| Locally executed result | None. No URL was harvested and the documented package installation/run was not attempted. |
| Editorial inference | A useful bounded exercise in selection bias, with collision and language-denominator examples; not proof of corpus completeness or a preservation service. |

**Rights/source availability.** No licence or source-data permission was identified in the README, full source file or tree. No dataset is distributed; students must select their own lawfully inspectable source. Recommend code `open` only in the schema's public-source sense, reusable data `not-applicable`, rights `unknown`, licence `null`. Language scope is `multilingual` as a documented intention/examples, not demonstrated universal support.

**Minimal lawful inspection and break point.** Read the pinned README and compare `url_to_safe_filename` (lines 252–265) with `save_result_as_txt` (316–330). The filename uses host plus path, omitting query parameters; write mode is `w`. Two illustrative URLs sharing a path but differing in query therefore map to one output filename. This is a **static derivation**, not a locally reproduced overwrite. Also, paragraphs under 30 characters and guesses below 0.80 are excluded from the language denominator (153–197); `langs` is not a distribution over all source text. Extraction uses server-returned HTML, without JavaScript rendering or implemented robots/rate-delay logic. Human source comparison, rights checks and collision prevention are prerequisites for any later run.

**Claims to qualify / missing showcase sections.** “One file per URL” needs the collision caveat. The field named `downloaded` is created during export, not stored at fetch time (282), so it is not a precise retrieval event record. The page's placeholder `https://example.org/article` is an illustration, not an inspected working article. Existing use cases, exercise and caution paragraphs partially supply purpose, inputs and limits. Missing substantive records are a bounded source/coverage decision, intended community, exact rights, dated evidence separation, demonstrated failure, manual adjudication record, version/support/preservation responsibility, and completed inspection outcome.

**Maintenance/disposition.** No supported environment lock, tests, release or succession record was found in the two-file tree. **Retain and upgrade**, with an inspection-only path until rights and a safe local fixture are settled. Do not imply currently maintained infrastructure.

**Ecosystem audit.** Research-design and texts/corpora links are direct conceptual fits; scraping is a direct workflow fit. Canonical MinHash and fastText links are possible downstream extensions, not implementations in this script (`langdetect`, not fastText, is imported). The page additionally lists FAIR packaging and dataset README; reconcile curated relations later rather than equating all useful follow-ons with performed stages.

<a id="case-vejice-add-in"></a>

## CASE-vejice-add-in

Audit access date: **2026-09-09**.

- **Current page:** `docs/en/case-studies/vejice-add-in.md`; English fallback, no Slovene case page.
- **Project/repository and relationship:** [damjan-popic/Vejice_add_in](https://github.com/damjan-popic/Vejice_add_in) is a GitHub-confirmed fork of [zojad/Vejice_add_in](https://github.com/zojad/Vejice_add_in), not wholly editor-originated work. Use `collaborative` to disclose the inherited/fork relationship, not to claim a reviewed coauthor agreement.
- **Availability/version:** unauthenticated fork API HTTP 200; public, not archived; fork commit [00464c7ecf34bae324c8ab06902dbd41f3ee8bf3](https://github.com/damjan-popic/Vejice_add_in/commit/00464c7ecf34bae324c8ab06902dbd41f3ee8bf3), 2026-05-06T14:47:21Z; 90 files, no releases. Upstream public package was also fetched unauthenticated at [a9bba794ddf81575746a2027e7ad1c2342d56f4a](https://github.com/zojad/Vejice_add_in/commit/a9bba794ddf81575746a2027e7ad1c2342d56f4a), 2026-05-02T13:29:59Z. No Word installation, add-in or remote correction endpoint was operated.
- **Licence/data:** both [fork package.json](https://github.com/damjan-popic/Vejice_add_in/blob/00464c7ecf34bae324c8ab06902dbd41f3ee8bf3/package.json) and [upstream package.json](https://github.com/zojad/Vejice_add_in/blob/a9bba794ddf81575746a2027e7ad1c2342d56f4a/package.json) declare MIT. Neither inspected tree has a repository-level licence grant. The fork's `dist/commands.js.LICENSE.txt` is a regenerator-runtime dependency notice, not a grant covering the fork; upstream also has bundled notices. Record MIT as a declaration with unverified scope, not a fully verified open-code permission. Document inputs are supplied by users; no reusable research dataset is necessary for the code-inspection task.
- **Documentation/files inspected:** [README](https://github.com/damjan-popic/Vejice_add_in/blob/00464c7ecf34bae324c8ab06902dbd41f3ee8bf3/README.md), package files above, [.env.example](https://github.com/damjan-popic/Vejice_add_in/blob/00464c7ecf34bae324c8ab06902dbd41f3ee8bf3/.env.example), [serviceConfig.js](https://github.com/damjan-popic/Vejice_add_in/blob/00464c7ecf34bae324c8ab06902dbd41f3ee8bf3/src/config/serviceConfig.js) (`resolveCorrectionServiceDecision`, `resolveLemmatizerServiceDecision`), [apiVejice.js](https://github.com/damjan-popic/Vejice_add_in/blob/00464c7ecf34bae324c8ab06902dbd41f3ee8bf3/src/api/apiVejice.js) (`requestPopravek` guard and mock early return), [service configuration tests](https://github.com/damjan-popic/Vejice_add_in/blob/00464c7ecf34bae324c8ab06902dbd41f3ee8bf3/tests/serviceConfig.test.mjs), [start-dev-server.js](https://github.com/damjan-popic/Vejice_add_in/blob/00464c7ecf34bae324c8ab06902dbd41f3ee8bf3/scripts/start-dev-server.js), and environment-loading/definition branches in [webpack.config.js](https://github.com/damjan-popic/Vejice_add_in/blob/00464c7ecf34bae324c8ab06902dbd41f3ee8bf3/webpack.config.js). Tests were read, not run.
- **Supported/overstrong claims:** empty configuration selects mock correction and synthetic anchoring; remote correction/lemmatization requires explicit trust/unsafe flags in the inspected decision functions. This is source evidence, not observed end-to-end non-disclosure or security certification. `start:internal` does not force mock mode: it delegates to the dev server; webpack loads `.env.local` with override, and the launcher may reuse a server retaining previous flags. Qualify the handbook's unconditional “This starts ... safe mock mode.”
- **Failure/manual work:** missing Word/Office HTTPS setup can prevent deployment; blocked/unavailable remote services prevent real correction, while mock output cannot validate comma accuracy. Inspect active environment and runtime flags and use invented non-sensitive text. A self-declared trusted endpoint is not an independently trusted processor. Correction quality, text anchoring, transmitted payloads and informed consent require separate tests/review.
- **Minimal lawful inspection:** compare the two decision functions with their named tests and trace `requestPopravek` until the mock return or guarded remote branch. No `npm install`, Office launch or network service call is necessary. A later permitted runtime exercise must verify active providers, clear stale-server assumptions and record environment/results.
- **Missing v1 material:** source/data coverage and evaluation set; explicit upstream authorship/reuse scope; observed Word behaviour; real anchoring/correction error; manual review and limits; exact legal terms for dependencies/service use; maintenance ownership and preservation. Existing privacy cautions do not demonstrate those outcomes.
- **Maintenance/disposition:** `maintenance-unclear`; **retain and upgrade** as a configuration/fork-accountability case, not a proven language-correction benchmark.
- **Ecosystem:** critical infrastructure and privacy are direct links. The canonical source-auditing-AI workflow is only an analogy: this project concerns punctuation processing, not source-grounded historical answer generation. A future bounded writing-support/correction-evaluation workflow would fit better. Do not add broad topic/emotion links or claim that the fork is a release-maintenance case without evidence.

| Evidence type | Inspected evidence and its limit |
| --- | --- |
| Project/institutional claim | README promises safe defaults and comma support; it supplies no independent security or accuracy evaluation. |
| Observed interface behaviour | Public fork/upstream repository metadata and package file are reachable; Word/add-in behaviour was not tested. |
| Inspected repository/file evidence | GitHub parent relationship, MIT package declarations, provider guards, mock early return, tests and environment/stale-server behaviour were read. |
| Locally executed result | None; no installation, tests, Office integration or remote text processing was run. |
| Editorial inference | The fork is valuable for configuration/privacy analysis, but configuration defaults alone cannot prove end-to-end privacy or linguistic effectiveness. |

<a id="case-wikivir"></a>

## CASE-wikivir

Audit access date: **2026-09-09**.

**Page:** `docs/en/case-studies/wikivir.md`. **Project/repository:** [wikivir](https://github.com/damjan-popic/wikivir). **Pinned revision:** [1a6f763da813abb9be8d276e41962c3aa7612df6](https://github.com/damjan-popic/wikivir/tree/1a6f763da813abb9be8d276e41962c3aa7612df6), committed 2025-07-16. Public HTTP 200, non-fork; checked 2026-09-09.

**Exact inspection.** Read [README](https://github.com/damjan-popic/wikivir/blob/1a6f763da813abb9be8d276e41962c3aa7612df6/README.md), complete root [`apply_header_map.py`](https://github.com/damjan-popic/wikivir/blob/1a6f763da813abb9be8d276e41962c3aa7612df6/apply_header_map.py), [`categorize/validate_header_map.py`](https://github.com/damjan-popic/wikivir/blob/1a6f763da813abb9be8d276e41962c3aa7612df6/categorize/validate_header_map.py) and [`tools/run_classla.py`](https://github.com/damjan-popic/wikivir/blob/1a6f763da813abb9be8d276e41962c3aa7612df6/tools/run_classla.py); inspected `categorize/header_curator.py`'s token extraction, menu, `classify_token` and main loop (104–249), `tools/run_bertopic.py` CLI/embedding/training (53–162), and `tools/run_lda.py` document/ID readers and `train_lda_gensim` (41–81). Tree presence only—not contents—was checked for `header_map.csv`, patch maps, `cache.sqlite` and `stats/`.

| Evidence type | Dated observation and limit |
| --- | --- |
| Project/institutional claim | README calls this a reproducible pipeline for about 50 million words / 23,000 texts and advertises successful zero-unmapped coverage. Neither size nor success was independently verified. |
| Observed interface behaviour | Public repository endpoints responded; no Wikisource UI, crawler, annotation or topic interface was run. |
| Inspected file/repository evidence | Mapping/curation and CLASSLA/BERTopic/LDA code exist, but several documented paths and full corpus inputs do not. Header rewriting only carries selected attributes. |
| Locally executed result | None. No corpus dump/cache was downloaded, crawler invoked, header map applied or model run. |
| Editorial inference | Strong teaching material for the difference between a pipeline description and an inspectable, bounded rerun; current evidence does not justify “reproducible” as an achieved result. |

**Rights/source availability.** No licence grant was identified for repository code, mappings, cache or statistical outputs. The tree exposes metadata-like artefacts, but their contents/rights were not inspected and they are not an evidenced reusable dataset. The full `normalized_corpus.xml`, `docs.txt` and `junk_tokens.txt` advertised by the README are absent. Do not transfer Wikimedia/Wikisource terms to every source text, dump, mapping or cached item without a specific source-rights record. Recommend code `open`, reusable data `unknown`, rights `unknown`, licence `null`.

**Minimal lawful inspection / failure / human intervention.** Compare the pinned tree with the README before executing anything. The handbook lists `tools/header_curator.py` and `tools/validate_header_map.py`; actual files are under `categorize/`. `tools/run_classla_xml.py` and `tools/topic_model.py` are absent; the existing `run_classla.py`, `run_bertopic.py` and `run_lda.py` are not drop-in equivalents to the documented commands. For example, the annotation parser accepts no `--threads`.

A bounded paper inspection of `process_header` (46–92) shows that only title/author/year/century existing attributes are initially carried over; an existing identifier or other attribute can disappear, and repeated mapped fields overwrite prior values. This is static code evidence, not observed corpus damage. Curation's skip action assigns a category (159–160), rather than recording an unresolved missing decision. Students should record field losses, multi-valued categories and unresolved classifications before applying mappings. Also, `run_classla.py` clears elements at every end event (89–102), raising a nested-text-loss risk before `<doc>` extraction; no run was performed to quantify it.

**Unsupported claims / v1 gaps.** The handbook's “reproducible pattern” should be an intended pattern, not a verified property. “Pipeline” does not establish a reproducible path when inputs and commands are missing. Existing prose supplies a useful metadata-normalization question, conceptual path, exercise and caution; it lacks a checked dump identity/coverage record, rights/citation terms, observed output and failure record, adjudication, institution/maintenance responsibility and preservation. Source versions are not identified by a public release.

**Maintenance/disposition.** README/tree drift and missing inputs block an advertised full rerun. **Retain as legacy**, with a recorded upgrade prerequisite of corrected paths, lawful pinned sample and verification. Do not silently archive or remove a reachable resource.

**Ecosystem audit.** Slovene infrastructure, text/corpus and CLASSLA links are supported by the topic and code. An open-living-handbook link is an analogy rather than evidence of a release/preservation system. Data-metadata-models and the topic-modelling chapter are stronger possible future additions, supported by actual mapping and BERTopic/LDA implementation. The page's Makefile-workflow link must not imply that this repository contains a Makefile; none is present. Phase 1 should record these recommendations rather than perform a broad relation rewrite.

## Remaining uncertainty

Source permissions, project stewardship, future availability, complete dependency licences, human scholarly judgement and Slovene terminology still require review. No models or data were run to manufacture reassurance. No tag, numbered release, DOI/ISBN or preservation deposit was created; publisher coordination remains in issue #30. External availability checks are dated audit work, not part of ordinary CI.
