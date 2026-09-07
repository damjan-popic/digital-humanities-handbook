---
title: "Databases and SQL"
description: "Relational models, dated assertions and reproducible queries for historical evidence that changes and disagrees."
tags: [database, SQL, relational-model, identifiers, provenance]
status: draft
---

# Databases and SQL

## Learning outcomes

After this chapter, you should be able to:

- distinguish entities, attributes, relations, observations, assertions and events;
- compare a flat table, a normalized schema and a source-qualified assertion model;
- represent changing names, statuses, language relations and territorial membership;
- separate historical validity from the time an editor records or corrects a claim;
- run and audit date-sensitive SQL, including disagreement and missing evidence;
- explain what constraints, normalization and exports cannot guarantee.

## Before you begin

Can a person change country without moving, use two languages without having one
timeless “language”, or be called a servant and a seamstress by different sources?
A database that stores only `person.status`, `person.language` and `place.country`
may answer confidently because it has already removed the distinctions needed
to ask the question. Before opening software, write one query you want to answer
and one distinction you refuse to lose.

You need familiarity with rows, columns and source citation; basic SQL helps but
is not required for the conceptual comparison. Begin with [Models, evidence and
interpretation](models-evidence-interpretation.md). The practical prerequisite is
being able to preserve an input file and run a supplied Python script. No server,
paid service or personal data is needed for the example.

## A database is an argument about the world

