"""Offline case metadata and content contract; no project URLs are requested.

Authored metadata has one home; conceptual relations come only from the existing
intertextuality map. Public access is not permission or proof of execution.
"""
from __future__ import annotations

import copy
import json
import re
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from markdown import markdown

from check_ai_publication import validate_review_metadata
from handbook_structure import CHAPTERS

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "data/case-studies.yml"
SCHEMA = "data/case-study-schema.json"
INDEX = "data/case-studies-index.json"
CONNECTION_FIELDS = ("chapter_connections", "workflow_connections")
SHOWCASE_HEADINGS = {
    "en": (
        "Research question and scholarly object", "Intended users or communities",
        "Sources and coverage", "Rights and access", "Data and modelling choices",
        "Technical and institutional architecture", "Evidence inspected",
        "Minimal lawful inspection or run path", "Where the workflow breaks",
        "Manual intervention and unresolved questions", "Reuse potential and exact licence conditions",
        "Claims supported and not supported", "Maintenance and preservation",
        "Connections across the handbook", "A bounded classroom task",
    ),
    "sl": (
        "Raziskovalno vprašanje in predmet raziskave", "Predvideni uporabniki ali skupnosti",
        "Viri in pokritost", "Pravice in dostop", "Podatki in odločitve pri modeliranju",
        "Tehnična in institucionalna arhitektura", "Pregledano dokazno gradivo",
        "Minimalni postopek dovoljenega pregleda ali zagona", "Kje postopek odpove",
        "Ročni posegi in odprta vprašanja", "Možnosti ponovne uporabe in natančni licenčni pogoji",
        "Podprte in nepodprte trditve", "Vzdrževanje in dolgoročna hramba",
        "Povezave s priročnikom", "Omejena učna naloga",
    ),
}
EVIDENCE_TYPES = {
    "en": ("Project or institutional claim", "Observed interface behaviour",
           "Inspected repository/file evidence", "Locally executed result", "Editorial inference"),
    "sl": ("Trditev projekta ali ustanove", "Opaženo delovanje vmesnika",
           "Pregledano dokazno gradivo iz repozitorija ali datoteke", "Rezultat lokalnega zagona", "Uredniški sklep"),
}


class UniqueLoader(yaml.SafeLoader):
    """Reject overwritten YAML keys, including in authored metadata."""


