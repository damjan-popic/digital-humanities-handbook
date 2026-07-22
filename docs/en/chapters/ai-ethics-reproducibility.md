---
title: "AI, ethics and reproducibility"
description: "How to use computational and generative systems while preserving evidence, rights, accountability and the ability to repeat a study."
tags: [AI, ethics, reproducibility, provenance, rights]
status: draft
---

# AI, ethics and reproducibility

## Learning outcomes

After this chapter, you should be able to:

- distinguish reproducibility, replicability and transparency;
- document data, code, models, prompts and environments as research materials;
- identify privacy, copyright, representational and labour risks in digital-humanities projects;
- design source-grounded uses of generative AI and verify their outputs;
- create a release package that another person can inspect and rerun.

## Before you begin

A chatbot produces a fluent summary with three convincing quotations. One quotation is slightly altered, one belongs to another author and one does not exist. The problem is not merely that “AI can hallucinate.” The workflow asked a generative system to act as a source of evidence without preserving a verifiable path back to the documents.

This chapter addresses safeguards within a project. For the upstream collections, standards, interfaces, labour and maintenance that condition such a project, read [Critical infrastructures: power, access and maintenance](critical-infrastructures.md).

## Reproducibility is a design choice

A result is **computationally reproducible** when another person can use the same data, code and environment to obtain the same or acceptably equivalent output. **Replicability** often refers to testing the claim with independently collected data or another implementation. **Transparency** means the relevant decisions, transformations and limitations are available for inspection.

Humanities projects may involve interpretive steps that cannot be reproduced mechanically. Those steps can still be made transparent through codebooks, decision logs, examples and provenance.

## Record the whole chain

A minimal research package should identify:

- source materials and access conditions;
- data selection and exclusion rules;
- scripts, queries and manual transformations;
- software, package and model versions;
- configuration, random seeds and hardware-sensitive steps;
- prompts, system instructions and model identifiers for generative AI;
- intermediate and final outputs;
- validation procedures and known failures;
- contributor roles and licences.

A notebook that runs only on the author's laptop is not reproducible. Neither is a repository that omits private data without explaining how authorized researchers can reconstruct the analysis.

## Environments and versioning

Dependencies change. Pin compatible versions in `requirements.txt`, `environment.yml`, a lockfile or a container definition. Include a small smoke test and expected output. Tag public releases and cite the release rather than the moving `main` branch.

Version data as well as code. A corrected corpus can change counts even when scripts remain identical. Release notes should distinguish content corrections, methodological changes and cosmetic edits.

## Ethical review begins before collection

Ask before acquiring data:

- Were the materials created for public circulation or a limited context?
- Do legal access and ethical permission point in the same direction?
- Could quotation, linking or aggregation expose a person who was obscure in the source context?
- Are there vulnerable communities, minors, health data or family histories?
- Does a platform's interface make data visible while its terms or social norms discourage bulk collection?
- Who bears the work of cleaning, annotation and moderation, and is that labour credited?

“Publicly accessible” is not a complete ethical argument.

## Copyright, licensing and reuse

Separate rights in source materials, annotations, code, documentation and outputs. A corpus may be shareable only as metadata, identifiers, derived features or scripts that authorized users can run locally. Do not assume that an open repository makes every included object openly licensed.

For each component, state:

- rights holder or source;
- licence or legal basis;
- permitted redistribution;
- attribution requirements;
- access restrictions and takedown procedure.

Use the least restrictive licence you can legitimately grant, not one you merely prefer.

## Bias and representational harm

Digital collections overrepresent what was preserved, digitized, catalogued, legible to OCR and available under workable rights. Models add biases from training data, annotation categories and performance differences across languages and communities.

Evaluation should therefore include:

- coverage by relevant group, genre, period and language;
- missingness and survival bias;
- subgroup error rates;
- examples of harmful or stereotyped output;
- consultation where communities are represented or named;
- limits on claims and publication of sensitive details.

A model can be technically accurate on average while reproducing a harmful historical category or failing precisely on minoritized material.

## Source-grounded generative AI

Generative AI is most defensible when it transforms or navigates supplied sources and every important assertion can be checked.

A source-grounded workflow might:

1. retrieve bounded passages from a documented collection;
2. ask the model to summarize or classify only those passages;
3. require passage identifiers and quoted evidence;
4. automatically check that quoted spans exist;
5. have a human verify interpretation and omissions;
6. preserve prompt, model, parameters, retrieved context and output;
7. compare against a non-generative baseline where possible.

Do not let citations generated from memory enter a bibliography unchecked. Treat model confidence language as rhetoric, not calibrated probability.

## Human responsibility and disclosure

A tool cannot accept authorship responsibility, obtain consent or judge whether a publication harms a living person. Name who made final decisions. Disclose AI assistance at the level relevant to readers: ideation, translation, coding, classification, copy-editing or generation.

Disclosure should enable evaluation, not perform ritual confession. “AI was used” is too vague; “Model X, version/date, classified 1,200 paragraphs under codebook Y; two annotators reviewed all low-confidence and a 20% random sample” is useful.

## Worked example: an AI-assisted archive guide

A team uses a language model to draft descriptions of archival folders.

1. Limit inputs to authorized catalogue notes and selected documents.
2. Define required fields and forbidden inferences.
3. Require source identifiers for each claim.
4. Test extraction accuracy on a manually prepared sample.
5. flag names, sensitive information and uncertain dates for review;
6. compare performance across languages and document types;
7. keep the generated description separate from the archival record until approved;
8. record reviewer, date and changes;
9. publish the model-use statement and correction channel.

The system accelerates drafting; archivists remain responsible for description and access decisions.

## Practice

Create a reproducibility and ethics checklist for one project. Include data rights, privacy, selection bias, model versions, random elements, human review, validation, release files, citation and a response plan for errors or takedown requests.

## Reflection

- Which parts of your workflow cannot be shared, and how can they still be documented?
- Who is represented in the data but absent from project decision-making?
- Would the result survive a changed model or unavailable web service?

## Summary

Responsible digital humanities combines technical repeatability with ethical accountability. Preserve the chain from source to output, version code and data, state rights and limits, test performance where harm or bias may concentrate and keep generative AI grounded in verifiable evidence. Reproducibility is not a folder added at the end; it is the architecture of a research process that others can inspect, challenge and improve.
