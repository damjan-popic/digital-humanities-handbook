---
title: "Linguistic annotation and CLASSLA"
description: "How predicted linguistic layers become usable evidence through task-specific, source-aware validation."
tags: [annotation, CLASSLA, lemma, morphology, dependency-parsing, NER, validation]
status: draft
---

# Linguistic annotation and CLASSLA

A historian asks who is represented as speaking in newspapers from two periods.
Finding verbs is only the first problem. OCR may join words, historical forms may
be unfamiliar to a contemporary model, a lemma may be wrong, and a dependency
parse may connect the speaker to the wrong predicate. Which layer is reliable
enough for the claim—and how would we know?

## Learning outcomes

After this chapter, you should be able to:

- distinguish sentence segmentation, tokenization, lemmatization, UPOS,
  morphology, dependency parsing and named-entity recognition;
- explain why every annotation layer is a model-based claim;
- choose only the layers required by a humanities research question;
- document a CLASSLA run with package, processors, resources, environment and
  input/output checksums;
- design a contestable reference draft and a documented human-review plan;
- calculate layer-specific metrics with explicit denominators; and
- trace annotation errors to source conditions and interpretive risk.

## Before you begin

Consider *Zala je v Novi Gorici predstavila novo Zalo.* Is each occurrence of
*Zala* a person, a product, a place or something else? Which evidence would you
use: capitalization, inflection, surrounding words, a catalogue, or knowledge
of the event? Now imagine that OCR returned *Novl Gorici*. The entity error would
begin before entity recognition ran.

Write down one claim you hope to make from annotated text. Underline the exact
annotation fields that the claim depends on. If you cannot name them, revisit
[Models, evidence and interpretation](models-evidence-interpretation.md) before
running a pipeline.

## Core argument: annotation is an evidential chain

Linguistic annotation makes patterns queryable by adding explicit analytical
layers to a text. It does not recover properties that were simply waiting in the
file. A pipeline applies a segmentation policy, an annotation scheme and learned
regularities to a particular textual representation. The result is a chain:

> source object → transcription or OCR → normalized text → sentences and tokens
> → lexical and grammatical labels → query → aggregation → interpretation

An error or editorial decision at one stage constrains every later stage. A
merged OCR form can change token count, lemma, part of speech and syntax at once.
A normalized name can improve recognition while hiding historically meaningful
spelling. A high aggregate score can conceal systematic failure in the very
genre or social group being compared. Validation therefore has to follow the
research claim through the chain, not merely report that software completed.

## What the layers claim

### Sentences and tokens

Sentence segmentation proposes where one local context ends and another begins.
Tokenization proposes which strings count as words, punctuation or multiword
units. These choices determine the denominator for most later measurements.
Historical abbreviations, initials, hyphens, apostrophes and OCR-damaged spaces
are common failure points. If *naroda in* becomes *narodain*, a later tagger sees
one unknown word rather than a noun followed by a conjunction.

Keep the original text and stable document identifier. Where possible, retain
character offsets. CoNLL-U can represent a surface multiword token and its
component words separately; a flattened spreadsheet often loses that relation.

### Lemmas

A lemma groups inflected forms under a dictionary-like form. Lemmas are useful
for tracing concepts across case, number, person or tense, but they can collapse
distinctions and inherit dictionary conventions. Historical, dialectal and
named forms are especially sensitive. A wrong lemma can remove a relevant
occurrence from a query or add a homograph that does not belong.

Do not discard surface forms after lemmatization. Report whether counts use
forms, lower-cased forms or lemmas, and inspect the contexts that carry the
argument.

### UPOS and morphology

Universal part-of-speech tags (UPOS) provide broad categories such as `NOUN`,
`VERB`, `ADJ` and `PRON`. Morphological features add values such as case,
gender, number, person, tense and polarity. The XPOS field can retain a
language-specific tag. These are scheme-bound analyses, not universal labels
that every linguist would assign identically.

A humanities query must state its operationalization. “Agents” cannot simply be
equated with nominative nouns; passive voice, ellipsis and non-human subjects
complicate that shortcut. A morphology score should also say whether a token is
correct only when its complete feature bundle matches or whether individual
features are scored separately.

### Dependencies

A dependency parse assigns each syntactic word a head and a relation such as
`nsubj`, `obj` or `obl`. It can help find constructions rather than isolated
words—for example, a person linked as subject to a reporting verb. But one wrong
token boundary shifts identifiers, and one wrong predicate can change several
arcs. Unlabelled attachment asks whether the head is correct; labelled
attachment asks whether both head and relation are correct.

