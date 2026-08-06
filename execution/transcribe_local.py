#!/usr/bin/env python3
"""Local word-level transcription for the Edit Bay (video-studio skill).

WhisperX (faster-whisper backend + wav2vec2 forced alignment) running fully
local — $0, no API keys. Word-level timestamps are the agent's "ears": cut
decisions land on word boundaries only because of this file (Bonanno pattern:
give the agent the missing sense).

Outputs transcript.json (schema below) and optionally an .srt.
Exit codes: 0 ok · 1 failure · 2 whisperx/deps missing (prints install cmd).

  transcript.json v1:
  {"v":1,"src":"...","duration":123.4,"language":"en","model":"small",
   "segments":[{"start":0.0,"end":4.2,"text":"...",
                "words":[{"w":"the","start":0.01,"end":0.14}]}]}

CLI:
  python3 execution/transcribe_local.py <media> [--project SLUG] [--model small]
          [--out PATH] [--srt] [--language en] [--device cpu]
"""
import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# macOS venv pythons often miss the system CA bundle for urllib (torch-hub
# alignment-model downloads die with CERTIFICATE_VERIFY_FAILED) — wire certifi.
try:
    import certifi
    os.environ.setdefault("SSL_CERT_FILE", certifi.where())
    os.environ.setdefault("REQUESTS_CA_BUNDLE", certifi.where())
except ImportError:
    pass


def srt_ts(t):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int((s % 1) * 1000):03d}"


def write_srt(segments, path, max_chars=42):
    """Caption-sized SRT: split segments on word timings so lines stay short."""
    blocks, n = [], 1
    for seg in segments:
        words = seg.get("words") or []
        if not words:
            blocks.append((n, seg["start"], seg["end"], seg["text"].strip()))
            n += 1
            continue
        line, line_start = [], None
        for w in words:
            if line_start is None:
                line_start = w["start"]
            line.append(w["w"])
            if len(" ".join(line)) >= max_chars:
                blocks.append((n, line_start, w["end"], " ".join(line)))
                n += 1
                line, line_start = [], None
        if line:
            blocks.append((n, line_start, words[-1]["end"], " ".join(line)))
            n += 1
    with open(path, "w") as f:
        for i, start, end, text in blocks:
            f.write(f"{i}\n{srt_ts(start)} --> {srt_ts(end)}\n{text}\n\n")
    return len(blocks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("media")
    ap.add_argument("--project", help="_active/<slug> — writes into 05-assets/video/")
    ap.add_argument("--model", default="small",
                    help="tiny|base|small|medium|large-v3 (small = good default on CPU)")
    ap.add_argument("--out")
    ap.add_argument("--srt", action="store_true")
    ap.add_argument("--language", default="en")
    ap.add_argument("--device", default="cpu")
    args = ap.parse_args()

    if not os.path.exists(args.media):
        print(json.dumps({"ok": False, "error": f"no such file: {args.media}"}))
        sys.exit(2)

    try:
        import whisperx  # noqa
    except ImportError:
        print(json.dumps({"ok": False, "error": "whisperx not installed",
                          "fix": ".venv/bin/pip install whisperx"}))
        sys.exit(2)

    if args.out:
        out_path = args.out
    elif args.project:
        vdir = os.path.join(ROOT, "_active", args.project, "05-assets", "video")
        os.makedirs(vdir, exist_ok=True)
        out_path = os.path.join(vdir, "transcript.json")
    else:
        out_path = os.path.splitext(args.media)[0] + ".transcript.json"

    audio = whisperx.load_audio(args.media)
    model = whisperx.load_model(args.model, args.device, compute_type="int8",
                                language=args.language)
    result = model.transcribe(audio, batch_size=8)
    align_model, meta = whisperx.load_align_model(
        language_code=result.get("language", args.language), device=args.device)
    aligned = whisperx.align(result["segments"], align_model, meta, audio,
                             args.device, return_char_alignments=False)

    segments = []
    for seg in aligned["segments"]:
        words = [{"w": w["word"].strip(), "start": round(w["start"], 3),
                  "end": round(w["end"], 3)}
                 for w in seg.get("words", []) if "start" in w and "end" in w]
        segments.append({"start": round(seg["start"], 3), "end": round(seg["end"], 3),
                         "text": seg["text"].strip(), "words": words})

    doc = {"v": 1, "src": os.path.relpath(args.media, ROOT)
           if args.media.startswith(ROOT) else args.media,
           "duration": round(len(audio) / 16000.0, 2),
           "language": result.get("language", args.language),
           "model": args.model, "segments": segments}
    with open(out_path, "w") as f:
        json.dump(doc, f, indent=1)

    srt_path, srt_blocks = None, 0
    if args.srt:
        base = out_path[:-5] if out_path.endswith(".json") else out_path
        srt_path = base + ".srt"
        if args.project:
            cdir = os.path.join(ROOT, "_active", args.project, "05-assets", "video", "captions")
            os.makedirs(cdir, exist_ok=True)
            srt_path = os.path.join(cdir, "auto.srt")
        srt_blocks = write_srt(segments, srt_path)

    print(json.dumps({"ok": True, "out": out_path, "srt": srt_path,
                      "srt_blocks": srt_blocks, "segments": len(segments),
                      "words": sum(len(s["words"]) for s in segments),
                      "duration": doc["duration"], "model": args.model}))


if __name__ == "__main__":
    main()
