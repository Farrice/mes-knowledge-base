#!/usr/bin/env python3
"""Regression tests for the dual-edition client-delivery room."""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


EXECUTION = Path(__file__).resolve().parent
ROOT = EXECUTION.parent
sys.path.insert(0, str(EXECUTION))

import client_delivery_room as room  # noqa: E402


FIXTURE = ROOT / "deliverables" / "client-rooms" / "angle-map-message-market-fit-v1"


class ClientDeliveryRoomTests(unittest.TestCase):
    def copy_fixture(self, target: Path) -> Path:
        project = target / "project"
        shutil.copytree(FIXTURE, project)
        return project

    def test_founding_fixture_is_ready_for_both_editions(self) -> None:
        report = room.validate_project(FIXTURE)
        self.assertEqual(report["working_errors"], [])
        self.assertEqual(report["release_errors"], [])
        self.assertTrue(report["ready_for_client_export"])

    def test_cold_start_builds_and_verifies_both_zips(self) -> None:
        with tempfile.TemporaryDirectory(prefix="client-room-test-") as tmp:
            release = Path(tmp) / "release"
            room.build_release(FIXTURE, release)
            self.assertTrue((release / "private-working-room.zip").is_file())
            self.assertTrue((release / "client-room.zip").is_file())
            self.assertEqual(room.verify_release(release), [])

    def test_client_internal_term_is_blocked_before_export(self) -> None:
        with tempfile.TemporaryDirectory(prefix="client-room-leak-") as tmp:
            project = self.copy_fixture(Path(tmp))
            manifest = json.loads((project / room.PROJECT_FILE).read_text(encoding="utf-8"))
            brief_path = project / manifest["paths"]["client_brief"]
            brief = json.loads(brief_path.read_text(encoding="utf-8"))
            brief["sections"][0]["body"] += " God Agent worktree note."
            room.write_json(brief_path, brief)
            report = room.validate_project(project)
            self.assertFalse(report["ready_for_client_export"])
            self.assertTrue(any("God Agent" in error for error in report["release_errors"]))

    def test_release_hold_blocks_client_but_allows_working_copy(self) -> None:
        with tempfile.TemporaryDirectory(prefix="client-room-hold-") as tmp:
            project = self.copy_fixture(Path(tmp))
            release_path = project / "release-gate.json"
            release = json.loads(release_path.read_text(encoding="utf-8"))
            release["reviews"]["editorial_review"] = "HOLD"
            room.write_json(release_path, release)
            with self.assertRaises(room.ProjectError):
                room.build_release(project, Path(tmp) / "blocked")
            working = Path(tmp) / "working"
            room.build_release(project, working, working_only=True)
            self.assertTrue((working / "private-working-room.zip").is_file())
            self.assertFalse((working / "client-room.zip").exists())
            self.assertEqual(room.verify_release(working), [])

    def test_new_project_starts_on_hold(self) -> None:
        with tempfile.TemporaryDirectory(prefix="client-room-init-") as tmp:
            project = Path(tmp) / "example-client"
            room.init_project(project, "Example Client")
            report = room.validate_project(project)
            self.assertFalse(report["ready_for_working_room"])
            self.assertFalse(report["ready_for_client_export"])
            self.assertTrue(any("intake field" in error for error in report["working_errors"]))


if __name__ == "__main__":
    unittest.main()
