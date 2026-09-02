# Scholarly-work foundations sample pack

Version: 1.0 (2 September 2026)

This small, original teaching corpus supports the paired scholarly-work workflows in the handbook. It models a fictional catalogue of digitized postcards; it is not a historical dataset and must not be cited as evidence about real collections.

## Layer map

- `source/` contains reading notes, a five-record RIS import and a persistent-identifier exercise.
- `raw/` contains the immutable messy table and a separate place lookup.
- `cleaned/` contains one documented interpretation of the raw table.
- `output/` contains model writing, document and spreadsheet outputs.
- `validation/` records independent checks and expected totals.
- `known-problems/` preserves deliberate writing and data faults for practice.
- `citation-style-audit/` is a compact audit trail for a notes-and-bibliography style.

Start with a copy of this directory or the versioned ZIP. Never overwrite `raw/postcards-messy.csv`. The model outputs are answers to inspect, challenge and reproduce, not substitutes for recording your own decisions.

## Suggested sequence

1. Import and correct `source/zotero-five-records.ris`.
2. Build an argument from `source/reading-notes.md` and compare it with the three writing outputs.
3. Open `output/structured-paper.docx` in Word or LibreOffice Writer; update fields and inspect its structure. The `.odt` copy tests exchange between editors.
4. Import the raw CSV into Excel, reproduce the cleaning decisions, and compare the result with the cleaned CSV and workbook.
5. Regenerate a PivotTable and chart, then compare their totals with the validation layer.

The workbook's Raw and Cleaned identifier cells use text-returning `TEXT` formulas only to preserve five-character cached values in the portable generated XLSX. When you perform the exercise, import `record_id` as Text in Power Query; do not substitute these fixture formulas for the documented transformation.

See `RIGHTS.md` for rights and provenance.
