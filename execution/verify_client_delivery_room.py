#!/usr/bin/env python3
"""Cold-start proof for the Angle Map Client Delivery Room V1."""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path


EXECUTION = Path(__file__).resolve().parent
ROOT = EXECUTION.parent
sys.path.insert(0, str(EXECUTION))

import client_delivery_room as room  # noqa: E402


FIXTURE = ROOT / "deliverables" / "client-rooms" / "angle-map-message-market-fit-v1"


def main() -> int:
    report = room.validate_project(FIXTURE)
    if not report["ready_for_client_export"]:
        print("CLIENT DELIVERY ROOM COLD-START FAIL")
        for error in report["working_errors"] + report["release_errors"]:
            print(f"- {error}")
        return 1

    with tempfile.TemporaryDirectory(prefix="client-room-proof-") as tmp:
        temp = Path(tmp)
        release = temp / "release"
        room.build_release(FIXTURE, release)
        errors = room.verify_release(release)
        if errors:
            print("CLIENT DELIVERY ROOM COLD-START FAIL")
            for error in errors:
                print(f"- {error}")
            return 1

        leak_project = temp / "leak-project"
        shutil.copytree(FIXTURE, leak_project)
        manifest = json.loads((leak_project / room.PROJECT_FILE).read_text(encoding="utf-8"))
        brief_path = leak_project / manifest["paths"]["client_brief"]
        brief = json.loads(brief_path.read_text(encoding="utf-8"))
        brief["dek"] += " Codex worktree implementation note."
        room.write_json(brief_path, brief)
        leak_report = room.validate_project(leak_project)
        if leak_report["ready_for_client_export"]:
            print("CLIENT DELIVERY ROOM COLD-START FAIL")
            print("- intentional client leak was not blocked")
            return 1

        client_zip = release / "client-room.zip"
        private_zip = release / "private-working-room.zip"
        print("CLIENT DELIVERY ROOM COLD-START PASS")
        print("- complete intake produced private and client editions")
        print("- both folders and both ZIPs passed portable verification")
        print("- intentional internal-language leak was blocked before export")
        print(f"- client ZIP sha256: {room.brief_export.sha256_file(client_zip)}")
        print(f"- private ZIP sha256: {room.brief_export.sha256_file(private_zip)}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
