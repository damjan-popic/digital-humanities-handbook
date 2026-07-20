#!/usr/bin/env python3
"""Report Slovene coverage against the English source tree."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = ROOT / "docs" / "en"
SL = ROOT / "docs" / "sl"


def files_under(root: Path) -> set[Path]:
    return {p.relative_to(root) for p in root.rglob("*.md")}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="Fail when any English page lacks a Slovene counterpart")
    parser.add_argument("--output", type=Path, help="Write a Markdown coverage report")
    args = parser.parse_args()

    en = files_under(EN)
    sl = files_under(SL)
    paired = en & sl
    missing = sorted(en - sl)
    extra = sorted(sl - en)
    percent = (len(paired) / len(en) * 100) if en else 100.0

    lines = [
        "# Translation coverage",
        "",
        f"- English Markdown pages: **{len(en)}**",
        f"- Slovene counterparts: **{len(paired)}**",
        f"- Coverage: **{percent:.1f}%**",
        f"- English pages currently using fallback in Slovene: **{len(missing)}**",
        "",
        "The stable chapters and learning paths must remain fully paired. The inherited workflow library is translated incrementally; untranslated pages are served from the English default edition and are not counted as Slovene translations.",
        "",
        "## Missing Slovene counterparts",
        "",
    ]
    lines.extend(f"- `{p.as_posix()}`" for p in missing)
    if extra:
        lines.extend(["", "## Slovene-only pages", ""])
        lines.extend(f"- `{p.as_posix()}`" for p in extra)
    report = "\n".join(lines) + "\n"
    print(f"Translation coverage: {len(paired)}/{len(en)} pages ({percent:.1f}%).")
    print(f"Fallback pages: {len(missing)}; Slovene-only pages: {len(extra)}.")
    if args.output:
        out = args.output if args.output.is_absolute() else ROOT / args.output
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report, encoding="utf-8")
        print(f"Wrote {out.relative_to(ROOT)}")
    return 1 if args.strict and missing else 0


if __name__ == "__main__":
    sys.exit(main())
