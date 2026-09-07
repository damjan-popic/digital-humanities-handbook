---
title: "Networks and visualization"
description: "Constructing, comparing and auditing source-qualified relations without confusing graph structure with historical importance."
tags: [networks, visualization, graph, centrality, uncertainty]
status: draft
---

# Networks and visualization

## Learning outcomes

After this chapter, you should be able to:

- distinguish documented participation, source assertions, inference and co-occurrence;
- define directed, weighted, signed, multiplex, bipartite and temporal networks;
- preserve identity decisions, source evidence, confidence and dates for edges;
- compare a person–document network with projected and correspondence networks;
- interpret centrality, components and communities under explicit construction rules;
- test thresholds, projection choices and missing records, and publish non-visual results.

## Before you begin

Four individually labelled people appear in one newspaper issue. Does that make them a connected political circle? Under a same-issue rule, they generate six undirected pairs. Under a correspondence rule, the same observations establish no letters between them. Neither result says that the people never interacted. The difference concerns what the selected records support.

The authentic archival-friction packet supplies this starting problem. The [companion packet](../../assets/downloads/contested-models-v1.zip) preserves the original observation identifiers and source locators, then adds a clearly synthetic six-person dossier to make controlled comparisons possible. No invented letter or biography is attributed to a real newspaper subject. Before calculating anything, write one sentence defining the relation you want to investigate and another defining what your records actually observe.

## The argument: an edge is an accountable claim

A graph consists of nodes and edges, but historical relations arrive through sources and editorial work. A surviving letter might document an act of writing; its address might assert a recipient; the researcher may infer reception. These are different claims. A catalogue entry is an observation about a described object, not direct observation of a historical friendship.

Distinguish four levels. An **observed record relation** links a named participant to an inspected document. An **asserted relation** reports what that document says. An **inferred relation** depends on an explicit interpretive rule. A **co-occurrence relation** joins entities sharing a chosen container, without asserting interaction. Even an inspected document can misidentify someone or report an event inaccurately.

A useful edge record therefore includes endpoints, relation type, direction, evidence identifier, source locator, date interval, confidence and construction rule. Keep the source wording or a recoverable passage. A plotted line should lead back through these decisions. [Models, evidence and interpretation](models-evidence-interpretation.md) provides the broader framework for separating data construction from historical explanation.

## Choosing nodes and resolving identity

Node identity determines the graph before any metric runs. Is a node a person, a signature, an institutional office, a collective character or an unresolved mention? Combining these without explanation makes the graph's population unstable. A node labelled “the editor” may represent successive officeholders, not one enduring person.

The dossier distinguishes person `SYN-A` from recorded name forms Anna Kovatsch and Ana Kovač. Their shared identity is stipulated for this synthetic exercise. In real work it would require evidence, not just spelling similarity. A false merge can give one node the neighbours of two people and create a fictitious bridge. A false split can hide continuity and make an actor appear peripheral.

Maintain an identity-decision table with evidence and alternatives. Test a consequential uncertain merge separately, preserving both versions. Do not exclude unresolved mentions merely to tidy the visualization: report how many remain and why they cannot safely enter person-level analysis. Stable identifiers help manage decisions; they do not prove identity.

## What different network types mean

A **directed** edge distinguishes sender from recipient. An **undirected** edge can represent shared membership without assigning an initiator. A **weighted** edge carries a specified quantity, such as distinct documents, rather than a vague strength score. A **signed** edge distinguishes positive and negative relations under an independently justified coding scheme; criticism is not automatically the negative of friendship.

A **multiplex** network retains separate relation layers, for example correspondence, employment and co-occurrence. Collapsing them makes a letter equivalent to shared employment unless a defensible combination rule is supplied. A **bipartite** network connects two node types, such as people and documents, with no within-type edges. A **temporal** network retains events or intervals so that paths can respect chronology.

These properties can coexist. A correspondence layer may be directed, weighted and temporal. Before selecting software, state the unit of observation and whether repeated letters are separate events or aggregated weights. Preserve the event table even when an aggregate graph is useful for exploration.

## Dates, confidence and relation semantics

