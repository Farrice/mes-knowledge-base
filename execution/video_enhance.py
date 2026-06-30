#!/usr/bin/env python3
"""Create inspection-friendly video enhancement outputs with transparent logs.

This tool is a viewing aid. It must not be used to claim forensic proof,
contact, fault, or causation.
"""

from __future__ import annotations

import argparse
import array
import hashlib
import json
import math
import re
import shutil
import struct
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_ROOT = ROOT / "deliverables" / "video-enhancement"
DEFAULT_TMP_ROOT = ROOT / ".tmp" / "video-enhancement"

DISCLAIMER = (
    "Enhanced output is a viewing aid only. It does not prove contact, fault, "
    "causation, or responsibility."
)

IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}
CONTACT_SHEET_COLUMNS = 3
CONTACT_SHEET_ROWS = 3
CONTACT_SHEET_TILE_WIDTH = 320
CONTACT_SHEET_PADDING = 8
PREMIUM_TIER_NOTE = (
    "Premium tier uses stronger local FFmpeg restoration filters as a Topaz-like "
    "viewing workflow approximation. It is not Topaz Video AI and is not forensic proof."
)


class ProcessingError(RuntimeError):
    """Raised when a required processing step fails."""


class JsonlLogger:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def event(self, step: str, status: str, **fields: Any) -> None:
        payload = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "step": step,
            "status": status,
            **fields,
        }
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")


