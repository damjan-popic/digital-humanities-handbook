#!/usr/bin/env node
/**
 * Build the original Excel teaching fixture for issue #20.
 *
 * This is an optional reproducibility aid; JavaScript is not a course
 * requirement. Generated data are CC BY 4.0 and this build code is MIT.
 */

import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";

const moduleLocation = process.env.CODEX_ARTIFACT_TOOL_MODULE;
if (!moduleLocation) {
  throw new Error("Set CODEX_ARTIFACT_TOOL_MODULE to the managed artifact-tool module.");
}
const moduleUrl = moduleLocation.startsWith("file:")
  ? moduleLocation
  : pathToFileURL(moduleLocation).href;
const { SpreadsheetFile, Workbook } = await import(moduleUrl);

const args = process.argv.slice(2);
const rootIndex = args.indexOf("--repo-root");
if (rootIndex < 0 || !args[rootIndex + 1]) {
  throw new Error("Usage: build_scholarly_work_workbook.mjs --repo-root <path>");
}
const repoRoot = path.resolve(args[rootIndex + 1]);
const sampleRoot = path.join(repoRoot, "examples", "scholarly-work-foundations");
const outputPath = path.join(sampleRoot, "output", "scholarly-data-workbook.xlsx");
const qaDir = path.join(repoRoot, ".codex-tmp", "issue-20-workbook");

function parseDelimited(text, delimiter) {
  const rows = [];
  let row = [];
  let field = "";
  let quoted = false;
  for (let i = 0; i < text.length; i += 1) {
    const char = text[i];
    if (char === '"') {
      if (quoted && text[i + 1] === '"') {
        field += '"';
        i += 1;
      } else {
        quoted = !quoted;
      }
    } else if (char === delimiter && !quoted) {
      row.push(field);
      field = "";
    } else if ((char === "\n" || char === "\r") && !quoted) {
      if (char === "\r" && text[i + 1] === "\n") i += 1;
      row.push(field);
      if (row.some((value) => value !== "")) rows.push(row);
      row = [];
      field = "";
    } else {
      field += char;
    }
  }
  if (field !== "" || row.length) {
    row.push(field);
    rows.push(row);
  }
  return rows;
}

function columnName(index) {
  let result = "";
  let value = index;
  while (value > 0) {
    value -= 1;
    result = String.fromCharCode(65 + (value % 26)) + result;
    value = Math.floor(value / 26);
  }
  return result;
}

function endCell(rows) {
  return `${columnName(rows[0].length)}${rows.length + 3}`;
}

function identifierFormula(value) {
  if (/^\d+$/.test(value)) {
    return `=TEXT(${Number(value)},"00000")`;
  }
  return `="${value.replaceAll('"', '""')}"`;
}

const palette = {
  navy: "#17324D",
  blue: "#2F75B5",
  paleBlue: "#DCEAF7",
  paleGray: "#F3F5F7",
  grid: "#CBD3DA",
  ink: "#1F2933",
  muted: "#5D6874",
  white: "#FFFFFF",
  amber: "#FFF2CC",
  amberText: "#7A5200",
  green: "#E2F0D9",
  greenText: "#215E21",
  red: "#FCE4D6",
  redText: "#9C0006",
};

function addTitle(sheet, lastColumn, title, note) {
  const titleRange = sheet.getRange(`A1:${lastColumn}1`);
  titleRange.merge();
  titleRange.values = [[title]];
  titleRange.format = {
    fill: palette.navy,
    font: { bold: true, color: palette.white, size: 16 },
    verticalAlignment: "center",
  };
  titleRange.format.rowHeight = 28;

  const noteRange = sheet.getRange(`A2:${lastColumn}2`);
  noteRange.merge();
  noteRange.values = [[note]];
  noteRange.format = {
    fill: palette.paleBlue,
    font: { color: palette.navy, italic: true, size: 10 },
    wrapText: true,
    verticalAlignment: "center",
  };
  noteRange.format.rowHeight = 34;
  sheet.showGridLines = false;
}

function styleTable(sheet, rangeAddress) {
  const range = sheet.getRange(rangeAddress);
  range.format.borders = { preset: "all", style: "thin", color: palette.grid };
  range.format.verticalAlignment = "center";
  const header = range.getRow(0);
  header.format = {
    fill: palette.blue,
    font: { bold: true, color: palette.white },
    wrapText: true,
    verticalAlignment: "center",
  };
  header.format.rowHeight = 32;
}

