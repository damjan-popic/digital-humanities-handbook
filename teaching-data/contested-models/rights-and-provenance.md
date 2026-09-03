# Source and rights audit

Checked 2026-09-03. This records provider statements and our transformations,
not a general legal determination for every jurisdiction.

## Authentic map

Ciril Metod Koch, *Ljubljana*, 1910. Plan at 1:8,200; 45 × 59 cm on a
47 × 61 cm sheet. Catalogue publisher entries: J. Blasnika nasl.;
Katoliška bukvarna. Provider: Narodna in univerzitetna knjižnica.
COBISS 49514240; dLib URN:NBN:SI:IMG-132KCU7C.

- [Primary catalogue](https://dlib.si/details/URN:NBN:SI:IMG-132KCU7C).
- [Downloaded image](https://dlib.si/stream/URN:NBN:SI:IMG-132KCU7C/70a09865-89e6-4365-97b8-76d9697c2884/IMAGE).
- The catalogue links a “javna domena” Public Domain Mark badge to
  [dLib's public-domain rights statement](https://www.dlib.si/Rights.aspx?q=PDM).
  We rely on that provider assessment for redistribution of this teaching scan.
  Do not relabel the underlying map as newly licensed CC BY.
- Preserved JPEG: 5747 × 7287 pixels; SHA256
  `d3c6c0475a6976c69c99065b7b9df1ae57a5fe6416a9acc858ef0cf75aebf21c`.
  No crop, colour edit or recompression was applied.
- This is the dLib image, not the differently sized Wikimedia Commons derivative.
  Map publication date is not a verified survey date for every feature.
- The map supplies a local, historically situated exercise; the fictional
  1920 district divider is NOT traced from it and is not historical evidence.

## Current coordinate records

Structured P625 coordinates were read from Wikidata on 2026-09-03. Wikidata
structured data are [CC0](https://www.wikidata.org/wiki/Wikidata:Licensing).
No imagery or prose from third-party basemaps is redistributed.

| Landmark | Record revision |
|---|---|
| Dragon Bridge | [Q660029, 2496507216](https://www.wikidata.org/w/index.php?title=Q660029&oldid=2496507216) |
| Trnovo church | [Q12786851, 2283288802](https://www.wikidata.org/w/index.php?title=Q12786851&oldid=2283288802) |
| Ljubljana Castle | [Q2075156, 2537158640](https://www.wikidata.org/w/index.php?title=Q2075156&oldid=2537158640) |
| Tivoli Castle | [Q3402462, 2445573064](https://www.wikidata.org/w/index.php?title=Q3402462&oldid=2445573064) |
| Railway station | [Q1817806, 2532059745](https://www.wikidata.org/w/index.php?title=Q1817806&oldid=2532059745) |
| Cathedral | [Q1236564, 2532079073](https://www.wikidata.org/w/index.php?title=Q1236564&oldid=2532079073) |

`input/landmarks.csv` preserves coordinates, revision, reported precision and
our image-selection notes. `prepare_georeferencing.py` transforms longitude,
latitude from EPSG:4326 to EPSG:3794 using pyproj 3.7.2 with `always_xy=True`.
The cached projected coordinates are rounded to millimetres for reproducibility,
not a claim of millimetre accuracy.

Manual pixel selections are unapproved first-pass landmark candidates. In
particular the station's coordinate may refer to another part of the complex,
and the cathedral selection requires re-identification. The four-control fit
has 15.231 m RMSE but the independent checks have 220.063 m RMSE. Retain this
failure; no approved georeferenced raster is supplied. The QGIS GUI procedure
awaits recorded manual testing and methodological review.

## Newspaper reuse and synthetic records

The runner reads the original eight observation rows from
`../archival-friction/reference/observations.csv`. The download carries the
same bytes in `source/archival-observations.csv`, plus copies of the original
rights/provenance and citation notes. These are handbook-authored observations
with short transcribed labels, not a new digitization. The full PDF and provider
OCR are not duplicated here. Consult the original packet's jurisdictional
limitations before reusing its facsimile; this map audit does not resolve them.

The SYN dossier, fictional multilingual names and boundary experiment are
original teaching text/data under CC BY 4.0. Scripts are original code under MIT.
Repository licence files are included in the download. Do not attribute the
synthetic “source wording” to Koch, dLib, Wikidata or the newspaper. No new
third-party photographs, sensitive personal locations or remote map tiles were
added. All numerical outputs retain the separation of authentic, synthetic and
derived evidence.
