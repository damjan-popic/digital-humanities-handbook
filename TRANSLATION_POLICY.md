# Translation policy

English and Slovene are editorially equal languages, not a decorative interface layer. Pages share the same path so the language selector can move readers between corresponding versions.

## Principles

- Translate meaning and disciplinary function, not word order.
- Preserve code, file names, commands, data fields and cited titles unless a localized equivalent is required.
- Use established Slovene terminology where it exists; record contested terms in the bilingual glossary.
- Keep examples locally meaningful, especially for Slovene language data and cultural material.
- Mark incomplete or machine-assisted translations clearly.
- Review technical instructions by running them, not by language inspection alone.

## Workflow

1. Open a translation issue and identify the source page/version.
2. Copy the path under the target language folder.
3. Translate prose and metadata while preserving executable material.
4. Run local checks and build both language editions.
5. Request language and subject review.
6. Merge only after terminology and technical steps are approved.

Translation coverage is reported by `python scripts/check_translation_coverage.py`.
