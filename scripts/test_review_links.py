#!/usr/bin/env python3
"""Regression tests for pinned review links and archive-safe source verification."""
from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from review_links import REPOSITORY_URL, SNAPSHOT_STATUS, ReviewSource, rewrite_links


class ReviewLinkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="handbook-review-links-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.fixtures = {
            ".gitattributes": (Path(__file__).resolve().parents[1] / ".gitattributes").read_bytes(),
            "docs/en/chapters/core.md": "# Core\n\n## Evidence\n",
            "docs/sl/chapters/core.md": "# Jedro\n\n## Dokazi\n",
            "docs/en/workflows/paired.md": "# Paired\n",
            "docs/sl/workflows/paired.md": "# Prevedeno\n",
            "docs/en/workflows/fallback.md": "# English only\n",
            "docs/assets/downloads/sample (draft).zip": b"PK\x03\x04\x00\r\npreserved binary fixture\r\n",
            "teaching-data/sample/source.txt": "preserved source\n",
            "teaching-data/sample/output.csv": "identifier,value\nEX-01,1\n",
            "teaching-data/sample/source.json": '{"identifier": "EX-01"}\n',
            "teaching-data/sample/annotation.conllu": "1\tbeseda\tbeseda\tNOUN\t_\t_\t0\troot\t_\t_\n",
            "scripts/example.py": 'print("stable text")\n',
            "teaching-data/archival-friction/source/provider-ocr.txt": (
                Path(__file__).resolve().parents[1]
                / "teaching-data/archival-friction/source/provider-ocr.txt"
            ).read_bytes(),
        }
        for relative, contents in self.fixtures.items():
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(contents if isinstance(contents, bytes) else contents.encode("utf-8"))
        self.git("init", "--quiet")
        self.git("config", "core.autocrlf", "false")
        self.git("add", ".")
        self.git("-c", "user.name=Review test", "-c", "user.email=test@example.invalid",
                 "-c", "commit.gpgsign=false", "commit", "--quiet", "-m", "Source fixture")
        self.commit = self.git("rev-parse", "HEAD").strip()
        self.source = ReviewSource.from_commit(self.root, self.commit)
        self.page = self.root / "docs/sl/chapters/core.md"

    def git(self, *arguments: str) -> str:
        environment = {
            **os.environ,
            "GIT_AUTHOR_DATE": "2026-09-07T12:30:00+02:00",
            "GIT_COMMITTER_DATE": "2026-09-07T12:30:00+02:00",
        }
        return subprocess.run(
            ["git", "-C", str(self.root), *arguments], env=environment,
            check=True, capture_output=True, text=True,
        ).stdout

    def expected(self, path: str, kind: str = "blob") -> str:
        return f"{REPOSITORY_URL}/{kind}/{self.commit}/{path}"

    def test_localized_link_and_anchor(self) -> None:
        result = self.source.rewrite("[Vaja](../workflows/paired.md#naloga)", self.page)
        self.assertEqual(result, f"[Vaja]({self.expected('docs/sl/workflows/paired.md')}#naloga)")

    def test_missing_slovene_target_uses_english_and_keeps_label(self) -> None:
        result = self.source.rewrite(
            "[Workflow](../workflows/fallback.md) *(angleška nadomestna stran)*", self.page
        )
        self.assertEqual(
            result,
            f"[Workflow]({self.expected('docs/en/workflows/fallback.md')}) *(angleška nadomestna stran)*",
        )

    def test_same_page_anchor_points_to_the_source_page(self) -> None:
        result = self.source.rewrite("[Dokazi](#dokazi)", self.page)
        self.assertEqual(result, f"[Dokazi]({self.expected('docs/sl/chapters/core.md')}#dokazi)")

    def test_asset_spaces_query_and_fragment_are_preserved(self) -> None:
        result = self.source.rewrite(
            '[Packet](<../../assets/downloads/sample (draft).zip?download=1#contents> "Archive")', self.page
        )
        self.assertEqual(
            result,
            f'[Packet](<{self.expected("docs/assets/downloads/sample%20%28draft%29.zip", "raw")}?download=1#contents> "Archive")',
        )

    def test_external_links_are_unchanged(self) -> None:
        markdown = "[Paper](https://example.org/a_(b)?x=1#part) [Mail](mailto:test@example.org)"
        self.assertEqual(self.source.rewrite(markdown, self.page), markdown)

    def test_own_living_source_directory_is_pinned(self) -> None:
        result = self.source.rewrite(
            f"[Data]({REPOSITORY_URL}/tree/main/teaching-data/sample)", self.page
        )
        self.assertEqual(result, f"[Data]({self.expected('teaching-data/sample', 'tree')})")
        self.source.verify()

    def test_relative_escape_and_encoded_escape_are_rejected(self) -> None:
        for destination in ("../../../../outside.txt", "%2e%2e/%2e%2e/%2e%2e/%2e%2e/outside.txt"):
            with self.subTest(destination=destination), self.assertRaisesRegex(ValueError, "escapes"):
                self.source.url(destination, self.page)

    def test_missing_target_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "Missing review"):
            self.source.url("../workflows/missing.md", self.page)

    def test_fences_and_inline_code_are_not_rewritten(self) -> None:
        markdown = (
            "```markdown\n[Missing](../../../../outside.txt)\n```\n"
            "    ~~~~markdown\n[Missing](missing.md)\n    ~~~\n[Missing](missing.md)\n    ~~~~\n"
            "`[Missing](missing.md)` and ``[Missing](missing.md)``\n"
        )
        self.assertEqual(self.source.rewrite(markdown, self.page), markdown)

    def test_image_and_reference_destinations_are_rewritten(self) -> None:
        markdown = (
            "![Diagram](../workflows/paired.md)\n"
            '[workflow]: ../workflows/paired.md "Reference title"\n'
            "[^source]: A scholarly footnote, not a link definition.\n"
        )
        expected = self.expected("docs/sl/workflows/paired.md")
        result = self.source.rewrite(markdown, self.page)
        self.assertEqual(
            result,
            f'![Diagram]({expected})\n[workflow]: {expected} "Reference title"\n'
            "[^source]: A scholarly footnote, not a link definition.\n",
        )

    def test_recording_rejects_uncommitted_source_changes(self) -> None:
        self.page.write_text("# Changed\n", encoding="utf-8")
        self.source.rewrite("[Dokazi](#dokazi)", self.page)
        with self.assertRaisesRegex(ValueError, "differs from the pinned source commit"):
            self.source.verify()

    def test_recording_rejects_new_untracked_link_targets(self) -> None:
        target = self.root / "docs/sl/workflows/new.md"
        target.write_text("# New\n", encoding="utf-8")
        self.source.rewrite("[New](../workflows/new.md)", self.page)
        with self.assertRaisesRegex(ValueError, "absent from the pinned source"):
            self.source.verify()

    def record_fixture(self) -> str:
        markdown = "[Workflow](../workflows/paired.md)"
        expected = self.source.rewrite(markdown, self.page)
        self.source.verify()
        metadata = self.root / "release/review-source.json"
        metadata.parent.mkdir()
        metadata.write_text(json.dumps(self.source.metadata()), encoding="utf-8")
        return expected

    def test_snapshot_timestamp_comes_from_source_commit_and_is_utc(self) -> None:
        self.assertEqual(self.source.source_date, "2026-09-07T10:30:00Z")

    def test_offline_snapshot_does_not_call_git(self) -> None:
        expected = self.record_fixture()
        with patch("review_links._git", side_effect=AssertionError("Offline builds must not use Git")):
            offline = ReviewSource.load(self.root)
            self.assertEqual(offline.rewrite("[Workflow](../workflows/paired.md)", self.page), expected)
            offline.verify()
            self.assertEqual(offline.metadata(), self.source.metadata())

    def autocrlf_clone(self) -> Path:
        temporary = tempfile.TemporaryDirectory(prefix="handbook-review-autocrlf-")
        self.addCleanup(temporary.cleanup)
        clone = Path(temporary.name) / "checkout"
        self.git(
            "clone", "--quiet", "--no-local", "--config", "core.autocrlf=true",
            str(self.root), str(clone),
        )
        return clone

    def test_autocrlf_clone_preserves_snapshot_source_and_offline_validation(self) -> None:
        markdown = "[Workflow](../workflows/paired.md)"
        expected = self.source.rewrite(markdown, self.page)
        for relative in self.fixtures:
            self.source.require_path(self.root / relative)
        self.source.verify()
        metadata = self.root / "release/review-source.json"
        metadata.parent.mkdir()
        metadata.write_text(json.dumps(self.source.metadata()), encoding="utf-8", newline="\n")
        self.git("add", "release/review-source.json")
        self.git("-c", "user.name=Review test", "-c", "user.email=test@example.invalid",
                 "-c", "commit.gpgsign=false", "commit", "--quiet", "-m", "Snapshot fixture")
        clone = self.autocrlf_clone()
        configured = subprocess.run(
            ["git", "-C", str(clone), "config", "core.autocrlf"],
            check=True, capture_output=True, text=True,
        ).stdout.strip()
        self.assertEqual(configured, "true")
        for relative in self.fixtures:
            with self.subTest(path=relative):
                self.assertEqual((clone / relative).read_bytes(), (self.root / relative).read_bytes())
        with patch("review_links._git", side_effect=AssertionError("Offline builds must not use Git")):
            offline = ReviewSource.load(clone)
            self.assertEqual(offline.rewrite(markdown, clone / self.page.relative_to(self.root)), expected)
            for relative in self.fixtures:
                offline.require_path(clone / relative)
            offline.verify()
            self.assertEqual(offline.metadata(), self.source.metadata())

    def test_autocrlf_clone_preserves_captured_provider_crlf_and_binary_bytes(self) -> None:
        clone = self.autocrlf_clone()
        provider = "teaching-data/archival-friction/source/provider-ocr.txt"
        original = self.fixtures[provider]
        self.assertIn(b"\r\n", original)
        with self.assertRaises(UnicodeDecodeError):
            original.decode("utf-8")
        self.assertEqual((clone / provider).read_bytes(), original)
        committed = subprocess.run(
            ["git", "-C", str(clone), "show", f"{self.commit}:{provider}"],
            check=True, capture_output=True,
        ).stdout
        self.assertEqual(committed, original)
        binary = "docs/assets/downloads/sample (draft).zip"
        self.assertEqual((clone / binary).read_bytes(), self.fixtures[binary])

    def test_offline_snapshot_rejects_changed_target(self) -> None:
        self.record_fixture()
        target = self.root / "docs/sl/workflows/paired.md"
        target.write_text("# Changed target\n", encoding="utf-8")
        offline = ReviewSource.load(self.root)
        offline.rewrite("[Workflow](../workflows/paired.md)", self.page)
        with self.assertRaisesRegex(ValueError, "differs from its recorded source digest"):
            offline.verify()

    def test_offline_snapshot_rejects_a_changed_dependency_set(self) -> None:
        self.record_fixture()
        offline = ReviewSource.load(self.root)
        offline.rewrite("No workflow link remains.", self.page)
        with self.assertRaisesRegex(ValueError, "paths differ from the recorded snapshot"):
            offline.verify()

    def test_offline_snapshot_rejects_added_directory_content(self) -> None:
        self.source.rewrite(f"[Data]({REPOSITORY_URL}/tree/main/teaching-data/sample)", self.page)
        self.source.verify()
        metadata = self.root / "release/review-source.json"
        metadata.parent.mkdir()
        metadata.write_text(json.dumps(self.source.metadata()), encoding="utf-8")
        (self.root / "teaching-data/sample/new.txt").write_text("new", encoding="utf-8")
        offline = ReviewSource.load(self.root)
        offline.rewrite(f"[Data]({REPOSITORY_URL}/tree/main/teaching-data/sample)", self.page)
        with self.assertRaisesRegex(ValueError, "directory contents differ"):
            offline.verify()

    def test_mutable_or_invalid_commit_ref_is_rejected(self) -> None:
        for reference in ("main", "v1.0", "a" * 39, None):
            with self.subTest(reference=reference), self.assertRaisesRegex(ValueError, "40-character"):
                ReviewSource(self.root, reference, SNAPSHOT_STATUS, "2026-09-07T10:30:00Z")

    def test_link_visitor_preserves_markdown_bytes(self) -> None:
        markdown = '[Link](https://example.org/a_(b) "A title")\n[ref]: <https://example.org>\n'
        self.assertEqual(rewrite_links(markdown, lambda destination: destination), markdown)


if __name__ == "__main__":
    unittest.main()
