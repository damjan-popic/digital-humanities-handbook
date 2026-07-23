---
title: "Student workflow contribution template"
description: "A structured template for turning coursework or disciplinary expertise into a small, reproducible handbook workflow."
tags: [student, contribution, workflow, template, reproducibility]
---

# Student workflow contribution template

Use this template when a student turns a piece of disciplinary knowledge into a practical contribution to the handbook.

The contribution should answer **one bounded question**, produce **one inspectable output**, and let another student repeat the procedure. It is not a shortened seminar paper and it is not a report about a tool.

!!! important "Assessment and publication are separate"
    Coursework does not become public automatically. A student may complete the assessed task without agreeing to publication. Public inclusion requires a separate editorial decision, attribution, rights clearance, and agreement to the handbook licences.

## Choose the contribution

A suitable question begins with **How do I ...?** and names a concrete task.

Good examples:

- How do I compare a historical map with a current orthophoto in QGIS?
- How do I turn field observations into a reusable heritage dataset?
- How do I measure OCR errors in a small historical corpus?
- How do I map uncertain place references without hiding ambiguity?
- How do I check an AI-generated summary against archival sources?

Avoid titles such as *QGIS*, *Digital archaeology*, *My BA thesis*, or *Artificial intelligence*. Those name a field or tool, not a reproducible task.

## Minimum submission package

Submit a small folder or repository containing:

```text
student-contribution/
├── workflow.md
├── README.md
├── sample/
│   ├── input/
│   └── output/
├── code/                 # optional
├── sources.md
└── contribution-statement.md
```

Use a tiny, rights-cleared sample. Do not submit a full thesis dataset, confidential institutional material, precise locations of vulnerable heritage, personal data, or third-party images unless publication and reuse are explicitly permitted.

## Copy-paste workflow template

Copy the Markdown below into `workflow.md` and replace the prompts.

