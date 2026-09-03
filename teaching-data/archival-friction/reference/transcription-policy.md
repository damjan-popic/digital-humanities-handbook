# Reference-transcription policy

The sample covers the masthead line, title and introductory paragraph at the
top of PDF page 1. `source/provider-ocr.txt` preserves text from the PDF's
ABBYY FineReader 9.0 layer apart from collapsed layout whitespace.
`reference/reference-transcription.txt` is a handbook-created, manually
checked transcription: it follows the visible print, retains historical
wording and punctuation, joins only line-break hyphenation and does not
modernize spelling.

The transcription is a documented reference, not unmediated “ground truth”.
Character alignment uses Unicode NFC and includes internal whitespace. Word
alignment splits on Unicode whitespace. When minimum-cost alignments tie, the
deterministic order is match, substitution, deletion, then insertion.

The sample is intentionally small. CER, WER and the detailed error audit
describe only these lines; they must not be generalized to the whole page,
issue, title or collection.
