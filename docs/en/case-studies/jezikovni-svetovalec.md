---
title: "Source-grounded Slovenian language advisor"
description: "A rights-cautious architecture for answering language questions from local sources and a persistent Markdown wiki."
tags: [projects, RAG, language-advisor, Slovene, wiki]
---

# Source-grounded Slovenian language advisor

<div class="answer-meta" markdown>
<span>language advisor</span>
<span>source grounding</span>
<span>rights caution</span>
</div>

## What this project does

This example shows an architecture for answering Slovenian language questions from a local source corpus and maintaining a persistent LLM-supported wiki. It combines raw source layers, extracted corpus pages, a searchable index, context-building tools, agent instructions, and durable Markdown wiki pages.

[:octicons-mark-github-16: Open the source repository](https://github.com/damjan-popic/jezikovni-svetovalec)

## Use this when

- you want to design a source-grounded language-advice system.
- you need to separate source material from generated summaries.
- you want a concrete example of a persistent LLM-maintained Markdown wiki.
- you need a cautionary case for copyright, local corpora, and private/public boundaries.

## What to inspect in the code

- `wiki/` — durable summaries, rule pages, contradictions, glossary entries, and logged answers.
- `wiki/index.md` — content-oriented index.
- `wiki/log.md` — append-only maintenance log.
- `tools/` — corpus search, context packs, wiki search, linting, and logging.
- `data/index/search.sqlite` — full-text search index.
- `AGENTS.md` and `.agents/skills/` — operating schema for AI agents.

## Minimal run path

Treat this primarily as an architecture example. The public README explicitly frames the repository as course/private and source-dependent. For public reuse, copy the architecture and use sources that you have the right to redistribute or keep the source layer private.

## Relevant handbook workflows

- [How do I audit AI output against source documents?](../workflows/ai/audit-ai-output-against-source-documents.md)
- [How do I write a README for a humanities dataset?](../workflows/publishing/write-a-readme-for-a-humanities-dataset.md)
- [How do I decide whether a digitised source should be public?](../workflows/ethics/decide-whether-a-digitised-source-should-be-public.md)

## Practice use

Ask users to design a source-grounded answer workflow: retrieve source passages, write a draft, cite exact passages, log unresolved questions, and update a persistent wiki page only after verification.

## Limits and cautions

- The source corpus may contain copyrighted or course-provided material that is not redistributable.
- Generated summaries should not replace source checking.
- A language-advice system needs citation discipline and clear uncertainty handling.
- Public documentation can describe the architecture without publishing restricted source texts.
