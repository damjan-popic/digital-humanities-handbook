---
title: "How do I audit AI output against source documents?"
description: "Use AI-assisted output while checking every claim against source evidence."
category: "AI"
difficulty: "beginner"
time: "30–60 min"
tags: [AI, source criticism, evaluation, LLM]
---

# How do I audit AI output against source documents?

<div class="answer-meta" markdown>
<span>AI</span>
<span>beginner</span>
<span>30–60 min</span>
</div>

## What you are trying to do

You want to use AI-assisted output while still checking every claim against source evidence.

!!! quote "One-sentence version"
    Start with a tiny sample, keep provenance, and only scale up once the workflow survives testing.

## You need

- Source document
- AI-generated summary or extraction

## Tools

- [Any LLM interface](https://en.wikipedia.org/wiki/Large_language_model)
- [Spreadsheet](https://www.libreoffice.org/discover/calc/)

## Workflow

1. Ask AI for a specific output: summary, entities, dates, or metadata.
2. Create an audit table: claim, source line/page, verdict, correction.
3. Mark each item as correct, wrong, unsupported, vague, or missed.
4. Revise the prompt and rerun.
5. Write an error typology.

## Output

Audited AI output and error report.

## Check yourself

- Does every important claim have source evidence?
- Are hallucinations separated from reasonable inferences?
- Did the prompt improvement reduce errors?

## Common traps

- Letting fluent prose hide missing evidence.
- Only checking errors that are easy to spot.
- Forgetting omissions.

## Worked examples

- [website crawler and chatbot corpus builder](../../case-studies/fifi.md) shows how website content can be crawled and chunked with source metadata before retrieval.
- [source-grounded Slovenian language-advisor architecture](../../case-studies/jezikovni-svetovalec.md) shows a source-grounded language-advisor architecture with a persistent Markdown wiki and citation-first workflow.

## Practice task

Make groups compete to produce the most useful error taxonomy, not the most “AI-friendly” prompt.

## Useful extension

Turn the workflow into a small reusable checklist: input, command or tool action, output, quality check, and known failure mode.
