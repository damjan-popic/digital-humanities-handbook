---
title: "From question to method"
description: "How to operationalize a humanities question, choose evidence and design validation before selecting a tool."
tags: [research design, operationalization, validation]
status: draft
---

# From question to method

## Learning outcomes

After this chapter, you should be able to:

- turn a broad humanities interest into an answerable research question;
- define units of analysis, variables, comparisons and baselines;
- match methods to claims rather than to available software;
- design manual validation and error analysis;
- distinguish exploratory findings from confirmatory evidence.

## Before you begin

Write down a question you would ask even if no digital tool existed. Then underline the nouns and verbs. The nouns often point to objects and units; the verbs often reveal the kind of comparison or explanation the project requires.

If the question concerns Slovenian material, use the ecosystem map in [Digital humanities in Slovenia](digital-humanities-in-slovenia.md) to distinguish discovery portals, research-data environments, repositories and language services before selecting a method.

## A question is not yet a method

Questions such as “How is identity represented in literature?” or “What emotions appear in political discourse?” are intellectually meaningful but computationally underspecified. A computer cannot act on *identity*, *representation* or *emotion* until the project decides what observable evidence will stand for those concepts.

**Operationalization** is the process of connecting a concept to observable, recordable and contestable indicators. It should not be hidden as a technical detail. Operationalization is part of the argument.

For example, “visibility of women in a newspaper” might be represented by:

- the proportion of named people recognized as women;
- the number of quotations attributed to women;
- the roles in which women are mentioned;
- article topics where women appear;
- prominence in headlines or opening paragraphs.

Each indicator answers a different question. None is a complete measure of visibility.

## Define the unit of analysis

A project needs a clear unit: document, page, article, paragraph, sentence, token, person, place, event, image or relation. The choice affects both statistics and interpretation.

If sentiment is calculated per sentence, one article may contribute dozens of observations. Treating those sentences as independent can exaggerate certainty. If a place is counted every time it appears, a travel narrative may dominate a corpus. If authors are compared by document, unequal document lengths may distort frequency measures.

Write the unit into the research question whenever possible:

> How does the frequency and context of migration-related terms differ **between editorials** in two newspaper periods?

## Comparisons and baselines

A pattern becomes meaningful through comparison. Ask “compared with what?” before running a method.

Useful baselines include:

- another period, genre, author, institution or region;
- the rest of the corpus;
- a random or majority-class prediction;
- a simple frequency method before a complex model;
- human agreement before machine accuracy;
- shuffled data to test whether structure exceeds chance.

A sophisticated model that barely beats a simple baseline is not a strong result. A simple method that answers the question transparently may be preferable.

## Exploratory and confirmatory work

Exploratory analysis looks for patterns and generates hypotheses. It is appropriate when categories or relationships are not yet known. Confirmatory analysis tests a pre-specified expectation with data and evaluation criteria chosen in advance.

Digital-humanities projects often move between the two. The danger is to explore many possibilities and then present the most attractive pattern as if it had been predicted. Keep an analysis log. Record when a category, threshold, corpus boundary or visualization changed and why.

## Validation is designed, not appended

Validation should be planned before the full analysis. Depending on the method, it can include:

- manually checking a random sample;
- oversampling rare or high-risk cases;
- calculating precision, recall or agreement;
- comparing two annotators and resolving disagreement;
- checking whether results survive alternative preprocessing;
- reading examples from both the centre and the edges of a distribution;
- testing whether a result is driven by one source, period or author.

Accuracy alone is rarely enough. A model with 90% accuracy may fail almost completely on the category that matters most. Error analysis asks which errors occur, for whom, in which genres and with what interpretive consequence.

## Triangulation

A strong project often combines methods that fail differently. Frequencies show scale but not meaning. Concordances restore context but are laborious. A topic model groups co-occurring terms but needs interpretation. Interviews may explain institutional practice but not historical prevalence.

Triangulation does not mean that every method must agree. Disagreement can be analytically valuable when it exposes different levels of the object.

## Worked example: emotion in parliamentary debate

Broad question: *How did emotional language change during a political crisis?*

A research design might specify:

- **sources:** official transcripts from six months before and after a defined event;
- **unit:** each speaker turn, preserving speaker and party metadata;
- **concept:** emotion represented through a manual multi-label scheme plus a lexicon baseline;
- **comparison:** pre-event versus post-event, by party and speaker role;
- **validation:** two annotators on a stratified sample, confusion analysis for automatic labels;
- **interpretation:** close reading of high-change categories and attention to quotation, irony and procedural language;
- **claim limit:** language in the transcript, not the private emotional state of speakers.

The last distinction is crucial. Text analysis can measure textual cues and labels; it does not directly read minds.

## Practice

Take a broad question from your field and complete this design card:

| Element | Decision |
|---|---|
| Research question | |
| Corpus or collection | |
| Unit of analysis | |
| Operational indicator(s) | |
| Comparison/baseline | |
| Validation sample | |
| Main confound | |
| Maximum defensible claim | |

## Reflection

- What does your operationalization make visible, and what does it erase?
- Which simpler baseline should a complex method beat?
- What error would most seriously damage the humanities interpretation?

## Summary

A digital method is appropriate only in relation to a research question, evidence model and claim. Operationalization, units, comparisons and validation are intellectual decisions. Good design defines the strongest claim the evidence can support and plans error analysis before scale makes mistakes expensive.
