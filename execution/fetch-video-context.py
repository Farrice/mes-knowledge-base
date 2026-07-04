#!/usr/bin/env python3
"""
fetch-video-context.py — Deterministic wrapper around the claude-video plugin (`/watch`).

Gives every extraction workflow access to visual frames + Whisper-grade transcripts
without depending on the AI assistant remembering to invoke the `/watch` slash command.
(See feedback_ai-memory-dependent-observability.md — banned pattern as of 2026-05-03.)

Usage:
    python3 execution/fetch-video-context.py <source> [expert_name] [options]

Examples:
    python3 execution/fetch-video-context.py "https://www.youtube.com/watch?v=QZMljuD10sU" brad-bonanno
    python3 execution/fetch-video-context.py "/path/to/local.mp4" my-recording
    python3 execution/fetch-video-context.py "https://youtu.be/abc" --no-vision   # explicit skip

Options:
    --max-frames N      Override frame budget (default: claude-video chooses based on duration)
    --max-duration SEC  Override the 600s skip threshold (default 600 = 10 min)
    --no-vision         Force SKIP — useful for testing transcript-only flow
    --force             Re-fetch even if visual-context.md already exists
    --whisper           Allow Whisper API fallback if no native captions (requires GROQ_API_KEY)

Exit codes:
    0  OK         — visual-context.md created (or already cached)
    2  SKIPPED    — non-video source, >10min, --no-vision, or no plugin
    1  FAILED     — system dep missing, network failure, or plugin error

Outputs:
    extractions/<expert>/visual-context.md      — markdown report (frame paths + transcript)
    extractions/<expert>/frames/                 — JPEG frames extracted by ffmpeg
    .agent/video-vision-log.jsonl                — append-only invocation log
"""

import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from glob import glob
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
EXTRACTIONS_DIR = PROJECT_ROOT / "extractions"
LOG_PATH = PROJECT_ROOT / ".agent" / "video-vision-log.jsonl"
DEFAULT_MAX_DURATION_SEC = 600  # 10 minutes — matches claude-video's own sweet spot

# Extend PATH so we resolve Homebrew-installed deps (ffmpeg/ffprobe/yt-dlp) even when
# Claude Code spawns a Bash subshell without sourcing the user's interactive shell init.
# This is intentional belt-and-suspenders alongside ~/.zshrc activation.
_HOMEBREW_BIN_PATHS = ("/opt/homebrew/bin", "/usr/local/bin")
for _p in _HOMEBREW_BIN_PATHS:
    if os.path.isdir(_p) and _p not in os.environ.get("PATH", "").split(os.pathsep):
        os.environ["PATH"] = _p + os.pathsep + os.environ.get("PATH", "")

# yt-dlp supports 1700+ sites; we recognize the common ones for fast-path detection.
# For everything else we let yt-dlp decide (any http(s) URL → try-it-and-see).
KNOWN_VIDEO_HOSTS = (
    "youtube.com", "youtu.be", "youtube-nocookie.com",
    "tiktok.com", "vimeo.com", "twitch.tv", "dailymotion.com",
    "facebook.com/watch", "fb.watch",
    "instagram.com/reel", "instagram.com/tv", "instagram.com/p/",
    "twitter.com/i/status", "x.com/i/status",
    "linkedin.com/posts",  # often contains embedded video
    "reddit.com",  # v.redd.it
    "loom.com", "wistia.com",
)

LOCAL_VIDEO_EXTENSIONS = (".mp4", ".mov", ".webm", ".mkv", ".avi", ".m4v", ".flv")


def log_event(event: dict) -> None:
    """Append an invocation event to the JSONL log. Best-effort — never raises."""
    try:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        event["timestamp"] = datetime.now(timezone.utc).isoformat()
        with LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(json.dumps(event) + "\n")
    except Exception:
        pass  # logging must never block the wrapper


def is_video_source(source: str) -> bool:
    """Heuristic: does this look like a video URL or local video file?"""
    s = source.strip()
    # Local file path
    if s.lower().endswith(LOCAL_VIDEO_EXTENSIONS):
        return Path(s).expanduser().exists()
    # URL — accept http/https with known video host, OR any yt-dlp-supported pattern
    if s.startswith(("http://", "https://")):
        s_lower = s.lower()
        if any(host in s_lower for host in KNOWN_VIDEO_HOSTS):
            return True
        # Fallback: if yt-dlp is installed, ask it whether the URL is supported.
        # If yt-dlp is missing entirely, default to True so we attempt and surface
        # the system-dep error cleanly downstream.
        ytdlp = shutil.which("yt-dlp")
        if not ytdlp:
            return True
        try:
            result = subprocess.run(
                [ytdlp, "--simulate", "--quiet", "--no-warnings", s],
                capture_output=True, timeout=10, text=True
            )
            return result.returncode == 0
        except Exception:
            return False
    return False


