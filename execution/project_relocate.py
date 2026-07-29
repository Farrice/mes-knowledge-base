#!/usr/bin/env python3
"""project_relocate.py — move a whole project directory WITH its inbound links.

`project_filer.py` files loose files *inside* a project. Nothing moved a project
*directory*, so the only way to do it was a bare `mv` — which
`directives/artifact-placement.md` forbids, because it orphans every inbound
reference. This closes that gap.

Unlike project_filer, this DOES rewrite control-plane referrers (CLAUDE.md,
.agent/workflows/, skills/, execution/). It has to: when a directory moves, a
hardcoded project path in CLAUDE.md is not a pin to respect, it is a broken
path. Every rewrite is listed before it happens and recorded in a receipt.

(Deliberately no literal project path appears in this file — it would make the
tool a referrer to its own examples and rewrite its own documentation.)

Usage:
  python3 execution/project_relocate.py plan  <src-rel> <dst-rel>
  python3 execution/project_relocate.py apply <src-rel> <dst-rel> [--stub]

  --stub   leave a pointer file at the old location (for archive moves, so a
           grep still finds where the work went). Never used for live moves.

Safety contract, same as project_filer:
  * `plan` writes nothing.
  * `apply` uses `git mv` (history preserved), rewrites every referrer,
    appends an inverse to .agent/organization/REVERT-<date>.sh, and writes a
    receipt to .agent/organization/receipts/.
  * Nothing is ever deleted.
  * Refuses if the destination exists.
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORG_HOME = ROOT / ".agent" / "organization"
RECEIPTS = ORG_HOME / "receipts"

# Never rewrite inside these: frozen historical records and machine ledgers whose
# whole purpose is to remember the OLD path.
FROZEN = (
    "_system/organization/inbox/",
    "_system/organization/backlog-maps/",
    "_system/organization/manifest.json",
    "_system/organization/move-ledger.jsonl",
    "_system/organization/aliases.json",
    ".agent/organization/receipts/",
    ".agent/organization/REVERT-",
    ".git/",
)

TEXT_SUFFIXES = {".md", ".py", ".json", ".jsonl", ".js", ".ts", ".tsx", ".yml",
                 ".yaml", ".txt", ".sh", ".html", ".toml", ".cfg"}


def _git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def find_referrers(needle: str) -> list[Path]:
    """Every tracked-or-untracked text file mentioning the old path."""
    out = _git("grep", "-I", "-l", "-F", "--untracked", needle).stdout
    hits = []
    for line in out.splitlines():
        if not line.strip():
            continue
        if any(line.startswith(f) or f in line for f in FROZEN):
            continue
        p = ROOT / line
        if p.is_file() and (p.suffix.lower() in TEXT_SUFFIXES or not p.suffix):
            hits.append(p)
    # The user-memory dir lives outside the repo; project_filer rewrites it too.
    mem = Path.home() / ".claude" / "projects" / "-Users-farricecain-Google-Antigravity" / "memory"
    if mem.is_dir():
        r = subprocess.run(["grep", "-rIlF", needle, str(mem)],
                           capture_output=True, text=True)
        hits += [Path(l) for l in r.stdout.splitlines() if l.strip()]
    return sorted(set(hits))


def rewrite(path: Path, src_rel: str, dst_rel: str) -> int:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return 0
    if src_rel not in text:
        return 0
    n = text.count(src_rel)
    path.write_text(text.replace(src_rel, dst_rel), encoding="utf-8")
    return n


def build(src_rel: str, dst_rel: str) -> dict:
    src, dst = ROOT / src_rel, ROOT / dst_rel
    if not src.is_dir():
        raise SystemExit(f"source is not a directory: {src_rel}")
    if dst.exists():
        raise SystemExit(f"destination already exists, refusing: {dst_rel}")
    referrers = find_referrers(src_rel)
    control = [p for p in referrers
               if any(str(p.relative_to(ROOT) if ROOT in p.parents else p).startswith(c)
                      for c in ("CLAUDE.md", "AGENTS.md", "CODEX.md", "GEMINI.md",
                                "OPERATING_MANUAL.md", "directives/", "execution/",
                                "skills/", ".agent/workflows/", ".claude/"))]
    return {
        "producer": "project_relocate.py",
        "schema": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "src": src_rel, "dst": dst_rel,
        "files_in_project": sum(1 for _ in src.rglob("*") if _.is_file()),
        "referrers": [str(p) for p in referrers],
        "control_referrers": [str(p) for p in control],
    }


def apply(plan: dict, stub: bool) -> dict:
    if plan.get("producer") != "project_relocate.py":
        raise SystemExit("plan not produced by project_relocate.py — refusing")
    src_rel, dst_rel = plan["src"], plan["dst"]
    src, dst = ROOT / src_rel, ROOT / dst_rel
    if dst.exists():
        raise SystemExit(f"destination appeared, refusing: {dst_rel}")

    dst.parent.mkdir(parents=True, exist_ok=True)
    r = _git("mv", src_rel, dst_rel)
    if r.returncode != 0:  # untracked dirs aren't git-movable; fall back
        import shutil
        shutil.move(str(src), str(dst))
        moved_by = "shutil (untracked)"
    else:
        moved_by = "git mv"

    # Inverse FIRST, before the rewrite phase, so a crash mid-rewrite is still
    # undoable (the 2026-07-08 lesson).
    ORG_HOME.mkdir(parents=True, exist_ok=True)
    rev = ORG_HOME / f"REVERT-{date.today().isoformat()}.sh"
    prior = rev.read_text(encoding="utf-8").splitlines() if rev.exists() else []
    body = [l for l in prior if l and not l.startswith("#!")]
    rev.write_text("\n".join(
        ["#!/bin/sh", "# Auto-generated inverse moves (newest first). Re-run to revert.", "",
         f'mv -n "{dst}" "{src}"'] + body) + "\n", encoding="utf-8")
    rev.chmod(0o755)

    rewrites = {}
    for ref in plan["referrers"]:
        p = Path(ref)
        if not p.exists():
            continue
        n = rewrite(p, src_rel, dst_rel)
        if n:
            rewrites[str(p)] = n

    if stub:
        src.mkdir(parents=True, exist_ok=True)
        (src / "MOVED.md").write_text(
            f"# Moved\n\nThis project now lives at `{dst_rel}`.\n\n"
            f"Relocated {date.today().isoformat()} by the global org sweep. "
            f"Nothing was deleted — the full contents moved intact.\n",
            encoding="utf-8")

    receipt = {
        "version": 1, "applied_at": datetime.now(timezone.utc).isoformat(),
        "action": "project-relocate", "moved_by": moved_by,
        "src": src_rel, "dst": dst_rel, "stub_left": stub,
        "files_moved": plan["files_in_project"],
        "rewrites": rewrites, "total_rewrites": sum(rewrites.values()),
        "revert_script": str(rev),
    }
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    rp = RECEIPTS / f"{date.today().isoformat()}-relocate-{Path(dst_rel).name.replace(' ', '_')}.json"
    rp.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    receipt["receipt_path"] = str(rp)

    with (ROOT / "_system" / "organization" / "move-ledger.jsonl").open("a") as fh:
        fh.write(json.dumps({"action": "project-relocate",
                             "moved_at": receipt["applied_at"],
                             "from": src_rel, "to": dst_rel,
                             "tool": "project_relocate.py"}) + "\n")
    return receipt


def verify(src_rel: str, dst_rel: str) -> dict:
    """Zero live references to the old path (frozen ledgers excluded)."""
    stale = [str(p.relative_to(ROOT)) if ROOT in p.parents else str(p)
             for p in find_referrers(src_rel)]
    return {"stale_referrers": stale, "ok": not stale,
            "destination_exists": (ROOT / dst_rel).is_dir()}


def main() -> int:
    if len(sys.argv) < 4:
        print(__doc__)
        return 1
    cmd, src_rel, dst_rel = sys.argv[1], sys.argv[2].rstrip("/"), sys.argv[3].rstrip("/")

    if cmd == "plan":
        plan = build(src_rel, dst_rel)
        print(json.dumps(plan, indent=2))
        return 0
    if cmd == "apply":
        plan = build(src_rel, dst_rel)
        receipt = apply(plan, stub="--stub" in sys.argv)
        print(json.dumps(receipt, indent=2))
        return 0
    if cmd == "verify":
        v = verify(src_rel, dst_rel)
        print(json.dumps(v, indent=2))
        return 0 if v["ok"] else 1
    print(f"unknown command: {cmd}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
