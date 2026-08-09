#!/usr/bin/env python3
"""Regression tests for portable Briefing Room export policy and integrity."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


EXECUTION = Path(__file__).resolve().parent
sys.path.insert(0, str(EXECUTION))

import brief_export  # noqa: E402
import verify_brief_export  # noqa: E402


class BriefExportTests(unittest.TestCase):
    def test_sensitive_paths_stay_denied(self) -> None:
        self.assertIsNotNone(brief_export.safe_dependency_reason(".env", False))
        self.assertIsNotNone(brief_export.safe_dependency_reason(".git/config", True))
        self.assertIsNotNone(brief_export.safe_dependency_reason("keys/client.pem", True))
        self.assertIsNotNone(brief_export.safe_dependency_reason(".agent/private.md", False))
        self.assertIsNone(brief_export.safe_dependency_reason(".agent/private.md", True))

    def test_source_root_becomes_provenance_label(self) -> None:
        raw = f"SOURCE: {brief_export.ROOT}/docs/example.md file://docs/example.md"
        portable = brief_export.sanitize_source_roots(raw)
        self.assertNotIn(str(brief_export.ROOT), portable)
        self.assertEqual(portable.count("source-repo://"), 2)

    def test_zip_slip_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / "bad.zip"
            target = Path(tmp) / "out"
            target.mkdir()
            with zipfile.ZipFile(archive, "w") as handle:
                handle.writestr("../escape.txt", "no")
            with self.assertRaises(ValueError):
                verify_brief_export.safe_extract(archive, target)

    def test_manifest_hash_and_context_resolution(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            brief_dir = root / "briefs" / "fixture"
            source = root / "context" / "repo" / "docs" / "source.md"
            brief_dir.mkdir(parents=True)
            source.parent.mkdir(parents=True)
            source.write_text("evidence\n", encoding="utf-8")
            (root / "index.html").write_text(
                '<a href="briefs/fixture/fixture-brief.html">open</a>', encoding="utf-8"
            )
            (brief_dir / "fixture-brief.html").write_text("<html><body>ok</body></html>", encoding="utf-8")
            (brief_dir / "fixture-context.json").write_text(json.dumps({
                "schema_version": brief_export.SCHEMA_VERSION,
                "paths": [{"path": "context/repo/docs/source.md", "scope": "bundle"}],
            }), encoding="utf-8")
            files = []
            for path in sorted(p for p in root.rglob("*") if p.is_file()):
                payload = path.read_bytes()
                files.append({
                    "path": path.relative_to(root).as_posix(),
                    "bytes": len(payload),
                    "sha256": hashlib.sha256(payload).hexdigest(),
                    "kind": "fixture",
                })
            manifest = {
                "schema_version": brief_export.SCHEMA_VERSION,
                "title": "fixture", "audience": "private", "briefs": [{"slug": "fixture"}],
                "files": files, "omissions": [],
            }
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            errors, _ = verify_brief_export.verify(root)
            self.assertEqual(errors, [])

            source.write_text("tampered\n", encoding="utf-8")
            errors, _ = verify_brief_export.verify(root)
            self.assertTrue(any("hash mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
