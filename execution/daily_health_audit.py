#!/usr/bin/env python3
"""daily_health_audit.py — the daily dead-channel drain (06:00, launchd
com.antigravity.daily-health-audit).

Rewired 2026-07-28 (merge of two same-day builds; commit message has the
history). This is a thin orchestrator — detection logic lives where it is
surfaced and verified:

  Tiers 1+2  execution/self_heal.py `report` — dead_hooks, dead_launchd,
             stale_feeds, core_surface_bypass, wiring_orphans (+ the original
             healers' detectors). Its report cache is what pending_decisions_
             hook (session open) and /cos read, so a finding here lands in a
             channel with a PROVEN reader — never a log nobody opens.
  Tier 3     execution/wiring_audit.py `drain` — the full-asset firing-path
             ratchet (~150/day maintenance; backlog fully drained 2026-07-28).

Read-only + report-only: nothing deleted, nothing blocked (compass doctrine).
Exit 0 always. Writes .agent/health/daily-audit.json (cadence evidence for
detect_dead_launchd) — and stdout, so launchd creates the log this job's own
detector checks.
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".agent" / "health" / "daily-audit.json"
PY = sys.executable
DRAIN_BATCH = "150"  # pinned; weekly-closeout runs its own deeper pass


def _run(args: list[str], timeout: int = 600) -> tuple[int, str]:
    try:
        r = subprocess.run([PY] + args, capture_output=True, text=True,
                           timeout=timeout, cwd=str(ROOT))
        return r.returncode, (r.stdout or "")
    except Exception as e:  # noqa: BLE001 — audit must finish and report
        return -1, f"{type(e).__name__}: {e}"


def main() -> int:
    report = {"timestamp": datetime.now().isoformat()}

    # Regenerate PROJECTS.md FIRST so self_heal's org_drift detector reads a fresh
    # index rather than yesterday's. This is the deterministic backstop for
    # organization: session-close can be skipped, but the 06:00 job cannot.
    rc, out = _run([str(ROOT / "execution" / "projects_index.py"), "sync"])
    report["projects_index"] = {"exit": rc, "out": out.strip()[:200]}

    # Wide catch-up sweep. Session-close runs a bounded window to stay inside its
    # 60s budget; this one has the full timeout, so files that missed the session
    # window get filed here instead of staying invisible forever.
    rc, out = _run([str(ROOT / "execution" / "project_filer.py"), "sweep"])
    report["artifact_sweep"] = {"exit": rc, "out": out.strip()[-200:]}

    rc, out = _run([str(ROOT / "execution" / "self_heal.py"), "report", "--json"])
    try:
        rows = json.loads(out)
    except ValueError:
        rows = []
    report["self_heal"] = {"exit": rc, "findings": len(rows) if isinstance(rows, list) else -1,
                           "ids": [r.get("id") for r in rows][:12] if isinstance(rows, list) else []}

    rc, out = _run([str(ROOT / "execution" / "wiring_audit.py"), "drain",
                    "--batch", DRAIN_BATCH])
    try:
        drain = json.loads(out)
    except ValueError:
        drain = {"error": out[:200]}
    report["wiring_drain"] = drain

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2))
    # stdout -> launchd StandardOutPath -> the log detect_dead_launchd reads.
    print(json.dumps({"daily_health_audit": report["timestamp"],
                      "findings": report["self_heal"]["findings"],
                      "wiring": drain.get("coverage") or drain.get("error", "?"),
                      "orphans": drain.get("orphans_total"),
                      "projects_index": report["projects_index"]["exit"],
                      "artifact_sweep": report["artifact_sweep"]["exit"]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
