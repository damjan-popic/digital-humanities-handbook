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

## Public rebuild

The ordinary website environment does not include authoring libraries. From a clean checkout, create and activate a Python 3.12 virtual environment, then run:

```text
python -m pip install -r requirements-authoring.txt
make scholarly-work-samples
```

The separate, pinned authoring requirements contain `python-docx`, Pillow and their direct runtime dependencies for DOCX/ODT fixtures, `openpyxl` and `et-xmlfile` for XLSX, and `pdf2image` for optional page-image inspection. ZIP packaging and structural checks use the Python standard library. Visual DOCX rendering additionally needs publicly available LibreOffice and Poppler executables; structural validation does not. The command regenerates the two DOCX files, the ODT file, the XLSX workbook, `MANIFEST.sha256`, the versioned ZIP and its adjacent `.sha256` digest. `make check` then verifies the package byte-for-byte and audits document/workbook structure without requiring Word, LibreOffice or Excel.

## Suggested sequence

1. Import and correct `source/zotero-five-records.ris`.
2. Build an argument from `source/reading-notes.md` and compare it with the three writing outputs.
3. Open `output/structured-paper.docx` in Word or LibreOffice Writer; update fields and inspect its structure. The `.odt` copy tests exchange between editors.
4. Import the raw CSV into Excel, reproduce the cleaning decisions, and compare the result with the cleaned CSV and workbook.
5. Regenerate a PivotTable and chart, then compare their totals with the validation layer.

When you perform the exercise, import `record_id` as Text in Power Query. The fixture stores these identifiers as text, including `00009`; verify them after every transformation.

Keep the working document with active Zotero fields as the master. Follow the venue or publisher's delivery instructions. If a static submission is required, unlink citations only in a separately named and backed-up final submission copy—never in the working master and never merely to repair formatting.

See `RIGHTS.md` for rights and provenance.
