---
title: "Data, metadata and models"
description: "How humanities materials become traceable records without erasing source wording, uncertainty, versions or interpretive decisions."
tags: [data, metadata, modelling, provenance, uncertainty]
status: draft
---

# Data, metadata and models

## Learning outcomes

After this chapter, you should be able to:

- distinguish source objects, provider metadata, research data, metadata and documentation;
- explain why a data model is an interpretation rather than neutral storage;
- design stable identifiers, source locators and a simple relational structure;
- preserve source wording alongside normalized dates, names and controlled terms;
- represent uncertainty, missingness, duplicates, reprints and versions explicitly;
- create an auditable provenance and correction log;
- select a metadata standard or vocabulary for a declared purpose and test its fit.

## Before you begin

Open a table you have used for research. Can you tell, without asking its
creator, what one row represents, which columns are required, what a blank
means, where each value came from, and whether a name is transcribed or
normalized? Can you return from a row to a page, line, image region or
catalogue record? If not, the table lacks semantics and provenance, not just
tidiness.

No database or coding experience is required. You need a small collection or
the [*Archival friction* teaching packet ZIP](../../assets/downloads/archival-friction-v1.zip);
the [packet source tree](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction)
is available for inspection.
Your outputs will be a record model, data dictionary, correction log and
quality report. A successful result preserves evidence even when a value is
normalized or left unresolved. The central failure mode is silent
replacement: making a table look consistent by erasing what the source,
provider or researcher actually said.

For the question and sampling frame, begin with [From question to
method](research-design.md). For the wider distinction among sources,
representations, outputs and evidence, see [Models, evidence and
interpretation](models-evidence-interpretation.md). The spreadsheet workflows
in [Scholarly-work foundations](../foundations/scholarly-work.md)
show how to keep raw, cleaned, decision and output layers separate without a
programming requirement.

## Data are made for a purpose

In humanities research, **data** are recorded observations or representations
used to support inquiry. **Metadata** describe objects, records or processes:
title, date, creator, language, rights, collection, source location,
transcription status or transformation. **Documentation** explains the model,
rules, history and limits that cannot be understood from cells alone.

The roles depend on the question. A publication date is metadata when you
retrieve a text, but analysed data in a history of publishing. A catalogue
description is metadata about an object and a historical source about the
institution that created the description.

Johanna Drucker uses *capta*—what has been taken—to emphasize that humanities
data are constituted through selection and parameterization rather than found
ready-made.[^drucker] The term is a valuable question, not a requirement to
rename every file. Ask: who selected this unit, according to which model,
from which surviving material, and with what loss?

## A model is a set of commitments

A **data model** states what kinds of things exist for the project, which
properties describe them, how they relate and which constraints apply. A
spreadsheet with one row per caption is already a model. It treats a caption
as a separable unit, chooses fields and decides which complexities remain in
notes.

Distinguish three levels:

1. A **conceptual model** names entities and relations in scholarly language:
   issue, page, image, caption, person, event, version and source.
2. A **logical model** translates these into tables, fields, identifiers,
   controlled values and constraints.
3. A **physical representation** stores them in CSV, a spreadsheet, XML,
   JSON, a relational database or another format.

Changing software without revisiting the first two levels does not repair a
poor model. Conversely, a careful small CSV can represent a defensible model.

Geoffrey Bowker and Susan Leigh Star show that classifications organize work
and distribute consequences while becoming easy to overlook as
infrastructure.[^bowker-star] Therefore keep the source's categories, the
provider's categories and your analytical categories distinguishable. A
historical polemical label is evidence about a publication, not automatically
an acceptable modern subject heading.

## Define the record before the fields

Complete the sentence:

> Each row represents exactly one ________.

If several answers fit, the table mixes levels. One row cannot safely be both
an issue and every person pictured in it. Repeating issue metadata in each
person row may be tolerable for a tiny export, but the underlying model still
contains separate entities.

For an illustrated periodical, a modest relational design might use:

- `issues(issue_id, title_as_printed, issue_date, source_id, rights_status)`;
- `pages(page_id, issue_id, page_label, file_id)`;
- `features(feature_id, page_id, feature_type, caption_as_printed, region)`;
- `persons(person_id, preferred_label, authority_uri, match_status)`;
- `feature_agents(feature_id, person_id, role, certainty)`;
- `decisions(decision_id, record_id, field, old_value, new_value, evidence)`.

Both designs are defensible:

| Schema | Enables | Suppresses or makes expensive |
| --- | --- | --- |
| Flat table | Rapid audit | Repeats data; obscures group portraits, versions and conflicting identities |
| Relational | Cross-entity queries; typed uncertainty | Requires joins; distances inspection from the page |

## Identifiers before labels

