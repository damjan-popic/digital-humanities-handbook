# Archival friction teaching packet

This bilingual packet accompanies the handbook route through research
design, data and metadata, and text/OCR work. It keeps authentic provider
material, handbook reference work, synthetic teaching disturbances and
derived results visibly separate.

## Research prompt

How does a politically partisan illustrated supplement turn people, places
and recent events into evidence, and what is lost when its captions are
treated as neutral metadata?

The inventory contains **one authentic historical object**, issue 7 of
*Ilustrirani Slovenec* dated 7 February 1925, represented by an unchanged
two-page PDF. From it the handbook creates **eight source-grounded reference
observations**: one issue record and seven feature records. The teaching layer
declares **four synthetic perturbations**. Reference observations and
perturbations are not additional authentic archival records.

## Packet layers

| Layer | Purpose | Exercise rule |
| --- | --- | --- |
| `source/` | Unchanged PDF, captured dLib and Commons records, unchanged provider OCR | Never edit; copy material forward |
| `reference/` | Handbook-created source-grounded observations, editorial decisions, reference transcription and policy | Use as an auditable comparison, not “ground truth” |
| `teaching/` | Four declared synthetic disturbances | Use only to construct the exercise |
| `raw/` | Deliberately awkward rows and copied provider OCR | Preserve; copy to `interim/` |
| `interim/` | Candidates awaiting source/reference review | Review and record a decision |
| `cleaned/` | Audited observations, reference transcription and decisions | Compare with your result |
| `output/` | OCR counts, error audit and record summaries | Regenerate; do not hand-edit |
| `validation/` | Expected results and file digests | Regenerate after an authorized change |
| `known-problems/` | Limits deliberately left open | Extend when a new limit is documented |

Top-level `metadata-raw.csv` and `metadata-clean.csv` are deterministic
copies of the corresponding layered tables. `correction-log.csv` combines
eight authentic editorial decisions (`synthetic=false`) with the four
reversals of declared teaching disturbances (`synthetic=true`).

## Low-threshold exercise

1. Read `rights-and-provenance.md`, then open the PDF.
2. Inspect `raw/messy-records.csv`. Label source observation, provider
   metadata, inference and synthetic disturbance separately.
3. Compare it with `reference/observations.csv`. Do not infer a photograph's
   creation date from the issue date.
4. Preserve the printed person/group label separately from
   `entity_structure`, an external `authority_candidate` and
   `authority_link_status`.
5. Compare `raw/provider-ocr.txt` with
   `reference/reference-transcription.txt`. Classify errors before consulting
   `output/ocr-error-audit.csv`.
6. Review `correction-log.csv`, `unresolved-cases.csv` and the summaries in
   `output/`. Explain how uncertainty affects a research claim.

No command line is required for the student exercise. Maintainers rebuild
all derived files, the deterministic ZIP and its SHA-256 with:

```text
make archival-friction-packet
```

The builder uses the Python standard library plus the repository's public
authoring utilities and never downloads or replaces the committed scan.

## Accessible page descriptions

**Page 1.** A grayscale illustrated front page headed *Ilustrirani
Slovenec*. A large political cartoon sits above photographs of a crowd
outside Ljubljana's Hotel Union, the Ljubljanica riverbed and four named
men. Captions frame the images in openly partisan language.

**Page 2.** A grayscale montage headed “Iz razpuščene narodne skupščine”. It
contains a group portrait of German deputies, photographs of Ljubljana and
street scenes labelled as German and American election campaigns. Dense
captions and uneven columns make the provider OCR's reading order unstable.

## Ethical use

The issue is a partisan historical publication. Its descriptions of people
and political groups are evidence of the publication's rhetoric, not neutral
descriptions endorsed by the handbook. Keep image, caption, provider OCR,
reference transcription and later authority claims distinguishable. The
sample contains no contemporary personal data.
