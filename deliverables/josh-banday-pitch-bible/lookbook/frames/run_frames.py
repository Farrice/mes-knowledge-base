"""Generate the lookbook frames from prompts.py — two takes per frame, log each call to the cost gate.

Usage: python3 run_frames.py [frame-key ...]   (default: all frames)
"""
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]  # repo (worktree) root
sys.path.insert(0, str(HERE))
from prompts import FRAMES  # noqa: E402

TAKES = 2
keys = sys.argv[1:] or list(FRAMES)
manifest_path = HERE / "manifest.json"
manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}

for key in keys:
    prompt = FRAMES[key]
    for take in range(1, TAKES + 1):
        out = HERE / f"{key}-t{take}.png"
        if out.exists():
            print(f"skip {out.name} (exists)")
            continue
        cmd = [sys.executable, str(ROOT / "execution" / "generate_image.py"),
               "--aspect", "16:9", "--resolution", "1K", "--output", str(out), prompt]
        t0 = time.time()
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT))
        ok = r.returncode == 0 and out.exists()
        print(f"{'OK ' if ok else 'ERR'} {out.name} {time.time()-t0:.0f}s")
        if not ok:
            print(r.stdout[-800:], r.stderr[-800:])
        subprocess.run([sys.executable, str(ROOT / "execution" / "cost_gate.py"), "log",
                        "--service=gemini-image", f"--status={'success' if ok else 'fail'}",
                        "--actual-cost=0.0062"], cwd=str(ROOT), capture_output=True)
        manifest[out.name] = {"frame": key, "take": take, "ok": ok, "model": "nano-banana-2",
                              "aspect": "16:9", "resolution": "1K", "est_cost_usd": 0.0062,
                              "generated": time.strftime("%Y-%m-%dT%H:%M:%S")}
        manifest_path.write_text(json.dumps(manifest, indent=2))

print("DONE", sum(1 for v in manifest.values() if v["ok"]), "frames ok")
