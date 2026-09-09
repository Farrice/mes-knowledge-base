#!/usr/bin/env python3
"""Build the frozen Greer source package from already-captured local evidence."""

from __future__ import annotations

import hashlib
import html
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CAPTURE = ROOT / ".tmp/watch-0kkAl04_0og"
OUTPUT = ROOT / "extractions/video-context/0kkAl04_0og"
VTT = CAPTURE / "download/video.en-orig.vtt"
INFO = CAPTURE / "download/video.info.json"
FRAME_DIR = CAPTURE / "storyboard-images"
TIMING = re.compile(r"(?P<start>\d{2}:\d{2}:\d{2}\.\d{3}|\d{2}:\d{2}\.\d{3})\s+-->\s+(?P<end>\d{2}:\d{2}:\d{2}\.\d{3}|\d{2}:\d{2}\.\d{3})")


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
        new = words[overlap:] if previous else words
        previous = words
        text_value = normalize(" ".join(new))
        if not text_value:
            continue
        segments.append({
            "id": f"0kkAl04_0og:s{len(segments):06d}",
            "start": row["start"],
            "end": row["end"],
            "start_seconds": seconds(row["start"]),
            "end_seconds": seconds(row["end"]),
            "text": text_value,
        })
    return segments


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    if not VTT.is_file() or not INFO.is_file():
        raise SystemExit("captured VTT or metadata is missing")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    shutil.copy2(VTT, OUTPUT / "transcript.vtt")
    info = json.loads(INFO.read_text())
    metadata = {key: info.get(key) for key in (
        "id", "title", "webpage_url", "duration", "uploader", "channel", "upload_date", "description"
    )}
    metadata["capture_status"] = "local automatic captions plus unreviewed storyboard contact sheets"
    (OUTPUT / "metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n")

    segments = parse_vtt(VTT.read_text(errors="ignore"))
    (OUTPUT / "transcript_segments.json").write_text(json.dumps(segments, indent=2, ensure_ascii=False) + "\n")
    transcript = "\n\n".join(
        " ".join(row["text"] for row in segments[index:index + 18])
        for index in range(0, len(segments), 18)
    )
    (OUTPUT / "transcript.txt").write_text(transcript + "\n")

    ledger = [{
        "row_id": row["id"], "timestamp": row["start"], "type": "observed_spoken",
        "content": row["text"], "source": "transcript.vtt", "speaker": "UNRESOLVED_FROM_CAPTIONS"
    } for row in segments]
    ledger.append({
        "row_id": "0kkAl04_0og:u000001", "timestamp": "full recording",
        "type": "uncertain_or_unavailable", "content": "Speaker turns are not encoded in the automatic captions; attribution requires human review.",
        "source": "capture limitation", "speaker": "N/A"
    })
    ledger.append({
        "row_id": "0kkAl04_0og:u000002", "timestamp": "full recording",
        "type": "uncertain_or_unavailable", "content": "Storyboard contact sheets were preserved but not promoted to observed visual claims.",
        "source": "visual review limitation", "speaker": "N/A"
    })
    (OUTPUT / "video-context-ledger.json").write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n")
    rows = ["# Andrew Sean Greer Video Context Ledger", "", "| Row | Timestamp | Lane | Content | Source |", "|---|---:|---|---|---|"]
    for row in ledger:
        content = row["content"].replace("|", "\\|")
        rows.append(f"| `{row['row_id']}` | {row['timestamp']} | `{row['type']}` | {content} | `{row['source']}` |")
    (OUTPUT / "video-context-ledger.md").write_text("\n".join(rows) + "\n")

    frames_out = OUTPUT / "storyboard-images"
    frames_out.mkdir(exist_ok=True)
    for frame in sorted(FRAME_DIR.glob("storyboard-*.jpg")):
        shutil.copy2(frame, frames_out / frame.name)
    (OUTPUT / "uncertainty-report.md").write_text(
        "# Uncertainty Report\n\n"
        "- Captions are automatic and may contain transcription errors.\n"
        "- Speaker turns are not encoded; downstream doctrine uses the human-reviewed `SOURCE-LEDGER.md`, not raw rows alone.\n"
        "- Direct video-stream retrieval returned HTTP 403 during capture.\n"
        "- Forty-nine storyboard contact sheets are preserved, but no visual or OCR claim is admitted without a later human review.\n"
        "- The package proves source preservation, not skill effectiveness, Greer authorship of every utterance, or deployment readiness.\n"
    )
    files = sorted(path for path in OUTPUT.rglob("*") if path.is_file() and path.name != "manifest.json")
    manifest = {"video_id": "0kkAl04_0og", "proof_boundary": "capture integrity only", "files": [
        {"path": str(path.relative_to(OUTPUT)), "bytes": path.stat().st_size, "sha256": sha(path)} for path in files
    ]}
    (OUTPUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"GREER SOURCE PACKAGE BUILT: {len(segments)} spoken rows, {len(files)} frozen files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
