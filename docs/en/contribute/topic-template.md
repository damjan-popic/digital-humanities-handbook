---
title: "Topic template"
description: "A comprehensive Markdown template for adding new handbook topics."
tags: [template, contribution, markdown]
---

# Topic template

Use this template when adding a new topic to the handbook. A topic is a **single practical answer** to a question that starts with **How do I ...?**

The finished page should help a reader complete one task, produce one visible output, and check whether the result can be trusted.

## Before you write

Choose a question that is:

- practical: it describes something a reader wants to do;
- narrow: it can be answered in one page;
- testable: the reader can check whether it worked;
- honest: it names limits, failure modes, data issues, and rights concerns;
- reusable: it documents inputs, outputs, and assumptions.

Good examples:

```text
How do I extract keywords from a small corpus?
How do I clean OCR errors in a historical text?
How do I map places mentioned in a novel?
How do I check whether an AI-generated answer invented sources?
How do I turn messy field notes into a reusable dataset?
```

Avoid vague topic labels:

```text
Voyant
AI
Corpus linguistics
My project
Translation tools
```

## File name and location

Place the file under the relevant category in `docs/workflows/`.

Example:

```text
docs/workflows/corpora/extract-keywords-from-a-small-corpus.md
```

Use lowercase letters, hyphens, and no spaces:

```text
extract-keywords-from-a-small-corpus.md
clean-ocr-errors-in-a-historical-text.md
map-places-mentioned-in-a-novel.md
```

## Copy-paste template

Copy everything below into a new `.md` file and replace the placeholder text.

```markdown
---
title: "How do I [complete one specific task]?"
description: "A one-sentence summary of the problem and expected result."
category: "corpora"
difficulty: "beginner"
time: "30–60 min"
tags: [corpus, keywords, beginner]
---

# How do I [complete one specific task]?

<div class="answer-meta" markdown>
<span>corpora</span>
<span>beginner</span>
<span>30–60 min</span>
</div>

## What you are trying to do

Explain the practical situation in two to five sentences.

Write for a reader who knows the general field but may not know this workflow. State the problem, the kind of source material involved, and the desired result.

Good pattern:

> Use this workflow when you have [input] and need to produce [output] for [purpose].

Avoid opening with tool history, theory, or long definitions. Put the task first.

## You need

List the minimum requirements.

- Source material: [texts, scans, spreadsheet, transcript, website, corpus, etc.]
- Access: [software, account, API key, command line, repository, institutional permission]
- Skills: [basic spreadsheet use, Python basics, XML basics, Git basics, none]
- Decisions: [language, date range, genre, source scope, metadata fields, privacy level]

If the workflow uses data that may be restricted, say so here.

## Tools

List the tools and link to official or stable sources.

- [Tool name](https://example.org) — one sentence about what it does in this workflow.
- [Alternative tool](https://example.org) — optional replacement.

Mention versions only when they matter.

## Input

Describe the input clearly enough that someone can prepare it.

Example:

```text
input/
├── text-001.txt
├── text-002.txt
└── metadata.csv
```

Required input fields:

| Field | Required? | Example | Notes |
|---|---:|---|---|
| `id` | yes | `text-001` | Stable identifier. |
| `title` | yes | `Interview 1` | Human-readable title. |
| `source_url` | no | `https://...` | Keep if available. |
| `date` | no | `2026-05-13` | Use ISO format if possible. |

Delete this table if the workflow does not use tabular data.

## Workflow

Write numbered steps. Each step should be an action, not an essay.

1. **Prepare a tiny test sample.**  
   Use two or three items first. Do not start with the full dataset.

2. **Run the first transformation.**  
   Explain exactly what to click, run, paste, or configure.

   ```bash
   example-command --input input/ --output output/
   ```

3. **Inspect the output manually.**  
   Open one or two output files and check whether the result looks plausible.

4. **Fix the obvious problems.**  
   Note what usually needs correction: encoding, dates, missing metadata, OCR noise, wrong language, broken links, bad segmentation, duplicated rows.

5. **Scale up.**  
   Only process the full dataset after the small sample works.

6. **Document the run.**  
   Record the date, tool version, input source, settings, and known problems.

## Output

Name the expected output and show its structure.

Example:

```text
output/
├── cleaned-texts/
├── metadata-clean.csv
├── report.md
└── known-problems.md
```

