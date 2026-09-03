---
title: "From question to method"
description: "How to turn a humanities question into a source-aware, testable and ethically bounded research design before selecting tools."
tags: [research design, operationalization, archives, validation]
status: draft
---

# From question to method

## Learning outcomes

After this chapter, you should be able to:

- turn a broad humanities interest into a bounded, answerable research question;
- distinguish an archive, a collection, a sampling frame and an analytical corpus;
- define units of observation and analysis, concepts, indicators and comparisons;
- reason carefully from absence without treating a catalogue gap as proof that an event did not occur;
- set source, rights, feasibility and quality gates before full data collection;
- plan provenance, manual validation, error analysis and stopping rules in advance;
- state the strongest claim the evidence could support and the evidence that would change your mind.

## Before you begin

Write down a question you would ask even if no digital tool existed. Underline
its nouns and verbs. The nouns often point to people, texts, events, places or
institutions; the verbs imply relations such as change, comparison,
circulation or representation. Now add: **according to which surviving
sources, for which period, and compared with what?**

No programming or statistics is required. You need a research question and
access to a small, lawfully reusable source set. Your output will be a design
card, a source-and-rights decision and a validation plan. A successful design
lets another reader identify every inferential step. Common failures are
starting from a tool, confusing convenient holdings with a population, and
letting undocumented cleaning decisions change the question.

This chapter turns the argument in [Models, evidence and
interpretation](models-evidence-interpretation.md) into a practical research
plan. [Data, metadata and models](data-metadata-models.md) develops the record
structure; [Texts, corpora and OCR](texts-corpora-ocr.md) addresses document
images, OCR/HTR and corpus sampling. These chapters share the small
[*Archival friction* teaching packet ZIP](../../assets/downloads/archival-friction-v1.zip),
whose [source tree remains inspectable](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction).

## Research design is an argument in advance

A research design connects a question to evidence before results are known.
It specifies what will count as a source, a case, an observation and a
comparison; how records will be selected and transformed; what could go
wrong; and how claims will be limited. It is not merely a timetable or a list
of software.

A useful design can be read as a chain:

> question → source population → accessible sampling frame → selected cases →
> representation and indicators → method → validation → bounded claim

Every arrow is contestable. A portal may expose only catalogued objects. A
scan may omit a verso. An OCR system may fail on names and diacritics. A
category such as “political event” may reflect a present-day codebook rather
than the publication's language. Research design makes these transitions
available for criticism rather than hiding them inside a finished dataset.

## Begin with the archive, not an imagined totality

An archive is not a transparent store of everything that happened. Records
were created for particular administrative, commercial, familial or
political purposes; some were never made, some were discarded, some were
withheld, and only part of what survives may be catalogued or digitized.
Michel-Rolph Trouillot describes silences entering historical production at
several moments, from the making of sources to the making of narratives.[^trouillot]
Rodney Carter likewise treats archival silence as a relation of power while
warning that silence can also be a strategy of people who decline to be
recorded.[^carter] Neither account licenses the researcher to fill a gap with
an attractive story.

Keep four scopes distinct:

| Scope | Practical question | Typical limitation |
| --- | --- | --- |
| **Target population of sources** | What records would be relevant if all had survived and were accessible? | It is often unknowable and partly hypothetical. |
| **Repository or collection** | What did an institution acquire, preserve and describe? | Appraisal, transfer, resources and institutional purpose shape survival. |
| **Sampling frame** | Which records could this project actually discover and obtain? | Catalogue quality, digitization, language, access rules and cost intervene. |
| **Analytical corpus** | Which accessible records pass the declared inclusion rules? | The researcher's exclusions create another boundary. |

Calling the last set “the archive” collapses four selections into one. Report
their sizes where possible, and describe unquantifiable gaps in prose.

### Selection decisions are evidence about the project

Maintain a selection log from the first search. For each query, repository or
box, record the date, search terms or shelfmarks, filters, result count,
access outcome and decision. Capture interface-specific details with an
access date because catalogues change. Keep stable identifiers rather than
session URLs. If a source can be viewed but not lawfully shared, record that
constraint before designing a classroom or reproducibility claim around it.

