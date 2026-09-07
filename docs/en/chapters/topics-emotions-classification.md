---
title: "Topics, sentiment and emotion"
description: "How to keep exploratory topics, clusters, supervised labels and contextual emotion claims methodologically distinct."
tags: [classification, clustering, topic-modeling, sentiment, stance, emotion, stability, validation]
status: draft
---

# Topics, sentiment and emotion

A newspaper sentence says, “Wonderful—another delay.” A lexicon finds a positive
word, a polarity classifier may predict negative sentiment, a topic model may
place the sentence near museum administration, and a human reader may leave the
speaker’s emotion unresolved. These outputs answer different questions. Which
one could support the historical claim you want to make?

## Learning outcomes

After this chapter, you should be able to:

- distinguish topic modelling, clustering and supervised classification;
- compare bag-of-words and contextual representations;
- explain how document segmentation, topic count, initialization and random seed
  affect an exploratory topic solution;
- match topics across runs and retain unstable or unmatched components;
- design train, validation and test partitions without source leakage;
- evaluate imbalanced classification against simple baselines and calibration;
- distinguish lexical association, sentiment, stance, affect, expressed emotion,
  attributed emotion and reader response; and
- identify temporal, domain, multilingual, OCR and translation limits.

## Before you begin

For *Brilliant—another glorious delay*, list all text-supported statements you
can make without knowing the author. The words have positive lexical associations.
The utterance likely performs negative evaluation through irony. The target is a
delay. The experiencer of a discrete emotion may remain unknown. The reader’s
response is not contained in the sentence. This separation is the beginning of a
codebook.

Classification operationalizes a concept rather than discovering a self-evident
category. Use [Models, evidence and interpretation](models-evidence-interpretation.md)
to keep codebook, input representation, output, validation evidence and claim
distinct.

## Three model families, three kinds of output

### Topic modelling

Topic models represent recurring co-occurrence patterns. Classical probabilistic
models describe documents as mixtures of word distributions; non-negative matrix
factorization (NMF) decomposes a non-negative document–term matrix into document
weights and term components. Researchers may interpret a component as a theme
after inspecting its terms and documents. The component is not an independently
existing subject and does not arrive with a trustworthy name.

### Clustering

Clustering groups observations by similarity under a chosen representation and
distance. A cluster usually assigns an observation to a group, whereas a topic
model can give one document weights across multiple components. Boundaries,
cluster shape and even the meaning of distance depend on the method. Calling a
cluster a topic does not make its members share one historical cause.

### Supervised classification

A classifier learns to predict categories already defined in labelled data:
genre, relevance, sentiment, stance, emotion or another operational label. Its
quality cannot exceed the coherence and coverage of the codebook and annotations.
Unlike exploratory topics, supervised labels have declared targets, but they are
still constructed research variables rather than natural kinds.

## Units and representations change the question

A model cannot represent what segmentation removes. Whole books emphasize broad
vocabulary; chapters or passages reveal local shifts; sentences help contextual
classification but may lose speaker and argument. Sliding windows duplicate
context and violate independence if they are treated as separate documents.
Preserve the source document ID through every segment so train/test leakage and
aggregation remain visible.

A **bag-of-words** representation records forms, lemmas or n-grams while largely
ignoring order. It is sparse and inspectable: top weights can be traced to exact
terms. It struggles with long-distance context, word sense, negation and irony.
A **contextual representation** maps a word or passage using a learned model that
encodes surrounding language. It can capture distinctions missed by counts, but
inherits opaque training data, model version, tokenization, language coverage and
prompt or pooling decisions. Greater representational complexity does not remove
the need for source reading.

For Slovene and code-switched material, test the exact language variety. A
multilingual model may allocate capacity unevenly across languages; a
Slovene-specific model may mishandle German, Italian, Croatian or dialectal
passages. Translation is not a neutral preprocessing shortcut. It changes lexical
choice, rhythm, named entities, sentiment cues and possibly topic structure, so a
translated corpus is a new modelled layer with its own provenance.

## Topic solutions are conditional

Results depend on document segmentation, vocabulary, normalization, stop list,
minimum and maximum document frequency, weighting, component count, model family,
initialization, random seed, convergence settings, corpus composition and
duplicates. OCR errors may become high-weight rare terms; lemmatization may reduce
inflectional sparsity while importing annotation error.

The **topic count** controls granularity. Too few components can merge distinct
patterns; too many can split one pattern, isolate a document or model noise.
There is rarely one hidden correct count. Compare several counts that correspond
to plausible levels of inquiry and report splits, merges and disappearances.

Randomized initialization searches a solution space with multiple local optima.
Setting a **random seed** makes one run repeatable, not stable. Repeat multiple
seeds under the same settings. Then change topic count or segmentation to test a
different source of sensitivity.

## Match topics before comparing them

