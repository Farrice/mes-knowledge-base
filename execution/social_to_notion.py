#!/usr/bin/env python3
"""
social_to_notion.py — Social URL -> rich Notion page, end to end.

CONTRACT: one command, any supported social URL in, one Notion page out —
metadata + embedded video + full transcript + engagement stats + a source
ledger (what was fetched, with what tool, and what degraded). This is the
glue the system was missing between apify_client.py / fetch-transcript.py
(acquisition) and notion_api.py (delivery).

Platform routing (by URL hostname):
    youtube.com / youtu.be -> fetch-transcript.py (youtube-transcript-api)
                              falling back to Apify sc-youtube-transcripts;
                              metadata via Apify `youtube` actor only if the
                              transcript path yielded none.
    tiktok.com             -> Apify sc-tiktok-video (metadata/stats) +
                              sc-tiktok-transcripts (transcript), unless
                              --no-transcript.
    instagram.com          -> Apify `instagram` (post/profile metadata).
    reddit.com              -> Apify `reddit`.
    linkedin.com            -> exit 2 (not in the approved actor whitelist).
    anything else            -> exit 2 (unsupported host).

Budget discipline: at most 3 Apify calls per invocation (hard local counter,
independent of apify_client.py's own $/month guard). Every Apify response is
checked for `.get("fallback")` / `status == "budget_exhausted"` (or any
other error/skip status) and the run degrades gracefully — never crashes,
never retries a fallback response.

Normalizes acquisition into one record dict:
    {platform, url, source_id, title, author, published,
     stats: {views, likes, comments, shares},
     transcript, embed_url, fetched_at, degraded: [...]}
Missing fields are always None — never invented.

--dry-run performs acquisition (network permitting) but NEVER calls Notion;
it prints the normalized record and the exact Notion payload (properties +
first block batch + total block count) as JSON. --transcript-file injects a
transcript from disk so dry-run is fully testable offline.

Usage:
    python3 execution/social_to_notion.py <url> [--db content|knowledge|captures]
        [--dry-run] [--transcript-file PATH] [--tags tag1,tag2]
        [--no-transcript] [--limit N]
    python3 execution/social_to_notion.py --watch-packet PATH [--topics a,b]
        [--inspection-receipt PATH] [--dry-run]

Exit codes: 0 ok, 1 failure, 2 skip/unsupported (bad host, LinkedIn, etc.)
"""

import argparse
import hashlib
import importlib.util
import json
import math
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import parse_qs, urlparse

BASE = Path(__file__).parent.parent
ENV_PATH = BASE / ".env"

MAX_APIFY_CALLS = 3
WATCH_PACKET_SCHEMA = "watch-video-intelligence/v1"
WATCH_RECEIPT_SCHEMA = "watch-visual-inspection/v1"
EVIDENCE_STATES = {
    "TRANSCRIPT_ONLY",
    "VISUAL_CAPTURED_UNREVIEWED",
    "PARTIAL_VISUAL_VERIFIED",
    "VISUAL_VERIFIED",
}
SHA256_RE = re.compile(r"[0-9a-f]{64}")
MAX_NOTION_TIMELINE_ROWS = 60
MAX_NOTION_TRANSCRIPT_CHARS = 250_000
MAX_NOTION_TRANSCRIPT_JSON_BYTES = 140_000
MAX_NOTION_TIMELINE_FIELD_JSON_BYTES = 800
MAX_NOTION_REQUEST_BYTES = 450_000

LINKEDIN_MESSAGE = (
    "LinkedIn scraping is not in the approved actor whitelist — see "
    "_active/knowledge/youtube-notion-replication/FULL-PICTURE.md § LinkedIn gap"
)


# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

def load_env(env_path: Optional[Path] = None):
    """Load .env into os.environ (setdefault — won't override existing)."""
    path = env_path or ENV_PATH
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# /watch packet bridge (no reacquisition)
# ---------------------------------------------------------------------------

def canonical_post_url(url: str) -> str:
    """Return one public YouTube dedup URL for the v1 /watch bridge."""
    value = str(url or "").strip()
    parsed = urlparse(value)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise ValueError("watch packets require a public http(s) canonical URL for Notion sync")

    host = parsed.hostname.lower()
    host = host[4:] if host.startswith("www.") else host
    if host == "m.youtube.com":
        host = "youtube.com"
    video_id = None
    if host == "youtu.be":
        video_id = parsed.path.strip("/").split("/")[0]
    elif host == "youtube.com" or host.endswith(".youtube.com"):
        video_id = (parse_qs(parsed.query).get("v") or [None])[0]
        if not video_id:
            match = re.match(r"^/(?:shorts|embed|v|live)/([A-Za-z0-9_-]{11})(?:/|$)", parsed.path)
            video_id = match.group(1) if match else None
    if video_id and re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
        return f"https://www.youtube.com/watch?v={video_id}"
    raise ValueError("watch-packet Notion sync v1 supports exact public YouTube video URLs only")


def normalize_topics(*values, limit: int = 12) -> list[str]:
    """Normalize caller/packet topics without inventing a second taxonomy."""
    topics: list[str] = []
    for value in values:
        if not value:
            continue
        candidates = value.split(",") if isinstance(value, str) else value
        for candidate in candidates:
            topic = " ".join(str(candidate).strip().split())[:60]
            if topic and topic.casefold() not in {item.casefold() for item in topics}:
                topics.append(topic)
            if len(topics) >= limit:
                return topics
    return topics


def _json_sha256(value) -> str:
    payload = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _ocr_integrity_rows(rows: list) -> list[dict]:
    return [
        {
            "timestamp_seconds": row.get("timestamp_seconds"),
            "status": row.get("status"),
            "text": row.get("text") or "",
        }
        for row in rows
        if isinstance(row, dict)
    ]


def _frame_integrity_rows(rows: list) -> list[dict]:
    return [
        {
            "timestamp_seconds": row.get("timestamp_seconds"),
            "reason": row.get("reason"),
            "width": row.get("width"),
            "height": row.get("height"),
            "sha256": row.get("sha256"),
        }
        for row in rows
        if isinstance(row, dict)
    ]


def _alignment_integrity_rows(rows: list) -> list[dict]:
    return [
        {
            "timestamp_seconds": row.get("timestamp_seconds"),
            "sha256": row.get("sha256"),
            "reason": row.get("reason"),
            "width": row.get("width"),
            "height": row.get("height"),
            "review_status": row.get("review_status"),
            "alignment_method": row.get("alignment_method"),
            "alignment_distance_seconds": row.get("alignment_distance_seconds"),
            "transcript": [
                {
                    "start": segment.get("start"),
                    "end": segment.get("end"),
                    "text": segment.get("text") or "",
                }
                for segment in row.get("transcript") or []
            ],
            "ocr": {
                "status": (row.get("ocr") or {}).get("status"),
                "text": (row.get("ocr") or {}).get("text") or "",
            },
        }
        for row in rows
        if isinstance(row, dict)
    ]


def _source_integrity_metadata(source: dict) -> dict:
    is_url_source = source.get("kind") == "url"
    return {
        "kind": source.get("kind"),
        "id": source.get("id") if is_url_source else None,
        "canonical_url": source.get("canonical_url") if is_url_source else None,
        "title": source.get("title") if is_url_source else None,
        "uploader": source.get("uploader") if is_url_source else None,
        "published": source.get("published") if is_url_source else None,
    }


def _ocr_meta_integrity(ocr: dict) -> dict:
    return {
        "status": ocr.get("status"),
        "reason": ocr.get("reason"),
        "attempted": ocr.get("attempted"),
        "succeeded": ocr.get("succeeded"),
        "nonempty": ocr.get("nonempty"),
        "failed": ocr.get("failed"),
    }


def _direct_media_integrity(acquisition: dict) -> dict:
    direct = acquisition.get("direct_media") or {}
    return {"status": direct.get("status"), "reason": direct.get("reason")}


def _transcript_meta_integrity(transcript: dict) -> dict:
    return {
        "status": transcript.get("status"),
        "source": transcript.get("source"),
        "segment_count": transcript.get("segment_count"),
    }


def _visual_meta_integrity(visual: dict) -> dict:
    return {
        "status": visual.get("status"),
        "evidence_label": visual.get("evidence_label"),
        "captured_count": visual.get("captured_count"),
        "reviewed_count": visual.get("reviewed_count"),
        "engine": visual.get("engine"),
        "candidate_count": visual.get("candidate_count"),
    }