function setWidths(sheet, widths) {
  widths.forEach((width, index) => {
    const col = columnName(index + 1);
    sheet.getRange(`${col}:${col}`).format.columnWidth = width;
  });
}

const rawText = await fs.readFile(path.join(sampleRoot, "raw", "postcards-messy.csv"), "utf8");
const lookupText = await fs.readFile(path.join(sampleRoot, "raw", "place-lookup.csv"), "utf8");
const cleanedText = await fs.readFile(path.join(sampleRoot, "cleaned", "postcards-clean.csv"), "utf8");
const rawRows = parseDelimited(rawText, ";");
const lookupRows = parseDelimited(lookupText, ",");
const cleanedRows = parseDelimited(cleanedText, ",");
const rawWorkbookRows = rawRows.map((row, rowIndex) =>
  rowIndex === 0
    ? row
    : [null, ...row.slice(1).map((value) => (value.trim() === "" ? "" : value))],
);
const cleanedWorkbookRows = cleanedRows.map((row, rowIndex) =>
  rowIndex === 0
    ? row
    : row.map((value, columnIndex) =>
        columnIndex === 0 ? null : value,
      ),
);

const workbook = Workbook.create();
const readme = workbook.worksheets.add("README");
const raw = workbook.worksheets.add("Raw");
const lookup = workbook.worksheets.add("Lookup");
const cleaned = workbook.worksheets.add("Cleaned");
const transform = workbook.worksheets.add("Transform Log");
const pivot = workbook.worksheets.add("Pivot Check");
const chartData = workbook.worksheets.add("Chart Data");
const validation = workbook.worksheets.add("Validation");
const problems = workbook.worksheets.add("Known Problems");

addTitle(
  readme,
  "H",
  "Scholarly-data teaching workbook",
  "Version 1.0 • Original fictional teaching data • CC BY 4.0 • 2 September 2026",
);
readme.getRange("A4:B13").values = [
  ["Purpose", "Practice controlled Excel import, repeatable Power Query transformations, PivotTables, validation and transparent charting."],
  ["Research question", "How do documented normalization choices change what this small fictional catalogue allows us to compare?"],
  ["Start", "Import raw/postcards-messy.csv into a copy. Preserve Raw and record every type and exclusion decision."],
  ["Raw", "Ten unchanged source rows, including one exact duplicate and one test record."],
  ["Cleaned", "Eight accepted rows with source fields, normalized fields, status columns and validation notes."],
  ["Pivot Check", "Formula-backed expected counts. Create your own native PivotTable from Cleaned and compare it here."],
  ["Chart Data", "Formula-linked helper range and a native chart with an explicit denominator and source note."],
  ["Validation", "Independent totals and known-value checks. Formula cells are intentionally visible."],
  ["Interface boundary", "Excel and Power Query labels vary by platform, locale and version. The scholarly outputs and checks are the stable requirement."],
  ["Identifier fixture", "Raw and Cleaned IDs use text-returning TEXT formulas only to preserve five-character cached values in this generated XLSX. In your own import, set record_id to Text instead."],
];
styleTable(readme, "A4:B13");
readme.getRange("A4:A13").format.font = { bold: true, color: palette.navy };
readme.getRange("B4:B13").format.wrapText = true;
setWidths(readme, [22, 88]);
readme.freezePanes.freezeRows(3);

addTitle(
  raw,
  "I",
  "Raw — immutable import layer",
  "Do not edit these ten records. Re-import from raw/postcards-messy.csv when testing delimiter, encoding, identifier and locale settings.",
);
raw.getRange("A5:I14").format.numberFormat = "@";
raw.getRange(`A4:${endCell(rawRows)}`).values = rawWorkbookRows;
raw.getRange("A5:A14").formulas = rawRows.slice(1).map((row) => [identifierFormula(row[0])]);
styleTable(raw, `A4:${endCell(rawRows)}`);
raw.getRange("A5:I14").format.wrapText = true;
raw.tables.add(`A4:${endCell(rawRows)}`, true, "RawRecords");
setWidths(raw, [15, 34, 22, 24, 16, 17, 13, 17, 38]);
raw.freezePanes.freezeRows(4);

