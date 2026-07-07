#!/usr/bin/env python3
"""solution_recorder.py — deterministic layer of the Solution Recorder.

WHY: hard-won fixes (a bug chased through N failed Bash attempts, a root
cause finally nailed) evaporate at session end unless someone remembers to
write them down. That's the banned AI-memory-dependent pattern (see
feedback_ai-memory-dependent-observability.md). This script is the
deterministic scaffolding half of the fix — it gathers real evidence (no LLM
calls) and validates the resulting card before it counts as saved. The
drafting/writing itself stays a Claude/agent job; this script never invents
prose.

Card contract (shared with session_ledger_hook.py / chain_runner.py / the
prose-layer builder — do not change without updating all three):
    Location: docs/solutions/<YYYY-MM-DD>-<slug>.md
    Frontmatter: name, problem_signature, domain, tags, date, status, session
    Body H2s (exact, in order): Problem, Root Cause, Approach That Worked
    (numbered steps), Dead Ends, Verification, Weaker-Model Trap, Pointers
    Success marker: on a passing save this CLI prints the success marker
    ("SOLUTION CARD SAVED", then a colon, then the docs/solutions path) at
    line start — other hooks string-match that PRINTED line. The contiguous
    literal is deliberately kept out of this docstring so cat/grep on this
    source file can never satisfy a naive marker scan.

Usage:
    python3 execution/solution_recorder.py draft --slug <s> [--problem "<one line>"]
    python3 execution/solution_recorder.py save --file <path>
    python3 execution/solution_recorder.py check
    python3 execution/solution_recorder.py search "<query>"
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import yaml
except ImportError:
    if __name__ == "__main__":
        print("Need PyYAML: pip install pyyaml", file=sys.stderr)
        sys.exit(1)
    # Imported as a module (chain_runner / end_session_closeout guard on
    # ImportError, not SystemExit) — re-raise so their fallbacks engage.
    raise

ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS_DIR = ROOT / "docs" / "solutions"
SESSIONS_DIR = ROOT / ".agent" / "sessions"
RECEIPTS_DIR = ROOT / ".agent" / "run-receipts"

REQUIRED_H2 = [
    "## Problem",
    "## Root Cause",
    "## Approach That Worked",
    "## Dead Ends",
    "## Verification",
    "## Weaker-Model Trap",
    "## Pointers",
]

REQUIRED_FRONTMATTER_KEYS = ["name", "problem_signature", "domain", "tags", "date", "status"]

# Learning debt older than this can't block a finalize (Fix 2, 2026-07-07):
# in practice the active session's ledger is almost always the newest one,
# and the GOLDEN RULE forbids concurrent drivers — so a freshness window is
# the proportionate guard against a stale ledger's debt blocking a new
# session, without full session-scoping machinery.
LEARNING_DEBT_FRESH_HOURS = 4


def split_debt_freshness(entries, hours: float = LEARNING_DEBT_FRESH_HOURS):
    """Split learning_debt entries into (fresh, stale) by ts age.

    Shared by chain_runner's finalize latch, `check` here, and
    end_session_closeout's solution-cards step. Entries with an unparseable
    ts count as STALE — a debt that can't prove freshness can't block."""
    fresh, stale = [], []
    cutoff = datetime.now() - timedelta(hours=hours)
    for d in entries or []:
        try:
            ok = datetime.fromisoformat(str(d.get("ts", ""))) >= cutoff
        except Exception:
            ok = False
        (fresh if ok else stale).append(d)
    return fresh, stale

TEMPLATE = """---
name: {slug}
problem_signature: "{problem}"
domain: system
tags: []
date: {today}
status: active
session: ""
---

## Problem

<!-- fill -->

## Root Cause

<!-- fill -->

## Approach That Worked

1. <!-- fill -->
2. <!-- fill -->

## Dead Ends

<!-- fill -->

## Verification

<!-- fill -->

## Weaker-Model Trap

<!-- fill -->

## Pointers

