#!/usr/bin/env python3
"""Audit freshness and structure of the public issue #20 sample artefacts."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET
from zipfile import ZIP_STORED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
SAMPLE_ROOT = ROOT / "examples" / "scholarly-work-foundations"
MANIFEST_PATH = SAMPLE_ROOT / "MANIFEST.sha256"
ZIP_PATH = ROOT / "docs" / "assets" / "downloads" / "scholarly-work-foundations-v1.zip"
ZIP_DIGEST_PATH = ZIP_PATH.with_suffix(ZIP_PATH.suffix + ".sha256")
PREFIX = "scholarly-work-foundations/"
FIXED_DATE = (2026, 9, 2, 0, 0, 0)

NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS_CP = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
NS_DC = "http://purl.org/dc/elements/1.1/"
NS_DCTERMS = "http://purl.org/dc/terms/"
NS_MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
NS_REL_DOC = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_REL_PKG = "http://schemas.openxmlformats.org/package/2006/relationships"
NS_OFFICE = "urn:oasis:names:tc:opendocument:xmlns:office:1.0"
NS_TEXT = "urn:oasis:names:tc:opendocument:xmlns:text:1.0"
NS_TABLE = "urn:oasis:names:tc:opendocument:xmlns:table:1.0"
NS_SVG = "urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0"

W = f"{{{NS_W}}}"
MAIN = f"{{{NS_MAIN}}}"

GENERATED = {
    "output/structured-paper.docx",
    "output/structured-paper.odt",
    "output/scholarly-data-workbook.xlsx",
    "citation-style-audit/generated-bibliography.docx",
    "MANIFEST.sha256",
}


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def fail(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def visible_sample_files(*, include_manifest: bool) -> dict[str, Path]:
    result = {}
    for path in SAMPLE_ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(SAMPLE_ROOT).as_posix()
        if relative.startswith(".") or relative.endswith(".inspect.ndjson"):
            continue
        if not include_manifest and relative == "MANIFEST.sha256":
            continue
        result[relative] = path
    return result


def check_manifest_and_zip(failures: list[str]) -> None:
    fail(MANIFEST_PATH.exists(), "missing examples/scholarly-work-foundations/MANIFEST.sha256", failures)
    fail(ZIP_PATH.exists(), "missing stable scholarly-work ZIP", failures)
    fail(ZIP_DIGEST_PATH.exists(), "missing checked ZIP SHA-256 file", failures)
    if failures:
        return

    source_without_manifest = visible_sample_files(include_manifest=False)
    parsed: dict[str, str] = {}
    pattern = re.compile(r"^([0-9a-f]{64})  ([^\r\n]+)$")
    for line_number, line in enumerate(MANIFEST_PATH.read_text(encoding="utf-8").splitlines(), start=1):
        match = pattern.fullmatch(line)
        if not match:
            failures.append(f"MANIFEST.sha256:{line_number}: malformed line")
            continue
        digest, relative = match.groups()
        if relative in parsed:
            failures.append(f"MANIFEST.sha256: duplicate member {relative}")
        parsed[relative] = digest
    fail(set(parsed) == set(source_without_manifest), "MANIFEST.sha256 member list differs from the source tree", failures)
    for relative, path in source_without_manifest.items():
        fail(parsed.get(relative) == sha256(path.read_bytes()), f"MANIFEST.sha256: stale digest for {relative}", failures)

    digest_match = pattern.fullmatch(ZIP_DIGEST_PATH.read_text(encoding="utf-8").strip())
    fail(bool(digest_match), f"{ZIP_DIGEST_PATH.name}: malformed digest record", failures)
    if digest_match:
        fail(digest_match.group(2) == ZIP_PATH.name, f"{ZIP_DIGEST_PATH.name}: wrong package name", failures)
        fail(digest_match.group(1) == sha256(ZIP_PATH.read_bytes()), f"{ZIP_DIGEST_PATH.name}: stale package digest", failures)

    source_with_manifest = visible_sample_files(include_manifest=True)
    with ZipFile(ZIP_PATH) as archive:
        fail(archive.testzip() is None, "stable scholarly-work ZIP has a failed CRC", failures)
        files = [entry for entry in archive.infolist() if not entry.is_dir()]
        archived = {entry.filename.removeprefix(PREFIX): entry for entry in files if entry.filename.startswith(PREFIX)}
        fail(len(archived) == len(files), "stable scholarly-work ZIP contains a member outside its package prefix", failures)
        fail(set(archived) == set(source_with_manifest), "stable scholarly-work ZIP member list differs from the source tree", failures)
        for relative, path in source_with_manifest.items():
            entry = archived.get(relative)
            if entry is None:
                continue
            fail(entry.date_time == FIXED_DATE, f"stable ZIP has a non-deterministic timestamp for {relative}", failures)
            fail(archive.read(entry) == path.read_bytes(), f"stable ZIP contains stale bytes for {relative}", failures)


def package_xml(archive: ZipFile, name: str, failures: list[str]) -> ET.Element | None:
    try:
        return ET.fromstring(archive.read(name))
    except (KeyError, ET.ParseError) as error:
        failures.append(f"{archive.filename}: cannot parse {name}: {error}")
        return None


def word_paragraph_text(paragraph: ET.Element) -> str:
    return "".join(node.text or "" for node in paragraph.findall(f".//{W}t"))


def check_docx(path: Path, *, bibliography: bool, failures: list[str]) -> None:
    with ZipFile(path) as archive:
        fail(archive.testzip() is None, f"{path.name}: failed ZIP CRC", failures)
        document = package_xml(archive, "word/document.xml", failures)
        core = package_xml(archive, "docProps/core.xml", failures)
        settings = package_xml(archive, "word/settings.xml", failures)
        if document is None or core is None or settings is None:
            return
        all_text = " ".join(word_paragraph_text(p) for p in document.findall(f".//{W}p"))
        headings = []
        for paragraph in document.findall(f".//{W}p"):
            style = paragraph.find(f"./{W}pPr/{W}pStyle")
            if style is not None and style.get(f"{W}val") in {"Heading1", "Heading2"}:
                headings.append(word_paragraph_text(paragraph))
        tables = document.findall(f".//{W}tbl")
        creator = core.findtext(f"{{{NS_DC}}}creator")
        created = core.findtext(f"{{{NS_DCTERMS}}}created")
        modified = core.findtext(f"{{{NS_DCTERMS}}}modified")
        fail(creator == "Digital Humanities Handbook", f"{path.name}: unexpected creator metadata", failures)
        fail(created == "2026-09-02T00:00:00Z", f"{path.name}: created timestamp is not fixed", failures)
        fail(modified == "2026-09-02T00:00:00Z", f"{path.name}: modified timestamp is not fixed", failures)
        fail(settings.find(f".//{W}updateFields") is not None, f"{path.name}: fields are not marked for update", failures)
        if bibliography:
            expected = {"Audit basis", "Full note", "Shortened repeat note", "Bibliography", "Field-level checks", "Unresolved case"}
            fail(expected.issubset(headings), f"{path.name}: missing audit headings", failures)
            for token in ("Eric Hayot", "Harvard College Writing Center", "Digital Humanities Handbook", "https://doi.org/10.3138/jsp.46.4.BR2"):
                fail(token in all_text, f"{path.name}: missing expected bibliography content {token!r}", failures)
            fail(len(tables) == 1, f"{path.name}: expected one audit table", failures)
            if tables:
                fail(len(tables[0].findall(f"./{W}tr")) == 5, f"{path.name}: audit table must have five rows", failures)
        else:
            expected = {
                "Contents", "Abstract", "1. Research question and claim",
                "1.1 Distinguishing description and interpretation", "2. Materials and method",
                "2.1 Data and provenance", "3. Results", "4. Discussion",
                "4.1 Claim, evidence and reasoning", "4.2 Counterargument", "4.3 Limitations",
                "5. Conclusion", "References",
            }
            fail(expected.issubset(headings), f"{path.name}: missing structured-paper headings", failures)
            field_roots = [document]
            for member in archive.namelist():
                if re.fullmatch(r"word/(?:header|footer)\d+\.xml", member):
                    root = package_xml(archive, member, failures)
                    if root is not None:
                        field_roots.append(root)
            instructions = " ".join(
                node.text or ""
                for root in field_roots
                for node in root.findall(f".//{W}instrText")
            )
            for token in ("TOC", "SEQ Table", "SEQ Figure", "REF tbl_layers", "REF fig_types", "PAGE", "NUMPAGES"):
                fail(token in instructions, f"{path.name}: missing field {token!r}", failures)
            fail(len(tables) == 1, f"{path.name}: expected one layer table", failures)
            if tables:
                fail(len(tables[0].findall(f"./{W}tr")) == 5, f"{path.name}: layer table must have five rows", failures)
            descriptions = [node.get("descr", "") for node in document.findall(".//{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}docPr")]
            fail(any("photograph 3, postcard 4, unknown 1" in value for value in descriptions), f"{path.name}: missing figure alternative description", failures)
            fail(len(document.findall(f".//{W}sectPr")) == 2, f"{path.name}: expected two document sections", failures)


def check_odt(path: Path, failures: list[str]) -> None:
    with ZipFile(path) as archive:
        fail(archive.testzip() is None, f"{path.name}: failed ZIP CRC", failures)
        entries = archive.infolist()
        fail(bool(entries) and entries[0].filename == "mimetype", f"{path.name}: mimetype is not first", failures)
        if entries:
            fail(entries[0].compress_type == ZIP_STORED, f"{path.name}: mimetype is compressed", failures)
        fail(archive.read("mimetype") == b"application/vnd.oasis.opendocument.text", f"{path.name}: wrong mimetype", failures)
        content = package_xml(archive, "content.xml", failures)
        manifest = package_xml(archive, "META-INF/manifest.xml", failures)
        package_xml(archive, "styles.xml", failures)
        package_xml(archive, "meta.xml", failures)
        package_xml(archive, "settings.xml", failures)
        if content is None or manifest is None:
            return
        headings = ["".join(node.itertext()) for node in content.findall(f".//{{{NS_TEXT}}}h")]
        for token in ("Contents", "Abstract", "1. Research question and claim", "5. Conclusion", "References"):
            fail(token in headings, f"{path.name}: missing heading {token!r}", failures)
        fail(len(content.findall(f".//{{{NS_TABLE}}}table")) == 1, f"{path.name}: expected one table", failures)
        description = " ".join("".join(node.itertext()) for node in content.findall(f".//{{{NS_SVG}}}desc"))
        fail("photograph 3, postcard 4, unknown 1" in description, f"{path.name}: missing figure alternative description", failures)
        for token in ("tbl_layers", "fig_types"):
            fail(token in ET.tostring(content, encoding="unicode"), f"{path.name}: missing reference {token!r}", failures)


def shared_strings(archive: ZipFile) -> list[str]:
    try:
        root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    return ["".join(node.itertext()) for node in root.findall(f"{MAIN}si")]


def workbook_sheets(archive: ZipFile, failures: list[str]) -> dict[str, ET.Element]:
    workbook = package_xml(archive, "xl/workbook.xml", failures)
    relationships = package_xml(archive, "xl/_rels/workbook.xml.rels", failures)
    if workbook is None or relationships is None:
        return {}
    targets = {node.get("Id"): node.get("Target") for node in relationships.findall(f"{{{NS_REL_PKG}}}Relationship")}
    result = {}
    for sheet in workbook.findall(f".//{MAIN}sheet"):
        name = sheet.get("name", "")
        target = targets.get(sheet.get(f"{{{NS_REL_DOC}}}id"), "")
        normalized = PurePosixPath("xl") / target
        if target.startswith("/"):
            normalized = PurePosixPath(target.removeprefix("/"))
        try:
            result[name] = ET.fromstring(archive.read(normalized.as_posix()))
        except (KeyError, ET.ParseError) as error:
            failures.append(f"scholarly-data-workbook.xlsx: cannot parse sheet {name}: {error}")
    return result


def sheet_cells(root: ET.Element, strings: list[str]) -> tuple[dict[str, str], dict[str, str]]:
    values: dict[str, str] = {}
    formulas: dict[str, str] = {}
    for cell in root.findall(f".//{MAIN}c"):
        reference = cell.get("r", "")
        formula = cell.findtext(f"{MAIN}f")
        if formula is not None:
            formulas[reference] = formula
        cell_type = cell.get("t")
        if cell_type == "inlineStr":
            inline = cell.find(f"{MAIN}is")
            values[reference] = "" if inline is None else "".join(inline.itertext())
        else:
            raw = cell.findtext(f"{MAIN}v", default="")
            if cell_type == "s" and raw:
                values[reference] = strings[int(raw)]
            else:
                values[reference] = raw
    return values, formulas


def check_xlsx(path: Path, failures: list[str]) -> None:
    expected_names = ["README", "Raw", "Lookup", "Cleaned", "Transform Log", "Pivot Check", "Chart Data", "Validation", "Known Problems"]
    with ZipFile(path) as archive:
        fail(archive.testzip() is None, f"{path.name}: failed ZIP CRC", failures)
        sheets = workbook_sheets(archive, failures)
        fail(list(sheets) == expected_names, f"{path.name}: unexpected sheet order {list(sheets)!r}", failures)
        strings = shared_strings(archive)
        cells = {name: sheet_cells(root, strings) for name, root in sheets.items()}
        if "Raw" in cells:
            raw_ids = [cells["Raw"][0].get(f"A{row}") for row in range(5, 15)]
            fail(raw_ids == ["00101", "00102", "00103", "00104", "00105", "00105", "00106", "TEST-01", "00107", "00009"], f"{path.name}: raw identifiers changed", failures)
        if "Cleaned" in cells:
            cleaned_ids = [cells["Cleaned"][0].get(f"A{row}") for row in range(5, 13)]
            fail(cleaned_ids == ["00101", "00102", "00103", "00104", "00105", "00106", "00107", "00009"], f"{path.name}: cleaned identifiers changed", failures)
            validations = sheets["Cleaned"].find(f".//{MAIN}dataValidations")
            fail(validations is not None and validations.get("count") == "2", f"{path.name}: expected two cleaned-sheet validations", failures)
        if "Pivot Check" in cells:
            formulas = cells["Pivot Check"][1]
            fail(formulas.get("B5") == "COUNTIF('Cleaned'!$G$5:$G$12,A5)", f"{path.name}: pivot count formula changed", failures)
            fail(formulas.get("B8") == "SUM(B5:B7)", f"{path.name}: pivot total formula changed", failures)
        if "Validation" in cells:
            formulas = cells["Validation"][1]
            fail(len([cell for cell in formulas if re.fullmatch(r"[CD](?:[5-9]|1[01])", cell)]) == 14, f"{path.name}: validation formula set is incomplete", failures)
            fail(not any("#REF!" in formula for formula in formulas.values()), f"{path.name}: formula contains #REF!", failures)
        if "Chart Data" in cells:
            values, formulas = cells["Chart Data"]
            fail("Text alternative:" in values.get("A12", ""), f"{path.name}: chart text alternative is missing", failures)
            fail(formulas.get("B5") == "'Pivot Check'!B5", f"{path.name}: chart source formula changed", failures)
        chart_names = sorted(name for name in archive.namelist() if name.startswith("xl/charts/chart") and name.endswith(".xml"))
        fail(len(chart_names) == 1, f"{path.name}: expected one native chart", failures)
        if chart_names:
            chart_text = " ".join(ET.fromstring(archive.read(chart_names[0])).itertext())
            for token in ("Normalized object types (n = 8)", "Retained records", "Normalized object type"):
                fail(token in chart_text, f"{path.name}: chart is missing {token!r}", failures)
        core = package_xml(archive, "docProps/core.xml", failures)
        if core is not None:
            fail(core.findtext(f"{{{NS_DC}}}title") == "Scholarly-data teaching workbook", f"{path.name}: title metadata changed", failures)
            fail(core.findtext(f"{{{NS_DCTERMS}}}created") == "2026-09-02T00:00:00Z", f"{path.name}: created timestamp is not fixed", failures)
            fail(core.findtext(f"{{{NS_DCTERMS}}}modified") == "2026-09-02T00:00:00Z", f"{path.name}: modified timestamp is not fixed", failures)


def main() -> int:
    failures: list[str] = []
    for relative in GENERATED:
        fail((SAMPLE_ROOT / relative).exists(), f"missing generated sample {relative}", failures)
    check_manifest_and_zip(failures)
    if (SAMPLE_ROOT / "output/structured-paper.docx").exists():
        check_docx(SAMPLE_ROOT / "output/structured-paper.docx", bibliography=False, failures=failures)
    if (SAMPLE_ROOT / "citation-style-audit/generated-bibliography.docx").exists():
        check_docx(SAMPLE_ROOT / "citation-style-audit/generated-bibliography.docx", bibliography=True, failures=failures)
    if (SAMPLE_ROOT / "output/structured-paper.odt").exists():
        check_odt(SAMPLE_ROOT / "output/structured-paper.odt", failures)
    if (SAMPLE_ROOT / "output/scholarly-data-workbook.xlsx").exists():
        check_xlsx(SAMPLE_ROOT / "output/scholarly-data-workbook.xlsx", failures)
    if failures:
        print("Scholarly-work sample audit failed:\n")
        for message in failures:
            print(f"- {message}")
        return 1
    print(
        "OK: 25 source/generated sample files match the checked manifest and deterministic ZIP byte-for-byte; "
        "the package digest and required DOCX, ODT and XLSX structures are valid."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
