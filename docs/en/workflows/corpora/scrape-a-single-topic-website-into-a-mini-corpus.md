---
title: "How do I scrape a single-topic website into a mini corpus?"
description: "You need a small focused corpus from one public website."
category: "Corpora"
difficulty: "intermediate"
time: "45–90 min"
tags: [web scraping, corpus building, BeautifulSoup, ethics]
---

# How do I scrape a single-topic website into a mini corpus?

<div class="answer-meta" markdown>
<span>Corpora</span>
<span>intermediate</span>
<span>45–90 min</span>
</div>

## What you are trying to do

You need a small focused corpus from one public website.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Seed URL list
- Scope rules: what to include and exclude

## Tools

- [requests](https://docs.python-requests.org)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [readability-lxml](https://github.com/buriy/python-readability)

## Workflow

1. Check site terms, robots.txt, and ethical constraints.
2. Create a small seed list.
3. Download slowly and politely.
4. Extract main text, not navigation or cookie banners.
5. Save each page with URL, date, and metadata.

## Output

Folder of clean `.txt` files plus metadata.

## Check yourself

- Can each text be traced back to a URL?
- Did you remove menus and boilerplate?
- Is the scope narrow enough to describe?

## Common traps

- Scraping too much too fast.
- Publishing copyrighted text without permission.
- Losing provenance.

## Worked examples

- [web text harvesting example](../../case-studies/text-harvester.md) shows a compact Python implementation for harvesting readable web text into corpus-ready files.
- [website crawler and chatbot corpus builder](../../case-studies/fifi.md) shows a larger crawler/chunking workflow for institutional website content and retrieval preparation.

## Practice task

Users scrape nothing at first: they design the collection policy and metadata sheet before any download.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
