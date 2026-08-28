#!/usr/bin/env python3
"""Outlier Radar — $0 keyless YouTube data spine for the Kallaway trend/hook stack.

Two-stage yt-dlp fetch (flat channel dump, then enrich only flagged outliers),
views-per-day outlier scoring against per-channel median baselines, and a
versioned signal-pack contract under .agent/outlier-radar/ that downstream
skills (and a future sandcastles_bridge.py / manual_csv lane) consume.

Scoring and clustering math is reused from execution/kallaway_trend_hook_radar.py.
No Apify anywhere on any path in this module. No cookies ever.
"""

from __future__ import annotations

import argparse
import html
import json
import random
import re
import shutil
import sqlite3
import statistics
import subprocess
import sys
import tempfile
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import yt_dlp
from yt_dlp.utils import DownloadError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

from kallaway_trend_hook_radar import (  # noqa: E402
    OutlierScore,
    cluster_patterns,
    desire_template,
    hook_format,
    infer_topic,
    winner_thresholds,
)

try:
    from degrade import degraded  # noqa: E402
except Exception:  # pragma: no cover - ledger is a nicety, never a dependency
    def degraded(value, why, exc=None):
        return value


PACK_VERSION = 1
FRESHNESS_TTL_HOURS = 12.0
MAX_CHANNELS_PER_RUN = 12
MAX_VIDEOS_PER_CHANNEL = 30
ENRICH_CAP = 10
CHANNEL_SLEEP_RANGE = (3.0, 8.0)
ENRICH_SLEEP_RANGE = (1.5, 3.5)
RANKED_CAP = 50

RADAR_DIR = ROOT / ".agent" / "outlier-radar"
DB_PATH = RADAR_DIR / "radar.db"
CHANNELS_JSON = RADAR_DIR / "channels.json"
RECEIPTS_DIR = RADAR_DIR / "receipts"
PACKS_DIR = RADAR_DIR / "packs"
TRANSCRIPTS_DIR = RADAR_DIR / "transcripts"

PACK_FIELDS = [
    "pack_version",
    "niche_slug",
    "niche_label",
    "generated_at",
    "freshness_ttl_hours",
    "run_id",
    "run_receipt_path",
    "status",
    "coverage",
    "source_lanes",
    "channels",
    "ranked_videos",
    "leaderboard",
    "watchlist_adds",
    "cost",
    "errors",
]

RECORD_FIELDS = [
    "video_id",
    "platform",
    "channel_id",
    "channel_handle",
    "channel_title",
    "url",
    "title",
    "published_at",
    "age_days",
    "duration_s",
    "views",
    "views_per_day",
    "channel_median_vpd",
    "channel_video_count_sampled",
    "outlier_score",
    "outlier_multiplier",
    "winner_line_status",
    "confidence",
    "likes",
    "comments",
    "velocity_vpd_7d",
    "hook_text",
    "format_hint",
    "topic",
    "transcript_path",
    "first_seen_at",
    "last_refreshed_at",
    "source_lane",
]

COVERAGE_PLATFORMS = ("youtube", "tiktok", "instagram")
COVERAGE_VALUES = ("measured", "partial", "none")
SOURCE_LANES = ("ytdlp_public", "manual_csv", "owned_metrics", "sandcastles_mcp")


@dataclass
class RunReceipt:
    run_id: str
    generated_at: str
    niche_slug: str
    channels_attempted: int
    channels_fetched: int
    channels_skipped_ttl: int
    channels_failed: int
    videos_seen: int
    videos_new: int
    snapshots_added: int
    outliers_flagged: int
    transcripts_written: int
    yt_dlp_requests: int
    cost_usd: float
    status: str
    pack_path: str
    notes: list[str] = field(default_factory=list)
    errors: list[dict[str, str]] = field(default_factory=list)


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso(dt: datetime) -> str:
    return dt.isoformat(timespec="seconds")


def clean_handle(raw: str) -> str:
    return raw.strip().lstrip("@")


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def receipt_line(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False))


# ---------------------------------------------------------------------------
# Storage
# ---------------------------------------------------------------------------

SCHEMA = """
CREATE TABLE IF NOT EXISTS channels (
    channel_id TEXT PRIMARY KEY,
    handle TEXT NOT NULL,
    title TEXT,
    subscriber_count INTEGER,
    median_vpd REAL,
    last_refreshed_at TEXT,
    fetch_status TEXT
);
CREATE TABLE IF NOT EXISTS videos (
    video_id TEXT PRIMARY KEY,
    channel_id TEXT NOT NULL,
    platform TEXT NOT NULL,
    url TEXT,
    title TEXT,
    published_at TEXT,
    duration_s REAL,
    first_seen_at TEXT,
    last_refreshed_at TEXT,
    source_lane TEXT
);
CREATE TABLE IF NOT EXISTS snapshots (
    video_id TEXT NOT NULL,
    run_id TEXT NOT NULL,
    views INTEGER,
    captured_at TEXT,
    PRIMARY KEY (video_id, run_id)
);
CREATE TABLE IF NOT EXISTS runs (
    run_id TEXT PRIMARY KEY,
    niche_slug TEXT,
    started_at TEXT,
    finished_at TEXT,
    status TEXT,
    cost_usd REAL,
    requests INTEGER
);
CREATE INDEX IF NOT EXISTS idx_videos_channel ON videos (channel_id);
CREATE INDEX IF NOT EXISTS idx_snapshots_video ON snapshots (video_id, captured_at);
"""


