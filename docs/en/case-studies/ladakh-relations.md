---
title: "Static knowledge graph, map, and corpus index"
description: "A static DH site pattern for publishing derived entities, relations, places, and corpus references without a backend."
tags: [projects, knowledge-graph, mapping, cultural-heritage, static-site]
---

# Static knowledge graph, map, and corpus index

<div class="answer-meta" markdown>
<span>knowledge graph</span>
<span>map</span>
<span>static site</span>
</div>

## What this project does

This example shows a static-site and local-pipeline pattern for an interactive research graph. It supports graph nodes and edges, a map view, geocoding review, a corpus index, cleaning and annotation workflows, candidate relation discovery, and GitHub Pages deployment without a backend.

[:octicons-mark-github-16: Open the source repository](https://github.com/damjan-popic/ladakh-relations)

## Use this when

- you want to publish a DH graph and map without a database server.
- you need to separate local source processing from public derived data.
- you want to teach entity normalization, candidate links, and geocoding review.
- you need a case study for public/private boundaries in cultural heritage work.

## What to inspect in the code

- `index.html`, `app.js`, and `style.css` — static public interface.
- `data/` — derived public graph and map data.
- `scripts/rebuild_all.py` — rebuilds derived data.
- `scripts/normalize_texts.py` — normalizes local text input.
- `schema/` — data model and validation expectations.
- `docs/` — architecture, corpus, embeddings, and deployment notes.

## Minimal run path

```bash
python scripts/serve_local.py
```

Then open the local server address. For new texts, the public README describes this pattern:

```text
raw text → normalized corpus → rebuilt derived data → static site
```

## Relevant handbook workflows

- [How do I map places mentioned in a text?](../workflows/mapping/map-places-mentioned-in-a-text.md)
- [How do I build a simple cultural heritage map?](../workflows/mapping/build-a-simple-cultural-heritage-map.md)
- [How do I turn messy humanities notes into a reusable dataset?](../workflows/data-wrangling/turn-messy-humanities-notes-into-a-reusable-dataset.md)
- [How do I decide whether a digitised source should be public?](../workflows/ethics/decide-whether-a-digitised-source-should-be-public.md)

## Practice use

Ask users to design a small graph with people, places, sources, and uncertainty notes. Then have them decide which fields can be public and which should remain private or local.

## Limits and cautions

- Cultural heritage projects need source, community, and access review.
- Full transcriptions may be copyrighted or sensitive, so derived metadata may be safer to publish than full text.
- Candidate links are hypotheses, not established facts.
- Coordinates and place identities should be reviewed, especially for culturally sensitive locations.