Names and titles are labels, not reliable identifiers. They change, repeat,
use several scripts and contain historical spelling. Give every record a
stable, opaque project identifier such as `AF-P2-003`. Never recycle it for a
different object. Preserve provider identifiers and external authority URIs
in separate fields.

A good identifier does not claim that two records denote the same person. It
only keeps your records stable. Identity is an evidential decision expressed
through a relation such as `same_as`, `possible_match`, `duplicate_of`,
`reprint_of` or `version_of`, with a status and rationale.

Every content record also needs a **source locator**: page, column, image
region, folio, timestamp or archival reference detailed enough for another
reader to inspect the claim. A generic link to a collection homepage is not a
locator.

## Preserve layers instead of overwriting

At least four values may legitimately differ:

1. **source form** — visible in the historical object;
2. **provider value** — catalogue metadata or machine OCR;
3. **researcher transcription or normalization** — a documented correction;
4. **analytical category** — a value created for a particular comparison.

Store them in different fields or tables. For a caption printed as “Mr.
Meker”, an OCR layer might agree, an authority-search layer might propose
“Ezra Meeker”, and the audited authority-link status may be
`candidate_rejected`. Replacing the printed form with the candidate makes the
source appear more certain than it is and prevents later review.

Keep four file or database layers even when you also separate values by
field: a **source/raw layer** that is never silently changed; an **interim
layer** for candidates and repeatable transformations; a
**processed/modelled layer** containing the accepted interpretation for a
stated purpose; and a **decision layer** recording interventions, rejections
and unresolved cases. The interim layer is not evidence merely because a
tool produced it, and the processed layer never replaces the source.

The teaching packet makes the directory roles still more explicit:
`source/` contains the unchanged PDF, captured provider records and the
byte-preserved dLib TXT export; `reference/` contains handbook-created
observations, editorial decisions and reference transcription; `teaching/`
declares synthetic disturbances; and `raw/` contains the selected, decoded
and whitespace-normalized OCR excerpt alongside deliberately awkward rows.
The remaining `interim/`, `cleaned/`, `output/`, `validation/` and
`known-problems/` layers preserve the subsequent evidence chain.

A correction log should contain at least a decision identifier, record and
field, previous and new value, action, evidence, responsible person or
process, date and rule version. Fix systematic problems through repeatable
transformations; use the log for source-specific judgement. Never “clean” the
only copy.

## Provenance is a chain of responsibility

**Provenance** records where a representation came from and how it changed.
The W3C PROV family describes entities, activities and agents, but a small
project does not need a full RDF implementation to benefit from the
distinction.[^prov] A readable ledger can state:

| Entity produced | Activity | Used entity | Responsible agent | Time/version |
| --- | --- | --- | --- | --- |
| committed PDF | download without byte changes | provider file URL | packet maintainer | access date and checksum |
| source record | manual selection and transcription | PDF page and region | researcher | codebook v1 |
| cleaned record | documented correction | raw record and decision | researcher or script | run date/version |
| chart | aggregation | cleaned release | named workflow | software and settings |

Checksums establish byte identity, not authenticity or accuracy. A matching
hash proves that two files are identical; it does not prove that the provider
described the object correctly or that your transcription is faithful.

## Dates need form, value and certainty

Humanities dates are often relative, approximate, disputed or incomplete.
Keep at least:

- the wording as printed, for example `dne 1. t. m.` (“on the first of this
  month”);
- a normalized value such as `1925-02-01`;
- a status such as `exact`, `derived_from_relative_date`, `approximate`,
  `uncertain` or `unknown`;
- the rule and contextual evidence used for normalization.

The Library of Congress Extended Date/Time Format (EDTF) provides syntax for
uncertain (`1984?`), approximate (`2004-06~`), unspecified and interval
dates.[^edtf] Use it only when your software supports the declared level and
your readers can recover the original wording. A plain interval with explicit
certainty fields may be more interoperable in a small project. Never turn
“probably 1925” into the exact date `1925-01-01` merely because a spreadsheet
expects a day.

## Printed identity, entity structure and authority reconciliation

Authority files can connect spelling variants and supply durable identifiers,
but reconciliation is a research claim. Preserve separately:

- `printed_person_or_group`, the local label from the source;
- `entity_structure` (`zero_people`, `one_person` or `multiple_people`);
- a normalized display label, if needed;
- the authority system and `authority_candidate` URI or label;
- `authority_link_status` (`not_attempted`, `not_reconciled`,
  `candidate_rejected`, `accepted`, `unresolved` or `not_applicable`);
- authority evidence, decision and reviewer;
- access date, because interfaces and records change.

Do not accept the highest search result solely because the label matches. Test
dates, roles, places, associates and source context. A historical newspaper
may misspell a name; two contemporaries may share one; an authority record
may itself be incomplete. The Getty Vocabularies, for example, provide
persistent subject identifiers and variant names but describe an evolving,
domain-bounded resource, not a universal list of people and places.[^getty]

