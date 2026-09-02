# Expected observations

These are checkable properties of packet version 1, not model answers to the
historical research prompt.

## Source and rights

- The source PDF has two pages and SHA-256
  `e7b4b9f27f2043f2a3861b6cf05e1b4d8e1053e16eb81bf05f96d21385b5ad79`.
- The provider record names the Digital Library of Slovenia source and marks
  the scan as public domain.
- The facsimile remains unchanged; all four synthetic disturbances are
  declared separately and occur only in derived teaching data.

## Records and decisions

- `source/source-records.csv` and `metadata-clean.csv` each contain eight
  records with unique stable identifiers.
- `metadata-raw.csv` contains nine rows: the eight source identifiers plus
  synthetic record `AF-P1-002-DUP`.
- Four synthetic interventions are declared, appear in the interim queue and
  have four corresponding correction decisions.
- The clean layer restores the capitalization in `AF-P1-001`, restores the
  printed “Mr. Meker” form in `AF-P2-003`, removes the unsupported authority
  candidate and excludes only the declared synthetic duplicate.
- Six entries remain in `unresolved-cases.csv`: five identity or unit cases
  and one approximate date. Their presence is expected.
- “Mr. Meker” is not linked to Ezra Meeker. The packet contains a plausible
  candidate but no independent identity evidence.
- The normalized date `1925-02-01` is derived from the issue date and the
  printed relative expression. The normalized value `1925` for the riverbed
  photograph is approximate, not an exact creation date.

## OCR/HTR evaluation

- Sample `AF-OCR-P1-INTRO` uses Unicode NFC, removes surrounding whitespace
  and uses Unicode whitespace for word tokenization.
- The checked reference has 591 characters and 93 words under those rules.
- Minimum edit alignment gives 15 character edits and 9 word edits.
- CER is `0.025381`; WER is `0.096774` when rounded to six decimal places.
- These values describe one selected OCR passage. They do not measure the
  complete issue, the publication, HTR, Wikimedia Commons, dLib.si or ABBYY
  FineReader in general.

## Interpretive limits

- The captions are partisan statements by the publication, not neutral
  subject headings endorsed by the handbook.
- Article boundaries, complete reading order and untranscribed regions have
  not been evaluated.
- A search miss in the provider OCR can result from recognition error and is
  not automatically evidence that the historical source omits a person or
  term.
- Different defensible transcription or tokenization rules can produce
  different CER and WER values; the rule must travel with the score.
