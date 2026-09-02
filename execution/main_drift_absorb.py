#!/usr/bin/env python3
"""Main drift absorb — the missing step between "main is dirty" and "lanes merge".

WHY (Farrice, 2026-09-02): scheduled maintenance (health collector, catalog,
homebase, index generators, research-brief regen, mission queue) writes
tracked files on the integration tree. `worktree_lane.py merge` correctly
refuses to merge into a dirty main, `lane_reconciler.py` correctly leaves
blocked lanes alone — and nothing ever cleaned main. Result on the day this
was built: 90 dirty tracked files, 40 parked lanes, 243 stranded commits,
main 70 commits ahead of origin and unpushed.

WHAT IT DOES (deterministic, loss-proof):
  1. Classify every tracked dirty path on main:
       generated-index   worktree_lane GENERATED_* + the top-level indexes
       state/receipt     .agent/, evolution_store/, knowledge/compiled/,
                         deliverables/research-briefs/, logs, jsonl, ...
       UNCLASSIFIED      anything else -> ABORT (exit 2). Human work is never
                         swept into a maintenance commit blind.
  2. Adopt only the untracked files that are clearly repo content minted by
     the harness (workflow wrappers, dated health/sweep receipts). Everything
     else stays untracked and is listed.
  3. Refuse if a fresh foreign writer holds main (session_lock) — integration
     is someone else's right now.
  4. Commit as `chore(main): absorb scheduled-maintenance drift`.
  5. --push: push main to origin. Never --force.

Usage:
    python3 execution/main_drift_absorb.py --dry-run     # classify + report only
    python3 execution/main_drift_absorb.py               # commit
    python3 execution/main_drift_absorb.py --push        # commit + push main
"""
from __future__ import annotations

import argparse
import collections
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import worktree_lane as wl  # noqa: E402

RECEIPT_REL = Path(".agent") / "health" / "main-drift-absorb.json"

STATE_PREFIXES = (
    ".agent/", "evolution_store/", "knowledge/compiled/", "deliverables/research-briefs/",
    "_active/farrice-brand/intelligence/", "_active/knowledge/", ".claude/commands/",
)
STATE_SUFFIXES = (".log", ".jsonl")
GENERATED_TOP = {
    "AGENT_INDEX.md", "PROJECTS.md", "SKILL_INDEX.md", "SLASH_COMMANDS.md",
    "guides/INDEX.md", "docs/solutions/index.md", "knowledge/index.md",
}
# Untracked paths the harness mints as real repo content (menu parity, receipts).
ADOPT_UNTRACKED_PREFIXES = (".agent/workflows/", ".claude/commands/", ".agent/health/", ".agent/sweep/")
ADOPT_UNTRACKED_SUFFIXES = (".md", ".json")


def _git(cwd: Path, *args: str, timeout: int = 120):
    r = subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True, timeout=timeout)
    # rstrip only: porcelain status lines begin with a significant space (" M path").
    return r.returncode, r.stdout.rstrip("\n"), r.stderr.strip()


def classify(path: str) -> str:
    if wl._is_generated(path) or path in GENERATED_TOP:
        return "generated-index"
    if path.startswith(STATE_PREFIXES) or path.endswith(STATE_SUFFIXES):
        return "state/receipt"
    return "UNCLASSIFIED"


