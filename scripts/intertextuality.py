#!/usr/bin/env python3
"""Shared intertextuality map helpers for the site, checks, and review manuscripts."""
from __future__ import annotations

import posixpath
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "intertextuality.yml"
SITE_URL = "https://damjan-popic.github.io/digital-humanities-handbook/"
START_MARKER = "<!-- handbook-ecosystem:start -->"
END_MARKER = "<!-- handbook-ecosystem:end -->"


@lru_cache(maxsize=1)
def load_map() -> dict[str, Any]:
    data = yaml.safe_load(MAP_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("intertextuality.yml must contain a mapping")
    return data


def strip_locale_prefix(src_uri: str) -> str:
    path = src_uri.replace("\\", "/").lstrip("/")
    for prefix in ("en/", "sl/"):
        if path.startswith(prefix):
            return path[len(prefix) :]
    return path


def locale_from_site_dir(site_dir: str | Path, src_uri: str = "") -> str:
    normalized = str(site_dir).replace("\\", "/").rstrip("/")
    if normalized.endswith("/sl"):
        return "sl"
    if src_uri.replace("\\", "/").lstrip("/").startswith("sl/"):
        return "sl"
    return "en"


def _read_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        _, _, remainder = text.partition("\n---\n")
        raw = text[4 : text.index("\n---\n")]
        metadata = yaml.safe_load(raw) or {}
        return metadata, remainder
    return {}, text


def source_path(locale: str, relative_path: str) -> tuple[Path, bool]:
    localized = ROOT / "docs" / locale / relative_path
    if localized.exists():
        return localized, False
    if locale == "sl":
        fallback = ROOT / "docs" / "en" / relative_path
        if fallback.exists():
            return fallback, True
    return localized, False


@lru_cache(maxsize=None)
def page_title(locale: str, relative_path: str) -> tuple[str, bool]:
    path, fallback = source_path(locale, relative_path)
    if not path.exists():
        raise FileNotFoundError(path)
    metadata, body = _read_front_matter(path)
    title = metadata.get("title")
    if not title:
        match = re.search(r"(?m)^# (.+)$", body)
        if not match:
            raise ValueError(f"{path.relative_to(ROOT)} has no title")
        title = match.group(1).strip()
    return str(title), fallback


@lru_cache(maxsize=None)
def workflow_category(relative_path: str) -> str:
    path = ROOT / "docs" / "en" / relative_path
    metadata, _ = _read_front_matter(path)
    category = metadata.get("category")
    if not category:
        raise ValueError(f"{path.relative_to(ROOT)} has no workflow category")
    return str(category)


def connections_for(relative_path: str, category: str | None = None) -> dict[str, list[str]]:
    data = load_map()
    if relative_path in data["chapters"]:
        entry = data["chapters"][relative_path]
        return {
            "workflows": list(entry.get("workflows", [])),
            "case_studies": list(entry.get("case_studies", [])),
        }

    if relative_path in data["case_studies"]:
        entry = data["case_studies"][relative_path]
        return {
            "chapters": list(entry.get("chapters", [])),
            "workflows": list(entry.get("workflows", [])),
        }

    if relative_path.startswith("workflows/") and not relative_path.endswith("/index.md"):
        category = category or workflow_category(relative_path)
        category_entry = data["workflow_categories"].get(category, {})
        related_cases = [
            case_path
            for case_path, entry in data["case_studies"].items()
            if relative_path in entry.get("workflows", [])
        ]
        return {
            "chapters": list(category_entry.get("chapters", [])),
            "case_studies": related_cases,
        }

    return {}


def _relative_url(current_path: str, target_path: str) -> str:
    start = posixpath.dirname(current_path) or "."
    return posixpath.relpath(target_path, start=start)


def _absolute_url(locale: str, target_path: str) -> str:
    prefix = "sl/" if locale == "sl" else ""
    if target_path.endswith("index.md"):
        clean = target_path[: -len("index.md")]
    elif target_path.endswith(".md"):
        clean = target_path[:-3] + "/"
    else:
        clean = target_path
    return f"{SITE_URL}{prefix}{clean}"


def _link_item(
    current_path: str,
    target_path: str,
    locale: str,
    link_mode: str,
) -> str:
    title, fallback = page_title(locale, target_path)
    url = (
        _absolute_url(locale, target_path)
        if link_mode == "absolute"
        else _relative_url(current_path, target_path)
    )
    suffix = ""
    if fallback:
        suffix = (
            " *(angleška nadomestna stran)*"
            if locale == "sl"
            else " *(English fallback)*"
        )
    return f"    - [{title}]({url}){suffix}"


def render_connections(
    current_path: str,
    locale: str,
    *,
    category: str | None = None,
    link_mode: str = "relative",
) -> str:
    connections = connections_for(current_path, category)
    if not any(connections.values()):
        return ""

    if current_path.startswith("chapters/"):
        heading = "Nadaljujte po ekosistemu" if locale == "sl" else "Continue through the ecosystem"
        sections = (
            ("workflows", "Preizkusite praktični postopek" if locale == "sl" else "Try a workflow"),
            ("case_studies", "Oglejte si študijo primera" if locale == "sl" else "Inspect a case study"),
        )
        admonition = "tip"
    elif current_path.startswith("workflows/"):
        heading = "Umestitev postopka v priročnik" if locale == "sl" else "Where this workflow fits"
        sections = (
            ("chapters", "Pojmovna poglavja" if locale == "sl" else "Conceptual chapters"),
            ("case_studies", "Sorodne študije primerov" if locale == "sl" else "Related case studies"),
        )
        admonition = "info"
    else:
        heading = "Primer povežite s priročnikom" if locale == "sl" else "Read this case across the handbook"
        sections = (
            ("chapters", "Pojmovna poglavja" if locale == "sl" else "Conceptual chapters"),
            ("workflows", "Izvedljivi postopki" if locale == "sl" else "Executable workflows"),
        )
        admonition = "example"

    lines = [START_MARKER, f'!!! {admonition} "{heading}"']
    for key, label in sections:
        targets = connections.get(key, [])
        if not targets:
            continue
        lines.extend([f"    **{label}**", ""])
        lines.extend(
            _link_item(current_path, target, locale, link_mode)
            for target in targets
        )
        lines.append("")
    while lines and lines[-1] == "":
        lines.pop()
    lines.append(END_MARKER)
    return "\n".join(lines)


def inject_connections(
    markdown: str,
    current_path: str,
    locale: str,
    *,
    category: str | None = None,
    link_mode: str = "relative",
) -> str:
    if START_MARKER in markdown:
        return markdown
    block = render_connections(
        current_path,
        locale,
        category=category,
        link_mode=link_mode,
    )
    if not block:
        return markdown

    if current_path.startswith("chapters/"):
        anchors = ("## Practice", "## Vaja")
    elif current_path.startswith("workflows/"):
        anchors = (
            "## Practice task",
            "## Naloga",
            "## Common traps",
            "## Pogoste pasti",
        )
    else:
        anchors = (
            "## Practice use",
            "## Uporaba pri pouku",
            "## Limits and cautions",
            "## Omejitve in opozorila",
            "## Reuse checklist",
        )

    for anchor in anchors:
        match = re.search(rf"(?m)^{re.escape(anchor)}\s*$", markdown)
        if match:
            return markdown[: match.start()].rstrip() + "\n\n" + block + "\n\n" + markdown[match.start() :]
    return markdown.rstrip() + "\n\n" + block + "\n"
