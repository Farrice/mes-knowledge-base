#!/usr/bin/env python3
"""Build a timestamped YouTube video context ledger."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from video_context.common import OUTPUT_ROOT, read_json, write_json
from video_context.frames import frame_notes, sample_frames
from video_context.ledger import build_ledger, markdown_ledger, uncertainty_report
from video_context.metadata import fetch_metadata, fixture_metadata
from video_context.ocr import ocr_notes, run_ocr
from video_context.report import write_analysis
from video_context.transcript import fetch_subtitles, transcript_from_fixture


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a YouTube video context ledger.")
    parser.add_argument("url", nargs="?", help="Public YouTube URL or video id.")
    parser.add_argument("--mode", choices=["transcript", "full", "fixture"], default="transcript")
    parser.add_argument("--fixture", help="Fixture JSON path for offline smoke tests.")
    parser.add_argument("--interval", type=int, default=60, help="Frame sample interval in seconds for full mode.")
    args = parser.parse_args()

    if args.mode == "fixture":
        return run_fixture(Path(args.fixture or "execution/video_context/fixtures/sample_video_context.json"))

    if not args.url:
        parser.error("url is required unless --mode fixture is used")

    metadata, metadata_warnings = fetch_metadata(args.url)
    video_id = metadata.get("id") or "unknown-video"
    output_dir = OUTPUT_ROOT / video_id
    output_dir.mkdir(parents=True, exist_ok=True)
    write_json(output_dir / "metadata.json", metadata)

    vtt_path, transcript_text, transcript_entries, transcript_warnings = fetch_subtitles(args.url, output_dir, video_id)
    write_json(output_dir / "transcript_segments.json", transcript_entries)
    if transcript_text:
        (output_dir / "transcript.txt").write_text(transcript_text + "\n", encoding="utf-8")
    else:
        (output_dir / "transcript.txt").write_text("", encoding="utf-8")

    frames: list[dict[str, Any]] = []
    frame_warnings: list[str] = []
    ocr_rows: list[dict[str, Any]] = []
    ocr_warnings: list[str] = []
    if args.mode == "full":
        frames, frame_warnings = sample_frames(args.url, output_dir, metadata.get("duration"), args.interval)
        ocr_rows, ocr_warnings = run_ocr(frames)
    else:
        frame_warnings.append("Frame extraction skipped because mode is transcript.")
        ocr_warnings.append("OCR skipped because mode is transcript.")

    warnings = metadata_warnings + transcript_warnings + frame_warnings + ocr_warnings
    ledger_rows = build_ledger(transcript_entries, frames, ocr_rows, warnings)
    write_json(output_dir / "video-context-ledger.json", ledger_rows)
    (output_dir / "video-context-ledger.md").write_text(markdown_ledger(ledger_rows), encoding="utf-8")
    (output_dir / "frame-notes.md").write_text(frame_notes(frames, frame_warnings), encoding="utf-8")
    (output_dir / "ocr-notes.md").write_text(ocr_notes(ocr_rows, ocr_warnings), encoding="utf-8")
    (output_dir / "uncertainty-report.md").write_text(uncertainty_report(ledger_rows, warnings), encoding="utf-8")
    write_analysis(output_dir, metadata, ledger_rows, transcript_text, len(frames), len(ocr_rows))

    print(f"Video context package written to: {output_dir}")
    print(f"Ledger rows: {len(ledger_rows)}")
    if vtt_path:
        print(f"Transcript VTT: {vtt_path}")
    if warnings:
        print(f"Warnings: {len(warnings)}")
    return 0


def run_fixture(path: Path) -> int:
    fixture = read_json(path)
    metadata = fixture_metadata(fixture)
    video_id = metadata.get("id", "fixture-video")
    output_dir = OUTPUT_ROOT / video_id
    output_dir.mkdir(parents=True, exist_ok=True)

    transcript_text, transcript_entries = transcript_from_fixture(fixture)
    frames = fixture.get("frames") or []
    ocr_rows = fixture.get("ocr_rows") or []
    visual_notes = fixture.get("visual_notes") or []
    warnings = ["Fixture mode: no live YouTube, ffmpeg, or OCR adapter was used."]

    write_json(output_dir / "metadata.json", metadata)
    write_json(output_dir / "transcript_segments.json", transcript_entries)
    (output_dir / "transcript.txt").write_text(transcript_text + "\n", encoding="utf-8")
    ledger_rows = build_ledger(transcript_entries, frames, ocr_rows, warnings, visual_notes=visual_notes)
    write_json(output_dir / "video-context-ledger.json", ledger_rows)
    (output_dir / "video-context-ledger.md").write_text(markdown_ledger(ledger_rows), encoding="utf-8")
    (output_dir / "frame-notes.md").write_text(frame_notes(frames, []), encoding="utf-8")
    (output_dir / "ocr-notes.md").write_text(ocr_notes(ocr_rows, []), encoding="utf-8")
    (output_dir / "uncertainty-report.md").write_text(uncertainty_report(ledger_rows, warnings), encoding="utf-8")
    write_analysis(output_dir, metadata, ledger_rows, transcript_text, len(frames), len(ocr_rows))
    print(f"Fixture video context package written to: {output_dir}")
    print(f"Ledger rows: {len(ledger_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
