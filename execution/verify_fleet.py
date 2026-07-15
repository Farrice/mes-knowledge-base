#!/usr/bin/env python3
"""verify_fleet.py — run every execution/verify_*.py and report the fleet's health.

Born 2026-07-15 from the orphan-verifier finding (23 of 82 verifiers referenced
nowhere — a verifier that never fires can't catch anything; see
docs/solutions/2026-07-14-deep-research-swarm-verify-never-fires.md for the
incident class). Instead of hand-wiring dozens of scripts into docs, this
runner IS the wiring: every verifier fires on the Sunday train, and the health
collector flags a stale or failing fleet.

Subcommands / flags:
    run [--timeout N] [--only substr]   Run the fleet (default), write
                                        .agent/health/verify-fleet.json
    status                              Print last run's summary without running

Exit code: 0 if every verifier passed or was skipped, 1 otherwise.
Scheduled by launchd com.antigravity.verify-fleet (Sun 05:30, before the
06:15 deep health snapshot that reads the result).
"""

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RESULT = REPO_ROOT / ".agent" / "health" / "verify-fleet.json"

# Verifiers that need an environment this runner can't provide (external CLIs,
# live auth). Each entry carries its reason — an unexplained skip is debt.
SKIP = {
    "verify_recall_mcp_auth.py": "needs live `codex mcp list` outside sandbox",
    "verify_fleet.py": "the runner itself — recursing would deadlock",
    "verify_proof_ledger.py": "per-artifact checker (requires --draft/--ledger); fires per-deliverable, not standalone",
    "verify_video_context_source_package.py": "per-artifact checker (requires package arg); fires per-extraction, not standalone",
}

DEFAULT_TIMEOUT = 90

# Per-script timeout overrides — verifiers that legitimately need longer than
# the fleet default (e.g. dozens of router probes, each rebuilding the index).
SLOW = {
    "verify_system_control_plane.py": 240,
}


def run_fleet(timeout: int, only: str = "") -> int:
    scripts = sorted((REPO_ROOT / "execution").glob("verify_*.py"))
    if only:
        scripts = [s for s in scripts if only in s.name]
    results = []
    for s in scripts:
        if s.name in SKIP:
            results.append({"script": s.name, "status": "SKIP", "reason": SKIP[s.name], "secs": 0})
            print(f"SKIP  {s.name} ({SKIP[s.name]})")
            continue
        t0 = time.time()
        script_timeout = max(timeout, SLOW.get(s.name, 0))
        try:
            r = subprocess.run([sys.executable, str(s)], cwd=REPO_ROOT,
                               capture_output=True, text=True, timeout=script_timeout)
            secs = round(time.time() - t0, 1)
            if r.returncode == 0:
                status, detail = "PASS", ""
            else:
                status = "FAIL"
                detail = (r.stdout + r.stderr).strip().splitlines()[-1][:200] if (r.stdout or r.stderr) else ""
        except subprocess.TimeoutExpired:
            secs, status, detail = script_timeout, "TIMEOUT", f">{script_timeout}s"
        except Exception as e:  # noqa: BLE001
            secs, status, detail = round(time.time() - t0, 1), "CRASH", str(e)[:200]
        results.append({"script": s.name, "status": status, "detail": detail, "secs": secs})
        print(f"{status:<7} {s.name} ({secs}s)" + (f" — {detail}" if detail else ""))

    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    summary = {
        "ts": datetime.now().isoformat(timespec="seconds"),
        "total": len(results),
        "counts": counts,
        "failing": [r["script"] for r in results if r["status"] in ("FAIL", "TIMEOUT", "CRASH")],
        "results": results,
    }
    if only:
        # Partial runs are for triage — never overwrite the fleet-wide record.
        print(f"\nFLEET (partial --only {only!r}, not recorded): "
              f"{counts.get('PASS', 0)} pass / {len(summary['failing'])} failing")
        return 0 if not summary["failing"] else 1
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(summary, indent=2) + "\n")
    print(f"\nFLEET: {counts.get('PASS', 0)} pass / {len(summary['failing'])} failing / "
          f"{counts.get('SKIP', 0)} skip of {len(results)} — {RESULT}")
    return 0 if not summary["failing"] else 1


def status() -> int:
    try:
        s = json.loads(RESULT.read_text())
    except Exception:
        print("No fleet run recorded — run: python3 execution/verify_fleet.py")
        return 1
    print(f"Last fleet run {s['ts']}: {s['counts']} — failing: {s['failing'] or 'none'}")
    return 0 if not s["failing"] else 1


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("cmd", nargs="?", default="run", choices=["run", "status"])
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    p.add_argument("--only", default="")
    args = p.parse_args()
    return status() if args.cmd == "status" else run_fleet(args.timeout, args.only)


if __name__ == "__main__":
    sys.exit(main())