addTitle(
  lookup,
  "D",
  "Lookup — reviewed place-name mapping",
  "The lookup preserves each source label. Reviewed grouping values support this exercise; they are not a universal authority file.",
);
lookup.getRange(`A4:${endCell(lookupRows)}`).values = lookupRows;
styleTable(lookup, `A4:${endCell(lookupRows)}`);
lookup.getRange(`A5:D${lookupRows.length + 3}`).format.wrapText = true;
lookup.tables.add(`A4:${endCell(lookupRows)}`, true, "PlaceLookup");
setWidths(lookup, [28, 25, 16, 68]);
lookup.freezePanes.freezeRows(4);

addTitle(
  cleaned,
  "O",
  "Cleaned — documented analytical layer",
  "One defensible interpretation for the stated exercise. Keep source expressions beside normalized values and leave uncertainty visible.",
);
cleaned.getRange("A5:A12").format.numberFormat = "@";
cleaned.getRange(`A4:${endCell(cleanedRows)}`).values = cleanedWorkbookRows;
cleaned.getRange("A5:A12").formulas = cleanedRows.slice(1).map((row) => [identifierFormula(row[0])]);
styleTable(cleaned, `A4:${endCell(cleanedRows)}`);
cleaned.getRange("L5:L12").format.numberFormat = "0";
cleaned.getRange("A5:O12").format.wrapText = true;
cleaned.getRange("G5:G12").dataValidation = {
  rule: { type: "list", values: ["photograph", "postcard", "unknown"] },
};
cleaned.getRange("K5:K12").dataValidation = {
  rule: { type: "list", values: ["valid", "approximate", "uncertain", "invalid", "missing"] },
};
cleaned.tables.add(`A4:${endCell(cleanedRows)}`, true, "CleanedRecords");
setWidths(cleaned, [14, 34, 18, 18, 25, 20, 20, 16, 15, 14, 14, 12, 23, 16, 42]);
cleaned.freezePanes.freezeRows(4);
cleaned.freezePanes.freezeColumns(1);

addTitle(
  transform,
  "F",
  "Transform log — Power Query recipe and scholarly rationale",
  "Recreate these operations in Power Query. Applied Steps make the recipe repeatable; the reason and check columns make it auditable.",
);
const transformRows = [
  ["Step", "Operation", "Fields", "Reason", "Check", "Failure mode"],
  [1, "Import UTF-8 semicolon-delimited text", "all", "Preserve characters and columns", "9 columns; 10 data rows", "comma chosen as delimiter"],
  [2, "Set record_id to text before load", "record_id", "Keep leading zeros", "00009 remains five characters", "automatic whole-number type"],
  [3, "Trim outer whitespace", "title, place_raw, object_type", "Remove layout noise", "00101 title/place have no outer spaces", "source file overwritten"],
  [4, "Filter explicit test identifier", "record_id", "Exclude non-collection calibration row", "TEST-01 absent; exclusion logged", "unexplained row deletion"],
  [5, "Remove one exact duplicate", "all", "Prevent double count", "one 00105 remains", "both duplicates removed"],
  [6, "Map object-type variants", "object_type", "Support stated comparison", "3 photograph, 4 postcard, 1 unknown", "blank silently dropped"],
  [7, "Merge place lookup; retain source", "place_raw", "Group reviewed variants without erasure", "Laibach source remains; grouping is Ljubljana", "unmatched rows discarded"],
  [8, "Parse views using documented convention", "views", "Create numeric measure", "00101=1204; 00103=1125; blank stays blank", "locale coercion changes values"],
  [9, "Parse dates into value, precision and status", "date_raw", "Avoid invented precision", "00106 invalid and blank ISO", "invalid date coerced"],
  [10, "Load to Cleaned table", "all", "Separate analytical layer", "8 rows and 15 fields", "raw and cleaned mixed"],
];
transform.getRange("A4:F14").values = transformRows;
styleTable(transform, "A4:F14");
transform.getRange("A5:F14").format.wrapText = true;
transform.tables.add("A4:F14", true, "TransformationLog");
setWidths(transform, [9, 35, 24, 45, 44, 38]);
transform.freezePanes.freezeRows(4);

