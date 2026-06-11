from __future__ import annotations

import html
import re
import shutil
from pathlib import Path
from typing import Any

from .common import YT_DLP, command_exists, run_command


TIMING_RE = re.compile(
    r"(?P<start>\d{2}:\d{2}:\d{2}\.\d{3}|\d{2}:\d{2}\.\d{3})\s+-->\s+"
    r"(?P<end>\d{2}:\d{2}:\d{2}\.\d{3}|\d{2}:\d{2}\.\d{3})"
)


def fetch_subtitles(url: str, output_dir: Path, video_id: str) -> tuple[Path | None, str, list[dict[str, Any]], list[str]]:
    warnings: list[str] = []
    output_dir.mkdir(parents=True, exist_ok=True)
    if not command_exists(YT_DLP):
        warnings.append(f"yt-dlp unavailable at {YT_DLP}; transcript fetch skipped.")
        return None, "", [], warnings

    before = set(output_dir.glob("*.vtt"))
    template = str(output_dir / f"{video_id}.%(ext)s")
    args = [
        str(YT_DLP),
        "--skip-download",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs",
        "en.*",
        "--sub-format",
        "vtt",
        "-o",
        template,
        url,
    ]
    result = run_command(args, timeout=180)
    after = set(output_dir.glob("*.vtt"))
    candidates = sorted(after - before) or sorted(output_dir.glob(f"{video_id}*.vtt"))
    if result.returncode != 0 and not candidates:
        warnings.append(f"yt-dlp subtitle fetch failed: {result.stderr.strip() or result.stdout.strip()}")
        return None, "", [], warnings
    if not candidates:
        warnings.append("No VTT subtitles were available for this video.")
        return None, "", [], warnings

    vtt_path = candidates[0]
    canonical_vtt = output_dir / "transcript.vtt"
    if vtt_path != canonical_vtt:
        shutil.copyfile(vtt_path, canonical_vtt)
        vtt_path = canonical_vtt
    text, entries = clean_vtt(vtt_path.read_text(encoding="utf-8", errors="ignore"))
    return vtt_path, text, entries, warnings


def clean_vtt(vtt: str) -> tuple[str, list[dict[str, Any]]]:
    entries: list[dict[str, Any]] = []
    current_start: str | None = None
    current_end: str | None = None
    buffer: list[str] = []

    def flush() -> None:
        nonlocal current_start, current_end, buffer
        if current_start is None or not buffer:
            buffer = []
            return
        text = normalize_caption_text(" ".join(buffer))
        if text:
            entries.append(
                {
                    "start": current_start,
                    "end": current_end or current_start,
                    "start_seconds": parse_timestamp(current_start),
                    "end_seconds": parse_timestamp(current_end or current_start),
                    "text": text,
                }
            )
        current_start = None
        current_end = None
        buffer = []

    for raw_line in vtt.splitlines():
        line = raw_line.strip()
        if not line or line == "WEBVTT" or line.startswith(("Kind:", "Language:", "NOTE")):
            flush()
            continue
        timing = TIMING_RE.search(line)
        if timing:
            flush()
            current_start = timing.group("start")
            current_end = timing.group("end")
            continue
        if "-->" in line:
            continue
        if current_start is not None and not line.isdigit():
            buffer.append(line)
    flush()

    segments = collapse_rolling_captions(entries)
    text = format_clean_transcript(segments)
    return text, segments


def collapse_rolling_captions(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Convert YouTube's rolling captions into non-overlapping transcript segments."""
    segments: list[dict[str, Any]] = []
    previous_words: list[str] = []

    for entry in entries:
        text = entry.get("text", "")
        words = text.split()
        if not words:
            continue

        if words == previous_words:
            continue

        if previous_words and is_prefix(words, previous_words):
            previous_words = words
            continue

        overlap = longest_suffix_prefix(previous_words, words)
        new_words = words[overlap:] if previous_words else words
        segment_text = normalize_transcript_spacing(" ".join(new_words))
        previous_words = words

        if not segment_text:
            continue
        if segments and segment_text == segments[-1]["text"]:
            continue

        segment = dict(entry)
        segment["text"] = segment_text
        segment["source_text"] = text
        segment["caption_overlap_words"] = overlap
        segments.append(segment)

    return segments


def is_prefix(shorter: list[str], longer: list[str]) -> bool:
    return len(shorter) < len(longer) and longer[: len(shorter)] == shorter


def longest_suffix_prefix(left: list[str], right: list[str]) -> int:
    max_overlap = min(len(left), len(right))
    for size in range(max_overlap, 0, -1):
        if left[-size:] == right[:size]:
            return size
    return 0


def normalize_transcript_spacing(text: str) -> str:
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def format_clean_transcript(segments: list[dict[str, Any]]) -> str:
    paragraphs: list[str] = []
    current: list[str] = []
    last_end: float | None = None

    def flush() -> None:
        nonlocal current
        paragraph = normalize_transcript_spacing(" ".join(current))
        if paragraph:
            paragraphs.append(paragraph)
        current = []

    for segment in segments:
        start_seconds = segment.get("start_seconds")
        if (
            current
            and isinstance(start_seconds, (int, float))
            and isinstance(last_end, (int, float))
            and start_seconds - last_end > 4
        ):
            flush()

        text = segment.get("text", "")
        if text:
            current.append(text)

        paragraph_text = " ".join(current)
        if len(paragraph_text) > 420 and re.search(r'[.!?]"?$', text):
            flush()

        end_seconds = segment.get("end_seconds")
        if isinstance(end_seconds, (int, float)):
            last_end = end_seconds

    if current:
        flush()

    return "\n\n".join(paragraphs)


def normalize_caption_text(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_timestamp(value: str | None) -> float | None:
    if not value:
        return None
    pieces = value.split(":")
    try:
        if len(pieces) == 3:
            hours = int(pieces[0])
            minutes = int(pieces[1])
            seconds = float(pieces[2])
            return hours * 3600 + minutes * 60 + seconds
        if len(pieces) == 2:
            minutes = int(pieces[0])
            seconds = float(pieces[1])
            return minutes * 60 + seconds
    except ValueError:
        return None
    return None


def transcript_from_fixture(fixture: dict[str, Any]) -> tuple[str, list[dict[str, Any]]]:
    entries = fixture.get("transcript_entries") or []
    normalized = []
    for entry in entries:
        start = entry.get("start") or "00:00"
        text = normalize_caption_text(str(entry.get("text") or ""))
        normalized.append(
            {
                "start": start,
                "end": entry.get("end") or start,
                "start_seconds": entry.get("start_seconds") if entry.get("start_seconds") is not None else parse_timestamp(start),
                "end_seconds": entry.get("end_seconds") if entry.get("end_seconds") is not None else parse_timestamp(entry.get("end") or start),
                "text": text,
            }
        )
    text = format_clean_transcript(normalized)
    return text, normalized