A letter's date is an event time, not the duration of a social tie. The dossier's `SYN-D6` is dated only to February 1925, represented as the possible event window from 1 February inclusive to 1 March exclusive. This does not mean continuous communication throughout the month. A dated membership assertion can instead describe a duration, depending on its source wording.

Aggregating 1910 and 1925 can create paths whose edges never coexisted. A temporal path also needs an ordering rule: a message cannot travel through an earlier event after a later one. Unknown dates complicate possible and certain reachability differently. Do not quietly assign undated material to the midpoint of your study period.

Confidence qualifies a particular assertion. In the example, the recipient of `SYN-D6` is probable; the existence of the synthetic document is not uncertain within the exercise. Keeping those distinctions allows a “certain recipients only” comparison without deleting the underlying record. Confidence categories are review conventions, not automatically calibrated probabilities.

## One dossier, three representations

The controlled dossier contains six people and six source records. Separate status notes used in the database chapter are not included in this network selection. Selection itself is documented, not an invisible preprocessing decision.

| Document | Participants | Source genre and relation information |
|---|---|---|
| `SYN-D1` | A, B, C | municipal list; no interaction asserted |
| `SYN-D2` | A, B | letter, A → B |
| `SYN-D3` | C, D, E | association list |
| `SYN-D4` | D, E | letter, D → E |
| `SYN-D5` | A, B, C, D, E, F | press list; no interaction asserted |
| `SYN-D6` | E, F | letter, E → F; probable recipient |

All labels abbreviate identifiers beginning `SYN-`. Build the bipartite graph directly from the 18 person–document participation rows. Project a person graph by linking people who share a document. Finally, construct a correspondence graph only from explicit sender and recipient roles in letter records. All three use the same selected records; their edges answer different questions.

The original newspaper remains a separate evidence check: its four individually labelled people yield six same-issue pairs, but these selected observations do not establish correspondence. Do not add synthetic letters to improve the authentic graph's apparent completeness.

## Projection changes the unit of evidence

Projection replaces shared document participation with person–person edges. A document containing k people contributes k(k−1)/2 possible pairs. A six-person list therefore contributes fifteen pairs, although it remains one source record. A three-person list contributes three. This is projection inflation, not fifteen independent testimonies of association.

A document containing only one selected person remains a valid person–document
edge in the bipartite graph but contributes no pair to a one-mode projection.
Record it in the projection audit instead of dropping it silently. Because it
forms no pair, it also creates no `1/(k−1)` fractional term and no division by zero.