def find_watch_script() -> Path | None:
    """Locate the marketplace-installed claude-video plugin's watch.py.

    Searches across Claude Code, Codex, and local installations, handling both
    v0.1.x flat layout (scripts/ at root) and v0.2.0+ nested layout (skills/watch/scripts/).
    """
    home = Path.home()
    candidates = []

    # Claude Code marketplace cache — v0.2.0+ nested layout
    candidates.extend(glob(str(home / ".claude/plugins/cache/*/watch/*/skills/watch/scripts/watch.py")))
    # Claude Code marketplace cache — v0.1.x flat layout (backward compat)
    candidates.extend(glob(str(home / ".claude/plugins/cache/*/watch/*/scripts/watch.py")))

    # Claude Code direct install layout
    candidates.extend(glob(str(home / ".claude/plugins/installed/watch/scripts/watch.py")))

    # Codex marketplace cache — v0.2.0+ nested layout
    candidates.extend(glob(str(home / ".codex/plugins/cache/*/watch/*/skills/watch/scripts/watch.py")))
    # Codex marketplace cache — v0.1.x flat layout (backward compat)
    candidates.extend(glob(str(home / ".codex/plugins/cache/*/watch/*/scripts/watch.py")))

    # Project-local fallback: skills/watch/scripts/watch.py
    candidates.extend(glob(str(PROJECT_ROOT / "skills/watch/scripts/watch.py")))

    if not candidates:
        return None
    # Prefer the most recently modified (handles plugin updates cleanly)
    return Path(max(candidates, key=lambda p: os.path.getmtime(p)))


def check_system_deps() -> list[str]:
    """Return a list of missing system dependencies."""
    missing = []
    for dep in ("ffmpeg", "ffprobe", "yt-dlp"):
        if shutil.which(dep) is None:
            missing.append(dep)
    return missing


def probe_duration(source: str) -> float | None:
    """Return duration in seconds, or None if probe fails. Uses yt-dlp for URLs, ffprobe for local."""
    if source.startswith(("http://", "https://")):
        ytdlp = shutil.which("yt-dlp")
        if not ytdlp:
            return None
        try:
            result = subprocess.run(
                [ytdlp, "--print", "duration", "--simulate", "--no-warnings", source],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0 and result.stdout.strip():
                return float(result.stdout.strip().splitlines()[0])
        except Exception:
            return None
    else:
        ffprobe = shutil.which("ffprobe")
        if not ffprobe:
            return None
        try:
            result = subprocess.run(
                [ffprobe, "-v", "error", "-show_entries", "format=duration",
                 "-of", "default=noprint_wrappers=1:nokey=1", source],
                capture_output=True, text=True, timeout=15
            )
            if result.returncode == 0 and result.stdout.strip():
                return float(result.stdout.strip())
        except Exception:
            return None
    return None


def parse_args(argv: list[str]) -> dict:
    """Minimal arg parser — keep dependency-free."""
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0 if (len(argv) > 1 and argv[1] in ("-h", "--help")) else 1)

    args = {
        "source": argv[1],
        "expert_name": None,
        "max_frames": None,
        "max_duration": DEFAULT_MAX_DURATION_SEC,
        "no_vision": False,
        "force": False,
        "whisper": False,
    }

    i = 2
    while i < len(argv):
        a = argv[i]
        if a == "--no-vision":
            args["no_vision"] = True
        elif a == "--force":
            args["force"] = True
        elif a == "--whisper":
            args["whisper"] = True
        elif a == "--max-frames" and i + 1 < len(argv):
            args["max_frames"] = int(argv[i + 1]); i += 1
        elif a == "--max-duration" and i + 1 < len(argv):
            args["max_duration"] = int(argv[i + 1]); i += 1
        elif not a.startswith("--") and args["expert_name"] is None:
            args["expert_name"] = a
        i += 1

    if args["expert_name"] is None:
        # Derive a stable slug from the source so output dirs are deterministic
        slug = re.sub(r"[^a-zA-Z0-9]+", "-", args["source"]).strip("-").lower()[:48]
        args["expert_name"] = f"_unnamed-{slug}" if slug else "_unnamed"

    return args


def emit(status: str, source: str, expert_name: str, **extra) -> None:
    """Print a one-line status to stderr (parent workflow can `tee` if desired) and log."""
    msg_parts = [f"[fetch-video-context] {status}", f"source={source[:60]}", f"expert={expert_name}"]
    for k, v in extra.items():
        if v is not None:
            msg_parts.append(f"{k}={v}")
    print(" | ".join(msg_parts), file=sys.stderr)
    log_event({"status": status, "source": source, "expert_name": expert_name, **extra})