This log helps distinguish “the item does not appear in the searched frame”
from “the item did not exist”. It also reveals when a search vocabulary has
excluded historical spellings, minority languages or descriptions produced
under earlier cataloguing practices.

## Establish a source-and-rights gate

Before collecting at scale, audit one representative object from discovery
to reuse. The gate should answer:

1. **Identity:** is this the intended edition, issue, page or archival unit?
2. **Provenance:** which institution holds the object, and which service
   supplies the digital representation and metadata?
3. **Completeness:** are all required pages, attachments, columns or versions
   present?
4. **Rights and authority:** may you download, analyse, quote and redistribute
   the source, metadata and derived files? Do community or donor conditions
   impose further responsibilities?
5. **Technical access:** is there a stable identifier, download or snapshot?
   Does access require a mutable interface or account?
6. **Research fit:** can the object supply the observations needed by the
   question, including known difficult cases?

Record a **go**, **revise** or **stop** decision. Stop when essential rights
are unknown, provenance cannot be established, the required population is
systematically inaccessible, or the sample cannot test the intended claim.
Revise when a narrower question remains defensible. A smaller lawful project
is stronger than a large collection that cannot be inspected or shared.

“Open” is not the same as ethically unproblematic. The FAIR principles make
findability, accessibility, interoperability and reuse important properties
of research objects, including provenance and licences.[^fair] The CARE
principles add collective benefit, authority to control, responsibility and
ethics for Indigenous data governance.[^care] Apply relevant community norms
rather than treating maximum circulation as an automatic good.

## Turn the question into explicit design decisions

### Bound the question

Questions such as “How is national identity represented in newspapers?” are
intellectually meaningful but underspecified. A design must name a source
population, period, unit, relation and comparison. For example:

> How do image captions in the surviving issues of two named Slovene
> illustrated supplements, 1924–1926, assign political agency to named and
> unnamed groups, and how does that distribution differ by publication?

This still needs source criticism, but it identifies what will be compared.
It does not claim to measure what all readers believed or what “the nation”
was.

### Define observation, sampling and analysis units

The **observation unit** is what one record describes: a page, caption,
letter, person, event or relation. The **sampling unit** is what is selected:
perhaps an issue even when captions are analysed. The **analysis unit** is
what contributes to a comparison. These can differ, but the differences must
be declared.

If sentences from one article are treated as independent observations, a
long article can dominate and uncertainty can be understated. If people are
counted every time they appear, a single recurring public figure may shape a
publication-level result. Decide whether clustering by issue, author or
source is part of the design.

### Operationalize without mistaking an indicator for the concept

**Operationalization** connects a concept to observable, recordable and
contestable indicators. Adcock and Collier emphasize that measurement
validity depends on the relation among a background concept, its
context-specific formulation, indicators and scores.[^validity] In
humanities work, the process may combine structured coding and close reading.

“Visibility of women” might be represented by the share of named people,
quoted speech, image area, headline prominence, or roles assigned in
captions. Each indicator preserves a different aspect. Gender attribution
also requires a documented and ethically defensible rule; a name is not a
transparent measurement. Write a **claim limit** beside every indicator:

| Concept | Indicator | What it does not establish |
| --- | --- | --- |
| Prominence | caption position and image area on a page | reader attention or political influence |
| Attribution of agency | active grammatical role in a caption | the person's actual responsibility |
| Circulation | number of repository copies or reprints found | total historical readership |
| Absence | no match in a documented sampling frame | that the event, person or expression did not exist |

### Specify inclusion, exclusion and ambiguity

Write rules before the full pass. Include positive examples, counterexamples
and borderline cases. Say what happens to an anonymous caption, an uncertain
date, an item spanning two pages, a reprint and a record in two languages.
Preserve an “uncertain” state when the evidence is insufficient. Forced
certainty improves neither comparability nor truth.

When categories change during exploration, version the codebook and record
which rows were recoded. Do not revise old decisions invisibly to make an
emerging pattern cleaner.

## Comparison, baselines and negative evidence

