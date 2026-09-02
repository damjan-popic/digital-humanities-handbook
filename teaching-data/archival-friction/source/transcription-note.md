# OCR sample locator and transcription policy

The sample covers the masthead line, title, and introductory paragraph at
the top of PDF page 1. `provider-ocr.txt` preserves the text extracted from
the PDF's ABBYY FineReader 9.0 text layer, apart from removing repeated
layout whitespace. `gold-transcription.txt` follows the visible print,
retains historical wording and punctuation, joins only line-break
hyphenation, and does not modernise spelling.

The sample is intentionally small. Its CER and WER describe only these
lines; they must not be generalized to the whole page, issue, title, or
collection.