def validate_watch_packet(packet: dict, *, verify_artifacts: bool = True) -> None:
    """Validate schema shape plus the producer's content-bound integrity basis."""
    if not isinstance(packet, dict) or packet.get("schema_version") != WATCH_PACKET_SCHEMA:
        raise ValueError(f"watch packet must use schema_version {WATCH_PACKET_SCHEMA}")
    fingerprint = str(packet.get("fingerprint") or "")
    packet_id = str(packet.get("packet_id") or "")
    if not SHA256_RE.fullmatch(fingerprint) or not packet_id.endswith(fingerprint[:16]):
        raise ValueError("watch packet is missing a valid packet_id/fingerprint binding")

    visual = packet.get("visual") or {}
    frames = visual.get("frames")
    if not isinstance(frames, list):
        raise ValueError("watch packet visual.frames must be a list")
    captured_count = int(visual.get("captured_count") or 0)
    if captured_count != len(frames):
        raise ValueError("watch packet captured_count does not match actual frame rows")
    frame_keys = set()
    frame_timestamps = set()
    for frame in frames:
        if not isinstance(frame, dict) or not SHA256_RE.fullmatch(str(frame.get("sha256") or "")):
            raise ValueError("every captured frame must carry a SHA256 digest")
        path_text = str(frame.get("path") or "").strip()
        timestamp = float(frame.get("timestamp_seconds") or 0)
        if not path_text or not math.isfinite(timestamp) or timestamp < 0:
            raise ValueError("every captured frame requires a path and finite nonnegative timestamp")
        rounded_timestamp = round(timestamp, 3)
        if rounded_timestamp in frame_timestamps:
            raise ValueError("watch packet contains duplicate frame timestamps")
        frame_timestamps.add(rounded_timestamp)
        key = (str(Path(path_text).resolve()), rounded_timestamp)
        if key in frame_keys:
            raise ValueError("watch packet contains duplicate frame path/timestamp rows")
        frame_keys.add(key)
        if verify_artifacts:
            path = Path(path_text).expanduser().resolve()
            if not path.exists() or not path.is_file() or _file_sha256(path) != frame["sha256"]:
                raise ValueError(f"captured frame artifact is missing or changed: {path}")

    transcript = packet.get("transcript") or {}
    segments = transcript.get("segments")
    if not isinstance(segments, list) or int(transcript.get("segment_count") or 0) != len(segments):
        raise ValueError("watch packet transcript segment_count does not match its rows")
    for segment in segments:
        if not isinstance(segment, dict):
            raise ValueError("watch packet transcript segments must be objects")
        start = float(segment.get("start") or 0)
        end = float(segment.get("end") if segment.get("end") is not None else start)
        if not math.isfinite(start) or not math.isfinite(end) or start < 0 or end < start:
            raise ValueError("watch packet transcript timestamps must be finite and ordered")
    transcript_text = transcript.get("text")
    if transcript_text is not None and not isinstance(transcript_text, str):
        raise ValueError("watch packet transcript.text must be a string or null")
    expected_transcript_status = "pass" if segments else "unavailable"
    if transcript.get("status") != expected_transcript_status:
        raise ValueError("watch packet transcript status does not match its evidence rows")

    ocr = packet.get("ocr") or {}
    ocr_rows = ocr.get("rows") or []
    if not isinstance(ocr_rows, list):
        raise ValueError("watch packet ocr.rows must be a list")
    attempted = int(ocr.get("attempted") or 0)
    nonempty = int(ocr.get("nonempty") or 0)
    if attempted != len(ocr_rows) or nonempty != sum(
        1 for row in ocr_rows if isinstance(row, dict) and str(row.get("text") or "").strip()
    ):
        raise ValueError("watch packet OCR counts do not match its evidence rows")
    ocr_by_frame = {}
    for row in ocr_rows:
        if not isinstance(row, dict):
            raise ValueError("watch packet OCR rows must be objects")
        path_text = str(row.get("path") or "").strip()
        timestamp = float(row.get("timestamp_seconds") or 0)
        if not path_text or not math.isfinite(timestamp) or timestamp < 0:
            raise ValueError("watch packet OCR rows require a path and finite timestamp")
        key = (str(Path(path_text).resolve()), round(timestamp, 3))
        if key in ocr_by_frame:
            raise ValueError("watch packet contains duplicate OCR rows")
        ocr_by_frame[key] = {
            "status": row.get("status"),
            "text": row.get("text") or "",
        }

    alignment_frames = (packet.get("alignment") or {}).get("frames") or []
    if not isinstance(alignment_frames, list) or (frames and len(alignment_frames) != len(frames)):
        raise ValueError("watch packet alignment row count does not match captured frames")
    frame_by_alignment_key = {
        (round(float(row.get("timestamp_seconds") or 0), 3), row.get("sha256")): row
        for row in frames
    }
    transcript_members = {
        (
            float(row.get("start") or 0),
            float(row.get("end") if row.get("end") is not None else row.get("start") or 0),
            str(row.get("text") or ""),
        )
        for row in segments
    }
    aligned_keys = set()
    for row in alignment_frames:
        if not isinstance(row, dict):
            raise ValueError("watch packet alignment rows must be objects")
        key = (round(float(row.get("timestamp_seconds") or 0), 3), row.get("sha256"))
        if key in aligned_keys or key not in frame_by_alignment_key:
            raise ValueError("watch packet alignment rows do not map uniquely to captured frames")
        aligned_keys.add(key)
        frame = frame_by_alignment_key[key]
        if str(Path(str(row.get("path") or "")).resolve()) != str(Path(str(frame.get("path") or "")).resolve()):
            raise ValueError("watch packet alignment path does not match its captured frame")
        if row.get("reason") != (frame.get("reason") or "selected"):
            raise ValueError("watch packet alignment reason does not match its captured frame")
        if row.get("width") != frame.get("width") or row.get("height") != frame.get("height"):
            raise ValueError("watch packet alignment dimensions do not match its captured frame")
        if row.get("review_status") != "not_inspected":
            raise ValueError("watch packet alignment rows cannot self-claim visual review")
        distance = row.get("alignment_distance_seconds")
        if distance is not None and (not math.isfinite(float(distance)) or float(distance) < 0):
            raise ValueError("watch packet alignment distance must be null or finite and nonnegative")
        for aligned_segment in row.get("transcript") or []:
            member = (
                float(aligned_segment.get("start") or 0),
                float(aligned_segment.get("end") if aligned_segment.get("end") is not None else aligned_segment.get("start") or 0),
                str(aligned_segment.get("text") or ""),
            )
            if member not in transcript_members:
                raise ValueError("watch packet alignment contains transcript evidence absent from transcript.segments")
        ocr_key = (str(Path(str(frame.get("path") or "")).resolve()), key[0])
        expected_ocr = ocr_by_frame.get(ocr_key, {"status": "not_run", "text": ""})
        actual_ocr = {
            "status": (row.get("ocr") or {}).get("status"),
            "text": (row.get("ocr") or {}).get("text") or "",
        }
        if actual_ocr != expected_ocr:
            raise ValueError("watch packet alignment OCR does not match its OCR evidence row")
    if aligned_keys != set(frame_by_alignment_key):
        raise ValueError("watch packet alignment rows do not cover the captured frames")
    expected_visual = (
        ("captured_unreviewed", "VISUALS_EXTRACTED_NOT_INSPECTED")
        if frames else
        ("unavailable", "TRANSCRIPT_ONLY" if segments else "NO_EVIDENCE")
    )
    if int(visual.get("reviewed_count") or 0) != 0 or (
        visual.get("status"), visual.get("evidence_label")
    ) != expected_visual:
        raise ValueError("watch packet visual proof state does not match its unreviewed evidence")

    integrity = packet.get("integrity") or {}
    basis = integrity.get("basis")
    if integrity.get("algorithm") != "sha256" or not isinstance(basis, dict):
        raise ValueError("watch packet is missing its watch-capture-integrity/v1 basis")
    source = packet.get("source") or {}
    if source.get("kind") == "url":
        if source.get("identity") != source.get("canonical_url") or source.get("content_sha256") is not None:
            raise ValueError("watch URL source identity is not bound to its canonical URL")
    elif source.get("kind") == "local":
        content_sha = str(source.get("content_sha256") or "")
        if not SHA256_RE.fullmatch(content_sha) or source.get("identity") != f"sha256:{content_sha}":
            raise ValueError("watch local source identity is not bound to its content SHA256")
    else:
        raise ValueError("watch packet source.kind must be url or local")
    acquisition = packet.get("acquisition") or {}
    limitations = packet.get("limitations") or []
    if not isinstance(limitations, list) or not all(isinstance(item, str) for item in limitations):
        raise ValueError("watch packet limitations must be a list of strings")
    expected_basis = {
        "schema_version": "watch-capture-integrity/v1",
        "source_identity": source.get("identity"),
        "source_content_sha256": source.get("content_sha256"),
        "source_metadata": _source_integrity_metadata(source),
        "scope": packet.get("scope") or {},
        "capture_config": packet.get("capture") or {},
        "transcript_sha256": _json_sha256(segments),
        "transcript_text_sha256": _json_sha256(transcript_text or ""),
        "transcript_meta_sha256": _json_sha256(_transcript_meta_integrity(transcript)),
        "frames": _frame_integrity_rows(frames),
        "ocr_sha256": _json_sha256(_ocr_integrity_rows(ocr_rows)),
        "ocr_meta_sha256": _json_sha256(_ocr_meta_integrity(ocr)),
        "alignment_sha256": _json_sha256(_alignment_integrity_rows(alignment_frames)),
        "visual_source": acquisition.get("visual_source"),
        "visual_meta_sha256": _json_sha256(_visual_meta_integrity(visual)),
        "direct_media_sha256": _json_sha256(_direct_media_integrity(acquisition)),
        "limitations_sha256": _json_sha256(limitations),
    }
    if basis != expected_basis or _json_sha256(basis) != fingerprint:
        raise ValueError("watch packet fingerprint does not match its evidence content")


