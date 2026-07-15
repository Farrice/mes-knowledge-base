#!/usr/bin/env python3
"""health_metrics.py — deterministic System Vitals collector (the health loop's engine).

Born 2026-07-15 from Farrice's standing intent: the harness stays at maximum
capability without him thinking about it, and NOTHING gets removed without him
knowing. This is the data layer: one fast snapshot a day, a time-series so
drift becomes visible as a TREND, and flags that are compass-not-cage (one
line + tradeoff, never a gate). Removal proposals go to the pending-review
ledger and wait for a human yes — the collector never deletes anything.

Subcommands:
    snapshot [--deep] [--dry-run]   Collect metrics -> .agent/health/latest.json
                                    + dated JSON + one line in metrics.jsonl.
                                    --deep (auto on Sundays) adds dead-skill /
                                    stale-dir scan and appends propose-archive
                                    entries to pending-review.md (propose-ONLY).
    flags [--latest]                Human-readable flag lines from latest snapshot
    trend --metric a.b.c [--days N] Time-series for one dotted metric path
    verify                          Self-check: is the loop itself alive?

No LLM calls. Stdlib only. Consumed by cos_prep.py (System Vitals brief
section) and /health-check Step 0. Scheduled by launchd
com.antigravity.health-metrics daily 06:15 (before cos-prep 06:45).
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
HEALTH = REPO_ROOT / ".agent" / "health"
METRICS_JSONL = HEALTH / "metrics.jsonl"
LATEST = HEALTH / "latest.json"
PENDING = HEALTH / "pending-review.md"
HOOKS_BASELINE = HEALTH / "hooks-baseline.json"
MEMORY_DIR = Path.home() / ".claude" / "projects" / "-Users-farricecain-Google-Antigravity" / "memory"

KEEP_DAILY = 30
KEEP_DEEP = 12


def _today() -> str:
    return datetime.now().date().isoformat()


def _git(*args, timeout=10) -> str:
    try:
        return subprocess.run(["git", *args], cwd=REPO_ROOT, capture_output=True,
                              text=True, timeout=timeout).stdout.strip()
    except Exception:
        return ""


def _dir_stats(path: Path, max_files=200_000):
    """(total_bytes, file_count) via os.scandir walk — fast, no du."""
    total, count = 0, 0
    stack = [path]
    while stack and count < max_files:
        d = stack.pop()
        try:
            with os.scandir(d) as it:
                for e in it:
                    if e.is_symlink():
                        continue
                    if e.is_dir():
                        stack.append(Path(e.path))
                    elif e.is_file():
                        try:
                            total += e.stat().st_size
                            count += 1
                        except OSError:
                            pass
        except OSError:
            pass
    return total, count


def _file_size(p: Path) -> int:
    try:
        return p.stat().st_size
    except OSError:
        return 0


def _count_stale(path: Path, days: int) -> int:
    cutoff = datetime.now().timestamp() - days * 86400
    n = 0
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d != "node_modules"]
        for f in files:
            try:
                if os.stat(os.path.join(root, f)).st_mtime < cutoff:
                    n += 1
            except OSError:
                pass
    return n


# ── collection ────────────────────────────────────────────────────


def collect_metrics(deep: bool = False) -> dict:
    m = {"ts": datetime.now().isoformat(timespec="seconds"), "date": _today(),
         "deep": deep}

    memory_md = MEMORY_DIR / "MEMORY.md"
    mem_entries = 0
    try:
        mem_entries = sum(1 for l in memory_md.read_text().splitlines()
                          if l.strip().startswith("- "))
    except Exception:
        pass
    mem_bytes, mem_files = _dir_stats(MEMORY_DIR) if MEMORY_DIR.exists() else (0, 0)
    claude_b = _file_size(REPO_ROOT / "CLAUDE.md")
    memory_b = _file_size(memory_md)
    master_b = _file_size(REPO_ROOT / "FARRICE-MASTER-CONTEXT.md")
    m["context_injection"] = {
        "claude_md_bytes": claude_b, "memory_md_bytes": memory_b,
        "memory_md_entries": mem_entries, "master_context_bytes": master_b,
        "total_bytes": claude_b + memory_b + master_b,
        "memory_dir_files": mem_files, "memory_dir_bytes": mem_bytes,
    }

    m["assets"] = {
        "skills": sum(1 for p in (REPO_ROOT / "skills").iterdir() if p.is_dir()),
        "workflows": sum(1 for p in (REPO_ROOT / ".agent" / "workflows").glob("*.md")),
        "agents": sum(1 for p in (REPO_ROOT / "agents").iterdir() if p.is_dir()),
        "directives": sum(1 for p in (REPO_ROOT / "directives").glob("*.md")),
        "execution_scripts": sum(1 for p in (REPO_ROOT / "execution").glob("*.py")),
        "verify_scripts": sum(1 for p in (REPO_ROOT / "execution").glob("verify_*.py")),
        "hooks": sum(1 for p in (REPO_ROOT / "execution" / "hooks").glob("*.py")),
        "solution_cards": sum(1 for p in (REPO_ROOT / "docs" / "solutions").glob("*.md")),
    }

    tmp_b, tmp_f = _dir_stats(REPO_ROOT / ".tmp") if (REPO_ROOT / ".tmp").exists() else (0, 0)
    m["tmp"] = {"bytes": tmp_b, "files": tmp_f}

    m["ledgers"] = {
        "observe_log_bytes": _file_size(REPO_ROOT / ".agent" / "sessions" / "observe-log.jsonl"),
        "steering_observe_bytes": _file_size(REPO_ROOT / ".agent" / "sessions" / "steering-observe.jsonl"),
        "missions_bytes": _file_size(REPO_ROOT / ".agent" / "missions.jsonl"),
        "content_finish_bytes": _file_size(REPO_ROOT / ".agent" / "content-finish-log.jsonl"),
    }

    remote_branches = [b for b in _git("branch", "-r", "--format=%(refname:short)").splitlines()
                       if b.strip() and not b.strip().endswith("/HEAD")]
    m["git"] = {
        "remote_branches": len(remote_branches),
        "stashes": len(_git("stash", "list").splitlines()),
        "dirty_files": len(_git("status", "--porcelain").splitlines()),
    }

    m["active_stale_files_60d"] = _count_stale(REPO_ROOT / "_active", 60)

    # Hook config drift: hash the hooks block; baseline is written on first
    # run and only re-blessed deliberately (delete the baseline to re-bless).
    hooks_hash = ""
    try:
        settings = json.loads((REPO_ROOT / ".claude" / "settings.json").read_text())
        hooks_hash = hashlib.sha256(
            json.dumps(settings.get("hooks", {}), sort_keys=True).encode()).hexdigest()[:16]
        if not HOOKS_BASELINE.exists():
            HEALTH.mkdir(parents=True, exist_ok=True)
            HOOKS_BASELINE.write_text(json.dumps(
                {"hash": hooks_hash, "blessed": _today()}, indent=2) + "\n")
    except Exception:
        pass
    baseline_hash = ""
    try:
        baseline_hash = json.loads(HOOKS_BASELINE.read_text()).get("hash", "")
    except Exception:
        pass
    # Fired-evidence: hook-written files' age proves the wiring is alive.
    def _age_days(p: Path) -> float:
        try:
            return round((datetime.now().timestamp() - p.stat().st_mtime) / 86400, 1)
        except OSError:
            return -1.0
    m["hooks_config"] = {
        "hash": hooks_hash, "baseline_hash": baseline_hash,
        "drifted": bool(hooks_hash and baseline_hash and hooks_hash != baseline_hash),
        "evidence_age_days": {
            "session_ledger": _age_days(REPO_ROOT / ".agent" / "sessions" / "observe-log.jsonl"),
            "steering_loop": _age_days(REPO_ROOT / ".agent" / "sessions" / "steering-observe.jsonl"),
        },
    }

    m["pending_review"] = _pending_counts()

    # Governance / constitution files — the ones injected into or steering
    # every session. Growth here is context debt at its most expensive.
    gov_files = ["CLAUDE.md", "CODEX.md", "AGENTS.md", "GEMINI.md",
                 "SLASH_COMMANDS.md", "SKILL_INDEX.md", "AGENT_INDEX.md",
                 "DOMAIN_REGISTRY.md", "PRODUCTION_CORE.md", "FARRICE-MASTER-CONTEXT.md"]
    m["governance"] = {f: _file_size(REPO_ROOT / f) for f in gov_files if (REPO_ROOT / f).exists()}
    child_claudes = [p for p in REPO_ROOT.rglob("CLAUDE.md")
                     if p != REPO_ROOT / "CLAUDE.md" and "node_modules" not in str(p)]
    agent_mds = list((REPO_ROOT / "agents").glob("*/AGENT.md"))
    m["governance"]["child_claude_md"] = {"count": len(child_claudes),
                                          "bytes": sum(_file_size(p) for p in child_claudes)}
    m["governance"]["agent_md"] = {"count": len(agent_mds),
                                   "bytes": sum(_file_size(p) for p in agent_mds),
                                   "largest": max(((_file_size(p), p.parent.name) for p in agent_mds),
                                                  default=(0, ""))[1]}

    # Self-healing launchd jobs: log-file age is fired-evidence. A launchd
    # job whose log stopped moving is a dead loop wearing a loaded label.
    m["launchd"] = _launchd_evidence()

    # Verifier fleet: freshness + failing count from the last full run.
    try:
        fleet = json.loads((HEALTH / "verify-fleet.json").read_text())
        m["verify_fleet"] = {
            "ts": fleet.get("ts", ""),
            "age_days": round((datetime.now() - datetime.fromisoformat(fleet["ts"])).total_seconds() / 86400, 1),
            "failing": len(fleet.get("failing", [])),
            "total": fleet.get("total", 0),
        }
    except Exception:
        m["verify_fleet"] = {"ts": "", "age_days": -1, "failing": -1, "total": 0}

    if deep:
        m["deep_scan"] = _deep_scan()
    return m


def _launchd_evidence() -> dict:
    """Per com.antigravity.* job: cadence (from StartCalendarInterval) and
    log-age in days. Read-only; missing plist dir or plistlib failure
    degrades to {}."""
    import plistlib
    jobs = {}
    try:
        for pl in sorted((Path.home() / "Library" / "LaunchAgents").glob("com.antigravity.*.plist")):
            try:
                data = plistlib.loads(pl.read_bytes())
                cal = data.get("StartCalendarInterval", {}) or {}
                weekly = "Weekday" in (cal if isinstance(cal, dict) else (cal[0] if cal else {}))
                log = data.get("StandardOutPath", "")
                age = -1.0
                if log and Path(log).exists():
                    age = round((datetime.now().timestamp() - Path(log).stat().st_mtime) / 86400, 1)
                jobs[data.get("Label", pl.stem)] = {"weekly": weekly, "log_age_days": age}
            except Exception:
                jobs[pl.stem] = {"weekly": False, "log_age_days": -1.0}
    except Exception:
        pass
    return jobs


def _pending_counts() -> dict:
    counts = {"pending": 0, "approved": 0, "rejected": 0}
    try:
        for l in PENDING.read_text().splitlines():
            s = re.match(r"^- status:\s*(\w+)", l.strip())
            if s and s.group(1) in counts:
                counts[s.group(1)] += 1
    except Exception:
        pass
    return counts


def _deep_scan() -> dict:
    """Sunday-grade scan: aging skills, fully-stale _active dirs (archive
    candidates), orphan verify scripts. Read-only; proposals land in the
    pending-review ledger via snapshot()."""
    scan = {}
    cutoff_120 = datetime.now().timestamp() - 120 * 86400
    aging = []
    for p in sorted((REPO_ROOT / "skills").iterdir()):
        sk = p / "SKILL.md"
        try:
            if p.is_dir() and sk.exists() and sk.stat().st_mtime < cutoff_120:
                aging.append(p.name)
        except OSError:
            pass
    scan["skills_untouched_120d"] = {"count": len(aging), "sample": aging[:10]}

    cutoff_90 = datetime.now().timestamp() - 90 * 86400
    stale_dirs = []
    for p in sorted((REPO_ROOT / "_active").iterdir()):
        if not p.is_dir():
            continue
        newest = 0
        for root, dirs, files in os.walk(p):
            for f in files:
                try:
                    newest = max(newest, os.stat(os.path.join(root, f)).st_mtime)
                except OSError:
                    pass
        if newest and newest < cutoff_90:
            stale_dirs.append(p.name)
    scan["active_dirs_fully_stale_90d"] = stale_dirs

    # Orphan verifiers: verify_*.py referenced NOWHERE — docs, configs, OR
    # code (a verifier invoked by another script is wired, not orphaned; the
    # md-only haystack over-counted 46 when the true number was 23,
    # 2026-07-15). verify_fleet.py runs them all regardless — "orphan" now
    # means "no owner documents/invokes it", a retirement signal, not a
    # never-fires signal.
    verify_names = [p.name for p in (REPO_ROOT / "execution").glob("verify_*.py")]
    haystack = ""
    for d in ("directives", ".agent/workflows", "docs", ".claude"):
        for p in (REPO_ROOT / d).rglob("*.md"):
            try:
                haystack += p.read_text(errors="ignore")
            except Exception:
                pass
    for p in (REPO_ROOT / ".claude").rglob("*.json"):
        try:
            haystack += p.read_text(errors="ignore")
        except Exception:
            pass
    for p in REPO_ROOT.glob("*.md"):
        try:
            haystack += p.read_text(errors="ignore")
        except Exception:
            pass
    for p in (REPO_ROOT / "execution").rglob("*.py"):
        if not p.name.startswith("verify_"):
            try:
                haystack += p.read_text(errors="ignore")
            except Exception:
                pass
    for p in (Path.home() / "Library" / "LaunchAgents").glob("com.antigravity.*.plist"):
        try:
            haystack += p.read_text(errors="ignore")
        except Exception:
            pass
    orphans = [v for v in verify_names if v not in haystack and v != "verify_fleet.py"]
    scan["orphan_verify_scripts"] = {"count": len(orphans), "sample": orphans[:10]}
    return scan


# ── flags (compass-not-cage: one line + tradeoff, never a gate) ───


def _history() -> list:
    try:
        return [json.loads(l) for l in METRICS_JSONL.read_text().splitlines() if l.strip()]
    except Exception:
        return []


def evaluate_flags(m: dict, history: list) -> list:
    flags = []

    def flag(text):
        flags.append(text)

    tmp_mb = m["tmp"]["bytes"] / 1e6
    if tmp_mb > 500:
        flag(f".tmp at {tmp_mb:,.0f}MB / {m['tmp']['files']:,} files — scratch with no cleanup; "
             f"classify-then-sweep reclaims disk, costs one review pass")
    ci = m["context_injection"]
    if ci["memory_md_bytes"] > 20_000 or ci["memory_md_entries"] > 150:
        flag(f"MEMORY.md at {ci['memory_md_bytes']/1e3:.0f}KB / {ci['memory_md_entries']} entries "
             f"(injected every session) — consolidating buys context headroom, costs recall granularity")
    obs_mb = m["ledgers"]["observe_log_bytes"] / 1e6
    if obs_mb > 5:
        flag(f"observe-log.jsonl at {obs_mb:.1f}MB — rotation due (gzip to .agent/sessions/archive/); "
             f"keeps ledger greppable, archives history")
    if m["git"]["remote_branches"] > 10:
        flag(f"{m['git']['remote_branches']} remote branches — content-audit then prune keeps "
             f"divergence checks fast; audit first, ours-merges make 'merged' untrustworthy")
    if m["hooks_config"].get("drifted"):
        flag("hook config drifted vs blessed baseline — diff .claude/settings.json, then delete "
             ".agent/health/hooks-baseline.json to re-bless deliberately")
    for name, age in m["hooks_config"].get("evidence_age_days", {}).items():
        if age > 7:
            flag(f"hook '{name}' has no fired-evidence in {age:.0f}d — silently-failing hook? "
                 f"(2026-07-13 incident class); check .claude/settings.json wiring")
    if m["active_stale_files_60d"] > 500:
        flag(f"_active/ holds {m['active_stale_files_60d']} files >60d old — archive candidates "
             f"accrue in pending-review; approving keeps _active meaning 'active'")
    if m["pending_review"]["pending"] > 0:
        flag(f"{m['pending_review']['pending']} removal proposal(s) awaiting your yes — "
             f".agent/health/pending-review.md")
    orphans = (m.get("deep_scan") or {}).get("orphan_verify_scripts", {})
    if orphans.get("count", 0) > 20:
        flag(f"{orphans['count']} verify_*.py scripts referenced nowhere — dead verifiers "
             f"can't catch anything (2026-07-14 incident class); wire or propose-archive them")

    gov = m.get("governance", {})
    if gov.get("CLAUDE.md", 0) > 20_000:
        flag(f"CLAUDE.md at {gov['CLAUDE.md']/1e3:.0f}KB (injected every session) — "
             f"compress per claude-md-optimization playbook; rules preserved, tokens back")
    if gov.get("SLASH_COMMANDS.md", 0) > 350_000:
        flag(f"SLASH_COMMANDS.md at {gov['SLASH_COMMANDS.md']/1e3:.0f}KB — index bloat; "
             f"trim descriptions or split before it degrades routing loads")
    agent_md = gov.get("agent_md", {})
    if agent_md.get("bytes", 0) > 3_000_000:
        flag(f"agents/*/AGENT.md total {agent_md['bytes']/1e6:.1f}MB across {agent_md['count']} agents "
             f"(largest: {agent_md.get('largest','')}) — persona bloat raises Tier-3 load cost")

    for label, j in m.get("launchd", {}).items():
        limit = 9 if j.get("weekly") else 2
        age = j.get("log_age_days", -1)
        if age < 0:
            flag(f"launchd {label}: no log evidence at all — job may never have run; "
                 f"`launchctl list {label}` to confirm")
        elif age > limit:
            flag(f"launchd {label}: log silent {age:.0f}d (cadence allows {limit}) — "
                 f"self-healing loop may be dark; check its log + `launchctl list {label}`")

    vf = m.get("verify_fleet", {})
    if vf.get("failing", 0) > 0:
        flag(f"verifier fleet: {vf['failing']}/{vf['total']} failing (run {vf['ts'][:10]}) — "
             f"each is a contract the system claims to hold; triage in weekly closeout")
    elif vf.get("age_days", -1) > 8 or vf.get("failing") == -1:
        flag("verifier fleet has no fresh run (>8d or never) — "
             "`python3 execution/verify_fleet.py` on the Sunday train")

    # Trend flags need a comparable entry ≥28d old.
    old = next((h for h in history
                if h.get("date", "9999") <= (datetime.now().date() - timedelta(days=28)).isoformat()
                and h.get("context_injection")), None)
    if old:
        then, now = old["context_injection"]["total_bytes"], ci["total_bytes"]
        if then and (now - then) / then > 0.10:
            flag(f"session context injection grew {100*(now-then)/then:.0f}% in ~1mo "
                 f"({then/1e3:.0f}KB → {now/1e3:.0f}KB) — every session pays this; trim or justify")
        s_then = old.get("assets", {}).get("skills", 0)
        if s_then and m["assets"]["skills"] - s_then >= 10:
            flag(f"skills grew +{m['assets']['skills'] - s_then} in ~1mo with growth unchecked — "
             f"pair new builds with archive passes or the routing surface dilutes")
    return flags


# ── proposals (propose-ONLY; a human flips status) ────────────────


def _append_proposals(m: dict) -> int:
    """Deep-scan findings become pending-review blocks. Dedup on target.
    NEVER executes anything — Farrice's binding rule: nothing removed
    without him knowing."""
    scan = m.get("deep_scan") or {}
    targets = [f"_active/{d}/" for d in scan.get("active_dirs_fully_stale_90d", [])]
    if not targets:
        return 0
    existing = ""
    try:
        existing = PENDING.read_text()
    except Exception:
        pass
    added = 0
    blocks = []
    for t in targets:
        if f"- target: {t}" in existing:
            continue
        added += 1
        pid = f"PR-{_today()}-{added:03d}"
        blocks.append(
            f"\n## {pid}\n- proposed: {_today()}\n- action: archive\n- target: {t}\n"
            f"- reason: every file >90d untouched (weekly deep snapshot)\n- status: pending\n")
    if blocks:
        HEALTH.mkdir(parents=True, exist_ok=True)
        header = "" if existing else (
            "# Pending Review — removal/archive proposals (nothing executes without a human yes)\n")
        with PENDING.open("a") as f:
            if header:
                f.write(header)
            f.writelines(blocks)
    return added


# ── commands ──────────────────────────────────────────────────────


def cmd_snapshot(deep: bool, dry_run: bool) -> int:
    deep = deep or datetime.now().weekday() == 6  # Sunday auto-deep
    m = collect_metrics(deep=deep)
    m["flags"] = evaluate_flags(m, _history())
    if dry_run:
        print(json.dumps(m, indent=2))
        return 0
    HEALTH.mkdir(parents=True, exist_ok=True)
    if deep:
        m["proposals_added"] = _append_proposals(m)
        m["pending_review"] = _pending_counts()
    dated = HEALTH / f"{_today()}{'-deep' if deep else ''}.json"
    dated.write_text(json.dumps(m, indent=2) + "\n")
    LATEST.write_text(json.dumps(m, indent=2) + "\n")
    with METRICS_JSONL.open("a") as f:
        slim = {k: v for k, v in m.items() if k not in ("deep_scan",)}
        f.write(json.dumps(slim) + "\n")
    _prune()
    print(f"Snapshot written: {dated} ({len(m['flags'])} flag(s)"
          + (f", {m.get('proposals_added', 0)} new proposal(s)" if deep else "") + ")")
    for fl in m["flags"]:
        print(f"  ⚑ {fl}")
    return 0


def _prune():
    daily = sorted(HEALTH.glob("????-??-??.json"))
    for p in daily[:-KEEP_DAILY]:
        p.unlink(missing_ok=True)
    deep = sorted(HEALTH.glob("????-??-??-deep.json"))
    for p in deep[:-KEEP_DEEP]:
        p.unlink(missing_ok=True)


def cmd_flags() -> int:
    try:
        m = json.loads(LATEST.read_text())
    except Exception:
        print("No snapshot yet — run: python3 execution/health_metrics.py snapshot")
        return 1
    age_h = (datetime.now() - datetime.fromisoformat(m["ts"])).total_seconds() / 3600
    print(f"System Vitals — snapshot {m['date']} ({age_h:.0f}h old)"
          + (" [DEEP]" if m.get("deep") else ""))
    if not m.get("flags"):
        print("  ✅ all green")
    for fl in m.get("flags", []):
        print(f"  ⚑ {fl}")
    return 0


def cmd_trend(metric: str, days: int) -> int:
    cutoff = (datetime.now().date() - timedelta(days=days)).isoformat()
    for h in _history():
        if h.get("date", "") < cutoff:
            continue
        v = h
        for part in metric.split("."):
            v = v.get(part) if isinstance(v, dict) else None
        if v is not None:
            print(f"{h['date']}{' deep' if h.get('deep') else ''}\t{v}")
    return 0


def cmd_verify() -> int:
    """Is the health loop itself alive? A dead health check is the failure
    mode this whole build exists to prevent."""
    problems = []
    try:
        m = json.loads(LATEST.read_text())
        age_h = (datetime.now() - datetime.fromisoformat(m["ts"])).total_seconds() / 3600
        if age_h > 48:
            problems.append(f"latest snapshot is {age_h:.0f}h old (>48h) — launchd job dead?")
    except Exception:
        problems.append("no parseable latest.json — collector has never run or is broken")
    if not METRICS_JSONL.exists():
        problems.append("metrics.jsonl missing — no time-series")
    try:
        out = subprocess.run(["launchctl", "list", "com.antigravity.health-metrics"],
                             capture_output=True, text=True, timeout=8)
        if out.returncode != 0:
            problems.append("launchd job com.antigravity.health-metrics not loaded")
    except Exception:
        problems.append("launchctl unavailable — cannot confirm scheduling")
    if PENDING.exists():
        for i, l in enumerate(PENDING.read_text().splitlines(), 1):
            if l.startswith("- status:") and not re.match(
                    r"^- status:\s*(pending|approved|rejected)\s*$", l):
                problems.append(f"pending-review.md line {i}: malformed status '{l.strip()}'")
    if problems:
        print("HEALTH LOOP VERIFY: FAIL")
        for p in problems:
            print(f"  ✗ {p}")
        return 1
    print("HEALTH LOOP VERIFY: PASS — collector fresh, time-series present, "
          "launchd loaded, ledger well-formed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_snap = sub.add_parser("snapshot", help="collect metrics + flags")
    p_snap.add_argument("--deep", action="store_true")
    p_snap.add_argument("--dry-run", action="store_true")
    p_flags = sub.add_parser("flags", help="print latest flags")
    p_flags.add_argument("--latest", action="store_true", help="(default behavior)")
    p_tr = sub.add_parser("trend", help="time-series for one metric")
    p_tr.add_argument("--metric", required=True, help="dotted path, e.g. context_injection.total_bytes")
    p_tr.add_argument("--days", type=int, default=30)
    sub.add_parser("verify", help="self-check the loop is alive")
    args = parser.parse_args()
    if args.cmd == "snapshot":
        return cmd_snapshot(args.deep, args.dry_run)
    if args.cmd == "flags":
        return cmd_flags()
    if args.cmd == "trend":
        return cmd_trend(args.metric, args.days)
    if args.cmd == "verify":
        return cmd_verify()
    return 1


if __name__ == "__main__":
    sys.exit(main())
