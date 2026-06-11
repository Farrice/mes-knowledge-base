#!/usr/bin/env python3
"""Deterministic smoke tests for execution/video_enhance.py."""

from __future__ import annotations

import hashlib
import json
import math
import shutil
import struct
import subprocess
import sys
import tempfile
import wave
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "execution" / "video_enhance.py"


def run(args: list[str], cwd: Path = ROOT, timeout: int = 240) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=str(cwd),
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )


def assert_rc(result: subprocess.CompletedProcess[str], expected: int) -> None:
    if result.returncode != expected:
        raise AssertionError(
            f"Expected rc={expected}, got {result.returncode}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )


def require_command(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise AssertionError(f"Required test command not found: {name}")
    return path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_spike_audio(path: Path, duration: float = 2.5, sample_rate: int = 8000, spike_at: float = 1.2) -> None:
    samples = int(duration * sample_rate)
    with wave.open(str(path), "wb") as handle:
        handle.setnchannels(1)
        handle.setsampwidth(2)
        handle.setframerate(sample_rate)
        for index in range(samples):
            t = index / sample_rate
            value = 0.03 * math.sin(2 * math.pi * 220 * t)
            if spike_at <= t <= spike_at + 0.08:
                value += 0.85 * math.sin(2 * math.pi * 1200 * t)
            packed = struct.pack("<h", int(max(-1.0, min(1.0, value)) * 32767))
            handle.writeframesraw(packed)


def create_sample_video(path: Path, tmp: Path) -> None:
    ffmpeg = require_command("ffmpeg")
    video_only = tmp / "video-only.mp4"
    audio = tmp / "spike.wav"
    write_spike_audio(audio)
    result = run(
        [
            ffmpeg,
            "-y",
            "-f",
            "lavfi",
            "-i",
            "testsrc2=size=160x90:rate=10:duration=2.5",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            str(video_only),
        ],
        timeout=60,
    )
    assert_rc(result, 0)
    result = run(
        [
            ffmpeg,
            "-y",
            "-i",
            str(video_only),
            "-i",
            str(audio),
            "-shortest",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            str(path),
        ],
        timeout=60,
    )
    assert_rc(result, 0)
    if not path.exists() or path.stat().st_size == 0:
        raise AssertionError("Synthetic test video was not created")


def read_log(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def assert_probe_ok(path: Path) -> None:
    ffprobe = require_command("ffprobe")
    result = run([ffprobe, "-v", "error", "-show_entries", "format=duration", "-of", "json", str(path)], timeout=30)
    assert_rc(result, 0)


def assert_file(path: Path) -> None:
    if not path.exists() or path.stat().st_size == 0:
        raise AssertionError(f"Expected output missing or empty: {path}")


def assert_single_output(source: Path, tmp: Path) -> None:
    source_hash = sha256(source)
    source_size = source.stat().st_size
    output_dir = tmp / "single-output"
    result = run(
        [
            sys.executable,
            str(TOOL),
            str(source),
            "--output-dir",
            str(output_dir),
            "--brightness",
            "0.01",
            "--contrast",
            "1.05",
            "--denoise",
            "hqdn3d",
            "--denoise-strength",
            "0.5",
            "--sharpen",
            "0.25",
            "--scale",
            "1.0",
            "--slowmo-factor",
            "1",
            "--ai-upscale",
        ],
        timeout=180,
    )
    assert_rc(result, 0)
    if sha256(source) != source_hash or source.stat().st_size != source_size:
        raise AssertionError("Original video changed during single-output enhancement")

    enhanced = output_dir / "enhanced.mp4"
    comparison = output_dir / "comparison.mp4"
    log_path = output_dir / "processing-log.jsonl"
    summary = output_dir / "processing-summary.md"
    for path in [enhanced, comparison, log_path, summary]:
        assert_file(path)
    for path in [enhanced, comparison]:
        assert_probe_ok(path)

    log_rows = read_log(log_path)
    required_steps = {
        "ffprobe_metadata",
        "extract_frames",
        "filter_chain",
        "encode_enhanced",
        "encode_comparison",
        "source_integrity",
    }
    observed_steps = {row.get("step") for row in log_rows}
    missing_steps = required_steps - observed_steps
    if missing_steps:
        raise AssertionError(f"Log missing expected steps: {sorted(missing_steps)}")

    if not shutil.which("realesrgan-ncnn-vulkan"):
        ai_rows = [row for row in log_rows if row.get("step") == "ai_upscale"]
        if not any(row.get("status") == "skipped" and "not installed" in row.get("reason", "") for row in ai_rows):
            raise AssertionError("Real-ESRGAN unavailable path was not logged as skipped")

    summary_text = summary.read_text(encoding="utf-8")
    if "does not prove contact, fault, causation, or responsibility" not in summary_text:
        raise AssertionError("Summary is missing the interpretation disclaimer")


def assert_variant_pack(source: Path, tmp: Path) -> None:
    source_hash = sha256(source)
    source_size = source.stat().st_size
    output_dir = tmp / "variant-output"
    result = run(
        [
            sys.executable,
            str(TOOL),
            str(source),
            "--output-dir",
            str(output_dir),
            "--variant-pack",
            "--focus-window",
            "2",
            "--slowmo-factor",
            "2",
            "--roi",
            "20,10,60,40",
            "--ai-upscale",
        ],
        timeout=240,
    )
    assert_rc(result, 0)
    if sha256(source) != source_hash or source.stat().st_size != source_size:
        raise AssertionError("Original video changed during variant-pack enhancement")

    expected = [
        "conservative.mp4",
        "detail.mp4",
        "motion.mp4",
        "motion-slowmo-2x.mp4",
        "motion-slowmo-4x.mp4",
        "roi-zoom.mp4",
        "variant-comparison.mp4",
        "focus-comparison.mp4",
        "contact-sheet.jpg",
        "variant-manifest.json",
        "processing-log.jsonl",
        "processing-summary.md",
    ]
    for name in expected:
        assert_file(output_dir / name)

    for name in [
        "conservative.mp4",
        "detail.mp4",
        "motion.mp4",
        "motion-slowmo-2x.mp4",
        "motion-slowmo-4x.mp4",
        "roi-zoom.mp4",
        "variant-comparison.mp4",
        "focus-comparison.mp4",
    ]:
        assert_probe_ok(output_dir / name)

    manifest = json.loads((output_dir / "variant-manifest.json").read_text(encoding="utf-8"))
    focus_time = float(manifest["focus"]["focus_time"])
    if abs(focus_time - 1.24) > 0.25:
        raise AssertionError(f"Audio focus detection missed the synthetic spike: {focus_time}")
    output_names = {entry["name"] for entry in manifest["outputs"]}
    for name in {"conservative", "detail", "motion", "motion-slowmo-2x", "motion-slowmo-4x", "roi", "variant-comparison", "focus-comparison", "contact-sheet"}:
        if name not in output_names:
            raise AssertionError(f"Variant manifest missing output: {name}")
    if "does not prove contact, fault, causation, or responsibility" not in manifest["disclaimer"]:
        raise AssertionError("Variant manifest is missing the disclaimer")

    log_rows = read_log(output_dir / "processing-log.jsonl")
    if not any(row.get("step") == "roi" and row.get("status") == "selected" for row in log_rows):
        raise AssertionError("ROI selection was not logged")
    if not any(row.get("step") == "audio_focus" and row.get("status") == "detected" for row in log_rows):
        raise AssertionError("Audio focus detection was not logged")
    if not shutil.which("realesrgan-ncnn-vulkan"):
        ai_rows = [row for row in log_rows if row.get("step") == "ai_upscale"]
        if not any(row.get("status") == "skipped" and "not installed" in row.get("reason", "") for row in ai_rows):
            raise AssertionError("Real-ESRGAN unavailable path was not logged as skipped in variant pack")


def assert_manual_focus_override(source: Path, tmp: Path) -> None:
    output_dir = tmp / "manual-focus-output"
    result = run(
        [
            sys.executable,
            str(TOOL),
            str(source),
            "--output-dir",
            str(output_dir),
            "--variant-pack",
            "--focus-time",
            "0.5",
            "--focus-window",
            "1",
            "--slowmo-factor",
            "2",
        ],
        timeout=240,
    )
    assert_rc(result, 0)
    manifest = json.loads((output_dir / "variant-manifest.json").read_text(encoding="utf-8"))
    if manifest["focus"]["source"] != "manual_focus_time":
        raise AssertionError("Manual focus time did not override auto focus")
    if abs(float(manifest["focus"]["focus_time"]) - 0.5) > 0.001:
        raise AssertionError("Manual focus time was not preserved")


def assert_premium_pack(source: Path, tmp: Path) -> None:
    output_dir = tmp / "premium-output"
    result = run(
        [
            sys.executable,
            str(TOOL),
            str(source),
            "--output-dir",
            str(output_dir),
            "--variant-pack",
            "--quality-tier",
            "premium",
            "--focus-search-start",
            "0.8",
            "--focus-search-end",
            "1.6",
            "--focus-window",
            "1",
            "--slowmo-factor",
            "2",
            "--roi",
            "20,10,60,40",
            "--ai-upscale",
        ],
        timeout=360,
    )
    assert_rc(result, 0)

    expected = [
        "restore-clean.mp4",
        "restore-sharp.mp4",
        "edge-map.mp4",
        "roi-premium.mp4",
        "premium-comparison.mp4",
        "focus-premium-comparison.mp4",
        "contact-sheet-roi.jpg",
        "variant-manifest.json",
        "processing-log.jsonl",
    ]
    for name in expected:
        assert_file(output_dir / name)

    for name in [
        "restore-clean.mp4",
        "restore-sharp.mp4",
        "edge-map.mp4",
        "roi-premium.mp4",
        "premium-comparison.mp4",
        "focus-premium-comparison.mp4",
    ]:
        assert_probe_ok(output_dir / name)

    manifest = json.loads((output_dir / "variant-manifest.json").read_text(encoding="utf-8"))
    if manifest["quality_tier"] != "premium":
        raise AssertionError("Premium manifest did not record the quality tier")
    focus_time = float(manifest["focus"]["focus_time"])
    if not (0.8 <= focus_time <= 1.6):
        raise AssertionError(f"Bounded focus detection ignored the requested search window: {focus_time}")
    output_names = {entry["name"] for entry in manifest["outputs"]}
    for name in {"restore-clean", "restore-sharp", "edge-map", "roi-premium", "premium-comparison", "focus-premium-comparison", "contact-sheet-roi"}:
        if name not in output_names:
            raise AssertionError(f"Premium manifest missing output: {name}")

    log_rows = read_log(output_dir / "processing-log.jsonl")
    if not any(row.get("step") == "capability_check" and row.get("tool") == "Topaz Video AI" for row in log_rows):
        raise AssertionError("Topaz Video AI capability check was not logged")
    if not any(row.get("step") == "audio_focus_search_window" for row in log_rows):
        raise AssertionError("Bounded focus search window was not logged")
    if "does not prove contact, fault, causation, or responsibility" not in manifest["disclaimer"]:
        raise AssertionError("Premium manifest is missing the disclaimer")


def main() -> int:
    require_command("ffmpeg")
    require_command("ffprobe")

    with tempfile.TemporaryDirectory() as tmp_name:
        tmp = Path(tmp_name)

        missing = run([sys.executable, str(TOOL), str(tmp / "missing.mp4")])
        assert_rc(missing, 2)
        assert "input video not found" in missing.stderr

        text_file = tmp / "not-video.txt"
        text_file.write_text("not a video\n", encoding="utf-8")
        non_video = run([sys.executable, str(TOOL), str(text_file), "--output-dir", str(tmp / "bad-output")])
        assert_rc(non_video, 1)
        assert "Input does not contain a video stream" in non_video.stderr or "ffprobe" in non_video.stderr

        source = tmp / "source.mp4"
        create_sample_video(source, tmp)
        assert_single_output(source, tmp)
        assert_variant_pack(source, tmp)
        assert_manual_focus_override(source, tmp)
        assert_premium_pack(source, tmp)

    print("video_enhance tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
