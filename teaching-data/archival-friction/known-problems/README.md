# Known problems and unresolved questions

- The PDF text layer was created with ABBYY FineReader 9.0. Dense columns,
  display type, and image captions disrupt reading order.
- The gold transcription was checked against the committed facsimile but is
  not a complete diplomatic edition. It does not encode typeface, column
  geometry, or illustrations.
- Dates inferred from “this month” or “this year” depend on the issue date.
  Photograph creation dates remain unknown unless the caption states one.
- The issue is a partisan publication. Its labels and political claims
  cannot be imported as neutral subject metadata.
- “Mr. Meker” may invite an authority match, but this packet supplies no
  independent evidence sufficient to accept one. The clean table therefore
  leaves the authority candidate blank.
- The synthetic duplicate and metadata conflicts are teaching devices, not
  source facts. Their identifiers all begin with `AF-SYN-` or end with
  `-DUP`, and every affected raw row is marked `synthetic=true`.
- CER and WER depend on the declared transcription policy, Unicode
  normalization, tokenization, and the chosen excerpt. A different defensible
  policy can produce a different score.