Topic number is arbitrary across runs: topic 1 in seed 7 need not be topic 1 in
seed 19. Define a matching rule. A transparent teaching rule can compare sets of
top terms using Jaccard overlap:

```text
J(A, B) = |A ∩ B| / |A ∪ B|
```

Pair topics one-to-one to maximize total overlap, using a documented assignment
method and tie rule. Matching by document weights or a distributional distance
may be preferable in a larger study. Whatever the rule, retain low-overlap and
unmatched topics. They are evidence of instability, not inconvenient rows.

The issue is not whether a score crosses a universal threshold. Inspect whether
the same terms and documents support a comparable reading. A numerically coherent
topic can be boilerplate, OCR damage or one prolific source. Conversely, a
historically meaningful pattern can use varied vocabulary and score modestly.
Numerical coherence and interpretive validity are different judgments.

## Human interpretation is part of the method

For every reported component, read several high-weight documents, a middling
document, a low or contradictory document, and documents from relevant metadata
groups. Record a provisional label, evidence passages, exclusions, uncertainty
and alternative labels. The label must be narrower than the observed pattern.
“Archival description vocabulary in this synthetic set” is safer than “the
archive topic in Slovene culture.”

Topic prevalence is a model weight, not the proportion of real-world attention.
Aggregate it by metadata only after checking document length, sampling,
uncertainty and source dependence. A change in preservation or OCR quality can
appear as thematic change.

Keep an interpretation ledger that joins each label to its run identifier,
component number, high-weight passages, counterexamples and reviewer. If a
second reader proposes a different label, preserve both labels and the evidence
that distinguishes them. This makes interpretation auditable without pretending
that the software discovered a uniquely correct name.

## Supervised evaluation requires separation

Begin with a codebook that defines unit, inclusion, exclusion, mixed and uncertain
cases, intended use and consequences of false positives and false negatives.
Pilot it with more than one annotator where feasible. Agreement is evidence about
the codebook and task; disagreement can reveal genuine interpretive complexity.
Do not erase it by forced adjudication without retaining the earlier decisions.

Separate **training**, **validation** and **test** roles. Training fits parameters;
validation selects features, thresholds or prompts; a held-out test estimates
performance after those choices. Split by document, author, issue or source when
segments could leak. Near duplicates in train and test can create impressive but
meaningless scores.

Compare against simple baselines: majority class, stratified random prediction,
a transparent lexical rule or metadata-only model. For imbalanced labels, report
a confusion matrix and class-specific precision, recall and F1 rather than only
accuracy. Macro averages weight classes equally; micro averages weight instances.
State which question the average answers.

When a score is used as a probability or to set review priority, inspect
**calibration**: among cases assigned probability 0.8, is the label correct about
80% of the time on appropriate held-out data? Ranking can be useful even when
calibration is poor, but the value must not be interpreted as confidence without
evidence.

Temporal and domain shift limit every evaluation. A classifier trained on modern
reviews may learn polarity words that do not transfer to historical letters.
Party, genre, source platform, OCR system or annotation convention can change.
Report performance by the strata relevant to the research and revalidate after a
substantive shift.

## Sentiment, stance, affect and emotion are not synonyms

**Sentiment** usually means positive, negative or neutral evaluation toward a
target. **Stance** concerns support, opposition or positioning toward a
proposition or actor. **Affect** can refer broadly to expressed or evoked valence
and intensity. **Emotion** may use discrete categories such as joy, fear, anger
and sadness or dimensional schemes such as valence and arousal. Define rather
than interchange these terms.

Emotion work needs further roles:

- **lexical association:** a form is associated with a category in a lexicon;
- **expressed emotion:** wording presents an emotion as currently expressed;
- **attributed emotion:** narrator or speaker assigns emotion to someone else;
- **experiencer:** the represented bearer of the emotion;
- **target or stimulus:** the person, object, event or proposition toward which
  the emotion is directed or which evokes it;
- **quoted speech:** an embedded voice whose wording must not be transferred to
  the reporter or author;
- **narrator stance:** the narrator’s evaluative position, which may differ from
  every character’s emotion; and
- **reader response:** an empirical or theoretical claim about readers, not a
  label recoverable directly from words on the page.

Negation can cancel *sad*: “she was not sad.” Modality weakens commitment: “she
may have feared” differs from “she feared.” Irony can reverse evaluative force
without licensing a discrete emotion: “How wonderful” after another failure.
Metalinguistic mention also matters: “anger in the record is not necessarily the
author’s anger.” A lexicon hit proves lexical association only.

## A transparent lexical baseline

A lexicon is useful because every match can be inspected. Record language,
version, source, construction method, categories, unit, matching rule, licence
and redistribution terms. Do not copy a third-party lexicon into a teaching
packet merely because it is downloadable. Inflection and lemmatization matter in
Slovene, and translated categories need linguistic and cultural validation.

