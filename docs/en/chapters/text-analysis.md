---
title: "Text analysis"
description: "How frequency, distribution, concordance, keyness and collocation become source-aware humanities evidence."
tags: [frequency, document-frequency, dispersion, concordance, keyness, collocation, stylometry]
status: draft
---

# Text analysis

A newspaper uses *svoboda* repeatedly in one long editorial. Ten other articles
never use it. Is freedom characteristic of the collection, or characteristic of
one document? The answer changes when we count occurrences, documents or
distribution—and changes again when OCR, genre and document length enter the
comparison.

## Learning outcomes

After this chapter, you should be able to:

- distinguish token frequency, normalized frequency, document frequency and
  dispersion;
- define the unit, denominator, query and corpus partition behind a count;
- use concordances to audit meaning, quotation, negation and boilerplate;
- explain why keywords require a comparable reference corpus;
- interpret collocation as parameter-dependent association rather than meaning;
- identify source, OCR, annotation and sampling effects in a quantitative result;
- separate exploratory pattern finding from corroboration; and
- preserve enough evidence to reproduce and challenge an analysis.

## Before you begin

Suppose a word occurs 300 times in corpus A and 180 times in corpus B. Write down
what you would need before calling it more characteristic of A. At minimum you
need corpus sizes, document counts and distribution, genres, dates, duplicate
policy, textual layers and a definition of the counted form. The two numbers
alone are outputs, not evidence.

Return to [Models, evidence and interpretation](models-evidence-interpretation.md)
if you need to distinguish a measured pattern from an interpretation. If your
count uses lemmas or grammatical categories, read
[Linguistic annotation and CLASSLA](linguistic-annotation-classla.md) as well.

## Core argument: every count embeds a corpus model

Text analysis turns repeated textual features into structured comparisons. A
count seems elementary, but it already embeds decisions about the source,
document boundary, transcription, normalization, tokenization, query and
denominator. These decisions determine what can be found.

A defensible result therefore has four connected parts:

1. **description:** what the corpus, query and calculation contain;
2. **evidence:** the counts, contexts, distributions and uncertainty relevant to
   the stated question;
3. **interpretation:** a historically and linguistically informed account of
   what the pattern may mean; and
4. **recommendation or decision:** the next sampling, reading or validation step.

Do not let the software collapse these parts into a ranked list that appears to
interpret itself.

## Frequency answers “how many times?”

**Token frequency** is the number of occurrences of a defined item. The item may
be an exact form, a case-folded form, a lemma, a phrase or an annotated pattern.
State which. Counting `arhiv`, `Arhiv` and inflected forms together is not a
neutral convenience; it is an operational definition.

Raw counts are useful within one collection and for checking data. They are not
directly comparable when corpus sizes differ. A **normalized frequency** uses a
declared denominator, often:

```text
normalized frequency = item occurrences / all eligible tokens × 10,000
```

“Eligible” matters. Are punctuation, metadata, repeated headers and unreadable
OCR fragments included? A rate per 10,000 tokens compares relative textual
space, not the probability that a document or author uses the item. If documents
vary greatly in length, one long text can dominate both numerator and denominator.

## Document frequency answers “how widely?”

**Document frequency (DF)** counts documents containing at least one occurrence.
Its denominator is the number of eligible documents. Report both the count and
share:

```text
document share = documents containing the item / eligible documents
```

Frequency and DF expose different corpus shapes. Ten uses in one editorial give
frequency 10 and DF 1. One use in each of ten articles gives the same frequency
but DF 10. Neither is inherently better. The first may signal an intensive local
argument; the second may show wider circulation. Document boundaries must be
meaningful: splitting one book into chapters changes DF without changing the
text.

When authors, issues or events—not files—are the real sampling units, calculate
those units too. Treating every article by one prolific author as independent
can exaggerate the reach of an individual habit.

## Dispersion answers “how evenly?”

DF distinguishes presence from absence but ignores concentration among present
documents. **Dispersion** describes how occurrences are distributed across
documents or meaningful corpus parts. Always name the measure and partition.

The teaching packet uses Juilland’s D across four equal authored theme groups.
For group frequencies \(f_i\), mean \(\bar f\), population standard deviation
\(s\), and \(n\) groups:

```text
D = 1 - (s / mean) / sqrt(n - 1)
```

With equal groups, D approaches 1 when occurrences are evenly spread and 0 when
they are confined to one group. The measure is undefined for zero total
frequency. Unequal corpus parts require an adjusted measure or rate-based
approach; do not apply this classroom calculation to uneven real collections
without reconsidering its assumptions. A dispersion value describes a partition,
not a word’s inherent generality.

Report the per-part counts beside D. A single index conceals which group drives
the imbalance and whether the partition corresponds to the historical question.