def open_db() -> sqlite3.Connection:
    RADAR_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


def load_niches() -> dict[str, dict[str, Any]]:
    if not CHANNELS_JSON.exists():
        return {}
    try:
        data = json.loads(CHANNELS_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def save_niches(niches: dict[str, dict[str, Any]]) -> None:
    RADAR_DIR.mkdir(parents=True, exist_ok=True)
    CHANNELS_JSON.write_text(json.dumps(niches, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Fetch — yt-dlp, two-stage, keyless, cookie-free
# ---------------------------------------------------------------------------

def _ydl_opts(flat: bool) -> dict[str, Any]:
    opts: dict[str, Any] = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "sleep_interval_requests": 1,
    }
    if flat:
        opts.update(
            {
                "extract_flat": "in_playlist",
                "playlistend": MAX_VIDEOS_PER_CHANNEL,
                # CLI twin: --extractor-args "youtubetab:approximate_date"
                "extractor_args": {"youtubetab": {"approximate_date": [""]}},
            }
        )
    return opts


def _extract_with_retry(url: str, flat: bool) -> dict[str, Any]:
    for attempt in (1, 2):
        try:
            with yt_dlp.YoutubeDL(_ydl_opts(flat)) as ydl:
                return ydl.extract_info(url, download=False)
        except DownloadError as exc:
            message = str(exc)
            if attempt == 1 and ("429" in message or "403" in message):
                time.sleep(15 + random.uniform(0, 15))
                continue
            raise
    raise RuntimeError("unreachable")


def fetch_channel_flat(handle: str) -> dict[str, Any]:
    return _extract_with_retry(f"https://www.youtube.com/@{clean_handle(handle)}/videos", flat=True)


def fetch_video_full(url: str) -> dict[str, Any]:
    return _extract_with_retry(url, flat=False)


# Vendored from execution/social_intel.py (_vtt_to_text + fetch_yt_transcript_ytdlp).
# Importing social_intel would pull apify_client into the import graph
# (social_intel.py line 53, module-level) — forbidden on any path here.
# Two adaptations: invoke `sys.executable -m yt_dlp` instead of a PATH binary
# so the venv copy is always the one used, and pass --ignore-no-formats-error —
# current YouTube serves no plain formats without a PO token, which otherwise
# aborts the run before the subtitle write (verified 2026-08-27).

def _vtt_to_text(vtt_content: str) -> str:
    lines = vtt_content.splitlines()
    cues: list[list[str]] = []
    current: list[str] = []
    for raw in lines:
        line = raw.strip()
        if not line:
            if current:
                cues.append(current)
                current = []
            continue
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:") or "-->" in line:
            continue
        clean = re.sub(r"<[^>]+>", "", line).strip()
        if clean:
            current.append(clean)
    if current:
        cues.append(current)

    kept: list[str] = []
    prev = None
    for cue in cues:
        last = cue[-1] if cue else ""
        if last and last != prev:
            kept.append(last)
            prev = last
    return html.unescape(" ".join(kept)).strip()


def fetch_captions(video_url: str, video_id: str) -> str | None:
    tmp_dir = Path(tempfile.mkdtemp(prefix="outlier_radar_yt_"))
    try:
        cmd = [
            sys.executable, "-m", "yt_dlp", "--skip-download", "--ignore-no-formats-error",
            "--write-auto-sub", "--write-sub",
            "--sub-lang", "en", "--sub-format", "vtt", "--quiet", "--no-warnings",
            "--sleep-requests", "1",
            "-o", str(tmp_dir / "%(id)s.%(ext)s"), video_url,
        ]
        subprocess.run(cmd, capture_output=True, timeout=120, text=True)
        vtt_files = list(tmp_dir.glob(f"{video_id}*.vtt")) or list(tmp_dir.glob("*.vtt"))
        if not vtt_files:
            return None
        text = _vtt_to_text(vtt_files[0].read_text(encoding="utf-8", errors="ignore"))
        return text or None
    except Exception:
        return None
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def _hook_from_text(text: str, max_len: int = 200) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_len:
        return text
    cut = text[:max_len]
    return cut[: cut.rfind(" ")] if " " in cut else cut


# ---------------------------------------------------------------------------
# Scoring — vpd vs channel median, winner line via radar's largest-drop logic
# ---------------------------------------------------------------------------

def published_at_from_entry(entry: dict[str, Any]) -> str | None:
    ts = entry.get("timestamp")
    if ts:
        try:
            return iso(datetime.fromtimestamp(float(ts), tz=timezone.utc))
        except (ValueError, OSError, OverflowError):
            pass
    upload_date = entry.get("upload_date")
    if upload_date:
        try:
            return iso(datetime.strptime(str(upload_date), "%Y%m%d").replace(tzinfo=timezone.utc))
        except ValueError:
            pass
    return None


def age_days_for(published_at: str | None, at: datetime) -> float | None:
    if not published_at:
        return None
    try:
        published = datetime.fromisoformat(published_at)
    except ValueError:
        return None
    if published.tzinfo is None:
        published = published.replace(tzinfo=timezone.utc)
    return (at - published).total_seconds() / 86400.0


def views_per_day(views: float | None, age_days: float | None) -> float | None:
    if views is None or views < 0 or age_days is None:
        return None
    effective = min(max(age_days, 2.0), 90.0)
    return views / effective


def percentile_rank(value: float, population: list[float]) -> float:
    if not population:
        return 0.0
    return sum(1 for item in population if item <= value) / len(population)


def confidence_for(multiplier: float | None, baseline_source: str, published_at: str | None) -> str:
    if multiplier is not None and baseline_source == "channel" and published_at:
        return "high"
    if multiplier is not None:
        return "medium"
    return "low"


def latest_views_by_video(conn: sqlite3.Connection, video_ids: list[str]) -> dict[str, int]:
    if not video_ids:
        return {}
    marks = ",".join("?" for _ in video_ids)
    rows = conn.execute(
        f"""
        SELECT s.video_id, s.views FROM snapshots s
        JOIN (SELECT video_id, MAX(captured_at) AS m FROM snapshots
              WHERE video_id IN ({marks}) GROUP BY video_id) t
        ON s.video_id = t.video_id AND s.captured_at = t.m
        """,
        video_ids,
    ).fetchall()
    return {row["video_id"]: row["views"] for row in rows}


def velocity_vpd_7d(conn: sqlite3.Connection, video_id: str, at: datetime) -> float | None:
    cutoff = iso(datetime.fromtimestamp(at.timestamp() - 7 * 86400, tz=timezone.utc))
    rows = conn.execute(
        "SELECT views, captured_at FROM snapshots WHERE video_id = ? AND captured_at >= ? ORDER BY captured_at",
        (video_id, cutoff),
    ).fetchall()
    if len(rows) < 2:
        return None
    first, last = rows[0], rows[-1]
    try:
        t0 = datetime.fromisoformat(first["captured_at"])
        t1 = datetime.fromisoformat(last["captured_at"])
    except ValueError:
        return None
    delta_days = max((t1 - t0).total_seconds() / 86400.0, 1.0)
    return round(((last["views"] or 0) - (first["views"] or 0)) / delta_days, 2)


def score_niche(conn: sqlite3.Connection, channel_rows: list[sqlite3.Row], at: datetime) -> list[dict[str, Any]]:
    channel_ids = [row["channel_id"] for row in channel_rows]
    if not channel_ids:
        return []
    marks = ",".join("?" for _ in channel_ids)
    video_rows = conn.execute(
        f"SELECT * FROM videos WHERE channel_id IN ({marks})", channel_ids
    ).fetchall()
    views_map = latest_views_by_video(conn, [row["video_id"] for row in video_rows])
    channels_by_id = {row["channel_id"]: row for row in channel_rows}

    records: list[dict[str, Any]] = []
    vpds_by_channel: dict[str, list[float]] = {}
    for row in video_rows:
        views = views_map.get(row["video_id"])
        age = age_days_for(row["published_at"], at)
        vpd = views_per_day(views, age)
        channel = channels_by_id[row["channel_id"]]
        title = row["title"] or ""
        records.append(
            {
                "video_id": row["video_id"],
                "platform": row["platform"],
                "channel_id": row["channel_id"],
                "channel_handle": "@" + channel["handle"],
                "channel_title": channel["title"],
                "url": row["url"],
                "title": title,
                "published_at": row["published_at"],
                "age_days": round(age, 2) if age is not None else None,
                "duration_s": row["duration_s"],
                "views": views,
                "views_per_day": round(vpd, 2) if vpd is not None else None,
                "channel_median_vpd": None,
                "channel_video_count_sampled": 0,
                "outlier_score": 0.0,
                "outlier_multiplier": None,
                "winner_line_status": "below_winner_line",
                "confidence": "low",
                "likes": None,
                "comments": None,
                "velocity_vpd_7d": velocity_vpd_7d(conn, row["video_id"], at),
                "hook_text": title,
                "format_hint": hook_format(title),
                "topic": infer_topic(title),
                "transcript_path": None,
                "first_seen_at": row["first_seen_at"],
                "last_refreshed_at": row["last_refreshed_at"],
                "source_lane": row["source_lane"],
            }
        )
        if vpd is not None:
            vpds_by_channel.setdefault(row["channel_id"], []).append(vpd)

    all_vpds = [vpd for vpds in vpds_by_channel.values() for vpd in vpds]
    global_median = statistics.median(all_vpds) if all_vpds else None
    median_by_channel: dict[str, tuple[float | None, str, int]] = {}
    for channel_id in channel_ids:
        vpds = vpds_by_channel.get(channel_id, [])
        if len(vpds) >= 5:
            median_by_channel[channel_id] = (statistics.median(vpds), "channel", len(vpds))
        else:
            median_by_channel[channel_id] = (global_median, "niche_global", len(vpds))

    vpd_population = all_vpds
    prelim: list[tuple[SimpleNamespace, float]] = []
    for record in records:
        baseline, baseline_source, sampled = median_by_channel[record["channel_id"]]
        record["channel_median_vpd"] = round(baseline, 2) if baseline is not None else None
        record["channel_video_count_sampled"] = sampled
        vpd = record["views_per_day"]
        multiplier = None
        if vpd is not None and baseline:
            multiplier = vpd / baseline
            score = multiplier
        elif vpd is not None:
            score = 0.5 + percentile_rank(vpd, vpd_population) * 1.5
        else:
            score = 0.0
        record["outlier_multiplier"] = round(multiplier, 4) if multiplier is not None else None
        record["outlier_score"] = round(score, 4)
        record["confidence"] = confidence_for(multiplier, baseline_source, record["published_at"])
        # winner_thresholds groups on signal.platform + signal.creator only
        prelim.append((SimpleNamespace(platform="youtube", creator=record["channel_handle"]), score))

    thresholds = winner_thresholds(prelim)
    for record in records:
        key = f"youtube:{record['channel_handle']}".lower()
        threshold = thresholds.get(key, 1.5)
        if record["outlier_score"] >= threshold:
            record["winner_line_status"] = "above_winner_line"
        elif record["outlier_score"] >= 1.0:
            record["winner_line_status"] = "study_but_not_winner"
        else:
            record["winner_line_status"] = "below_winner_line"

    for channel_id, (baseline, source, _sampled) in median_by_channel.items():
        if source == "channel" and baseline is not None:
            conn.execute(
                "UPDATE channels SET median_vpd = ? WHERE channel_id = ?", (round(baseline, 2), channel_id)
            )

    records.sort(key=lambda item: item["outlier_score"], reverse=True)
    return records


# ---------------------------------------------------------------------------
# Pack build + validation
# ---------------------------------------------------------------------------

def build_leaderboard(records: list[dict[str, Any]]) -> dict[str, Any]:
    topics: dict[str, dict[str, Any]] = {}
    for record in records:
        entry = topics.setdefault(
            record["topic"], {"topic": record["topic"], "score_sum": 0.0, "video_count": 0, "example_video_ids": []}
        )
        entry["score_sum"] = round(entry["score_sum"] + record["outlier_score"], 4)
        entry["video_count"] += 1
        if len(entry["example_video_ids"]) < 3:
            entry["example_video_ids"].append(record["video_id"])
    topic_rows = sorted(topics.values(), key=lambda item: item["score_sum"], reverse=True)[:15]

    scored = [
        OutlierScore(
            signal_id=record["video_id"],
            platform=record["platform"],
            creator=record["channel_handle"],
            hook_text=record["hook_text"],
            topic=record["topic"],
            url=record["url"] or "",
            views=record["views"],
            baseline_views=record["channel_median_vpd"],
            outlier_multiplier=record["outlier_multiplier"],
            engagement_rate=None,
            lead_rate=None,
            outlier_score=record["outlier_score"],
            confidence=record["confidence"],
            winner_line_status=record["winner_line_status"],
            reason_codes=[],
        )
        for record in records
    ]
    formats = [
        {
            "hook_format": pattern.hook_format,
            "desire_template": pattern.desire_template,
            "avg_score": pattern.avg_outlier_score,
            "count": pattern.signal_count,
            "sample_hooks": pattern.sample_hooks,
        }
        for pattern in cluster_patterns(scored)
    ]
    return {"topics": topic_rows, "formats": formats}


def validate_pack(pack: dict[str, Any]) -> list[str]:
    problems: list[str] = []
    for name in PACK_FIELDS:
        if name not in pack:
            problems.append(f"missing pack field: {name}")
    if pack.get("status") not in ("ok", "degraded"):
        problems.append(f"bad status: {pack.get('status')!r}")
    coverage = pack.get("coverage")
    if not isinstance(coverage, dict):
        problems.append("coverage is not a dict")
    else:
        for platform in COVERAGE_PLATFORMS:
            if coverage.get(platform) not in COVERAGE_VALUES:
                problems.append(f"coverage.{platform} invalid: {coverage.get(platform)!r}")
    lanes = pack.get("source_lanes")
    if not isinstance(lanes, list) or not lanes or any(lane not in SOURCE_LANES for lane in lanes):
        problems.append(f"source_lanes invalid: {lanes!r}")
    leaderboard = pack.get("leaderboard")
    if not isinstance(leaderboard, dict) or "topics" not in leaderboard or "formats" not in leaderboard:
        problems.append("leaderboard missing topics/formats")
    ranked = pack.get("ranked_videos")
    if not isinstance(ranked, list):
        problems.append("ranked_videos is not a list")
    else:
        if len(ranked) > RANKED_CAP:
            problems.append(f"ranked_videos over cap: {len(ranked)} > {RANKED_CAP}")
        for index, record in enumerate(ranked):
            missing = [name for name in RECORD_FIELDS if name not in record]
            if missing:
                problems.append(f"ranked_videos[{index}] missing: {', '.join(missing)}")
                break
    if not isinstance(pack.get("watchlist_adds"), list):
        problems.append("watchlist_adds is not a list")
    cost = pack.get("cost")
    if not isinstance(cost, dict) or "usd" not in cost or "yt_dlp_requests" not in cost:
        problems.append("cost missing usd/yt_dlp_requests")
    if not isinstance(pack.get("errors"), list):
        problems.append("errors is not a list")
    return problems


def write_pack(pack: dict[str, Any], niche_slug: str) -> Path:
    problems = validate_pack(pack)
    if problems:
        raise ValueError("pack failed validation: " + "; ".join(problems))
    pack_dir = PACKS_DIR / niche_slug
    pack_dir.mkdir(parents=True, exist_ok=True)
    body = json.dumps(pack, indent=2, ensure_ascii=False) + "\n"
    latest = pack_dir / "latest.json"
    latest.write_text(body, encoding="utf-8")
    (pack_dir / f"{now_utc():%Y-%m-%d}.json").write_text(body, encoding="utf-8")
    return latest


# ---------------------------------------------------------------------------
# refresh — fetch + score + enrich + pack
# ---------------------------------------------------------------------------

def upsert_channel(conn: sqlite3.Connection, channel_id: str, handle: str, title: str | None,
                   subscribers: int | None, status: str, at: str) -> None:
    conn.execute(
        """
        INSERT INTO channels (channel_id, handle, title, subscriber_count, last_refreshed_at, fetch_status)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(channel_id) DO UPDATE SET
            handle = excluded.handle, title = excluded.title,
            subscriber_count = COALESCE(excluded.subscriber_count, channels.subscriber_count),
            last_refreshed_at = excluded.last_refreshed_at, fetch_status = excluded.fetch_status
        """,
        (channel_id, handle, title, subscribers, at, status),
    )


def store_flat_dump(conn: sqlite3.Connection, info: dict[str, Any], handle: str, run_id: str, at: str) -> tuple[int, int, int]:
    channel_id = info.get("channel_id") or info.get("uploader_id") or f"handle:{handle}"
    upsert_channel(conn, channel_id, handle, info.get("channel"), info.get("channel_follower_count"), "ok", at)
    seen = new = snaps = 0
    for entry in info.get("entries") or []:
        if not isinstance(entry, dict) or not entry.get("id"):
            continue
        video_id = entry["id"]
        seen += 1
        exists = conn.execute("SELECT 1 FROM videos WHERE video_id = ?", (video_id,)).fetchone()
        published_at = published_at_from_entry(entry)
        if exists:
            conn.execute(
                """
                UPDATE videos SET title = ?, published_at = COALESCE(?, published_at),
                    duration_s = COALESCE(?, duration_s), last_refreshed_at = ?
                WHERE video_id = ?
                """,
                (entry.get("title"), published_at, entry.get("duration"), at, video_id),
            )
        else:
            new += 1
            conn.execute(
                """
                INSERT INTO videos (video_id, channel_id, platform, url, title, published_at,
                                    duration_s, first_seen_at, last_refreshed_at, source_lane)
                VALUES (?, ?, 'youtube', ?, ?, ?, ?, ?, ?, 'ytdlp_public')
                """,
                (video_id, channel_id, f"https://www.youtube.com/watch?v={video_id}",
                 entry.get("title"), published_at, entry.get("duration"), at, at),
            )
        views = entry.get("view_count")
        if views is not None:
            conn.execute(
                "INSERT OR REPLACE INTO snapshots (video_id, run_id, views, captured_at) VALUES (?, ?, ?, ?)",
                (video_id, run_id, int(views), at),
            )
            snaps += 1
    return seen, new, snaps


def enrich_outliers(conn: sqlite3.Connection, records: list[dict[str, Any]], cap: int,
                    errors: list[dict[str, str]]) -> tuple[list[str], int, int]:
    flagged = [record for record in records if record["winner_line_status"] == "above_winner_line"][:cap]
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    transcripts_written = 0
    requests = 0
    for index, record in enumerate(flagged):
        if index > 0:
            time.sleep(random.uniform(*ENRICH_SLEEP_RANGE))
        try:
            requests += 1
            info = fetch_video_full(record["url"])
            record["likes"] = info.get("like_count")
            record["comments"] = info.get("comment_count")
            exact = published_at_from_entry(info)
            if exact:
                record["published_at"] = exact
                conn.execute("UPDATE videos SET published_at = ? WHERE video_id = ?", (exact, record["video_id"]))
        except Exception as exc:
            errors.append({"channel": record["channel_handle"], "stage": "enrich_metadata", "message": str(exc)[:200]})
        transcript_file = TRANSCRIPTS_DIR / f"{record['video_id']}.txt"
        if not transcript_file.exists():  # captions are durable — never refetched
            requests += 1
            text = fetch_captions(record["url"], record["video_id"])
            if text:
                transcript_file.write_text(text, encoding="utf-8")
                transcripts_written += 1
            else:
                errors.append({"channel": record["channel_handle"], "stage": "enrich_captions",
                               "message": f"no captions for {record['video_id']}"})
        if transcript_file.exists():
            record["transcript_path"] = relative(transcript_file)
            record["hook_text"] = _hook_from_text(transcript_file.read_text(encoding="utf-8")) or record["title"]
            record["format_hint"] = hook_format(record["hook_text"])
    return [record["video_id"] for record in flagged], transcripts_written, requests


def cmd_refresh(args: argparse.Namespace) -> int:
    niches = load_niches()
    niche = niches.get(args.niche)
    if not niche:
        receipt_line({"cmd": "refresh", "status": "error", "message": f"unknown niche '{args.niche}' — run add-channels first"})
        return 1

    started = now_utc()
    run_id = f"{args.niche}-{started.astimezone():%Y-%m-%d-%H%M%S}"
    conn = open_db()
    conn.execute(
        "INSERT OR REPLACE INTO runs (run_id, niche_slug, started_at, status, cost_usd, requests) VALUES (?, ?, ?, 'running', 0.0, 0)",
        (run_id, args.niche, iso(started)),
    )
    conn.commit()

    seeds = [clean_handle(seed) for seed in niche.get("seeds", [])][:MAX_CHANNELS_PER_RUN]
    errors: list[dict[str, str]] = []
    notes: list[str] = []
    fetched = skipped = failed = 0
    videos_seen = videos_new = snapshots_added = 0
    requests = 0
    ttl_cutoff = started.timestamp() - FRESHNESS_TTL_HOURS * 3600

    for index, handle in enumerate(seeds):
        row = conn.execute("SELECT * FROM channels WHERE lower(handle) = lower(?)", (handle,)).fetchone()
        if not args.force and row and row["fetch_status"] == "ok" and row["last_refreshed_at"]:
            try:
                if datetime.fromisoformat(row["last_refreshed_at"]).timestamp() > ttl_cutoff:
                    skipped += 1
                    continue
            except ValueError:
                pass
        if index > 0:
            time.sleep(random.uniform(*CHANNEL_SLEEP_RANGE))
        try:
            requests += 1
            info = fetch_channel_flat(handle)
            seen, new, snaps = store_flat_dump(conn, info, handle, run_id, iso(now_utc()))
            videos_seen += seen
            videos_new += new
            snapshots_added += snaps
            fetched += 1
            conn.commit()
        except Exception as exc:
            failed += 1
            errors.append({"channel": "@" + handle, "stage": "flat_dump", "message": str(exc)[:200]})
            if row:
                conn.execute(
                    "UPDATE channels SET fetch_status = 'failed', last_refreshed_at = ? WHERE channel_id = ?",
                    (iso(now_utc()), row["channel_id"]),
                )
                conn.commit()

    attempted = fetched + failed
    degraded_run = attempted > 0 and failed / attempted > 0.5
    if degraded_run:
        note = f"{failed}/{attempted} channel fetches failed — YouTube layout may have shifted; try: pip install -U yt-dlp"
        notes.append(note)
        degraded(None, f"outlier-radar refresh {run_id}: {note}")

    channel_rows = [
        row for handle in seeds
        if (row := conn.execute("SELECT * FROM channels WHERE lower(handle) = lower(?)", (handle,)).fetchone())
    ]
    scoring_time = now_utc()
    records = score_niche(conn, channel_rows, scoring_time)
    watchlist, transcripts_written, enrich_requests = enrich_outliers(conn, records, args.enrich_cap, errors)
    requests += enrich_requests
    conn.commit()

    channels_with_data = {record["channel_id"] for record in records}
    if not channels_with_data:
        youtube_coverage = "none"
    elif failed or len(channels_with_data) < len(seeds):
        youtube_coverage = "partial"
    else:
        youtube_coverage = "measured"

    status = "degraded" if degraded_run else "ok"
    receipt_path = RECEIPTS_DIR / f"{run_id}.json"
    pack = {
        "pack_version": PACK_VERSION,
        "niche_slug": args.niche,
        "niche_label": niche.get("label", args.niche),
        "generated_at": iso(now_utc()),
        "freshness_ttl_hours": FRESHNESS_TTL_HOURS,
        "run_id": run_id,
        "run_receipt_path": relative(receipt_path),
        "status": status,
        "coverage": {"youtube": youtube_coverage, "tiktok": "none", "instagram": "none"},
        "source_lanes": ["ytdlp_public"],
        "channels": [
            {
                "channel_id": row["channel_id"],
                "handle": "@" + row["handle"],
                "title": row["title"],
                "subscriber_count": row["subscriber_count"],
                "median_vpd": row["median_vpd"],
                "fetch_status": row["fetch_status"],
                "last_refreshed_at": row["last_refreshed_at"],
            }
            for row in (
                conn.execute("SELECT * FROM channels WHERE lower(handle) = lower(?)", (handle,)).fetchone()
                for handle in seeds
            )
            if row
        ],
        "ranked_videos": records[:RANKED_CAP],
        "leaderboard": build_leaderboard(records),
        "watchlist_adds": watchlist,
        "cost": {"usd": 0.0, "yt_dlp_requests": requests},
        "errors": errors,
    }
    pack_path = write_pack(pack, args.niche)

    receipt = RunReceipt(
        run_id=run_id,
        generated_at=iso(now_utc()),
        niche_slug=args.niche,
        channels_attempted=attempted,
        channels_fetched=fetched,
        channels_skipped_ttl=skipped,
        channels_failed=failed,
        videos_seen=videos_seen,
        videos_new=videos_new,
        snapshots_added=snapshots_added,
        outliers_flagged=len(watchlist),
        transcripts_written=transcripts_written,
        yt_dlp_requests=requests,
        cost_usd=0.0,
        status=status,
        pack_path=relative(pack_path),
        notes=notes,
        errors=errors,
    )
    RECEIPTS_DIR.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(asdict(receipt), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    conn.execute(
        "UPDATE runs SET finished_at = ?, status = ?, cost_usd = 0.0, requests = ? WHERE run_id = ?",
        (iso(now_utc()), status, requests, run_id),
    )
    conn.commit()
    conn.close()

    receipt_line(
        {
            "cmd": "refresh", "niche": args.niche, "status": status, "run_id": run_id,
            "channels": f"{fetched} fetched / {skipped} ttl-skipped / {failed} failed",
            "videos_seen": videos_seen, "snapshots_added": snapshots_added,
            "outliers_flagged": len(watchlist), "transcripts_written": transcripts_written,
            "pack": relative(pack_path), "receipt": relative(receipt_path),
            "cost_usd": 0.0, "yt_dlp_requests": requests,
        }
    )
    return 0


# ---------------------------------------------------------------------------
# Other commands
# ---------------------------------------------------------------------------

def latest_pack_path(niche_slug: str) -> Path:
    return PACKS_DIR / niche_slug / "latest.json"


def cmd_pack(args: argparse.Namespace) -> int:
    path = latest_pack_path(args.niche)
    if not path.exists():
        receipt_line({"cmd": "pack", "niche": args.niche, "status": "error", "message": "no pack yet — run refresh"})
        return 1
    pack = json.loads(path.read_text(encoding="utf-8"))
    receipt_line(
        {
            "cmd": "pack", "niche": args.niche, "status": pack.get("status"),
            "path": relative(path), "generated_at": pack.get("generated_at"),
            "ranked_videos": len(pack.get("ranked_videos", [])),
            "above_winner_line": sum(
                1 for record in pack.get("ranked_videos", []) if record.get("winner_line_status") == "above_winner_line"
            ),
            "coverage": pack.get("coverage"),
        }
    )
    return 0


def cmd_add_channels(args: argparse.Namespace) -> int:
    niches = load_niches()
    entry = niches.setdefault(args.niche, {"label": args.label or args.niche, "seeds": []})
    if args.label:
        entry["label"] = args.label
    existing = {clean_handle(seed).lower() for seed in entry["seeds"]}
    added = []
    for handle in args.handles:
        cleaned = clean_handle(handle)
        if cleaned and cleaned.lower() not in existing:
            entry["seeds"].append("@" + cleaned)
            existing.add(cleaned.lower())
            added.append("@" + cleaned)
    save_niches(niches)
    receipt_line(
        {
            "cmd": "add-channels", "niche": args.niche, "status": "ok",
            "added": added, "total_seeds": len(entry["seeds"]), "path": relative(CHANNELS_JSON),
        }
    )
    return 0


def cmd_emit_radar_rows(args: argparse.Namespace) -> int:
    path = latest_pack_path(args.niche)
    if not path.exists():
        receipt_line({"cmd": "emit-radar-rows", "niche": args.niche, "status": "error", "message": "no pack yet — run refresh"})
        return 1
    pack = json.loads(path.read_text(encoding="utf-8"))
    conn = open_db()
    # radar's multiplier is views/avg_views, so avg_views must be a raw-view
    # median (not vpd): compute per channel from the latest snapshots.
    median_views_by_channel: dict[str, float] = {}
    for record in pack.get("ranked_videos", []):
        channel_id = record["channel_id"]
        if channel_id in median_views_by_channel:
            continue
        video_ids = [
            row["video_id"]
            for row in conn.execute("SELECT video_id FROM videos WHERE channel_id = ?", (channel_id,)).fetchall()
        ]
        views = [value for value in latest_views_by_video(conn, video_ids).values() if value and value > 0]
        if views:
            median_views_by_channel[channel_id] = statistics.median(views)
    conn.close()

    rows = [
        {
            "platform": "youtube",
            "creator": record["channel_handle"],
            "url": record["url"],
            "published_at": record["published_at"] or "",
            "title": record["title"],
            "hook_text": record["hook_text"],
            "caption": "",
            "topic": record["topic"],
            "format_hint": record["format_hint"],
            "views": record["views"],
            "avg_views": median_views_by_channel.get(record["channel_id"]),
            "evidence_lane": "public_web",
            "permission_status": "public_read_only",
        }
        for record in pack.get("ranked_videos", [])
    ]
    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = ROOT / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    receipt_line({"cmd": "emit-radar-rows", "niche": args.niche, "status": "ok", "rows": len(rows), "out": relative(out_path)})
    return 0


def cmd_status(_args: argparse.Namespace) -> int:
    niches = load_niches()
    if not niches:
        receipt_line({"cmd": "status", "status": "empty", "message": "no niches configured — run add-channels"})
        return 0
    conn = open_db()
    now = now_utc()
    for slug, entry in niches.items():
        seeds = [clean_handle(seed) for seed in entry.get("seeds", [])]
        fresh = 0
        for handle in seeds:
            row = conn.execute(
                "SELECT last_refreshed_at, fetch_status FROM channels WHERE lower(handle) = lower(?)", (handle,)
            ).fetchone()
            if row and row["fetch_status"] == "ok" and row["last_refreshed_at"]:
                try:
                    age_h = (now - datetime.fromisoformat(row["last_refreshed_at"])).total_seconds() / 3600
                    if age_h < FRESHNESS_TTL_HOURS:
                        fresh += 1
                except ValueError:
                    pass
        pack_path = latest_pack_path(slug)
        pack_at = None
        if pack_path.exists():
            try:
                pack_at = json.loads(pack_path.read_text(encoding="utf-8")).get("generated_at")
            except (json.JSONDecodeError, OSError):
                pass
        receipt_line(
            {
                "cmd": "status", "niche": slug, "label": entry.get("label", slug),
                "seeds": len(seeds), "fresh_channels": f"{fresh}/{len(seeds)}",
                "ttl_hours": FRESHNESS_TTL_HOURS, "latest_pack": pack_at or "never",
            }
        )
    conn.close()
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Outlier Radar — yt-dlp data spine for the Kallaway trend/hook stack.")
    sub = parser.add_subparsers(dest="command", required=True)

    refresh = sub.add_parser("refresh", help="Fetch + score + enrich + write signal pack for one niche.")
    refresh.add_argument("--niche", required=True)
    refresh.add_argument("--enrich-cap", type=int, default=ENRICH_CAP, help="Max flagged outliers to enrich this run.")
    refresh.add_argument("--force", action="store_true", help="Bypass the per-channel TTL (testing/velocity runs).")
    refresh.set_defaults(func=cmd_refresh)

    pack = sub.add_parser("pack", help="Print latest pack path + one-line summary.")
    pack.add_argument("--niche", required=True)
    pack.set_defaults(func=cmd_pack)

    add = sub.add_parser("add-channels", help="Seed channels into a niche.")
    add.add_argument("--niche", required=True)
    add.add_argument("--label", default="")
    add.add_argument("handles", nargs="+", help="@handles to add.")
    add.set_defaults(func=cmd_add_channels)

    emit = sub.add_parser("emit-radar-rows", help="Radar-compatible rows JSON for --signals-json interop.")
    emit.add_argument("--niche", required=True)
    emit.add_argument("--out", required=True)
    emit.set_defaults(func=cmd_emit_radar_rows)

    status = sub.add_parser("status", help="Freshness per niche.")
    status.set_defaults(func=cmd_status)

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