Treat reconciliation as **linking with evidence**, not replacing the local
record. A clearly printed name is not an unresolved identity merely because
no URI has been assigned, and a group portrait is not one unresolved person.
If a tested candidate is insufficiently supported, `candidate_rejected` is a
valid, auditable result.

## Missingness has meanings

A blank can mean unknown, not recorded, illegible, not applicable, withheld,
not yet checked or lost during processing. These states have different
historical and ethical consequences. Define allowed missing-status values in
the data dictionary and use a separate note when needed.

Do not replace unknown values with zero. “No surviving record was found” is
not “zero events occurred”. Do not publish a suppressed value as `unknown` if
that erases a community or privacy decision; record the access category at an
appropriate level without exposing the protected value.

## Duplicates, reprints and versions are relations

Exact file copies can be detected with hashes, but documentary identity is
not only byte identity. A reprinted article, a revised edition, an OCR export
and a new scan of the same page can share content while serving different
research purposes.

Avoid one overloaded `duplicate` flag. Prefer typed relations:

- `duplicate_of`: the same record entered twice;
- `copy_of`: another carrier of substantially the same object;
- `reprint_of`: republication in a new issue or venue;
- `version_of`: a related state with meaningful change;
- `derived_from`: OCR, normalization, crop or analysis output based on a
  source representation.

Then state the analytical rule. A study of circulation may count reprints; a
lexical study may retain only one text instance; a study of OCR may compare
several scans of the same page. Never delete relations that later researchers
would need to reconstruct the choice.

## Standards are tools, not automatic quality

A standard supplies shared terms or structures, but it cannot decide what
your project should observe. Start from requirements, then choose a small
**application profile**: the fields, obligations, vocabularies and local rules
you will actually use.

- [DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)
  provide broad cross-domain properties and stable term URIs.
- [TEI P5](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/)
  represents textual structure and editorial alternatives; `<choice>` can
  group original and corrected forms rather than erasing one.[^tei]