Dependencies approximate a syntactic reading. They do not by themselves
identify historical agency, responsibility, quotation source or causal force.
Those require contextual interpretation.

### Named entities

Named-entity recognition (NER) proposes spans and categories such as person,
organization or location. Measure exact spans as spans: token-level tag accuracy
can look high because most tokens are not entities. Report precision as correct
predicted spans divided by predicted spans, recall as correct predicted spans
divided by reference spans, and F1 as their harmonic mean.

Recognition is not entity resolution. Tagging *Ljubljana* as a location does not
link it to a stable authority record. *J. Novak*, *Janez Novak* and *Novak* may
refer to one person or several. Preserve aliases, dates, source provenance and
an unresolved state; a missing link is safer than a confident false identity.

## CLASSLA as regional infrastructure

CLASSLA supplies pipelines and resources for Slovene and other South Slavic
languages. Depending on language and model availability, a pipeline can perform
tokenization, sentence segmentation, part-of-speech and morphological tagging,
lemmatization, dependency parsing and NER. Its regional documentation and
connection to CLARIN.SI make models and tag sets easier to locate and cite. The
institutional context is discussed in
[Digital humanities in Slovenia](digital-humanities-in-slovenia.md).

A reproducible citation needs more than the name CLASSLA. The frozen teaching
run used CLASSLA `2.2.1`, Python `3.12.3`, CPU execution and the processors
`tokenize,pos,lemma,depparse,ner`. Its UTC inference timestamp was recovered from
the preserved candidate metadata-file time; the older runner did not preserve a
truthful resource-acquisition time, so that field remains `unknown`. Separate
records identify the operating platform, Python, Torch, NumPy, SciPy,
scikit-learn, CLASSLA, Stanza and Obeliks versions, the complete environment
lock, the command, normalized input and output hashes, and the SHA-256 value and
byte size of every resource file. Model files are not redistributed. Package
and resource licences must be checked separately before redistribution or
production use.

This detail does not imply that one frozen run is universally reproducible.
Hardware, packages and resources change. It makes the run identifiable and
allows a later researcher to distinguish a deliberate update from drift.

### Guidelines, treebanks and model practice

Universal Dependencies (UD) publishes cross-linguistic guidelines, but an
implemented pipeline does not annotate directly from the abstract guideline.
It learns from particular treebanks, language-specific conventions, conversion
histories and model objectives. A current model can therefore differ from a
plausible guideline reading, and two treebanks can resolve a construction
differently. Record the actual model resources and tag-set documentation, not
only “UD”. When a distinction matters, compare examples in the relevant
treebank, document your project rule and retain disagreement rather than quietly
rewriting the model output.

## Domain dependence and responsible intervention

Keep three strings conceptually separate: the **source form** visible in a page
or born-digital object, any **normalized form** produced by editorial policy, and
the exact **model input**. They may coincide, but do not assume that they do.
Store transformations and source offsets or another reversible alignment so a
reviewer can return from annotation to evidence. If normalization changes word
length or boundaries, document how offsets are translated.

Historical spelling, dialectal and other non-standard Slovene, and code-switching
can all fall outside the dominant training distribution. Abbreviations and names
are difficult for a different reason: sparse forms interact with punctuation,
capitalization, sentence boundaries and entity categories. Test these phenomena
as named strata. A single “historical” score can hide that edited prose succeeds
while advertisements, verse, German insertions or abbreviated women’s names fail.

Intervention can take several forms. **Manual correction** is appropriate for a
bounded, high-consequence set when decisions and earlier values remain visible.
A **rule-based remapping** can repair a systematic tag or normalization mismatch,
but it must be versioned, tested for false corrections and applied to new
material—not only the examples that inspired it. A **custom lexicon** can improve
known names or historical forms, but coverage is selective and may increase
false positives or encode outdated authority decisions. Retraining or adapting a
model needs sufficient licensed annotations and a held-out evaluation.

Never overwrite frozen automatic output with corrected labels. Preserve source,
prediction and reference draft as distinct layers. Report the downstream
calculation before and after the intervention; otherwise a technically improved
tag may have no demonstrated value for the research question.

## Choose only the layers the question requires

More processors do not automatically produce stronger evidence. Each adds time,
storage and another opportunity for error.

