#!/usr/bin/env python3
"""Lane reconciler — the sprinkler for the worktree-lane smoke alarm.

WHY (Farrice, 2026-08-08): the harness already DETECTED stranded lanes
(concurrent_session_alarm, divergence_alarm) and already PROVISIONED them
(worktree_lane bootstrap). Nothing CLOSED the loop. Sessions get abandoned
mid-flight — "the end session doesn't run because I forget to, or I'm moving
too quickly" — and work sat on branches main could not see. 274 files across
3 lanes, oldest 19h, on the day this was built.

This runs on a cadence (launchd, hourly) and does the hygiene the operator
should not have to remember:

  empty lane      -> tear the worktree down
  clean lane      -> merge it back to main via worktree_lane.py
  conflicted lane -> leave it ALONE, record exactly which files collide
  blocked lane    -> leave it ALONE, record why (dirty main / fresh writer)

LOSS-PROOF BY CONSTRUCTION — the binding constraint is "I don't want to lose
stuff":
  * never --force, never teardown a lane that is ahead of main
  * never teardown a lane with uncommitted changes
  * never resolve a conflict; conflicts are surfaced, never guessed
  * all merging delegates to worktree_lane.py merge, which carries the Law-3
    AUDITSET (proves every file the branch added actually landed) and parks
    instead of forcing

Receipt: .agent/health/lane-reconciler.json  (read by the pulse board + the
SessionStart alarm, so the state is deterministic, never AI memory —
feedback_ai-memory-dependent-observability).

Usage:
    python3 execution/lane_reconciler.py            # reconcile
    python3 execution/lane_reconciler.py --dry-run  # report only, touch nothing
    python3 execution/lane_reconciler.py --json     # machine-readable
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LANE_TOOL = REPO / "execution" / "worktree_lane.py"
RECEIPT = REPO / ".agent" / "health" / "lane-reconciler.json"
TIMEOUT = 180


def git(*args: str, cwd: Path = REPO) -> tuple[int, str]:
    p = subprocess.run(["git", "-C", str(cwd), *args],
                       capture_output=True, text=True, timeout=TIMEOUT)
    return p.returncode, (p.stdout or "").strip()


def lanes() -> list[dict]:
    """Every lane worktree_lane knows about, with its branch and path."""
    rc, out = git("worktree", "list", "--porcelain")
    if rc != 0:
        return []
    found, cur = [], {}
    for line in out.splitlines():
        if line.startswith("worktree "):
            cur = {"path": line[9:]}
        elif line.startswith("branch "):
            cur["branch"] = line[7:].replace("refs/heads/", "")
        elif not line.strip() and cur:
            found.append(cur)
            cur = {}
    if cur:
        found.append(cur)
    # the main tree is not a lane
    return [w for w in found
            if w.get("branch") and w["branch"] != "main"
            and Path(w["path"]).resolve() != REPO.resolve()]


def commits_ahead(branch: str) -> int:
    rc, out = git("rev-list", "--count", f"main..{branch}")
    return int(out) if rc == 0 and out.isdigit() else 0


def merge_probe(branch: str) -> tuple[list[str], str]:
    """Probe a merge without touching a worktree or writing repo objects.

    ``git merge-tree --write-tree`` needs an object database even though it
    never changes refs. Codex's normal sandbox cannot write ``.git/objects``;
    an unchecked failure there previously looked identical to a clean merge.
    Use a temporary object database backed by the repository's objects and
    fail closed when Git cannot complete the probe.
    """
    rc, object_path = git("rev-parse", "--git-path", "objects")
    if rc != 0 or not object_path:
        return [], "cannot resolve Git object directory"
    objects = Path(object_path)
    if not objects.is_absolute():
        objects = (REPO / objects).resolve()

    with tempfile.TemporaryDirectory(prefix="lane-reconciler-objects-") as temp_objects:
        env = os.environ.copy()
        env["GIT_OBJECT_DIRECTORY"] = temp_objects
        alternates = [str(objects)]
        if env.get("GIT_ALTERNATE_OBJECT_DIRECTORIES"):
            alternates.append(env["GIT_ALTERNATE_OBJECT_DIRECTORIES"])
        env["GIT_ALTERNATE_OBJECT_DIRECTORIES"] = os.pathsep.join(alternates)
        p = subprocess.run(
            ["git", "-C", str(REPO), "merge-tree", "--write-tree", "main", branch],
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
            env=env,
        )
    blob = (p.stdout or "") + (p.stderr or "")
    conflicts: set[str] = set()
    for line in blob.splitlines():
        if "Merge conflict in " in line:
            conflicts.add(line.split("Merge conflict in ", 1)[1].strip())
            continue
        if not line.startswith("CONFLICT "):
            continue
        match = re.search(
            r"CONFLICT \([^)]+\): (.+?)(?: deleted in | renamed to | added in |$)",
            line,
        )
        if match:
            conflicts.add(match.group(1).strip())

    if p.returncode and not conflicts:
        detail = next((line.strip() for line in reversed(blob.splitlines()) if line.strip()), "")
        return [], detail or f"merge-tree failed with exit {p.returncode}"
    return sorted(conflicts), ""


def worktree_dirty(path: str) -> int:
    wt = Path(path)
    if not wt.exists():
        return 0
    rc, out = git("status", "--porcelain", cwd=wt)
    if rc != 0:
        return 0
    return len([l for l in out.splitlines() if l.strip() and not l.startswith("??")])


def run_lane_tool(*args: str) -> tuple[int, str]:
    p = subprocess.run([sys.executable, str(LANE_TOOL), *args],
                       capture_output=True, text=True, timeout=600, cwd=str(REPO))
    return p.returncode, ((p.stdout or "") + (p.stderr or "")).strip()


def reconcile(dry_run: bool = False) -> dict:
    results = []
    for lane in lanes():
        branch, path = lane["branch"], lane["path"]
        ahead = commits_ahead(branch)
        dirty = worktree_dirty(path)
        row = {"branch": branch, "path": path, "commits_ahead": ahead,
               "dirty_files": dirty, "conflicts": [], "probe_error": "",
               "action": "", "detail": ""}

        # --- empty lane: nothing ahead, nothing uncommitted -> reclaim it ------
        if ahead == 0 and dirty == 0:
            row["action"] = "would-teardown" if dry_run else "torn-down"
            if not dry_run:
                rc, out = run_lane_tool("merge", "--lane", branch)
                row["detail"] = out.splitlines()[-1] if out else f"rc={rc}"
                if rc != 0:
                    row["action"] = "teardown-failed"
            else:
                row["detail"] = "empty lane — worktree reclaimable"
            results.append(row)
            continue

        # --- a lane with uncommitted work is a LIVE lane: never touch ----------
        if dirty:
            row["action"] = "skipped-live"
            row["detail"] = f"{dirty} uncommitted file(s) — a session is still working here"
            results.append(row)
            continue

        # --- probe before acting ---------------------------------------------
        row["conflicts"], row["probe_error"] = merge_probe(branch)
        if row["probe_error"]:
            row["action"] = "parked-probe-error"
            row["detail"] = f"merge safety probe failed — {row['probe_error']}"
            results.append(row)
            continue
        if row["conflicts"]:
            row["action"] = "parked-conflict"
            row["detail"] = f"{len(row['conflicts'])} file(s) collide — needs resolution"
            results.append(row)
            continue

        # --- clean: delegate to the Law-3 audited merge ------------------------
        if dry_run:
            row["action"] = "would-merge"
            row["detail"] = f"{ahead} commit(s) merge clean"
        else:
            rc, out = run_lane_tool("merge", "--lane", branch)
            last = out.splitlines()[-1] if out else ""
            if rc == 0 and "LANE MERGED" in out:
                row["action"] = "merged"
            else:
                # worktree_lane parks on dirty main / fresh writer / audit fail
                row["action"] = "parked-blocked"
            row["detail"] = last
        results.append(row)

    stranded = sum(r["commits_ahead"] for r in results
                   if r["action"].startswith(("parked", "skipped")))
    receipt = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "dry_run": dry_run,
        "lanes": len(results),
        "merged": sum(1 for r in results if r["action"] == "merged"),
        "torn_down": sum(1 for r in results if r["action"] == "torn-down"),
        "parked": sum(1 for r in results if r["action"].startswith("parked")),
        "live": sum(1 for r in results if r["action"] == "skipped-live"),
        "stranded_commits": stranded,
        "results": results,
    }
    if not dry_run:
        RECEIPT.parent.mkdir(parents=True, exist_ok=True)
        RECEIPT.write_text(json.dumps(receipt, indent=2))
    return receipt


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would happen; touch nothing")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    r = reconcile(dry_run=args.dry_run)

    if args.json:
        print(json.dumps(r, indent=2))
        return 0

    if not r["results"]:
        print("LANES: none — nothing to reconcile.")
        return 0

    tag = "[dry-run] " if args.dry_run else ""
    for row in r["results"]:
        line = f"{tag}{row['action']:<16} {row['branch']:<46} {row['detail']}"
        print(line)
        for f in row["conflicts"][:8]:
            print(f"{' ' * 19}└─ {f}")
        if len(row["conflicts"]) > 8:
            print(f"{' ' * 19}└─ … +{len(row['conflicts']) - 8} more")

    print(f"\n{tag}{r['lanes']} lane(s): {r['merged']} merged · {r['torn_down']} reclaimed "
          f"· {r['parked']} parked · {r['live']} live "
          f"· {r['stranded_commits']} commit(s) still stranded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
