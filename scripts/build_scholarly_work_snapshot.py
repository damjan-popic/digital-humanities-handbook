#!/usr/bin/env python3
"""Build the deterministic versioned sample ZIP for issue #20."""

from __future__ import annotations

from pathlib import Path
import stat
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE = REPO_ROOT / "examples" / "scholarly-work-foundations"
TARGET = REPO_ROOT / "docs" / "assets" / "downloads" / "scholarly-work-foundations-v1.zip"
PREFIX = "scholarly-work-foundations"
FIXED_DATE = (2026, 9, 2, 0, 0, 0)


def main() -> None:
    files = sorted(path for path in SOURCE.rglob("*") if path.is_file())
    if not files:
        raise SystemExit(f"No sample files found under {SOURCE}")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(TARGET, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for source_path in files:
            relative = source_path.relative_to(SOURCE).as_posix()
            if relative.endswith(".inspect.ndjson") or relative.startswith("."):
                continue
            info = ZipInfo(f"{PREFIX}/{relative}", FIXED_DATE)
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, source_path.read_bytes(), compress_type=ZIP_DEFLATED, compresslevel=9)
    print(f"Wrote {TARGET.relative_to(REPO_ROOT)} with {len(files)} source files")


if __name__ == "__main__":
    main()