| Research operation | Likely minimum layers | Additional check |
| --- | --- | --- |
| Count variants of a word | tokens or lemmas | concordance and document distribution |
| Compare case marking | tokens, UPOS, morphology | exact feature-bundle review |
| Find speakers of reporting verbs | lemmas, UPOS, dependencies | quotation and voice review |
| Map named institutions | tokens, NER | entity resolution and place/time disambiguation |

Begin with the observable needed by the claim. Name the annotation that
approximates it and imagine the most damaging plausible error. If the
interpretation survives that error, the layer may be sufficient. If not,
strengthen the sample, correction process or claim.

## Build a reference, not an oracle

A useful reference sample is manually annotated or reviewed according to an
explicit policy. It is still a scholarly intervention. Record who reviewed it,
when, which source layer they saw, how OCR errors were treated, which scheme was
used and where reasonable disagreement remains. Independent double annotation
and adjudication improve reliability; when they are absent, say so.

The packet used here has not completed that process. Its labels form a
machine-assisted reference draft pending human review. Promotion to a
`human-reviewed` state requires a named reviewer, an ISO review date and a
declared review scope; until then, the draft records decisions to inspect rather
than settled ground truth.

Sample for likely variation rather than selecting only easy prose. Include
period, genre, document condition, named entities and phenomena central to the
question. Keep source damage separate from model error. If a provider OCR file
has already lost a word boundary, the tagger did not cause the recognition
error, though its response to that error still matters.

## Report one denominator per layer

“The model was 92% accurate” is incomplete. The unit and eligible set change by
layer. A compact evaluation should publish the counts behind every value:

For sentence segmentation, represent boundaries as positions or spans. Boundary
precision divides correct predicted boundaries by predicted boundaries; recall
divides them by reference boundaries; F1 combines the two. Exact sentence-span
agreement is stricter and is useful in this packet because each sample contains
one declared sentence. Token/span agreement should likewise say whether
punctuation, multiword-token ranges and character offsets are eligible.

| Layer | Example measure | Denominator |
| --- | --- | --- |
| sentence segmentation | exact sentence match | reference samples or sentences |
| tokenization | aligned correct word tokens | reference word tokens, plus insertions/deletions reported |
| lemma / UPOS | exact label accuracy | one-to-one aligned word tokens |
| morphology | exact feature-bundle accuracy | aligned tokens eligible for morphology |
| dependencies | UAS and LAS | aligned syntactic words whose heads are alignable |
| NER | span precision / recall / F1 | predicted spans / reference spans |

Do not average these into one prestige number. A perfect NER span score on two
entities is not strong evidence, and a dependency denominator that silently
excludes unaligned OCR tokens can flatter the result. Publish numerator,
denominator, exclusions and an error log.
Feature-level morphology can complement exact bundles by counting individual
attribute/value decisions, but it answers a different question and must expose
its own denominator.

## Preserve a result that can be audited

A Python object in memory is not yet a research output. Export a structured form
that preserves document, sentence and word identifiers; surface form and lemma;
UPOS, language-specific tag and features; head and dependency relation; entity
span; and a link to the source layer. CoNLL-U preserves linguistic structure
well. A token table may be convenient for analysis, but document metadata should
remain in a linked table rather than being copied inconsistently into every row.

Record normalization separately from the source. If you lower-case text,
standardize historical spelling or repair OCR before annotation, preserve the
unaltered layer and a reproducible transformation or decision log. A result must
not imply that edited characters came from the page. The same rule applies to
excluded passages and failed documents: absence from the final table is itself a
selection decision.

A minimal run record contains timestamps, package and runtime versions,
processor order and settings, model/resource identifiers or hashes, execution
device, input identifiers and hashes, output hashes, and the command or script
revision. A checksum proves byte identity, not correctness. Together with a
reference policy and error log, however, it lets another scholar reconstruct
which evidence was seen and which decisions intervened.

Set a decision rule before seeing the score. You might require manual review of
all named entities, reject a period comparison if recall differs materially by
period, or use annotations only to retrieve candidates for close reading. If the
denominator is too small or disagreement concentrates in the target category,
stop, expand validation and narrow the claim. “Unable to validate” is a useful
methodological result, not a failed software demonstration.

## Worked example: clean, historical and provider OCR

