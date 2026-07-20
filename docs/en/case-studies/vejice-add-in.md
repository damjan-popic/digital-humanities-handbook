---
title: "Slovenian comma-checking Word add-in"
description: "A Microsoft Word add-in pattern for reviewing Slovenian comma placement with safe-by-default service configuration."
tags: [projects, Word-add-in, punctuation, Slovene, JavaScript]
---

# Slovenian comma-checking Word add-in

<div class="answer-meta" markdown>
<span>application code</span>
<span>Word add-in</span>
<span>privacy</span>
</div>

## What this project does

This example shows a Microsoft Word add-in for reviewing Slovenian comma placement. The fork is configured with safety defaults: mock mode avoids sending document text out of the add-in, and remote services must be explicitly trusted or allowed.

[:octicons-mark-github-16: Open the source repository](https://github.com/damjan-popic/Vejice_add_in)

## Use this when

- you want users to inspect a real language-technology application, not only scripts.
- you need a privacy-aware example of local vs remote processing.
- you want to discuss service configuration, manifests, tests, and build steps.
- you need a concrete case for Slovenian punctuation support in writing tools.

## What to inspect in the code

- `src/` — add-in source code.
- `docs/manifest.web.xml` and related manifests — Office add-in deployment.
- `.env.example` — safe configuration pattern.
- `tests/` — logic and service-configuration tests.
- `package.json` — scripts for build, validation, and internal testing.
- `proxy/` — optional service proxy logic.

## Minimal run path

```bash
npm install
npm run start:internal
```

This starts the add-in in safe mock mode. For production or remote service testing, configuration must be explicit.

## Relevant handbook workflows

- [How do I audit AI output against source documents?](../workflows/ai/audit-ai-output-against-source-documents.md)
- [How do I automate a linguistic workflow with a Makefile?](../workflows/automation/automate-a-linguistic-workflow-with-a-makefile.md)
- [How do I write a README for a humanities dataset?](../workflows/publishing/write-a-readme-for-a-humanities-dataset.md)
- [How do I decide whether a digitised source should be public?](../workflows/ethics/decide-whether-a-digitised-source-should-be-public.md)

## Practice use

Ask users to trace what happens to document text in mock mode and remote mode. They should identify the exact setting that permits text to leave the add-in and explain the privacy implications.

## Limits and cautions

- A language-checking add-in can process sensitive document text.
- Remote APIs must be treated as data processors, not invisible plumbing.
- Mock mode is safe for demonstrations but does not validate the quality of comma correction.
- Production deployment requires careful service, security, and user-consent review.
