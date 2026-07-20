# Contribute

This handbook is designed to grow through small, credited and reviewable contributions. A useful contribution leaves the next reader with a clearer question, a more reproducible method or a more accurate translation.

## Ways to contribute

- report a broken instruction, link or factual claim;
- translate or review one corresponding page;
- improve an example, validation step or expected output;
- document a bounded workflow;
- contribute a small rights-cleared teaching dataset;
- add a critical case study of a public project;
- propose a revision to a handbook chapter for the next reviewed release.

## Minimum standard

Before opening a pull request, run:

```bash
python scripts/check_handbook.py
python scripts/check_translation_coverage.py
mkdocs build --strict
```

The pull request should explain what changed, how it was tested, which language and release it affects, and whether any data, copyright, privacy or ethical conditions apply.

## Students as contributors

Coursework does not become public automatically. Students choose whether to submit their work, understand the open licences, receive attribution, and pass editorial review. A grade and a publication decision are separate things. That separation protects students and the handbook.

Read the repository-level `CONTRIBUTING.md`, `EDITORIAL_POLICY.md`, `REVIEW_POLICY.md` and `TRANSLATION_POLICY.md` before substantial work.
