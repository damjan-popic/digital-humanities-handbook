---
title: "Case studies"
description: "Functional case studies that connect handbook workflows to public source repositories."
---

# Case studies

These pages describe public repositories by **function**, not by repository nickname. The goal is to help readers move from a workflow to working code quickly: what the code does, which files to inspect, how to run a minimal example, what output to expect, and what limits matter.

<div class="search-panel" markdown>

<a class="big-search-button" href="#" data-search-launcher>🔎 <span><strong>Search case studies and workflows</strong> — try crawler, CLASSLA, NER, metadata, chatbot, Wikisource, or comma.</span></a>

</div>

## Catalogue

<div class="grid cards" markdown>

-   <span class="project-label">corpus building</span>  
    **Web text harvesting**  
    Extract readable web text into corpus-ready files.  
    [:octicons-arrow-right-24: View](text-harvester.md)

-   <span class="project-label">corpus annotation</span>  
    **Corpus conversion and CLASSLA annotation**  
    Convert TEI/VRT data and enrich CoNLL-U annotation layers.  
    [:octicons-arrow-right-24: View](corpus-augmenter.md)

-   <span class="project-label">large corpus</span>  
    **Slovene Wikisource corpus build pipeline**  
    Normalize metadata, annotate, and prepare a large Wikisource-derived corpus.  
    [:octicons-arrow-right-24: View](wikivir.md)

-   <span class="project-label">learner corpus</span>  
    **Learner-corpus lexical analysis**  
    Preserve metadata while reannotating and analysing Šolar-style corpus data.  
    [:octicons-arrow-right-24: View](korpus-solar-analysis.md)

-   <span class="project-label">dialogue analysis</span>  
    **Dialogue corpus tabulation and lexical-diversity analysis**  
    Turn dialogue exports into token, turn, speaker, and aggregate tables.  
    [:octicons-arrow-right-24: View](pracomul.md)

-   <span class="project-label">historical NLP</span>  
    **Medieval notarial NER workflow**  
    Combine rules, annotation, baselines, and model training for historical entity extraction.  
    [:octicons-arrow-right-24: View](medieval-ner.md)

-   <span class="project-label">DH publishing</span>  
    **Static knowledge graph, map, and corpus index**  
    Publish derived graph, map, and corpus-index data without a backend.  
    [:octicons-arrow-right-24: View](ladakh-relations.md)

-   <span class="project-label">crawler + chatbot</span>  
    **Website crawler and chatbot corpus builder**  
    Crawl an institutional website into documents and retrieval chunks.  
    [:octicons-arrow-right-24: View](fifi.md)

-   <span class="project-label">source-grounded AI</span>  
    **Source-grounded Slovenian language advisor**  
    Maintain a searchable source corpus and persistent Markdown wiki for language advice.  
    [:octicons-arrow-right-24: View](jezikovni-svetovalec.md)

-   <span class="project-label">writing tool</span>  
    **Slovenian comma-checking Word add-in**  
    Review comma placement with explicit local/remote service safety settings.  
    [:octicons-arrow-right-24: View](vejice-add-in.md)

-   <span class="project-label">transcript analysis</span>  
    **User/AI transcript analysis**  
    Compare user and assistant sections with token-level and summary-level outputs.  
    [:octicons-arrow-right-24: View](createai.md)

</div>

## Why some public repositories are not listed

A repository is included here only when its public README or visible file structure makes its function clear enough to describe responsibly. Repositories without a public description, minimal run path, or clear reusable workflow are better left out of the production-facing catalogue until they are documented.

## Reuse checklist

Before featuring or reusing a repository publicly, check:

- the README explains the purpose and the minimal command.
- dependencies are listed in `requirements.txt`, `pyproject.toml`, `package.json`, or similar.
- sample data is legal to publish.
- large or generated data is not accidentally committed.
- private credentials, tokens, PDFs, transcripts, or local paths are not exposed.
- expected outputs are named.
- failure modes are documented.
- license and citation expectations are clear.
