#!/usr/bin/env python3
"""Client-package linter — a client-facing doc set may only reference things the
client actually has: sibling docs in the package, files shipped with it, or
public URLs. Internal repo paths, tool names, and operator vocabulary are ship
blockers. Farrice 2026-07-09 (binding): "we shouldn't be having the documents
pointing to files or assets or commands or internal workings that he can't
deploy himself."

Usage:
  python3 execution/client_package_lint.py <dir-or-files> [--allow name ...]

Exit 1 on any finding. Wire into client-doc build workflows before delivery.
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

# Repo-internal path shapes a client can never open.
PATH_PATTERNS = [
    (re.compile(r"`[^`\n]*/(?:[^`\n]*\.(?:md|py|json|yaml|yml|sh|js|txt))`"), "backticked repo file path"),
    (re.compile(r"\b\d{2}-[a-z][a-z-]+/[A-Za-z0-9._\-]+"), "numbered internal dir path"),
    (re.compile(r"\b(?:execution|directives|skills|agents|knowledge|_active|\.agent|00-strategy|0[1-9]-[a-z-]+)/"), "internal repo directory"),
    (re.compile(r"_take-b|_gate-records|_archive"), "internal working dir"),
]
# Operator/tooling vocabulary that means nothing to (or shouldn't reach) a client.
JARGON = [
    "prose_classifier", "Playwright", "SKILL.md", "genius.md", "workflow_router",
    "chain_runner", "sub-agent", "subagent", "MUST-FIX", "gate record", "Gate Record",
    "fact-verifier", "adversarial review", "[ASSUMPTION]", "UNCONFIRMED",
    "STRATEGY-SPINE", "SQUEEZE-PAGE.md", "FLYER-COPY-AND-SPEC",
]
# Always fine: package-relative language and the public web.
ALLOW_DEFAULT = [
    r"doc 0\d", r"in this folder", r"Receipts →", r"Print Files",
    r"https?://", r"coachcooz\.com", r"\.svg\b",  # shipped print files
]


def lint_file(path: Path, allow: list[re.Pattern]) -> list[tuple[int, str, str]]:
    findings = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
        probe = line
        for a in allow:
            probe = a.sub(" ", probe)
        for pat, label in PATH_PATTERNS:
            m = pat.search(probe)
            if m:
                findings.append((lineno, label, m.group(0)[:60]))
        for word in JARGON:
            if word in probe:
                findings.append((lineno, "operator jargon", word))
    return findings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("targets", nargs="+")
    ap.add_argument("--allow", action="append", default=[], help="extra allowed regex")
    args = ap.parse_args()

    allow = [re.compile(a) for a in ALLOW_DEFAULT + args.allow]
    files: list[Path] = []
    for t in args.targets:
        p = Path(t)
        if p.is_dir():
            files += [f for f in sorted(p.glob("*.md")) if not f.name.startswith("_")]
        elif p.is_file():
            files.append(p)

    total = 0
    for f in files:
        findings = lint_file(f, allow)
        if findings:
            print(f"✗ {f.name}")
            for lineno, label, snippet in findings:
                print(f"    L{lineno} [{label}] {snippet}")
            total += len(findings)
        else:
            print(f"✓ {f.name}")
    print(f"\n{'FAIL' if total else 'PASS'} — {total} finding(s) across {len(files)} file(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
