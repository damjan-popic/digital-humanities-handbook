---
title: "Texts, corpora and OCR"
description: "How to build interpretable text collections from born-digital, scanned and handwritten sources without hiding selection or recognition error."
tags: [text, corpus, OCR, HTR, sampling, transcription]
status: draft
---

# Texts, corpora and OCR

A searchable transcription can make an archive feel complete. It is not the archive. It is one representation produced from selected objects, page images, layout decisions, a recognition system and editorial rules. What can you responsibly infer when every one of those stages can omit or alter evidence?

This chapter treats a corpus as a research instrument rather than a folder of text. It connects [research design](research-design.md), [data, metadata and models](data-metadata-models.md), and [critical infrastructures](critical-infrastructures.md). Its worked example uses the [Archival Friction teaching packet ZIP](../../assets/downloads/archival-friction-v1.zip), while the [packet source tree](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction) remains inspectable, so you can examine the scan, provider text, reference transcription, metadata decisions and validation results together.

## Learning outcomes

After this chapter, you should be able to:

- distinguish OCR from HTR and distinguish page image, layout, transcription, normalized text, annotation and metadata layers;
- write a transcription policy for historical print or handwriting;
- define a target population, sampling frame and defensible corpus sample;
- calculate and interpret character error rate (CER) and word error rate (WER) against a reference transcription;
- test whether recognition errors threaten a particular search, count or interpretation;
- preserve source, rights, processing and correction provenance through a text pipeline; and
- describe duplicate, reprint and version relationships without erasing historically meaningful circulation.

## Before you begin

You need no command line or programming experience. You do need a research question, permission to use the material, a small set of document images, and a spreadsheet or text editor. For evaluation, you also need a carefully checked reference transcription of a sample.

Your outputs are a corpus card, rights record, transcription policy, linked layers, sampling log, quality report, correction log and known-problems note. Another reader must be able to recover a passage's source, transformations and remaining limits.

## Begin with the research claim

Suppose you want to examine how a 1925 illustrated newspaper represented public institutions. “Download all available OCR” does not define a method. Ask instead:

- What is the target population: one title in 1925, illustrated newspapers in the region, or all surviving periodicals accessible through one portal?
- What is the unit of sampling: issue, page, article, caption or advertisement?
- What is the unit of analysis: word, named person, image-caption pair, article or issue?
- Which comparisons matter: months, genres, publishers, languages or page positions?
- What evidence would contradict the interpretation?

These decisions reveal when the available collection cannot answer the question. As Douglas Biber argues, representativeness begins with a defined population and theoretically relevant strata, not a large word count.

## Pass a source-and-rights gate before recognition

Before running OCR or HTR, make one record for each source object. At minimum record:

- repository and collection;
- stable source URL or catalogue identifier;
- title, creator or publisher, date and extent as supplied;
- rights statement or licence and who made that assessment;
- access date and download date;
- file name, format, size and cryptographic checksum;
- whether the file is the repository original, a derivative or your own capture; and
- known missing pages, access restrictions or sensitive content.

Stop if you cannot identify the source, obtain or document permission, or explain whether redistribution is allowed. Revise the plan if research use is permitted but republishing images is not. Proceed only when the intended acquisition, processing and delivery are compatible with the rights record. “Online” does not mean public domain, and a public-domain work may still be delivered through a file with institutional terms or personal data concerns.

The packet models this gate in `rights-and-provenance.md`, `SOURCE_CITATION.md`, `source/dlib-source.json`, `source/commons-source.json` and the checksum manifest. dLib supplies the stable URN and bibliographic record through NUK; its displayed rights field was blank at the audit date. Wikimedia Commons identifies dLib as source and applies a public-domain assessment to the unchanged PDF copy, while also displaying a notice that a United States public-domain tag should be supplied. The packet therefore assigns final cross-jurisdiction clearance to the publisher's v1.0 rights review. This tiny sample tests a method; it cannot represent the newspaper.

## OCR and HTR solve related but different problems

**Optical character recognition (OCR)** usually means automatic recognition of printed or typeset characters in a page image. **Handwritten text recognition (HTR)** predicts sequences from handwriting, often using models trained or adapted on line images and transcriptions. Historical type, mixed print and handwriting, marginal additions and decorative headings blur the boundary; record what model and process you actually used rather than relying on the label.

Multiple hands may require separate models or validation strata. A model confidence score is an output under that model's assumptions, not a measured error rate; calibrate it against checked text before using it as a filter.

Recognition is only one stage. Segmentation identifies regions, columns, reading order and lines; transcription predicts characters or words; correction alters that prediction; export may flatten layout. Plausible plain text can therefore put correct words in the wrong order or omit a caption.

