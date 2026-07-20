# About the project

The **Digital Humanities Handbook** is an open, bilingual and versioned publication for practical and critical digital humanities. It grew from the *Digital Linguistics Playbook* but now has a broader architecture: text analysis remains the central spine, while data modelling, databases, OCR, digital editions, GIS, networks, visualization, AI, ethics and open research are treated as connected forms of humanities inquiry.

## Who it is for

The handbook serves humanities students encountering digital methods for the first time; advanced students building reproducible projects; teachers designing practical courses; researchers, translators, archivists, librarians and cultural-heritage professionals; and contributors working with Slovene or other under-resourced languages.

## Two publication tempos

The **stable handbook core** changes deliberately. It is written as chapters, aligned with learning outcomes and suitable for formal peer review. The **living workbench** changes more often. Workflows, links, translations and small examples can be corrected or extended through reviewed pull requests.

A numbered release freezes both layers into a citable edition. The web view of `main` is useful for teaching, but scholarly citation should identify a release or commit.

## Editorial principles

- Start with a humanities question, not a fashionable tool.
- Show how evidence was selected, transformed and interpreted.
- Prefer small inspectable examples before scale.
- Treat model output as an argument requiring validation, not as a result requiring admiration.
- Document uncertainty, failure modes, provenance, licences and ethical limits.
- Keep code and data close to the explanation without making the prose dependent on one interface version.
- Credit students and other contributors as authors of accepted work.

See the repository policies for editorial governance, peer review, translation and versioning.

## Languages and translation

English is the complete default edition inherited from the original workflow library. Slovene is a first-class editorial edition: all stable chapters and learning paths are paired, while practical workflows are translated incrementally. When a Slovene counterpart is missing, the site may show the English fallback page; it is not labelled as a completed translation.

Every release generates `release/translation-coverage.md`, which lists paired, fallback and Slovene-only pages. New or changed stable chapters cannot be released without both language versions.
