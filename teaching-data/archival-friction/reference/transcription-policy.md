# Reference-transcription policy

The sample covers the masthead line, title and introductory paragraph at the
top of PDF page 1. `source/provider-ocr.txt` is the byte-preserved dLib TXT
export: 5,710 bytes with CRLF line endings and SHA-256
`ab4e9e5464eb349d4c27b3b895c2b98b3a6509f3ce4be76f387b739a1fcee456`.
The builder decodes it as Windows-1250, selects source lines 1–4, joins lines
1–2 as the masthead, retains lines 3 and 4 as the title and paragraph, applies
Unicode NFC and collapses whitespace runs within those three comparison
lines. The resulting UTF-8 derivative is `raw/provider-ocr.txt`; AF-ED-009
records this source-grounded selection and normalization decision.

`reference/reference-transcription.txt` is a handbook-created, manually
checked transcription: it follows the visible print, retains historical
wording and punctuation, joins only line-break hyphenation and does not
modernize spelling.

The transcription is a documented reference, not unmediated “ground truth”.
Character alignment uses Unicode NFC and includes internal whitespace. Word
alignment splits on Unicode whitespace. When minimum-cost alignments tie, the
deterministic order is match, substitution, deletion, then insertion.

The sample is intentionally small. CER, WER and the detailed error audit
begin after the declared extraction and whitespace normalization. They do
not measure omitted layout-whitespace behaviour and describe only these
lines; they must not be generalized to the whole page, issue, title or
collection.
