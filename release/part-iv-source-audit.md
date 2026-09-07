# Part IV source and service audit — issue #26

Access/check date for every entry below: **2026-09-07**.
Status: **machine-assisted source and bibliographic check; scholarly and
competent human Slovene-language review remain pending**. An access date is
not a review-completion date.

This audit supports the paired `ai-ethics-reproducibility.md` and
`open-living-handbook.md` chapters and the two AI and three publishing workflows
specified in [issue #26](https://github.com/damjan-popic/digital-humanities-handbook/issues/26).
It records the sources used for the argument and versioned manuscript links,
not every work cited by those sources. The teaching records and correction
scenarios are authored simulations, not reported AI inference or completed
human validation.

## Sources, supported uses and limits

| ID | Source and identified edition/version | Supported use in Part IV | Limit or access qualification |
| --- | --- | --- | --- |
| S01 | National Academies of Sciences, Engineering, and Medicine, [*Reproducibility and Replicability in Science*](https://doi.org/10.17226/25303), 2019; [official report summary](https://www.nationalacademies.org/news/new-report-examines-reproducibility-and-replicability-in-science-recommends-ways-to-improve-transparency-and-rigor-in-research) | Distinguish reconstruction with the same computational inputs from replication with new data. | The handbook's five-part teaching distinction is its own explicit convention, not a universal terminology attributed to the report. |
| S02 | Autio et al., [*Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*](https://doi.org/10.6028/NIST.AI.600-1), NIST AI 600-1, 26 July 2024; [NIST publication record](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Confabulation, risk identification, documentation and bounded evaluation of generative systems. | A voluntary cross-sectoral profile; following a checklist does not certify a model or validate a historical claim. |
| S03 | Guo, Pleiss, Sun and Weinberger, [“On Calibration of Modern Neural Networks”](https://proceedings.mlr.press/v70/guo17a.html), PMLR 70, 1321–1330, 2017 | Explain why classification scores require empirical calibration. | Results concern the investigated architectures and datasets, not every classifier or a generator's confident wording. |
| S04 | Liu et al., [“Lost in the Middle: How Language Models Use Long Contexts”](https://aclanthology.org/2024.tacl-1.9/), TACL 12, 157–173, 2024; DOI `10.1162/tacl_a_00638` | Motivate passage-order and context-length sensitivity checks. | The study examines multi-document question answering and key-value retrieval; it is not a universal present-model performance claim. |
| S05 | NUK/dLib, [*Ilustrirani Slovenec*](https://www.dlib.si/details/URN:NBN:SI:doc-YPI8OFSU), 7 February 1925, volume 1, number 7; `URN:NBN:SI:doc-YPI8OFSU` | Verify the historical object's identity and distinguish its publication date from dLib's record publication date. | A catalogue record does not verify a proposed quotation or settle all reuse rights; consult the existing packet's source, rights and transcription records. |
| S06 | European Data Protection Board, [“Data protection basics”](https://www.edpb.europa.eu/sme/learn-the-basics/data-protection-basics_en), live guidance, no numbered edition asserted | Purpose limitation, data minimization, identifiable individuals, sensitive data and organizational accountability. | General guidance, not a project-specific lawful-basis decision, transfer approval or procurement agreement. |
| S07 | Carroll et al., [“The CARE Principles for Indigenous Data Governance”](https://datascience.codata.org/en/articles/dsj-2020-043), *Data Science Journal* 19, article 43, 2020; DOI `10.5334/dsj-2020-043` | Collective benefit, authority to control, responsibility and ethics in Indigenous data governance. | Preserve the Indigenous context; a researcher cannot replace community authority with a generic consent checklist. Direct retrieval failed in the research interface; the journal's indexed primary text and metadata were available. |
| S08 | Global Indigenous Data Alliance, [“The CARE Principles for Indigenous Data Governance”](https://www.gida-global.org/careprinciples), live organizational source | Locate the principles and their institutional/community provenance; the page records the 8 November 2018 Gaborone workshop. | Availability of the principles does not constitute permission from a community or collection steward. |
| S09 | Luccioni, Jernite and Strubell, [“Power Hungry Processing: Watts Driving the Cost of AI Deployment?”](https://doi.org/10.1145/3630106.3658542), FAccT 2024; [author manuscript, arXiv v3](https://arxiv.org/abs/2311.16863v3), 15 October 2024 | Motivate measuring inference costs and comparing task-specific and general-purpose approaches. | The authors' benchmark findings do not supply a current footprint or price for an untested hosted service. ACM direct retrieval was unavailable; the author manuscript verifies content and DOI/venue, while [DBLP's conference record](https://dblp.uni-trier.de/db/conf/fat/facct2024.html) corroborates pages 85–99. |
| S10 | ALLEA, [*The European Code of Conduct for Research Integrity*](https://allea.org/code-of-conduct/), revised edition 2023, originally published 23 June 2023 | Research responsibility, transparent assistance and integrity beyond disclosure alone. | A research-integrity framework does not substitute for source validation, institutional policy or a named human review. |
| S11 | UNESCO, [*Recommendation on Open Educational Resources (OER)*](https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer), adopted 25 November 2019 | Connect open licensing with inclusion, capacity and sustainable provision. | The proposed maintenance budget and student publication arrangements are handbook teaching decisions, not budgets or procedures mandated verbatim by UNESCO. |
| S12 | Chacon and Straub, [*Pro Git*, second edition, “Git Basics—Tagging”](https://git-scm.com/book/en/v2/Git-Basics-Tagging), maintained book chapter | Distinguish tags from commits and explain lightweight/annotated tags and tag deletion. | A tag is not automatically an immutable scholarly edition or a preservation service. |
| S13 | GitHub Docs, [“About releases”](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases), live documentation | Releases are based on tags and associate notes and downloadable material; tag and release dates may differ. | Documentation does not establish that this project has published a release or deposited its outputs. |
| S14 | GitHub Docs, [“Immutable releases”](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases), live documentation | When enabled, associated tags and attached assets are protected; release title and notes remain editable. | The chapter makes no claim that this setting is enabled here. Platform protections do not amount to an institutional preservation commitment. |
| S15 | Zenodo, [“Digital Object Identifier (DOI)”](https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/), live deposit documentation | Distinguish reserving/registering a DOI from using an existing DOI for the same publication object. | No DOI was reserved or registered for this task; publisher and repository responsibilities remain to be agreed. |
| S16 | Preston-Werner, [*Semantic Versioning 2.0.0*](https://semver.org/spec/v2.0.0.html) | Explain the software public-interface basis of major/minor/patch numbering. | Applying this convention to changes in scholarly argument requires an explicit editorial policy and judgement. |
| S17 | NISO, [*CRediT—Contributor Role Taxonomy*](https://credit.niso.org/), 14-role taxonomy, ANSI/NISO standard approved in 2022 | Record multiple kinds of research contribution rather than only prose authorship. | Role labels neither settle authorship disputes nor exhaust editorial and translation labour. |
| S18 | COPE Council, [*Retraction Guidelines*](https://doi.org/10.24318/cope.2019.1.4), version 3; prescribed citation August 2025 | Distinguish retraction, editorial responsibility and visible notices from silent replacement. | Journal guidance must be adapted to the digital object. Official indexed content states last review 29 August 2025 and version-3 publication 4 September 2025; these are distinct dates. Direct DOI/guidance retrieval returned HTTP 403. |
| S19 | Creative Commons, [*Attribution 4.0 International*](https://creativecommons.org/licenses/by/4.0/), CC BY 4.0 | Attribution, indication of changes, continued permissions subject to conditions, and separate privacy/publicity/moral rights. | The deed is a summary, not the legal code; neither it nor this audit clears third-party material or supplies legal approval. |
| S20 | Digital Preservation Coalition, [“Fixity and checksums”](https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums), *Digital Preservation Handbook*, maintained guidance | Compare bytes at transfer, storage and retrieval; create new checksums after deliberate transformation. | Fixity requires a trusted baseline and does not establish interpretive correctness or prove a deposit occurred. |
| S21 | Digital Preservation Coalition, [“File formats and standards”](https://www.dpconline.org/handbook/technical-solutions-and-tools/file-formats-and-standards), *Digital Preservation Handbook*, maintained guidance | Define significant properties and validate migration against intended preservation outcomes. | No format is declared universally safe; examples and tools on a maintained page may age. No institutional format acceptance was tested. |
| S22 | W3C, [*Web Content Accessibility Guidelines (WCAG) 2.2*](https://www.w3.org/TR/WCAG22/), current Recommendation dated 12 December 2024; [dated version](https://www.w3.org/TR/2024/REC-WCAG22-20241212/) | Define testable web-accessibility criteria and specify the scope of an accessibility assessment. | Citing WCAG or passing automated checks does not establish full conformance or accessible PDF reading order. |
| S23 | GitHub Docs, [“Getting permanent links to files”](https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files), live documentation | Use a full source commit ID rather than a branch name in manuscript source links. | A commit URL identifies a revision while the hosting service retains it; it is not a DOI or an independent guarantee of permanent preservation. |

## Service and publication boundaries

No AI provider, model inference endpoint, retention policy, pricing plan or
privacy capability was selected or tested for the teaching simulations in this
change. The workflow fields specify what a researcher must investigate if a
real service is later selected. They do not report a completed model run,
measured energy use, procurement review or legal approval. Existing packet
model outputs retain their separately documented provenance and are not new
generative-AI runs.

The repository's [tagged-release workflow](../.github/workflows/release.yml)
provides evidence of packaging instructions and Actions artefact upload, not
evidence of a completed scholarly deposit or publisher-approved edition. Its
behaviour is distinct from the external GitHub release capabilities documented
in S13–S14. No publisher contract, DOI/ISBN assignment, permanent deposit or
completed institutional accessibility assessment is claimed by issue #26.
Those operational decisions remain in
[publisher-coordinated release issue #30](https://github.com/damjan-popic/digital-humanities-handbook/issues/30).

The source snapshot recorded for review manuscripts is a development record,
not a numbered edition. Its commit is checked when the snapshot is recorded;
preserved file digests support later checking without Git history, including
source archives and squash-merged checkouts. This checks the recorded sources
and targets, not their scholarly validity or future availability on GitHub.
The recorded LF checkout policy prevents platform-dependent newline conversion
of authored text and linked tables. It leaves binary files unchanged and
explicitly preserves the captured provider OCR's Windows-1250/CRLF bytes; this
policy changes no primary source or existing model-data content.

## Remaining review and access limitations

Direct retrieval restrictions for the journal page in S07, ACM in S09 and COPE
in S18 are recorded above. Primary indexed content or the authors' manuscript
supported the stated claims; no less authoritative mirror was silently
substituted for a cited source. Before formal publication, reviewers should
inspect those originals through an available route and recheck mutable service
documentation. This audit does not claim that the complete bibliography has
received human subject review.

The paired chapters, workflows, terminology and proposed interpretation remain
subject to continuous scholarly and competent human Slovene-language review.
Student consent, privacy, contractual rights, publisher metadata, preservation
arrangements and review completion require actual responsible people and
records; successful deterministic checks do not supply them.