A pattern becomes meaningful through comparison. Ask **compared with what?**
Useful baselines include another period, genre, institution or region; the
rest of the corpus; human agreement; a simple rule before a complex model;
and a shuffled or majority-class result. A sophisticated method that does not
improve the relevant evidence over a transparent baseline has not earned its
complexity.

Negative evidence requires a special audit. Before arguing from a missing
name or topic, ask:

- Was the relevant kind of record normally created and preserved?
- Does the catalogue index the feature being searched?
- Were spelling variants, languages, OCR errors and access restrictions
  tested?
- Is the denominator known?
- Would the same procedure find a positive control that should be present?

The strongest defensible statement may be: “No instance was found in 312
searchable captions under these queries and manual checks.” That is useful,
but it is narrower than “the publication never mentioned the person.”

## Separate exploration from confirmation

Exploration discovers patterns, revises categories and generates hypotheses.
Confirmation evaluates a pre-specified expectation against data and criteria
not chosen to favour the observed result. Many humanities projects move
iteratively between them; that movement becomes misleading only when the
history is concealed.

Keep an analysis diary with dated entries for corpus-boundary changes,
category revisions, thresholds, exclusions and visual choices. Label
exploratory charts. For a confirmatory pass, freeze the question, codebook,
primary comparison and acceptance criteria, or use a new sample when one is
available. If neither is possible, present the result as exploratory and make
the limitation part of the argument.

## Design provenance and validation together

Validation is not a final button. It is a plan for discovering where the
research design fails. Depending on the claim, include:

- a random sample for an overall error estimate and a stratified sample for
  rare or high-risk cases;
- independent double coding, followed by a disagreement log rather than only
  an agreement score;
- checks of source locators, retained identifiers, row counts and duplicate
  decisions;
- sensitivity tests under alternative inclusion rules, date ranges or
  normalization policies;
- close reading of central cases, boundary cases, errors and outliers;
- a comparison with a simpler baseline;
- a deliberate search for evidence that could contradict the preferred
  interpretation.

Define thresholds and actions in advance: for example, pause data collection
if more than 5% of sampled records lack resolvable source locators; redesign
the date field if two coders cannot consistently distinguish exact, derived,
approximate and unknown dates; do not aggregate a subgroup with fewer than a
declared number of independent documents.

A **stopping rule** prevents endless cleaning and convenient stopping after a
favourable result. It may be a fixed corpus boundary, saturation criterion,
time budget, target precision, maximum unresolved share or source-access
gate. Record both the rule and whether it was met.

## Worked example: *Archival friction*

The packet starts with one authentic historical object: a two-page 1925 issue
of *Ilustrirani Slovenec*. The handbook creates eight source-grounded
reference observations—one issue and seven features—from its captions.
These contain relative dates, historical names, partisan description and a
tempting but rejected authority candidate for the printed “Meker”. The
provider OCR corrupts several words and diacritics. Four additional
disturbances—a duplicate and conflicting values—are synthetic and separately
declared.

Suppose the question is: **Which source and processing uncertainties would
change a comparison of named political actors in illustrated captions?** A
compact design is:

- **Source population:** the two pages of the cited issue, not all Slovene
  illustrated press.
- **Sampling frame and corpus:** every captioned unit on those pages; the
  teaching table selects eight units for a pilot, so it cannot estimate the
  distribution of the whole issue without completing the inventory.
- **Observation unit:** one issue, portrait, group portrait or captioned
  feature; `record_kind` preserves the difference.
- **Indicators:** the printed person/group label, whether the unit represents
  zero, one or multiple people, the separate authority-link status, and
  whether a date is exact, rule-derived, unknown or not applicable.
- **Validation:** return every row to its PDF locator; compare provider OCR
  with the documented reference excerpt; verify eight clean observation
  identifiers, twelve editorial decisions and exclusion of only the declared
  synthetic duplicate. The riverbed photograph remains undated; the issue
  date is stored only as publication context.
- **Stopping rule:** no authority identifier is added until an independent
  source supports the match; unresolved cases remain unresolved.
- **Claim limit:** the result evaluates record construction in this pilot. It
  does not establish historical prominence or public opinion.

The unresolved row is not a failed exercise. It demonstrates that good
research design sometimes produces an explicit “not enough evidence”.

