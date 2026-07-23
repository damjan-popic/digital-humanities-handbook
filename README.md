# Digital Humanities Handbook / Priročnik za digitalno humanistiko

An open, bilingual and versioned handbook for digital humanities methods. The repository combines a stable, reviewable handbook core with a living collection of practical workflows, case studies and course pathways.

**Public site:** `https://damjan-popic.github.io/digital-humanities-handbook/`

## What changed from the Digital Linguistics Playbook

- The scope is now digital humanities, with text analysis as the main spine and databases, GIS, networks, digital editions, AI and research publishing as connected methods.
- English and Slovene are built from one repository, with a language switch that keeps readers on the corresponding page when a translation exists.
- Narrative chapters provide the stable, peer-reviewable publication core.
- A validated ecosystem map connects chapters, workflows and case studies in both directions instead of presenting them as separate collections.
- Practical workflows remain modular and can be expanded by students and external contributors.
- Learning paths connect the handbook to *Pismenost za informacijsko družbo* and *Digitalna slovenistika*.
- Tagged releases provide citable snapshots; `main` remains the living edition.

## Local setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
mkdocs serve
```

## Validate and build

```bash
make check
```

The validation suite checks the bilingual stable core, course-path order, workflow and case-study structure, translation coverage, and the reciprocal ecosystem map before running a strict MkDocs build.

## Language structure

```text
docs/
├── assets/   # shared images, CSS and JavaScript
├── en/       # English edition (default site)
└── sl/       # Slovene edition (/sl/)
```

The English edition currently also preserves the broader workflow library inherited from the original playbook. The Slovene edition begins with a complete handbook core and selected teaching workflows. Translation coverage is measured automatically and is designed to grow through reviewed contributions. Clearly marked English fallback pages keep the wider ecosystem usable without pretending that untranslated pages are finished Slovene translations.

## Publication model

- `main`: continuously maintained living edition;
- `v1.0`, `v1.1`, ...: reviewed and citable releases;
- release archive: DOI/long-term repository when institutional arrangements are confirmed;
- optional PDF/EPUB: generated snapshot for review, deposit and offline use, not the canonical source.

## Licensing

- Prose, teaching materials and original figures: **CC BY 4.0**.
- Code and scripts: **MIT**.
- Third-party data, screenshots and linked repositories retain their own licenses.

See [LICENSE.md](LICENSE.md), [CONTRIBUTING.md](CONTRIBUTING.md), and [EDITORIAL_POLICY.md](EDITORIAL_POLICY.md).
