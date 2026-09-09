#!/usr/bin/env python3
"""Voice for the narrated presentation via fal (MiniMax speech-2.8-hd, $0.10 per 1k chars, VERIFIED 2026-08-02).
Writes audio/<key>.mp3 per narration segment; build_video.py picks them up automatically.

  python3 tts_fal.py --test              # first segment only (~$0.02)
  python3 tts_fal.py                     # every segment missing an mp3
  python3 tts_fal.py --voice Wise_Woman  # different preset voice
  python3 tts_fal.py --force             # regenerate all

Cost gate: requires a fresh `cost_gate.py approve --service fal-generic` token; logs actual spend per call."""
import argparse, json, os, pathlib, subprocess, sys, time, urllib.request

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parents[4]
AUDIO = HERE / "audio"
ENDPOINT = "https://fal.run/fal-ai/minimax/speech-2.8-hd"
PRICE_PER_1K = 0.10


def env_key():
    for line in (ROOT / ".env").read_text().splitlines():
        if line.startswith("FAL_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("FAL_KEY missing in .env")


def gate(est):
    r = subprocess.run([sys.executable, str(ROOT / "execution" / "cost_gate.py"), "check", "--service", "fal-generic",
                        "--est-cost", f"{est:.3f}"], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"cost gate denied:\n{r.stdout}{r.stderr}")


def log(cost, note):
    subprocess.run([sys.executable, str(ROOT / "execution" / "cost_gate.py"), "log", "--service", "fal-generic",
                    "--status", "success", "--actual-cost", f"{cost:.4f}", "--request", note,
                    "--project", "jen-listings"], capture_output=True, text=True)


def speak(key, text, voice, speed, out):
    body = json.dumps({
        "text": text,
        "voice_setting": {"voice_id": voice, "speed": speed, "vol": 1, "pitch": 0, "emotion": "neutral"},
        "audio_setting": {"format": "mp3", "sample_rate": 32000, "bitrate": 128000},
    }).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method="POST", headers={
        "Authorization": f"Key {env_key()}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read())
    url = (data.get("audio") or {}).get("url") or data.get("audio_url")
    if not url:
        sys.exit(f"{key}: no audio url in response: {json.dumps(data)[:400]}")
    with urllib.request.urlopen(url, timeout=180) as r:
        out.write_bytes(r.read())
    return data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice", default="Calm_Woman")
    ap.add_argument("--speed", type=float, default=0.96)
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    AUDIO.mkdir(exist_ok=True)
    segs = json.loads((HERE / "narration.json").read_text())
    if a.test:
        segs = segs[:1]
    todo = [s for s in segs if a.force or not (AUDIO / f"{s['key']}.mp3").exists()]
    est = sum(len(s["text"]) for s in todo) / 1000 * PRICE_PER_1K
    print(f"{len(todo)} segments, {sum(len(s['text']) for s in todo)} chars, est ${est:.2f}, voice {a.voice}")
    if not todo:
        return
    gate(est)
    spent = 0.0
    for s in todo:
        out = AUDIO / f"{s['key']}.mp3"
        t0 = time.time()
        try:
            speak(s["key"], s["text"], a.voice, a.speed, out)
        except urllib.error.HTTPError as e:
            sys.exit(f"{s['key']}: HTTP {e.code}: {e.read()[:600].decode(errors='replace')}")
        c = len(s["text"]) / 1000 * PRICE_PER_1K
        spent += c
        log(c, f"jen presentation narration {s['key']} ({a.voice})")
        print(f"  {s['key']}: {out.stat().st_size // 1024} KB in {time.time() - t0:.1f}s  (${c:.3f})")
    print(f"done: ${spent:.2f} spent, files in {AUDIO}")


if __name__ == "__main__":
    main()
