"""MkDocs hook that injects ecosystem links from the canonical relation map."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from intertextuality import inject_connections, locale_from_site_dir, strip_locale_prefix


def on_page_markdown(markdown: str, page: Any, config: Any, files: Any) -> str:
    del files
    src_uri = str(page.file.src_uri)
    relative_path = strip_locale_prefix(src_uri)
    if not relative_path.startswith(("chapters/", "workflows/", "case-studies/")):
        return markdown
    if relative_path.endswith("/index.md") or relative_path == "chapters/index.md":
        return markdown

    site_dir = Path(config.site_dir)
    locale = locale_from_site_dir(site_dir, src_uri)
    category = page.meta.get("category") if hasattr(page, "meta") else None
    return inject_connections(
        markdown,
        relative_path,
        locale,
        category=str(category) if category else None,
        link_mode="relative",
    )
