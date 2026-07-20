---
title: "Web text harvesting"
description: "A small Python workflow for extracting readable text from web pages into corpus-ready files."
tags: [projects, corpus, scraping, web, python]
---

# Web text harvesting

<div class="answer-meta" markdown>
<span>corpus building</span>
<span>Python</span>
<span>web text</span>
</div>

## What this project does

This example shows how a small Python script can collect readable text from web pages. For each URL, the workflow downloads HTML, removes obvious boilerplate, detects the main language, wraps the result in a minimal corpus-like structure, and saves one text file per URL.

[:octicons-mark-github-16: Open the source repository](https://github.com/damjan-popic/text_harvester)

## Use this when

- you need a small web corpus for teaching, exploration, or a pilot study.
- you want a transparent introduction to content extraction heuristics.
- you need to connect scraping, cleaning, language detection, and export in one inspectable script.
- you want a lightweight alternative to a full crawler.

## What to inspect in the code

- `textharvester.py` — the main script and importable functions.
- `harvest()` — returns the extracted result for one URL.
- `save_result_as_txt()` — writes the extracted text to disk.
- HTML-cleaning and content-selection functions — useful for showing why boilerplate removal is heuristic.
- language-detection logic — useful for multilingual-page diagnostics.

## Minimal run path

```bash
pip install requests beautifulsoup4 lxml langdetect
python textharvester.py https://example.org/article
```

Expected output:

```text
harvested_texts/example_org_article.txt
```

The file contains a minimal `<corpus><text ...>` wrapper with URL, title, download time, primary language, language distribution, and extracted paragraphs.

## Relevant handbook workflows

- [How do I scrape a single-topic website into a mini corpus?](../workflows/corpora/scrape-a-single-topic-website-into-a-mini-corpus.md)
- [How do I filter a corpus by language with fastText?](../workflows/corpora/filter-a-corpus-by-language-with-fasttext.md)
- [How do I package a corpus with FAIR metadata?](../workflows/publishing/package-a-corpus-with-fair-metadata.md)
- [How do I write a README for a humanities dataset?](../workflows/publishing/write-a-readme-for-a-humanities-dataset.md)

## Practice use

Ask users to harvest three pages from the same website. They should compare the extracted text with the original pages and mark what was kept correctly, what boilerplate remained, what useful content was removed, and whether language detection matches the main article text.

## Limits and cautions

- Content extraction is heuristic and will fail on some layouts.
- Scraping should respect terms of use, access limits, robots policies, and copyright.
- A small script is not a preservation system; keep source URLs, timestamps, and collection-scope notes.
- Do not treat harvested text as neutral: menus, captions, comments, ads, and related links can slip into the corpus.
