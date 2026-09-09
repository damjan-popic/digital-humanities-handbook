#!/usr/bin/env python3
"""Resolve review-manuscript links against an explicit, verified source commit."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable
from urllib.parse import quote, unquote, urlsplit, urlunsplit

REPOSITORY_URL = "https://github.com/damjan-popic/digital-humanities-handbook"
SNAPSHOT_STATUS = "development review snapshot; not a numbered edition"
ROOT = Path(__file__).resolve().parents[1]


def _git(root: Path, *arguments: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *arguments], capture_output=True, check=False
    )
    if result.returncode:
        raise ValueError(
            "Cannot verify the recorded review source commit: "
            + result.stderr.decode("utf-8", errors="replace").strip()
            + ". Fetch its history before recording a new source snapshot."
        )
    return result.stdout


class ReviewSource:
    """A fixed source revision and offline-verifiable manuscript dependencies."""

    def __init__(
        self,
        root: Path,
        source_commit: str,
        snapshot_status: str,
        source_timestamp_utc: str,
        files_sha256: dict[str, str] | None = None,
        directory_files: dict[str, list[str]] | None = None,
    ) -> None:
        if not isinstance(source_commit, str) or not re.fullmatch(r"[0-9a-f]{40}", source_commit):
            raise ValueError("Review source_commit must be a full 40-character commit ID")
        if snapshot_status != SNAPSHOT_STATUS:
            raise ValueError(f"Review snapshot_status must be {SNAPSHOT_STATUS!r}")
        self.root = root.resolve()
        self.source_commit = source_commit
        self.snapshot_status = snapshot_status
        self.files: set[Path] = set()
        self.directories: set[Path] = set()
        if not isinstance(source_timestamp_utc, str) or not re.fullmatch(
            r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", source_timestamp_utc
        ):
            raise ValueError("Review source_timestamp_utc must be an ISO UTC timestamp")
        datetime.fromisoformat(source_timestamp_utc)
        self.source_date = source_timestamp_utc
        self.files_sha256 = files_sha256
        self.directory_files = directory_files or {}

    @classmethod
    def from_commit(cls, root: Path, source_commit: str) -> ReviewSource:
        """Use Git only during the explicitly requested snapshot-recording step."""
        if not isinstance(source_commit, str) or not re.fullmatch(r"[0-9a-f]{40}", source_commit):
            raise ValueError("Review source_commit must be a full 40-character commit ID")
        if _git(root, "cat-file", "-t", source_commit).strip() != b"commit":
            raise ValueError("Review source_commit must identify a Git commit")
        timestamp = _git(root, "show", "-s", "--format=%cI", source_commit)
        source_date = (
            datetime.fromisoformat(timestamp.decode("utf-8").strip())
            .astimezone(timezone.utc)
            .isoformat(timespec="seconds")
            .replace("+00:00", "Z")
        )
        return cls(root, source_commit, SNAPSHOT_STATUS, source_date)

    @classmethod
    def load(cls, root: Path = ROOT) -> ReviewSource:
        path = root / "release" / "review-source.json"
        if not path.exists():
            raise ValueError(
                "Missing release/review-source.json: commit the reviewed source first, "
                "then record its commit ID before generating manuscripts"
            )
        metadata = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(metadata, dict):
            raise ValueError("release/review-source.json must contain an object")
        files = metadata.get("files_sha256")
        directories = metadata.get("directory_files")
        if not isinstance(files, dict) or not files or any(
            not isinstance(path, str) or not isinstance(digest, str)
            or not re.fullmatch(r"[0-9a-f]{64}", digest)
            for path, digest in files.items()
        ):
            raise ValueError("Review files_sha256 must map source paths to SHA-256 digests")
        if not isinstance(directories, dict) or any(
            not isinstance(path, str) or not isinstance(items, list)
            or any(not isinstance(item, str) for item in items)
            for path, items in directories.items()
        ):
            raise ValueError("Review directory_files must record each linked directory's file paths")
        return cls(
            root, metadata.get("source_commit", ""), metadata.get("snapshot_status", ""),
            metadata.get("source_timestamp_utc", ""), files, directories,
        )

    def require_path(self, path: Path) -> Path:
        resolved = path.resolve()
        if not resolved.is_relative_to(self.root):
            raise ValueError(f"Review link escapes the repository: {path}")
        if not resolved.exists() and resolved.is_relative_to(self.root / "docs" / "sl"):
            relative = resolved.relative_to(self.root / "docs" / "sl")
            resolved = (self.root / "docs" / "en" / relative).resolve()
        if not resolved.is_relative_to(self.root):
            raise ValueError(f"Review fallback link escapes the repository: {path}")
        if not resolved.exists():
            raise ValueError(f"Missing review source or link target: {resolved.relative_to(self.root)}")
        if resolved.is_dir():
            self.directories.add(resolved)
            self.files.update(item for item in resolved.rglob("*") if item.is_file())
        elif resolved.is_file():
            self.files.add(resolved)
        else:
            raise ValueError(f"Unsupported review link target: {resolved}")
        return resolved

    def url(self, destination: str, source_path: Path) -> str:
        parsed = urlsplit(destination)
        if parsed.scheme or parsed.netloc:
            # Preserve external citations. Links to this repository's living
            # source are part of the snapshot and therefore use its recorded ID.
            prefix = REPOSITORY_URL + "/"
            if not destination.startswith(prefix):
                return destination
            repository_path = parsed.path[len(urlsplit(REPOSITORY_URL).path):]
            match = re.fullmatch(r"/(?:blob|tree)/(?:main|master|HEAD)/(.+)", repository_path)
            if not match:
                return destination
            target = self.require_path(self.root / unquote(match.group(1)))
        else:
            decoded_path = unquote(parsed.path)
            if decoded_path.startswith(("/", "\\")) or "\\" in decoded_path:
                raise ValueError(f"Review link is not a repository-relative path: {destination}")
            target = self.require_path(source_path.parent / decoded_path if decoded_path else source_path)
        relative = target.relative_to(self.root).as_posix()
        kind = "tree" if target.is_dir() else "blob"
        if target.is_file() and target.is_relative_to(self.root / "docs" / "assets"):
            # Downloads and embedded images need file bytes, not GitHub's HTML
            # file viewer; the raw route is pinned to the same source commit.
            kind = "raw"
        absolute = f"{REPOSITORY_URL}/{kind}/{self.source_commit}/{quote(relative, safe='/')}"
        return urlunsplit((*urlsplit(absolute)[:3], parsed.query, parsed.fragment))

    def rewrite(self, markdown: str, source_path: Path) -> str:
        source_path = self.require_path(source_path)
        return rewrite_links(markdown, lambda destination: self.url(destination, source_path))

    def verify(self) -> None:
        """Compare Git bytes when recording; compare preserved hashes otherwise."""
        failures: list[str] = []
        recording = self.files_sha256 is None
        current_directories: dict[str, list[str]] = {}
        for directory in sorted(self.directories):
            relative = directory.relative_to(self.root).as_posix()
            current = sorted(
                item.relative_to(self.root).as_posix()
                for item in directory.rglob("*")
                if item.is_file()
            )
            current_directories[relative] = current
            if recording:
                recorded = sorted(
                    item.decode("utf-8")
                    for item in _git(
                        self.root, "ls-tree", "-r", "--name-only", "-z", self.source_commit, "--", relative
                    ).split(b"\0")
                    if item
                )
            else:
                recorded = self.directory_files.get(relative, [])
            if recorded != current:
                failures.append(f"{relative}: directory contents differ from the pinned source")
        current_hashes: dict[str, str] = {}
        for path in sorted(self.files):
            relative = path.relative_to(self.root).as_posix()
            current = path.read_bytes()
            current_hashes[relative] = hashlib.sha256(current).hexdigest()
            if recording:
                try:
                    recorded_bytes = _git(self.root, "show", f"{self.source_commit}:{relative}")
                except ValueError:
                    failures.append(f"{relative}: absent from the pinned source commit")
                    continue
                if current != recorded_bytes:
                    failures.append(f"{relative}: differs from the pinned source commit")
            elif current_hashes[relative] != self.files_sha256.get(relative):
                failures.append(f"{relative}: differs from its recorded source digest")
        if not recording:
            if set(current_hashes) != set(self.files_sha256):
                failures.append("Manuscript source/target paths differ from the recorded snapshot")
            if set(current_directories) != set(self.directory_files):
                failures.append("Linked directories differ from the recorded snapshot")
        if failures:
            raise ValueError(
                "Review source snapshot is stale. Commit the source changes and update "
                "it with --record-source <full-commit-ID> before regenerating:\n- " + "\n- ".join(failures)
            )
        self.files_sha256 = current_hashes
        self.directory_files = current_directories

    def metadata(self) -> dict[str, object]:
        if self.files_sha256 is None:
            raise ValueError("Verify source files before recording snapshot metadata")
        return {
            "source_commit": self.source_commit,
            "snapshot_status": self.snapshot_status,
            "source_timestamp_utc": self.source_date,
            "files_sha256": self.files_sha256,
            "directory_files": self.directory_files,
        }


def _inline_links(text: str, replace: Callable[[str], str]) -> str:
    """Rewrite link destinations without changing labels, titles or code spans."""
    spans: list[tuple[int, int, str]] = []
    cursor = 0
    while cursor < len(text):
        if text[cursor] == "\\":
            cursor += 2
            continue
        if text[cursor] == "`":
            end = cursor
            while end < len(text) and text[end] == "`":
                end += 1
            closing = text.find(text[cursor:end], end)
            cursor = closing + end - cursor if closing >= 0 else end
            continue
        if text[cursor:cursor + 2] != "](" or "[" not in text[:cursor]:
            cursor += 1
            continue
        start = cursor + 2
        while start < len(text) and text[start] in " \t":
            start += 1
        if start >= len(text):
            break
        if text[start] == "<":
            start += 1
            end = text.find(">", start)
            if end < 0:
                cursor = start
                continue
        else:
            end = start
            depth = 0
            while end < len(text):
                char = text[end]
                if char == "\\" and end + 1 < len(text):
                    end += 2
                    continue
                if char == "(":
                    depth += 1
                elif char == ")":
                    if depth == 0:
                        break
                    depth -= 1
                elif char.isspace() and depth == 0:
                    break
                end += 1
        if end > start:
            spans.append((start, end, replace(text[start:end])))
        cursor = max(end + 1, start + 1)
    for start, end, replacement in reversed(spans):
        text = text[:start] + replacement + text[end:]
    return text


def rewrite_links(markdown: str, replace: Callable[[str], str]) -> str:
    """Visit inline/image and reference links, excluding fenced and inline code."""
    result: list[str] = []
    fence_character = ""
    fence_length = 0
    for line in markdown.splitlines(keepends=True):
        fence = re.match(r"^[ \t]*(`{3,}|~{3,})(.*)$", line)
        if fence_character:
            if fence and fence.group(1)[0] == fence_character and len(fence.group(1)) >= fence_length and not fence.group(2).strip():
                fence_character = ""
            result.append(line)
            continue
        if fence:
            fence_character = fence.group(1)[0]
            fence_length = len(fence.group(1))
            result.append(line)
            continue
        definition = re.match(r"^(\s{0,3}\[(?!\^)[^\]]+\]:[ \t]*)(<[^>\n]+>|\S+)(.*)$", line)
        if definition:
            destination = definition.group(2)
            wrapped = destination.startswith("<")
            replacement = replace(destination[1:-1] if wrapped else destination)
            if wrapped:
                replacement = "<" + replacement + ">"
            start, end = definition.span(2)
            result.append(line[:start] + replacement + line[end:])
        else:
            result.append(_inline_links(line, replace))
    return "".join(result)
