# Archival friction teaching packet

This compact packet accompanies the handbook chapters on research design,
data and metadata, and text/OCR work. It begins with a two-page historical
source and preserves the difference between what the source shows, what a
provider's OCR reports, what a researcher corrects, and what remains
uncertain.

## Research prompt

How does a politically partisan illustrated supplement turn people, places,
and recent events into evidence, and what is lost when its captions are
treated as neutral metadata?

The source is issue 7 of *Ilustrirani Slovenec*, dated 7 February 1925. The
unchanged PDF is in `source/`. Wikimedia Commons identifies the file as a
public-domain scan supplied by the Digital Library of Slovenia (dLib.si).
See `RIGHTS.md` and `SOURCE_CITATION.md` before reusing it.

## Packet layers

| Layer | Purpose | May you edit it during an exercise? |
| --- | --- | --- |
| `source/` | Unchanged facsimile, provider record, eight source-grounded records, and the declared synthetic perturbations | No; make a copy |
| `raw/` | Deliberately awkward metadata and the provider OCR excerpt | Yes, in a working copy |
| `cleaned/` | Audited metadata, a short gold transcription, and logged decisions | Use as the comparison target |
| `output/` | Recomputed OCR metrics and record counts | Regenerate; do not hand-edit |
| `validation/` | Checksums for the complete packet | Regenerate after an authorised packet change |
| `known-problems/` | Limits that the exercise does not resolve | Extend when you discover another limit |

The `raw/` duplicate and conflicting values are **synthetic teaching
perturbations**. They are declared one by one in
`source/synthetic-perturbations.csv`; they must never be cited as facts about
the 1925 issue.

## Suggested low-threshold route

1. Open the PDF and read the two page descriptions in `RIGHTS.md`.
2. Inspect `raw/messy-records.csv`. Mark observation, provider metadata,
   inference, and synthetic disturbance in different notes or columns.
3. Compare the printed captions with `source/source-records.csv`. Do not
   resolve a person, date, or place merely because a candidate looks
   plausible.
4. Compare `raw/provider-ocr.txt` with
   `cleaned/gold-transcription.txt`. Classify at least five errors and note
   which ones would change search, counting, or interpretation.
5. Consult `cleaned/decisions.csv`, then compare your result with
   `cleaned/records.csv`.
6. Read the counts in `output/`. Explain why a single CER or WER is not an
   interpretation of the document or a guarantee about the rest of the
   issue.

No command line is required for the student exercise. Instructors and
maintainers can rebuild every derived CSV and checksum with:

```text
make archival-friction-packet
```

The builder uses only the Python standard library. It does not download or
replace the committed source scan.

## Accessible page descriptions

**Page 1.** A grayscale illustrated front page headed *Ilustrirani
Slovenec*. A large political cartoon sits above photographs of a crowd
outside Ljubljana's Hotel Union, the Ljubljanica riverbed, and four named
men. Captions frame the images in openly partisan language.

**Page 2.** A grayscale montage headed “Iz razpuščene narodne skupščine”. It
contains a group portrait of German deputies, photographs of Ljubljana, and
street scenes labelled as German and American election campaigns. Dense
captions and uneven columns make the provider OCR's reading order unstable.

## Ethical use

The issue is a partisan historical publication. Its descriptions of people
and political groups are evidence of the publication's rhetoric, not neutral
descriptions endorsed by this handbook. Keep the image, caption, provider
OCR, researcher transcription, and later authority claims distinguishable.
The sample contains no contemporary personal data.
