---
title: "Linguistic annotation and CLASSLA"
description: "How automatic linguistic annotation turns text into analysable layers—and why every layer still needs validation."
tags: [annotation, CLASSLA, lemma, POS, NER]
status: draft
---

# Linguistic annotation and CLASSLA

## Learning outcomes

After this chapter, you should be able to:

- distinguish tokenization, lemmatization, part-of-speech tagging, morphology, dependency parsing and named-entity recognition;
- explain why linguistic annotation is a model-based interpretation rather than a neutral fact;
- choose annotation layers that match a humanities research question;
- run and document a basic CLASSLA workflow for Slovene or another supported South Slavic language;
- validate automatic output with a task-specific sample and error analysis.

## Before you begin

Take the sentence *Zala je v Novi Gorici predstavila novo Zalo.* Is *Zala* a person, a product, a place or something else? What evidence would a human use? An annotator has to make related decisions from form, context and patterns learned from data.

## Annotation creates analytical layers

Raw text contains characters and spacing. Most computational methods first create more explicit units:

- **tokens** divide running text into words, punctuation marks or other units;
- **sentences** establish boundaries for local context;
- **lemmas** group inflected forms under a dictionary-like base form;
- **part-of-speech and morphological tags** describe grammatical category and features;
- **dependency relations** represent syntactic links between words;
- **named entities** identify spans such as people, organizations, locations or dates.

These layers enable questions that surface forms alone cannot answer. Lemmas support comparisons across inflection. Morphological tags help examine case, number or tense. Entities can connect texts to databases and maps. Dependency relations can approximate who acts upon whom.

## Every annotation is a claim

Automatic annotation is produced by rules or statistical models trained on previously annotated examples. The output therefore reflects:

- the annotation scheme used in training data;
- the genres, periods and varieties represented there;
- tokenization and normalization decisions;
- model architecture and software version;
- ambiguities that the available context cannot resolve.

A tag is not a discovered property in the same sense as a page number. It is a prediction under a particular representation. This distinction matters most when the research claim depends on a small category, unusual language, historical spelling, dialect, poetry or named entities absent from training data.

## CLASSLA in a South Slavic context

CLASSLA provides linguistic processing pipelines and resources for Slovene and several other South Slavic languages. A typical pipeline can tokenize text, split sentences, assign lemmas and morphosyntactic descriptions, parse dependencies and recognize named entities, depending on language and model availability.

The practical advantage is not merely convenience. Using a documented regional infrastructure makes it easier to cite models, compare languages and understand tag sets. The methodological obligation remains the same: record the language, model or package version, processors used, input preparation and date of processing.

## Choose only the layers you need

More annotation is not automatically better. Each layer introduces computation, storage and possible error.

For a study of lexical change, tokens, lemmas and metadata may be enough. A study of grammatical constructions may need morphology and dependencies. A map of institutions requires named entities plus entity resolution. Running every processor because it is available can make a workflow slower and harder to audit without improving the argument.

Start with the research variable. Ask what observable feature is required, which annotation approximates it, and how errors in that layer would change the result.

## From output to a tidy table

A useful annotation table commonly contains one row per token and fields such as:

| document_id | sentence_id | token_id | form | lemma | upos | feats | head | deprel |
|---|---:|---:|---|---|---|---|---:|---|
| d001 | 1 | 1 | Raziskovalke | raziskovalka | NOUN | Case=Nom\|Gender=Fem\|Number=Plur | 2 | nsubj |

Keep document metadata in a separate table linked by `document_id`. Preserve the original text and, where possible, character offsets that map annotations back to it. Exporting only a flattened spreadsheet can destroy sentence structure, multiword tokens or uncertainty.

## Validation must match the research task

A global accuracy reported by a model author is not a validation of your corpus. Draw a sample from your own material and examine the layer your analysis uses.

A defensible procedure is:

1. stratify the sample by genre, period or other likely source of variation;
2. manually annotate or verify the relevant features;
3. compare automatic and reference labels;
4. report precision, recall or agreement where appropriate;
5. inspect recurring error types, not only one aggregate score;
6. estimate whether errors are random or systematically related to the groups being compared.

If a named-entity recognizer misses historical women more often because names are abbreviated differently, a group comparison can be biased even when overall accuracy looks respectable.

## Entity recognition is not entity resolution

Recognizing the string *Ljubljana* as a location does not identify which database record it refers to. Likewise, *J. Novak*, *Janez Novak* and *Novak* may denote one person or several. **Entity resolution** links mentions to stable identities and records uncertainty.

Use identifiers, aliases, temporal information and provenance. Do not force a link when evidence is insufficient. An unresolved mention is better than a confident but false connection.

## Worked example: verbs of speaking in newspapers

Suppose we want to compare reporting verbs across two newspaper periods.

1. Define and sample comparable newspaper material.
2. Preserve article and date metadata.
3. run tokenization, lemmatization, morphology and dependency parsing;
4. identify candidate speech verbs by lemma and construction;
5. manually check a stratified sample, including headlines and quotations;
6. separate true reporting uses from homonyms and parsing errors;
7. normalize counts by corpus size and article distribution;
8. interpret differences alongside editorial and historical context.

The annotation reduces the search space. It does not replace the interpretive distinction between quotation, reported speech, metaphor and formulaic language.

## Practice

Choose one research question and create an annotation plan. Name the required layers, software and language model, input format, output fields, validation sample, expected errors and the point at which a human decision is required.

## Reflection

- Which categories in your material are poorly represented in standard training data?
- Would an error affect all documents equally, or could it distort a comparison?
- Which annotation layers can be omitted without weakening the argument?

## Summary

Linguistic annotation makes textual patterns computable by adding predicted layers such as lemmas, grammatical tags, syntax and entities. CLASSLA offers a strong infrastructure for Slovene and South Slavic material, but its output remains model-dependent. Use only the layers demanded by the question, preserve links to source text, record versions and validate the exact feature on which the interpretation depends.