addTitle(
  pivot,
  "D",
  "Pivot check — expected summary",
  "Create a native PivotTable from Cleaned with object_type_normalized in Rows and record_id in Values (Count). Compare it with these formula-backed checks.",
);
pivot.getRange("A4:D8").values = [
  ["object_type_normalized", "Formula count", "Share", "Independent manual count"],
  ["photograph", null, null, 3],
  ["postcard", null, null, 4],
  ["unknown", null, null, 1],
  ["Total", null, null, 8],
];
pivot.getRange("B5").formulas = [["=COUNTIF('Cleaned'!$G$5:$G$12,A5)"]];
pivot.getRange("B5:B7").fillDown();
pivot.getRange("B8").formulas = [["=SUM(B5:B7)"]];
pivot.getRange("C5").formulas = [["=B5/$B$8"]];
pivot.getRange("C5:C7").fillDown();
pivot.getRange("C8").formulas = [["=SUM(C5:C7)"]];
pivot.getRange("C5:C8").format.numberFormat = "0.0%";
styleTable(pivot, "A4:D8");
pivot.getRange("A8:D8").format = {
  fill: palette.paleBlue,
  font: { bold: true, color: palette.navy },
  borders: { preset: "doubleBottom", style: "medium", color: palette.blue },
};
pivot.getRange("A10:D11").merge(true);
pivot.getRange("A10:A11").values = [
  ["Interpretation check: this summary describes eight retained fictional records. It does not measure a real collection. Unknown is retained in the denominator."],
  ["Refresh test: add one controlled row to a copy of the raw CSV, refresh your query and PivotTable, and confirm that exactly one category count and the total increase by one."],
];
pivot.getRange("A10:D11").format = { fill: palette.amber, font: { color: palette.amberText }, wrapText: true };
pivot.getRange("A10:D11").format.rowHeight = 36;
setWidths(pivot, [28, 19, 16, 28]);
pivot.freezePanes.freezeRows(4);

addTitle(
  chartData,
  "I",
  "Chart data — formula-linked and transparent",
  "The chart reads from formulas linked to Pivot Check. Keep the denominator, category definition, exclusions and source visible beside any exported chart.",
);
chartData.getRange("A4:B7").values = [
  ["Normalized object type", "Record count"],
  ["photograph", null],
  ["postcard", null],
  ["unknown", null],
];
chartData.getRange("B5").formulas = [["='Pivot Check'!B5"]];
chartData.getRange("B5:B7").fillDown();
styleTable(chartData, "A4:B7");
chartData.getRange("A9:C11").merge(true);
chartData.getRange("A9:A11").values = [
  ["Caption: Retained fictional catalogue records by normalized object type (n = 8)."],
  ["Source: Digital Humanities Handbook, Fictional Postcard Catalogue Teaching Dataset, version 1.0."],
  ["Transformations/exclusions: source labels mapped to two categories plus unknown; one exact duplicate and TEST-01 excluded."],
];
chartData.getRange("A9:C11").format = { fill: palette.paleGray, font: { color: palette.muted, italic: true }, wrapText: true };
chartData.getRange("A9:C9").format.rowHeight = 36;
chartData.getRange("A10:C10").format.rowHeight = 48;
chartData.getRange("A11:C11").format.rowHeight = 54;
const chart = chartData.charts.add("bar", chartData.getRange("A4:B7"));
chart.title = "Normalized object types (n = 8)";
chart.hasLegend = false;
chart.xAxis = { axisType: "textAxis" };
chart.xAxis.title.text = "Normalized object type";
chart.yAxis = { min: 0, max: 5, numberFormatCode: "0" };
chart.yAxis.title.text = "Retained records";
chart.setPosition("D4", "I18");
setWidths(chartData, [28, 18, 4, 16, 16, 16, 16, 16, 16]);
chartData.freezePanes.freezeRows(4);