## Concordances reconnect pattern and passage

A keyword-in-context (KWIC) concordance places each occurrence in a bounded left
and right window. It bridges distant and close reading by making a query
inspectable without pretending that a short window is the whole text.

Use concordances to:

- separate homographs, names and irrelevant senses;
- inspect negation, reported speech, quotation and irony;
- find repeated headers, advertisements or syndicated text;
- compare grammatical constructions and nearby evaluative language;
- locate passages for sustained reading; and
- explain why a count changed after OCR correction or lemmatization.

Preserve document ID, occurrence number, query form, offsets or token positions,
window size, sorting rule and source layer. A screenshot is not a reproducible
concordance. Increase the window or open the document whenever interpretation
depends on speaker, genre or argument beyond the snippet.

## Keywords require a reference corpus

A **keyword** is unusually frequent in a target corpus relative to a reference
corpus. It is not merely a common or important-looking word. Both corpora define
the result.

The reference should control the contrast you intend. To compare two parties in
one election, align period, genre, medium and document-selection rules. Comparing
one party’s speeches with a general web corpus mixes party, politics, speech,
period and medium effects. A “neutral” reference does not exist; there are only
references suitable or unsuitable for a question.

Log-likelihood and related tests measure evidence against equal relative
frequency under assumptions. Effect sizes such as log ratio describe magnitude
and direction. Very large corpora can make tiny differences statistically strong.
Publish target and reference counts, token totals, smoothing rule for zeros,
statistic, effect size, multiple-comparison policy and concordances. A ranked
keyword list is the beginning of interpretation, not its conclusion.

## Collocation measures association, not meaning

A **collocate** co-occurs with a node within a defined span or grammatical
relation more than expected under a stated baseline. Results depend on:

- whether the node is a form, lemma or pattern;
- window width, direction and sentence boundaries;
- tokenization and stop-list policy;
- minimum node, collocate and pair frequency;
- association measure; and
- corpus subdivision and metadata filters.

Pointwise mutual information tends to favour relatively exclusive and sometimes
rare pairs. Frequency- or likelihood-oriented measures tend to favour robust,
common patterns. LogDice offers a bounded association score useful for comparing
pairs but still inherits preprocessing and sampling. No measure proves a semantic
relation, evaluative stance or causal connection. Inspect concordances and the
documents in which pairs cluster.

## Comparability comes before calculation

Before comparing groups, audit document counts and lengths, authors, genres,
dates, venues, duplicate and syndication patterns, missing material, OCR quality,
language variety, annotation quality and selection rules. A difference in
publication practice can masquerade as lexical change.

Aggregates can produce Simpson’s paradox: an overall trend may reverse within
genre, outlet or period. Produce document-level summaries and stratified results.
A token is not an independent sample when thousands come from one document.
Balance is not always historically desirable, but imbalance must be visible and
interpreted rather than silently normalized away.

OCR deserves special attention. Recognition errors can reduce a word’s apparent
frequency, create false rare words, damage function words and change corpus size.
If one comparison group has worse OCR, a normalized rate may still be biased.
Report quality by group, test a corrected sample and trace high-impact candidates
to page images or reviewed transcriptions.

## Preserve denominators and uncertainty

Do not save only a final chart. A reusable document table should contain a stable
ID, source citation, date, author or unresolved author status, genre, language,
text-layer identifier, rights status, eligible-token count, OCR-quality measure
where available, inclusion decision and reason. A query table should contain the
query string or pattern, case and lemma policy, software/script revision,
timestamp and input hash. Derived rows should retain the document ID so every
aggregate can be unfolded.

Uncertainty enters before statistical modelling. A missing issue changes the
corpus denominator; uncertain dates change period strata; OCR confidence may not
be calibrated; an ambiguous concordance changes the numerator. Record these as
fields, ranges or alternative analyses rather than converting every uncertainty
to a confident value. For a small corpus, showing all document counts can be more
informative than an elaborate interval based on implausible independence.

When sampling supports inference, choose an uncertainty method that respects the
sampling unit. Resampling tokens from one article exaggerates information;
resampling documents, authors or issues may better match the claim. Report the
number of independent units and assumptions. A significance value cannot repair
selection bias, unbalanced preservation or an inappropriate reference corpus.

Before interpreting, establish stopping rules. Investigate if one document
contributes more than a declared share, if OCR quality differs materially between
groups, if top candidates vanish under a plausible preprocessing choice, or if
concordance review rejects many matches. The remedy may be a corrected sample, a
document-level analysis or a narrower claim—not another decorative statistic.

## Preprocessing is part of the argument

Case folding, Unicode normalization, punctuation removal, stop-word filtering,
stemming and lemmatization change the analytical object. Preserve the source
layer and record transformations in order. Apply the same declared rule across
a comparison unless the research design justifies otherwise.

