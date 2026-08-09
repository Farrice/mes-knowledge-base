#!/usr/bin/env python3
"""Master Fleet Verifier — actually runs every execution/verify_*.py.

WHAT BROKE (found 2026-08-08, repaired here):
Commit 2397327cf (2026-07-28) replaced the real glob with a hardcoded two-item
list — `verify_loop_integrity.py` and `verify_core_surface.py` — and NEITHER
FILE EXISTS. `run_tier()` returned {"error": "not found"} and the caller
discarded the return value. `aggregate_findings()` then read three tier JSONs
last written 2026-07-28 and republished them as fresh.

Measured at repair time: fleet.json was stamped 2026-08-02T05:30 and reported
"18 PROVEN" — from inputs dated 2026-07-28T09:31. A report five days newer than
its own data, and nothing noticed. All 85 verifiers had not executed in 13 days,
while `wiring_audit.py` stamped every one of them PROVEN via "run by the Sunday
fleet glob" — a firing path that no longer existed.

THE RULES THIS FILE NOW OBEYS
  1. A discovered-but-unrunnable verifier is a FINDING, never a discarded return.
  2. An aggregated artifact older than this run's start is STALE and says so.
     Republishing yesterday's data under today's timestamp is the whole bug.
  3. exit 0 always — audit-only, never blocks (COMPASS DOCTRINE).
  4. `--self-test` proves these checks CAN fail. A test that has never failed
     has not been tested (docs/solutions/2026-07-27-verification-with-no-reader).

Writes (both, deliberately):
  .agent/health/verify-fleet.json — per-verifier results. THE CONSUMED ONE:
      self_heal.py:60, health_metrics.py:264, execution_receipt.py:44,
      verify_self_heal.py:290 all read this path and this schema. Do not rename.
  .agent/health/fleet.json + fleet-report.md — aggregate rollup.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HEALTH_DIR = REPO_ROOT / ".agent" / "health"
FLEET_JSON = HEALTH_DIR / "verify-fleet.json"     # consumed by 4 scripts — name is load-bearing
OUTPUT_JSON = HEALTH_DIR / "fleet.json"
OUTPUT_MD = HEALTH_DIR / "fleet-report.md"

PER_SCRIPT_TIMEOUT = 180
MAX_PARALLEL = 6
SELF = Path(__file__).name

# Verifiers measured slower than the default budget (2026-08-08 triage, solo
# runs on this machine). A budget below reality manufactures false TIMEOUTs —
# five of the six "timeouts" in the first honest fleet run passed standalone.
# This raises the ceiling for named heavyweights; it never weakens a check.
SLOW_BUDGET = {
    # ~6 min solo, slower under 6-way fleet contention (480s still tripped on
    # the 2026-08-08 run while the standalone run passed).
    "verify_system_control_plane.py": 900,
}

# Rollups produced by other tools. Aggregated ONLY when fresher than this run.
# The three 2026-07-28 tier JSONs (loop-integrity, core-surface, birth-wiring)
# were REMOVED 2026-08-08: their producer scripts were archived on 07-28, so
# they can never be fresh again — a permanent STALE line is wallpaper, and
# wallpaper trains the eye to skip warnings. If a tier producer returns, add
# its artifact back here.
TIER_ARTIFACTS: list[tuple[str, Path]] = []


def discover() -> list[Path]:
    """Every verifier on disk. THE GLOB — this is what went missing."""
    return sorted(
        p for p in (REPO_ROOT / "execution").glob("verify_*.py")
        if p.name != SELF and p.is_file()
    )


def run_one(script: Path) -> dict:
    t0 = time.time()
    budget = SLOW_BUDGET.get(script.name, PER_SCRIPT_TIMEOUT)
    try:
        proc = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True, text=True,
            timeout=budget, cwd=str(REPO_ROOT),
        )
        secs = round(time.time() - t0, 1)
        if proc.returncode == 0:
            return {"script": script.name, "status": "PASS", "detail": "", "secs": secs}
        tail = (proc.stderr or proc.stdout or "").strip().splitlines()
        return {"script": script.name, "status": "FAIL",
                "detail": (tail[-1][:200] if tail else f"exit {proc.returncode}"),
                "secs": secs}
    except subprocess.TimeoutExpired:
        return {"script": script.name, "status": "TIMEOUT",
                "detail": f"exceeded {budget}s", "secs": budget}
    except Exception as e:  # a verifier that cannot start is a FINDING, not silence
        return {"script": script.name, "status": "ERROR",
                "detail": f"{type(e).__name__}: {e}"[:200],
                "secs": round(time.time() - t0, 1)}


def stale_artifacts(run_started: float) -> list[dict]:
    """Rule 2. An input older than the run is not evidence about the run."""
    out = []
    for name, path in TIER_ARTIFACTS:
        if not path.exists():
            out.append({"tier": name, "state": "MISSING", "path": str(path)})
            continue
        age_h = (run_started - path.stat().st_mtime) / 3600.0
        if age_h > 0:
            out.append({"tier": name, "state": "STALE", "path": str(path),
                        "age_hours": round(age_h, 1),
                        "mtime": datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="minutes")})
    return out


def aggregate_fresh(run_started: float) -> tuple[list, dict]:
    """Merge ONLY artifacts written during/after this run. Stale ones are reported, never merged."""
    findings, summaries = [], {}
    for name, path in TIER_ARTIFACTS:
        if not path.exists() or path.stat().st_mtime < run_started:
            continue
        try:
            data = json.loads(path.read_text())
        except (OSError, ValueError) as e:
            findings.append({"tier": name, "classification": "FLAGGED",
                             "message": f"{path.name} unreadable: {type(e).__name__}"})
            continue
        rows = [f for f in data.get("findings", []) if f.get("classification")]
        for f in rows:
            f["tier"] = name
        findings.extend(rows)
        summaries[name] = {"total": len(rows), "summary": data.get("summary", {})}
    return findings, summaries


def run_fleet(limit: int | None = None) -> dict:
    run_started = time.time()
    scripts = discover()
    if limit:
        scripts = scripts[:limit]

    results = []
    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as pool:
        results = list(pool.map(run_one, scripts))

    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    failing = [r["script"] for r in results if r["status"] != "PASS"]

    stale = stale_artifacts(run_started)
    merged, summaries = aggregate_fresh(run_started)

    # Rule 1 + 2 become findings, not silence.
    for r in results:
        if r["status"] != "PASS":
            merged.append({"tier": "verifiers", "classification": "FLAGGED",
                           "message": f"{r['script']}: {r['status']} — {r['detail']}"})
    for s in stale:
        merged.append({"tier": "aggregate", "classification": "FLAGGED",
                       "message": f"{s['tier']} artifact {s['state']}"
                                  + (f" ({s['age_hours']}h older than this run, mtime {s['mtime']})"
                                     if s["state"] == "STALE" else "")
                                  + " — NOT merged"})

    ts = datetime.now().isoformat()
    HEALTH_DIR.mkdir(parents=True, exist_ok=True)

    # consumed schema — keep exactly
    FLEET_JSON.write_text(json.dumps({
        "ts": ts, "total": len(results), "counts": counts,
        "failing": failing, "results": results,
    }, indent=2))

    classifications = {}
    for f in merged:
        c = f.get("classification")
        if c:
            classifications[c] = classifications.get(c, 0) + 1

    OUTPUT_JSON.write_text(json.dumps({
        "timestamp": ts,
        "summary": {
            "total_findings": len(merged),
            "by_classification": classifications,
            "tier_summaries": summaries,
            "verifiers_run": len(results),
            "verifiers_failing": len(failing),
            "stale_or_missing_artifacts": stale,
        },
        "findings": merged,
    }, indent=2))

    lines = [
        "# Fleet Verification Report", f"**Generated**: {ts}", "",
        f"**Verifiers run**: {len(results)} · "
        + " · ".join(f"{k} {v}" for k, v in sorted(counts.items())), "",
    ]
    if stale:
        lines += ["## ⚠️ Stale or missing aggregate inputs (NOT merged)", ""]
        lines += [f"- **{s['tier']}** — {s['state']}"
                  + (f", mtime {s['mtime']} ({s['age_hours']}h before this run)"
                     if s["state"] == "STALE" else "") for s in stale]
        lines.append("")
    if failing:
        lines += ["## 🚨 Verifiers not passing", ""]
        lines += [f"- **{r['script']}** — {r['status']}: {r['detail']}"
                  for r in results if r["status"] != "PASS"]
        lines.append("")
    OUTPUT_MD.write_text("\n".join(lines))

    return {"ts": ts, "run": len(results), "counts": counts,
            "failing": failing, "stale": stale}


def self_test() -> int:
    """Rule 4 — prove each check CAN fail, in both directions."""
    import tempfile
    ok, bad = 0, []

    def check(name, cond):
        nonlocal ok
        if cond:
            ok += 1
        else:
            bad.append(name)

    # 1 discovery is real, not hardcoded
    found = discover()
    check("discovery finds the fleet (>50)", len(found) > 50)
    check("discovery excludes self", all(p.name != SELF for p in found))

    # 2 FALSE-GREEN control: a deliberately failing script must NOT report PASS
    with tempfile.TemporaryDirectory() as td:
        boom = Path(td) / "verify_selftest_boom.py"
        boom.write_text("import sys\nsys.exit(3)\n")
        check("nonzero exit is not PASS", run_one(boom)["status"] == "FAIL")
        good = Path(td) / "verify_selftest_ok.py"
        good.write_text("print('fine')\n")
        check("zero exit is PASS (false-red control)", run_one(good)["status"] == "PASS")
        missing = Path(td) / "verify_selftest_absent.py"
        r = run_one(missing)
        check("unrunnable script surfaces, never silent", r["status"] in ("ERROR", "FAIL"))

    # 3 staleness — exercised on a SYNTHETIC artifact, not live repo state.
    # (The first version leaned on the July tier JSONs existing; when those
    # were retired the control broke. A self-test must own its fixtures.)
    global TIER_ARTIFACTS
    saved = TIER_ARTIFACTS
    try:
        with tempfile.TemporaryDirectory() as td2:
            old = Path(td2) / "synthetic-tier.json"
            old.write_text("{}")
            import os as _os
            _os.utime(old, (time.time() - 86400, time.time() - 86400))  # 1 day old
            TIER_ARTIFACTS = [("synthetic", old)]
            now = time.time()
            stale_now = stale_artifacts(now)
            check("day-old artifact reads STALE against a fresh run",
                  len(stale_now) == 1 and stale_now[0]["state"] == "STALE")
            # false-red: same artifact against a run that started BEFORE it
            check("artifact newer than the run is not stale",
                  not [s for s in stale_artifacts(now - 10 ** 7) if s["state"] == "STALE"])
            TIER_ARTIFACTS = [("gone", Path(td2) / "never-written.json")]
            check("missing artifact reads MISSING",
                  stale_artifacts(now) and stale_artifacts(now)[0]["state"] == "MISSING")
    finally:
        TIER_ARTIFACTS = saved

    print(f"self-test: {'OK' if not bad else 'FAILED'} ({ok} passed, {len(bad)} failed)")
    for b in bad:
        print(f"  FAIL: {b}")
    return 0 if not bad else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--list", action="store_true", help="show what would run")
    ap.add_argument("--limit", type=int, help="run only the first N (smoke test)")
    ap.add_argument("--self-test", action="store_true", dest="self_test")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()
    if args.list:
        found = discover()
        print(f"{len(found)} verifier(s) discovered by glob execution/verify_*.py")
        for p in found:
            print(f"  {p.name}")
        return 0

    r = run_fleet(limit=args.limit)
    if args.json:
        print(json.dumps(r, indent=2))
    else:
        print(f"FLEET: {r['run']} verifier(s) — "
              + " · ".join(f"{k} {v}" for k, v in sorted(r["counts"].items())))
        for s in r["stale"]:
            print(f"  ⚠ {s['tier']} artifact {s['state']} — not merged")
        if r["failing"]:
            print(f"  {len(r['failing'])} not passing → {OUTPUT_MD}")
    return 0  # COMPASS DOCTRINE: audit-only, never blocks


if __name__ == "__main__":
    sys.exit(main())
