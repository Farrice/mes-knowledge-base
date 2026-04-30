#!/usr/bin/env python3
"""
Kling Video v3 Pro image-to-video wrapper for fantastic-posters skill.

Endpoint: fal-ai/kling-video/v3/pro/image-to-video
Pricing (per second of generated video):
  audio off:      $0.112
  audio on:       $0.168
  voice control:  $0.196

Per-call ceiling: $2.00 (covers ~10s with audio on, or ~17s audio off — capped at 15s by API).

Usage (single-prompt):
  python3 fal_video_kling.py \\
      --prompt "<motion description>" \\
      --start-image "<local path or URL>" \\
      --duration 5 --audio on

Usage (multi-shot narrative):
  python3 fal_video_kling.py \\
      --start-image "<path>" \\
      --multi-prompt path/to/shots.json \\
      --duration 12 --audio on

  multi-prompt JSON shape:
    [{"prompt": "shot 1 description"}, {"prompt": "shot 2 description"}, ...]

Usage (with custom elements):
  python3 fal_video_kling.py \\
      --prompt "@Element1 walks through @Element2" \\
      --start-image "<path>" \\
      --elements path/to/elements.json \\
      --duration 5

  elements JSON shape (mix of image-based and video-based references):
    [
      {"reference_image_urls": ["url"], "frontal_image_url": "url"},
      {"video_url": "url"}
    ]

ALWAYS pre-flight via:
  python3 execution/fal_budget_guard.py check --mode=kling --duration=<N> --audio=<off|on|voice_control>
"""
from __future__ import annotations

import argparse
import json
import os
import ssl
import subprocess
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
OUT_DIR = ROOT / "skills" / "fantastic-posters" / "out"

PRICING_PER_SEC = {"off": 0.112, "on": 0.168, "voice_control": 0.196}
ALLOWED_DURATIONS = list(range(3, 16))  # 3..15


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


def estimate_cost(audio_mode: str, duration: int) -> float:
    return round(PRICING_PER_SEC[audio_mode] * duration, 4)


def resolve_image(arg: str, fal_client_mod, label: str) -> str:
    if is_url(arg):
        return arg
    path = Path(arg)
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    if not path.exists():
        sys.exit(f"ERROR: {label} image not found: {path}")
    print(f"Uploading {label}: {path.relative_to(ROOT)}", flush=True)
    url = fal_client_mod.upload_file(str(path))
    print(f"  ✓ uploaded: {url}", flush=True)
    return url


def download_video(url: str, dest: Path) -> None:
    print(f"  source URL: {url}", flush=True)
    print(f"  → downloading MP4 to {dest.relative_to(ROOT)}", flush=True)
    # Try requests first (handles cert chain better than urllib)
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
    # Fallback to system curl
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
    p = argparse.ArgumentParser(description="Kling v3 Pro image-to-video via Fal")
    p.add_argument("--prompt", default=None, help="Single-shot prompt. Either --prompt or --multi-prompt required.")
    p.add_argument("--multi-prompt", default=None,
                   help="Path to JSON file with array of {prompt: str} entries for multi-shot.")
    p.add_argument("--start-image", required=True, help="Starting frame: local path or URL")
    p.add_argument("--end-image", default=None, help="Optional ending frame: local path or URL")
    p.add_argument("--duration", type=int, default=5, choices=ALLOWED_DURATIONS,
                   help="Duration in seconds (3-15). Default: 5")
    p.add_argument("--audio", choices=["off", "on", "voice_control"], default="on",
                   help="Audio mode. Default: on")
    p.add_argument("--elements", default=None,
                   help="Path to JSON file with element refs for character/object consistency")
    p.add_argument("--negative-prompt", default="blur, distort, and low quality")
    p.add_argument("--cfg-scale", type=float, default=0.5, help="0..1, prompt adherence. Default: 0.5")
    p.add_argument("--shot-type", default="customize", help="Multi-shot type. Default: customize")
    p.add_argument("--dry-run", action="store_true", help="Validate args + load env, no API call")
    args = p.parse_args()

    # Validate prompt mode
    if args.prompt and args.multi_prompt:
        sys.exit("ERROR: pass --prompt OR --multi-prompt, not both.")
    if not args.prompt and not args.multi_prompt:
        sys.exit("ERROR: must pass --prompt or --multi-prompt.")

    # Load multi-prompt if given
    multi_prompt_data = None
    if args.multi_prompt:
        mp_path = Path(args.multi_prompt)
        if not mp_path.is_absolute():
            mp_path = (ROOT / mp_path).resolve()
        if not mp_path.exists():
            sys.exit(f"ERROR: multi-prompt file not found: {mp_path}")
        with mp_path.open() as f:
            multi_prompt_data = json.load(f)
        if not isinstance(multi_prompt_data, list) or not all("prompt" in e for e in multi_prompt_data):
            sys.exit("ERROR: multi-prompt JSON must be array of {prompt: str} objects")

    # Load elements if given
    elements_data = None
    if args.elements:
        el_path = Path(args.elements)
        if not el_path.is_absolute():
            el_path = (ROOT / el_path).resolve()
        if not el_path.exists():
            sys.exit(f"ERROR: elements file not found: {el_path}")
        with el_path.open() as f:
            elements_data = json.load(f)

    estimated = estimate_cost(args.audio, args.duration)
    print(f"Kling v3 Pro  |  {args.duration}s  |  audio={args.audio}")
    print(f"Estimated cost: ${estimated:.4f}")
    print(f"  (per-second @ audio={args.audio}: ${PRICING_PER_SEC[args.audio]:.4f})")

    if args.dry_run:
        print("DRY RUN — no API call.")
        return 0

    load_fal_key()
    import fal_client

    start_url = resolve_image(args.start_image, fal_client, "start image")
    end_url = resolve_image(args.end_image, fal_client, "end image") if args.end_image else None

    arguments = {
        "start_image_url": start_url,
        "duration": str(args.duration),
        "generate_audio": args.audio != "off",
        "negative_prompt": args.negative_prompt,
        "cfg_scale": args.cfg_scale,
    }
    if args.prompt:
        arguments["prompt"] = args.prompt
    if multi_prompt_data:
        arguments["multi_prompt"] = multi_prompt_data
        arguments["shot_type"] = args.shot_type
    if end_url:
        arguments["end_image_url"] = end_url
    if elements_data:
        arguments["elements"] = elements_data

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
            "fal-ai/kling-video/v3/pro/image-to-video",
            arguments=arguments,
            with_logs=True,
            on_queue_update=on_update,
        )
    except Exception as e:
        elapsed = time.time() - started
        print(f"\n❌ Kling call FAILED after {elapsed:.1f}s: {e}")
        print(f"\nTo log the failure:")
        print(f"  python3 execution/fal_budget_guard.py log --mode=kling "
              f"--duration={args.duration} --audio={args.audio} --status=failed [--fal-billed]")
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
    fname = f"kling_{args.duration}s_audio-{args.audio}_{ts}.mp4"
    dest = OUT_DIR / fname
    download_video(video_url, dest)

    print()
    print(f"Output:         {dest.relative_to(ROOT)}")
    print(f"Estimated cost: ${estimated:.4f}")
    print()
    print(f"Now log spend:")
    brief_short = (args.prompt or f"multi-shot {len(multi_prompt_data)} prompts")[:60]
    print(f"  python3 execution/fal_budget_guard.py log --mode=kling "
          f"--duration={args.duration} --audio={args.audio} --status=success "
          f"--actual-cost={estimated} --output-path='{dest.relative_to(ROOT)}' "
          f"--brief='{brief_short}'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