Interfaces, model catalogues and export menus change. Record the service, version or access date, model identifier, settings and export format. Preserve the input and downloaded result; if a hosted service cannot expose a stable version, say so.

## Keep the document layers linked

A text object contains non-interchangeable layers:

1. **source object** — the physical or born-digital item described by the repository;
2. **page image** — a scan or photograph with a stable page identifier;
3. **layout** — regions, columns, lines, reading order and coordinates;
4. **provider transcription** — the text delivered by an archive or recognition service;
5. **reference or corrected transcription** — human-checked text under a declared policy;
6. **normalized text** — standardized spelling, whitespace or characters for a stated purpose;
7. **annotation** — tokens, entities, topics, editorial notes or linguistic labels; and
8. **metadata and provenance** — identity, rights, relations and processing history.

Never overwrite one layer with another. Corrections should point to the previous value, source location, agent, date and rule. TEI `<choice>` can represent original and corrected forms; ALTO XML can preserve strings and layout; IIIF manifests can link page views, rights and annotations. Their separation of object, surface, text and description is a useful design test.

## Write the transcription policy before making ground truth

A **reference transcription**, often called *ground truth*, is human-produced under explicit conventions. Two transcribers can disagree because one records glyphs and line breaks while another records words. Write and pilot the policy before transcribing the evaluation sample.

Specify at least:

- **scope:** body text only, or also mastheads, captions, advertisements, page numbers and marginalia;
- **reading order:** how columns, boxes, footnotes and interrupted articles are sequenced;
- **line breaks and hyphenation:** whether layout line breaks are preserved; whether a word divided at a line end remains divided, is joined, or records both forms;
- **characters and ligatures:** whether visible ligatures and historical glyphs are encoded literally, expanded, or represented by an original/normalized pair;
- **spelling and punctuation:** whether historical spelling, capitalization, abbreviation and punctuation are retained;
- **Unicode:** which composed characters, quotation marks, dashes, spaces and replacement symbols are permitted;
- **illegible or missing text:** the notation for unreadable, damaged and cropped passages;
- **corrections:** how printer's errors, handwritten corrections and editorial interventions are represented; and
- **layout:** whether paragraphs, headings, tables and image captions are represented in plain text, structured markup or a separate layout file.

These choices change CER and WER. If the reference joins a line-end word while the OCR preserves a hyphen and newline, the score measures a policy difference as well as recognition. Normalize only the features declared irrelevant to the test, apply the same normalization to candidate and reference, and publish that rule.

## A corpus is a designed sample

The **target population** is the larger body about which you want to make a claim. The **sampling frame** is what you could actually select. Describe gaps caused by survival, cataloguing, digitization, licensing or access.

Then distinguish three related properties:

- **coverage** asks whether relevant categories and periods are present;
- **balance** describes their proportions in the corpus; and
- **comparability** asks whether groups were produced and processed in sufficiently similar ways for the proposed contrast.

A balanced corpus is not automatically representative: equal numbers by decade may differ from the historical population. Comparability can fail when one decade uses repository OCR and another newly corrected HTR.

Create a sampling table with strata, eligibility, selection, rights, image quality, recognition route and exclusions. Count documents and words. Random sampling within strata can reduce convenience bias; label purposive selection honestly.

## Build an evaluation sample that can reveal failure

Do not evaluate only the cleanest page. Select a sample across the features that may affect the claim: year, title, typeface or hand, scan quality, column count, language, genre, captions, tables, damage and proper names. Keep a random or systematic component so memorable failures do not define the whole estimate. Add an explicitly purposive “challenge” set if needed, but report it separately.

One checked passage can teach the mechanics. For research, record sample size, selection, strata, transcribers, checking, disagreement resolution and policy version. An estimate says nothing about excluded advertisements or handwriting.

## Worked example: archival friction

### Where the first pipeline fails

The packet begins with a two-page illustrated newspaper and provider OCR. Treating the exported text as the article silently accepts unstable column order, missed captions and corrupted names. Treating every caption as an article also confuses document and analytical units. The sample is too small and too selectively illustrated to support a claim about the newspaper as a whole.

### Manual intervention

The reference transcription follows a declared reading order, retains historical spelling and punctuation, and joins layout-only line breaks. The exact dLib TXT export stays unchanged in `source/`; the builder decodes it, selects the declared lines and normalizes their whitespace into a derivative in `raw/`. That source-grounded decision is logged, and the checked passage remains a separate, documented `reference/` object. A human compares image and text, logs error categories, checks disputed names and calculates CER and WER after the declared extraction normalization under one alignment policy.

