#!/usr/bin/env python3
"""
Divergence Alarm — SessionStart hook. Makes silent loss impossible.

Born from the 2026-07-13 divergent-branch discovery (docs/solutions/
2026-07-13-divergent-branch-work-silently-lost.md): a June session's work sat
on an unmerged session branch for three weeks while memory cited it as live.
Policy since (Farrice, 2026-07-13): ALL work on main; Codex keeps its worktree
branch with mandatory merge-back; anything that diverges gets announced at
every session open.

Reports (only when non-zero — silence means healthy):
  1. Branches (local + remote) holding commits main lacks (patch-equivalence,
     not SHA ancestry — a branch whose content already landed on main under a
     different SHA does not alarm)
  2. EMPTY-ABSORB: recent merges into main that dropped files the merged
     branch created (the `merge -s ours` loss class, 2026-07-15 incident:
     ad7978724/39840843d discarded the 07-14 GEO brief). Checks against
     CURRENT main, so restoring the files clears the alarm.
  3. Unpushed commits on main
  4. Uncommitted changes in the working tree
  5. Citation-integrity missing-pointer count (fast local scan)
  6. Stale FETCH_HEAD (>24h) — divergence counts are only as fresh as the
     last fetch

Emits plain text to stdout -> SessionStart additionalContext. Never blocks.
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


def _git(*args) -> str:
    try:
        return subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=8
        ).stdout.strip()
    except Exception:
        return ""


# Paths whose absence from main is telemetry churn, not content loss.
_IGNORE_PREFIXES = (".agent/", ".tmp/", ".memory/", "node_modules/")

# Cap work so the hook stays fast at session open.
_MAX_MERGES = 12
_MAX_FILES_PER_MERGE = 200


def _detect_empty_absorbs(baseline: str = "main", since: str = "14.days"):
    """Merges into `baseline` whose branch-created files are absent from the
    CURRENT `baseline` tree. Returns {merge_sha: [lost_paths]}."""
    merges = _git("log", "--merges", f"--since={since}", "--format=%H", baseline).splitlines()
    candidates = []  # (merge_sha, path)
    for m in merges[:_MAX_MERGES]:
        base = _git("merge-base", f"{m}^1", f"{m}^2")
        if not base:
            continue
        added = _git("diff", "--diff-filter=A", "--name-only", base, f"{m}^2").splitlines()
        for f in added[:_MAX_FILES_PER_MERGE]:
            f = f.strip()
            if f and not f.startswith(_IGNORE_PREFIXES):
                candidates.append((m, f))
    if not candidates:
        return {}
    # One batched existence check against the current baseline tree.
    try:
        r = subprocess.run(
            ["git", "cat-file", "--batch-check"],
            input="".join(f"{baseline}:{f}\n" for _, f in candidates),
            cwd=ROOT, capture_output=True, text=True, timeout=15,
        )
        results = r.stdout.splitlines()
    except Exception:
        return {}
    lost = {}
    for (m, f), line in zip(candidates, results):
        if "missing" in line:
            lost.setdefault(m, []).append(f)
    return lost


def _lane_exemptions():
    """Branches that are ACTIVE worktree lanes or registered parked lanes are
    expected to diverge — that's a live lane, not lost work (2026-08-06 lanes
    build). Ground truth from `git worktree list`; parked set from lanes.json.
    Returns (exempt_refs, n_active, parked_info)."""
    exempt, active, parked = set(), [], []
    try:
        sys.path.insert(0, str(ROOT / "execution"))
        import worktree_lane as wl
        lanes = wl.active_lanes(ROOT)
        for b in lanes:
            exempt.add(b)
            exempt.add(f"origin/{b}")
            active.append(b)
        for b, meta in wl.load_registry(ROOT).items():
            if meta.get("status") == "parked":
                exempt.add(b)
                exempt.add(f"origin/{b}")
                parked.append((b, meta.get("reason", "?"), meta.get("parked_at", "")))
    except Exception:
        pass
    return exempt, active, parked


def main():
    lines = []
    exempt, active_lanes_, parked_lanes = _lane_exemptions()

    # 1) Branches with work main lacks (local + remote, skip HEAD pointers).
    #    --cherry-pick drops commits whose PATCH already exists on main under a
    #    different SHA (rebased / recovered file-wise), killing that false-
    #    positive class. A true alarm here means real unabsorbed content.
    #    Active/parked LANES are exempt — they are announced separately below.
    refs = _git("for-each-ref", "--format=%(refname:short)", "refs/heads", "refs/remotes/origin")
    diverged = []
    for ref in refs.splitlines():
        ref = ref.strip()
        if not ref or ref in ("main", "origin/main", "origin/HEAD") or ref.endswith("/HEAD"):
            continue
        if ref in exempt:
            continue
        count = _git("rev-list", "--cherry-pick", "--right-only", "--count", f"main...{ref}")
        if count.isdigit() and int(count) > 0:
            diverged.append(f"{ref} (+{count})")
    if diverged:
        lines.append(
            f"⚠ DIVERGENCE: {len(diverged)} branch(es) hold work main lacks: "
            + ", ".join(diverged[:5])
            + (" …" if len(diverged) > 5 else "")
            + " — RECOVER FILES FIRST, then merge (never `merge -s ours` to silence this alarm; that is how the 07-14 brief was lost)."
        )

    # 1b) EMPTY-ABSORB detector: merges into main (last 14 days) that dropped
    #     files the merged branch itself created. Verifies against CURRENT
    #     main so a completed recovery clears the alarm.
    lost_by_merge = _detect_empty_absorbs()
    for merge_sha, files in lost_by_merge.items():
        preview = ", ".join(files[:3]) + (" …" if len(files) > 3 else "")
        lines.append(
            f"⚠ EMPTY-ABSORB: merge {merge_sha[:9]} dropped {len(files)} file(s) the branch created: "
            f"{preview} — recover with `git show <branch>:<path>` (loss class: docs/solutions/2026-07-13-divergent-branch-work-silently-lost.md)."
        )

    # 2) Unpushed commits on main.
    unpushed = _git("rev-list", "--count", "origin/main..main")
    if unpushed.isdigit() and int(unpushed) > 0:
        lines.append(f"⚠ UNPUSHED: main is {unpushed} commit(s) ahead of origin — push (auto-push hook should handle this; if it recurs, the hook is broken).")

    # 3) Dirty working tree (excluding pure telemetry churn).
    status = _git("status", "--porcelain")
    real = [
        l for l in status.splitlines()
        if l.strip() and not any(
            p in l for p in (".agent/sessions/", ".agent/steering", ".agent/routing-intelligence",
                             ".agent/skill-index", ".agent/forge-state", ".agent/handoffs/")
        )
    ]
    if len(real) > 3:
        lines.append(f"⚠ UNCOMMITTED: {len(real)} non-telemetry files changed in the working tree — commit early, the end-session gate will insist.")

    # 4) Citation integrity (fast, local).
    try:
        r = subprocess.run(
            [sys.executable, str(ROOT / "execution" / "citation_integrity.py"), "--quiet"],
            capture_output=True, text=True, timeout=20, cwd=ROOT,
        )
        out = (r.stdout or "").strip()
        if "missing pointers:" in out:
            n = out.rsplit(":", 1)[-1].strip()
            if n.isdigit() and int(n) > 0:
                lines.append(f"⚠ CITATIONS: {n} doc/memory pointer(s) reference missing files — run `python3 execution/citation_integrity.py` (a live doc citing a missing file is a LOSS SIGNAL).")
    except Exception:
        pass

    # 5) Stale remote-tracking refs make every count above untrustworthy.
    try:
        import time
        fetch_head = ROOT / ".git" / "FETCH_HEAD"
        if fetch_head.exists():
            age_h = (time.time() - fetch_head.stat().st_mtime) / 3600
            if age_h > 24:
                lines.append(f"⚠ STALE FETCH: last `git fetch` was {age_h:.0f}h ago — divergence counts may be stale; run `git fetch --all`.")
    except Exception:
        pass

    # 6) Lanes — informational, never an alarm (they merge back automatically).
    #    Parked lanes older than 7 days escalate to a nudge.
    if active_lanes_ or parked_lanes:
        import time as _t
        from datetime import datetime as _dt
        stale_parked = []
        for b, reason, at in parked_lanes:
            try:
                age_d = (_t.time() - _dt.fromisoformat(at).timestamp()) / 86400
            except Exception:
                age_d = 0
            if age_d > 7:
                stale_parked.append(f"{b} ({age_d:.0f}d)")
        info = (f"LANES: {len(active_lanes_)} active"
                + (f" ({', '.join(active_lanes_[:3])})" if active_lanes_ else "")
                + (f", {len(parked_lanes)} parked — resolve: python3 execution/"
                   f"worktree_lane.py merge --lane <branch>" if parked_lanes else ""))
        lines.append(info)
        if stale_parked:
            lines.append(f"⚠ PARKED >7d: {', '.join(stale_parked[:3])} — merge or teardown "
                         f"(worktree_lane.py doctor shows the full picture).")

    if lines:
        print("GIT INTEGRITY (deterministic, from divergence_alarm_hook.py):")
        for l in lines:
            print(f"  {l}")

    sys.exit(0)


if __name__ == "__main__":
    main()