Stop words are not inherently uninformative. Function words can carry style,
register and grammatical structure. Removing them may help a topic model while
destroying a stylometric question. Lemmas reduce inflectional sparsity but can
import annotation error and erase historically meaningful forms. Run sensitivity
checks with plausible alternatives instead of searching for one universally
correct preprocessing pipeline.

## Style and stylometry

Stylometry compares documents through measurable features such as function-word
frequencies, character n-grams, sentence length or grammatical patterns. It can
support questions about authorship, genre, period and translation style, but a
cluster does not name its cause.

Separate feature design, distance or model, evaluation and historical
interpretation. Do not place chunks from the same work in both training and test
sets. Repeat analyses across plausible chunk sizes, feature sets, OCR thresholds
and metadata controls. Publication date, editor, genre and recognition quality
can produce an apparent authorial signature.

## From exploration to corroboration

Exploration is valuable for discovering candidate patterns. It becomes circular
when the same data select the pattern, tune the parameters and then appear to
confirm it. Whenever possible, explore on one subset, state the claim and rule,
then test on held-out documents or another collection. Archive unsuccessful
queries and parameter choices as well as the attractive result.

Humanities evidence does not require pretending that interpretation is a
clinical trial. It does require honesty about when a pattern was noticed, which
alternatives were tried and what independent material could challenge it.

## Worked example: frequency is not reach

The [text and NLP validation packet](../../assets/downloads/text-nlp-validation-v1.zip)
contains twelve short, synthetic Slovene documents in four equal authored theme
groups. The corpus is designed for teaching and says nothing about real archives,
museums, language practice or newspapers.

The term *arhiv* occurs several times but is concentrated in a small number of
archive-themed documents. *Korpus* repeats within one language document.
*Svoboda* is prominent in one press document but absent elsewhere. Comparing
frequency, DF, document share, per-theme counts and Juilland’s D reveals these
different shapes. A concordance then shows whether occurrences make the same
claim or merely share a form.

The result supports statements about the constructed dataset: one term is
repeated locally; another reaches more documents; both may be confined to one
theme group. It does not support a claim about Slovene public discourse. The
synthetic design makes the metric distinction visible precisely so that the
student can test it before approaching consequential historical data.

## Failure modes and ethical limits

Common failures include comparing raw counts across unequal corpora, using file
names as meaningful documents, ignoring a dominant text, treating keywords as
topics, interpreting collocation as sentiment, discarding contradictory
concordances and reporting only a favourable parameter setting.

Counts can make harmful categories look objective. Search labels may reproduce
historical slurs; entity and demographic inferences can expose people; a corpus
may overrepresent preserved institutions and powerful speakers. Quote only what
the argument needs, respect rights and privacy, preserve provenance and describe
absence as a property of the collection rather than silence in the past.

## Practice

Complete [How do I compare frequency, document frequency and dispersion?](../workflows/text-analysis/compare-frequency-document-frequency-and-dispersion.md).
Choose three terms with contrasting distributions. For each, write a description
of the measure, one source-grounded interpretation and one claim the packet does
not warrant. Inspect every concordance line before deciding.

## Reflection

- Is your unit a token, sentence, document, work, author, issue or event?
- Could one document or duplicated passage generate the pattern?
- Does the reference corpus isolate the contrast you intend?
- Which preprocessing decision most changes the candidate list?
- What passage contradicts the aggregate pattern, and why does it matter?

## Summary

Frequency measures volume, document frequency measures reach and dispersion
measures distribution across a declared partition. Normalization makes a chosen
denominator explicit but does not repair an incomparable corpus. Concordances
return counts to passages; keywords depend on a suitable reference; collocations
depend on windows and association measures. Source criticism, metadata strata,
sensitivity checks and close reading turn calculations into defensible evidence.

## Further reading

- Gries, Stefan Th. 2008. “Dispersions and Adjusted Frequencies in Corpora.”
  *International Journal of Corpus Linguistics* 13 (4): 403–437.
  [https://doi.org/10.1075/ijcl.13.4.02gri](https://doi.org/10.1075/ijcl.13.4.02gri).
- Gries, Stefan Th. 2022. “Toward More Careful Corpus Statistics: Uncertainty
  Estimates for Frequencies, Dispersion, Association, and Keyness.” *Research
  Methods in Applied Linguistics* 1 (1).
  [https://doi.org/10.1016/j.rmal.2021.100002](https://doi.org/10.1016/j.rmal.2021.100002).
- Dunning, Ted. 1993. “Accurate Methods for the Statistics of Surprise and
  Coincidence.” *Computational Linguistics* 19 (1): 61–74.
  [ACL Anthology record](https://aclanthology.org/J93-1003/).
