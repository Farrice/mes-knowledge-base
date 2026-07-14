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
  1. Branches (local + remote) holding commits main lacks
  2. Unpushed commits on main
  3. Uncommitted changes in the working tree
  4. Citation-integrity missing-pointer count (fast local scan)

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


def main():
    lines = []

    # 1) Branches with work main lacks (local + remote, skip HEAD pointers).
    refs = _git("for-each-ref", "--format=%(refname:short)", "refs/heads", "refs/remotes/origin")
    diverged = []
    for ref in refs.splitlines():
        ref = ref.strip()
        if not ref or ref in ("main", "origin/main", "origin/HEAD") or ref.endswith("/HEAD"):
            continue
        count = _git("rev-list", "--count", f"main..{ref}")
        if count.isdigit() and int(count) > 0:
            diverged.append(f"{ref} (+{count})")
    if diverged:
        lines.append(
            f"⚠ DIVERGENCE: {len(diverged)} branch(es) hold work main lacks: "
            + ", ".join(diverged[:5])
            + (" …" if len(diverged) > 5 else "")
            + " — absorb before building (policy: all work on main)."
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

    if lines:
        print("GIT INTEGRITY (deterministic, from divergence_alarm_hook.py):")
        for l in lines:
            print(f"  {l}")

    sys.exit(0)


if __name__ == "__main__":
    main()