Explain what the reader should have at the end:

- a CSV table;
- a cleaned corpus;
- a map;
- an HTML page;
- an annotated file;
- a transcript;
- a report;
- a list of candidates for manual review.

## Check yourself

Give concrete checks. Do not write only “check the result”.

Use questions like these:

- Open three random outputs. Do they match the source?
- Are all source items represented exactly once?
- Are names, dates, and places preserved correctly?
- Did the tool introduce hallucinated, inferred, or normalized information?
- Are missing values marked consistently?
- Are uncertain cases marked as uncertain?
- Can another person reproduce the result from your instructions?

Add at least one pass/fail criterion.

Example:

> The workflow passes if every input file has one output file, no output is empty, and a manual check of five random examples finds no source-title mismatch.

## Common traps

List at least two realistic problems.

- **Trap:** The tool silently drops short texts.  
  **Fix:** Count input and output files before trusting the result.

- **Trap:** Metadata looks clean but mixes date formats.  
  **Fix:** Normalize dates to `YYYY-MM-DD` and keep an `uncertain_date` note.

- **Trap:** AI output sounds plausible but has no source support.  
  **Fix:** Require source references for every factual claim.

## Rights, ethics, and access

Include this section whenever relevant. For some topics, it may be the most important part.

Address:

- copyright and licensing;
- personal data;
- interviews and consent;
- sensitive cultural or community material;
- institutional access restrictions;
- web scraping limits;
- whether the output should be public, private, anonymized, or restricted.

If there are no special issues, write:

> No special rights or privacy issues beyond normal source citation were identified for the sample data used here.

## Worked example

Link to a real or toy example.

Options:

- a public GitHub repository;
- a small sample dataset;
- a screenshot;
- a notebook;
- a code-example page in this handbook.

Example:

> See also: `[web text harvesting example](../../case-studies/text-harvester.md)`, a small Python workflow for harvesting readable web text into corpus-ready files. If you place your page somewhere other than `docs/workflows/[category]/`, adjust the relative path.

## Practice task

Write a short exercise that lets another reader test the workflow.

Example:

> Take five short texts from the same source. Run the workflow, then manually inspect two outputs and write a five-sentence note about what the tool kept, removed, or distorted.

## Further reading

Add only sources that directly help with this task.

- [Source title](https://example.org) — why it is useful.
- [Tool documentation](https://example.org) — relevant section.

## Changelog

Optional, but useful for living pages.

| Date | Change |
|---|---|
| YYYY-MM-DD | First version. |
```

## Required frontmatter values

Use these fields at the top of every answer page:

| Field | What it means | Example |
|---|---|---|
| `title` | Question-style page title. | `"How do I extract keywords from a small corpus?"` |
| `description` | One-sentence summary. | `"A beginner workflow for finding repeated and distinctive words."` |
| `category` | Category slug. | `"corpora"` |
| `difficulty` | `beginner`, `intermediate`, or `advanced`. | `"beginner"` |
| `time` | Approximate time. | `"30–60 min"` |
| `tags` | Searchable keywords. | `[corpus, keywords, voyant]` |

Allowed categories:

```text
terminology
cat-tools
subtitling
automation
nlp
corpora
pdf
visualization
mt-eval
audio
publishing
data-wrangling
editions
mapping
ai
ethics
```

## Writing rules

- Answer one question, not a whole field.
- Use plain English.
- Prefer short paragraphs.
- Use numbered steps for workflows.
- Name the expected output.
- Include checks and failure modes.
- Do not hide uncertainty.
- Do not publish restricted data.
- Link to official documentation when possible.
- Keep code snippets minimal and runnable.

## Submission checklist

Before submitting the page, confirm:

- [ ] The title starts with `How do I` and ends with `?`.
- [ ] The file is in the right `docs/workflows/` category.
- [ ] The page has all required frontmatter fields.
- [ ] The workflow starts with a tiny sample.
- [ ] The output is named and recognizable.
- [ ] The checks are concrete.
- [ ] At least two common traps are listed.
- [ ] Rights, ethics, or access issues are addressed where relevant.
- [ ] Links work.
- [ ] Another person has tested or reviewed the instructions.

## Local validation

From the repository root:

```bash
python scripts/check_answers.py
mkdocs build --strict
```

If the page is not visible in the menu, add it to `mkdocs.yml` or ask a maintainer to do so.