def command_path(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise ProcessingError(f"Required command not found: {name}")
    return path


def detect_topaz_video_ai() -> str | None:
    candidates = [
        Path("/Applications/Topaz Video AI.app"),
        Path("/Applications/Topaz Video AI.app/Contents/MacOS/Topaz Video AI"),
        Path("/Applications/Topaz Video AI.app/Contents/MacOS/ffmpeg"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    for name in ["topaz-video-ai", "tvai", "tvai_up", "tvai_updater"]:
        path = shutil.which(name)
        if path:
            return path
    return None


def detect_optional_capabilities(logger: JsonlLogger) -> dict[str, Any]:
    capabilities: dict[str, Any] = {
        "realesrgan_ncnn_vulkan": {
            "available": False,
            "path": None,
            "role": "optional AI frame upscaling",
        },
        "topaz_video_ai": {
            "available": False,
            "path": None,
            "role": "optional proprietary video restoration, not invoked by this local FFmpeg pipeline",
        },
    }

    realesrgan_path = shutil.which("realesrgan-ncnn-vulkan")
    if realesrgan_path:
        capabilities["realesrgan_ncnn_vulkan"].update({"available": True, "path": realesrgan_path})
        logger.event("capability_check", "found", tool="realesrgan-ncnn-vulkan", path=realesrgan_path)
    else:
        logger.event(
            "capability_check",
            "skipped",
            tool="realesrgan-ncnn-vulkan",
            reason="not installed or not on PATH",
        )

    topaz_path = detect_topaz_video_ai()
    if topaz_path:
        capabilities["topaz_video_ai"].update({"available": True, "path": topaz_path})
        logger.event("capability_check", "found", tool="Topaz Video AI", path=topaz_path)
    else:
        photo_note = ""
        if Path("/Applications/Topaz Photo AI.app").exists():
            photo_note = " Topaz Photo AI was detected, but it is not the video restoration app."
        logger.event(
            "capability_check",
            "skipped",
            tool="Topaz Video AI",
            reason=f"Topaz Video AI was not detected.{photo_note}".strip(),
        )

    return capabilities


def sanitize_stem(path: Path) -> str:
    stem = re.sub(r"[^a-zA-Z0-9._-]+", "-", path.stem).strip("-._")
    return stem or "video"


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tail(text: str, limit: int = 4000) -> str:
    text = text or ""
    if len(text) <= limit:
        return text
    return text[-limit:]


def run_command(
    args: list[str],
    logger: JsonlLogger,
    step: str,
    cwd: Path = ROOT,
    timeout: int | None = None,
    required: bool = True,
) -> subprocess.CompletedProcess[str]:
    started = time.time()
    logger.event(step, "started", command=args, cwd=str(cwd))
    result = subprocess.run(
        args,
        cwd=str(cwd),
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    elapsed = round(time.time() - started, 3)
    logger.event(
        step,
        "completed" if result.returncode == 0 else "failed",
        command=args,
        returncode=result.returncode,
        elapsed_seconds=elapsed,
        stdout_tail=tail(result.stdout),
        stderr_tail=tail(result.stderr),
    )
    if required and result.returncode != 0:
        raise ProcessingError(f"{step} failed with return code {result.returncode}: {tail(result.stderr, 1000)}")
    return result


def parse_rate(rate: str | None) -> float:
    if not rate or rate == "0/0":
        return 30.0
    if "/" in rate:
        num, den = rate.split("/", 1)
        denominator = float(den)
        if denominator == 0:
            return 30.0
        return float(num) / denominator
    return float(rate)


def format_rate(rate: float) -> str:
    if abs(rate - round(rate)) < 0.001:
        return str(int(round(rate)))
    return f"{rate:.3f}".rstrip("0").rstrip(".")


def duration_seconds(metadata: dict[str, Any]) -> float:
    try:
        return float((metadata.get("format") or {}).get("duration") or 0.0)
    except (TypeError, ValueError):
        return 0.0


def ffprobe(video_path: Path, logger: JsonlLogger) -> dict[str, Any]:
    ffprobe_bin = command_path("ffprobe")
    result = run_command(
        [
            ffprobe_bin,
            "-v",
            "error",
            "-show_entries",
            "format=duration,size,format_name:stream=index,codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,duration,bit_rate",
            "-of",
            "json",
            str(video_path),
        ],
        logger,
        "ffprobe_metadata",
        timeout=60,
    )
    try:
        metadata = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise ProcessingError(f"ffprobe returned invalid JSON for {video_path}") from exc
    if not video_stream(metadata):
        raise ProcessingError(f"Input does not contain a video stream: {video_path}")
    return metadata


def video_stream(metadata: dict[str, Any]) -> dict[str, Any] | None:
    for stream in metadata.get("streams", []):
        if stream.get("codec_type") == "video":
            return stream
    return None


def has_audio(metadata: dict[str, Any]) -> bool:
    return any(stream.get("codec_type") == "audio" for stream in metadata.get("streams", []))


def output_dir_for(input_path: Path, output_dir_arg: str | None) -> Path:
    if output_dir_arg:
        return Path(output_dir_arg).expanduser().resolve()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return DEFAULT_OUTPUT_ROOT / f"{sanitize_stem(input_path)}-{timestamp}"


def build_filter_chain(args: argparse.Namespace, logger: JsonlLogger) -> str:
    filters: list[str] = []

    if args.brightness != 0.0 or args.contrast != 1.0:
        filters.append(f"eq=brightness={args.brightness}:contrast={args.contrast}")

    if args.denoise == "hqdn3d":
        strength = max(args.denoise_strength, 0.0)
        filters.append(
            "hqdn3d="
            f"{1.5 * strength:.3f}:"
            f"{1.5 * strength:.3f}:"
            f"{6.0 * strength:.3f}:"
            f"{6.0 * strength:.3f}"
        )
    elif args.denoise == "nlmeans":
        strength = max(args.denoise_strength, 0.1)
        filters.append(f"nlmeans=s={strength:.3f}:p=7:r=15")

    if args.stabilize:
        filters.append("deshake")
        logger.event(
            "stabilization_notice",
            "info",
            message="FFmpeg deshake is enabled; it may crop or warp geometry and should be treated as a viewing aid.",
        )

    if args.scale != 1.0:
        filters.append(scale_filter(args.scale))

    if args.sharpen > 0.0:
        amount = min(max(args.sharpen, 0.0), 2.0)
        filters.append(f"unsharp=5:5:{amount:.3f}:5:5:0.0")

    filters.append("format=yuv420p")
    chain = ",".join(filters)
    logger.event("filter_chain", "selected", filter_chain=chain)
    return chain


def scale_filter(scale: float) -> str:
    scale = max(scale, 0.1)
    return f"scale=trunc(iw*{scale}/2)*2:trunc(ih*{scale}/2)*2:flags=lanczos"


def extract_frames(input_path: Path, frames_dir: Path, logger: JsonlLogger) -> int:
    ffmpeg_bin = command_path("ffmpeg")
    frames_dir.mkdir(parents=True, exist_ok=True)
    output_pattern = frames_dir / "frame_%06d.jpg"
    run_command(
        [
            ffmpeg_bin,
            "-y",
            "-i",
            str(input_path),
            "-map",
            "0:v:0",
            "-vsync",
            "0",
            "-q:v",
            "2",
            str(output_pattern),
        ],
        logger,
        "extract_frames",
        timeout=900,
    )
    count = len(list(frames_dir.glob("frame_*.jpg")))
    logger.event("extract_frames", "counted", frame_count=count, frames_dir=str(frames_dir))
    if count == 0:
        raise ProcessingError("FFmpeg frame extraction produced no frames.")
    return count


def maybe_ai_upscale(
    args: argparse.Namespace,
    input_path: Path,
    frames_dir: Path,
    tmp_dir: Path,
    output_dir: Path,
    metadata: dict[str, Any],
    logger: JsonlLogger,
) -> Path:
    if not args.ai_upscale:
        logger.event("ai_upscale", "skipped", reason="--ai-upscale was not requested")
        return input_path

    realesrgan_bin = shutil.which("realesrgan-ncnn-vulkan")
    if not realesrgan_bin:
        logger.event("ai_upscale", "skipped", reason="realesrgan-ncnn-vulkan is not installed or not on PATH")
        return input_path

    stream = video_stream(metadata) or {}
    fps = format_rate(parse_rate(stream.get("avg_frame_rate") or stream.get("r_frame_rate")))
    upscaled_frames_dir = tmp_dir / "ai_upscaled_frames"
    upscaled_frames_dir.mkdir(parents=True, exist_ok=True)
    run_command(
        [
            realesrgan_bin,
            "-i",
            str(frames_dir),
            "-o",
            str(upscaled_frames_dir),
            "-n",
            "realesrgan-x4plus",
        ],
        logger,
        "ai_upscale_realesrgan",
        timeout=None,
    )

    frame_files = sorted(path for path in upscaled_frames_dir.iterdir() if path.suffix.lower() in IMAGE_SUFFIXES)
    if not frame_files:
        logger.event("ai_upscale", "failed", reason="Real-ESRGAN produced no image frames; falling back to original input.")
        return input_path

    extension = frame_files[0].suffix.lower()
    glob_pattern = str(upscaled_frames_dir / f"*{extension}")
    ai_source = output_dir / "ai-upscaled-source.mp4"
    ffmpeg_bin = command_path("ffmpeg")
    run_command(
        [
            ffmpeg_bin,
            "-y",
            "-framerate",
            fps,
            "-pattern_type",
            "glob",
            "-i",
            glob_pattern,
            "-i",
            str(input_path),
            "-map",
            "0:v:0",
            "-map",
            "1:a?",
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "18",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-shortest",
            "-movflags",
            "+faststart",
            str(ai_source),
        ],
        logger,
        "encode_ai_upscaled_source",
        timeout=None,
    )
    logger.event("ai_upscale", "completed", output=str(ai_source))
    return ai_source


def encode_filtered(
    source_path: Path,
    output_path: Path,
    filter_chain: str,
    logger: JsonlLogger,
    step: str,
    crf: str = "18",
) -> None:
    ffmpeg_bin = command_path("ffmpeg")
    run_command(
        [
            ffmpeg_bin,
            "-y",
            "-i",
            str(source_path),
            "-map",
            "0:v:0",
            "-map",
            "0:a?",
            "-vf",
            filter_chain,
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            crf,
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-movflags",
            "+faststart",
            str(output_path),
        ],
        logger,
        step,
        timeout=None,
    )


def encode_enhanced(source_path: Path, output_path: Path, filter_chain: str, logger: JsonlLogger) -> None:
    encode_filtered(source_path, output_path, filter_chain, logger, "encode_enhanced")


def create_comparison(original_path: Path, enhanced_path: Path, comparison_path: Path, logger: JsonlLogger) -> None:
    enhanced_metadata = ffprobe(enhanced_path, logger)
    stream = video_stream(enhanced_metadata) or {}
    target_height = int(stream.get("height") or 720)
    ffmpeg_bin = command_path("ffmpeg")
    filter_complex = (
        f"[0:v]scale=-2:{target_height},setsar=1[left];"
        f"[1:v]scale=-2:{target_height},setsar=1[right];"
        "[left][right]hstack=inputs=2[v]"
    )
    logger.event("comparison_filter_chain", "selected", filter_complex=filter_complex)
    run_command(
        [
            ffmpeg_bin,
            "-y",
            "-i",
            str(original_path),
            "-i",
            str(enhanced_path),
            "-filter_complex",
            filter_complex,
            "-map",
            "[v]",
            "-map",
            "0:a?",
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "18",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-shortest",
            "-movflags",
            "+faststart",
            str(comparison_path),
        ],
        logger,
        "encode_comparison",
        timeout=None,
    )


def atempo_chain(factor: float) -> str:
    tempo = 1.0 / factor
    parts: list[float] = []
    while tempo < 0.5:
        parts.append(0.5)
        tempo /= 0.5
    while tempo > 2.0:
        parts.append(2.0)
        tempo /= 2.0
    parts.append(tempo)
    return ",".join(f"atempo={part:.6g}" for part in parts)


def create_slowmo(enhanced_path: Path, slowmo_path: Path, factor: float, logger: JsonlLogger, step: str = "encode_slow_motion") -> None:
    if factor <= 1.0:
        logger.event("slow_motion", "skipped", reason="--slowmo-factor must be greater than 1 to export slow motion")
        return

    metadata = ffprobe(enhanced_path, logger)
    ffmpeg_bin = command_path("ffmpeg")
    if has_audio(metadata):
        tempo_filters = atempo_chain(factor)
        filter_complex = f"[0:v]setpts={factor}*PTS[v];[0:a]{tempo_filters}[a]"
        logger.event("slow_motion_filter_chain", "selected", filter_complex=filter_complex, factor=factor)
        args = [
            ffmpeg_bin,
            "-y",
            "-i",
            str(enhanced_path),
            "-filter_complex",
            filter_complex,
            "-map",
            "[v]",
            "-map",
            "[a]",
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "18",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-movflags",
            "+faststart",
            str(slowmo_path),
        ]
    else:
        filter_chain = f"setpts={factor}*PTS,format=yuv420p"
        logger.event("slow_motion_filter_chain", "selected", filter_chain=filter_chain, factor=factor)
        args = [
            ffmpeg_bin,
            "-y",
            "-i",
            str(enhanced_path),
            "-vf",
            filter_chain,
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "18",
            "-movflags",
            "+faststart",
            str(slowmo_path),
        ]
    run_command(args, logger, step, timeout=None)


def parse_roi(roi_text: str | None, metadata: dict[str, Any], logger: JsonlLogger) -> tuple[int, int, int, int] | None:
    if not roi_text:
        return None
    pieces = [piece.strip() for piece in roi_text.split(",")]
    if len(pieces) != 4:
        raise ProcessingError("--roi must use x,y,w,h")
    try:
        x, y, width, height = [int(piece) for piece in pieces]
    except ValueError as exc:
        raise ProcessingError("--roi values must be integers") from exc
    stream = video_stream(metadata) or {}
    source_width = int(stream.get("width") or 0)
    source_height = int(stream.get("height") or 0)
    if width <= 0 or height <= 0:
        raise ProcessingError("--roi width and height must be positive")
    if x < 0 or y < 0 or x + width > source_width or y + height > source_height:
        raise ProcessingError(f"--roi is outside the source bounds {source_width}x{source_height}")
    x -= x % 2
    y -= y % 2
    width -= width % 2
    height -= height % 2
    logger.event("roi", "selected", x=x, y=y, width=width, height=height)
    return x, y, width, height


def variant_profiles(quality_tier: str = "standard") -> dict[str, str]:
    profiles = {
        "conservative": ",".join(
            [
                "eq=brightness=0.02:contrast=1.10",
                "hqdn3d=0.750:0.750:3.000:3.000",
                "cas=strength=0.35",
                "format=yuv420p",
            ]
        ),
        "detail": ",".join(
            [
                "eq=brightness=0.035:contrast=1.25",
                "normalize=smoothing=8:strength=0.25",
                "atadenoise=s=9",
                scale_filter(1.5),
                "cas=strength=0.55",
                "unsharp=5:5:0.650:5:5:0.0",
                "format=yuv420p",
            ]
        ),
        "motion": ",".join(
            [
                "eq=brightness=0.025:contrast=1.15",
                "hqdn3d=1.000:1.000:4.000:4.000",
                "cas=strength=0.40",
                "minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:me=epzs",
                "format=yuv420p",
            ]
        ),
    }
    if quality_tier == "premium":
        profiles.update(
            {
                "restore-clean": ",".join(
                    [
                        "eq=brightness=0.025:contrast=1.18",
                        "normalize=smoothing=12:strength=0.30",
                        "deblock=filter=strong:block=8:alpha=0.098:beta=0.05:gamma=0.05:delta=0.05",
                        "fftdnoiz=sigma=1.6:amount=0.65:block=32:overlap=0.5:prev=1:next=1",
                        "vaguedenoiser=threshold=1.2:method=garrote:nsteps=6:percent=55",
                        scale_filter(2.0),
                        "cas=strength=0.45",
                        "unsharp=7:7:0.420:3:3:0.0",
                        "format=yuv420p",
                    ]
                ),
                "restore-sharp": ",".join(
                    [
                        "eq=brightness=0.02:contrast=1.28",
                        "atadenoise=s=7",
                        "deblock=filter=weak:block=8:alpha=0.075:beta=0.035:gamma=0.035:delta=0.035",
                        scale_filter(1.75),
                        "cas=strength=0.75",
                        "unsharp=5:5:0.900:3:3:0.0",
                        "format=yuv420p",
                    ]
                ),
                "edge-map": ",".join(
                    [
                        scale_filter(1.5),
                        "format=gray",
                        "eq=contrast=1.45",
                        "edgedetect=mode=wires:low=0.05:high=0.18",
                        "format=yuv420p",
                    ]
                ),
            }
        )
    return profiles


def roi_filter(roi: tuple[int, int, int, int], premium: bool = False) -> str:
    x, y, width, height = roi
    if premium:
        return ",".join(
            [
                f"crop={width}:{height}:{x}:{y}",
                "eq=brightness=0.025:contrast=1.22",
                "normalize=smoothing=12:strength=0.30",
                "deblock=filter=strong:block=8:alpha=0.098:beta=0.05:gamma=0.05:delta=0.05",
                "fftdnoiz=sigma=1.4:amount=0.60:block=32:overlap=0.5:prev=1:next=1",
                "vaguedenoiser=threshold=1.0:method=garrote:nsteps=6:percent=50",
                "scale=trunc(iw*2/2)*2:trunc(ih*2/2)*2:flags=lanczos",
                "cas=strength=0.55",
                "unsharp=7:7:0.520:3:3:0.0",
                "format=yuv420p",
            ]
        )
    return ",".join(
        [
            f"crop={width}:{height}:{x}:{y}",
            "eq=brightness=0.035:contrast=1.25",
            "normalize=smoothing=8:strength=0.25",
            "atadenoise=s=9",
            "scale=trunc(iw*3/2)*2:trunc(ih*3/2)*2:flags=lanczos",
            "cas=strength=0.55",
            "unsharp=5:5:0.650:5:5:0.0",
            "format=yuv420p",
        ]
    )


def detect_audio_focus(
    input_path: Path,
    metadata: dict[str, Any],
    tmp_dir: Path,
    logger: JsonlLogger,
    sample_rate: int = 8000,
    window_seconds: float = 0.12,
    hop_seconds: float = 0.03,
    search_start: float | None = None,
    search_end: float | None = None,
) -> dict[str, Any]:
    duration = duration_seconds(metadata)
    if not has_audio(metadata):
        fallback = max(duration / 2.0, 0.0)
        logger.event("audio_focus", "fallback", reason="input has no audio stream", focus_time=fallback)
        return {"focus_time": fallback, "source": "midpoint_fallback", "rms": None}

    pcm_path = tmp_dir / "focus-audio.s16le"
    ffmpeg_bin = command_path("ffmpeg")
    run_command(
        [
            ffmpeg_bin,
            "-y",
            "-i",
            str(input_path),
            "-vn",
            "-map",
            "0:a:0",
            "-ac",
            "1",
            "-ar",
            str(sample_rate),
            "-f",
            "s16le",
            str(pcm_path),
        ],
        logger,
        "extract_audio_for_focus",
        timeout=180,
    )

    raw = pcm_path.read_bytes()
    if not raw:
        fallback = max(duration / 2.0, 0.0)
        logger.event("audio_focus", "fallback", reason="extracted audio was empty", focus_time=fallback)
        return {"focus_time": fallback, "source": "midpoint_fallback", "rms": None}

    samples = array.array("h")
    samples.frombytes(raw)
    if sys.byteorder != "little":
        samples.byteswap()
    if not samples:
        fallback = max(duration / 2.0, 0.0)
        logger.event("audio_focus", "fallback", reason="decoded sample array was empty", focus_time=fallback)
        return {"focus_time": fallback, "source": "midpoint_fallback", "rms": None}

    window = max(1, int(sample_rate * window_seconds))
    hop = max(1, int(sample_rate * hop_seconds))
    bounded_start = max(float(search_start or 0.0), 0.0)
    bounded_end = float(search_end) if search_end is not None else (duration if duration else len(samples) / sample_rate)
    if duration:
        bounded_end = min(bounded_end, duration)
    bounded_end = max(bounded_end, bounded_start)
    sample_start = min(len(samples), max(0, int(bounded_start * sample_rate)))
    sample_end = min(len(samples), max(sample_start, int(bounded_end * sample_rate)))
    logger.event(
        "audio_focus_search_window",
        "selected",
        start_seconds=round(bounded_start, 3),
        end_seconds=round(bounded_end, 3),
        sample_start=sample_start,
        sample_end=sample_end,
    )
    if sample_end - sample_start < window:
        fallback = min(duration, bounded_start + window_seconds / 2.0) if duration else bounded_start
        logger.event(
            "audio_focus",
            "fallback",
            reason="focus search window is shorter than the RMS analysis window",
            focus_time=round(fallback, 3),
        )
        return {
            "focus_time": round(fallback, 3),
            "source": "bounded_window_fallback",
            "rms": None,
            "search_start_seconds": round(bounded_start, 3),
            "search_end_seconds": round(bounded_end, 3),
        }

    best_start = sample_start
    best_rms = -1.0
    stop = max(sample_start + 1, sample_end - window + 1)
    for start in range(sample_start, stop, hop):
        chunk = samples[start : start + window]
        if not chunk:
            continue
        rms = math.sqrt(sum(sample * sample for sample in chunk) / len(chunk))
        if rms > best_rms:
            best_rms = rms
            best_start = start

    focus_time = min(duration, (best_start + window / 2.0) / sample_rate) if duration else (best_start + window / 2.0) / sample_rate
    result = {
        "focus_time": round(focus_time, 3),
        "source": "auto_focus_audio",
        "rms": round(best_rms, 3),
        "window_seconds": window_seconds,
        "hop_seconds": hop_seconds,
        "sample_rate": sample_rate,
        "search_start_seconds": round(bounded_start, 3),
        "search_end_seconds": round(bounded_end, 3),
    }
    logger.event("audio_focus", "detected", **result)
    return result


def focus_range(focus_time: float, focus_window: float, duration: float) -> tuple[float, float]:
    window = max(focus_window, 0.5)
    start = max(0.0, focus_time - window / 2.0)
    if duration > 0 and start + window > duration:
        start = max(0.0, duration - window)
    actual_duration = min(window, duration - start) if duration > 0 else window
    return round(start, 3), round(max(actual_duration, 0.5), 3)


def trim_clip(source_path: Path, output_path: Path, start: float, duration: float, logger: JsonlLogger, step: str) -> None:
    ffmpeg_bin = command_path("ffmpeg")
    run_command(
        [
            ffmpeg_bin,
            "-y",
            "-ss",
            f"{start:.3f}",
            "-t",
            f"{duration:.3f}",
            "-i",
            str(source_path),
            "-map",
            "0:v:0",
            "-map",
            "0:a?",
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "18",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-movflags",
            "+faststart",
            str(output_path),
        ],
        logger,
        step,
        timeout=None,
    )


def create_grid_comparison(
    entries: list[dict[str, Any]],
    output_path: Path,
    logger: JsonlLogger,
    step: str,
    tile_width: int = 640,
    tile_height: int = 360,
) -> None:
    if len(entries) < 4:
        raise ProcessingError("Grid comparison needs at least four entries.")
    selected = entries[:4]
    ffmpeg_bin = command_path("ffmpeg")
    inputs: list[str] = []
    for entry in selected:
        inputs.extend(["-i", str(entry["path"])])
    scaled = []
    for index in range(4):
        scaled.append(
            f"[{index}:v]scale={tile_width}:{tile_height}:force_original_aspect_ratio=decrease,"
            f"pad={tile_width}:{tile_height}:(ow-iw)/2:(oh-ih)/2,setsar=1[v{index}]"
        )
    filter_complex = ";".join(
        scaled
        + [
            "[v0][v1]hstack=inputs=2[top]",
            "[v2][v3]hstack=inputs=2[bottom]",
            "[top][bottom]vstack=inputs=2[v]",
        ]
    )
    logger.event(
        f"{step}_filter_chain",
        "selected",
        filter_complex=filter_complex,
        layout=[entry["name"] for entry in selected],
    )
    run_command(
        [
            ffmpeg_bin,
            "-y",
            *inputs,
            "-filter_complex",
            filter_complex,
            "-map",
            "[v]",
            "-map",
            "0:a?",
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "18",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-shortest",
            "-movflags",
            "+faststart",
            str(output_path),
        ],
        logger,
        step,
        timeout=None,
    )


FONT_5X7 = {
    "0": ["111", "101", "101", "101", "101", "101", "111"],
    "1": ["010", "110", "010", "010", "010", "010", "111"],
    "2": ["111", "001", "001", "111", "100", "100", "111"],
    "3": ["111", "001", "001", "111", "001", "001", "111"],
    "4": ["101", "101", "101", "111", "001", "001", "001"],
    "5": ["111", "100", "100", "111", "001", "001", "111"],
    "6": ["111", "100", "100", "111", "101", "101", "111"],
    "7": ["111", "001", "001", "010", "010", "010", "010"],
    "8": ["111", "101", "101", "111", "101", "101", "111"],
    "9": ["111", "101", "101", "111", "001", "001", "111"],
    ":": ["0", "1", "1", "0", "1", "1", "0"],
    ".": ["0", "0", "0", "0", "0", "1", "1"],
    "s": ["111", "100", "100", "111", "001", "001", "111"],
    "-": ["0", "0", "0", "1", "0", "0", "0"],
}


def read_ppm(path: Path) -> tuple[int, int, bytearray]:
    data = path.read_bytes()
    offset = 0

    def next_token() -> bytes:
        nonlocal offset
        while offset < len(data) and data[offset] in b" \t\r\n":
            offset += 1
        if offset < len(data) and data[offset] == ord("#"):
            while offset < len(data) and data[offset] not in b"\r\n":
                offset += 1
            return next_token()
        start = offset
        while offset < len(data) and data[offset] not in b" \t\r\n":
            offset += 1
        return data[start:offset]

    magic = next_token()
    if magic != b"P6":
        raise ProcessingError(f"Unsupported PPM format in {path}")
    width = int(next_token())
    height = int(next_token())
    max_value = int(next_token())
    if max_value != 255:
        raise ProcessingError(f"Unsupported PPM max value in {path}: {max_value}")
    while offset < len(data) and data[offset] in b" \t\r\n":
        offset += 1
    return width, height, bytearray(data[offset:])


def write_ppm(path: Path, width: int, height: int, pixels: bytearray) -> None:
    path.write_bytes(f"P6\n{width} {height}\n255\n".encode("ascii") + bytes(pixels))


def set_pixel(pixels: bytearray, width: int, height: int, x: int, y: int, color: tuple[int, int, int]) -> None:
    if x < 0 or y < 0 or x >= width or y >= height:
        return
    index = (y * width + x) * 3
    pixels[index : index + 3] = bytes(color)


def fill_rect(
    pixels: bytearray,
    width: int,
    height: int,
    x: int,
    y: int,
    rect_width: int,
    rect_height: int,
    color: tuple[int, int, int],
) -> None:
    for yy in range(y, y + rect_height):
        for xx in range(x, x + rect_width):
            set_pixel(pixels, width, height, xx, yy, color)


def draw_text(
    pixels: bytearray,
    width: int,
    height: int,
    x: int,
    y: int,
    text: str,
    color: tuple[int, int, int] = (255, 255, 255),
    scale: int = 2,
) -> None:
    cursor = x
    for char in text:
        glyph = FONT_5X7.get(char.lower())
        if glyph is None:
            cursor += 4 * scale
            continue
        for gy, row in enumerate(glyph):
            for gx, value in enumerate(row):
                if value == "1":
                    fill_rect(pixels, width, height, cursor + gx * scale, y + gy * scale, scale, scale, color)
        cursor += (len(glyph[0]) + 1) * scale


def copy_tile(
    source_pixels: bytearray,
    source_width: int,
    source_height: int,
    dest_pixels: bytearray,
    dest_width: int,
    dest_height: int,
    x: int,
    y: int,
) -> None:
    for row in range(source_height):
        dest_y = y + row
        if dest_y >= dest_height:
            break
        source_start = row * source_width * 3
        source_end = source_start + source_width * 3
        dest_start = (dest_y * dest_width + x) * 3
        dest_end = dest_start + source_width * 3
        dest_pixels[dest_start:dest_end] = source_pixels[source_start:source_end]


def timestamp_label(seconds: float) -> str:
    minutes, secs = divmod(max(seconds, 0.0), 60.0)
    return f"{int(minutes):02d}:{secs:05.2f}s"


def create_contact_sheet(
    source_path: Path,
    output_path: Path,
    focus_time: float,
    focus_window: float,
    duration: float,
    tmp_dir: Path,
    logger: JsonlLogger,
) -> None:
    ffmpeg_bin = command_path("ffmpeg")
    frames_dir = tmp_dir / "contact-sheet-frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    start, window = focus_range(focus_time, focus_window, duration)
    frame_total = CONTACT_SHEET_COLUMNS * CONTACT_SHEET_ROWS
    if frame_total == 1:
        times = [focus_time]
    else:
        step = window / (frame_total - 1)
        times = [min(duration, start + index * step) if duration else start + index * step for index in range(frame_total)]

    frame_paths: list[Path] = []
    actual_times: list[float] = []
    for index, second in enumerate(times):
        frame_path = frames_dir / f"frame_{index:02d}.ppm"
        attempt_second = min(second, max(0.0, duration - 0.1)) if duration else second
        for attempt in range(8):
            if frame_path.exists():
                frame_path.unlink()
            result = run_command(
                [
                    ffmpeg_bin,
                    "-y",
                    "-ss",
                    f"{attempt_second:.3f}",
                    "-i",
                    str(source_path),
                    "-frames:v",
                    "1",
                    "-vf",
                    f"scale={CONTACT_SHEET_TILE_WIDTH}:-2:flags=lanczos",
                    "-f",
                    "image2",
                    "-update",
                    "1",
                    "-vcodec",
                    "ppm",
                    str(frame_path),
                ],
                logger,
                "extract_contact_sheet_frame",
                timeout=60,
                required=False,
            )
            if result.returncode == 0 and frame_path.exists() and frame_path.stat().st_size > 0:
                actual_times.append(round(attempt_second, 3))
                break
            logger.event(
                "extract_contact_sheet_frame",
                "retry",
                requested_second=round(second, 3),
                attempted_second=round(attempt_second, 3),
                attempt=attempt + 1,
            )
            attempt_second = max(0.0, attempt_second - 0.25)
        if not frame_path.exists() or frame_path.stat().st_size == 0:
            if frame_paths:
                shutil.copyfile(frame_paths[-1], frame_path)
                fallback_second = actual_times[-1]
                actual_times.append(fallback_second)
                logger.event(
                    "extract_contact_sheet_frame",
                    "fallback_copy",
                    requested_second=round(second, 3),
                    fallback_second=fallback_second,
                )
            else:
                raise ProcessingError(f"Could not extract first contact-sheet frame near {second:.3f}s")
        frame_paths.append(frame_path)

    loaded = [read_ppm(path) for path in frame_paths]
    tile_width, tile_height, _ = loaded[0]
    sheet_width = CONTACT_SHEET_COLUMNS * tile_width + (CONTACT_SHEET_COLUMNS + 1) * CONTACT_SHEET_PADDING
    sheet_height = CONTACT_SHEET_ROWS * tile_height + (CONTACT_SHEET_ROWS + 1) * CONTACT_SHEET_PADDING
    sheet_pixels = bytearray([22, 22, 22] * sheet_width * sheet_height)

    for index, (width, height, pixels) in enumerate(loaded):
        col = index % CONTACT_SHEET_COLUMNS
        row = index // CONTACT_SHEET_COLUMNS
        x = CONTACT_SHEET_PADDING + col * (tile_width + CONTACT_SHEET_PADDING)
        y = CONTACT_SHEET_PADDING + row * (tile_height + CONTACT_SHEET_PADDING)
        copy_tile(pixels, width, height, sheet_pixels, sheet_width, sheet_height, x, y)
        fill_rect(sheet_pixels, sheet_width, sheet_height, x + 6, y + 6, 98, 22, (0, 0, 0))
        draw_text(sheet_pixels, sheet_width, sheet_height, x + 12, y + 10, timestamp_label(actual_times[index]), scale=2)

    ppm_sheet = tmp_dir / "contact-sheet.ppm"
    write_ppm(ppm_sheet, sheet_width, sheet_height, sheet_pixels)
    run_command(
        [
            ffmpeg_bin,
            "-y",
            "-i",
            str(ppm_sheet),
            "-q:v",
            "2",
            str(output_path),
        ],
        logger,
        "encode_contact_sheet",
        timeout=60,
    )
    logger.event("contact_sheet", "completed", output=str(output_path), frame_times=actual_times)


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def write_summary(
    summary_path: Path,
    input_path: Path,
    original_sha: str,
    original_size: int,
    metadata: dict[str, Any],
    frame_count: int,
    filter_chain: str,
    output_paths: dict[str, Path | None],
    args: argparse.Namespace,
) -> None:
    stream = video_stream(metadata) or {}
    duration = (metadata.get("format") or {}).get("duration", "unknown")
    lines = [
        "# Video Enhancement Processing Summary",
        "",
        f"**Disclaimer:** {DISCLAIMER}",
        "",
        "## Source",
        f"- Input: `{input_path}`",
        f"- SHA-256 before processing: `{original_sha}`",
        f"- Size before processing: `{original_size}` bytes",
        f"- Duration: `{duration}` seconds",
        f"- Video: `{stream.get('width', 'unknown')}x{stream.get('height', 'unknown')}` at `{stream.get('avg_frame_rate') or stream.get('r_frame_rate') or 'unknown'}` fps",
        "",
        "## Outputs",
        f"- Enhanced video: `{output_paths['enhanced']}`",
        f"- Side-by-side comparison: `{output_paths['comparison']}`",
    ]
    if output_paths.get("slowmo"):
        lines.append(f"- Slow-motion export: `{output_paths['slowmo']}`")
    if output_paths.get("ai_source"):
        lines.append(f"- AI-upscaled intermediate: `{output_paths['ai_source']}`")
    lines.extend(
        [
            "",
            "## Processing Settings",
            f"- Extracted frames: `{frame_count}`",
            f"- Brightness: `{args.brightness}`",
            f"- Contrast: `{args.contrast}`",
            f"- Denoise: `{args.denoise}`",
            f"- Denoise strength: `{args.denoise_strength}`",
            f"- Sharpen: `{args.sharpen}`",
            f"- Scale: `{args.scale}`",
            f"- Stabilization: `{args.stabilize}`",
            f"- AI upscaling requested: `{args.ai_upscale}`",
            f"- Slow-motion factor: `{args.slowmo_factor}`",
            "",
            "## FFmpeg Filter Chain",
            f"`{filter_chain}`",
            "",
            "## Interpretation Boundary",
            "Use these outputs to inspect the clip more comfortably. Do not treat them as proof that any person or object made contact with glass, caused damage, or is responsible for the shattering.",
        ]
    )
    summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_variant_summary(summary_path: Path, manifest: dict[str, Any]) -> None:
    lines = [
        "# Video Enhancement Variant Pack Summary",
        "",
        f"**Disclaimer:** {DISCLAIMER}",
        "",
        "## Quality Tier",
        f"- Tier: `{manifest.get('quality_tier', 'standard')}`",
    ]
    if manifest.get("quality_note"):
        lines.append(f"- Note: {manifest['quality_note']}")
    if manifest.get("capabilities"):
        lines.extend(["", "## Local Capability Checks"])
        for name, payload in manifest["capabilities"].items():
            status = "available" if payload.get("available") else "unavailable"
            path = payload.get("path") or "not found"
            lines.append(f"- {name}: `{status}` ({path})")
    lines.extend(
        [
            "",
            "## Focus",
            f"- Focus time: `{manifest['focus']['focus_time']}` seconds",
            f"- Focus source: `{manifest['focus']['source']}`",
            f"- Focus window: `{manifest['focus']['window_seconds']}` seconds",
        ]
    )
    if manifest["focus"].get("search_start_seconds") is not None:
        lines.append(
            f"- Focus search bounds: `{manifest['focus']['search_start_seconds']}` to `{manifest['focus']['search_end_seconds']}` seconds"
        )
    lines.extend(
        [
            "",
            "## Outputs",
        ]
    )
    for output in manifest["outputs"]:
        lines.append(f"- {output['name']}: `{output['path']}`")
    lines.extend(
        [
            "",
            "## Interpretation Boundary",
            "The variants are different viewing treatments of the same source. They are not independent evidence and do not prove contact, fault, causation, or responsibility.",
        ]
    )
    summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def cleanup_tmp(tmp_dir: Path, keep_frames: bool, logger: JsonlLogger) -> None:
    if keep_frames:
        logger.event("cleanup", "skipped", reason="--keep-frames was requested", tmp_dir=str(tmp_dir))
        return
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
    logger.event("cleanup", "completed", removed_tmp_dir=str(tmp_dir))


def verify_source_preserved(input_path: Path, original_sha: str, original_size: int, logger: JsonlLogger) -> None:
    after_sha = file_sha256(input_path)
    after_size = input_path.stat().st_size
    preserved = after_sha == original_sha and after_size == original_size
    logger.event("source_integrity", "verified", preserved=preserved, sha256_after=after_sha, size_after=after_size)
    if not preserved:
        raise ProcessingError("Original input changed during processing; aborting.")


def run_single_output(
    args: argparse.Namespace,
    input_path: Path,
    output_dir: Path,
    tmp_dir: Path,
    frames_dir: Path,
    metadata: dict[str, Any],
    frame_count: int,
    original_sha: str,
    original_size: int,
    logger: JsonlLogger,
) -> list[Path]:
    source_for_enhancement = maybe_ai_upscale(args, input_path, frames_dir, tmp_dir, output_dir, metadata, logger)
    filter_chain = build_filter_chain(args, logger)

    enhanced_path = output_dir / "enhanced.mp4"
    comparison_path = output_dir / "comparison.mp4"
    slowmo_path = output_dir / "enhanced-slowmo.mp4" if args.slowmo_factor > 1.0 else None

    encode_enhanced(source_for_enhancement, enhanced_path, filter_chain, logger)
    create_comparison(input_path, enhanced_path, comparison_path, logger)
    if slowmo_path:
        create_slowmo(enhanced_path, slowmo_path, args.slowmo_factor, logger)

    verify_source_preserved(input_path, original_sha, original_size, logger)
    summary_path = output_dir / "processing-summary.md"
    write_summary(
        summary_path,
        input_path,
        original_sha,
        original_size,
        metadata,
        frame_count,
        filter_chain,
        {
            "enhanced": enhanced_path,
            "comparison": comparison_path,
            "slowmo": slowmo_path,
            "ai_source": source_for_enhancement if source_for_enhancement != input_path else None,
        },
        args,
    )
    logger.event("summary", "written", path=str(summary_path))

    outputs = [enhanced_path, comparison_path, summary_path, output_dir / "processing-log.jsonl"]
    if slowmo_path:
        outputs.append(slowmo_path)
    return outputs


def run_variant_pack(
    args: argparse.Namespace,
    input_path: Path,
    output_dir: Path,
    tmp_dir: Path,
    frames_dir: Path,
    metadata: dict[str, Any],
    frame_count: int,
    original_sha: str,
    original_size: int,
    logger: JsonlLogger,
    capabilities: dict[str, Any],
) -> list[Path]:
    source_for_enhancement = maybe_ai_upscale(args, input_path, frames_dir, tmp_dir, output_dir, metadata, logger)
    roi = parse_roi(args.roi, metadata, logger)

    variants: list[dict[str, Any]] = []
    logger.event("quality_tier", "selected", tier=args.quality_tier, topaz_like=args.topaz_like)
    if args.quality_tier == "premium":
        logger.event("quality_tier_notice", "info", message=PREMIUM_TIER_NOTE)

    for name, filter_chain in variant_profiles(args.quality_tier).items():
        output_path = output_dir / f"{name}.mp4"
        logger.event("variant_filter_chain", "selected", variant=name, filter_chain=filter_chain)
        encode_filtered(source_for_enhancement, output_path, filter_chain, logger, f"encode_variant_{name}")
        variants.append({"name": name, "path": output_path, "filter_chain": filter_chain, "kind": "variant"})

    motion_path = next(entry["path"] for entry in variants if entry["name"] == "motion")
    motion_slowmo_2x = output_dir / "motion-slowmo-2x.mp4"
    motion_slowmo_4x = output_dir / "motion-slowmo-4x.mp4"
    create_slowmo(motion_path, motion_slowmo_2x, max(args.slowmo_factor, 2.0), logger, "encode_motion_slowmo_2x")
    create_slowmo(motion_path, motion_slowmo_4x, 4.0, logger, "encode_motion_slowmo_4x")
    variants.extend(
        [
            {"name": "motion-slowmo-2x", "path": motion_slowmo_2x, "filter_chain": f"setpts={max(args.slowmo_factor, 2.0)}*PTS", "kind": "slow_motion"},
            {"name": "motion-slowmo-4x", "path": motion_slowmo_4x, "filter_chain": "setpts=4.0*PTS", "kind": "slow_motion"},
        ]
    )

    if roi:
        roi_path = output_dir / "roi-zoom.mp4"
        roi_chain = roi_filter(roi)
        logger.event("variant_filter_chain", "selected", variant="roi", filter_chain=roi_chain)
        encode_filtered(source_for_enhancement, roi_path, roi_chain, logger, "encode_variant_roi")
        variants.append({"name": "roi", "path": roi_path, "filter_chain": roi_chain, "kind": "roi", "roi": roi})
        if args.quality_tier == "premium":
            roi_premium_path = output_dir / "roi-premium.mp4"
            roi_premium_chain = roi_filter(roi, premium=True)
            logger.event("variant_filter_chain", "selected", variant="roi-premium", filter_chain=roi_premium_chain)
            encode_filtered(source_for_enhancement, roi_premium_path, roi_premium_chain, logger, "encode_variant_roi_premium")
            variants.append(
                {
                    "name": "roi-premium",
                    "path": roi_premium_path,
                    "filter_chain": roi_premium_chain,
                    "kind": "roi",
                    "roi": roi,
                }
            )

    focus_detection: dict[str, Any]
    if args.focus_time is not None:
        focus_detection = {"focus_time": round(max(args.focus_time, 0.0), 3), "source": "manual_focus_time", "rms": None}
        logger.event("audio_focus", "manual", **focus_detection)
    elif args.auto_focus_audio:
        focus_detection = detect_audio_focus(
            input_path,
            metadata,
            tmp_dir,
            logger,
            search_start=args.focus_search_start,
            search_end=args.focus_search_end,
        )
    else:
        midpoint = max(duration_seconds(metadata) / 2.0, 0.0)
        focus_detection = {"focus_time": round(midpoint, 3), "source": "midpoint_no_auto_focus", "rms": None}
        logger.event("audio_focus", "fallback", **focus_detection)

    source_duration = duration_seconds(metadata)
    focus_start, focus_duration = focus_range(focus_detection["focus_time"], args.focus_window, source_duration)

    comparison_entries = [
        {"name": "original", "path": input_path},
        {"name": "conservative", "path": output_dir / "conservative.mp4"},
        {"name": "detail", "path": output_dir / "detail.mp4"},
        {"name": "motion", "path": output_dir / "motion.mp4"},
    ]
    if roi:
        comparison_entries[-1] = {"name": "roi", "path": output_dir / "roi-zoom.mp4"}

    variant_comparison = output_dir / "variant-comparison.mp4"
    create_grid_comparison(comparison_entries, variant_comparison, logger, "encode_variant_comparison")

    focus_entries: list[dict[str, Any]] = []
    for entry in comparison_entries:
        focus_path = output_dir / f"focus-{entry['name']}.mp4"
        trim_clip(entry["path"], focus_path, focus_start, focus_duration, logger, f"trim_focus_{entry['name']}")
        focus_entries.append({"name": f"focus-{entry['name']}", "path": focus_path})

    focus_comparison = output_dir / "focus-comparison.mp4"
    create_grid_comparison(focus_entries, focus_comparison, logger, "encode_focus_comparison")

    contact_sheet = output_dir / "contact-sheet.jpg"
    create_contact_sheet(output_dir / "detail.mp4", contact_sheet, focus_detection["focus_time"], args.focus_window, source_duration, tmp_dir, logger)

    premium_comparison: Path | None = None
    focus_premium_comparison: Path | None = None
    focus_premium_entries: list[dict[str, Any]] = []
    if args.quality_tier == "premium":
        premium_entries = [
            {"name": "original", "path": input_path},
            {"name": "detail", "path": output_dir / "detail.mp4"},
            {"name": "restore-clean", "path": output_dir / "restore-clean.mp4"},
            {"name": "roi-premium" if roi else "restore-sharp", "path": output_dir / ("roi-premium.mp4" if roi else "restore-sharp.mp4")},
        ]
        premium_comparison = output_dir / "premium-comparison.mp4"
        create_grid_comparison(premium_entries, premium_comparison, logger, "encode_premium_comparison")

        for entry in premium_entries:
            focus_path = output_dir / f"focus-premium-{entry['name']}.mp4"
            trim_clip(entry["path"], focus_path, focus_start, focus_duration, logger, f"trim_focus_premium_{entry['name']}")
            focus_premium_entries.append({"name": f"focus-premium-{entry['name']}", "path": focus_path})
        focus_premium_comparison = output_dir / "focus-premium-comparison.mp4"
        create_grid_comparison(focus_premium_entries, focus_premium_comparison, logger, "encode_focus_premium_comparison")

    outputs: list[dict[str, Any]] = [
        {"name": "variant-comparison", "path": str(variant_comparison), "kind": "comparison"},
        {"name": "focus-comparison", "path": str(focus_comparison), "kind": "comparison"},
        {"name": "contact-sheet", "path": str(contact_sheet), "kind": "contact_sheet"},
    ]
    if premium_comparison:
        outputs.append({"name": "premium-comparison", "path": str(premium_comparison), "kind": "comparison"})
    if focus_premium_comparison:
        outputs.append({"name": "focus-premium-comparison", "path": str(focus_premium_comparison), "kind": "comparison"})
    if roi:
        roi_contact_sheet_source = output_dir / ("roi-premium.mp4" if args.quality_tier == "premium" else "roi-zoom.mp4")
        roi_contact_sheet = output_dir / "contact-sheet-roi.jpg"
        create_contact_sheet(
            roi_contact_sheet_source,
            roi_contact_sheet,
            focus_detection["focus_time"],
            args.focus_window,
            source_duration,
            tmp_dir,
            logger,
        )
        outputs.append({"name": "contact-sheet-roi", "path": str(roi_contact_sheet), "kind": "contact_sheet"})
    for variant in variants:
        payload = {
            "name": variant["name"],
            "path": str(variant["path"]),
            "kind": variant["kind"],
            "filter_chain": variant["filter_chain"],
        }
        if "roi" in variant:
            payload["roi"] = variant["roi"]
        outputs.append(payload)
    for entry in focus_entries:
        outputs.append({"name": entry["name"], "path": str(entry["path"]), "kind": "focus_clip"})
    for entry in focus_premium_entries:
        outputs.append({"name": entry["name"], "path": str(entry["path"]), "kind": "focus_clip"})

    manifest = {
        "disclaimer": DISCLAIMER,
        "source": {
            "path": str(input_path),
            "sha256": original_sha,
            "size_bytes": original_size,
            "duration_seconds": source_duration,
            "frame_count_extracted": frame_count,
        },
        "focus": {
            **focus_detection,
            "start_seconds": focus_start,
            "duration_seconds": focus_duration,
            "window_seconds": args.focus_window,
        },
        "ai_upscale_requested": args.ai_upscale,
        "capabilities": capabilities,
        "quality_tier": args.quality_tier,
        "quality_note": PREMIUM_TIER_NOTE if args.quality_tier == "premium" else "Standard local FFmpeg inspection tier.",
        "topaz_like_shortcut": args.topaz_like,
        "outputs": outputs,
    }
    manifest_path = output_dir / "variant-manifest.json"
    write_json(manifest_path, manifest)
    logger.event("variant_manifest", "written", path=str(manifest_path))

    summary_path = output_dir / "processing-summary.md"
    write_variant_summary(summary_path, manifest)
    logger.event("summary", "written", path=str(summary_path))
    verify_source_preserved(input_path, original_sha, original_size, logger)

    return [
        variant_comparison,
        focus_comparison,
        contact_sheet,
        manifest_path,
        summary_path,
        output_dir / "processing-log.jsonl",
        *[Path(output["path"]) for output in outputs if output["kind"] not in {"comparison", "contact_sheet"}],
    ]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Enhance a video for easier viewing and produce transparent inspection outputs."
    )
    parser.add_argument("video_path", help="Path to one input video file. The original file is never modified.")
    parser.add_argument("--output-dir", help="Directory for enhanced outputs.")
    parser.add_argument("--brightness", type=float, default=0.03, help="FFmpeg eq brightness. Default: 0.03")
    parser.add_argument("--contrast", type=float, default=1.2, help="FFmpeg eq contrast. Default: 1.2")
    parser.add_argument("--denoise", choices=["off", "hqdn3d", "nlmeans"], default="hqdn3d")
    parser.add_argument("--denoise-strength", type=float, default=1.0)
    parser.add_argument("--sharpen", type=float, default=0.8, help="Unsharp amount, 0 disables sharpening. Default: 0.8")
    parser.add_argument("--scale", type=float, default=1.5, help="Lanczos scale factor. Default: 1.5")
    parser.add_argument("--stabilize", action="store_true", help="Enable FFmpeg deshake stabilization.")
    parser.add_argument("--slowmo-factor", type=float, default=2.0, help="Slow-motion factor. Default: 2.")
    parser.add_argument("--ai-upscale", action="store_true", help="Use Real-ESRGAN if realesrgan-ncnn-vulkan is installed.")
    parser.add_argument("--keep-frames", action="store_true", help="Keep extracted temporary frames.")
    parser.add_argument("--variant-pack", action="store_true", help="Produce a multi-variant inspection pack.")
    parser.add_argument(
        "--quality-tier",
        choices=["standard", "premium"],
        default="standard",
        help="Variant-pack quality tier. Premium adds heavier restoration views and ROI review artifacts.",
    )
    parser.add_argument(
        "--topaz-like",
        action="store_true",
        help="Shortcut for --variant-pack --quality-tier premium --ai-upscale with transparent local capability checks.",
    )
    parser.add_argument("--focus-time", type=float, help="Manual focus time in seconds for thud-window outputs.")
    parser.add_argument(
        "--auto-focus-audio",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Detect the strongest short-window audio spike for focus outputs. Default: enabled.",
    )
    parser.add_argument("--focus-search-start", type=float, default=0.0, help="Start second for bounded auto audio focus search. Default: 0.")
    parser.add_argument("--focus-search-end", type=float, help="End second for bounded auto audio focus search.")
    parser.add_argument("--focus-window", type=float, default=4.0, help="Focus clip/contact sheet window in seconds. Default: 4.")
    parser.add_argument("--roi", help="Optional crop/zoom rectangle as x,y,w,h in source pixels.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.topaz_like:
        args.variant_pack = True
        args.quality_tier = "premium"
        args.ai_upscale = True
    if args.focus_search_end is not None and args.focus_search_end < args.focus_search_start:
        print("ERROR: --focus-search-end must be greater than or equal to --focus-search-start", file=sys.stderr)
        return 2

    input_path = Path(args.video_path).expanduser().resolve()
    if not input_path.exists():
        print(f"ERROR: input video not found: {input_path}", file=sys.stderr)
        return 2
    if not input_path.is_file():
        print(f"ERROR: input path is not a file: {input_path}", file=sys.stderr)
        return 2

    output_dir = output_dir_for(input_path, args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    logger = JsonlLogger(output_dir / "processing-log.jsonl")

    run_id = f"{sanitize_stem(input_path)}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    tmp_dir = DEFAULT_TMP_ROOT / run_id
    frames_dir = tmp_dir / "raw_frames"

    try:
        logger.event(
            "run",
            "started",
            input=str(input_path),
            output_dir=str(output_dir),
            mode="variant_pack" if args.variant_pack else "single_output",
            quality_tier=args.quality_tier,
            topaz_like=args.topaz_like,
            disclaimer=DISCLAIMER,
        )
        capabilities = detect_optional_capabilities(logger)
        original_sha = file_sha256(input_path)
        original_size = input_path.stat().st_size
        logger.event("source_integrity", "recorded", sha256=original_sha, size_bytes=original_size)

        metadata = ffprobe(input_path, logger)
        frame_count = extract_frames(input_path, frames_dir, logger)

        if args.variant_pack:
            outputs = run_variant_pack(
                args,
                input_path,
                output_dir,
                tmp_dir,
                frames_dir,
                metadata,
                frame_count,
                original_sha,
                original_size,
                logger,
                capabilities,
            )
        else:
            outputs = run_single_output(
                args,
                input_path,
                output_dir,
                tmp_dir,
                frames_dir,
                metadata,
                frame_count,
                original_sha,
                original_size,
                logger,
            )

        cleanup_tmp(tmp_dir, args.keep_frames, logger)
        logger.event("run", "completed", output_dir=str(output_dir), disclaimer=DISCLAIMER)

        for output in outputs:
            print(f"Output: {output}")
        print(f"Processing log: {output_dir / 'processing-log.jsonl'}")
        print(DISCLAIMER)
        return 0
    except ProcessingError as exc:
        logger.event("run", "failed", error=str(exc), disclaimer=DISCLAIMER)
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        logger.event("run", "interrupted")
        print("Interrupted.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
