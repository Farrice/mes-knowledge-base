#!/usr/bin/env python3
"""Build the transcript-only source package from preserved YouTube files."""

from __future__ import annotations

import argparse
import html
import json
import re
import textwrap
from pathlib import Path


TIMESTAMP_RE = re.compile(
    r"(?P<sh>\d{2}):(?P<sm>\d{2}):(?P<ss>\d{2})[.,](?P<sms>\d{3})"
    r"\s+-->\s+"
    r"(?P<eh>\d{2}):(?P<em>\d{2}):(?P<es>\d{2})[.,](?P<ems>\d{3})"
)
TAG_RE = re.compile(r"<[^>]+>")


def seconds(hours: str, minutes: str, secs: str, millis: str) -> float:
    return int(hours) * 3600 + int(minutes) * 60 + int(secs) + int(millis) / 1000


def stamp(value: float) -> str:
    total_ms = round(value * 1000)
    hours, remainder = divmod(total_ms, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{millis:03d}"


def parse_cues(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    cues: list[dict] = []
    index = 0
    while index < len(lines):
        match = TIMESTAMP_RE.match(lines[index])
        if not match:
            index += 1
            continue

        values = match.groupdict()
        start = seconds(values["sh"], values["sm"], values["ss"], values["sms"])
        end = seconds(values["eh"], values["em"], values["es"], values["ems"])
        index += 1
        cue_lines: list[str] = []
        while index < len(lines) and lines[index].strip():
            cleaned = html.unescape(TAG_RE.sub("", lines[index])).strip()
            if cleaned:
                cue_lines.append(cleaned)
            index += 1
        cue_text = " ".join(cue_lines)
        cue_text = re.sub(r"\s+", " ", cue_text).strip()
        if cue_text:
            cues.append({"start_seconds": start, "end_seconds": end, "source_text": cue_text})
        index += 1
    return cues


def overlap_words(previous: list[str], current: list[str]) -> int:
    ceiling = min(len(previous), len(current))
    for size in range(ceiling, 0, -1):
        if previous[-size:] == current[:size]:
            return size
    return 0


def transcript_segments(cues: list[dict]) -> list[dict]:
    segments: list[dict] = []
    previous_words: list[str] = []
    for cue in cues:
        current_words = cue["source_text"].split()
        overlap = overlap_words(previous_words, current_words)
        novel_words = current_words[overlap:]
        previous_words = current_words
        if not novel_words:
            continue
        start = cue["start_seconds"]
        end = cue["end_seconds"]
        segments.append(
            {
                "start": stamp(start),
                "end": stamp(end),
                "start_seconds": round(start, 3),
                "end_seconds": round(end, 3),
                "text": " ".join(novel_words),
                "source_text": cue["source_text"],
                "caption_overlap_words": overlap,
            }
        )
    return segments


def clean_transcript(segments: list[dict]) -> str:
    words = " ".join(segment["text"] for segment in segments)
    return "\n\n".join(textwrap.wrap(words, width=1200)) + "\n"


def reduced_metadata(raw: dict) -> dict:
    keys = (
        "id",
        "title",
        "uploader",
        "channel",
        "duration",
        "upload_date",
        "webpage_url",
        "description",
        "chapters",
    )
    return {key: raw.get(key) for key in keys if raw.get(key) is not None}


def ledger_rows(segments: list[dict]) -> list[dict]:
    return [
        {
            "type": "observed_spoken",
            "timestamp": segment["start"],
            "start_seconds": segment["start_seconds"],
            "spoken_evidence": segment["text"],
            "visual_evidence": None,
            "evidence_status": "TRANSCRIPT_BACKED",
        }
        for segment in segments
    ]


def markdown_ledger(rows: list[dict]) -> str:
    lines = [
        "# Video Context Ledger — SupWhagSCm8",
        "",
        "> Transcript-backed spoken evidence from public YouTube auto-captions. Visual frames and OCR were not collected.",
        "",
    ]
    lines.extend(
        f"- **{row['timestamp']}** — {row['spoken_evidence']}" for row in rows
    )
    return "\n".join(lines) + "\n"


def uncertainty_report(segment_count: int, word_count: int) -> str:
    return f"""# Uncertainty Report — SupWhagSCm8

## Evidence Available

- Public YouTube metadata captured with `yt-dlp` on 2026-09-01.
- English auto-captions preserved as `transcript.vtt`.
- Clean transcript and {segment_count:,} timestamped spoken segments generated from the captions ({word_count:,} words).

## Evidence Unavailable

- Visual frames and OCR were not collected. Do not attribute slides, UI state, demonstrations, or on-screen text to this package.
- Speaker diarization was not independently verified.
- Auto-caption punctuation, product names, and proper nouns may contain transcription errors.
- The source is one practitioner's tutorial, not controlled evidence that the demonstrated workflows improve conversion, ranking, or return on ad spend.

## Use Boundary

Treat workflow descriptions as `TRANSCRIPT_BACKED` practitioner instruction. Treat performance, causal, and market-effect claims as `UNTESTED` unless independently verified. Preserve `VERIFIED`, `LIKELY`, `UNCONFIRMED`, `UNTESTED`, and `NO EVENT` states in downstream work.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vtt", type=Path, required=True)
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    cues = parse_cues(args.vtt)
    segments = transcript_segments(cues)
    raw_metadata = json.loads(args.metadata.read_text(encoding="utf-8"))
    rows = ledger_rows(segments)
    transcript = clean_transcript(segments)

    (args.output / "metadata.json").write_text(
        json.dumps(reduced_metadata(raw_metadata), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (args.output / "transcript_segments.json").write_text(
        json.dumps(segments, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (args.output / "transcript.txt").write_text(transcript, encoding="utf-8")
    (args.output / "video-context-ledger.json").write_text(
        json.dumps(rows, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (args.output / "video-context-ledger.md").write_text(markdown_ledger(rows), encoding="utf-8")
    (args.output / "uncertainty-report.md").write_text(
        uncertainty_report(len(segments), len(transcript.split())), encoding="utf-8"
    )

    print(f"SOURCE PACKAGE: {args.output}")
    print(f"CUES: {len(cues)}")
    print(f"SEGMENTS: {len(segments)}")
    print(f"WORDS: {len(transcript.split())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
