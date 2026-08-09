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

    def test_index_uses_premium_minimal_report_contract(self) -> None:
        document = brief_export.build_index("Client Intelligence Room", "share", [{
            "slug": "fixture",
            "meta": {"title": "the useful *decision*", "chip": "CLIENT BRIEF", "dek": "One clear move."},
        }])
        for token in ("#F3F3F0", "#FAFAF8", "#101010", "#555553", "#D8D8D3", "#8C8C82", "#3D5A94"):
            self.assertIn(token, document)
        self.assertIn("'Helvetica Neue'", document)
        self.assertIn("FARRICE CAIN", document)
        self.assertIn("PREMIUM MINIMAL · REPORT DIALECT", document)
        self.assertIn("<em>decision</em>", document)
        self.assertNotIn("#18202a", document)
        self.assertNotIn("background:var(--ink);color", document)

    def test_portable_brief_chrome_uses_same_brand_tokens(self) -> None:
        document = brief_export.apply_portable_brand_chrome("<html><head></head><body><footer class=\"brief\">old</footer></body></html>", "CLIENT EDITION")
        self.assertIn("FARRICE CAIN", document)
        self.assertIn("#F3F3F0", document)
        self.assertIn("#101010", document)
        self.assertIn("'Helvetica Neue'", document)
        self.assertNotIn("#18202a", document)

    def test_share_html_removes_internal_source_commentary(self) -> None:
        document = '''<html><head><style>/* _active/private source */</style></head>
<body><!-- internal note --><script>\n// Every internal link uses a local path\nconst safe = true;</script></body></html>'''
        cleaned = brief_export.sanitize_share_html(document)
        self.assertNotIn("_active/private", cleaned)
        self.assertNotIn("internal note", cleaned)
        self.assertNotIn("Every internal link", cleaned)
        self.assertNotIn("<script", cleaned)

    def test_client_brand_contract_omits_repo_provenance(self) -> None:
        contract = brief_export.client_brand_contract()
        self.assertNotIn("source_provenance", contract)
        self.assertEqual(contract["name"], "Farrice Cain Premium Minimal")

    def test_share_index_uses_client_language(self) -> None:
        document = brief_export.build_index("Client Room", "share", [{
            "slug": "fixture",
            "meta": {"title": "one useful *decision*", "chip": "CLIENT BRIEF", "dek": "Clear evidence."},
        }])
        self.assertIn("CLIENT EDITION", document)
        self.assertIn("About this room", document)
        self.assertNotIn("PORTABLE BRIEFING ROOM · SHARE", document)
        self.assertNotIn(">Manifest<", document)

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
