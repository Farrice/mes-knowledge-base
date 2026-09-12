#!/usr/bin/env python3
"""verify_content_finish_gate.py — both-direction check for the copy floor gate (2026-09-11).

The gate (`content_finish_gate.py check`) had a real log but no verifier, and nothing proved it
still fails what it must fail. Positive: clean copy → CLEAN, exit 0, a log line with the label.
Negative: copy carrying the banned structural tells (reveal reversal, triple anaphora, cheap
question close, em-dash flood) → FAIL, exit 2, the fails named; empty input → exit 2 and no log
line. The log is snapshotted and restored. Exit 0 pass, 1 fail.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
GATE = REPO / "execution" / "content_finish_gate.py"
LOG = REPO / ".agent" / "content-finish-log.jsonl"
PASS = FAIL = 0

CLEAN = ("I lost the first listing because I priced it like a spreadsheet. The second one sold in nine days "
         "because I priced it like a neighbor. Here is the difference, in plain words. A spreadsheet looks at "
         "comps. A neighbor looks at who is walking the block on Saturday. You want the neighbor.")
SLOPPY = ("It's not about the price. It's about the story. If you want it, if you need it, if you crave it, "
          "you'll get it — and that's the truth — the whole truth — nothing but — the truth. "
          "Here's the part nobody tells you. What would you do?")


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"  ok  {name}")
    else:
        FAIL += 1
        print(f"FAIL  {name}" + (f" — {detail}" if detail else ""))


def run(*args):
    r = subprocess.run([sys.executable, str(GATE), "check", *args], capture_output=True, text=True, cwd=str(REPO), timeout=60)
    return r.returncode, r.stdout + r.stderr


def main():
    snap = LOG.read_bytes() if LOG.exists() else None
    try:
        before = len(LOG.read_text().splitlines()) if LOG.exists() else 0
        rc, out = run("--text", CLEAN, "--label", "verify-clean")
        check("clean copy → CLEAN, exit 0", rc == 0 and "CLEAN" in out, out[:200])
        lines = LOG.read_text().splitlines() if LOG.exists() else []
        last = json.loads(lines[-1]) if lines else {}
        check("clean run wrote a log line with the label and verdict", len(lines) == before + 1 and last.get("label") == "verify-clean" and last.get("verdict") == "CLEAN", str(last)[:200])
        rc, out = run("--text", SLOPPY, "--label", "verify-sloppy")
        check("sloppy copy → FAIL, exit 2", rc == 2 and "FAIL" in out, out[:300])
        check("the fails are named (reveal pattern, anaphora, cheap close, em-dashes)",
              sum(k in out for k in ("It's not X", "anaphora", "Cheap-question", "em-dashes")) >= 3, out[:400])
        lines = LOG.read_text().splitlines()
        last = json.loads(lines[-1])
        check("sloppy run logged FAIL with its fails list", last.get("verdict") == "FAIL" and len(last.get("fails") or []) >= 3, str(last)[:200])
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as fh:
            fh.write(CLEAN)
            fp = fh.name
        rc, out = run("--file", fp, "--platform", "linkedin")
        check("--file input works and platform rules run (LinkedIn)", rc in (0, 2) and "CONTENT FINISH GATE" in out, out[:200])
        n = len(LOG.read_text().splitlines())
        rc, out = run("--text", "   ")
        check("empty input → exit 2, no log line", rc == 2 and len(LOG.read_text().splitlines()) == n, out[:200])
    finally:
        if snap is None:
            if LOG.exists():
                LOG.unlink()
        else:
            LOG.write_bytes(snap)
    print(f"\nverify_content_finish_gate: {PASS} pass, {FAIL} fail")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
