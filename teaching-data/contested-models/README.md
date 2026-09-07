# Contested models: a companion to archival friction

Research question: how do documentary labels become identities, territorial
memberships and apparent relationships when editors turn sources into models?

The original archival-friction packet remains unchanged. Its eight reference
observations describe one authentic issue of *Ilustrirani Slovenec* (1925-02-07).
The runner selects four individually labelled people to demonstrate six
same-issue co-occurrence pairs. This does not establish correspondence.

The six people A–F, six documents D1–D6, status notes, name variants and boundaries
in `input/` are **entirely synthetic**, identified by `SYN-` IDs. Ana Kovač /
Anna Kovatsch is fictional, not an identification of anyone in the newspaper.
Read `input/dossier.md` before using the tables. Source-readable test records
make it possible to check an output against something other than generated data.

The authentic `source/ljubljana-1910.jpg` is used separately for georeferencing.
It does not authenticate the invented boundary model. Read
`rights-and-provenance.md` before reuse.

## Run the downloaded packet

With Python 3.10 or later (tested on 3.12), standard library only:

```bash
python run.py --output output-first
python query.py --database output-first/dossier.sqlite --subject SYN-A --as-of 1910-06-15
python query.py --database output-first/dossier.sqlite --conflicts
```

Use a new output directory for every run; the runner refuses to overwrite one.
The output includes a SQLite database, source-linked CSVs, metrics and
`results.json`. Compare with `expected/`. No network request is made by the
runner. The downloadable archive includes the unchanged observation extract and
its source/rights notes, plus a machine-readable dLib item record; the full
newspaper facsimile remains in the
[archival-friction packet](https://github.com/damjan-popic/digital-humanities-handbook/tree/main/teaching-data/archival-friction).

## Repository maintenance

From the repository root:

```bash
python teaching-data/contested-models/run.py --output .cache/contested-models
python scripts/build_contested_models_packet.py
python scripts/check_contested_models.py
make check
```

The builder regenerates expected outputs and the deterministic download. Its
`--check` mode recomputes and compares without replacing committed artifacts.
The ZIP contains a SHA256 manifest and fixed member dates. Do not edit generated
expected files manually.

## Optional GIS preparation

The cached coordinates in `input/gcps.csv` are already projected. To regenerate
them, install the pinned optional dependency in an isolated environment:

```bash
python -m pip install -r requirements-gis.txt
python prepare_georeferencing.py --check
```

This uses cached Wikidata longitude/latitude, no live lookup, and EPSG:3794.
The source image is 5747 × 7287 pixels. Pixel y is positive downward in the CSV
and negative in the generated QGIS points file. Its initial residual zeros are
placeholders. The affine numerical check does not resample a raster.

## Interpretation and access

Every exercise has non-visual tables. No colour, layout or mouse interaction is
needed to interpret the core comparisons. The QGIS workflow is a separate manual
exercise: the numerical fit and tabular audit do not certify a visually inspected
alignment. The first-pass controls fail independent accuracy checking and remain
a review exercise, not an approved georeferenced map.

The local engineering square and multilingual gazetteer note are invented.
Never place their coordinates on a real basemap or merge synthetic people into
the authentic observation table. Read `data-dictionary.md` for field meanings,
`expected/results.json` for complete results, and `README.sl.md` for Slovene
instructions. Human methodological and Slovene-language review remain pending.
