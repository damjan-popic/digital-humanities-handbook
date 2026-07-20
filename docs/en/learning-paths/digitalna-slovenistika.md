---
title: "Digital Slovenian Studies"
description: "An advanced course path through Slovene and South Slavic corpora, annotation, text analysis, databases, GIS, networks and reproducible research."
tags: [course, Slovenian-studies, CLASSLA, corpus, reproducibility]
status: draft
---

# Digital Slovenian Studies

## Purpose

This path trains students to design, execute and critically interpret computational research on Slovene language, literature and cultural material. It is technically more demanding than Information Society Literacy: students work with structured data, Python environments, CLASSLA, relational databases and reproducible project repositories.

Technical competence is not the final goal. Every operation must remain connected to a Slovenian-studies question, source criticism and the linguistic, literary or historical consequences of modelling choices.

## Prior knowledge

Students should be comfortable with files, CSV tables, basic corpus concepts, references and critical source evaluation. No advanced programming is assumed, but the course uses Python 3.12, the command line, virtual environments and short scripts. A preparatory clinic should be available for students without this background.

## Learning outcomes

By the end of the path, students should be able to:

- formulate a digital Slovenian-studies question and an auditable research design;
- build and document a small Slovene or South Slavic corpus;
- use CLASSLA and interpret annotation layers and errors;
- calculate and validate corpus, stylistic, thematic and emotion-related features;
- model humanities entities and relationships in SQLite and SQL;
- resolve and map place evidence with uncertainty;
- construct and critique a source-linked network;
- release data, code and interpretation as a citable, reproducible project.

## Suggested 14-module sequence

### 1. Digital Slovenian studies as a field

Read [What is digital humanities?](../chapters/what-is-digital-humanities.md) and [From question to method](../chapters/research-design.md). Reformulate one traditional Slovenian-studies question so that data, unit of analysis, comparison and limits are explicit.

### 2. Reproducible Python workspace

Create a Python 3.12 virtual environment, install packages, run a script and initialize a repository. Complete the relevant [Python and NLP workflows](../workflows/nlp/index.md). Commit a README and environment specification.

### 3. Text formats, encoding and corpus design

Read [Texts, corpora and OCR](../chapters/texts-corpora-ocr.md). Inspect plain text, CSV, JSON and TEI/XML examples. Design a corpus card with sampling rules, document IDs, metadata and rights.

### 4. Collection, OCR, cleaning and deduplication

Acquire or prepare a small authorized corpus. Preserve raw and processed layers, measure an OCR or extraction sample, remove boilerplate and flag exact or near duplicates without losing provenance.

### 5. CLASSLA annotation

Read [Linguistic annotation and CLASSLA](../chapters/linguistic-annotation-classla.md). Install/test CLASSLA, annotate text and export token-level results. Record model and software versions and inspect errors in Slovene names, non-standard forms or historical language.

### 6. Concordance, frequency, keywords and collocation

Read [Text analysis](../chapters/text-analysis.md). Compare two defensible subcorpora, normalize counts, calculate document frequency and inspect concordances. Report at least one effect size and one corpus-composition limitation.

### 7. Style and authorship signals

Create a document-feature matrix from function words, character n-grams or other justified features. Visualize similarity, test sensitivity to text length and genre and distinguish clustering from proof of authorship.

### 8. Topics, sentiment and emotion

Read [Topics, sentiment and emotion](../chapters/topics-emotions-classification.md). Prepare a codebook and human-labelled sample. Compare one simple baseline with one model or topic approach and conduct a qualitative error analysis.

### 9. Entities and relational data

Read [Databases and SQL](../chapters/databases-sql.md). Extract or manually identify people, places, institutions or works, resolve aliases and design a normalized SQLite schema with provenance and uncertainty.

### 10. SQL analysis

Import the data, enforce keys and write saved SQL queries that join entities, aggregate records and reveal missing coverage. Export one query result for further analysis while preserving the query itself.

### 11. GIS and literary/cultural space

Read [GIS and spatial humanities](../chapters/gis-spatial-humanities.md). Resolve place mentions against appropriate gazetteers, preserve alternatives and dates and build a map whose legend shows uncertainty.

### 12. Networks

Read [Networks and visualization](../chapters/networks-visualization.md). Define an edge from source evidence, build an edge list, compare a bipartite and projected view and interpret centrality only in relation to the construction rule.

### 13. AI, ethics and research packaging

Read [AI, ethics and reproducibility](../chapters/ai-ethics-reproducibility.md). Audit licences, privacy and representational bias. Add tests, citation metadata, a data dictionary, limitations and an AI-use statement.

### 14. Release and defence

Read [The living open handbook](../chapters/open-living-handbook.md). Tag a release candidate, exchange projects for reproducibility review, repair blocking issues and present both a substantive finding and the strongest reason for caution.

## Assessment model

A suggested distribution is:

- **technical labs (25%)** — reproducible exercises in Python, CLASSLA, SQL, GIS and networks;
- **method critique (15%)** — close analysis of one published or public digital project;
- **corpus/data design dossier (15%)** — sampling, metadata, rights and validation plan;
- **final reproducible project (35%)** — data, code, results and interpretation;
- **peer review and oral defence (10%)** — rerun another project and defend methodological choices.

Code elegance should not outweigh research validity. Evaluation should distinguish a technically failed but well-diagnosed experiment from an opaque successful run.

## Final project specification

The project release should include:

1. one specific Slovenian-studies research question;
2. source and rights statement;
3. corpus or data model with inclusion rules;
4. raw-data location or reconstruction instructions;
5. documented preprocessing and annotation;
6. one primary method and one validation strategy;
7. source-linked examples supporting the interpretation;
8. at least one table, plot, map or network with complete caption;
9. discussion of error, bias, uncertainty and alternative explanations;
10. README, environment file, licence and `CITATION.cff`;
11. tagged release and changelog;
12. a short contribution back to the handbook when the workflow is reusable.

## Recommended project themes

Suitable themes include lexical or grammatical change, literary style, newspaper discourse, emotion framing, translation history, named entities in historical collections, spatial narrative, correspondence networks, terminology, digitized heritage or evaluation of language technology for Slovene.

The question should remain small enough for manual validation. A modest corpus with inspectable evidence is preferable to an enormous dataset that the student cannot understand.

## Course versioning

Pin one stable handbook release and one tested environment file for the semester. When a tool breaks, document the change in the living edition and issue a course patch rather than altering graded instructions silently. Student repositories should record the exact commit or release from which workflows were followed.
