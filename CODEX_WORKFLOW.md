# Codex handoff workflow

This project separates editorial design from implementation so that large changes remain reviewable.

## Roles

- **Editorial architect**: defines the intellectual structure, sources, scope, bilingual requirements and acceptance criteria in a GitHub issue.
- **Codex implementer**: reads the issue and `AGENTS.md`, makes the bounded change on a task branch, runs validation and opens a pull request.
- **Maintainer/editor**: reviews argument, Slovene quality, visual result and source accuracy before merging.

The roles may be performed by different tools or people, but their outputs must remain visible in the issue and pull request.

## Standard cycle

1. **Create or refine one issue.** It must state what problem is being solved, what is out of scope, which files or sections are expected to change, and how completion will be judged.
2. **Give Codex the issue, not a vague request.** Use the prompt below and replace the issue number.
3. **Codex works on a new branch.** It should inspect the repository before changing files and should not push directly to `main`.
4. **Codex opens a pull request.** The pull request links the issue, reports tests and includes screenshots for visual work.
5. **Review in two passes.** First review factual, editorial and translation quality; then review implementation, accessibility and build output.
6. **Merge only after `make check` passes.** A merged change should be small enough to revert without disturbing unrelated work.

## Ready-to-paste Codex prompt

```text
Implement GitHub issue #ISSUE_NUMBER in the repository
`damjan-popic/digital-humanities-handbook`.

Read `AGENTS.md`, `CODEX_WORKFLOW.md`, the issue body and all files named by the
issue before editing. Work on a new task branch and open a pull request; do not
push directly to `main`.

Stay within the issue scope. Preserve English/Slovene parity for the stable
handbook core. Verify all factual references rather than inventing citations.
Run `make check`, inspect the generated English and Slovene pages, and include
exact test results in the pull request. For visual changes, test light and dark
mode at mobile, tablet and desktop widths and include before-and-after
screenshots. Record any uncertainty instead of silently guessing.
```

## Issue design template

A strong implementation issue contains these headings:

```markdown
## Problem
## Editorial or design rationale
## Required changes
## Files and navigation affected
## Sources or design tokens
## Out of scope
## Acceptance criteria
## Validation
```

## Content task rules

- One new stable chapter normally equals one issue and one pull request.
- Historical or theoretical chapters must be written in both English and Slovene in the same pull request.
- Source gathering and chapter drafting may be separate issues when the literature base is still unsettled.
- Do not ask Codex to translate a long chapter blindly. The Slovene text must be edited as academic Slovene and checked against the English argument, not sentence by sentence.
- Update the review manuscripts and navigation when a stable chapter is added or reordered.

## Visual task rules

- Separate palette and typography changes from major layout restructuring where possible.
- Define named CSS variables before styling individual components.
- Preserve Material for MkDocs behaviour unless the issue explicitly requests a template override.
- Use the smallest robust fix for a local glitch; avoid hiding useful functions merely to conceal an overlap.
- A visual task is incomplete without checking the homepage, one theory chapter, one workflow page and both language editions.

## Review questions

Before merging, the maintainer should be able to answer yes to these questions:

- Does the change solve the issue without broad collateral edits?
- Is the humanities argument clearer or the reading experience better?
- Are English and Slovene substantively aligned?
- Are sources real, accurate and appropriately cited?
- Does the site build strictly and remain usable at mobile width?
- Is the change understandable from the issue and pull-request record alone?
