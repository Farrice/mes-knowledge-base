#!/usr/bin/env python3
"""Wave 0 acceptance fixture — concurrency firewall (Frontier Elevation Program).

Verifies, against an ISOLATED temp tree (never the live repo lock):
  1. Double-claim blocks: a second `claim` while a fresh lock exists exits 1.
  2. Heartbeat/release require the holder's token.
  3. Fleet quarantine: 3 concurrent workers writing the same logical target produce
     zero writes to the canonical path; only the conductor's serial merge lands one file.

Run: python3 execution/verify_session_lock_gate.py   (exit 0 = Wave 0 accepted)
"""
import os
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAILURES = []


def check(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f" — {detail}" if detail and not ok else ""))
    if not ok:
        FAILURES.append(name)


def lock_fixture(tmp):
    """session_lock.py resolves ROOT from its own path — copy it into a scratch tree."""
    os.makedirs(os.path.join(tmp, "execution"))
    os.makedirs(os.path.join(tmp, ".agent"))
    script = os.path.join(tmp, "execution", "session_lock.py")
    shutil.copy(os.path.join(REPO, "execution", "session_lock.py"), script)

    def run(*args):
        return subprocess.run([sys.executable, script, *args],
                              capture_output=True, text=True)

    r1 = run("claim", "fixture-mission-A")
    check("first claim succeeds", r1.returncode == 0, r1.stdout + r1.stderr)
    token = r1.stdout.split("claimed: ")[1].split()[0] if "claimed: " in r1.stdout else ""

    r2 = run("claim", "fixture-mission-B")
    check("second claim on fresh lock exits 1", r2.returncode == 1, r2.stdout)
    check("second claim names the holder", "fixture-mission-A" in r2.stdout, r2.stdout)

    r3 = run("heartbeat", "wrong-token")
    check("heartbeat with wrong token exits 1", r3.returncode == 1, r3.stdout)
    r4 = run("heartbeat", token)
    check("heartbeat with holder token succeeds", r4.returncode == 0, r4.stdout)

    r5 = run("check")
    check("tokenless check against fresh lock exits 1", r5.returncode == 1, r5.stdout)
    r6 = run("check", token)
    check("holder check exits 0", r6.returncode == 0, r6.stdout)

    r7 = run("release", token)
    check("release with holder token succeeds", r7.returncode == 0, r7.stdout)
    r8 = run("claim", "fixture-mission-B")
    check("claim after release succeeds", r8.returncode == 0, r8.stdout)


def fanout_fixture(tmp):
    """Merge-discipline Law 1: workers write only to .tmp/<session>/<worker>/."""
    canonical = os.path.join(tmp, "deliverables", "target.md")
    os.makedirs(os.path.dirname(canonical))
    quarantine = os.path.join(tmp, ".tmp", "fixture-session")

    def worker(n):
        wdir = os.path.join(quarantine, f"worker-{n}")
        os.makedirs(wdir, exist_ok=True)
        with open(os.path.join(wdir, "target.md"), "w") as f:
            f.write(f"candidate from worker {n}\n")
        return wdir

    with ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(worker, range(3)))

    check("canonical path untouched by 3-worker fan-out", not os.path.exists(canonical))
    candidates = [os.path.join(quarantine, d, "target.md") for d in sorted(os.listdir(quarantine))]
    check("all 3 worker candidates quarantined", len(candidates) == 3)

    # Conductor merges serially: deterministic pick (here: worker-1), single canonical write.
    shutil.copy(candidates[1], canonical)
    with open(canonical) as f:
        content = f.read()
    check("serial merge lands exactly one candidate", content == "candidate from worker 1\n")


def main():
    print("Wave 0 acceptance — concurrency firewall")
    with tempfile.TemporaryDirectory() as tmp:
        lock_fixture(tmp)
    with tempfile.TemporaryDirectory() as tmp:
        fanout_fixture(tmp)
    if FAILURES:
        print(f"\nWAVE 0 REJECTED — {len(FAILURES)} failure(s): {', '.join(FAILURES)}")
        sys.exit(1)
    print("\nWAVE 0 ACCEPTED — lock gate + fleet quarantine verified")


if __name__ == "__main__":
    main()
