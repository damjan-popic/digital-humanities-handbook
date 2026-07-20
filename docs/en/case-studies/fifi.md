---
title: "Website crawler and chatbot corpus builder"
description: "A crawler and corpus-building pattern for turning institutional website content into documents and retrieval chunks."
tags: [projects, crawler, chatbot, RAG, metadata]
---

# Website crawler and chatbot corpus builder

<div class="answer-meta" markdown>
<span>crawler</span>
<span>RAG preparation</span>
<span>metadata</span>
</div>

## What this project does

This example shows how to crawl an institutional website and build a corpus suitable for retrieval and chatbot preparation. It outputs page/file records, smaller text chunks, downloaded files, optional HTML snapshots, and a crawl manifest with provenance metadata.

[:octicons-mark-github-16: Open the source repository](https://github.com/damjan-popic/fifi)

## Use this when

- you need to prepare website content for a retrieval-based chatbot.
- you want to show that chatbot data preparation starts with crawling, cleaning, chunking, and metadata.
- you need a practical example of document and chunk JSONL outputs.
- you want to discuss institutional websites, provenance, and freshness.

## What to inspect in the code

- `fifi/crawler.py` — crawl logic and corpus generation.
- `scripts/crawl_ff.py` — command-line entry point.
- `data/` — local crawl outputs kept out of Git.
- `documents.jsonl` — one record per HTML page or downloadable file after a crawl.
- `chunks.jsonl` — smaller retrieval-ready text chunks.
- `manifest.json` — crawl summary and provenance.

## Minimal run path

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/crawl_ff.py
```

For a classroom-scale exercise, crawl only a small allowlisted subset and inspect the produced `documents.jsonl` and `chunks.jsonl`.

## Relevant handbook workflows

- [How do I scrape a single-topic website into a mini corpus?](../workflows/corpora/scrape-a-single-topic-website-into-a-mini-corpus.md)
- [How do I audit AI output against source documents?](../workflows/ai/audit-ai-output-against-source-documents.md)
- [How do I package a corpus with FAIR metadata?](../workflows/publishing/package-a-corpus-with-fair-metadata.md)
- [How do I decide whether a digitised source should be public?](../workflows/ethics/decide-whether-a-digitised-source-should-be-public.md)

## Practice use

Ask users to design metadata for a retrieval chunk: source URL, canonical URL, title, heading path, language, crawl time, hash, and text span. Then discuss which fields are needed for citation and error correction.

## Limits and cautions

- Institutional websites change; a crawl is a dated snapshot.
- Respect robots policies, access limits, copyright, and server load.
- A chunk is not a document; retrieval answers must point back to sources.
- Do not crawl private, login-only, or sensitive pages unless explicit permission and data handling are in place.
