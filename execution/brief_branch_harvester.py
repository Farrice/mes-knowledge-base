#!/usr/bin/env python3
"""
brief_branch_harvester.py — land remote `brief/*` branch work into main, file-level.

WHY (apex W0.2, 2026-07-29): the daily GEO-brief cloud routine pushes each day's
brief to `origin/brief/<date>`. That half is CORRECT — a remote job should not
write main. The missing half was the harvester: nothing ever landed the branches,
so 7 days (~1,827 lines) of finished briefs sat invisible while the automation
degraded its own output ("no daily brief exists for 07-22..07-26" — its words).

Method (merge-discipline compliant):
  - NEVER merge — brief branches sit on bases hundreds of thousands of deletions
    stale; file-level `git show` is the only safe recovery (Law 3 spirit).
  - Recover: `_active/**/daily/*.md` + `.agent/handoffs/*.md` that main lacks;
    JSONL ledgers (insights, content-finish-log) are dedupe-MERGED, never replaced.
  - Skips shared mutable state the branch also touched (routing-intelligence.json,
    handoffs/index.md, LATEST.md) — main's copy is newer by definition.
  - --prune deletes a remote branch ONLY after every recoverable file is verified
    present in main (committed), per merge-discipline Law 3 ("recover first").
  - Exit 0 always when run with --quiet (cron-safe); prints nothing when clean.

Usage:
  python3 execution/brief_branch_harvester.py            # report + recover, no prune
  python3 execution/brief_branch_harvester.py --prune    # recover, verify, prune landed branches
  python3 execution/brief_branch_harvester.py --dry-run  # report only
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Files harvested by copy-if-absent (the branch's unique deliverables).
HARVEST_PREFIXES = ("_active/", ".agent/handoffs/")
HARVEST_SUFFIX = ".md"
# JSONL files merged row-wise with dedupe.
MERGE_JSONL = (
    "_active/health-performance-ip-library/ledger/insights.jsonl",
    ".agent/content-finish-log.jsonl",
)
# Shared mutable state: never harvested (main is authoritative).
SKIP_NAMES = ("LATEST.md", "index.md")


def git(*args: str) -> str:
    p = subprocess.run(["git", *args], capture_output=True, text=True, cwd=ROOT)
    return p.stdout


def brief_branches() -> list[str]:
    out = git("branch", "-r", "--format=%(refname:short)")
    return [b.strip() for b in out.splitlines()
            if b.strip().startswith("origin/brief/") and not b.endswith("/HEAD")]


def unique_files(branch: str) -> list[str]:
    out = git("diff", "main..." + branch, "--name-only")
    return [f for f in out.splitlines() if f.strip()]


def merge_jsonl(branch: str, rel: str) -> int:
    """Dedupe-merge a branch's JSONL rows into main's file. Returns rows added."""
    branch_txt = git("show", f"{branch}:{rel}")
    if not branch_txt.strip():
        return 0
    path = ROOT / rel
    main_rows = [l for l in path.read_text().splitlines() if l.strip()] if path.exists() else []
    seen = set(main_rows)
    added = 0
    for l in branch_txt.splitlines():
        if l.strip() and l not in seen:
            main_rows.append(l)
            seen.add(l)
            added += 1
    if added:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(main_rows) + "\n")
    return added


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prune", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    git("fetch", "origin", "--quiet")
    report, recovered_any = [], False

    for branch in brief_branches():
        files = unique_files(branch)
        if not files:
            if args.prune and not args.dry_run:
                git("push", "origin", "--delete", branch.removeprefix("origin/"))
                report.append(f"pruned (nothing unique): {branch}")
            continue
        landed, pending = [], []
        for rel in files:
            name = Path(rel).name
            if rel in MERGE_JSONL:
                if not args.dry_run:
                    n = merge_jsonl(branch, rel)
                    if n:
                        landed.append(f"{rel} (+{n} rows)")
                        recovered_any = True
                continue
            if name in SKIP_NAMES or not rel.startswith(HARVEST_PREFIXES) \
                    or not rel.endswith(HARVEST_SUFFIX):
                continue  # shared state or out-of-charter — main wins
            dest = ROOT / rel
            if dest.exists():
                continue  # already in main (recovered earlier or parallel run)
            if not args.dry_run:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(git("show", f"{branch}:{rel}"))
                landed.append(rel)
                recovered_any = True
        # verify: every harvestable file now present in main?
        for rel in files:
            name = Path(rel).name
            if rel in MERGE_JSONL or name in SKIP_NAMES:
                continue
            if rel.startswith(HARVEST_PREFIXES) and rel.endswith(HARVEST_SUFFIX) \
                    and not (ROOT / rel).exists():
                pending.append(rel)
        if landed:
            report.append(f"{branch}: landed {len(landed)} — " + "; ".join(landed[:3]))
        if args.prune and not pending and not args.dry_run:
            # Everything recoverable is on disk. Caller commits before prune —
            # refuse to prune with a dirty harvest (uncommitted recovery).
            dirty = git("status", "--porcelain").strip()
            if dirty:
                report.append(f"prune SKIPPED (uncommitted harvest): {branch}")
            else:
                git("push", "origin", "--delete", branch.removeprefix("origin/"))
                report.append(f"pruned (recovered + committed): {branch}")
        elif pending:
            report.append(f"{branch}: NOT pruned — unrecovered: {pending[:3]}")

    if report and not args.quiet:
        print("BRIEF HARVEST (deterministic, from brief_branch_harvester.py):")
        for r in report:
            print(f"  {r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
