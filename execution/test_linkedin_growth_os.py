#!/usr/bin/env python3
"""Positive and negative controls for linkedin_growth_os.py."""

from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "execution" / "linkedin_growth_os.py"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(TOOL), *args], cwd=ROOT, text=True, capture_output=True, check=False)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="linkedin-growth-os-") as raw:
        root = Path(raw) / "client"
        result = run("init", "--name", "Fixture", "--offer", "Advisory", "--icp", "B2B founders", "--outcome", "qualified demand", "--mechanism", "source-grounded content", "--output", str(root))
        assert result.returncode == 0, result.stderr
        assert run("doctor", "--workspace", str(root)).returncode == 0

        with (root / "ideas.csv").open("a", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["I-1", "Strong idea", "Proof", "Authority", "call", "5", "4", "", "actionable", "idea"])
            writer.writerow(["I-2", "Weak idea", "Proof", "Authority", "notes", "2", "2", "", "no", "idea"])
        assert run("rank-ideas", "--input", str(root / "ideas.csv")).returncode == 0
        rows = list(csv.DictReader((root / "ideas.csv").open(encoding="utf-8")))
        assert [row["smart_score"] for row in rows] == ["9", "4"]

        bad = root / "bad-ideas.csv"
        bad.write_text((root / "ideas.csv").read_text(encoding="utf-8").replace(",5,4,9,", ",9,4,9,"), encoding="utf-8")
        assert run("rank-ideas", "--input", str(bad)).returncode == 2
        assert run("review", "--input", str(root / "posts.csv"), "--output", str(root / "review.md")).returncode == 2

        with (root / "posts.csv").open("a", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["P-1", "2026-08-29", "Proof beats claims", "Proof", "Authority", "Text", "result-system", "", "1000", "20", "5", "10", "40", "12", "2", "1", "100", "fixture"])
        assert run("review", "--input", str(root / "posts.csv"), "--output", str(root / "review.md")).returncode == 0
        report = (root / "review.md").read_text(encoding="utf-8")
        assert "12.00" in report and "3.50%" in report and "does not prove causality" in report
        (root / "profile.md").unlink()
        assert run("doctor", "--workspace", str(root)).returncode == 1
    print("LinkedIn growth OS tests: PASS (init, ranking, review, and negative controls)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