```markdown
---
title: "How do I [complete one specific task]?"
description: "A one-sentence description of the input, method, and expected output."
category: "mapping"
difficulty: "beginner"
time: "60–120 min"
tags: [heritage, qgis, validation]
author: "Student name"
status: "student-draft"
---

# How do I [complete one specific task]?

<div class="answer-meta" markdown>
<span>mapping</span>
<span>beginner</span>
<span>60–120 min</span>
</div>

## What you are trying to do

Use this workflow when you have [input material] and need to produce [visible output] for [humanities purpose].

State the task in two to five sentences. Name the disciplinary problem before the software.

## Research context

Explain why the task matters in your field.

- What kind of source or object is involved?
- What scholarly decision does the procedure support?
- What would a reader misunderstand if the source were treated as neutral data?

Keep this section short. Link to a relevant handbook chapter rather than repeating general theory.

## You need

- **Source material:** [maps, texts, photographs, field notes, database records, etc.]
- **Access:** [software, account, repository, institutional permission]
- **Skills:** [none, spreadsheet basics, QGIS basics, Python basics, etc.]
- **Decisions:** [unit of analysis, date range, coordinate system, categories, uncertainty rules]

## Input and provenance

Describe the sample and where it came from.

| Item | Source or creator | Date | Licence/access | Changes made |
|---|---|---|---|---|
| `sample-map.tif` | [source] | YYYY | [licence or restriction] | cropped for teaching |
| `observations.csv` | [creator] | YYYY-MM-DD | CC BY / private / restricted | names generalized |

List the minimum required fields if you use a table.

| Field | Required? | Example | Meaning |
|---|---:|---|---|
| `id` | yes | `site-001` | Stable record identifier. |
| `source` | yes | `field survey` | Where the observation came from. |
| `date` | yes | `2026-07-23` | ISO date where possible. |
| `uncertainty` | no | `medium` | Documented confidence or ambiguity. |

## Tools and versions

- [Tool name](https://example.org) — role in this workflow.
- Version used: [version, only when consequential].
- Alternative: [optional alternative and what changes].

Use official documentation where possible.

## Workflow

1. **Prepare a tiny sample.**  
   Start with two or three records, one image, or one short text. Preserve the original files unchanged.

2. **Record the source and settings.**  
   Note the source URL or archive reference, access date, file format, coordinate system, tool version, and relevant settings.

3. **Perform the first transformation.**  
   Explain exactly what to click, run, enter, or configure.

4. **Inspect the result manually.**  
   Compare at least one output with its source. Record mismatches, uncertainty, and information lost during transformation.

5. **Correct or annotate problems.**  
   Never silently repair a source. Preserve the original value and document the normalized, inferred, or corrected value separately.

6. **Scale up only after the test works.**  
   Apply the procedure to the full teaching sample, not automatically to every available item.

7. **Export and document the output.**  
   Use stable file names and include a short README explaining how the output was produced.

## Output

Name the expected result and show its structure.

```text
sample/output/
├── result.csv
├── result-map.png
├── validation-sample.csv
└── known-limitations.md
```

Explain what each file contains and which file should be inspected first.

## Validation

Provide concrete checks.

- Are all source items represented exactly once?
- Can every output be traced to its source?
- Have coordinates, dates, names, or categories been changed?
- Are uncertain cases marked rather than forced into a category?
- Does a second person obtain the same output from the instructions?

Add at least one pass/fail criterion.

> The workflow passes if [specific count or condition], and a manual check of [number] examples finds no [defined blocking error].

## Interpretation and limits

State what the output can support and what it cannot establish.

Include at least:

- one gain from the digital procedure;
- one loss or transformation;
- one likely source of error;
- one claim that would be too strong.

## Rights, ethics, access, and heritage sensitivity

Address the issues relevant to the sample:

- copyright and image reuse;
- personal data and consent;
- archival or institutional restrictions;
- precise locations of vulnerable sites;
- community or cultural authority;
- whether the output should be public, generalized, restricted, or omitted.

Do not publish a technically impressive example that creates a heritage, privacy, or rights problem.

## Worked example

Describe one small run from input to output. Use a toy or legally reusable sample where necessary.

Include:

- the input;
- the consequential settings;
- the output;
- one error or ambiguous case;
- the correction or interpretation.

## Connection to the handbook

Link to:

- at least one conceptual chapter;
- at least one related workflow;
- one case study when a meaningful example exists.

Explain the connection in one sentence rather than adding a bare list of links.

## Practice task

Give another student a small extension or test.

> Apply the workflow to [small new sample], inspect [number] outputs, and write a short note explaining one successful result, one failure, and one methodological limit.

## Further reading

Add only sources directly needed to understand or repeat this task.

## Changelog

| Date | Change |
|---|---|
| YYYY-MM-DD | First student draft. |
```

## Contribution statement

Create `contribution-statement.md` with the following information:

```markdown
# Contribution statement

- Student author:
- Course or examination:
- Instructor/editor:
- Date submitted:
- Tested by:
- Sources and third-party material checked: yes / no / not applicable
- AI assistance used: none / describe precisely
- Publication choice: assessment only / may be considered for publication
- Licence consent for accepted prose: CC BY 4.0 / not yet given
- Licence consent for accepted original code: MIT / not yet given
- Known restrictions or material that must not be published:
```

A publication choice of **assessment only** is valid and must not affect the grade.

## Language policy for student work

Unless the instructor specifies otherwise:

- submit the complete workflow in the language of the course;
- provide an English title and one-sentence description when the main version is Slovene;
- a full second-language version is a separate contribution and must receive language review;
- use the same filename and relative path for paired English and Slovene pages.

## Acceptance checklist

- [ ] The title asks one practical question.
- [ ] The input and expected output are named.
- [ ] A tiny sample is included or reconstructable.
- [ ] Source provenance and rights are documented.
- [ ] The workflow contains numbered, executable steps.
- [ ] At least one output is manually checked against its source.
- [ ] A pass/fail criterion is stated.
- [ ] At least two realistic failure modes or limitations are explained.
- [ ] Sensitive information is omitted, generalized, or access-controlled.
- [ ] Another person has tested the instructions.
- [ ] AI assistance, if any, is disclosed.
- [ ] Assessment and publication consent are recorded separately.