### What remains uncertain

The printed “Mr. Meker” remains distinct from a rejected Ezra Meeker authority candidate, the riverbed photograph's creation date is unknown rather than inherited from the issue, and untranscribed regions have not been evaluated. The exercise does not estimate variation across issues, layouts or recognition models.

### Effect on the downstream claim

After the declared extraction normalization, the checked passage has CER 0.020305 and WER 0.096774, but a corrupted proper name still changes exact search. You may claim that the provider text needs name-aware checking for this passage. You may not infer a publication-wide error rate or interpret absence from search as historical absence.

## Calculate CER and WER

Align the recognition output with the reference and count the minimum substitutions \(S\), deletions \(D\) and insertions \(I\). For a reference of \(N\) units:

\[
\mathrm{error\ rate}=\frac{S+D+I}{N}
\]

Use characters for **CER** and defined word tokens for **WER**. State whether spaces, punctuation and case count as characters, how Unicode is normalized and how words are tokenized. Because insertions are possible, an error rate can exceed 1. Do not convert the score into “percent accuracy” without defining the relationship; the intuitive complement can be misleading when alignment contains insertions.

After the declared extraction normalization, the packet records 591 reference characters with 7 substitutions, 5 deletions and 0 insertions (12 edits), hence CER \(12/591=0.020305\). Its 93 whitespace-delimited reference words have 7 substitutions, 2 deletions and 0 insertions (9 edits), giving WER \(9/93=0.096774\). Tied minimum alignments prefer match, substitution, deletion and insertion in that order; rates use round-half-even to six decimals. These deterministic values do not measure omitted layout-whitespace behaviour and describe one passage, not an issue, title, platform or model.

## Turn one score into an error profile

CER and WER collapse different failures. Add an error table with source location, reference, candidate, operation, category and likely consequence. Useful categories include:

- character confusion, especially diacritics and historically similar glyphs;
- joined or split words;
- line-end hyphenation;
- omitted line, region, column or caption;
- duplicated text or wrong reading order;
- punctuation or case difference;
- proper name, date or number error; and
- editorial-policy disagreement rather than recognition failure.

Report metrics by relevant stratum when the sample permits. A low aggregate CER can coexist with catastrophic omission of captions or poor recall for names. Conversely, historical spelling is not an OCR error when the image contains it.

## Test the downstream claim, not an abstract threshold

There is no universal “good enough” CER. The acceptable error depends on the task and the distribution of error. Full-text search loses recall when target strings are corrupted. Frequency lists split one lexical item into variants. Named-entity recognition is vulnerable to rare names. Topic or clustering methods can organize repeated recognition noise. Exact quotation, collation and scholarly editing require direct verification against the image.

Evaluate the task itself:

1. Write the intended claim and the text features it depends on.
2. Run a small analysis on provider text and checked text.
3. Compare retrieved items, counts, rankings or classifications.
4. Inspect false negatives and false positives by stratum.
5. Decide whether to correct, change method, narrow the claim or stop.

Research by Traub, van Ossenbruggen and Hardman and by Hill and Hengchen shows that OCR's effect depends on the research task. Quality reporting should combine intrinsic metrics, error categories and a downstream test.

## Preserve duplicates, reprints and versions as relations

The same content may appear as an identical file, second scan, syndicated article, changed reprint, revised edition or OCR export. These are different relations.

Use stable identifiers. Checksums detect byte-identical files, not intellectual identity. Review metadata and text, then record `duplicate_of`, `reprint_of` or `version_of`. Decide whether analysis counts manifestations, articles or works; retain repetition when circulation is the phenomenon.

If one record represents several manifestations, retain a relation table and explicit selection rule, then verify identifiers and counts. Similarity is evidence for review, not historical judgment.

## Design the pipeline as a chain of evidence

Use directories or equivalent storage layers whose roles remain visible:

```text
source/          unchanged object, provider records and byte-preserved export
reference/       handbook observations, reference transcription and policy
teaching/        declared synthetic disturbances
raw/             derived normalized OCR excerpt and awkward working rows
interim/         candidates awaiting source/reference review
cleaned/         audited records, transcription copy and decisions
output/          metrics, error audit and record summaries
validation/      expected values, checksums and test reports
known-problems/  unresolved errors and scope limits
```

Record each transformation with input, output, procedure, version or access date, parameters, agent, date and result. A manifest should connect identifiers, paths, checksums, media types and layer roles. After correction, verify files, unique identifiers, page links, counts, raw checksums, encoding and recomputed metrics.

