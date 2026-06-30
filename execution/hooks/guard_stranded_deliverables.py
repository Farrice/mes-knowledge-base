#!/usr/bin/env python3
"""
guard_stranded_deliverables.py — deterministic backstop against work vanishing
on a working-tree branch switch.

ROOT CAUSE this guards (2026-06-22 incident): session deliverables get committed
onto a `session/<thread>` handoff branch, then the working tree is switched back to
`main` (by the session/handoff harness or a parallel Codex worktree — i.e. OUTSIDE
this repo's own code). Files that live only on the session branch then disappear
from the working tree the user is looking at, and clickable links 404.

This guard makes the system resilient to that EXTERNAL branch switch:
  - `check`   (default): read-only. Lists deliverable files that exist on the active
              handoff branch but are MISSING from the current working tree. Prints a
              concise summary suitable for injection as hook context. Never mutates.
  - `restore`: restores ONLY the missing files via `git checkout <branch> -- <path>`.
              MISSING-ONLY by design: it never overwrites a file present in the working
              tree, never deletes anything, never touches git history. Logs every action.

Safety properties:
  - Scoped to the ACTIVE handoff-thread branch (from .agent/handoffs/LATEST.md), not all
    branches — so intentionally-deleted old work is not resurrected.
  - Scoped to PROTECTED_DIRS (deliverable output dirs) only.
  - Restore is additive + idempotent; re-running is a no-op once in sync.
  - Deterministic logging to .agent/logs/stranded-restore.log (no silent no-op).

Wire (optional, user-approved): add to .claude/settings.json UserPromptSubmit hooks as
  python3 "$CLAUDE_PROJECT_DIR/execution/hooks/guard_stranded_deliverables.py" check
(or `restore` to self-heal automatically each turn).
"""
from __future__ import annotations
import os
import sys
import subprocess
import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HANDOFF_LATEST = REPO / ".agent" / "handoffs" / "LATEST.md"
LOG = REPO / ".agent" / "logs" / "stranded-restore.log"

# Deliverable output dirs worth protecting. Intentionally NOT the whole repo —
# only where session content lands, to keep the guard precise and low-risk.
PROTECTED_DIRS = [
    "_active",
    "deliverables",
    "strategy_briefs",
    "research_outputs",
    "products",
]


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=REPO, capture_output=True, text=True
    ).stdout.strip()


def current_branch() -> str:
    return git("rev-parse", "--abbrev-ref", "HEAD")


def active_handoff_branch() -> str | None:
    """The branch the live handoff thread is on (the one whose work is 'in flight')."""
    if not HANDOFF_LATEST.exists():
        return None
    for line in HANDOFF_LATEST.read_text(encoding="utf-8", errors="ignore").splitlines():
        s = line.strip()
        if s.startswith("branch:"):
            return s.split(":", 1)[1].strip()
    return None


def branch_exists(branch: str) -> bool:
    return bool(git("rev-parse", "--verify", "--quiet", branch))


def files_on_branch(branch: str) -> list[str]:
    # -z gives NUL-delimited RAW paths (no C-quoting of ™, en-dashes, spaces),
    # so paths round-trip correctly back into `git checkout`.
    out = subprocess.run(
        ["git", "ls-tree", "-r", "-z", "--name-only", branch, "--", *PROTECTED_DIRS],
        cwd=REPO, capture_output=True, text=True,
    ).stdout
    return [p for p in out.split("\x00") if p.strip()]


def find_stranded(branch: str) -> list[str]:
    """Files committed on `branch` (under PROTECTED_DIRS) but absent from working tree."""
    return [p for p in files_on_branch(branch) if not (REPO / p).exists()]


def log(msg: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    stamp = datetime.datetime.now().isoformat(timespec="seconds")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"{stamp} {msg}\n")


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    cur = current_branch()
    active = active_handoff_branch()

    if not active or not branch_exists(active):
        # Nothing to guard against; stay quiet so it's a clean hook no-op.
        return 0
    if active == cur:
        return 0  # working tree is already on the active branch; nothing can be stranded

    stranded = find_stranded(active)
    if not stranded:
        return 0

    if mode == "restore":
        restored = []
        for p in stranded:
            r = subprocess.run(
                ["git", "checkout", active, "--", p], cwd=REPO,
                capture_output=True, text=True,
            )
            if r.returncode == 0 and (REPO / p).exists():
                restored.append(p)
        log(f"RESTORE on '{cur}' from '{active}': {len(restored)}/{len(stranded)} files")
        if restored:
            print(
                f"[guard] Restored {len(restored)} stranded deliverable(s) from "
                f"'{active}' into the working tree (you're on '{cur}'). "
                f"Files: {', '.join(restored[:6])}{'…' if len(restored) > 6 else ''}"
            )
        return 0

    # check (default) — read-only warning
    log(f"CHECK on '{cur}': {len(stranded)} stranded vs '{active}'")
    print(
        f"[guard] WARNING: {len(stranded)} deliverable file(s) are committed on "
        f"'{active}' but MISSING from your working tree (you're on '{cur}'). "
        f"They will not be viewable/clickable until restored. Run:\n"
        f"    python3 execution/hooks/guard_stranded_deliverables.py restore\n"
        f"Missing: {', '.join(stranded[:8])}{'…' if len(stranded) > 8 else ''}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
