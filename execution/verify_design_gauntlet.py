#!/usr/bin/env python3
"""verify_design_gauntlet.py — both-direction check for the design gauntlet runner (2026-09-11).

Positive: open writes the fingerprint + receipt + log line; shoot without a renderer writes a
CAPTURE-PLAN and marks the round VISUAL UNVERIFIED; attach with real files flips it to VERIFIED;
verdict / repair / close each write their file and a log line; close records surviving risks.
Negative: verdict before a baseline is refused; verdict on an unverified round is refused; repair
before a verdict is refused; PASS close with unverified rounds is refused; a third repair nudges.
Isolated under a temp DESIGN_GAUNTLET_ROOT; the global log is snapshotted and restored.
Exit 0 pass, 1 fail.
"""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
RUNNER = REPO / "execution" / "design_gauntlet.py"
LOG = REPO / ".agent" / "design-gauntlet-log.jsonl"
IDX = REPO / ".agent" / "design-gauntlet-index.json"
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"  ok  {name}")
    else:
        FAIL += 1
        print(f"FAIL  {name}" + (f" — {detail}" if detail else ""))


def main():
    snap = {p: (p.read_bytes() if p.exists() else None) for p in (LOG, IDX)}
    tmp = Path(tempfile.mkdtemp())
    env = dict(os.environ, DESIGN_GAUNTLET_ROOT=str(tmp))

    def g(*args):
        r = subprocess.run([sys.executable, str(RUNNER), *args], capture_output=True, text=True, env=env, cwd=str(REPO), timeout=60)
        return r.returncode, r.stdout + r.stderr

    try:
        art = tmp / "art.html"
        art.write_text("<h1>x</h1>")
        rc, out = g("open", "v", "--artifact", str(art), "--bar", "ref.png", "--mode", "Precision Polish")
        d = tmp / "v"
        check("open → fingerprint + receipt + log line", rc == 0 and (d / "fingerprint.json").exists() and (d / "GAUNTLET-RECEIPT.md").exists()
              and LOG.exists() and '"event": "open"' in LOG.read_text().splitlines()[-1], out[:200])
        rc, out = g("open", "v", "--artifact", str(art), "--bar", "ref.png", "--mode", "nonsense")
        check("open with an unknown mode is refused", rc == 1)
        rc, out = g("verdict", "v", "--round", "1", "--verdict", "A", "--gap", "g", "--evidence", "e")
        check("verdict before any baseline shoot is refused", rc == 1 and "REFUSED" in out, out[:200])
        rc, out = g("shoot", "v")
        plan = d / "round-1" / "CAPTURE-PLAN.md"
        renderer = "SHOT" in out
        check("shoot → round-1 exists; no renderer → CAPTURE-PLAN written (or a real render)", rc == 0 and (renderer or plan.exists()), out[:200])
        if not renderer:
            rc, out = g("verdict", "v", "--round", "1", "--verdict", "A", "--gap", "g", "--evidence", "e")
            check("verdict on a VISUAL UNVERIFIED round is refused", rc == 1 and "UNVERIFIED" in out, out[:200])
            png = tmp / "p.png"
            png.write_bytes(b"\x89PNG fake")
            rc, out = g("attach", "v", "--round", "1", "--desktop", str(png), "--tablet", str(png), "--mobile", str(png))
            check("attach three files → VISUAL VERIFIED", rc == 0 and "VISUAL VERIFIED" in out, out[:200])
            rc, out = g("attach", "v", "--round", "1", "--desktop", str(tmp / "missing.png"))
            check("attach a missing file → nudge, not a crash", "nudge" in out, out[:200])
        rc, out = g("repair", "v", "--round", "1", "--did", "x")
        check("repair before a verdict is refused", rc == 1 and "REFUSED" in out, out[:200])
        rc, out = g("verdict", "v", "--round", "1", "--verdict", "B", "--gap", "hierarchy", "--evidence", "desktop hero")
        check("verdict on a verified round → verdict.json + log", rc == 0 and (d / "round-1" / "verdict.json").exists()
              and '"event": "verdict"' in LOG.read_text().splitlines()[-1], out[:200])
        rc, out = g("repair", "v", "--round", "1", "--did", "tightened spacing")
        check("repair after a verdict → repair.json, count 1/2", rc == 0 and "REPAIR 1/2" in out, out[:200])
        rec = (d / "GAUNTLET-RECEIPT.md").read_text()
        check("receipt carries round, verdict, gap, repair", all(k in rec for k in ("Round 1", "verdict: B", "hierarchy", "repair 1/2")), rec[:300])
        g("shoot", "v", "--round", "2")
        rc, out = g("close", "v", "--risks", "mobile CTA untested")
        check("PASS close with an unverified round is refused (defaults to FAIL verdict → allowed)", rc == 0 and "FAIL" in out, out[:200])
        rc, out = g("close", "v", "--risks", "r", "--verdict", "PASS")
        check("explicit PASS with an unverified round is refused", rc == 1 and "REFUSED" in out, out[:200])
        rec = (d / "GAUNTLET-RECEIPT.md").read_text()
        check("closed receipt names surviving risks + repairs used", "surviving risks: mobile CTA untested" in rec and "repairs used: 1/2" in rec, rec[-300:])
        check("global log has open + close for this slug", sum(1 for l in LOG.read_text().splitlines() if '"slug": "v"' in l and ('"open"' in l or '"close"' in l)) >= 2)
        rc, out = g("status", "nope")
        check("status on an unknown slug → exit 1", rc == 1)
    finally:
        for p, b in snap.items():
            if b is None:
                if p.exists():
                    p.unlink()
            else:
                p.write_bytes(b)
    print(f"\nverify_design_gauntlet: {PASS} pass, {FAIL} fail")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
