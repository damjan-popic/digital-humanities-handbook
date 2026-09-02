# Rights and provenance audit

## Authentic source

- **Object:** *Ilustrirani Slovenec*, year 1, issue 7, 7 February 1925,
  two-page illustrated supplement to *Slovenec* no. 30.
- **Committed source:** `source/ilustrirani-slovenec-1925-02-07.pdf`.
- **Wikimedia Commons record:**
  <https://commons.wikimedia.org/wiki/File:Ilustrirani_Slovenec_1925-02-07.pdf>.
- **Original-file URL:**
  <https://upload.wikimedia.org/wikipedia/commons/9/99/Ilustrirani_Slovenec_1925-02-07.pdf>.
- **Digital Library of Slovenia reference:** `YPI8OFSU`, as reported in the
  Commons source record.
- **Publisher in the provider record:** Fran Kulovec (1884–1941).
- **Provider rights statement:** public domain; `Copyrighted: False`.
- **Access and download date:** 2 September 2026.
- **Downloaded-file SHA-256:**
  `e7b4b9f27f2043f2a3861b6cf05e1b4d8e1053e16eb81bf05f96d21385b5ad79`.

Wikimedia Commons hosts the scan, attributes the source to the Digital
Library of Slovenia and marks the file as public domain. The provider record
is preserved in `source/commons-source.json`. The committed PDF has not been
cropped, recompressed, annotated or otherwise altered after download. Its
two pages are the only facsimile material included.

The PDF contains an ABBYY FineReader 9.0 text layer. The packet preserves a
short excerpt of that machine-produced text in `source/provider-ocr.txt` and
`raw/provider-ocr.txt`. Provider OCR is not represented as a human or
diplomatic transcription.

## Handbook-created material

The selected eight source-grounded records, checked reference transcription,
correction decisions, evaluation results, descriptions and instructional
prose were created for this handbook. Repository text and original
annotations are licensed CC BY 4.0; original code is MIT licensed, following
the repository licences.

No third-party screenshot is included. Page descriptions in `README.md` are
original accessibility text, not a substitute for the historical source.

## Synthetic perturbations

Four teaching disturbances are declared in
`source/synthetic-perturbations.csv`:

1. `AF-SYN-001` changes capitalization in the Ljubljana caption;
2. `AF-SYN-002` changes the printed form “Meker” to “Meeker”;
3. `AF-SYN-003` inserts the unsupported authority candidate “Ezra Meeker”;
4. `AF-SYN-004` adds record `AF-P1-002-DUP` as a duplicate of `AF-P1-002`.

They are generated only in raw and interim teaching layers, marked
`synthetic=true`, and reversed or excluded through `correction-log.csv`.
They are not historical text, provider metadata, archival damage or evidence
about the 1925 publication.

## Reuse decision

The public-domain facsimile and handbook-created CC BY/MIT material may be
redistributed with the source and repository notices retained. Reusers
should still preserve the provider attribution, distinguish the publication's
polemical captions from neutral description, and reconsider privacy or
contextual-harm risks before applying this workflow to other collections.

The identity suggested for “Mr. Meker” remains unresolved. Public-domain
status does not make an unsupported authority match acceptable.