def adoptable(path: str) -> bool:
    if path.endswith("/") or path == str(RECEIPT_REL):
        return False
    return path.startswith(ADOPT_UNTRACKED_PREFIXES) and path.endswith(ADOPT_UNTRACKED_SUFFIXES)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--push", action="store_true", help="push main to origin after committing")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    main_root = wl.main_root()
    rc, branch, _ = _git(main_root, "rev-parse", "--abbrev-ref", "HEAD")
    if rc != 0 or branch != "main":
        print(f"ABORT: integration tree is on '{branch}', not main ({main_root})")
        return 2

    rc, out, err = _git(main_root, "status", "--porcelain")
    if rc != 0:
        print(f"ABORT: git status failed: {err}")
        return 2
    tracked, untracked = [], []
    for line in out.splitlines():
        if not line.strip():
            continue
        code, path = line[:2], line[3:]
        if " -> " in path:
            path = path.split(" -> ")[-1]
        (untracked if code == "??" else tracked).append((code, path))

    buckets = collections.defaultdict(list)
    for code, path in tracked:
        buckets[classify(path)].append(path)
    adopt = [p for _, p in untracked if adoptable(p)]
    leave = [p for _, p in untracked if not adoptable(p)]

    rc, ahead, _ = _git(main_root, "rev-list", "--count", "origin/main..main")
    receipt = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "dry_run": a.dry_run,
        "tracked_dirty": len(tracked),
        "generated_index": len(buckets["generated-index"]),
        "state_receipt": len(buckets["state/receipt"]),
        "unclassified": buckets["UNCLASSIFIED"],
        "adopted_untracked": adopt,
        "left_untracked": leave,
        "main_ahead_of_origin_before": int(ahead or 0),
        "committed": None,
        "pushed": False,
    }

    print(f"main: {main_root}")
    print(f"tracked dirty: {len(tracked)}  → generated-index {len(buckets['generated-index'])} · "
          f"state/receipt {len(buckets['state/receipt'])} · UNCLASSIFIED {len(buckets['UNCLASSIFIED'])}")
    print(f"untracked: {len(untracked)}  → adopt {len(adopt)} · leave {len(leave)}")
    for p in leave:
        print(f"   leave untracked: {p}")

    if buckets["UNCLASSIFIED"]:
        print("\nABORT — these tracked changes are not generated/state. A human decides them:")
        for p in buckets["UNCLASSIFIED"]:
            print(f"   ? {p}")
        _write_receipt(main_root, receipt)
        return 2

    if not tracked and not adopt:
        print("main is already clean — nothing to absorb")
        _write_receipt(main_root, receipt)
        return 0

    writer = wl.fresh_main_writer(main_root, exclude_ids=wl._lane_session_ids(main_root))
    if writer:
        print(f"\nABORT — main has a fresh writer: {writer}. Integration is theirs right now.")
        receipt["blocked_by_writer"] = str(writer)
        _write_receipt(main_root, receipt)
        return 3

    if a.dry_run:
        print("\nDRY RUN — would commit the above as chore(main): absorb scheduled-maintenance drift")
        _write_receipt(main_root, receipt)
        return 0

    # The receipt is operational state (gitignored, like lane-reconciler.json). If an
    # earlier run adopted it into tracking, drop it from the index in this commit —
    # otherwise the receipt written after every run re-dirties main (2026-09-02).
    rc, tracked_receipt, _ = _git(main_root, "ls-files", "--error-unmatch", "--", str(RECEIPT_REL))
    if rc == 0 and tracked_receipt:
        _git(main_root, "rm", "--cached", "-q", "--", str(RECEIPT_REL))

    # Stage: tracked modifications/deletions (-u touches only tracked paths) + adopted untracked.
    rc, _, err = _git(main_root, "add", "-u", "--", ".")
    if rc != 0:
        print(f"ABORT: git add -u failed: {err}")
        return 2
    if adopt:
        rc, _, err = _git(main_root, "add", "--", *adopt)
        if rc != 0:
            print(f"ABORT: git add (adopt) failed: {err}")
            return 2

    msg = (f"chore(main): absorb scheduled-maintenance drift "
           f"({len(tracked)} tracked · {len(adopt)} minted) — unblocks lane merges\n\n"
           f"generated-index {len(buckets['generated-index'])} · state/receipt {len(buckets['state/receipt'])} · "
           f"UNCLASSIFIED 0. Written by scheduled jobs on the integration tree; no human authoring.\n"
           f"Receipt: {RECEIPT_REL}\n\n"
           f"Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>")
    rc, _, err = _git(main_root, "commit", "-q", "-m", msg)
    if rc != 0:
        print(f"ABORT: commit failed: {err}")
        return 2
    rc, sha, _ = _git(main_root, "rev-parse", "--short", "HEAD")
    receipt["committed"] = sha
    print(f"\nCOMMITTED {sha} on main")

    if a.push:
        rc, out, err = _git(main_root, "push", "origin", "main", timeout=300)
        receipt["pushed"] = rc == 0
        print("PUSHED main → origin" if rc == 0 else f"push failed: {err[:300]}")

    _write_receipt(main_root, receipt)
    if a.json:
        print(json.dumps(receipt, indent=2))
    return 0


def _write_receipt(main_root: Path, receipt: dict) -> None:
    try:
        p = main_root / RECEIPT_REL
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(receipt, indent=2))
    except OSError:
        pass


if __name__ == "__main__":
    raise SystemExit(main())