def unique_mapping(loader: UniqueLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def load_yaml(path: Path) -> object:
    return yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueLoader)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def schema(root: Path = ROOT) -> dict:
    result = json.loads((root / SCHEMA).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(result)
    return result


def validate_schema(records: object, root: Path = ROOT) -> None:
    validator = Draft202012Validator(schema(root), format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(records), key=lambda error: str(list(error.path)))
    require(not errors, "JSON schema: " + "; ".join(
        f"{'.'.join(map(str, error.path))}: {error.message}" for error in errors
    ))


def connections(record: dict, mapping: dict) -> dict[str, list[str]]:
    entry = mapping.get("case_studies", {}).get(f"case-studies/{record['slug']}.md", {})
    return {"chapter_connections": list(entry.get("chapters", [])),
            "workflow_connections": list(entry.get("workflows", []))}


def load_records(root: Path = ROOT) -> list[dict]:
    source = load_yaml(root / SOURCE)
    require(isinstance(source, dict) and set(source) == {"schema_version", "cases"}
            and type(source["schema_version"]) is int and source["schema_version"] == 1,
            "Authored case metadata requires schema_version: 1 and cases only")
    require(isinstance(source["cases"], list), "cases must be a list")
    mapping = load_yaml(root / "intertextuality.yml")
    fields = schema(root)["$defs"]["case"]["properties"]
    records = []
    for item in source["cases"]:
        require(isinstance(item, dict), "Each authored case must be a mapping")
        require(not set(CONNECTION_FIELDS) & item.keys(),
                "Author connections only in intertextuality.yml, not case metadata")
        require("slug" in item, "Missing case slug")
        record = copy.deepcopy(item)
        record.update(connections(record, mapping))
        # Facets are sets for browsing; relation-list order remains the map's order.
        for field in ("method_domains", "source_types", "languages_regions"):
            if isinstance(record.get(field), list):
                record[field] = sorted(record[field])
        records.append(record)
    validate_schema(records, root)
    return [{field: record[field] for field in fields}
            for record in sorted(records, key=lambda record: record["case_id"])]


def frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    require(match is not None, f"{path}: missing frontmatter")
    meta = yaml.load(match.group(1), Loader=UniqueLoader)
    require(isinstance(meta, dict), f"{path}: frontmatter must be a mapping")
    return meta, text[match.end():]


def local_file(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    require(path.is_relative_to(root.resolve()) and path.is_file(), f"Missing local page/file: {relative}")
    return path


class VisibleContent(HTMLParser):
    """Ignore comments and code examples in content assertions."""

    def __init__(self) -> None:
        super().__init__()
        self.hidden = 0
        self.heading: list[str] | None = None
        self.headings: set[str] = set()
        self.text: list[str] = []
        self.section: str | None = None
        self.sections: dict[str, list[str]] = {}
        self.rows: dict[str, list[list[str]]] = {}
        self.row: list[str] | None = None
        self.cell: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "pre", "code"}:
            self.hidden += 1
        if tag == "h2" and not self.hidden:
            self.heading = []
            self.section = None
        if tag == "tr" and not self.hidden:
            self.row = []
        if tag in {"td", "th"} and self.row is not None:
            self.cell = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "h2" and self.heading is not None:
            self.section = " ".join("".join(self.heading).split())
            self.headings.add(self.section)
            self.sections.setdefault(self.section, [])
            self.heading = None
        if tag in {"td", "th"} and self.cell is not None:
            self.row.append(" ".join("".join(self.cell).split()))
            self.cell = None
        if tag == "tr" and self.row is not None:
            if self.section is not None:
                self.rows.setdefault(self.section, []).append(self.row)
            self.row = None
        if tag in {"script", "style", "pre", "code"} and self.hidden:
            self.hidden -= 1

    def handle_data(self, data: str) -> None:
        if not self.hidden:
            self.text.append(data)
            if self.heading is not None:
                self.heading.append(data)
            elif self.section is not None:
                self.sections[self.section].append(data)
            if self.cell is not None:
                self.cell.append(data)


def visible_content(text: str) -> VisibleContent:
    parser = VisibleContent()
    parser.feed(markdown(text, extensions=["fenced_code", "tables"]))
    return parser


def headings(text: str) -> set[str]:
    return visible_content(text).headings


def audit_section(root: Path, record: dict) -> str:
    relative, anchor = record["audit_record"].split("#", 1)
    text = local_file(root, relative).read_text(encoding="utf-8")
    marker = f'<a id="{anchor}"></a>'
    require(text.count(marker) == 1, f"{record['case_id']}: missing/duplicate audit record {anchor}")
    section = text.split(marker, 1)[1].split('<a id="case-', 1)[0]
    require(record["case_id"] in section and record["last_checked"] in section,
            f"{record['case_id']}: audit must identify case and matching check date")
    return section


def validate_records(records: list[dict], root: Path = ROOT) -> None:
    validate_schema(records, root)
    mapping = load_yaml(root / "intertextuality.yml")
    legacy_ids = schema(root)["x-legacy-case-ids"]
    require(set(legacy_ids) <= {record["case_id"] for record in records},
            "Original legacy inventory cannot disappear; retain an audited archived/deferred record")
    for field in ("case_id", "slug", "audit_record"):
        values = [record[field] for record in records]
        require(len(values) == len(set(values)), f"Duplicate {field}")
    pages = [record[field] for record in records for field in ("page_en", "page_sl") if record[field]]
    require(len(pages) == len(set(pages)), "Duplicate local page path")
    actual_pages = {path.relative_to(root).as_posix() for locale in ("en", "sl")
                    for path in (root / "docs" / locale / "case-studies").rglob("*.md")
                    if path.name != "index.md"}
    require(set(pages) == actual_pages,
            f"Case inventory differs from local pages: {sorted(set(pages) ^ actual_pages)}")
    for record in records:
        case_id = record["case_id"]
        require(case_id == "CASE-" + record["slug"], f"{case_id}: ID and slug must agree")
        require(record["audit_record"] == f"release/case-study-audit.md#case-{record['slug']}",
                f"{case_id}: audit anchor must identify this case")
        if record["content_standard"] == "legacy-audited":
            require(case_id in legacy_ids, f"{case_id}: new cases cannot claim the legacy exemption")
        require(date.fromisoformat(record["last_checked"]) <= date.today(), f"{case_id}: future last_checked")
        audit = audit_section(root, record)
        expected = connections(record, mapping)
        require(all(record[field] == expected[field] for field in CONNECTION_FIELDS),
                f"{case_id}: connections differ from authoritative intertextuality.yml")
        if any(not record[field] for field in CONNECTION_FIELDS):
            note = record["connection_remediation"]
            require(record["content_standard"] != "showcase-v1" and isinstance(note, str)
                    and len(note.split()) >= 4 and note in audit,
                    f"{case_id}: missing chapter/workflow connection requires explicit audited remediation")
        else:
            require(record["connection_remediation"] is None, f"{case_id}: stale connection remediation")
        for field in CONNECTION_FIELDS:
            for target in record[field]:
                local_file(root, "docs/en/" + target)
                if field == "chapter_connections":
                    require(target.removeprefix("chapters/") in CHAPTERS,
                            f"{case_id}: connection must target a core chapter, not an index")
                else:
                    require(not target.endswith("/index.md"), f"{case_id}: connection must target a workflow, not an index")
        for locale in ("en", "sl"):
            relative = record[f"page_{locale}"]
            expected_path = f"docs/{locale}/case-studies/{record['slug']}.md"
            if relative is None:
                require(not (root / expected_path).exists(), f"{case_id}: undeclared paired page")
                continue
            require(relative == expected_path, f"{case_id}: slug and page path disagree")
            meta, body = frontmatter(local_file(root, relative))
            require(meta.get("title") == record[f"title_{locale}"], f"{case_id}: frontmatter title drift")
            for field in ("case_id", "content_standard", "translation_status", "audit_record"):
                if field in meta:
                    require(meta[field] == record[field], f"{case_id}: frontmatter {field} drift")
            if record["content_standard"] == "showcase-v1":
                require(all(field in meta for field in ("case_id", "content_standard", "translation_status", "audit_record")),
                        f"{case_id}: showcase-v1 requires explicit matching page metadata")
                visible = visible_content(body)
                missing = set(SHOWCASE_HEADINGS[locale]) - visible.headings
                require(not missing, f"{case_id}/{locale}: missing showcase-v1 sections: {sorted(missing)}")
                for heading in SHOWCASE_HEADINGS[locale]:
                    require(len(" ".join(visible.sections[heading]).split()) >= 4,
                            f"{case_id}/{locale}: empty showcase-v1 section: {heading}")
                rows = visible.rows.get(SHOWCASE_HEADINGS[locale][6], [])
                for evidence_type in EVIDENCE_TYPES[locale]:
                    require(any(len(row) == 4 and row[0] == evidence_type
                                and all(cell.strip() for cell in row[1:]) for row in rows),
                            f"{case_id}/{locale}: missing evidence-table row: {evidence_type}")
            else:
                require(meta.get("content_standard") != "showcase-v1" and meta.get("v1_complete") is not True,
                        f"{case_id}: legacy/deferred page falsely marked v1-complete")
            if locale == "sl" and record["translation_status"] == "paired-human-reviewed":
                validate_review_metadata(meta.get("translation_reviewed_by"), meta.get("translation_reviewed_on"),
                                         meta.get("translation_review_scope"), f"{case_id}: translation review")
            elif locale == "sl" and record["translation_status"] == "paired-draft":
                visible = " ".join(visible_content(body).text).lower()
                require("strojno" in visible or "jezikovni pregled" in visible,
                        f"{case_id}: paired draft needs visible language-review status")


def label(field: str, value: str, locale: str, definitions: dict) -> str:
    return definitions[field]["x-labels"][value][locale]