A baseline should preserve zero-match cases, false positives and false negatives.
Adjusting a lexicon after reading evaluation examples is model development; test
the revision on different examples. Sensitivity to exact forms versus lemmas, or
to adding one documented entry, reveals what the method gains and loses.

## Recurring bounded comparison

The [text and NLP validation packet](../../assets/downloads/text-nlp-validation-v1.zip)
supports a deliberately small comparison. Its emotion sample has eight synthetic
sentences and an original eight-entry teaching micro-lexicon. Its topic sample
has twelve synthetic documents. Neither estimates a historical population.

| Method | Unit and input | Output and validation | Supported claim | Unsupported claim | Gain, loss and known failure |
| --- | --- | --- | --- | --- | --- |
| exact-form lexicon | sentence; surface forms | category hits compared with an eight-case machine-assisted reference draft pending human review | which declared forms match | who truly feels an emotion | transparent; misses inflection and context |
| contextual reference annotation | sentence plus context and codebook | emotion, experiencer, target, voice, negation, irony and uncertainty in a draft pending human review | how the codebook was applied in the draft | objective psychology or full-corpus prevalence | contextual; contestable and labour-intensive |
| supervised classifier | would require labelled train/validation/test units | deliberately not fitted: eight cases are inadequate | none for this packet | predictive performance | omission prevents a decorative, leaky model |
| NMF topic exploration | document; TF-IDF bag of words | 2, 3 and 4 components × seeds 7, 19 and 31; matched terms and read passages | sensitivity of this synthetic representation | general thematic structure | shows splits and instability; tiny and vocabulary-bound |

The emotion examples include quotation (*obiskovalci se bojijo*), negated
sadness, metalinguistic *jeza*, attributed fear, ironic *čudovita* and a zero-match
past-tense form *bali*. Exact matching therefore yields observable false positives
and a false negative. The contextual draft identifies experiencer and target and may
leave irony unresolved rather than invent a feeling.

The NMF demonstration holds vectorization fixed while changing seed and component
count. Some components retain related terms and documents; others merge archives,
museums, language and press vocabulary differently. That is a lesson about
sensitivity, not evidence that the authored themes were “discovered.”

## Failure modes and ethical limits

Common failures include naming topics from top words alone, choosing a topic count
because the chart looks tidy, discarding unstable runs, splitting sentences from
one source across train and test, reporting accuracy for an imbalanced task,
treating model probability as calibrated confidence and translating material
without recording the intervention.

Emotion and stance labels can pathologize people, infer protected attributes or
misrepresent quoted speakers. Historical vocabulary may encode violence and
stigma. Minimize personal data, preserve voice and source context, document
uncertainty, audit errors by relevant groups and avoid claims about inner states
that the text cannot warrant. Check corpus, lexicon and model licences separately.

## Practice

Complete both paired workflows:

1. [How do I test topic-model stability and interpretability?](../workflows/text-analysis/test-topic-model-stability-and-interpretability.md)
2. [How do I analyse emotion with a lexicon and a manual check?](../workflows/text-analysis/analyse-emotion-with-a-lexicon-and-manual-check.md)

For each, write one supported and one unsupported claim. Identify which change in
source, representation or codebook would most threaten the supported claim.

## Reflection

- Are you organizing lexical patterns, predicting a codebook label or inferring a
  human state?
- Which documents or speakers could leak across evaluation partitions?
- Which unstable topic was most tempting to name, and what contradicted it?
- Does a quoted emotion belong to the quoted speaker, narrator, author or none of
  these without more evidence?
- What temporal, domain or language shift requires new validation?

## Summary

Topic modelling, clustering and supervised classification produce different
representations and require different validation. Topic counts, seeds,
initialization, segmentation and matching rules make stability an empirical
question. Supervised labels require separated data, baselines, class-aware metrics
and shift tests. Emotion analysis must distinguish words, evaluation, voice,
experiencer, target and reader response. Source-linked examples, retained
uncertainty and human reading keep these outputs within defensible claims.

## Further reading

- Su, Jinyu, David Greene, and Derek O’Callaghan. 2016. “Topic Stability over
  Noisy Sources.” [ACL Anthology](https://aclanthology.org/W16-3913/).
- Morstatter, Fred, and Huan Liu. 2018. “In Search of Coherence and Consensus:
  Measuring the Interpretability of Statistical Topics.” *Journal of Machine
  Learning Research* 18 (169): 1–32.
  [JMLR article](https://jmlr.org/papers/v18/17-069.html).
- Bostan, Laura Ana Maria, Evgeny Kim, and Roman Klinger. 2020. “GoodNewsEveryone:
  A Corpus of News Headlines Annotated with Emotions, Semantic Roles, and Reader
  Perception.” [ACL Anthology](https://aclanthology.org/2020.peoples-1.12/).
- Reschke, Kevin, and Pranav Anand. 2011. “Extracting Contextual Evaluativity.”
  [ACL Anthology](https://aclanthology.org/W11-1511/).