## Practice: a design and stop/go memo

Download the [packet ZIP](../../assets/downloads/archival-friction-v1.zip) or
use a small source set from your field; consult the [source tree](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction)
when auditing how the exercise was assembled. Produce a one-page memo with:

1. a bounded research question;
2. source population, repository holdings, sampling frame and analytical
   corpus;
3. source-and-rights gate with a go, revise or stop decision;
4. sampling, observation and analysis units;
5. two indicators and their claim limits;
6. inclusion, exclusion, duplicate and uncertainty rules;
7. one baseline and one negative-evidence check;
8. validation sample, error analysis and a stopping rule;
9. the strongest defensible claim and one finding that would make you revise
   it.

**Check:** exchange memos. Your reader should be able to predict one record
you would include, one you would exclude, and one you would keep as
uncertain. **Failure mode:** if the memo names a platform but not a source
population or unit, the method is still tool-led.

## Reflection

- Which absence in your project was produced before the archive, by the
  archive, by digitization, by search, or by your own rule?
- Which operational indicator is most convenient but least faithful to the
  concept?
- What right or community interest could override a technical possibility to
  collect or publish?
- Which error would most seriously damage the humanities interpretation?
- What evidence would genuinely change your conclusion?

## Summary

A defensible digital-humanities method begins with a bounded question and a
source-aware design. Archives, catalogues, interfaces and analytical corpora
are different selections. A source-and-rights gate tests identity,
provenance, completeness, reuse conditions, access and research fit before
scale. Units, indicators, comparisons and missing-value rules turn concepts
into inspectable operations without making them equivalent to their
measurements.

Selection logs, negative-evidence checks and explicit uncertainty prevent a
catalogue gap from becoming a historical fact. Exploration may revise a
design, but those revisions must remain visible. Provenance, validation,
error analysis and stopping rules are parts of the argument, not technical
appendices. The result is not certainty; it is a traceable account of what
the selected evidence can and cannot support.

## Further reading and references

- Adcock, Robert, and David Collier. “[Measurement Validity: A Shared
  Standard for Qualitative and Quantitative
  Research](https://doi.org/10.1017/S0003055401003100).” *American Political
  Science Review* 95, no. 3 (2001): 529–546. DOI:
  `10.1017/S0003055401003100`.
- Carter, Rodney G. S. “[Of Things Said and Unsaid: Power, Archival Silences,
  and Power in
  Silence](https://archivaria.ca/index.php/archivaria/article/view/12541).”
  *Archivaria* 61 (2006): 215–233. Accessed 2 September 2026.
- Global Indigenous Data Alliance. “[CARE Principles for Indigenous Data
  Governance](https://www.gida-global.org/careprinciples).” Accessed 2
  September 2026.
- Trouillot, Michel-Rolph. [*Silencing the Past: Power and the Production of
  History*](https://www.beacon.org/Silencing-the-Past-P1109.aspx). Boston:
  Beacon Press, 1995. Publisher page accessed 2 September 2026.
- Wilkinson, Mark D., et al. “[The FAIR Guiding Principles for Scientific
  Data Management and
  Stewardship](https://doi.org/10.1038/sdata.2016.18).” *Scientific Data* 3
  (2016): 160018. DOI: `10.1038/sdata.2016.18`.

[^trouillot]: Trouillot, *Silencing the Past*, especially his account of
    silences entering the production of sources, archives, narratives and
    retrospective significance.
[^carter]: Carter, “Of Things Said and Unsaid,” 215–233. The article treats
    archival silences as effects of power and also considers silence as an
    exercise of agency by marginalized people.
[^fair]: Wilkinson et al., “FAIR Guiding Principles.” FAIR concerns the
    properties and stewardship of research objects; it does not by itself
    settle whether access or reuse is ethically appropriate.
[^care]: Global Indigenous Data Alliance, “CARE Principles.” The principles
    are cited here as a corrective to assuming that technically open data
    should circulate without collective authority and responsibility.
[^validity]: Adcock and Collier, “Measurement Validity,” 529–546. Their
    framework crosses qualitative and quantitative research and emphasizes
    the contextual character of measurement claims.
