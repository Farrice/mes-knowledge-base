#!/usr/bin/env python3
"""platform_compiler.py — keep per-platform constitutions honest and in sync.

The system runs on multiple agent platforms, each reading its own constitution:
    Claude Code      -> CLAUDE.md                      (canon, hand-authored)
    Gemini surfaces  -> GEMINI.md                      (derived sibling)
    Codex            -> AGENTS.md                      (derived sibling, self-contained)
    Antigravity IDE  -> .agent/rules/constitution.md   (derived sibling, distilled)

v1 is deliberately read-only on constitutions: it detects drift and lints
invariants; it never rewrites a working file. (v2 may generate siblings from
canon + overlays.)

Commands:
    check   exit 1 if any tracked file changed since the last bless (sync)
    lint    exit 1 if any portability invariant is violated
    sync    bless current state (writes .agent/platform_hashes.json)
    forks   report known fork locations and their staleness (informational)
    report  human summary of check + lint + forks (exit 1 if check/lint fail)

Wired into evolution_orchestrator.run_daily() as an observe-only report section.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HASH_STORE = ROOT / ".agent" / "platform_hashes.json"

TRACKED = [
    "CLAUDE.md",
    "GEMINI.md",
    "AGENTS.md",
    ".agent/rules/constitution.md",
    ".gemini/settings.json",
    ".codex/config.toml",
]

CANON = "CLAUDE.md"

CANARIES = {
    "GEMINI.md": "ANTIGRAVITY-GEMINI-7X4K",
    "AGENTS.md": "ANTIGRAVITY-CODEX-3J8R",
    ".agent/rules/constitution.md": "ANTIGRAVITY-IDE-9Q2M",
}

# Gemini drops early-placed constraints; CRITICAL block must sit in the
# final third of every derived constitution.
CONSTRAINTS_LAST = ["GEMINI.md", "AGENTS.md", ".agent/rules/constitution.md"]
CONSTRAINTS_MARKER = "## CRITICAL"
CONSTRAINTS_MIN_OFFSET = 0.60

GEMINI_MAX_CHARS = 15_000

# Internal paths referenced by constitutions must exist (broken pointers were
# a root cause of the failed ports).
REF_PATTERN = re.compile(
    r"`((?:directives|execution|skills|\.agent|\.gemini)/[A-Za-z0-9_\-./]+\.(?:md|py|json))`"
)

# Active Opus pins caused "model not available" stalls. Archived agents are exempt.
OPUS_SCAN_GLOBS = [".claude/agents/**/*.md", "agents/**/AGENT.md"]
OPUS_PIN = re.compile(r"^\s*model:\s*.*opus", re.IGNORECASE)

KNOWN_FORKS = [
    Path.home() / "Codex Antigravity",
    Path.home() / ".codex" / "skills",
    Path.home() / ".gemini" / "antigravity" / "knowledge",
]


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _current_hashes() -> dict:
    out = {}
    for rel in TRACKED:
        p = ROOT / rel
        out[rel] = _sha(p) if p.exists() else "MISSING"
    return out


def cmd_sync() -> int:
    HASH_STORE.parent.mkdir(parents=True, exist_ok=True)
    HASH_STORE.write_text(json.dumps({
        "blessed_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "hashes": _current_hashes(),
    }, indent=2) + "\n")
    print(f"Blessed {len(TRACKED)} files -> {HASH_STORE.relative_to(ROOT)}")
    return 0


def cmd_check(as_json: bool = False) -> int:
    if not HASH_STORE.exists():
        result = {"drifted": [], "error": "no baseline — run: python3 execution/platform_compiler.py sync"}
        print(json.dumps(result) if as_json else result["error"])
        return 1
    blessed = json.loads(HASH_STORE.read_text())["hashes"]
    current = _current_hashes()
    drifted = [rel for rel in TRACKED if blessed.get(rel) != current.get(rel)]
    result = {"drifted": drifted, "blessed_at": json.loads(HASH_STORE.read_text()).get("blessed_at")}
    if as_json:
        print(json.dumps(result))
        return 1 if drifted else 0
    if not drifted:
        print("In sync — all platform constitutions match the blessed baseline.")
        return 0
    print("PLATFORM DRIFT — files changed since last bless:")
    for rel in drifted:
        print(f"  - {rel}")
    if CANON in drifted:
        siblings = [f for f in CONSTRAINTS_LAST if f not in drifted]
        if siblings:
            print(f"  CLAUDE.md (canon) changed but these siblings did not: {', '.join(siblings)}")
            print("  Review whether the change must propagate before blessing.")
    print("After reviewing siblings: python3 execution/platform_compiler.py sync")
    return 1


def _lint_failures() -> list:
    fails = []

    for rel in TRACKED:
        if not (ROOT / rel).exists():
            fails.append(f"missing tracked file: {rel}")

    gemini = ROOT / "GEMINI.md"
    if gemini.exists() and len(gemini.read_text()) > GEMINI_MAX_CHARS:
        fails.append(f"GEMINI.md exceeds {GEMINI_MAX_CHARS} chars (Gemini context budget)")

    for rel, token in CANARIES.items():
        p = ROOT / rel
        if p.exists() and token not in p.read_text():
            fails.append(f"canary {token} missing from {rel}")

    for rel in CONSTRAINTS_LAST:
        p = ROOT / rel
        if not p.exists():
            continue
        text = p.read_text()
        idx = text.find(CONSTRAINTS_MARKER)
        if idx == -1:
            fails.append(f"{rel}: no '{CONSTRAINTS_MARKER}' block")
        elif idx < len(text) * CONSTRAINTS_MIN_OFFSET:
            fails.append(f"{rel}: CRITICAL block sits too early ({idx}/{len(text)} chars) — constraints go LAST")

    for rel in CONSTRAINTS_LAST:
        p = ROOT / rel
        if not p.exists():
            continue
        for ref in REF_PATTERN.findall(p.read_text()):
            if not (ROOT / ref).exists():
                fails.append(f"{rel}: references missing file {ref}")

    for pattern in OPUS_SCAN_GLOBS:
        for p in ROOT.glob(pattern):
            if "_archived" in p.parts:
                continue
            try:
                head = "".join(p.read_text().splitlines(keepends=True)[:20])
            except (UnicodeDecodeError, OSError):
                continue
            for i, line in enumerate(head.splitlines(), 1):
                if OPUS_PIN.match(line):
                    fails.append(f"active Opus pin: {p.relative_to(ROOT)}:{i} — never pin opus (capacity-flaky)")

    settings = ROOT / ".claude" / "settings.json"
    if settings.exists() and "opus" in settings.read_text().lower():
        fails.append('active Opus reference in .claude/settings.json')

    return fails


def cmd_lint() -> int:
    fails = _lint_failures()
    if not fails:
        print("Lint clean — all portability invariants hold.")
        return 0
    print(f"LINT FAILURES ({len(fails)}):")
    for f in fails:
        print(f"  - {f}")
    return 1


def cmd_forks() -> int:
    print("Known fork locations (informational — canonical system is THIS repo):")
    now = time.time()
    for fork in KNOWN_FORKS:
        if not fork.exists():
            print(f"  - {fork}: absent")
            continue
        newest = max((f.stat().st_mtime for f in fork.rglob("*") if f.is_file()), default=fork.stat().st_mtime)
        days = (now - newest) / 86_400
        flag = "  <-- ACTIVE, harvest/retire" if days < 7 else ""
        print(f"  - {fork}: newest file {days:.1f}d old{flag}")
    return 0


def cmd_report() -> int:
    print("=== platform_compiler report ===")
    rc_check = cmd_check()
    print()
    rc_lint = cmd_lint()
    print()
    cmd_forks()
    return 1 if (rc_check or rc_lint) else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Platform constitution drift + lint")
    sub = parser.add_subparsers(dest="cmd", required=True)
    chk = sub.add_parser("check")
    chk.add_argument("--json", action="store_true")
    sub.add_parser("lint")
    sub.add_parser("sync")
    sub.add_parser("forks")
    sub.add_parser("report")
    args = parser.parse_args()
    if args.cmd == "check":
        return cmd_check(as_json=args.json)
    return {"lint": cmd_lint, "sync": cmd_sync, "forks": cmd_forks, "report": cmd_report}[args.cmd]()


if __name__ == "__main__":
    sys.exit(main())