The discussion of two-mode networks by [Latapy, Magnien and Del Vecchio](https://doi.org/10.1016/j.socnet.2007.04.006) provides a formal basis for retaining the bipartite structure. In our example, `SYN-D5` alone connects every pair. The resulting complete graph conceals whether a pair shares one list or several distinct records.

Keep a support table with one row per pair and supporting document. Deduplicate repeated mentions within the same document before counting document support. Also inspect whether two documents copy a common source: distinct identifiers do not guarantee evidential independence. A projected edge is a derived summary with provenance, not a new archival fact.

## Thresholds and fractional weighting

Let an edge weight equal the number of distinct shared documents. At threshold 1, retain any supported pair; at threshold 2, require two documents; at threshold 3, require three. These thresholds do not mean weak, reliable and certain friendship. They mean increasingly repeated co-documentation under this rule.

A second projection gives each shared document a contribution of 1/(k−1), where k is its number of participants. This reduces a large list's contribution to each pair: `SYN-D5` contributes 0.2 rather than 1. The normalization is an explicit analytical choice, not a universal correction. Other weighting conventions answer other questions.

The packet retains all six people, including isolates, in every person-level comparison. Its metrics treat surviving edges as unit-length connections; document weights select edges but are not used as path lengths. Do not interpret a large document count as a large distance. If you convert strength to distance, justify that transformation and test its effect separately.

## Worked comparison: structure and degree

| Construction rule | Edges | Components | Highest person degree |
|---|---:|---:|---|
| Bipartite participation | 18 | 1 | E: 4 documents |
| Projection, threshold 1 | 15 | 1 | all six: 5 people |
| Projection, threshold 2 | 7 | 1 | C: 4 people |
| Projection, threshold 3 | 2 | 4 | A, B, D, E: 1 person |
| Fractional projection, weight ≥1 | 3 | 3 | E: 2 people |
| Directed correspondence | 3 | 3 weak components | E: 2 incident edges |

A bipartite degree counts documents, not people; compare its rankings cautiously with a projected degree. At threshold 1, the press list makes everybody equally connected. At threshold 2, the remaining pairs are AB, AC, BC, CD, CE, DE and EF. C now connects the ABC and CDE portions. At threshold 3, only AB and DE remain, while C and F are isolated.

The correspondence graph contains A→B, D→E and E→F. Its weak components ignore direction when identifying connected sets; directed reachability remains different. E's total degree is two, but its in-degree and out-degree are each one. A highest degree claim must name both the graph and the meaning of degree.

## Betweenness and closeness require assumptions

**Betweenness** allocates credit to nodes on shortest paths between other nodes. The packet reports raw, unnormalized values and divides undirected pair counts by two. In the threshold-2 projection C has betweenness 6 and E has 4; everyone else has zero. In the complete threshold-1 graph every value is zero because each pair already has a direct edge.

In the directed correspondence graph E has betweenness 1, from D to F through E. This is a graph-theoretic path across records, not proof that E transmitted a message, brokered influence or knew every sender. Temporal and contextual evidence would be needed for those interpretations.

Ordinary **closeness** uses distances to other nodes and needs a convention for disconnected graphs. The packet instead reports outgoing harmonic closeness: sum reciprocal finite distances and divide by N−1; unreachable nodes contribute zero. At threshold 2 C scores 0.9 and E 0.8. In correspondence D scores 0.3, E 0.2 and B zero. A reachable-node convention or reversed direction would answer another question.

These measures summarize a model. Before calling someone influential, explain why shortest paths or direct neighbours represent a plausible historical process and inspect the supporting passages.

## Components and communities are not factions

A component records reachability under the chosen direction convention. It is not necessarily a social group. **Community detection** seeks a partition according to a chosen objective; results depend on that objective, resolution and implementation. Layout clusters are yet another object.

For six people, the packet evaluates all 203 set partitions using unweighted, undirected modularity at resolution 1 and retains every maximizing tie. This small exhaustive comparison avoids presenting one arbitrary algorithm run as definitive. It is not a scalable recommendation for large datasets. For correspondence, the community calculation explicitly discards direction; centrality calculations retain it.

At threshold 1 the unique optimum places all six together, with modularity 0. At threshold 2 the unique optimum is ABC | DEF, with modularity approximately 0.204082. At threshold 3 there are ten tied optimal partitions: isolated nodes can move without changing the score. The correspondence structure has three tied optima.

The [resolution-limit study by Fortunato and Barthélemy](https://doi.org/10.1073/pnas.0605965104) is a further reason not to equate modularity groups with historical communities. Validate proposed factions against independent evidence and report equally good alternatives. A mathematical optimum is not a source verdict.

## Missing archives and ascertainment bias

Missing data are often structured. Institutions preserve some correspondence and destroy other records; prominent individuals receive more cataloguing; language tools recognize some names better than others. **Ascertainment bias** concerns how the procedure makes particular people and relations observable. Random deletion alone cannot represent every archival mechanism.

[Borgatti, Carley and Krackhardt](https://doi.org/10.1016/j.socnet.2005.05.001) study centrality robustness under imperfect data. Treat such research as motivation to specify an error process, not as a guarantee that your incomplete archive preserves rankings.

In the packet, withholding `SYN-D6` before applying threshold 2 removes EF and isolates F. E's betweenness falls from 4 to 0, while C's falls from 6 to 4. An apparently distinctive intermediary role for E depends on one selected record. Removing probable recipient assertions also reduces correspondence from three edges to two.

Report survival, selection, extraction and identity-resolution losses separately. A missing edge means “not observed under this construction and coverage,” not “these people had no relationship.”

## Robustness as a research result

A sensitivity analysis varies a defensible assumption while holding other choices explicit. Here, removing the large press list at threshold 1 produces the same seven edges as the original threshold-2 projection. Fractional weighting at weight ≥1 instead retains AB, DE and EF. Different corrections to projection inflation need not select the same graph.

Record which conclusions survive. “C has the highest degree in the threshold-2 shared-document projection” is reproducible. “C was the most important person” is unsupported. “E's intermediary position is sensitive to `SYN-D6`” accurately reports the experiment. Do not average incompatible edge semantics into a supposedly more robust social network.

The [comparison workflow](../workflows/networks/compare-bipartite-and-projected-networks.md) produces the tables, and the [claim-audit workflow](../workflows/networks/audit-a-network-claim-against-source-records.md) returns selected edges to the dossier. Include inconvenient counterexamples, not just the central node that fits your initial interpretation.

## Visualization, accessibility and ethics

Force-directed layouts arrange nodes according to an optimization procedure, often with arbitrary orientation and variable initialization. Distance on such a plot is not geographic distance, elapsed time or historical affinity unless explicitly encoded. Changing a random seed can move a cluster without changing any edge.

State node-size, edge-width and colour rules. Size by area rather than an unexplained radius convention, distinguish isolates and explain filtering. Do not rely on colour alone to communicate relation types or confidence: provide labels, line patterns and a textual legend. Avoid using a striking cluster as evidence before inspecting its table.

Every exercise here supports a non-visual submission: node metrics, component membership, edge provenance and a prose comparison. A readable table is essential for exact values and screen-reader access; an image description should summarize findings and exceptions. Sensitive relationships can also harm living people or communities. Consider consent, inference risks and access restrictions before publishing names or speculative ties, even when individual source records are public.

## Hybrid modelling

A relational database or event table is often the better primary representation when relations have multiple participants, changing roles, incompatible sources or uncertain dates. Generate a graph as a documented view. Retain TEI/XML for textual variation, GeoPackage for dated geometries, facsimiles and diplomatic transcription for evidence, and prose for distinctions that should resist categorical encoding.

Ask which distinctions must be queryable, which must remain recoverable and which should resist formalization. Stable identifiers can connect these representations without pretending that every assertion is a timeless binary relation.

## Practice

Unpack the companion archive and run:

```bash
python run.py --output output-first
```

Compare `bipartite-metrics.csv`, `projection_t1-metrics.csv`, `projection_t2-metrics.csv` and `correspondence-metrics.csv`. Use `projection-evidence.csv` to explain AB and CE, then inspect the probable recipient in `correspondence-edges.csv`. Check all alternative constructions in `results.json`.

Submit the source-selection rule, a three-model comparison, a threshold table, one missing-record experiment and a corrected 150-word claim. Preserve isolates and give a source locator for every audited edge. A graph drawing is optional; the source-linked tables and interpretation are required.

## Reflection

- What did the source assert, and what did your edge-construction rule add?
- Which identity decision could create a false bridge?
- Which ranking or community changes under another plausible rule?
- What does your graph omit that the event table or source passage preserves?

## Summary

Networks formalize selected relations, not the social world in its entirety. Node identity, source selection, projection, thresholds, dates and missingness determine what a metric summarizes. Centrality does not establish generic importance, communities are not automatically factions, and layout is not evidence. Preserve bipartite participation and source-qualified events, test alternatives, and write conclusions that name the construction rule.

## Further reading

- Latapy, Matthieu, Clémence Magnien and Nathalie Del Vecchio. 2008. [“Basic notions for the analysis of large two-mode networks.”](https://doi.org/10.1016/j.socnet.2007.04.006) *Social Networks* 30(1): 31–48.
- Borgatti, Stephen P., Kathleen M. Carley and David Krackhardt. 2006. [“On the robustness of centrality measures under conditions of imperfect data.”](https://doi.org/10.1016/j.socnet.2005.05.001) *Social Networks* 28(2): 124–136.
- Fortunato, Santo, and Marc Barthélemy. 2007. [“Resolution limit in community detection.”](https://doi.org/10.1073/pnas.0605965104) *Proceedings of the National Academy of Sciences* 104(1): 36–41.
- Drucker, Johanna. 2011. [“Humanities Approaches to Graphical Display.”](https://digitalhumanities.org/dhq/vol/5/1/000091/000091.html) *Digital Humanities Quarterly* 5(1). Read alongside the chapter's distinction between display and evidential claims.