def _validate_inspection_receipt(receipt: dict, packet: dict) -> None:
    validate_watch_packet(packet)
    if not isinstance(receipt, dict) or receipt.get("schema_version") != WATCH_RECEIPT_SCHEMA:
        raise ValueError(f"inspection receipt must use schema_version {WATCH_RECEIPT_SCHEMA}")
    state = receipt.get("review_state")
    if state not in {"PARTIAL_VISUAL_VERIFIED", "VISUAL_VERIFIED"}:
        raise ValueError("inspection receipt review_state must be PARTIAL_VISUAL_VERIFIED or VISUAL_VERIFIED")
    source_id = str((packet.get("source") or {}).get("id") or "")
    if source_id and str(receipt.get("source_id") or "") != source_id:
        raise ValueError("inspection receipt source_id does not match the watch packet")
    if str(receipt.get("packet_fingerprint") or "") != str(packet.get("fingerprint") or ""):
        raise ValueError("inspection receipt fingerprint does not match the watch packet")

    packet_frames = (packet.get("visual") or {}).get("frames") or []
    captured = int(receipt.get("captured_count") or 0)
    reviewed = int(receipt.get("reviewed_count") or 0)
    reviewed_frames = receipt.get("reviewed_frames")
    if not isinstance(reviewed_frames, list) or len(reviewed_frames) != reviewed:
        raise ValueError("inspection receipt reviewed_count does not match reviewed frame rows")
    if captured != len(packet_frames) or reviewed < 1 or reviewed > captured:
        raise ValueError("inspection receipt has invalid captured/reviewed counts")

    available = {
        (Path(str(row.get("path") or "")).name, round(float(row.get("timestamp_seconds") or 0), 3), row.get("sha256"))
        for row in packet_frames
    }
    seen = set()
    for row in reviewed_frames:
        key = (
            Path(str(row.get("path") or "")).name,
            round(float(row.get("timestamp_seconds") or 0), 3),
            row.get("sha256"),
        )
        if key not in available or key in seen:
            raise ValueError("inspection receipt contains an unmapped or duplicate reviewed frame")
        if not str(row.get("observation") or "").strip():
            raise ValueError("every reviewed frame requires a nonblank observation")
        seen.add(key)
    if state == "VISUAL_VERIFIED" and seen != available:
        raise ValueError("VISUAL_VERIFIED requires every captured frame to be reviewed")
    if state == "VISUAL_VERIFIED" and (packet.get("acquisition") or {}).get("visual_source") == "storyboard":
        raise ValueError("sparse storyboard evidence cannot be promoted to VISUAL_VERIFIED")


def _watch_sync_fingerprint(packet: dict, evidence_state: str, topics: list[str], receipt: Optional[dict]) -> str:
    reviewed = []
    if receipt:
        reviewed = [
            {
                "path": Path(str(row.get("path") or "")).name,
                "timestamp_seconds": row.get("timestamp_seconds"),
                "sha256": row.get("sha256"),
                "observation": str(row.get("observation") or "").strip(),
            }
            for row in receipt.get("reviewed_frames") or []
        ]
    return _json_sha256({
        "packet_fingerprint": packet["fingerprint"],
        "evidence_state": evidence_state,
        "topics": topics,
        "coverage_limit": (receipt or {}).get("coverage_limit"),
        "reviewed_frames": reviewed,
    })


def load_watch_packet(path: str | Path) -> dict:
    packet_path = Path(path).expanduser().resolve()
    try:
        packet = json.loads(packet_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"could not read watch packet: {exc}") from exc
    validate_watch_packet(packet)
    packet["_packet_path"] = str(packet_path)
    return packet


def load_inspection_receipt(path: str | Path, packet: dict) -> dict:
    receipt_path = Path(path).expanduser().resolve()
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"could not read visual inspection receipt: {exc}") from exc
    _validate_inspection_receipt(receipt, packet)
    receipt["_receipt_path"] = str(receipt_path)
    return receipt


def _first_spoken_line(transcript: dict, title: str) -> str:
    segments = transcript.get("segments") if isinstance(transcript.get("segments"), list) else []
    for row in segments:
        text = " ".join(str(row.get("text") or "").split())
        if text:
            return text[:500]
    for line in str(transcript.get("text") or "").splitlines():
        text = re.sub(r"^\[[^]]+\]\s*", "", line).strip()
        if text:
            return text[:500]
    return title[:500]


def normalize_published_date(value) -> Optional[str]:
    if value in (None, ""):
        return None
    compact = None
    if isinstance(value, int) and not isinstance(value, bool):
        compact = str(value)
    elif isinstance(value, float) and math.isfinite(value) and value.is_integer():
        compact = str(int(value))
    else:
        compact = str(value).strip()
    if re.fullmatch(r"\d{8}", compact):
        try:
            return datetime.strptime(compact, "%Y%m%d").date().isoformat()
        except ValueError:
            return None
    if isinstance(value, (int, float)) and math.isfinite(float(value)):
        try:
            return datetime.fromtimestamp(float(value), tz=timezone.utc).date().isoformat()
        except (OverflowError, OSError, ValueError):
            return None
    text = str(value).strip()
    if re.match(r"^\d{4}-\d{2}-\d{2}", text):
        try:
            return datetime.fromisoformat(text[:10]).date().isoformat()
        except ValueError:
            return None
    return None


