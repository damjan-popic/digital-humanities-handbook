# Publish the new repository on GitHub

The prepared repository targets:

- repository: `damjan-popic/digital-humanities-handbook`
- Pages URL: `https://damjan-popic.github.io/digital-humanities-handbook/`
- default branch: `main`

## Automated route

Install and authenticate GitHub CLI, then from the repository root run:

```bash
bash scripts/publish_to_github.sh
```

The script refuses to overwrite an existing remote and performs validation before the first push.

## Manual route

1. Create a **public** empty repository named `digital-humanities-handbook` under `damjan-popic`. Do not add a README or licence in the GitHub form.
2. In this repository run:

```bash
git remote add origin git@github.com:damjan-popic/digital-humanities-handbook.git
git push -u origin main
```

HTTPS is also possible:

```bash
git remote add origin https://github.com/damjan-popic/digital-humanities-handbook.git
git push -u origin main
```

3. Open **Settings → Pages** and select **GitHub Actions** as the source.
4. Add repository topics: `digital-humanities`, `open-education`, `mkdocs`, `slovenian`, `text-analysis`, `corpus-linguistics`.
5. Set the homepage to the Pages URL.
6. Enable issues and discussions if they will be moderated.
7. Protect `main`: require pull requests and the `build` status check once the first workflow has run.

## First public milestone

Push the prepared commit as development release `0.1.0`. Do not tag `v1.0.0` until the content freeze, formal review and publisher decision are complete.
