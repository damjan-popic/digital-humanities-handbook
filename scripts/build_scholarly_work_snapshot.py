#!/usr/bin/env python3
"""Build the deterministic versioned sample ZIP for issue #20."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from scholarly_work_package_utils import deterministic_zip

PREFIX = "scholarly-work-foundations"
MANIFEST_NAME = "MANIFEST.sha256"


def included_files(source: Path, *, include_manifest: bool) -> list[Path]:
    files = []
    for path in source.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(source).as_posix()
        if relative.endswith(".inspect.ndjson") or relative.startswith("."):
            continue
        if not include_manifest and relative == MANIFEST_NAME:
            continue
        files.append(path)
    return sorted(files)


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def build_snapshot(repo_root: Path) -> tuple[Path, Path, Path]:
    source = repo_root / "examples" / "scholarly-work-foundations"
    target = repo_root / "docs" / "assets" / "downloads" / "scholarly-work-foundations-v1.zip"
    digest_path = target.with_suffix(target.suffix + ".sha256")
    files = included_files(source, include_manifest=False)
    if not files:
        raise SystemExit(f"No sample files found under {source}")

    manifest_path = source / MANIFEST_NAME
    manifest_lines = [
        f"{sha256_bytes(path.read_bytes())}  {path.relative_to(source).as_posix()}"
        for path in files
    ]
    manifest_path.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8", newline="\n")

    archive_files = included_files(source, include_manifest=True)
    deterministic_zip(
        target,
        [
            (f"{PREFIX}/{path.relative_to(source).as_posix()}", path.read_bytes())
            for path in archive_files
        ],
    )
    digest_path.write_text(
        f"{sha256_bytes(target.read_bytes())}  {target.name}\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Wrote {manifest_path.relative_to(repo_root)} with {len(files)} member digests")
    print(f"Wrote {target.relative_to(repo_root)} with {len(archive_files)} source files")
    print(f"Wrote {digest_path.relative_to(repo_root)}")
    return manifest_path, target, digest_path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    args = parser.parse_args()
    build_snapshot(args.repo_root.resolve())


if __name__ == "__main__":
    main()
