---
title: "Networks and visualization"
description: "How to construct, measure and display relationships without mistaking a graph for the social or cultural world itself."
tags: [networks, visualization, graph, centrality, uncertainty]
status: draft
---

# Networks and visualization

## Learning outcomes

After this chapter, you should be able to:

- define nodes, edges, direction, weight and bipartite networks;
- distinguish observed relationships from relationships inferred by a construction rule;
- interpret basic centrality and community measures cautiously;
- design a visualization that exposes scale, uncertainty and missing data;
- document the transformations from source records to a graph.

## Before you begin

Two people occur in the same newspaper article. Are they connected? Perhaps they collaborated, opposed one another, were merely listed, or appear in unrelated paragraphs. A network edge is not found automatically in the source. It is created by a rule whose meaning must be defended.

Node and edge rules are modelling choices that shape every metric and image. Use [Models, evidence and interpretation](models-evidence-interpretation.md) to keep construction, output and interpretation distinct, and [Infrastructures of digital humanities](critical-infrastructures.md) when source APIs or visualization platforms determine visibility and reuse.

## A network is a data model

A graph contains **nodes** and **edges**. Nodes may represent people, texts, places, institutions or concepts. Edges may represent correspondence, citation, kinship, co-authorship, travel, co-occurrence or another relationship.

Specify whether an edge is:

- directed or undirected;
- weighted or unweighted;
- dated or time-bounded;
- observed directly or inferred;
- positive, negative or typed;
- supported by one or several sources.

Different edge definitions create different networks. The definition belongs in the methods section and ideally in machine-readable data.

## One-mode and bipartite networks

A one-mode network links the same kind of node, such as person to person. A **bipartite** network links two kinds, such as people to organizations or characters to scenes.

Projects often project a bipartite network into a one-mode co-occurrence network: two characters are linked if they appear in the same scene. Projection loses information and can create dense edges around large scenes. Preserve the original bipartite data and state the projection and weighting rule.

## Centrality is question-dependent

Common measures include:

- **degree:** number of immediate connections;
- **weighted degree:** sum of edge weights;
- **betweenness:** how often a node lies on shortest paths;
- **closeness:** distance to other reachable nodes;
- **eigenvector/PageRank-style measures:** connection to already well-connected nodes.

No measure equals “importance” in general. Degree may indicate visibility, opportunity or simply better documentation. Betweenness depends strongly on the assumption that shortest paths model the process. Disconnected and very small networks require special care.

## Communities and clusters

Community-detection algorithms partition networks into groups with dense internal connections. Results depend on algorithm, resolution and random initialization. A community is not automatically a historical faction or literary theme.

Compare multiple resolutions, inspect boundary nodes and relate groups to independent metadata. Report when several plausible partitions exist. A visually tidy modular graph may be produced by the layout even when evidence is weak.

## Time and change

Aggregating decades of relationships into one graph can create connections that never coexisted. Build time slices, interval networks or event-based views when chronology matters.

Ask whether nodes can enter and leave, whether edge weights accumulate, and whether missing years reflect no activity or no surviving data. Animation can be attractive but hard to compare; small multiples or interactive filters often communicate change more clearly.

## Missing data and unequal visibility

Networks are especially sensitive to archival survival. A prolific correspondent may look peripheral because only one archive survives. Famous figures may have better cataloguing and entity resolution. Co-occurrence networks privilege long documents and common names.

Represent coverage and source counts. Consider sensitivity analyses: remove uncertain edges, use alternative thresholds or compare archives. Absence of an edge often means “not observed under this procedure,” not “no relationship existed.”

## Visualization as analytical design

A network plot needs more than colourful nodes. Decisions include layout, node size, edge opacity, labels, filtering and colour categories. Force-directed layouts optimize readability, not geographical or chronological truth; repeated runs can place nodes differently.

Good practice:

- label only when labels serve the question;
- explain every visual encoding;
- avoid scaling node area in a misleading way;
- show isolated nodes when exclusion would hide coverage;
- provide a table or searchable view for exact values;
- preserve accessibility in colour and contrast;
- include provenance and a downloadable edge list.

## Worked example: a literary character network

A defensible workflow might be:

1. Define character identity, aliases and collective characters.
2. Choose an edge rule: shared scene, direct address or reported interaction.
3. Segment the text and preserve passage references.
4. Build a bipartite character-scene table.
5. Project only if the research question requires a character-character graph.
6. Test alternative scene definitions and edge thresholds.
7. compare centrality with narrative point of view and amount of speech;
8. inspect apparently central and surprisingly peripheral characters in the text;
9. publish both the visualization and construction data.

The graph summarizes one relational aspect of the novel. It does not model character depth, thematic importance or reader experience unless those have been operationalized separately.

## Practice

Construct a small network from at least ten source records. Write the edge rule in one sentence, keep an evidence field for every edge, calculate degree, and create two visualizations with different thresholds. Explain which relationships disappear and why.

## Reflection

- What does an edge mean in source terms?
- Which nodes are visible because their records survive or are easier to recognize?
- Would a bipartite representation preserve distinctions hidden by projection?

## Summary

Networks are explicit models of relationships, not transparent pictures of society or literature. Node and edge definitions, projection, time, missing data and algorithms shape every result. Centrality is not generic importance, communities are not self-interpreting groups and layouts are not evidence. Traceable construction rules and source-linked edges make network analysis suitable for humanistic interpretation.
