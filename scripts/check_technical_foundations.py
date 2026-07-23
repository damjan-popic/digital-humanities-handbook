#!/usr/bin/env python3
"""Validate the paired technical-foundations route required by issue #19."""
from __future__ import annotations

import posixpath
import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
HUB = "foundations/technical-workspace.md"
FOUNDATION_WORKFLOWS = {
    "clone-run-change-and-commit-a-handbook-project.md",
    "install-and-configure-git.md",
    "install-wsl-and-ubuntu-on-windows.md",
    "navigate-files-and-directories-with-bash.md",
    "track-a-small-project-with-git.md",
    "use-pipes-redirection-and-grep-in-bash.md",
}
PYTHON_WORKFLOWS = {
    "create-a-python-312-virtual-environment.md",
    "install-python-312-for-nlp.md",
    "install-python-packages-with-pip.md",
    "run-a-python-script-from-terminal.md",
    "structure-a-small-python-nlp-project.md",
    "troubleshoot-python-venv-and-pip.md",
}
TECHNICAL_WORKFLOWS = {
    *(f"workflows/foundations/{name}" for name in FOUNDATION_WORKFLOWS),
    *(f"workflows/nlp/{name}" for name in PYTHON_WORKFLOWS),
}
ALLOWED_CHAPTERS = {
    "chapters/data-metadata-models.md",
    "chapters/research-design.md",
    "chapters/ai-ethics-reproducibility.md",
    "chapters/open-living-handbook.md",
}
META = {
    "en": {
        "hub_title": "Technical workspace: terminal, WSL, Bash, Git, and Python",
        "nav_group": "Foundations",
        "clinic": "## Technical-readiness clinic",
        "category": "Foundations",
        "module_marker": "clinic",
    },
    "sl": {
        "hub_title": "Tehnično delovno okolje: terminal, WSL, Bash, Git in Python",
        "nav_group": "Osnove",
        "clinic": "## Preverjanje tehnične pripravljenosti",
        "category": "Osnove",
        "module_marker": "pripravljenosti",
    },
}


class MkDocsLoader(yaml.SafeLoader):
    """Treat trusted MkDocs Python-name tags as inert strings."""


MkDocsLoader.add_multi_constructor(
    "tag:yaml.org,2002:python/name:",
    lambda _loader, suffix, _node: suffix,
)


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return {}
    raw = text[4 : text.index("\n---\n", 4)]
    return yaml.safe_load(raw) or {}


def markdown_links(text: str) -> list[str]:
    return re.findall(r"!?(?:\[[^\]]*\])\(([^)]+)\)", text)


def localized_nav(config: dict, locale: str) -> list[dict]:
    if locale == "en":
        return config["nav"]
    for plugin in config["plugins"]:
        if not isinstance(plugin, dict) or "i18n" not in plugin:
            continue
        for language in plugin["i18n"]["languages"]:
            if language["locale"] == locale:
                return language["nav"]
    raise ValueError(f"mkdocs.yml: missing navigation for locale '{locale}'")


def check_hub_links(locale: str, failures: list[str]) -> None:
    hub_path = ROOT / "docs" / locale / HUB
    if not hub_path.exists():
        failures.append(f"Missing technical hub: {hub_path.relative_to(ROOT)}")
        return
    text = hub_path.read_text(encoding="utf-8")
    if f"# {META[locale]['hub_title']}" not in text:
        failures.append(
            f"{hub_path.relative_to(ROOT)}: missing required displayed title"
        )

    resolved_links: set[str] = set()
    for raw_target in markdown_links(text):
        target = raw_target.strip().strip("<>")
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, flags=re.IGNORECASE):
            continue
        path_part = unquote(target.split("#", 1)[0])
        if not path_part:
            continue
        resolved = posixpath.normpath(
            posixpath.join(posixpath.dirname(HUB), path_part)
        )
        resolved_links.add(resolved)
        target_path = ROOT / "docs" / locale / resolved
        if not target_path.exists():
            failures.append(
                f"{hub_path.relative_to(ROOT)}: missing linked page '{resolved}'"
            )

    missing_route_links = TECHNICAL_WORKFLOWS - resolved_links
    if missing_route_links:
        failures.append(
            f"{hub_path.relative_to(ROOT)}: missing technical-route links "
            f"{sorted(missing_route_links)}"
        )


def check_navigation(locale: str, config: dict, failures: list[str]) -> None:
    label = META[locale]["nav_group"]
    nav = localized_nav(config, locale)
    matches = [entry[label] for entry in nav if isinstance(entry, dict) and label in entry]
    if len(matches) != 1:
        failures.append(
            f"mkdocs.yml ({locale}): expected one top-level '{label}' group"
        )
        return
    expected = [{META[locale]["hub_title"]: HUB}]
    if matches[0] != expected:
        failures.append(
            f"mkdocs.yml ({locale}): '{label}' group is {matches[0]!r}; "
            f"expected {expected!r}"
        )