def main() -> int:
    args = parse_args(sys.argv)
    source = args["source"]
    expert_name = args["expert_name"]

    # ----- Gate 1: explicit opt-out -----
    if args["no_vision"]:
        emit("SKIPPED", source, expert_name, reason="explicit_no_vision")
        return 2

    # ----- Gate 2: is this a video source? -----
    if not is_video_source(source):
        emit("SKIPPED", source, expert_name, reason="not_a_video_source")
        return 2

    # ----- Gate 3: cache check -----
    expert_dir = EXTRACTIONS_DIR / expert_name
    visual_context_path = expert_dir / "visual-context.md"
    if visual_context_path.exists() and not args["force"]:
        emit("OK", source, expert_name, reason="cached", path=str(visual_context_path))
        print(str(visual_context_path))  # stdout for parent workflow consumption
        return 0

    # ----- Gate 4: plugin installed? -----
    watch_script = find_watch_script()
    if watch_script is None:
        emit("FAILED", source, expert_name,
             reason="plugin_not_installed",
             hint="run: /plugin marketplace add bradautomates/claude-video && /plugin install watch@bradautomates/claude-video")
        return 1

    # ----- Gate 5: system deps -----
    missing = check_system_deps()
    if missing:
        emit("FAILED", source, expert_name,
             reason="system_dep_missing", missing=",".join(missing),
             hint="run: brew install ffmpeg yt-dlp")
        return 1

    # ----- Gate 6: duration cap -----
    duration = probe_duration(source)
    if duration is not None and duration > args["max_duration"]:
        emit("SKIPPED", source, expert_name,
             reason="duration_exceeds_cap",
             duration_sec=round(duration), cap=args["max_duration"])
        return 2

    # ----- Run watch.py -----
    expert_dir.mkdir(parents=True, exist_ok=True)
    frames_dir = expert_dir / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)

    cmd = [sys.executable, str(watch_script), source, "--out-dir", str(expert_dir)]
    if args["max_frames"] is not None:
        cmd.extend(["--max-frames", str(args["max_frames"])])
    if not args["whisper"]:
        # Suppress Whisper fallback by default — surface "uncaptioned" cleanly instead
        cmd.append("--no-whisper")

    start = time.time()
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    except subprocess.TimeoutExpired:
        emit("FAILED", source, expert_name, reason="watch_py_timeout", elapsed_sec=900)
        return 1
    except Exception as e:
        emit("FAILED", source, expert_name, reason="watch_py_exception", error=str(e))
        return 1
    elapsed = round(time.time() - start, 1)

    if result.returncode != 0:
        # Detect the "uncaptioned, no whisper key" case for cleaner reporting
        stderr_lower = (result.stderr or "").lower()
        if "whisper" in stderr_lower and ("groq" in stderr_lower or "openai" in stderr_lower or "api key" in stderr_lower):
            emit("SKIPPED", source, expert_name,
                 reason="uncaptioned_no_whisper_key",
                 hint="set GROQ_API_KEY or pass --whisper to enable transcription fallback",
                 elapsed_sec=elapsed)
            return 2
        emit("FAILED", source, expert_name,
             reason="watch_py_nonzero",
             returncode=result.returncode,
             stderr_tail=(result.stderr or "")[-500:],
             elapsed_sec=elapsed)
        return 1

    # ----- Capture stdout as the report -----
    # claude-video's watch.py prints the report (frame paths + timestamped transcript) to stdout.
    # The skill model: Claude reads this stdout, then Read()s each frame path inline.
    # We persist it as visual-context.md so workflows can load it like any other source artifact.
    stdout_text = (result.stdout or "").strip()
    frame_files = sorted(frames_dir.glob("*"))

    with visual_context_path.open("w", encoding="utf-8") as f:
        f.write(f"# Visual Context — {expert_name}\n\n")
        f.write(f"**Source**: {source}\n")
        f.write(f"**Duration**: {round(duration)}s\n" if duration else "**Duration**: unknown\n")
        f.write(f"**Frames extracted**: {len(frame_files)}\n")
        f.write(f"**Frames directory**: `{frames_dir.relative_to(PROJECT_ROOT)}`\n\n")
        f.write("> **How to read this**: The block below is `watch.py`'s native output. Frame paths reference\n")
        f.write("> `frames/frame_NNNN.jpg` — `Read` each frame inline to combine vision with the transcript.\n\n")
        f.write("---\n\n")
        if stdout_text:
            f.write(stdout_text)
            if not stdout_text.endswith("\n"):
                f.write("\n")
        else:
            f.write("> Note: watch.py emitted no stdout report. Frames are at `frames/` for direct Read access.\n")

    frame_count = len(list(frames_dir.glob("*"))) if frames_dir.exists() else 0
    emit("OK", source, expert_name,
         path=str(visual_context_path),
         frames=frame_count,
         duration_sec=round(duration) if duration else None,
         elapsed_sec=elapsed)
    print(str(visual_context_path))  # stdout for parent workflow consumption
    return 0


if __name__ == "__main__":
    sys.exit(main())
