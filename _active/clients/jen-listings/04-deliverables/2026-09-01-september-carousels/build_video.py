#!/usr/bin/env python3
"""The talking version of the presentation: one 1080x1920 mp4 that walks Jen through every board with a voice and
burned-in captions, built from narration.json + the rendered PNGs.

  python3 build_video.py            # voice from audio/<key>.wav if present, else macOS `say` (free draft)
  python3 build_video.py --say-only # force the free draft voice

narration.json: [{"key": "deck-01", "text": "..."}, ...]  (key = png stem in png/)
Audio for a real voice: drop audio/<key>.wav|.mp3 (any TTS) and rerun; the frame timing follows the audio.
Captions are rendered as frames (chrome-headless), so no ffmpeg subtitle filter is needed.
Writes video/september-for-jen.mp4 and video/september-for-jen.srt."""
import glob, json, os, pathlib, re, shutil, subprocess, sys

HERE = pathlib.Path(__file__).parent
PNG, AUDIO, OUT = HERE / "png", HERE / "audio", HERE / "video"
TMP = HERE / ".video_tmp"
CHROME = sorted(glob.glob(os.path.expanduser(
    "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell")))[-1]
W, H = 1080, 1920
BOARD_H = 1350
SAY_ONLY = "--say-only" in sys.argv
GAP = 0.55  # silence after each segment, seconds

INK, CREAM, SOFT, STEEL = "#1E3A5F", "#F7F5F2", "#C9D4E2", "#4C7CA8"


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def duration(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)]).stdout
    return float(out.strip())


def tts(key, text):
    """Return a wav path for this segment."""
    for ext in ("wav", "mp3", "m4a"):
        p = AUDIO / f"{key}.{ext}"
        if p.exists() and not SAY_ONLY:
            wav = TMP / f"{key}.wav"
            run(["ffmpeg", "-y", "-i", str(p), "-ar", "44100", "-ac", "1", str(wav)])
            return wav, "file"
    aiff = TMP / f"{key}.aiff"
    run(["say", "-v", "Samantha", "-r", "172", "-o", str(aiff), text])
    wav = TMP / f"{key}.wav"
    run(["ffmpeg", "-y", "-i", str(aiff), "-ar", "44100", "-ac", "1", str(wav)])
    return wav, "say"


def chunks(text, max_words=14):
    """Caption chunks: split on sentence ends, then cap length."""
    sents = re.split(r"(?<=[.?!])\s+", text.strip())
    out = []
    for s in sents:
        words = s.split()
        while len(words) > max_words:
            cut = max_words
            for k in range(max_words, 6, -1):
                if words[k - 1].endswith((",", ";", ":")):
                    cut = k
                    break
            out.append(" ".join(words[:cut]))
            words = words[cut:]
        if words:
            out.append(" ".join(words))
    return out


def frame_html(png, caption, section):
    return f'''<!doctype html><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&family=Overpass:wght@400;600&display=swap">
<style>
  html, body {{ margin: 0; width: {W}px; height: {H}px; background: {INK}; overflow: hidden; font-family: Figtree, system-ui, sans-serif; }}
  .board {{ position: absolute; left: 0; top: 0; width: {W}px; height: {BOARD_H}px; }}
  .board img {{ width: {W}px; height: {BOARD_H}px; display: block; }}
  .cap {{ position: absolute; left: 0; top: {BOARD_H}px; width: {W}px; height: {H - BOARD_H}px; box-sizing: border-box;
          padding: 64px 90px 0; display: flex; flex-direction: column; gap: 26px; }}
  .sec {{ font-family: Overpass, sans-serif; font-size: 20px; font-weight: 600; letter-spacing: 0.24em; color: {STEEL}; text-transform: uppercase; }}
  .txt {{ font-size: 46px; line-height: 1.34; color: {CREAM}; font-weight: 500; letter-spacing: -0.005em; }}
</style>
<div class="board"><img src="{png.as_uri()}"></div>
<div class="cap"><div class="sec">{section}</div><div class="txt">{caption}</div></div>'''


def render(html_path, png_path):
    run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
         f"--window-size={W},{H}", "--virtual-time-budget=2500", f"--screenshot={png_path}", html_path.as_uri()])


def srt_time(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def main():
    if TMP.exists():
        shutil.rmtree(TMP)
    TMP.mkdir()
    OUT.mkdir(exist_ok=True)
    AUDIO.mkdir(exist_ok=True)
    segs = json.loads((HERE / "narration.json").read_text())

    concat_v, concat_a, srt, t = [], [], [], 0.0
    voices = set()
    n = 0
    for seg in segs:
        key, text, section = seg["key"], seg["text"], seg.get("section", "")
        png = PNG / f"{key}.png"
        if not png.exists():
            print("missing png:", key)
            continue
        wav, src = tts(key, text)
        voices.add(src)
        d = duration(wav)
        # pad silence after the segment
        padded = TMP / f"{key}-p.wav"
        run(["ffmpeg", "-y", "-i", str(wav), "-af", f"apad=pad_dur={GAP}", str(padded)])
        concat_a.append(padded)
        parts = chunks(text)
        total_chars = sum(len(p) for p in parts) or 1
        for k, cap in enumerate(parts):
            share = (d * len(cap) / total_chars) + (GAP if k == len(parts) - 1 else 0)
            fh = TMP / f"f{n:03d}.html"
            fp = TMP / f"f{n:03d}.png"
            fh.write_text(frame_html(png, cap, section))
            render(fh, fp)
            concat_v.append((fp, share))
            srt.append(f"{len(srt) + 1}\n{srt_time(t)} --> {srt_time(t + share)}\n{cap}\n")
            t += share
            n += 1
        print(f"{key}: {d:.1f}s, {len(parts)} captions ({src})")

    lst = TMP / "frames.txt"
    lines = []
    for fp, share in concat_v:
        lines.append(f"file '{fp}'\nduration {share:.3f}")
    lines.append(f"file '{concat_v[-1][0]}'")  # concat demuxer needs the last frame repeated
    lst.write_text("\n".join(lines) + "\n")
    alist = TMP / "audio.txt"
    alist.write_text("".join(f"file '{p}'\n" for p in concat_a))
    audio_all = TMP / "audio.wav"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(alist), str(audio_all)])
    out = OUT / "september-for-jen.mp4"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-i", str(audio_all),
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30", "-vf", f"scale={W}:{H}", "-preset", "medium", "-crf", "20",
         "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(out)])
    (OUT / "september-for-jen.srt").write_text("\n".join(srt))
    print(f"video: {out} ({out.stat().st_size // 1024 // 1024} MB, {t / 60:.1f} min, voice: {', '.join(sorted(voices))})")


if __name__ == "__main__":
    main()