The [text and NLP validation packet](../../assets/downloads/text-nlp-validation-v1.zip)
compares four purposively selected Slovene sentences. Two are handbook-authored
contemporary examples. The other two are aligned textual realizations of one
1925 newspaper passage from the archival-friction packet: a manually checked
reference transcription and the declared provider OCR. They are not independent
historical observations.

The clean sentence beginning *Kustosinja Maja Kovač* produces plausible lemmas,
syntax and exact entity spans for the person, museum and Ljubljana. That success
is evidence for those selected items only. In the historical reference,
substantival *vse* invites a documented disagreement between an adverbial model
analysis and the draft reference’s pronoun/subject analysis. In the provider
OCR, *naroda in* is merged as *narodain*, *stanovske* becomes *stavovske*,
*kulturnega* becomes *kultrunega*, and relative *ki* becomes *i*. The last error
is analysed as a noun and helps redirect the dependency structure.

The comparison separates three descriptions:

1. **source condition:** what the page, transcription or provider OCR contains;
2. **annotation behaviour:** what the frozen pipeline predicts for that input;
3. **interpretive consequence:** which query, count or attribution could change.

Against the current reference draft, the corrected dependency results are:

| Input sample | UAS | LAS |
| --- | ---: | ---: |
| contemporary clean 1 | 11/11 | 11/11 |
| contemporary clean 2 | 9/9 | 9/9 |
| historical reference transcription | 50/52 | 50/52 |
| provider OCR | 43/46 | 42/46 |

These fractions describe agreement with a pending draft, not accuracy against a
human-adjudicated truth. Of 24 detailed disagreements, 14 recur across the
historical transcription and OCR layers: ten fields for *vse* and four dependency
fields for *stranko*. The remaining ten are provider-OCR-conditioned. This
cross-layer comparison is the basis for causal attribution; the input stratum
alone is not.

This is more informative than saying that OCR is “bad”. A joined conjunction
threatens word counts and syntax; a damaged relative marker threatens clause and
speaker attribution; an entity that remains correct may be robust for this one
passage. The error taxonomy does not excuse the output—it locates the point at
which intervention is warranted.

## Failure modes and responsible limits

Common failures include processing a PDF rather than its documented text layer,
normalizing away meaningful spelling, losing document IDs during export,
flattening multiword tokens, validating only familiar contemporary prose,
reporting a global score without denominators, and treating uncertain entity
resolution as certain.

Annotation can also amplify representational inequality. Names, varieties and
genres underrepresented in training resources may fail systematically. A query
about women, minority-language writers or regional institutions can therefore
be biased even when the overall metric appears high. Inspect errors by the
groups the research compares, protect sensitive personal data, and avoid
inferring identity or mental state from grammatical or entity labels.

## Practice

Complete [How do I evaluate CLASSLA on a domain-specific sample?](../workflows/nlp/evaluate-classla-on-a-domain-specific-sample.md).
Recalculate one metric from its numerator and denominator, trace two logged
errors back to the source layers, and write a claim that the evidence supports.
Then write a stronger claim that it does not support and identify the missing
validation.

## Reflection

- Which layer carries the greatest interpretive risk in your project?
- Does the validation sample include the periods, genres and social groups in
  your comparison?
- Which errors began in OCR or transcription rather than annotation?
- What would another qualified reviewer reasonably annotate differently?
- Which processors could you omit without weakening the argument?

## Summary

Linguistic annotation is an evidential chain of predicted, scheme-dependent
layers. CLASSLA provides valuable regional infrastructure, but a package name or
global benchmark cannot validate a humanities claim. Preserve source layers,
run only the processors you need, identify software and resources precisely,
build reference annotation with a documented review state, report layer-specific
denominators and connect every consequential error to the interpretation it
could change. In this packet, treat the machine-assisted draft as pending human
review, not as an adjudicated reference.

## Further reading

- Ljubešić, Nikola, Luka Terčon, and Kaja Dobrovoljc. 2024. *CLASSLA-Stanza: The Next Step for
  Linguistic Processing of South Slavic Languages*. [Archived release and
  citation record](https://doi.org/10.5281/zenodo.13936406).
- [CLASSLA source repository and usage documentation](https://github.com/clarinsi/classla).
- Universal Dependencies. [CoNLL-U format](https://universaldependencies.org/format.html)
  and [universal dependency relations](https://universaldependencies.org/u/dep/).
- Revisit [Texts, corpora and OCR](texts-corpora-ocr.md) for the distinction
  between source images, recognition output, corrected text and downstream use.