A schema establishes what counts as a thing, which distinctions are repeatable,
and which relationships can be queried. Codd's relational model separates logical
data organization from physical storage and addresses redundancy and consistency;
it does not decide what a historical person, community or event is. Those remain
research decisions. [Codd 1970](https://doi.org/10.1145/362384.362685) provides the
technical foundation, not a warrant to treat a successful query as historical proof.

Consider the authentic [archival-friction packet](../../assets/downloads/archival-friction-v1.zip).
Its reference observation `AF-P1-003` transcribes the printed label “Dr. Ante
Trumbić”. This is initially an observation about a caption in a particular issue,
not an independently established biography. `AF-P2-003` retains “Mr. Meker” while
rejecting an attempted authority match. A database must allow that rejection to
remain visible without pretending that the printed person has vanished.

Source-oriented prosopography offers a useful precedent: make the relationship
between a source, a person and an assertion an object of study. Bradley and
Short's discussion supports distinguishing the historian's structured work from
the historical world it describes. Our teaching schema adopts that distinction;
it does not claim to implement a complete prosopographical ontology.
[Bradley and Short 2005](https://doi.org/10.1093/llc/fqi022).

## Entities, relationships and the level of a claim

An **entity** has a project identity: a person, document, place or institution.
An **attribute** describes a record within a declared scope. A **relation** joins
entities, such as a person participating in a document. An **observation** records
what a researcher inspected. An **assertion** says something about an entity and
identifies its evidential basis. An **event** models an occurrence with participants,
roles and time. These are different choices, not increasingly truthful containers.

For example, a letter is a document; sending it is an event; its addressed name
is an observation; identifying the addressee is an assertion. A letter may survive
without proof that it was delivered. A sender–recipient edge therefore need not
mean successful communication. Keeping an event table makes such distinctions
possible, though it also demands decisions about what counts as one event.

A primary key identifies a row; a foreign key points to another row. Names make
poor keys because spelling, language and identification change. A many-to-many
relation needs a **junction table**: `participation(document_id, person_id, role)`
allows many people in one document and one person in many documents. A role can
carry its own evidence. A group portrait is not a single unidentified person,
and an institution should not be silently stored as a person to simplify a join.

## Worked example: one dossier, three models

The [contested-models companion](../../assets/downloads/contested-models-v1.zip)
contains a deliberately **synthetic** longitudinal dossier. Its Ana Kovač / Anna
Kovatsch (`SYN-A`) is fictional, not a person identified in the newspaper. The
archival-friction packet, built around an authentic newspaper issue, remains
unchanged; the companion tests difficulties that one issue cannot itself
document. Read the bilingual dossier before its
tables. Source-readable test records are essential: otherwise validating a query
against another generated table merely repeats the same assumptions.

In invented document D1, an administrative list uses Anna Kovatsch and classifies
A as a servant. In D2, a Slovene letter signed Ana Kovač, she calls herself a
seamstress and claims to read German. A later association note describes an
independent craft worker; a 1925 application records German use. Her stipulated
fixed residence changes district when a synthetic boundary moves. These are
test conditions, not reconstructed Slovenian administrative history.

### Model 1: the convenient flat spreadsheet

| Person | Name | Status | Language | District |
| --- | --- | --- | --- | --- |
| SYN-A | Ana Kovač | seamstress | Slovene | West |

This is a clean display row for a narrowly declared purpose, but a dangerous
master record. It hides the earlier name form, the administrative category, the
German application and the period of district membership. Replacing each cell
with comma-separated values restores some wording without restoring the relations:
which language was used when, and who assigned which status?

The flat model enables quick sorting and a readable handout. It obscures change
and makes source-level disagreement expensive: the analyst must reread notes
for every count. A table is not inadequate because it is a spreadsheet; it is
inadequate when its row definition cannot express the research question.

### Model 2: normalized entities and relationships

Separate people, names, places, documents and participation. Store a name variant
once per attestation or naming context and link it to its person and source.
This removes repeated person columns and supports finding every document linked
to A. A normalized design can also be temporal: normalization does not prohibit
dates or conflicting statements. The limitation here is a deliberately simple
entity/relationship design that still treats relationships as unqualified facts.

```text
person 1 -- many name_attestation many -- 1 document
person 1 -- many participation    many -- 1 document
person 1 -- many residence        many -- 1 place
```

This representation helps maintain identifiers and avoid inconsistent updates.
It does not, by itself, distinguish an editor's identification from a source's
self-description. Adding provenance only to a whole document is insufficient
when two claims in that document receive different editorial assessments.

### Model 3: assertions and events

The executable schema separates `entity`, `source` and `assertion`. Each assertion
has a subject, predicate, text value or entity object, context, historical interval,
interval kind, record timestamp, source wording, its declared relation to the
source (`exact`, `translation` or `summary`) and confidence. The exact
source inventory links D1–D6, N1, N2, BORDER and NAMES to anchored blocks in the
readable dossier. The separate participation table supplies document roles for
later event-oriented graphs.

```text
entity 1 -- many assertion many -- 1 source
entity 1 -- many assertion.object_id       (entity-valued claims)
assertion 1 -- zero-or-one assertion.supersedes  (editorial revision)
```

| Model | Enables | Obscures or makes expensive |
| --- | --- | --- |
| Flat display | Readable snapshot; simple sorting | Temporal and source-specific joins |
| Normalized entity/relationship | Reusable identities; many-to-many queries | Disagreement if relations remain unqualified |
| Qualified assertion/event | Date-specific evidence and editorial snapshots | More joins; interpretation and vocabulary maintenance |

The third model preserves more distinctions, but loses the document's layout,
tone and sequence unless linked back to facsimiles and prose. Its generic predicate
column also makes some type rules harder to enforce than separate, specialized
tables would. Choose that cost knowingly; an assertion table is not a universal
substitute for careful domain modelling.

## Names, status and language are contextual relations

Keep a **multilingual name variant** with its source form, language when known,
script, context and date of attestation. An administrative spelling need not
replace a signature. A preferred display name is an editorial policy for an
interface or edition, not a timeless property of the person. Preserve search
normalization separately: removing diacritics may find candidates but cannot
authorize a merge or silently rewrite a quotation.

Social, legal and institutional status require different predicates or a declared
vocabulary. Occupation, citizenship, membership and an institution's eligibility
category are not interchangeable. In the dossier, “servant” and “seamstress”
overlap in 1910. This may be simultaneous employment, self-presentation or a
difference between classification systems. The database reports the difference;
it cannot adjudicate it. “Certain” means the synthetic document clearly asserts
the label, not that the label exhaustively describes its subject.

Likewise separate **language knowledge**, **language use** and **language assigned
by an institution**. A German category in a register, a Slovene letter and a claim
to read German can coexist. None establishes mother tongue, national identity
or exclusive proficiency. An application may have been translated or written by
an intermediary; document language alone need not establish personal authorship.
The dossier stipulates use to test the distinction, whereas a real project would
need evidence about the production of each document.

Role vocabularies also change. “Member”, “deputy” or “independent worker” may have
different admission rules across periods and institutions. Retain source wording
and version the mapping to analytical categories. A crosswalk can mark partial
equivalence or no equivalent. Do not force every historical label into the nearest
modern occupation just to produce a complete bar chart.

## Historical time and the time of recording

**Valid time** concerns the period a claim describes. **Record/transaction time**
concerns when it entered or changed in the database. A modern correction to a
1910 name changes the editorial record, not the person's historical name on
the correction date. This introductory distinction follows the temporal-database
tradition described by [Snodgrass and Ahn 1986](https://doi.org/10.1109/MC.1986.1663327).

The companion uses half-open intervals `[start,end)`: 1910 is represented by
`1910-01-01` through `1911-01-01`, excluding the latter. This avoids counting
the boundary day in two adjacent periods. Its ISO dates are Gregorian teaching
conventions. Real projects must record calendars, conversion rules and original
date expressions rather than assuming every source used the same calendar.

An **event window** is not a duration. “Sometime in February” means one event
within a range; “employed throughout February” describes a state over that range.
Selecting a day inside the first interval finds a possibly relevant event, not
proof it occurred that day. Approximate expressions need a declared rule and
retained wording. Unknown endpoints should not be replaced by fabricated early
or late dates. The executable fixture deliberately uses bounded intervals;
a production schema needs explicit handling for open, unknown and contested bounds.

For editorial change, insert a new assertion linked by `supersedes`. The sample
retains both the mistaken Ana Kovać and its corrected transcription Ana Kovač.
The teaching schema permits this only when source, subject, predicate, context,
valid interval and interval kind are identical; it also prevents two rows from
claiming to be the direct successor of one assertion. That narrow rule models a
replacement of the same editorial claim, not a change in the historical period.
By contrast, the occupational disagreement is not a correction and neither source
supersedes the other. An append-only ledger supports reconstruction of earlier
views, but timestamps must be controlled by the application to be trustworthy;
a manually entered timestamp is not an independently secured transaction audit.

## Querying evidence at a specified date

SQL makes selection rules explicit. The saved `queries/at-date.sql` accepts a
subject, historical date and editorial snapshot. Its central condition is:

```sql
a.valid_start <= :as_of AND :as_of < a.valid_end
AND a.recorded_at <= :known_at
```

It also excludes assertions superseded by that editorial snapshot. Merely reading
the current view would be wrong for a question about what the database said last
week. Python supplies parameters; do not construct SQL by concatenating an
untrusted name into a query. Save the query and input version alongside the result.

The companion yields thirteen assertion rows, twelve in the current view and
one candidate status-conflict pair, `SYN-A04` / `SYN-A05`. The earlier 1910
editorial snapshot shows Ana Kovać; the corrected snapshot shows Ana Kovač.
Both still show the two occupational descriptions. The 1925 query reports the
later status and German-use event, not the 1910 letter as a lifelong language label.

Counting requires equally explicit units. Joining one person to three name
attestations and two roles can produce six rows. `COUNT(*)` then counts join
combinations, not six people. Inspect the joined rows before choosing
`COUNT(DISTINCT person_id)`. Use a left join to retain entities without evidence
of a selected relation, and distinguish zero observations from an observed zero.

## Boundaries, hierarchies and entity resolution

Store territorial membership as a relation between a place and an administrative
unit, qualified by date and source. In the synthetic exercise, a fixed residence
at x=550 belongs east of a boundary at x=500, then west of a boundary at x=600.
That is a jurisdictional change without migration. The real Ljubljana context
also crosses the collapse of Austria-Hungary in 1918; the companion's invented
district lines are not evidence for that historical transition.
[City of Ljubljana history](https://www.ljubljana.si/sl/mestna-obcina/o-ljubljani/zgodovina-ljubljane/nemirno-20-stoletje).

Administrative containment may be hierarchical: parish within district within
province. A recursive query can follow parent relations, but each link must be
valid for the queried period. A present-day hierarchy is not a shortcut to a
historical one. Check cycles and multiple parents explicitly; overlapping civil
and ecclesiastical jurisdictions may be meaningful, not errors to delete.
[SQLite recursive queries](https://www.sqlite.org/lang_with.html).

**Entity resolution** decides which records refer to the same entity. Retain
candidate links, evidence and decisions rather than merging on a similar name.
Test a proposed merge by inspecting dates, places, roles and source independence.
A false merge creates connections between two biographies and contaminates both
maps and networks. In the archival-friction packet's reference layer, the
rejected Meker/Meeker match is
a useful counterexample to automatic spelling-based identity.

## Validation, sensitivity and export loss

Normalization reduces update anomalies; deliberate denormalization can produce
a documented analytical snapshot. Do it through a saved query with a declared
date, selection rule and input revision. Keep the normalized or assertion-level
source authoritative. Otherwise an edited export and the database gradually
become competing, undocumented editions.

Constraints catch duplicate keys, missing references and reversed intervals.
Enable SQLite foreign keys on every connection before importing. Check that the
setting actually took effect, then run integrity and foreign-key checks. None
verifies a caption's claim or the appropriateness of a category.
[SQLite foreign-key documentation](https://www.sqlite.org/foreignkeys.html).

For sensitivity, compare all overlapping status assertions with a policy that
selects only the municipal register. On 1910-06-15, the first returns two labels;
the second returns one. The person count remains one. A resulting occupational
distribution changes because the evidence policy changed, not because a worker
changed occupation. Publish both counts and the excluded assertion ID. Repeat
the boundary query immediately before and on 1920-01-01 to check interval edges.

A flat CSV cannot enforce foreign keys, preserve database views or carry all
many-to-many relationships in one person row without duplication or aggregation.
Export linked tables with stable IDs, a dictionary and saved queries; include
source wording and editorial timestamps where relevant. Distinguish blank, unknown,
not applicable and withheld values explicitly. Test reimport on a small sample.
An accessible human-readable table is an analytical product, not a lossless backup.

## Hybrid modelling

One representation need not carry everything. Relational tables can hold entities
and queryable assertions; TEI/XML can preserve textual variation and editorial
structure; GeoPackage can hold dated geometries; a graph can support exploratory
relations. Facsimiles and diplomatic transcription retain source evidence, while
prose can explain distinctions that should resist controlled fields. Shared IDs
and versioned links connect these representations. The guiding question is:
which distinctions must be queryable, which must remain recoverable, and which
should resist formalization? See the [GIS](gis-spatial-humanities.md) and
[networks](networks-visualization.md) chapters for the same dossier's transformations.

## Practice

Use the paired [SQLite assertion workflow](../workflows/data/model-changing-names-statuses-and-boundaries-in-sqlite.md).
Download the companion, read its rights audit, and run `python run.py --output output`
inside the extracted directory. Use a new output name on a second run. Compare
`assertions-1910_early.csv`, `assertions-1910_corrected.csv` and
`status-conflicts.csv` against the dossier. Explain the spelling correction and
the surviving disagreement separately.

Submit a schema sketch, both status-selection counts, a source-linked result
table and a short account of export loss. As a manual check, trace every result
for A to its document or note; as a failure test, attempt an orphan foreign key
in a disposable copy. Do not edit the preserved source or publish invented
identities as historical findings. Human methodological and Slovene-language
review remain necessary even when every automated check passes.

## Reflection

- Which apparent contradictions arise from different contexts rather than false statements?
- What does your query mean for an event with an uncertain date?
- Which person disappears when you replace a left join with an inner join?
- Could a reader reconstruct the evidence policy from your exported table alone?

## Summary

A relational database makes selected distinctions queryable; it does not turn
assertions into truth. Stable identifiers, contextual names, qualified relations,
historical intervals and editorial history help preserve change and disagreement.
The strongest database argument includes its query, its source trail, a sensitivity
comparison and an explicit account of what remains outside the schema.

## Further reading

- Codd, E. F. 1970. “A Relational Model of Data for Large Shared Data Banks.” *Communications of the ACM* 13(6): 377–387. [DOI](https://doi.org/10.1145/362384.362685). Relational organization and consistency.
- Bradley, John, and Harold Short. 2005. “Texts into Databases: The Evolving Field of New-style Prosopography.” *Literary and Linguistic Computing* 20(Suppl): 3–24. [DOI](https://doi.org/10.1093/llc/fqi022). Source-oriented historical assertions.
- Snodgrass, Richard, and Ilsoo Ahn. 1986. “Temporal Databases.” *Computer* 19(9): 35–42. [DOI](https://doi.org/10.1109/MC.1986.1663327). Distinguishing temporal dimensions.
- SQLite. [Foreign keys](https://www.sqlite.org/foreignkeys.html), [date functions](https://www.sqlite.org/lang_datefunc.html), and [WITH/recursive queries](https://www.sqlite.org/lang_with.html). Operational references checked 3 September 2026; the sample implements its own bounded interval policy.