addTitle(
  validation,
  "D",
  "Validation — independent checks",
  "Expected values were counted independently from the raw identifiers. Formula cells point only to the cleaned and summary layers.",
);
validation.getRange("A4:D11").values = [
  ["Check", "Expected", "Calculated", "Status"],
  ["Accepted rows", 8, null, null],
  ["Pivot total", 8, null, null],
  ["Unknown categories", 1, null, null],
  ["Leading-zero ID retained", 1, null, null],
  ["Invalid dates flagged", 1, null, null],
  ["Missing view values", 1, null, null],
  ["Category shares sum", 1, null, null],
];
const checks = [
  "=COUNTA('Cleaned'!A5:A12)",
  "=SUM('Pivot Check'!B5:B7)",
  '=COUNTIF(\'Cleaned\'!G5:G12,"unknown")',
  '=COUNTIF(\'Cleaned\'!A5:A12,"00009")',
  '=COUNTIF(\'Cleaned\'!K5:K12,"invalid")',
  "=COUNTBLANK('Cleaned'!L5:L12)",
  "=SUM('Pivot Check'!C5:C7)",
];
validation.getRange("C5:C11").formulas = checks.map((formula) => [formula]);
validation.getRange("D5").formulas = [["=IF(ABS(B5-C5)<0.0001,\"PASS\",\"CHECK\")"]];
validation.getRange("D5:D11").fillDown();
validation.getRange("B11:C11").format.numberFormat = "0.0%";
styleTable(validation, "A4:D11");
validation.getRange("D5:D11").conditionalFormats.add("containsText", {
  text: "PASS",
  format: { fill: palette.green, font: { color: palette.greenText, bold: true } },
});
validation.getRange("D5:D11").conditionalFormats.add("containsText", {
  text: "CHECK",
  format: { fill: palette.red, font: { color: palette.redText, bold: true } },
});
setWidths(validation, [34, 18, 18, 16]);
validation.freezePanes.freezeRows(4);

addTitle(
  problems,
  "D",
  "Known problems — deliberate traps",
  "Use this sheet to test import and cleaning decisions. A successful workflow preserves evidence and records uncertainty rather than merely producing a tidy table.",
);
const problemRows = [
  ["Problem", "Where", "Required response", "Do not do"],
  ["Leading zeros", "record_id 00009", "Import identifier as text", "Convert it to 9"],
  ["Exact duplicate", "second 00105", "Exclude once and log the rule", "Delete both rows"],
  ["Test row", "TEST-01", "Filter through an explicit step", "Delete from raw file"],
  ["Locale-sensitive numbers", "1.204 and 1 125", "Apply the documented source convention and test known values", "Trust automatic detection"],
  ["Mixed date precision", "date_raw", "Separate display, normalized value, precision and status", "Invent missing days"],
  ["Impossible date", "00106", "Flag invalid and leave ISO date blank", "Silently coerce"],
  ["Missing values", "creator, views, type, date", "Keep missingness explicit", "Replace with zero or guesses"],
  ["Historical/bilingual places", "Laibach; Koper / Capodistria", "Retain source form beside reviewed grouping", "Erase the source wording"],
];
problems.getRange("A4:D12").values = problemRows;
styleTable(problems, "A4:D12");
problems.getRange("A5:D12").format.wrapText = true;
problems.tables.add("A4:D12", true, "KnownProblems");
setWidths(problems, [31, 31, 58, 40]);
problems.freezePanes.freezeRows(4);

await fs.mkdir(path.dirname(outputPath), { recursive: true });
await fs.mkdir(qaDir, { recursive: true });

const summary = await workbook.inspect({
  kind: "workbook,sheet,drawing",
  maxChars: 5000,
});
console.log(summary.ndjson ?? summary);

const validationInspect = await workbook.inspect({
  kind: "region,formula",
  sheetId: "Validation",
  range: "A4:D11",
  maxChars: 5000,
});
console.log(validationInspect.ndjson ?? validationInspect);

for (const sheetName of [
  "README",
  "Raw",
  "Lookup",
  "Cleaned",
  "Transform Log",
  "Pivot Check",
  "Chart Data",
  "Validation",
  "Known Problems",
]) {
  const preview = await workbook.render({
    sheetName,
    autoCrop: "all",
    scale: 1,
    format: "png",
  });
  const safeName = sheetName.toLowerCase().replaceAll(" ", "-");
  await fs.writeFile(
    path.join(qaDir, `${safeName}.png`),
    new Uint8Array(await preview.arrayBuffer()),
  );
}

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);
await fs.rm(`${outputPath}.inspect.ndjson`, { force: true });
console.log(`Wrote ${outputPath}`);
console.log(`Rendered worksheet previews to ${qaDir}`);