def watch_packet_to_record(
    packet: dict,
    *,
    topics: str | list[str] = "",
    inspection_receipt: Optional[dict] = None,
) -> dict:
    validate_watch_packet(packet)
    if inspection_receipt:
        _validate_inspection_receipt(inspection_receipt, packet)
    source = packet.get("source") or {}
    canonical_url = canonical_post_url(source.get("canonical_url") or "")
    transcript = packet.get("transcript") or {}
    visual = packet.get("visual") or {}
    ocr = packet.get("ocr") or {}
    acquisition = packet.get("acquisition") or {}
    alignment = packet.get("alignment") or {}
    segments = transcript.get("segments") if isinstance(transcript.get("segments"), list) else []
    transcript_text = str(transcript.get("text") or "").strip()
    if not transcript_text and segments:
        transcript_text = "\n".join(str(row.get("text") or "").strip() for row in segments).strip()
    captured_count = int(visual.get("captured_count") or 0)
    if captured_count:
        evidence_state = "VISUAL_CAPTURED_UNREVIEWED"
    elif transcript_text or segments:
        evidence_state = "TRANSCRIPT_ONLY"
    else:
        raise ValueError("watch packet contains neither transcript nor visual evidence")
    if inspection_receipt:
        evidence_state = inspection_receipt["review_state"]

    title = str(source.get("title") or source.get("id") or canonical_url)
    raw_duration = (packet.get("scope") or {}).get("duration_seconds")
    duration = None if raw_duration is None else float(raw_duration)
    if duration is not None and (not math.isfinite(duration) or duration < 0):
        raise ValueError("watch packet duration_seconds must be a finite nonnegative number")
    packet_topics = ((packet.get("catalog") or {}).get("topics") or [])
    direct_media = acquisition.get("direct_media") or {}
    analysis = (
        f"Evidence: {evidence_state}. Visual route: {acquisition.get('visual_source') or 'none'}. "
        f"Transcript: {len(segments)} segments. OCR: {int(ocr.get('nonempty') or 0)} non-empty "
        f"of {int(ocr.get('attempted') or 0)} attempted. Direct media: "
        f"{direct_media.get('status') or 'unknown'}"
    )[:1900]

    observations = {}
    if inspection_receipt:
        observations = {
            round(float(row.get("timestamp_seconds") or 0.0), 3): str(row.get("observation") or "").strip()
            for row in inspection_receipt.get("reviewed_frames") or []
        }
    timeline = []
    for row in alignment.get("frames") or visual.get("frames") or []:
        item = dict(row)
        stamp = round(float(item.get("timestamp_seconds") or 0.0), 3)
        if observations.get(stamp):
            item["review_observation"] = observations[stamp]
        timeline.append(item)

    normalized_topics = normalize_topics(packet_topics, topics)
    sync_fingerprint = _watch_sync_fingerprint(
        packet, evidence_state, normalized_topics, inspection_receipt
    )
    return {
        "packet_id": packet["packet_id"],
        "fingerprint": packet["fingerprint"],
        "sync_fingerprint": sync_fingerprint,
        "packet_path": packet.get("_packet_path"),
        "inspection_receipt_path": inspection_receipt.get("_receipt_path") if inspection_receipt else None,
        # canonical_post_url() is deliberately YouTube-only for bridge v1.
        "platform": "YouTube",
        "url": canonical_url,
        "source_id": source.get("id"),
        "title": title,
        "creator": source.get("uploader"),
        "published": normalize_published_date(source.get("published")),
        "duration_seconds": duration,
        "type": "Short" if duration is not None and 0 < duration <= 60 else "Video",
        "scraped": now_iso()[:10],
        "hook": _first_spoken_line(transcript, title),
        "analysis": analysis,
        "batch": f"watch:{packet['fingerprint']}",
        "evidence_state": evidence_state,
        "topics": normalized_topics,
        "transcript": transcript_text,
        "transcript_segments": segments,
        "timeline": timeline,
        "acquisition": acquisition,
        "ocr": ocr,
        "limitations": list(packet.get("limitations") or []),
        "inspection": inspection_receipt,
    }


# ---------------------------------------------------------------------------
# Module loaders (hyphenated filename, apify_client)
# ---------------------------------------------------------------------------

