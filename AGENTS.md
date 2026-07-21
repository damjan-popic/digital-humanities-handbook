# Repository instructions for coding and editorial agents

This repository is a bilingual, open educational publication. Treat it as both software and a peer-reviewable handbook. A technically successful change is not complete unless it is also editorially coherent, bilingual where required, accessible and reproducible.

## Task contract

- Work from one GitHub issue or an equally explicit task brief.
- Before editing, identify the objective, affected files, exclusions and acceptance criteria.
- Keep one bounded concern per branch and pull request. Do not mix a content expansion, a visual redesign and unrelated maintenance unless the issue explicitly combines them.
- Do not push directly to `main`. Commit the change on a task branch and open a pull request.
- Do not opportunistically rewrite unrelated prose or reorganize navigation beyond the stated scope.
- When instructions conflict or a factual claim cannot be verified, stop and record the uncertainty instead of guessing.

## Non-negotiable architecture

- English is the default edition in `docs/en/`.
- Slovene is the parallel edition in `docs/sl/`.
- The handbook chapters and both learning paths are the stable publication core. Every change to one language must update the paired page in the same pull request, unless the issue explicitly authorizes a tracked translation gap.
- The workflow library may use English fallback, but do not present fallback as a completed Slovene translation.
- `main` is the living edition. Tagged releases are frozen, citable snapshots.
- Do not edit generated files in `site/`.
- When chapter order or content changes, update both language navigation trees in `mkdocs.yml`, internal links, review manuscripts and any generated indexes affected by the change.

## Writing and editorial rules

- Begin with a humanities research question or conceptual problem, not a product name.
- State learning outcomes, prerequisites, inputs, outputs, checks, failure modes and ethical or licensing limits where appropriate.
- Separate stable concepts and methods from interface-specific instructions so pages survive software updates.
- Use real humanities examples and never imply that computational output interprets itself.
- Distinguish description, evidence, interpretation and recommendation.
- Slovene must read as authored academic Slovene, not literal machine translation. Keep established software names, code and identifiers unchanged.
- Preserve the pedagogical anatomy of the stable chapters: learning outcomes, prior-knowledge prompt, core argument, worked example, practice, reflection, summary and further reading.

## Historical and theoretical content

- Use authoritative, traceable sources. Prefer original project or organization histories, peer-reviewed scholarship, scholarly books and stable DOI-bearing publications.
- Never invent bibliographic details, dates, quotations or URLs. Verify every reference before committing it.
- Treat the history of digital humanities as a contested genealogy, not a single heroic origin story. Include institutions, standards, infrastructures, collaborative labour and changes in terminology as well as famous individuals.
- Explain why historical developments matter methodologically: representation, modelling, scale, interpretation, access, labour, language, power and preservation.
- Include Slovenian and wider regional developments where the issue calls for them, using official infrastructure and project sources where possible.
- New stable theory chapters must be substantively equivalent in English and Slovene and must include a compact further-reading section.

## Design and accessibility

- Put visual changes in `docs/assets/stylesheets/extra.css` unless a template override is genuinely necessary.
- Use CSS custom properties for the palette and support both the light and dark schemes.
- Do not add external fonts, tracking scripts, remote images or decorative dependencies without explicit approval.
- Maintain readable contrast, visible keyboard focus and sensible reduced-motion behaviour. Do not communicate meaning by colour alone.
- Test visual changes at approximately 360 px, 768 px and 1280 px viewport widths, in light and dark mode.
- Avoid brittle absolute positioning when normal document flow, flexbox, grid or `clear` will solve the problem.
- For visual pull requests, include before-and-after screenshots or state clearly why screenshots could not be produced.

## Rights and provenance

- Do not add third-party images, datasets or substantial quoted material without documenting rights and provenance.
- Text is licensed under CC BY 4.0 and original code under MIT unless a file says otherwise.
- Keep quotations short and attribute them precisely. Prefer paraphrase when a quotation is not analytically necessary.

## Files agents should read first

- `README.md`
- `CODEX_WORKFLOW.md`
- `EDITORIAL_POLICY.md`
- `TRANSLATION_POLICY.md`
- `CONTRIBUTING.md`
- `REVIEW_POLICY.md`
- `VERSIONING.md`
- `.github/PULL_REQUEST_TEMPLATE.md`

## Required validation

Run:

```bash
make check
```

This rebuilds workflow indexes, reports translation coverage, validates the paired core, checks workflow metadata and builds both language editions with strict MkDocs validation.

For navigation, theme or homepage changes, also inspect the generated English and Slovene pages and check that:

- the language switch remains paired;
- edit and source actions do not overlap page content;
- no horizontal scrolling appears at mobile width;
- light and dark modes both remain legible;
- internal links and table-of-contents anchors work.

## Pull-request completion rule

A pull request is ready only when it:

1. links the governing issue;
2. explains the editorial or technical rationale;
3. lists the English and Slovene files changed;
4. reports the exact validation commands and results;
5. records any remaining uncertainty or follow-up work;
6. leaves the worktree clean and all changes committed.
