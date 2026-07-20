---
title: "What is digital humanities?"
description: "A practical definition of digital humanities as critical work with cultural materials, data and computation."
tags: [foundations, methods, interpretation]
status: draft
---

# What is digital humanities?

## Learning outcomes

After this chapter, you should be able to:

- explain digital humanities as a relationship between humanities questions, structured evidence and computation;
- distinguish digitization, digital research and critical interpretation;
- describe the main stages of a digital-humanities project;
- identify where modelling choices and bias enter a workflow;
- explain why computational scale does not remove the need for close reading.

## Before you begin

Think of one humanities object you know well: a novel, newspaper archive, translation corpus, collection of letters, historical map, oral-history interview or museum catalogue. What parts of that object are immediately visible to a reader, and what would have to be represented explicitly before a computer could work with it?

## A field, a method and an argument

Digital humanities is often described through tools: corpora, OCR, GIS, databases, network analysis, topic models or machine learning. That list is useful, but incomplete. A project becomes digital-humanities research when computational work is part of a humanities argument about language, culture, history, literature, memory, space or society.

Three activities are related but not identical:

1. **Digitization** creates digital representations of analogue materials, for example scans and OCR text.
2. **Digital scholarly work** organizes, searches, annotates, links or publishes cultural materials.
3. **Computational analysis** uses formal procedures to identify, compare or model patterns that are difficult to inspect manually.

None of these activities automatically produces interpretation. A frequency table does not explain a historical change; a map does not prove spatial causation; a topic model does not discover the true themes of a corpus. The researcher still has to connect the result to a defensible claim and to the contexts in which the evidence was produced.

## The research cycle

A useful project can be understood as a cycle rather than a straight pipeline:

1. **Question** — formulate a humanities problem that can be investigated with evidence.
2. **Sources** — select and document materials, including exclusions and rights.
3. **Model** — decide what counts as a document, person, place, event, emotion, topic or relation.
4. **Transform** — digitize, clean, normalize, annotate or link the material.
5. **Analyse** — apply a method appropriate to the question and data.
6. **Validate** — inspect errors, compare baselines and test alternative explanations.
7. **Interpret** — return patterns to historical, linguistic, literary or cultural context.
8. **Publish** — make the reasoning, data provenance and limitations inspectable.

The cycle matters because later findings often force earlier decisions to be revised. An OCR error may explain a suspicious keyword. A map may reveal inconsistent place names. Manual checking may show that an emotion lexicon confuses fear with politeness. Iteration is not failure; undocumented iteration is.

## Data are made, not found

Cultural material does not arrive as neutral data. A corpus is produced through selection. A database is produced through categories. An annotation scheme decides which differences matter. Missing values can represent absence, uncertainty, loss, censorship or simply an unrecorded fact.

This does not make digital methods invalid. It makes documentation essential. A strong project records:

- where each source came from;
- how it was transformed;
- which units and categories were defined;
- which material was excluded and why;
- which errors were measured or observed;
- which claims the method can and cannot support.

## Scale and reading

Digital methods can move across thousands of documents, but scale is not a replacement for reading. It changes where reading happens. Researchers read sample texts to design categories, read model errors to understand limitations, read outliers to discover unexpected cases, and read passages in context to test whether aggregate patterns are meaningful.

A productive relationship is therefore not **close reading versus distant reading**, but movement between levels: collection, document, passage, token, entity, place and relation.

## Worked example: changing descriptions of migration

Suppose you ask how Slovenian newspapers framed migration between 1995 and 2025.

A weak design downloads whatever articles are easy to find, counts words and treats the graph as the answer.

A stronger design asks:

- Which newspapers and genres are represented in each period?
- Are article counts comparable across years?
- Which terms are used to retrieve relevant texts, and what do they miss?
- Is the unit of analysis an article, paragraph, sentence or quoted speaker?
- How will frames be operationalized: keywords, collocations, manual labels, embeddings or a combination?
- How will automatic labels be validated?
- Which political and media changes must be considered when interpreting the result?

The computational method is only one component. The argument depends equally on source criticism, corpus design, validation and historical interpretation.

## Practice

Choose one cultural collection and write a one-page project sketch with eight headings: question, sources, model, transformation, analysis, validation, interpretation and publication. Under each heading, state one decision and one risk.

## Reflection

- Which part of your project is most likely to be mistaken for a purely technical task?
- Where could an apparently reasonable category impose a modern or institutional viewpoint on the sources?
- What would you need to read manually before trusting a large-scale result?

## Summary

Digital humanities joins computation to humanities inquiry. Its central object is not the tool but the chain of reasoning from sources to claims. Because cultural data are constructed through selection and modelling, a credible project makes those decisions visible, validates automated results and moves repeatedly between aggregate patterns and contextual reading.

## Further reading

- Burdick, Anne et al. *Digital_Humanities*. MIT Press, 2012.
- Drucker, Johanna. *Graphesis: Visual Forms of Knowledge Production*. Harvard University Press, 2014.
- Gold, Matthew K., and Lauren F. Klein, eds. *Debates in the Digital Humanities*. University of Minnesota Press.
- Ramsay, Stephen. *Reading Machines: Toward an Algorithmic Criticism*. University of Illinois Press, 2011.