def _load_fetch_transcript_module():
    """fetch-transcript.py has a hyphen in its name — import via spec since
    a plain `import` statement can't reference it.

    Returns None (never raises, never exits the process) if the module
    can't be loaded — e.g. the optional `youtube-transcript-api` dependency
    is missing, which makes fetch-transcript.py call sys.exit(1) at import
    time. Callers must fall back gracefully (local regex extraction + Apify
    transcript actor) rather than crash the whole script over an optional dep.
    """
    # fetch-transcript.py prints an error + sys.exit(1) at *import time* if
    # youtube-transcript-api isn't installed. Check the dependency first so
    # we never trigger that noisy side effect (which would otherwise pollute
    # our stdout JSON output) — just fall back cleanly.
    if importlib.util.find_spec("youtube_transcript_api") is None:
        return None
    try:
        spec = importlib.util.spec_from_file_location(
            "fetch_transcript_mod", BASE / "execution" / "fetch-transcript.py"
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    except BaseException:
        return None


_VIDEO_ID_PATTERNS = [
    r'^[a-zA-Z0-9_-]{11}$',
    r'[?&]v=([a-zA-Z0-9_-]{11})',
    r'youtu\.be/([a-zA-Z0-9_-]{11})',
    r'youtube\.com/embed/([a-zA-Z0-9_-]{11})',
    r'youtube\.com/v/([a-zA-Z0-9_-]{11})',
]


def _extract_video_id_fallback(url_or_id: str) -> Optional[str]:
    """Local re-implementation of fetch-transcript.py's extract_video_id,
    used only when that module can't be imported (missing optional dep)."""
    import re
    if re.match(_VIDEO_ID_PATTERNS[0], url_or_id):
        return url_or_id
    for pattern in _VIDEO_ID_PATTERNS[1:]:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return None


def _load_apify_client_module():
    spec = importlib.util.spec_from_file_location(
        "apify_client_mod", BASE / "execution" / "apify_client.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# Apify call budget
# ---------------------------------------------------------------------------

class ApifyBudget:
    """Hard local counter — at most MAX_APIFY_CALLS Apify calls per
    invocation of this script, independent of apify_client.py's own
    dollar-denominated monthly guard."""

    def __init__(self, apify_mod, max_calls: int = MAX_APIFY_CALLS):
        self.apify_mod = apify_mod
        self.max_calls = max_calls
        self.calls_made = 0

    def run(self, actor_key: str, run_input: dict, max_results: int) -> dict:
        if self.calls_made >= self.max_calls:
            return {
                "status": "call_budget_exhausted",
                "fallback": True,
                "message": (
                    f"social_to_notion.py local Apify call cap "
                    f"({self.max_calls}/invocation) reached before calling "
                    f"'{actor_key}'."
                ),
                "items": [],
            }
        self.calls_made += 1
        return self.apify_mod.run_actor(actor_key, run_input, max_results)


def is_degraded(result: dict) -> bool:
    """True if an Apify (or acquisition) response should be treated as a
    degraded/failed fetch rather than a usable result."""
    if not isinstance(result, dict):
        return True
    if result.get("fallback"):
        return True
    if result.get("status") not in ("ok", None):
        return True
    return False


# ---------------------------------------------------------------------------
# Normalized record
# ---------------------------------------------------------------------------

def new_record(platform: str, url: str) -> dict:
    return {
        "platform": platform,
        "url": url,
        "source_id": None,
        "title": None,
        "author": None,
        "published": None,
        "stats": {"views": None, "likes": None, "comments": None, "shares": None},
        "transcript": None,
        "embed_url": url,
        "fetched_at": now_iso(),
        "degraded": [],
        "ledger": [],  # [{tool, note}] — what was actually used
    }


def ledger_note(record: dict, tool: str, note: str):
    record["ledger"].append({"tool": tool, "note": note, "ts": now_iso()})


def _inject_transcript_file(record: dict, args):
    """--transcript-file always wins over any live fetch (offline-testable
    contract) — shared by every platform acquirer."""
    if not args.transcript_file:
        return
    try:
        record["transcript"] = Path(args.transcript_file).read_text(encoding="utf-8")
        ledger_note(record, "transcript-file", f"injected from {args.transcript_file}")
    except OSError as e:
        record["degraded"].append(f"failed to read --transcript-file: {e}")


def _dry_run_no_token_skip(record: dict, args, note: str) -> bool:
    """Returns True (and marks the record degraded-but-titled) if this is a
    dry run with no APIFY_TOKEN configured — Apify calls would just error,
    so skip them and let dry-run stay offline-friendly."""
    if args.dry_run and not os.environ.get("APIFY_TOKEN"):
        record["degraded"].append(f"dry-run: {note} (no APIFY_TOKEN)")
        record["title"] = record["title"] or record["url"]
        return True
    return False


def _fetch_single_item(record: dict, budget: ApifyBudget, actor_key: str,
                        run_input: dict, ledger_tool: str, ledger_desc: str) -> Optional[dict]:
    """Run one Apify actor expecting a single result item. Handles the
    degraded/zero-items/ledger bookkeeping shared by every metadata call —
    returns the item dict, or None (with `record` already updated) on any
    failure/degrade."""
    result = budget.run(actor_key, run_input, 1)
    if is_degraded(result):
        record["degraded"].append(
            f"Apify {actor_key} degraded: {result.get('message', result.get('status'))}"
        )
        return None
    items = result.get("items", [])
    if not items:
        record["degraded"].append(f"Apify {actor_key} returned zero items")
        return None
    ledger_note(record, ledger_tool, ledger_desc)
    return items[0]


# ---------------------------------------------------------------------------
# Platform: YouTube
# ---------------------------------------------------------------------------

def acquire_youtube(url: str, args, budget: ApifyBudget) -> dict:
    record = new_record("youtube", url)

    ft_mod = _load_fetch_transcript_module()
    if ft_mod is None:
        record["degraded"].append(
            "fetch-transcript.py unavailable (youtube-transcript-api not installed) — "
            "using local video-id regex fallback"
        )
        video_id = _extract_video_id_fallback(url)
    else:
        try:
            video_id = ft_mod.extract_video_id(url)
        except ValueError as e:
            record["degraded"].append(f"could not extract video id: {e}")
            video_id = None

    if video_id:
        record["source_id"] = video_id
        record["embed_url"] = f"https://www.youtube.com/embed/{video_id}"
    else:
        record["degraded"].append("could not extract a video id from the URL")

    _inject_transcript_file(record, args)
    if not record["transcript"] and not args.no_transcript and video_id and ft_mod is not None:
        try:
            record["transcript"] = ft_mod.fetch_transcript(video_id)
            ledger_note(record, "fetch-transcript.py", "youtube-transcript-api")
        except Exception as e:
            record["degraded"].append(f"youtube-transcript-api failed: {e}")
            # Fallback: Apify sc-youtube-transcripts
            t_item = _fetch_single_item(record, budget, "sc-youtube-transcripts",
                                         {"videoUrls": [url]}, "apify:sc-youtube-transcripts",
                                         "fallback transcript")
            if t_item:
                text = t_item.get("transcript") or t_item.get("text")
                if text:
                    record["transcript"] = text
                else:
                    record["degraded"].append("Apify sc-youtube-transcripts returned no transcript field")

    # Metadata: only hit Apify's `youtube` actor if we still have no title —
    # keep Apify calls minimal per the budget contract.
    if not record["title"] and not args.dry_run:
        item = _fetch_single_item(record, budget, "youtube",
                                   {"startUrls": [{"url": url}], "maxItems": 1},
                                   "apify:youtube", "metadata")
        if item:
            record["title"] = item.get("title")
            record["author"] = item.get("channelName") or item.get("author")
            record["published"] = item.get("date") or item.get("uploadDate")
            record["stats"]["views"] = item.get("viewCount") or item.get("views")
            record["stats"]["likes"] = item.get("likes")
            record["stats"]["comments"] = item.get("commentsCount") or item.get("comments")
    elif not record["title"] and args.dry_run and not args.transcript_file:
        record["degraded"].append("dry-run: metadata fetch skipped (no network / not attempted)")

    record["title"] = record["title"] or record["source_id"] or url

    return record


# ---------------------------------------------------------------------------
# Platform: TikTok
# ---------------------------------------------------------------------------

def acquire_tiktok(url: str, args, budget: ApifyBudget) -> dict:
    record = new_record("tiktok", url)
    _inject_transcript_file(record, args)

    if _dry_run_no_token_skip(record, args, "metadata/transcript fetch skipped"):
        return record

    item = _fetch_single_item(record, budget, "sc-tiktok-video", {"videos": [url]},
                               "apify:sc-tiktok-video", "metadata/stats")
    if item:
        record["source_id"] = item.get("id") or item.get("videoId")
        record["title"] = item.get("desc") or item.get("title") or item.get("text")
        author_meta = item.get("authorMeta")
        record["author"] = author_meta.get("name") if isinstance(author_meta, dict) else item.get("author")
        record["published"] = item.get("createTime") or item.get("createTimeISO")
        stats = item.get("stats") if isinstance(item.get("stats"), dict) else item
        record["stats"]["views"] = stats.get("playCount") or stats.get("views")
        record["stats"]["likes"] = stats.get("diggCount") or stats.get("likes")
        record["stats"]["comments"] = stats.get("commentCount") or stats.get("comments")
        record["stats"]["shares"] = stats.get("shareCount") or stats.get("shares")

    if not args.no_transcript and not record["transcript"]:
        t_item = _fetch_single_item(record, budget, "sc-tiktok-transcripts", {"videos": [url]},
                                     "apify:sc-tiktok-transcripts", "transcript")
        if t_item:
            text = t_item.get("transcript") or t_item.get("text")
            if text:
                record["transcript"] = text
            else:
                record["degraded"].append("Apify sc-tiktok-transcripts returned no transcript field")

    record["title"] = record["title"] or record["source_id"] or url
    return record


# ---------------------------------------------------------------------------
# Platform: Instagram
# ---------------------------------------------------------------------------

def acquire_instagram(url: str, args, budget: ApifyBudget) -> dict:
    record = new_record("instagram", url)
    _inject_transcript_file(record, args)

    if _dry_run_no_token_skip(record, args, "metadata fetch skipped"):
        return record

    item = _fetch_single_item(
        record, budget, "instagram",
        {"directUrls": [url], "resultsType": "posts", "resultsLimit": 1},
        "apify:instagram", "post/profile metadata",
    )
    if item:
        record["source_id"] = item.get("id") or item.get("shortCode")
        record["title"] = item.get("caption") or item.get("title")
        record["author"] = item.get("ownerUsername") or item.get("author")
        record["published"] = item.get("timestamp")
        record["stats"]["likes"] = item.get("likesCount")
        record["stats"]["comments"] = item.get("commentsCount")
        record["stats"]["views"] = item.get("videoViewCount") or item.get("videoPlayCount")

    record["degraded"].append("no transcript expected for instagram")
    record["title"] = record["title"] or record["source_id"] or url
    return record


# ---------------------------------------------------------------------------
# Platform: Reddit
# ---------------------------------------------------------------------------

def acquire_reddit(url: str, args, budget: ApifyBudget) -> dict:
    record = new_record("reddit", url)
    _inject_transcript_file(record, args)

    if _dry_run_no_token_skip(record, args, "metadata fetch skipped"):
        return record

    item = _fetch_single_item(
        record, budget, "reddit",
        {"startUrls": [{"url": url}], "maxItems": 1, "skipComments": True,
         "skipUserPosts": False, "skipCommunity": False},
        "apify:reddit", "post metadata",
    )
    if item:
        record["source_id"] = item.get("id")
        record["title"] = item.get("title")
        record["author"] = item.get("username") or item.get("author")
        record["published"] = item.get("createdAt") or item.get("date")
        record["stats"]["likes"] = item.get("upVotes") or item.get("score")
        record["stats"]["comments"] = item.get("numberOfComments")

    record["title"] = record["title"] or record["source_id"] or url
    return record


# ---------------------------------------------------------------------------
# Routing
# ---------------------------------------------------------------------------

def route_platform(url: str) -> Optional[str]:
    host = (urlparse(url).hostname or "").lower()
    host = host[4:] if host.startswith("www.") else host

    if host in ("youtube.com", "m.youtube.com") or host.endswith(".youtube.com") or host == "youtu.be":
        return "youtube"
    if host == "tiktok.com" or host.endswith(".tiktok.com"):
        return "tiktok"
    if host == "instagram.com" or host.endswith(".instagram.com"):
        return "instagram"
    if host == "reddit.com" or host.endswith(".reddit.com") or host == "redd.it":
        return "reddit"
    if host == "linkedin.com" or host.endswith(".linkedin.com"):
        return "linkedin"
    return None


ACQUIRERS = {
    "youtube": acquire_youtube,
    "tiktok": acquire_tiktok,
    "instagram": acquire_instagram,
    "reddit": acquire_reddit,
}


# ---------------------------------------------------------------------------
# Notion payload construction
# ---------------------------------------------------------------------------

def chunk_text(text: str, size: int = 1900) -> list:
    if not text:
        return []
    return [text[i:i + size] for i in range(0, len(text), size)]


def build_notion_payload(record: dict, notion_api, db_id: str, args) -> dict:
    """Returns {"properties": ..., "children": [...]} — the full block list
    (caller batches it into <=100-block create + append chunks)."""

    props_wanted = {
        "Name": {"title": {}},
        "Platform": {"select": {"options": [
            {"name": "youtube"}, {"name": "tiktok"},
            {"name": "instagram"}, {"name": "reddit"},
        ]}},
        "Author": {"rich_text": {}},
        "Source URL": {"rich_text": {}},
        "Views": {"number": {}},
        "Likes": {"number": {}},
        "Comments": {"number": {}},
        "Fetched": {"date": {}},
        "Tags": {"multi_select": {}},
    }
    available = notion_api._ensure_properties(db_id, props_wanted)

    properties = {}
    if "Name" in available:
        properties["Name"] = notion_api.title(record["title"] or record["url"])
    if "Platform" in available:
        properties["Platform"] = notion_api.select(record["platform"])
    if "Author" in available and record["author"]:
        properties["Author"] = notion_api.rich_text(str(record["author"]))
    if "Source URL" in available:
        properties["Source URL"] = notion_api.rich_text(record["url"])
    if "Views" in available and record["stats"]["views"] is not None:
        properties["Views"] = notion_api.number(record["stats"]["views"])
    if "Likes" in available and record["stats"]["likes"] is not None:
        properties["Likes"] = notion_api.number(record["stats"]["likes"])
    if "Comments" in available and record["stats"]["comments"] is not None:
        properties["Comments"] = notion_api.number(record["stats"]["comments"])
    if "Fetched" in available:
        properties["Fetched"] = notion_api.date(record["fetched_at"][:10])
    if "Tags" in available and args.tags:
        tags = [t.strip() for t in args.tags.split(",") if t.strip()]
        if tags:
            properties["Tags"] = notion_api.multi_select(tags)

    children = []

    # Embed block — NotionBlocks has no embed builder, construct inline.
    children.append({"object": "block", "type": "embed", "embed": {"url": record["url"]}})

    if record["degraded"]:
        children.append(notion_api.heading2("DEGRADED"))
        for reason in record["degraded"]:
            children.append(notion_api.para(f"DEGRADED: {reason}"))

    if record["transcript"]:
        children.append(notion_api.heading2("Transcript"))
        for chunk in chunk_text(record["transcript"]):
            children.append(notion_api.para(chunk))
    elif not args.no_transcript:
        children.append(notion_api.heading2("Transcript"))
        children.append(notion_api.para("(no transcript available)"))

    children.append(notion_api.heading2("Source Ledger"))
    children.append(notion_api.bullet(f"Platform: {record['platform']}"))
    children.append(notion_api.bullet(f"Fetched: {record['fetched_at']}"))
    for entry in record["ledger"]:
        children.append(notion_api.bullet(f"{entry['tool']}: {entry['note']}"))
    if not record["ledger"]:
        children.append(notion_api.bullet("No acquisition tool recorded"))
    for reason in record["degraded"]:
        children.append(notion_api.bullet(f"Degradation: {reason}"))

    return {"properties": properties, "children": children}


def _timestamp_label(seconds: float) -> str:
    whole = max(0, int(float(seconds or 0)))
    return f"{whole // 60:02d}:{whole % 60:02d}"


def _even_sample_rows(rows: list, limit: int) -> list:
    if len(rows) <= limit:
        return list(rows)
    if limit <= 1:
        return [rows[0]]
    indices = sorted({round(i * (len(rows) - 1) / (limit - 1)) for i in range(limit)})
    return [rows[index] for index in indices]


def _json_wire_bytes(value) -> int:
    """Match requests' default JSON serialization, including Unicode escapes."""
    return len(json.dumps(value, separators=(",", ":"), allow_nan=False).encode("utf-8"))


def _truncate_json_string(value, max_bytes: int) -> str:
    """Return the longest prefix whose requests-style JSON string fits."""
    text = str(value or "")
    if _json_wire_bytes(text) <= max_bytes:
        return text
    low, high = 0, len(text)
    while low < high:
        midpoint = (low + high + 1) // 2
        if _json_wire_bytes(text[:midpoint]) <= max_bytes:
            low = midpoint
        else:
            high = midpoint - 1
    return text[:low]


def build_social_intel_payload(record: dict, notion_api, db_id: str) -> dict:
    """Build the existing Social Intelligence schema from one /watch packet."""
    props_wanted = {
        "Name": {"title": {}},
        "Creator": {"rich_text": {}},
        "Platform": {"select": {"options": [{"name": "YouTube"}]}},
        "Type": {"select": {"options": [{"name": "Video"}, {"name": "Short"}]}},
        "Post URL": {"url": {}},
        "Duration (s)": {"number": {"format": "number"}},
        "Posted": {"date": {}},
        "Scraped": {"date": {}},
        "Hook": {"rich_text": {}},
        "Analysis": {"rich_text": {}},
        "Batch": {"rich_text": {}},
        "Watch Fingerprint": {"rich_text": {}},
        "Evidence State": {"select": {"options": [{"name": item} for item in sorted(EVIDENCE_STATES)]}},
        "Topics": {"multi_select": {}},
        "Extract Candidate": {"checkbox": {}},
    }
    available = notion_api._ensure_properties(db_id, props_wanted)
    essential = {
        "Name", "Platform", "Type", "Post URL", "Scraped", "Analysis", "Batch",
        "Watch Fingerprint", "Evidence State", "Topics", "Extract Candidate",
    }
    missing = sorted(essential - set(available))
    if missing:
        raise RuntimeError(f"Social Intelligence schema is missing required properties: {', '.join(missing)}")

    properties = {
        "Name": notion_api.title(record["title"][:500]),
        "Platform": notion_api.select(record["platform"]),
        "Type": notion_api.select(record["type"]),
        "Post URL": {"url": record["url"]},
        "Scraped": notion_api.date(record["scraped"]),
        "Analysis": notion_api.rich_text(record["analysis"][:1900]),
        "Batch": notion_api.rich_text(record["batch"]),
        "Watch Fingerprint": notion_api.rich_text(record["sync_fingerprint"]),
        "Evidence State": notion_api.select(record["evidence_state"]),
        "Topics": notion_api.multi_select(record["topics"]),
        "Extract Candidate": notion_api.checkbox(False),
    }
    if "Creator" in available and record.get("creator"):
        properties["Creator"] = notion_api.rich_text(str(record["creator"])[:1900])
    if "Duration (s)" in available and record.get("duration_seconds"):
        properties["Duration (s)"] = notion_api.number(record["duration_seconds"])
    if "Posted" in available and record.get("published"):
        properties["Posted"] = notion_api.date(str(record["published"])[:10])
    if "Hook" in available and record.get("hook"):
        properties["Hook"] = notion_api.rich_text(record["hook"][:1900])

    children = [
        {"object": "block", "type": "embed", "embed": {"url": record["url"]}},
        notion_api.heading2("Evidence Summary"),
        notion_api.bullet(f"Evidence state: {record['evidence_state']}"),
        notion_api.bullet(f"Acquisition route: {record['acquisition'].get('visual_source') or 'none'}"),
        notion_api.bullet(f"Transcript segments: {len(record['transcript_segments'])}"),
        notion_api.bullet(
            f"OCR: {int(record['ocr'].get('nonempty') or 0)} non-empty of "
            f"{int(record['ocr'].get('attempted') or 0)} attempted"
        ),
    ]
    if record.get("inspection") and record["inspection"].get("coverage_limit"):
        children.append(notion_api.bullet(f"Review coverage: {record['inspection']['coverage_limit']}"))

    timeline_rows = _even_sample_rows(record.get("timeline") or [], MAX_NOTION_TIMELINE_ROWS)
    if timeline_rows:
        children.append(notion_api.heading2("Timestamped Visual Timeline"))
        if len(timeline_rows) < len(record["timeline"]):
            children.append(notion_api.bullet(
                f"Showing {len(timeline_rows)} evenly spaced rows from {len(record['timeline'])}; full evidence remains in the packet."
            ))
        for row in timeline_rows:
            timestamp = _timestamp_label(row.get("timestamp_seconds") or 0)
            parts = [f"[{timestamp}]", str(row.get("reason") or "frame")]
            ocr = row.get("ocr") or {}
            if isinstance(ocr, dict) and str(ocr.get("text") or "").strip():
                observed_text = _truncate_json_string(
                    " ".join(str(ocr["text"]).split()), MAX_NOTION_TIMELINE_FIELD_JSON_BYTES
                )
                parts.append(f"On-screen text: {observed_text}")
            spoken = row.get("transcript") if isinstance(row.get("transcript"), list) else []
            spoken_text = " ".join(str(item.get("text") or "").strip() for item in spoken).strip()
            if spoken_text:
                parts.append(
                    f"Spoken: {_truncate_json_string(spoken_text, MAX_NOTION_TIMELINE_FIELD_JSON_BYTES)}"
                )
            if row.get("review_observation"):
                parts.append(
                    "Reviewed observation: "
                    + _truncate_json_string(
                        row["review_observation"], MAX_NOTION_TIMELINE_FIELD_JSON_BYTES
                    )
                )
            frame_name = Path(str(row.get("path") or "")).name
            if frame_name:
                parts.append(f"Local artifact: {frame_name}")
            children.append(notion_api.para(" | ".join(parts)))

    children.append(notion_api.heading2("Transcript"))
    if record.get("transcript"):
        transcript_body = _truncate_json_string(
            record["transcript"][:MAX_NOTION_TRANSCRIPT_CHARS],
            MAX_NOTION_TRANSCRIPT_JSON_BYTES,
        )
        for chunk in chunk_text(transcript_body, 150_000):
            children.append(notion_api.para(chunk))
        if len(record["transcript"]) > len(transcript_body):
            children.append(notion_api.para(
                f"Transcript truncated in Notion to a size-safe {len(transcript_body):,}-character excerpt; "
                "the full transcript remains in the watch packet."
            ))
    else:
        children.append(notion_api.para("(no transcript available)"))

    children.append(notion_api.heading2("Source Ledger"))
    children.append(notion_api.bullet(f"Packet: {record['packet_id']}"))
    children.append(notion_api.bullet(f"Fingerprint: {record['fingerprint']}"))
    children.append(notion_api.bullet(f"Watch sync fingerprint: {record['sync_fingerprint']}"))
    direct = record["acquisition"].get("direct_media") or {}
    children.append(notion_api.bullet(f"Direct media: {direct.get('status') or 'unknown'}"))
    if direct.get("reason"):
        children.append(notion_api.bullet(f"Fallback reason: {direct['reason']}"))
    if record.get("packet_path"):
        children.append(notion_api.bullet(f"Local package pointer: {Path(record['packet_path']).name}"))
    if record.get("inspection_receipt_path"):
        children.append(notion_api.bullet(
            f"Inspection receipt: {Path(record['inspection_receipt_path']).name}"
        ))
    limitations = list(record.get("limitations") or [])
    limitation_label = "Capture-time limitation" if record.get("inspection") else "Limitation"
    for reason in limitations[:20]:
        children.append(notion_api.bullet(
            limitation_label + ": "
            + _truncate_json_string(reason, MAX_NOTION_TIMELINE_FIELD_JSON_BYTES)
        ))
    if len(limitations) > 20:
        children.append(notion_api.bullet(
            f"Showing 20 of {len(limitations)} limitations; the complete list remains in the watch packet."
        ))

    refresh_children = [
        notion_api.heading2(f"Watch Refresh — {now_iso()}"),
        notion_api.para(f"WATCH_SYNC:{record['sync_fingerprint']}"),
        notion_api.bullet(f"Evidence state: {record['evidence_state']}"),
        notion_api.bullet(f"Topics: {', '.join(record['topics']) or '(none)'}"),
        notion_api.bullet(f"Capture packet: {record['packet_id']}"),
    ]
    if record.get("inspection") and record["inspection"].get("coverage_limit"):
        refresh_children.append(notion_api.bullet(
            f"Review coverage: {record['inspection']['coverage_limit']}"
        ))
    for row in timeline_rows:
        if row.get("review_observation"):
            refresh_children.append(notion_api.para(
                f"[{_timestamp_label(row.get('timestamp_seconds') or 0)}] Reviewed observation: "
                f"{_truncate_json_string(row['review_observation'], MAX_NOTION_TIMELINE_FIELD_JSON_BYTES)}"
            ))
    if len(children) > 90:
        raise RuntimeError(f"watch packet produced {len(children)} Notion blocks; bounded payload limit is 90")
    create_request_bytes = _json_wire_bytes({
        "parent": {"database_id": db_id},
        "properties": properties,
        "children": children,
    })
    refresh_request_bytes = _json_wire_bytes({"children": refresh_children})
    if max(create_request_bytes, refresh_request_bytes) > MAX_NOTION_REQUEST_BYTES:
        raise RuntimeError(
            "watch packet exceeds the size-safe Notion request envelope; the full evidence remains in the local packet"
        )
    return {
        "properties": properties,
        "children": children,
        "refresh_children": refresh_children,
        "request_bytes": {
            "create": create_request_bytes,
            "refresh": refresh_request_bytes,
        },
    }


def _plain_rich_text(prop: dict) -> str:
    if not isinstance(prop, dict):
        return ""
    rows = prop.get("rich_text") or prop.get("title") or []
    text = []
    for row in rows:
        text.append(str(row.get("plain_text") or (row.get("text") or {}).get("content") or ""))
    return "".join(text)


def append_block_batches(notion_api, page_id: str, blocks: list[dict]) -> None:
    for i in range(0, len(blocks), 90):
        notion_api._request(
            "PATCH",
            f"/blocks/{page_id}/children",
            {"children": blocks[i:i + 90]},
        )


def _block_plain_text(block: dict) -> str:
    block_type = str(block.get("type") or "")
    content = block.get(block_type) if block_type else None
    rows = content.get("rich_text") if isinstance(content, dict) else []
    return _plain_rich_text({"rich_text": rows or []})


def has_watch_sync_marker(notion_api, page_id: str, sync_fingerprint: str) -> bool:
    marker = f"WATCH_SYNC:{sync_fingerprint}"
    cursor = None
    for _ in range(100):
        page = notion_api.list_block_children(page_id, start_cursor=cursor, page_size=100)
        if any(marker in _block_plain_text(block) for block in page.get("results") or []):
            return True
        if not page.get("has_more"):
            return False
        cursor = page.get("next_cursor")
        if not cursor:
            return False
    raise RuntimeError("Notion block marker scan exceeded 10,000 blocks")


def query_social_intel_matches(notion_api, db_id: str, canonical_url: str) -> list[dict]:
    try:
        query = notion_api.query_database(
            db_id,
            filter={"property": "Post URL", "url": {"equals": canonical_url}},
            page_size=3,
        )
    except Exception as exc:
        raise RuntimeError(f"Social Intelligence dedup query failed; no page was written: {exc}") from exc
    matches = query.get("results") or []
    if len(matches) > 1:
        raise RuntimeError(f"duplicate audit failed: {len(matches)} pages already use {canonical_url}; no write performed")
    return matches


_UNQUERIED = object()


def upsert_social_intel_page(
    notion_api,
    db_id: str,
    payload: dict,
    canonical_url: str,
    sync_fingerprint: str,
    *,
    matches=_UNQUERIED,
) -> dict:
    """Fail-closed exact-URL upsert; never create after a failed dedup query."""
    if matches is _UNQUERIED:
        matches = query_social_intel_matches(notion_api, db_id, canonical_url)
    if not matches:
        page_url = create_notion_page(notion_api, db_id, payload)
        return {"action": "created", "notion_url": page_url}

    page = matches[0]
    existing_fingerprint = _plain_rich_text(
        (page.get("properties") or {}).get("Watch Fingerprint") or {}
    )
    if existing_fingerprint == sync_fingerprint:
        return {"action": "unchanged", "notion_url": page.get("url")}

    # Keep human-edited title/creator/hook intact on refresh; update only the
    # evidence-owned fields and append a versioned body section.
    refresh_keys = {
        "Platform", "Type", "Post URL", "Duration (s)", "Posted", "Scraped",
        "Watch Fingerprint", "Evidence State", "Topics",
    }
    refresh_properties = {
        key: value for key, value in payload["properties"].items() if key in refresh_keys
    }
    # A visible machine marker makes the multi-call refresh retry-safe: if
    # append succeeded but property update failed, the next run sees the body
    # marker and only completes the property update.
    if not has_watch_sync_marker(notion_api, page["id"], sync_fingerprint):
        append_block_batches(notion_api, page["id"], payload["refresh_children"])
    notion_api.update_page(page["id"], refresh_properties)
    return {"action": "updated", "notion_url": page.get("url")}


def sync_social_intel_record(notion_api, db_id: str, record: dict) -> dict:
    """Query before any schema/data mutation, then build and upsert."""
    matches = query_social_intel_matches(notion_api, db_id, record["url"])
    payload = build_social_intel_payload(record, notion_api, db_id)
    return upsert_social_intel_page(
        notion_api,
        db_id,
        payload,
        record["url"],
        record["sync_fingerprint"],
        matches=matches,
    )


def create_notion_page(notion_api, db_id: str, payload: dict) -> str:
    """Create page with first <=90 blocks, then append the rest in batches
    of <=90 (Notion caps children at 100 blocks per API call)."""
    children = payload["children"]
    first_batch, rest = children[:90], children[90:]

    result = notion_api.create_page(db_id, payload["properties"], children=first_batch)
    page_id = result["id"]
    url = result["url"]

    for i in range(0, len(rest), 90):
        batch = rest[i:i + 90]
        notion_api._request("PATCH", f"/blocks/{page_id}/children", {"children": batch})

    return url


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog="social_to_notion.py",
        description="One command: social URL -> rich Notion page (metadata + embed + transcript + stats + ledger).",
    )
    parser.add_argument("url", nargs="?", help="Social URL (YouTube, TikTok, Instagram, Reddit)")
    parser.add_argument("--db", default="content", choices=["content", "knowledge", "captures"],
                        help="Target Notion database (default: content)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Acquire but never call Notion — print the payload as JSON")
    parser.add_argument("--watch-packet", default=None,
                        help="Use a watch-video-intelligence/v1 packet without reacquiring the source")
    parser.add_argument("--inspection-receipt", default=None,
                        help="Optional validated watch-visual-inspection/v1 receipt")
    parser.add_argument("--topics", default="",
                        help="Comma-separated Social Intelligence topics for --watch-packet")
    parser.add_argument("--transcript-file", default=None,
                        help="Inject a transcript from disk (enables fully offline testing)")
    parser.add_argument("--tags", default="", help="Comma-separated tags")
    parser.add_argument("--no-transcript", action="store_true",
                        help="Skip transcript acquisition entirely")
    parser.add_argument("--limit", type=int, default=1,
                        help="Result limit passed through to acquisition calls (default 1)")
    args = parser.parse_args()

    load_env()

    if args.watch_packet and args.url:
        parser.error("provide either a positional social URL or --watch-packet, not both")
    if not args.watch_packet and not args.url:
        parser.error("a positional social URL or --watch-packet is required")
    if args.inspection_receipt and not args.watch_packet:
        parser.error("--inspection-receipt requires --watch-packet")

    if args.watch_packet:
        # Packet mode intentionally branches before Apify or any URL
        # acquisition.  Dry-run imports static builders only and makes zero
        # API/network calls.
        try:
            from execution.notion_api import NotionAPI, DB_IDS
        except ImportError:
            sys.path.insert(0, str(BASE))
            from execution.notion_api import NotionAPI, DB_IDS
        try:
            packet = load_watch_packet(args.watch_packet)
            receipt = (
                load_inspection_receipt(args.inspection_receipt, packet)
                if args.inspection_receipt else None
            )
            record = watch_packet_to_record(packet, topics=args.topics, inspection_receipt=receipt)
        except ValueError as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            sys.exit(1)

        if args.dry_run:
            class _DrySocialNotion:
                title = staticmethod(NotionAPI.title)
                rich_text = staticmethod(NotionAPI.rich_text)
                select = staticmethod(NotionAPI.select)
                multi_select = staticmethod(NotionAPI.multi_select)
                number = staticmethod(NotionAPI.number)
                date = staticmethod(NotionAPI.date)
                checkbox = staticmethod(NotionAPI.checkbox)
                heading2 = staticmethod(NotionAPI.heading2)
                para = staticmethod(NotionAPI.para)
                bullet = staticmethod(NotionAPI.bullet)

                def _ensure_properties(self, database_id, required):
                    return set(required.keys())

            payload = build_social_intel_payload(record, _DrySocialNotion(), "dry-run-social-intel")
            print(json.dumps({
                "status": "dry_run",
                "database": "social_intel",
                "record": record,
                "notion_payload": {
                    "properties": payload["properties"],
                    "first_blocks": payload["children"][:90],
                    "block_count": len(payload["children"]),
                    "additional_batches": max(0, (len(payload["children"]) - 1) // 90),
                },
            }, indent=2, default=str))
            sys.exit(0)

        db_id = DB_IDS.get("social_intel", "")
        if not db_id:
            print("ERROR: NOTION_DB_SOCIAL_INTEL is not configured in .env.", file=sys.stderr)
            sys.exit(1)
        try:
            notion_api = NotionAPI()
            result = sync_social_intel_record(notion_api, db_id, record)
        except Exception as exc:
            print(f"ERROR: Social Intelligence sync failed: {exc}", file=sys.stderr)
            sys.exit(1)
        print(json.dumps({
            "status": "ok",
            "packet_id": record["packet_id"],
            "evidence_state": record["evidence_state"],
            "topics": record["topics"],
            **result,
        }, indent=2))
        sys.exit(0)

    platform = route_platform(args.url)

    if platform == "linkedin":
        print(f"ERROR: {LINKEDIN_MESSAGE}", file=sys.stderr)
        sys.exit(2)

    if platform is None:
        host = urlparse(args.url).hostname or "(unparseable)"
        print(f"ERROR: unsupported host '{host}' — no acquisition route for this URL.", file=sys.stderr)
        sys.exit(2)

    apify_mod = _load_apify_client_module()
    budget = ApifyBudget(apify_mod)

    acquirer = ACQUIRERS[platform]
    try:
        record = acquirer(args.url, args, budget)
    except Exception as e:
        print(f"ERROR: acquisition failed for {platform}: {e}", file=sys.stderr)
        sys.exit(1)

    # notion_api is only needed once we're actually about to build/send a
    # payload — import lazily so --dry-run --transcript-file works with zero
    # network and no NOTION_API_KEY required for the acquisition side.
    try:
        from execution.notion_api import NotionAPI, DB_IDS
    except ImportError:
        sys.path.insert(0, str(BASE))
        from execution.notion_api import NotionAPI, DB_IDS

    if args.dry_run:
        # Build payload without ever touching Notion. Use a lightweight
        # stand-in for _ensure_properties so dry-run needs no API key/network.
        class _DryNotion:
            title = staticmethod(NotionAPI.title)
            rich_text = staticmethod(NotionAPI.rich_text)
            select = staticmethod(NotionAPI.select)
            multi_select = staticmethod(NotionAPI.multi_select)
            number = staticmethod(NotionAPI.number)
            date = staticmethod(NotionAPI.date)
            heading2 = staticmethod(NotionAPI.heading2)
            para = staticmethod(NotionAPI.para)
            bullet = staticmethod(NotionAPI.bullet)

            def _ensure_properties(self, database_id, required):
                # dry-run assumes every requested property is available so
                # the printed payload shows the full intended shape.
                return set(required.keys())

        dry_notion = _DryNotion()
        payload = build_notion_payload(record, dry_notion, DB_IDS.get(args.db, ""), args)

        output = {
            "record": record,
            "notion_payload": {
                "database": args.db,
                "properties": payload["properties"],
                "first_blocks": payload["children"][:90],
                "block_count": len(payload["children"]),
                "additional_batches": max(0, (len(payload["children"]) - 90 + 89) // 90) if len(payload["children"]) > 90 else 0,
            },
        }
        print(json.dumps(output, indent=2, default=str))
        sys.exit(0)

    db_id = DB_IDS.get(args.db, "")
    if not db_id:
        env_var = {
            "content": "NOTION_DB_CONTENT",
            "knowledge": "NOTION_DB_KNOWLEDGE",
            "captures": "NOTION_DB_CAPTURES",
        }.get(args.db, f"NOTION_DB_{args.db.upper()}")
        print(f"ERROR: no database id configured for --db {args.db}. Set {env_var} in .env.", file=sys.stderr)
        sys.exit(1)

    try:
        notion_api = NotionAPI()
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    payload = build_notion_payload(record, notion_api, db_id, args)

    try:
        page_url = create_notion_page(notion_api, db_id, payload)
    except Exception as e:
        print(f"ERROR: Notion page creation failed: {e}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps({
        "status": "ok",
        "platform": platform,
        "title": record["title"],
        "notion_url": page_url,
        "transcript_chars": len(record["transcript"]) if record["transcript"] else 0,
        "degraded": record["degraded"],
    }, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()