<!-- fill -->
"""


# ──────────────────────────────────────────────────────────────────
# evidence gathering (draft)
# ──────────────────────────────────────────────────────────────────
def _newest_ledger() -> Tuple[Optional[Path], Optional[dict]]:
    if not SESSIONS_DIR.exists():
        return None, None
    candidates = sorted(SESSIONS_DIR.glob("ledger-*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not candidates:
        return None, None
    try:
        return candidates[0], json.loads(candidates[0].read_text(encoding="utf-8"))
    except Exception:
        return candidates[0], None


def _git_evidence() -> Dict[str, str]:
    evidence = {}
    for key, cmd in (
        ("diff_stat", ["git", "diff", "--stat"]),
        ("status_short", ["git", "status", "--short"]),
    ):
        try:
            r = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, timeout=15)
            evidence[key] = (r.stdout or "").strip()
        except Exception as exc:
            evidence[key] = f"(error: {exc})"
    return evidence


def _newest_receipts(n: int = 2) -> List[str]:
    if not RECEIPTS_DIR.exists():
        return []
    files = [p for p in RECEIPTS_DIR.glob("*.md") if p.name != "latest.md"]
    files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return [p.name for p in files[:n]]


def cmd_draft(args: argparse.Namespace) -> int:
    ledger_path, ledger = _newest_ledger()
    lines = ["EVIDENCE BUNDLE", "=" * 60]
    if ledger_path is not None:
        lines.append(f"Ledger: {ledger_path.name}")
        if ledger is not None:
            lines.append(f"  produced_paths: {ledger.get('produced_paths', [])}")
            lines.append(f"  debts: {ledger.get('debts', [])}")
            lines.append(f"  subagent_spawns: {ledger.get('subagent_spawns', 0)}")
            lines.append(f"  bash_fail_streak: {ledger.get('bash_fail_streak', 0)}")
            lines.append(f"  learning_debt: {ledger.get('learning_debt', [])}")
        else:
            lines.append("  (ledger file unreadable)")
    else:
        lines.append("Ledger: none found in .agent/sessions/")

    git_ev = _git_evidence()
    lines.append("")
    lines.append("git diff --stat:")
    lines.append(git_ev["diff_stat"] or "(empty)")
    lines.append("")
    lines.append("git status --short:")
    lines.append(git_ev["status_short"] or "(clean)")

    receipts = _newest_receipts()
    lines.append("")
    lines.append("Newest run-receipts:")
    lines.append(", ".join(receipts) if receipts else "(none)")

    print("\n".join(lines))
    print("\n" + "=" * 60)
    print("CARD TEMPLATE — fill every <!-- fill --> placeholder, save under")
    print(f"docs/solutions/{date.today().isoformat()}-{args.slug}.md, then run:")
    print(f"  python3 execution/solution_recorder.py save --file docs/solutions/{date.today().isoformat()}-{args.slug}.md")
    print("=" * 60 + "\n")

    problem = (args.problem or "<fill>").replace('"', "'")
    print(TEMPLATE.format(slug=args.slug, problem=problem, today=date.today().isoformat()))
    return 0


# ──────────────────────────────────────────────────────────────────
# frontmatter / section parsing (shared by save + index regen)
# ──────────────────────────────────────────────────────────────────
def _parse_frontmatter(text: str) -> Tuple[Optional[dict], str]:
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return None, text
    fm_text, body = m.group(1), m.group(2)
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError:
        return None, body
    if not isinstance(fm, dict):
        return None, body
    return fm, body


def _extract_sections(body: str) -> Dict[str, str]:
    sections: Dict[str, str] = {}
    matches = list(re.finditer(r"^## (.+)$", body, re.MULTILINE))
    for i, m in enumerate(matches):
        title = f"## {m.group(1).strip()}"
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        sections[title] = body[start:end].strip()
    return sections


# ──────────────────────────────────────────────────────────────────
# save (validate + regenerate index)
# ──────────────────────────────────────────────────────────────────
def _regenerate_index() -> None:
    rows: List[Tuple[str, str, str]] = []
    for p in sorted(SOLUTIONS_DIR.glob("*.md")):
        if p.name in ("index.md",):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except OSError:
            continue
        fm, _ = _parse_frontmatter(text)
        if not fm:
            continue
        rows.append((str(fm.get("date", "")), str(fm.get("name", p.stem)), str(fm.get("problem_signature", ""))))
    rows.sort(key=lambda r: r[0], reverse=True)
    lines = ["# Solution Cards Index", "", "One line per card: date · name · problem_signature.", ""]
    for d, name, sig in rows:
        lines.append(f"- {d} · {name} · {sig}")
    SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)
    (SOLUTIONS_DIR / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate_card(path) -> List[str]:
    """Validate a Solution Card file against the card contract.

    Returns [] when the card is valid, else EVERY violation found.
    Importable — chain_runner's finalize `--learning` latch runs this same
    validation so a random file can never satisfy the latch (Fix 3,
    2026-07-07). Checks: lives under docs/solutions/ (never moves files),
    frontmatter parses with all required keys, non-empty problem_signature,
    all 7 exact H2 sections present/non-placeholder, >=2 numbered steps in
    "Approach That Worked"."""
    path = Path(path).resolve()
    violations: List[str] = []

    if not path.exists():
        return [f"file not found: {path}"]

    try:
        solutions_dir_resolved = SOLUTIONS_DIR.resolve()
    except Exception:
        solutions_dir_resolved = SOLUTIONS_DIR
    if solutions_dir_resolved not in path.parents:
        return [
            f"file must already live under docs/solutions/ (got {path}). "
            "This tool does not move files — place it there and rerun."
        ]

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"file unreadable: {exc}"]

    fm, body = _parse_frontmatter(text)
    if fm is None:
        violations.append("frontmatter block not found or malformed (expected a leading --- ... --- YAML block)")
        fm = {}

    for key in REQUIRED_FRONTMATTER_KEYS:
        if key not in fm or fm.get(key) in (None, ""):
            violations.append(f"missing required frontmatter key: {key}")

    problem_signature = str(fm.get("problem_signature") or "").strip()
    if not problem_signature:
        violations.append("problem_signature is empty")

    sections = _extract_sections(body)
    for h2 in REQUIRED_H2:
        content = sections.get(h2)
        if content is None:
            violations.append(f"missing section: {h2}")
            continue
        if not content or "<!-- fill -->" in content:
            violations.append(f"section not filled in (placeholder remains or empty): {h2}")

    approach = sections.get("## Approach That Worked", "")
    steps = re.findall(r"^\s*\d+\.\s+\S", approach, re.MULTILINE)
    if len(steps) < 2:
        violations.append(f"## Approach That Worked needs >=2 numbered steps (found {len(steps)})")

    return violations


def cmd_save(args: argparse.Namespace) -> int:
    path = Path(args.file).resolve()
    violations = validate_card(path)

    if violations:
        print("SOLUTION CARD VALIDATION FAILED:", file=sys.stderr)
        for v in violations:
            print(f"  - {v}", file=sys.stderr)
        return 1

    _regenerate_index()
    print(f"SOLUTION CARD SAVED: docs/solutions/{path.name}")
    return 0


# ──────────────────────────────────────────────────────────────────
# check (learning-debt visibility)
# ──────────────────────────────────────────────────────────────────
def cmd_check(args: argparse.Namespace) -> int:
    _, ledger = _newest_ledger()
    debt = (ledger or {}).get("learning_debt") or []
    fresh, stale = split_debt_freshness(debt)
    if not fresh and not stale:
        print("no learning debt")
        return 0
    if fresh:
        print(f"OPEN LEARNING DEBT ({len(fresh)} fresh entries, <{LEARNING_DEBT_FRESH_HOURS}h):")
        for entry in fresh:
            print(f"  - {entry}")
    else:
        print("no fresh learning debt")
    for entry in stale:
        print(f"  - stale, ignored (>{LEARNING_DEBT_FRESH_HOURS}h): {entry}")
    return 0


# ──────────────────────────────────────────────────────────────────
# search (reuse knowledge_compiler's scorer — never reimplement it)
# ──────────────────────────────────────────────────────────────────
def cmd_search(args: argparse.Namespace) -> int:
    sys.path.insert(0, str(ROOT / "execution"))
    from knowledge_compiler import find_solution_docs  # noqa: E402

    find_solution_docs(args.query, top=3, stdout=True)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Solution Recorder — deterministic scaffolding for docs/solutions/ cards")
    sub = ap.add_subparsers(dest="command", required=True)

    d = sub.add_parser("draft", help="Gather session evidence + print a prefilled card template")
    d.add_argument("--slug", required=True)
    d.add_argument("--problem", default="", help="One-line problem_signature")
    d.set_defaults(func=cmd_draft)

    s = sub.add_parser("save", help="Validate an existing card file and regenerate the index")
    s.add_argument("--file", required=True)
    s.set_defaults(func=cmd_save)

    c = sub.add_parser("check", help="Print open learning debt from the newest session ledger")
    c.set_defaults(func=cmd_check)

    se = sub.add_parser("search", help="Search docs/solutions/ via knowledge_compiler.find_solution_docs")
    se.add_argument("query")
    se.set_defaults(func=cmd_search)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
