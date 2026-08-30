#!/usr/bin/env python3
"""Build a frozen transcript-only package for The Futur storytelling source."""

from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path


VIDEO_ID = "FFPaVFBEIhI"
OUTPUT = Path(__file__).resolve().parent
VTT = OUTPUT / "transcript.vtt"
TIMING = re.compile(
    r"(?P<start>\d{2}:\d{2}:\d{2}\.\d{3}|\d{2}:\d{2}\.\d{3})\s+-->\s+"
    r"(?P<end>\d{2}:\d{2}:\d{2}\.\d{3}|\d{2}:\d{2}\.\d{3})"
)


def seconds(value: str) -> float:
    parts = value.split(":")
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    return int(parts[0]) * 60 + float(parts[1])


def normalize(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = html.unescape(value).replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", value).strip()


def parse_vtt(text: str) -> list[dict]:
    raw: list[dict] = []
    start = end = None
    buffer: list[str] = []

    def flush() -> None:
        nonlocal start, end, buffer
        caption = normalize(" ".join(buffer))
        if start and caption:
            raw.append({"start": start, "end": end or start, "text": caption})
        start = end = None
        buffer = []

    for line in text.splitlines():
        line = line.strip()
        match = TIMING.search(line)
        if match:
            flush()
            start, end = match.group("start"), match.group("end")
        elif not line or line == "WEBVTT" or line.startswith(("Kind:", "Language:", "NOTE")):
            flush()
        elif start and not line.isdigit() and "-->" not in line:
            buffer.append(line)
    flush()

    segments: list[dict] = []
    previous: list[str] = []
    for row in raw:
        words = row["text"].split()
        if not words or words == previous:
            continue
        overlap = 0
        for size in range(min(len(previous), len(words)), 0, -1):
            if previous[-size:] == words[:size]:
                overlap = size
                break
        new_words = words[overlap:] if previous else words
        previous = words
        text_value = normalize(" ".join(new_words))
        if not text_value:
            continue
        segments.append(
            {
                "id": f"{VIDEO_ID}:s{len(segments):06d}",
                "start": row["start"],
                "end": row["end"],
                "start_seconds": seconds(row["start"]),
                "end_seconds": seconds(row["end"]),
                "text": text_value,
            }
        )
    return segments


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    if not VTT.is_file():
        raise SystemExit("transcript.vtt is missing")

    segments = parse_vtt(VTT.read_text(encoding="utf-8", errors="ignore"))
    transcript = "\n\n".join(
        " ".join(row["text"] for row in segments[index : index + 18])
        for index in range(0, len(segments), 18)
    )
    metadata = {
        "id": VIDEO_ID,
        "title": "Stop Promoting Your Business. Start Telling Better Stories.",
        "uploader": "The Futur",
        "webpage_url": f"https://www.youtube.com/watch?v={VIDEO_ID}",
        "duration": 2711.131,
        "retrieved": "2026-08-29",
        "capture_status": "YouTube automatic English captions; visual stream unavailable",
    }
    (OUTPUT / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (OUTPUT / "transcript_segments.json").write_text(
        json.dumps(segments, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (OUTPUT / "transcript.txt").write_text(transcript + "\n", encoding="utf-8")

    ledger = [
        {
            "row_id": row["id"],
            "timestamp": row["start"],
            "type": "observed_spoken",
            "content": row["text"],
            "source": "transcript.vtt",
            "speaker": "UNRESOLVED_FROM_CAPTIONS",
        }
        for row in segments
    ]
    ledger.extend(
        [
            {
                "row_id": f"{VIDEO_ID}:u000001",
                "timestamp": "full recording",
                "type": "uncertain_or_unavailable",
                "content": "Speaker turns are not encoded in the automatic captions.",
                "source": "capture limitation",
                "speaker": "N/A",
            },
            {
                "row_id": f"{VIDEO_ID}:u000002",
                "timestamp": "full recording",
                "type": "uncertain_or_unavailable",
                "content": "Video frames and OCR were unavailable because YouTube media formats required a PO token that the configured provider could not generate.",
                "source": "visual capture limitation",
                "speaker": "N/A",
            },
        ]
    )
    (OUTPUT / "video-context-ledger.json").write_text(
        json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    rows = [
        "# The Futur Storytelling Video Context Ledger",
        "",
        "| Row | Timestamp | Lane | Content | Source |",
        "|---|---:|---|---|---|",
    ]
    for row in ledger:
        content = row["content"].replace("|", "\\|")
        rows.append(
            f"| `{row['row_id']}` | {row['timestamp']} | `{row['type']}` | {content} | `{row['source']}` |"
        )
    (OUTPUT / "video-context-ledger.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    (OUTPUT / "frame-notes.md").write_text(
        "# Frame Notes\n\nFrames were not captured; no visual claims are admitted.\n", encoding="utf-8"
    )
    (OUTPUT / "ocr-notes.md").write_text(
        "# OCR Notes\n\nOCR was not run because frames were unavailable.\n", encoding="utf-8"
    )
    (OUTPUT / "uncertainty-report.md").write_text(
        "# Uncertainty Report\n\n"
        "- Captions are automatic and may contain transcription errors.\n"
        "- Speaker turns are unresolved; downstream claims must not rely on attribution that the captions do not prove.\n"
        "- Video frames, slide text, body language, and demonstrations were not observed.\n"
        "- The package proves transcript capture and timestamped spoken evidence, not method effectiveness or deployment readiness.\n",
        encoding="utf-8",
    )

    files = sorted(
        path for path in OUTPUT.iterdir() if path.is_file() and path.name != "manifest.json"
    )
    manifest = {
        "video_id": VIDEO_ID,
        "proof_boundary": "transcript capture integrity only",
        "segments": len(segments),
        "words": len(transcript.split()),
        "files": [
            {"path": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)}
            for path in files
        ],
    }
    (OUTPUT / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"FUTUR SOURCE PACKAGE BUILT: {len(segments)} spoken rows, "
        f"{len(transcript.split())} clean words, {len(files)} frozen files"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
