---
title: "Topics, sentiment and emotion"
description: "How to use classification and exploratory models without confusing labels, themes or scores with human meaning."
tags: [classification, topic-modeling, sentiment, emotion, validation]
status: draft
---

# Topics, sentiment and emotion

## Learning outcomes

After this chapter, you should be able to:

- distinguish supervised classification, unsupervised clustering and topic modelling;
- explain the difference between sentiment, stance, affect and emotion;
- design an annotation scheme and evaluate agreement;
- interpret topic-model output as an exploratory representation rather than discovered truth;
- validate model output against source texts, metadata and human judgement.

## Before you begin

The sentence *Brilliant—another glorious delay* contains positive words but probably expresses negative evaluation. A model that scores vocabulary without context may fail. Before selecting a tool, decide what exactly the category means and which textual evidence licenses the label.

## Classification starts with an operational definition

A classifier assigns texts or passages to predefined categories. Examples include genre, period, author, stance, sentiment, emotion or relevance. The central research act is not choosing an algorithm; it is translating a concept into observable annotation rules.

A good codebook specifies:

- the unit to label: sentence, paragraph, document or event;
- category definitions and boundaries;
- inclusion and exclusion examples;
- treatment of uncertainty, mixed cases and absence;
- the intended use of the labels;
- known cultural, historical and genre limitations.

If trained annotators cannot apply a category consistently, a model cannot repair the conceptual ambiguity.

## Sentiment is not emotion

**Sentiment analysis** usually predicts evaluative polarity—positive, negative or neutral—toward a target. **Stance** concerns support, opposition or positioning toward a proposition or actor. **Emotion analysis** attempts categories or dimensions such as joy, fear, anger, sadness, arousal or valence. **Affect** may refer more broadly to expressed or evoked intensity.

These are not interchangeable. A historical letter may describe fear without the author being afraid; a tragedy may evoke sadness while containing little negative evaluation; satire may use praise to criticize. State whether the aim is to classify wording, narrator, character, speaker, target or reader response.

## Three common approaches

### Lexicon-based methods

A lexicon maps words to scores or categories. It is transparent and easy to inspect, but context, negation, intensification, metaphor, domain shift and morphology can undermine it. For Slovene, inflection and lemmatization choices matter, and translated lexicons need cultural validation.

### Supervised models

A supervised model learns from labelled examples. Its ceiling is set by label quality and representativeness. Split data by document, author or source where leakage is possible. A random sentence split can make performance look excellent because nearly identical passages occur in both training and test sets.

### Prompted language models

A language model can classify using instructions and examples, but its behaviour can vary with wording, model version and context length. Treat prompts as part of the method, preserve exact inputs and outputs, test stability and do not substitute fluent explanations for evaluation.

## Evaluation beyond accuracy

For imbalanced categories, accuracy can be misleading. Report a confusion matrix and class-specific precision, recall and F1 where appropriate. Compare against simple baselines: majority class, lexicon rule or metadata-only model.

Also ask:

- Are errors concentrated in one genre, period or social group?
- Does the model learn document source rather than the intended concept?
- Are uncertain human cases counted as model failures without acknowledging ambiguity?
- Would the remaining error change the historical or literary conclusion?

## Topic models are lenses

Topic models and related clustering methods reduce a document-term or embedding space into recurring patterns. In a probabilistic topic model, a “topic” is a distribution over words and documents, not a ready-made subject with a natural name.

Results depend on:

- preprocessing and vocabulary;
- unit of analysis and document length;
- number of topics or clusters;
- random initialization and hyperparameters;
- model family, such as LDA, NMF or embedding-based clustering;
- corpus composition and duplicated text.

Topic labels are supplied by researchers after inspecting words and documents. A label should therefore be accompanied by representative documents, negative cases and uncertainty—not merely a word cloud.

## Stability and interpretability

A coherent-looking topic can be unstable across random seeds or minor corpus changes. Run multiple configurations and compare whether the pattern persists. Statistical coherence scores may help select candidates, but they do not replace domain interpretation.

A defensible topic-analysis report includes:

1. corpus and preprocessing decisions;
2. model and parameter settings;
3. selection process for the reported solution;
4. representative and contradictory documents;
5. topic prevalence by relevant metadata with uncertainty;
6. sensitivity to another seed, model or topic count;
7. an account of what the model excludes or conflates.

## Worked example: emotional framing in parliamentary debate

Suppose we study emotional framing around climate policy.

1. Define the target: emotion words used by speakers, attributed emotion, or emotional framing of policy.
2. Sample debates and preserve speaker, party, date and agenda metadata.
3. Develop a codebook on a pilot sample and revise ambiguous categories.
4. Have at least two annotators label a subset and discuss disagreement.
5. Compare a lexicon baseline, a supervised model and a prompted model if feasible.
6. Test by party, period and speech type, not only overall.
7. Read false positives, false negatives and high-confidence cases.
8. Use topic or cluster analysis only as a complementary exploratory view.
9. Present model output as evidence about language in the corpus, not direct access to speakers' inner states.

## Practice

Write a one-page codebook for one category: relevance, sentiment, stance or emotion. Include five positive examples, five exclusions, two uncertain cases, the unit of analysis and the consequences of a false positive and false negative.

## Reflection

- Are you measuring language, an attributed state, or a psychological state?
- Could a model predict the label from source or period without reading the relevant passage?
- Which human disagreements reveal genuine conceptual complexity rather than poor annotation?

## Summary

Classification and topic analysis can organize large text collections, but labels and themes are constructed through operational definitions, data and modelling choices. Sentiment is not emotion, a topic is not an independently existing subject, and fluent model output is not validation. Codebooks, baselines, held-out evaluation, subgroup error analysis, sensitivity checks and close reading turn these methods into defensible humanities evidence.
