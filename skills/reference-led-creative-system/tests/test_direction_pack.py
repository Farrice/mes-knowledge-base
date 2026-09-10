#!/usr/bin/env python3
"""Deterministic positive and negative controls for direction_pack.py."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "direction_pack.py"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="direction-pack-test-") as temp:
        root = Path(temp)
        colors = ["#d7d2c8", "#151515", "#b88b62"]
        directions = []
        for index, color in enumerate(colors, start=1):
            image_path = root / f"source-{index}.png"
            Image.new("RGB", (800, 500), color).save(image_path)
            directions.append(
                {
                    "id": chr(64 + index),
                    "name": f"Direction {index}",
                    "preview_path": image_path.name,
                    "primary_reference": {
                        "title": f"Reference {index}",
                        "uuid": f"fixture-{index}",
                    },
                }
            )

        manifest_path = root / "manifest.json"
        manifest_path.write_text(
            json.dumps(
                {
                    "run_id": "fixture-pass",
                    "title": "Direction pack fixture",
                    "directions": directions,
                }
            ),
            encoding="utf-8",
        )
        output_dir = root / "output"
        captured = run(
            "capture",
            "--manifest",
            str(manifest_path),
            "--output-dir",
            str(output_dir),
            "--no-network",
        )
        assert captured.returncode == 0, captured.stderr
        verified = run(
            "verify",
            "--manifest",
            str(manifest_path),
            "--output-dir",
            str(output_dir),
        )
        assert verified.returncode == 0, verified.stderr
        receipt = json.loads((output_dir / "receipt.json").read_text(encoding="utf-8"))
        assert receipt["status"] == "PASS"
        assert receipt["direction_count"] == 3
        assert Path(receipt["contact_sheet"]["local_path"]).is_file()
        assert all(Path(item["local_path"]).is_file() for item in receipt["directions"])

        tampered_preview = Path(receipt["directions"][0]["local_path"])
        tampered_preview.write_bytes(tampered_preview.read_bytes() + b"tamper")
        tampered = run(
            "verify",
            "--manifest",
            str(manifest_path),
            "--output-dir",
            str(output_dir),
        )
        assert tampered.returncode != 0
        assert "Checksum mismatch" in tampered.stderr

        remote_manifest = root / "remote-only.json"
        remote_manifest.write_text(
            json.dumps(
                {
                    "directions": [
                        {
                            "id": "A",
                            "name": "Remote A",
                            "primary_reference": {
                                "title": "Remote reference A",
                                "preview_url": "https://example.com/a.jpg",
                            },
                        },
                        {
                            "id": "B",
                            "name": "Remote B",
                            "primary_reference": {
                                "title": "Remote reference B",
                                "preview_url": "https://example.com/b.jpg",
                            },
                        },
                    ]
                }
            ),
            encoding="utf-8",
        )
        blocked = run(
            "capture",
            "--manifest",
            str(remote_manifest),
            "--output-dir",
            str(root / "blocked"),
            "--no-network",
        )
        assert blocked.returncode != 0
        assert "remote-only" in blocked.stderr

    print(
        "PASS — direction pack capture, checksum-tamper rejection, "
        "and remote-only negative control"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