- [CIDOC CRM](https://cidoc-crm.org/get-last-official-release) offers a
  conceptual model for cultural-heritage entities and event-centred
  relations. The last official release listed on 2 September 2026 was 7.1.3;
  later versions on the versions page were drafts.[^cidoc]

Interface and specification pages are mutable; record access dates and pin a
version when exact conformance matters. A minimal local schema with clear
crosswalks may be better than claiming full compliance with a large standard
you use only superficially.

Audit the fit with concrete questions: Can the profile preserve source
wording and a normalized value? Can it distinguish an uncertain identity
from a confirmed one? Can it record rights for both the source and your
annotations? Does export round-trip without losing language, diacritics,
identifiers or relations?

## Quality checks for a small scholarly dataset

Run structural and interpretive checks:

- identifiers are unique, non-blank and stable;
- foreign keys point to existing records;
- required source locators and rights fields are present;
- controlled values occur in the versioned vocabulary;
- normalized dates match their declared precision and certainty;
- original strings remain unchanged;
- accepted authority links have recorded evidence;
- duplicate and version relations are typed and non-circular;
- row counts and retained identifiers match the decision log;
- a stratified sample returns correctly to the facsimile;
- exports preserve UTF-8 text and leading identifier characters.

Automated checks find structural contradictions. They cannot decide whether a
caption is politically neutral, a person match is historically persuasive or
a category is adequate. Combine them with source review.

## Worked example: one object and eight reference observations

The teaching packet contains one authentic two-page issue. In `reference/`,
the handbook records eight source-grounded observations: one issue and seven
features. The observation table preserves transcribed labels, provider OCR,
date scope and status, a separate issue-context date, printed person/group
labels, entity structure, authority candidates and statuses, source locators
and evidence notes. `teaching/` introduces four declared problems. The
generated raw table therefore contains nine rows: three altered fields and
one duplicate row.

The audit proceeds as follows:

1. Verify the committed PDF against its provider and SHA-256.
2. Confirm that all eight reference-observation identifiers resolve to a page and region.
3. Compare each changed raw field with the facsimile, not only the clean
   answer table.
4. Restore the caption's capitalization where the image decides the matter.
5. Remove only the row explicitly declared as a synthetic duplicate; retain
   the underlying feature.
6. Reject the silent change from “Meker” to “Meeker”; retain Ezra Meeker as a
   reviewed candidate with `candidate_rejected`, not as an accepted identity.
7. Derive 1925-02-01 and 1925-01-27 under explicit rules, but leave the
   riverbed photograph's creation date blank/`unknown`; its issue date is
   context only.
8. Verify eight clean IDs, nine source-grounded editorial decisions, four
   synthetic reversals and no altered source bytes.

The clean result is not a claim that all eight records are complete. It is a
claim that every retained value has a declared evidential status and can be
audited.

## Practice: build and audit a record model

Using the [packet ZIP](../../assets/downloads/archival-friction-v1.zip)—with
its [source tree available for audit](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction)—or
five to ten records from your field, prepare:

1. a conceptual sketch of entities and relations;
2. a table or set of tables in which every row has one meaning;
3. stable internal identifiers and precise source locators;
4. separate source, provider, normalized and analytical values where they
   differ;
5. a data dictionary defining type, allowed values, missingness and
   obligation for every field;
6. one uncertain date, one unresolved authority candidate and one typed
   duplicate/version relation;
7. a correction and provenance log;
8. a quality report containing row counts, identifier checks and two manual
   source comparisons.

**Check:** another reader should be able to reconstruct one normalized value
and explain one unresolved value without asking you. **Failure mode:** if the
cleaned table is more confident than the source and the decision log cannot
explain why, restore the layers before analysing it.

## Reflection

- Which fields describe the historical object, and which describe your
  encounter with it?
- Which category comes from the source, provider, standard or research
  question?
- Could an external authority link import a modern or domain-specific
  identity into a historically ambiguous record?
- Which blank values represent archival silence, and which represent
  unfinished work?
- What would be lost if every reprint or version were collapsed into one
  “master” record?

## Summary

Humanities data are structured representations made for a purpose. A model
defines entities, properties, relations and constraints before a file format
implements them. Stable identifiers keep records continuous; source locators
return claims to evidence. Original, provider, normalized and analytical
values must remain distinguishable.

Dates require printed form, normalized value and certainty. Names require
evidence-based reconciliation, not automatic replacement. Missingness,
duplicates, reprints and versions carry meaning and should be modelled rather
than erased. Provenance and correction logs assign responsibility to each
transformation. Standards can improve exchange when used through a declared,
versioned application profile, but conformance does not substitute for
source criticism. Good data are not frictionless facts: they are records whose
construction, uncertainty and limits remain inspectable.

## Further reading and references

- Bowker, Geoffrey C., and Susan Leigh Star. [*Sorting Things Out:
  Classification and Its
  Consequences*](https://mitpress.mit.edu/9780262024617/sorting-things-out/).
  MIT Press, 1999. Publisher page accessed 2 September 2026.
- CIDOC CRM Special Interest Group. [*Definition of the CIDOC Conceptual
  Reference Model*, version
  7.1.3](https://cidoc-crm.org/get-last-official-release). February 2024.
  Accessed 2 September 2026.
- Dublin Core Metadata Initiative. “[DCMI Metadata
  Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/).”
  DCMI Recommendation, issued 20 January 2020. Accessed 2 September 2026.
- Drucker, Johanna. “[Humanities Approaches to Graphical
  Display](https://dhq.digitalhumanities.org/vol/5/1/000091/000091.html).”
  *Digital Humanities Quarterly* 5, no. 1 (2011). Accessed 2 September 2026.
- Library of Congress. “[Extended Date/Time Format (EDTF)
  Specification](https://www.loc.gov/standards/datetime/).” 4 February 2019.
  Accessed 2 September 2026.
- Moreau, Luc, and Paolo Missier, eds. “[PROV-DM: The PROV Data
  Model](https://www.w3.org/TR/prov-dm/).” W3C Recommendation, 30 April 2013.
  Accessed 2 September 2026.
- TEI Consortium. [*TEI P5: Guidelines for Electronic Text Encoding and
  Interchange*](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/), version
  4.11.0, 18 February 2026. Accessed 2 September 2026.

[^drucker]: Drucker, “Humanities Approaches to Graphical Display,” on data as
    capta and the interpretive character of parameterization.
[^bowker-star]: Bowker and Star, *Sorting Things Out*, especially their
    analysis of classification systems as consequential infrastructure.
[^prov]: W3C, “PROV-DM.” The formal model is optional here; the practical
    distinction among an entity, an activity and a responsible agent is the
    important minimum.
[^edtf]: Library of Congress, “EDTF Specification.” The 2019 specification
    defines conformance levels and syntax for reduced precision, uncertainty,
    approximation and intervals.
[^getty]: Getty Research Institute, “[Obtain the Getty
    Vocabularies](https://www.getty.edu/research/tools/vocabularies/obtain/).”
    The page documents identifiers, open-data terms and changing delivery
    services. Accessed 2 September 2026.
[^tei]: TEI Consortium, “[`<choice>`](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-choice.html),”
    P5 version 4.11.0. Accessed 2 September 2026.
[^cidoc]: CIDOC CRM Special Interest Group, “[Versions of the
    CIDOC-CRM](https://cidoc-crm.org/versions-of-the-cidoc-crm).” Accessed 2
    September 2026.