A script may automate these checks, but automation is an optional extension. A spreadsheet checklist and operating-system checksum tool can implement the same control. Passing this chapter requires the evidence chain, not a particular platform.

## Practice: make one defensible claim

Download the [Archival Friction teaching packet ZIP](../../assets/downloads/archival-friction-v1.zip). Use the [packet source tree](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction) to inspect how it is assembled.

1. Read the rights record and source citation. State which assessment supports reuse of the PDF and what clearance remains for the publisher.
2. Inspect both source pages before reading the transcriptions. Identify two layout features likely to affect reading order.
3. Compare `raw/provider-ocr.txt` with `reference/reference-transcription.txt`. Classify at least five differences.
4. Read `reference/transcription-policy.md`. Decide whether each difference is recognition error, policy difference or unresolved reading.
5. Confirm every character and word S/D/I count, recompute the rates under the declared rounding rule, and compare your classification with `output/ocr-error-audit.csv`.
6. Choose one task—search for a name, count a form or quote a sentence—and test it on both versions.
7. Write a claim limited to this sample, followed by one sentence explaining what you cannot generalize.

The exercise passes if another student can trace every number and quotation to a file and page, reproduce your classification under the stated policy, and see why your conclusion is no broader than the sample. CER and WER begin after the documented excerpt selection and whitespace normalization, so they do not measure omitted layout-whitespace behaviour elsewhere in the provider export.

## Failure modes and repair decisions

Stop when rights are incompatible with the planned output, source identity is unresolved, pages are missing in a way that invalidates the comparison, or reference transcription cannot be checked. Revise when strata are absent, identifiers are unstable, policy changed midstream, layout was flattened incorrectly, or a downstream result changes materially after correction. Proceed with a documented limitation when the error is measured, its likely effect is bounded and the claim remains supported.

Never replace the raw file. Preserve failed output, log corrections and issue a new derivative. Record a rerun after a model or interface change as another version.

## Ethics and licensing limits

Recognition can expose names or sensitive facts that were difficult to search in images. Public-domain status does not remove privacy, community authority or contextual-harm concerns. Follow repository restrictions and relevant law, minimize unnecessary personal data, and document access decisions.

Credit scanning, cataloguing, transcription, correction and community knowledge as labour. Do not call provider OCR your transcription. Specify training, review, attribution and disagreement procedures for student or volunteer work.

## Reflection

- Which texts are absent before recognition even begins?
- Which transcription rule most changes your planned measurement?
- Does your quality sample represent ordinary material, difficult material, or both?
- Would the same error profile support search but invalidate quotation?
- When is a reprint noise, and when is it evidence of circulation?

## Summary

A corpus is an argued relationship between a question, a population, a sampling frame and representations. OCR and HTR produce predictions, not transparent text. Preserve page, layout, provider, corrected, normalized and annotated layers; define transcription policy before evaluation; report CER and WER with their rules and strata; and test the downstream claim. Rights, provenance and failures belong inside the pipeline.

## Further reading and current technical references

- Biber, Douglas. 1993. [“Representativeness in Corpus Design.”](https://doi.org/10.1093/llc/8.4.243) *Literary and Linguistic Computing* 8 (4): 243–257.
- Hill, Mark J., and Simon Hengchen. 2019. [“Quantifying the Impact of Dirty OCR on Historical Text Analysis.”](https://doi.org/10.1093/llc/fqz024) *Digital Scholarship in the Humanities* 34 (4): 825–843.
- Traub, Myriam C., Jacco van Ossenbruggen, and Lynda Hardman. 2015. [“Impact Analysis of OCR Quality on Research Tasks in Digital Archives.”](https://doi.org/10.1007/978-3-319-24592-8_19) In *Research and Advanced Technology for Digital Libraries*, 252–263.
- OCR-D. [Ground Truth Guidelines](https://ocr-d.de/en/gt-guidelines/trans/) and [quality-assurance definition of CER](https://ocr-d.de/en/spec/ocrd_eval.html) (living technical documentation; accessed 2 September 2026).
- Text Encoding Initiative. [TEI P5 Guidelines, `<choice>`](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-choice.html), version 4.11.0 dated 18 February 2026 (accessed 2 September 2026).
- Library of Congress. [ALTO: Technical Metadata for Layout and Text Objects](https://www.loc.gov/standards/alto/) (current official schema listed as 4.4; accessed 2 September 2026).
- IIIF Consortium. [Presentation API 3.0](https://iiif.io/api/presentation/3.0/) (stable version 3.0.0 at access; accessed 2 September 2026). A 4.0 release candidate was also listed, so implementations should record the version they use.

Interfaces change. Record versions and access dates.