def check_learning_path(locale: str, failures: list[str]) -> None:
    path = ROOT / "docs" / locale / "learning-paths/digitalna-slovenistika.md"
    text = path.read_text(encoding="utf-8")
    clinic = META[locale]["clinic"]
    if text.count(clinic) != 1:
        failures.append(
            f"{path.relative_to(ROOT)}: expected one readiness heading '{clinic}'"
        )
    modules = [int(number) for number in re.findall(r"(?m)^### (\d+)\. ", text)]
    if modules != list(range(1, 15)):
        failures.append(
            f"{path.relative_to(ROOT)}: module sequence is {modules}; expected 1 through 14"
        )
    required_tokens = (
        "technical-readiness/",
        "README.md",
        "environment-check.md",
        "hello.py",
        "requirements.txt",
        "output/",
        "../foundations/technical-workspace.md",
        "../workflows/foundations/install-wsl-and-ubuntu-on-windows.md",
        "../workflows/foundations/navigate-files-and-directories-with-bash.md",
        "../workflows/foundations/install-and-configure-git.md",
        "../workflows/foundations/clone-run-change-and-commit-a-handbook-project.md",
        "../workflows/nlp/create-a-python-312-virtual-environment.md",
        "../workflows/nlp/install-python-packages-with-pip.md",
        "../workflows/nlp/run-a-python-script-from-terminal.md",
    )
    for token in required_tokens:
        if token not in text:
            failures.append(f"{path.relative_to(ROOT)}: missing readiness token {token!r}")

    module_three = re.search(
        r"(?ms)^### 3\. .+?\n(.*?)(?=^### 4\. )",
        text,
    )
    if not module_three:
        failures.append(f"{path.relative_to(ROOT)}: missing module 3 body")
    else:
        body = module_three.group(1)
        if META[locale]["module_marker"] not in body.casefold():
            failures.append(
                f"{path.relative_to(ROOT)}: module 3 does not build on readiness clinic"
            )
        for token in (
            "../workflows/nlp/structure-a-small-python-nlp-project.md",
            "../workflows/nlp/troubleshoot-python-venv-and-pip.md",
        ):
            if token not in body:
                failures.append(
                    f"{path.relative_to(ROOT)}: module 3 missing follow-on workflow {token!r}"
                )


def main() -> int:
    failures: list[str] = []
    config = yaml.load(
        (ROOT / "mkdocs.yml").read_text(encoding="utf-8"),
        Loader=MkDocsLoader,
    )
    ecosystem = yaml.safe_load(
        (ROOT / "intertextuality.yml").read_text(encoding="utf-8")
    )

    for locale in ("en", "sl"):
        foundation_root = ROOT / "docs" / locale / "workflows/foundations"
        actual = (
            {path.name for path in foundation_root.glob("*.md")}
            if foundation_root.exists()
            else set()
        )
        if actual != FOUNDATION_WORKFLOWS:
            failures.append(
                f"docs/{locale}/workflows/foundations: paired path set drifted; "
                f"missing={sorted(FOUNDATION_WORKFLOWS - actual)}, "
                f"unexpected={sorted(actual - FOUNDATION_WORKFLOWS)}"
            )

        for relative_path in sorted(TECHNICAL_WORKFLOWS):
            path = ROOT / "docs" / locale / relative_path
            if not path.exists():
                failures.append(
                    f"Missing paired technical workflow: {path.relative_to(ROOT)}"
                )

        for name in sorted(FOUNDATION_WORKFLOWS & actual):
            path = foundation_root / name
            metadata = front_matter(path)
            if metadata.get("category_id") != "foundations":
                failures.append(
                    f"{path.relative_to(ROOT)}: category_id must be 'foundations'"
                )
            if metadata.get("category") != META[locale]["category"]:
                failures.append(
                    f"{path.relative_to(ROOT)}: localized category is "
                    f"{metadata.get('category')!r}; expected {META[locale]['category']!r}"
                )

        check_hub_links(locale, failures)
        check_navigation(locale, config, failures)
        check_learning_path(locale, failures)

    category_entry = ecosystem.get("workflow_categories", {}).get("foundations")
    if not category_entry or not category_entry.get("chapters"):
        failures.append(
            "intertextuality.yml: stable category 'foundations' has no ecosystem mapping"
        )

    overrides = ecosystem.get("workflows", {})
    for workflow in sorted(TECHNICAL_WORKFLOWS):
        chapters = set(overrides.get(workflow, {}).get("chapters", []))
        if not chapters:
            failures.append(
                f"intertextuality.yml: technical workflow '{workflow}' has no curated override"
            )
        unexpected = chapters - ALLOWED_CHAPTERS
        if unexpected:
            failures.append(
                f"intertextuality.yml: technical workflow '{workflow}' links outside "
                f"the curated foundation chapters: {sorted(unexpected)}"
            )

    if failures:
        print("Technical-foundations check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "OK: paired bilingual technical route has 2 hubs, "
        f"{len(FOUNDATION_WORKFLOWS)} paired foundation workflows, "
        f"{len(PYTHON_WORKFLOWS)} paired curated Python workflows, "
        "one unnumbered readiness clinic in each 14-module path, "
        "deterministic category IDs, valid hub links, and curated ecosystem mappings."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
