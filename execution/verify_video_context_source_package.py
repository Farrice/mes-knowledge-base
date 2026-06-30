#!/usr/bin/env python3
"""Verify a YouTube video-context source package is extraction-ready."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_FILES = (
    "metadata.json",
    "transcript.vtt",
    "transcript.txt",
    "transcript_segments.json",
    "video-context-ledger.md",
    "video-context-ledger.json",
    "uncertainty-report.md",
)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def timestamped_line_ratio(text: str) -> float:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return 1.0
    timestamped = sum(1 for line in lines if re.match(r"^\[\d{2}:\d{2}", line.strip()))
    return timestamped / len(lines)


def verify_package(package_dir: Path) -> tuple[bool, list[str], list[str]]:
    failures: list[str] = []
    notes: list[str] = []

    if not package_dir.exists():
        return False, [f"Package directory missing: {package_dir}"], notes

    for filename in REQUIRED_FILES:
        path = package_dir / filename
        if not path.exists():
            failures.append(f"Missing required file: {filename}")
        elif path.stat().st_size == 0:
            failures.append(f"Required file is empty: {filename}")

    metadata_path = package_dir / "metadata.json"
    if metadata_path.exists() and metadata_path.stat().st_size:
        try:
            metadata = read_json(metadata_path)
            if not (metadata.get("id") or metadata.get("webpage_url") or metadata.get("original_url")):
                failures.append("metadata.json lacks a video id or URL field")
        except json.JSONDecodeError as exc:
            failures.append(f"metadata.json is not valid JSON: {exc}")

    segments_path = package_dir / "transcript_segments.json"
    if segments_path.exists() and segments_path.stat().st_size:
        try:
            segments = read_json(segments_path)
            if not isinstance(segments, list) or not segments:
                failures.append("transcript_segments.json must be a non-empty list")
            else:
                missing_fields = [
                    index
                    for index, segment in enumerate(segments[:20], start=1)
                    if not isinstance(segment, dict) or not segment.get("start") or not segment.get("text")
                ]
                if missing_fields:
                    failures.append("first transcript segments must include start and text")
                notes.append(f"Transcript segments: {len(segments)}")
        except json.JSONDecodeError as exc:
            failures.append(f"transcript_segments.json is not valid JSON: {exc}")

    transcript_path = package_dir / "transcript.txt"
    if transcript_path.exists() and transcript_path.stat().st_size:
        transcript = transcript_path.read_text(encoding="utf-8", errors="ignore")
        if len(transcript.split()) < 100:
            failures.append("transcript.txt appears too short for extraction")
        if timestamped_line_ratio(transcript) > 0.2:
            failures.append("transcript.txt is still row-shaped; expected clean continuous transcript")
        notes.append(f"Clean transcript words: {len(transcript.split())}")

    ledger_path = package_dir / "video-context-ledger.json"
    if ledger_path.exists() and ledger_path.stat().st_size:
        try:
            ledger = read_json(ledger_path)
            if not isinstance(ledger, list) or not ledger:
                failures.append("video-context-ledger.json must be a non-empty list")
            else:
                observed_spoken = sum(1 for row in ledger if isinstance(row, dict) and row.get("type") == "observed_spoken")
                if observed_spoken == 0:
                    failures.append("video-context-ledger.json has no observed_spoken rows")
                notes.append(f"Observed spoken ledger rows: {observed_spoken}")
        except json.JSONDecodeError as exc:
            failures.append(f"video-context-ledger.json is not valid JSON: {exc}")

    return not failures, failures, notes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", help="Path to extractions/video-context/<video-id>")
    args = parser.parse_args()

    package_dir = Path(args.package)
    ok, failures, notes = verify_package(package_dir)
    if ok:
        print(f"Video context source package: PASS ({package_dir})")
        for note in notes:
            print(f"- {note}")
        return 0

    print(f"Video context source package: FAIL ({package_dir})")
    for failure in failures:
        print(f"- {failure}")
    for note in notes:
        print(f"- {note}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
