#!/usr/bin/env python3
"""Deterministic package helpers for issue #20 teaching fixtures."""

from __future__ import annotations

from pathlib import Path
import stat
from typing import Callable
from zipfile import ZIP_DEFLATED, ZIP_STORED, ZipFile, ZipInfo


FIXED_ZIP_DATE = (2026, 9, 2, 0, 0, 0)


def deterministic_zip(
    target: Path,
    members: list[tuple[str, bytes]],
    *,
    stored_first: str | None = None,
) -> None:
    """Write sorted members with fixed timestamps, permissions and compression."""
    ordered = sorted(members, key=lambda item: item[0])
    if stored_first is not None:
        ordered.sort(key=lambda item: item[0] != stored_first)
    target.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(target, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name, payload in ordered:
            info = ZipInfo(name, FIXED_ZIP_DATE)
            info.compress_type = ZIP_STORED if name == stored_first else ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, payload, compress_type=info.compress_type, compresslevel=9)


def normalize_office_package(
    path: Path,
    *,
    stored_first: str | None = None,
    transforms: dict[str, Callable[[bytes], bytes]] | None = None,
) -> None:
    """Normalize an existing OOXML/ODT ZIP container in place."""
    transforms = transforms or {}
    with ZipFile(path) as archive:
        archive.testzip()
        members = [
            (name, transforms.get(name, lambda payload: payload)(archive.read(name)))
            for name in archive.namelist()
            if not name.endswith("/")
        ]
    temporary = path.with_suffix(path.suffix + ".tmp")
    deterministic_zip(temporary, members, stored_first=stored_first)
    temporary.replace(path)
