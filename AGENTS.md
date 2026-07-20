# Repository instructions for coding agents

This repository is a bilingual, open educational publication. Treat it as both software and a peer-reviewable handbook.

## Non-negotiable architecture

- English is the default edition in `docs/en/`.
- Slovene is the parallel edition in `docs/sl/`.
- The 12 handbook chapters and both learning paths are the stable publication core. Every change to one language must either update the paired page or open an explicit translation issue.
- The workflow library may use English fallback, but do not present fallback as a completed Slovene translation.
- `main` is the living edition. Tagged releases are frozen, citable snapshots.

## Writing rules

- Begin with a research or practical question, not a product name.
- State learning outcomes, prerequisites, inputs, outputs, checks, failure modes and ethical/licensing limits.
- Separate method from interface instructions so pages survive software updates.
- Use real humanities examples and avoid claiming that computational output is self-interpreting.
- Slovene must read as authored academic Slovene, not literal machine translation. Keep established software names and code unchanged.

## Before proposing a change

Run:

```bash
make check
```

The command rebuilds the workflow indexes, reports translation coverage, validates the paired core, checks workflow metadata and builds both language editions with strict MkDocs validation.

## Files agents should read first

- `README.md`
- `EDITORIAL_POLICY.md`
- `TRANSLATION_POLICY.md`
- `CONTRIBUTING.md`
- `REVIEW_POLICY.md`
- `VERSIONING.md`

Do not edit generated files in `site/`. Do not add third-party images or datasets without documenting their rights and provenance.
