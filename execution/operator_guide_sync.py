#!/usr/bin/env python3
"""operator_guide_sync.py — deterministic detector for the Root-Core Operator Guide.

The guide (docs/ROOT-CORE-OPERATOR-GUIDE.md) is the operator's source of truth
for how to run what we build. It must never depend on the model remembering to
update it (AI-memory-dependent observability is banned). This script is the
deterministic half of the loop:

    check   — list operator assets changed/created since the last sync stamp
              (git diff vs stamp commit + working-tree changes). Exit 1 with a
              prefilled /operator-guide-sync prompt when an update is due.
    record  — stamp the current HEAD + timestamp after the guide is updated.

The model half is .agent/workflows/operator-guide-sync.md, which reads this
delta and updates the guide surgically (per-asset sections, never wholesale
regeneration). Wired into end_session_closeout.py as a nudge step.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / ".agent" / "operator-guide-state.json"
GUIDE = "docs/ROOT-CORE-OPERATOR-GUIDE.md"

# Paths whose changes mean "operator surface changed" — new/updated ways to
# run things. The detector over-reports on purpose; the sync workflow judges
# relevance (telemetry-only edits are ignored there, not here).
ASSET_PATTERNS = [
    ".agent/workflows/*.md",
    "skills/*/SKILL.md",
    "skills/*/workflows/*.md",
    "directives/*.md",
    "docs/agents/*.md",
    "docs/solutions/*.md",
]
EXCLUDE = {GUIDE}


def _git(*args: str) -> str:
    r = subprocess.run(
        ["git", *args], capture_output=True, text=True, cwd=str(ROOT), timeout=30
    )
    return r.stdout if r.returncode == 0 else ""


def _matches(path: str) -> bool:
    if path in EXCLUDE:
        return False
    return any(fnmatch.fnmatch(path, pat) for pat in ASSET_PATTERNS)


def _load_state() -> dict:
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _sha1(path: Path) -> str:
    import hashlib

    try:
        return hashlib.sha1(path.read_bytes()).hexdigest()
    except Exception:
        return ""


def _pending_assets() -> list[str]:
    state = _load_state()
    paths: set[str] = set()

    stamp = state.get("last_synced_commit")
    if stamp:
        for line in _git("diff", "--name-only", f"{stamp}..HEAD").splitlines():
            if line.strip():
                paths.add(line.strip())

    # Working tree: modified + untracked, so uncommitted session work counts.
    for line in _git("status", "--porcelain").splitlines():
        if len(line) > 3:
            p = line[3:].strip().strip('"')
            if p.endswith("/"):
                for f in (ROOT / p).rglob("*.md"):
                    paths.add(str(f.relative_to(ROOT)))
            else:
                paths.add(p)

    # A path already synced at its current content is not pending — this is
    # what lets uncommitted-but-synced work go quiet until it changes again.
    synced: dict = state.get("synced_hashes", {})
    out = []
    for p in sorted(paths):
        if not _matches(p):
            continue
        if synced.get(p) and synced[p] == _sha1(ROOT / p):
            continue
        out.append(p)
    return out


def cmd_check(plain: bool) -> int:
    pending = _pending_assets()
    state = _load_state()
    last = state.get("last_synced_at", "never")
    if not pending:
        print(f"OPERATOR GUIDE current (last synced: {last})")
        return 0
    shown = pending[:20]
    print(f"OPERATOR GUIDE UPDATE DUE — {len(pending)} operator asset(s) changed since last sync ({last}):")
    for p in shown:
        print(f"  - {p}")
    if len(pending) > len(shown):
        print(f"  … and {len(pending) - len(shown)} more")
    print("Run: /operator-guide-sync   (updates docs/ROOT-CORE-OPERATOR-GUIDE.md surgically, then stamps)")
    return 1


def cmd_record() -> int:
    head = _git("rev-parse", "HEAD").strip()
    # Snapshot content hashes of every currently-pending working-tree asset so
    # uncommitted-but-synced files stop re-triggering until they change again.
    hashes: dict = {}
    prior = _load_state()
    prior_hashes = prior.get("synced_hashes", {})
    STATE.parent.mkdir(parents=True, exist_ok=True)
    for line in _git("status", "--porcelain").splitlines():
        if len(line) > 3:
            p = line[3:].strip().strip('"')
            candidates = (
                [str(f.relative_to(ROOT)) for f in (ROOT / p).rglob("*.md")]
                if p.endswith("/")
                else [p]
            )
            for c in candidates:
                if _matches(c):
                    hashes[c] = _sha1(ROOT / c)
    state = {
        "last_synced_commit": head or None,
        "last_synced_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "guide": GUIDE,
        "synced_hashes": {**{k: v for k, v in prior_hashes.items() if (ROOT / k).exists()}, **hashes},
    }
    STATE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    print(f"OPERATOR GUIDE stamped at {state['last_synced_at']} (commit {head[:9] if head else 'n/a'}, {len(hashes)} working-tree asset(s) snapshotted)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic detector for the Root-Core Operator Guide")
    sub = ap.add_subparsers(dest="command", required=True)
    cp = sub.add_parser("check", help="Exit 1 + asset list when a guide update is due")
    cp.add_argument("--plain", action="store_true", help="(reserved) plain output")
    sub.add_parser("record", help="Stamp HEAD + now as the last synced point")
    args = ap.parse_args()
    if args.command == "check":
        return cmd_check(getattr(args, "plain", False))
    if args.command == "record":
        return cmd_record()
    return 0


if __name__ == "__main__":
    sys.exit(main())
