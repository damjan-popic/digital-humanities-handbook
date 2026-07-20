#!/usr/bin/env python3
"""Generate localized workflow catalogue pages from Markdown frontmatter."""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    result = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"')
    return result


def anchor(text: str) -> str:
    text = text.lower().replace("&", " ")
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"[\s_]+", "-", text).strip("-")


def build(lang: str) -> None:
    root = ROOT / "docs" / lang / "workflows"
    groups: dict[str, list[tuple[str, Path, str]]] = defaultdict(list)
    for path in sorted(root.rglob("*.md")):
        if path.name == "index.md":
            continue
        meta = frontmatter(path.read_text(encoding="utf-8"))
        if not meta.get("title"):
            continue
        groups[meta.get("category", "Other")].append(
            (meta["title"], path.relative_to(root), meta.get("difficulty", ""))
        )

    if lang == "en":
        title = "# Workflows"
        intro = (
            "This catalogue contains the complete inherited workflow library plus new digital-humanities methods. "
            "Search when you know the task; browse by category when you are designing a method."
        )
        coverage = "The Slovene edition contains the stable core and a growing curated set of translated workflows."
    else:
        title = "# Praktični postopki"
        intro = (
            "Ta katalog vsebuje slovensko napisane in pregledane postopke. Ko ustrezni prevod še ne obstaja, "
            "je zaradi nastavitve nadomestnega jezika dostopna angleška privzeta stran; to ni prikazano kot dokončan prevod."
        )
        coverage = "[Poročilo o prevodni pokritosti](../about.md#jeziki-in-prevajanje) se ob vsaki izdaji ustvari samodejno."

    lines = ["---", f'title: "{title[2:]}"', 'description: "Generated catalogue of practical handbook workflows."', "---", "", title, "", intro, "", coverage, "", "## Categories" if lang == "en" else "## Kategorije", ""]
    for category in sorted(groups, key=str.casefold):
        lines.append(f"- **{category}** — {len(groups[category])}")
    lines.extend(["", "## All workflows" if lang == "en" else "## Vsi prevedeni postopki", ""])
    for category in sorted(groups, key=str.casefold):
        lines.append(f"### {category}")
        lines.append("")
        for title_text, rel, difficulty in sorted(groups[category], key=lambda x: x[0].casefold()):
            suffix = f' <span class="tiny">— {difficulty}</span>' if difficulty else ""
            lines.append(f"- [{title_text}]({rel.as_posix()}){suffix}")
        lines.append("")
    (root / "index.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {root.relative_to(ROOT) / 'index.md'} with {sum(map(len, groups.values()))} workflows")


if __name__ == "__main__":
    build("en")
    build("sl")
