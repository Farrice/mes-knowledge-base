#!/usr/bin/env python3
"""
Seedance 2.0 image-to-video wrapper for fantastic-posters skill.

Endpoint: bytedance/seedance-2.0/image-to-video
Pricing:
  480p:  ~$0.13/sec
  720p:  ~$0.30/sec  (default)
  1080p: ~$0.68/sec  ← HARD-BLOCKED in budget guard, refused here too

Usage:
  python3 fal_video_seedance.py \\
      --prompt "<motion description>" \\
      --image "<local path or URL>" \\
      --duration 6 --resolution 720p --aspect auto --audio on

  Optional: --end-image <path/url>, --aspect 16:9|9:16|1:1|21:9|4:3|3:4|auto, --seed N

ALWAYS pre-flight via:
  python3 execution/fal_budget_guard.py check --mode=seedance-<res> --duration=<N>

After call, log via:
  python3 execution/fal_budget_guard.py log --mode=seedance-<res> --duration=<N> \\
      --status=success --actual-cost=<computed>
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
OUT_DIR = ROOT / "skills" / "fantastic-posters" / "out"
FAL_GUARD = ROOT / "execution" / "fal_budget_guard.py"

PRICING_PER_SEC = {"480p": 0.13, "720p": 0.3024, "1080p": 0.68}
ALLOWED_DURATIONS = list(range(4, 16))  # 4..15
ALLOWED_RESOLUTIONS = ("480p", "720p", "1080p")
ALLOWED_ASPECT = ("auto", "21:9", "16:9", "4:3", "1:1", "3:4", "9:16")


def record_spend(*, resolution: str, duration: int, status: str, actual_cost: float | None = None,
                  audio: str = "", output_path: str = "", brief: str = "") -> None:
    """Deterministically log spend via fal_budget_guard.py — never rely on the caller
    remembering to run the printed command (that AI-memory-dependent pattern is exactly
    why fal-usage.json went stale 2026-05→07)."""
    cmd = ["python3", str(FAL_GUARD), "log", f"--mode=seedance-{resolution}",
           f"--duration={duration}", f"--status={status}"]
    if audio:
        cmd.append(f"--audio={audio}")
    if actual_cost is not None:
        cmd.append(f"--actual-cost={actual_cost}")
    if output_path:
        cmd.append(f"--output-path={output_path}")
    if brief:
        cmd.append(f"--brief={brief}")
    # Note: we don't know whether Fal actually billed a failed call, so we default to
    # NOT setting --fal-billed (conservative: undercounting a rare billed-failure beats
    # inflating every transient error into phantom spend). Re-run manually with
    # --fal-billed if you confirm Fal charged for this specific failure.
    try:
        subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, timeout=15, check=True)
    except Exception as e:
        print(f"⚠️  fal_budget_guard log FAILED (spend not recorded): {e}")


def load_fal_key() -> str:
    if os.environ.get("FAL_KEY"):
        return os.environ["FAL_KEY"]
    if not ENV_PATH.exists():
        sys.exit(f"ERROR: FAL_KEY not in env and {ENV_PATH} not found")
    for line in ENV_PATH.read_text().splitlines():
        if line.startswith("FAL_KEY="):
            key = line.split("=", 1)[1].strip()
            if key:
                os.environ["FAL_KEY"] = key
                return key
    sys.exit(f"ERROR: FAL_KEY not found in {ENV_PATH}")


def is_url(s: str) -> bool:
    return s.startswith("http://") or s.startswith("https://")


def estimate_cost(resolution: str, duration: int) -> float:
    return round(PRICING_PER_SEC[resolution] * duration, 4)


def download_video(url: str, dest: Path) -> None:
    print(f"  source URL: {url}", flush=True)
    print(f"  → downloading MP4 to {dest.relative_to(ROOT)}", flush=True)
    try:
        import requests
        r = requests.get(url, stream=True, timeout=120)
        r.raise_for_status()
        with dest.open("wb") as f:
            for chunk in r.iter_content(chunk_size=1 << 20):
                f.write(chunk)
        size_mb = dest.stat().st_size / (1024 * 1024)
        print(f"  ✓ saved via requests ({size_mb:.1f} MB)", flush=True)
        return
    except Exception as e:
        print(f"  requests download failed ({e}); trying curl fallback...", flush=True)
    try:
        subprocess.run(["curl", "-fsSL", "-o", str(dest), url], check=True, timeout=120)
        size_mb = dest.stat().st_size / (1024 * 1024)
        print(f"  ✓ saved via curl ({size_mb:.1f} MB)", flush=True)
        return
    except Exception as e:
        print(f"  curl fallback also failed ({e})", flush=True)
        print(f"\n⚠️  Local download failed but the video EXISTS at the URL above.")
        print(f"  Manually download via:  curl -o '{dest}' '{url}'")
        raise


def main() -> int:
    p = argparse.ArgumentParser(description="Seedance 2.0 image-to-video via Fal")
    p.add_argument("--prompt", required=True, help="Motion / action description for the video")
    p.add_argument("--image", required=True, help="Starting frame: local path or URL")
    p.add_argument("--duration", type=int, default=5, choices=ALLOWED_DURATIONS,
                   help="Video duration in seconds (4-15). Default: 5")
    p.add_argument("--resolution", default="720p", choices=ALLOWED_RESOLUTIONS,
                   help="Video resolution. 1080p is HARD-BLOCKED. Default: 720p")
    p.add_argument("--aspect", default="auto", choices=ALLOWED_ASPECT,
                   help="Aspect ratio. Default: auto (infer from input)")
    p.add_argument("--audio", choices=["on", "off"], default="on",
                   help="Generate synchronized audio. Default: on (cost is identical)")
    p.add_argument("--end-image", default=None, help="Optional ending frame: local path or URL")
    p.add_argument("--seed", type=int, default=None, help="Optional seed for reproducibility")
    p.add_argument("--dry-run", action="store_true", help="Validate args + load env, no API call")
    args = p.parse_args()

    # Hard-block 1080p
    if args.resolution == "1080p":
        print("ERROR: --resolution=1080p is HARD-BLOCKED. Single 15s call ~$10.21 (50% of wallet).")
        print("  Use --resolution=720p (max ~$4.54 for 15s, ceiling allows ~10s).")
        print("  See directives/fal-usage-policy.md")
        return 2

    estimated = estimate_cost(args.resolution, args.duration)
    print(f"Seedance 2.0  |  {args.resolution}  |  {args.duration}s  |  audio={args.audio}")
    print(f"Estimated cost: ${estimated:.4f}")
    print(f"  (per-second @ {args.resolution}: ${PRICING_PER_SEC[args.resolution]:.4f})")

    if args.dry_run:
        print("DRY RUN — no API call.")
        return 0

    load_fal_key()
    import fal_client  # imported after env is loaded

    # Resolve start image
    if is_url(args.image):
        image_url = args.image
        print(f"Start image: {image_url}")
    else:
        path = Path(args.image)
        if not path.is_absolute():
            path = (ROOT / path).resolve()
        if not path.exists():
            sys.exit(f"ERROR: start image not found: {path}")
        print(f"Uploading start image: {path.relative_to(ROOT)}")
        image_url = fal_client.upload_file(str(path))
        print(f"  ✓ uploaded: {image_url}")

    # Resolve optional end image
    end_url = None
    if args.end_image:
        if is_url(args.end_image):
            end_url = args.end_image
        else:
            ep = Path(args.end_image)
            if not ep.is_absolute():
                ep = (ROOT / ep).resolve()
            if not ep.exists():
                sys.exit(f"ERROR: end image not found: {ep}")
            print(f"Uploading end image: {ep.relative_to(ROOT)}")
            end_url = fal_client.upload_file(str(ep))
            print(f"  ✓ uploaded: {end_url}")

    arguments = {
        "prompt": args.prompt,
        "image_url": image_url,
        "resolution": args.resolution,
        "duration": str(args.duration),
        "aspect_ratio": args.aspect,
        "generate_audio": args.audio == "on",
    }
    if end_url:
        arguments["end_image_url"] = end_url
    if args.seed is not None:
        arguments["seed"] = args.seed

    print("Submitting to Fal queue...")
    started = time.time()

    def on_update(update):
        if hasattr(update, "logs") and update.logs:
            for log in update.logs:
                msg = log.get("message", "") if isinstance(log, dict) else str(log)
                if msg:
                    print(f"  [fal] {msg}", flush=True)

    try:
        result = fal_client.subscribe(
            "bytedance/seedance-2.0/image-to-video",
            arguments=arguments,
            with_logs=True,
            on_queue_update=on_update,
        )
    except Exception as e:
        elapsed = time.time() - started
        print(f"\n❌ Seedance call FAILED after {elapsed:.1f}s: {e}")
        record_spend(resolution=args.resolution, duration=args.duration, status="failed",
                     audio=args.audio, brief=args.prompt[:60])
        return 1

    elapsed = time.time() - started
    print(f"\n✓ Generation complete in {elapsed:.1f}s")

    video = result.get("video", {})
    video_url = video.get("url")
    if not video_url:
        print(f"⚠️  Unexpected response shape (no video.url): {result}")
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"seedance-{args.resolution}_{args.duration}s_{ts}.mp4"
    dest = OUT_DIR / fname
    download_video(video_url, dest)

    print()
    print(f"Output:        {dest.relative_to(ROOT)}")
    print(f"Estimated cost: ${estimated:.4f}")
    print(f"Seed: {result.get('seed', '?')}")
    record_spend(resolution=args.resolution, duration=args.duration, status="success",
                 actual_cost=estimated, audio=args.audio,
                 output_path=str(dest.relative_to(ROOT)), brief=args.prompt[:60])
    print("Spend logged via fal_budget_guard.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
