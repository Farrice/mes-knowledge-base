#!/usr/bin/env python3
"""
Citation Integrity — detect doc/memory pointers to files that don't exist.

Born from the 2026-07-13 divergent-branch loss (docs/solutions/
2026-07-13-divergent-branch-work-silently-lost.md): MEMORY.md and CLAUDE.md
cited files as live and binding for weeks while the working tree silently
lacked them. A live doc pointing at a missing file is a LOSS SIGNAL, not doc
rot — this check makes that signal deterministic instead of
audit-luck-dependent.

Scans (default): CLAUDE.md, directives/*.md, the auto-memory dir
(MEMORY.md + every memory card), docs/solutions/*.md.

Usage:
    python3 execution/citation_integrity.py            # human report
    python3 execution/citation_integrity.py --quiet    # counts only
    python3 execution/citation_integrity.py --json     # machine output
Exit code: 0 clean · 1 missing pointers found (cron/launchd friendly).
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEMORY_DIR = Path.home() / ".claude" / "projects" / "-Users-farricecain-Google-Antigravity" / "memory"

# Repo-relative roots a path citation can start with.
KNOWN_ROOTS = (
    "execution/", "directives/", "skills/", "agents/", "docs/", "knowledge/",
    "councils/", "extractions/", "strategy_briefs/", "research_outputs/",
    "deliverables/", "products/", "projects/", "_active/", "evolution_store/",
    ".agent/", ".claude/", "evolution/", "config/",
)

# A path: known root + path chars, ending in an extension we care about.
PATH_RE = re.compile(
    r"(?<![\w/])((?:" + "|".join(re.escape(r) for r in KNOWN_ROOTS) + r")[\w./-]+\.(?:md|py|json|jsonl|txt|yaml|yml|csv|sh))\b"
)
# Markdown link targets inside a memory dir file: [title](file.md) — relative to that dir.
MEMLINK_RE = re.compile(r"\]\(([\w./-]+\.md)\)")

# Noise filters: template/example paths, globs, placeholders.
NOISE = re.compile(r"[<>{}*$\[\]]|/name/|/<|example|<expert|<skill|\.\.\.")

# Runtime artifacts: created on first use, gitignored secrets, rotating logs.
# Their absence is normal, not a loss signal. Annotated "(planned" / "(not yet"
# pointers are also skipped via the annotation check in scan_file.
RUNTIME_ALLOWLIST = re.compile(
    r"^(\.agent/(browser-actions-log|hermes-usage|knowledge-cache|citation-integrity)"
    r"|config/gws/client_secret\.json"
    r"|\.claude/(backups|plans)/)"
)


def _existing(path_str: str) -> bool:
    return (ROOT / path_str).exists()


def scan_file(fp: Path, memory_mode: bool) -> list:
    """Return list of (cited_path, resolved_kind) that do NOT exist."""
    try:
        text = fp.read_text(errors="replace")
    except OSError:
        return []
    missing = []
    seen = set()
    for m in PATH_RE.finditer(text):
        cited = m.group(1).rstrip(".")
        if cited in seen or NOISE.search(cited) or RUNTIME_ALLOWLIST.match(cited):
            continue
        # Pointers annotated as planned/expired/not-yet/deleted/superseded are acknowledged absences.
        tail = text[m.end():m.end() + 40]
        if re.match(r"[`')\s]*\((?:planned|not yet|ephemeral|deleted|superseded)", tail):
            seen.add(cited)
            continue
        seen.add(cited)
        if not _existing(cited):
            missing.append(cited)
    if memory_mode:
        for m in MEMLINK_RE.finditer(text):
            cited = m.group(1)
            if cited in seen or NOISE.search(cited) or "/" in cited:
                continue  # memory links are flat filenames; pathed ones hit PATH_RE
            seen.add(cited)
            if not (MEMORY_DIR / cited).exists():
                missing.append(f"(memory) {cited}")
    return missing


def collect_sources() -> list:
    sources = []
    claude_md = ROOT / "CLAUDE.md"
    if claude_md.exists():
        sources.append((claude_md, False, "BINDING"))
    for fp in sorted((ROOT / "directives").glob("*.md")):
        sources.append((fp, False, "BINDING"))
    if MEMORY_DIR.exists():
        for fp in sorted(MEMORY_DIR.glob("*.md")):
            sources.append((fp, True, "MEMORY"))
    sol = ROOT / "docs" / "solutions"
    if sol.exists():
        for fp in sorted(sol.glob("*.md")):
            sources.append((fp, False, "SOLUTIONS"))
    return sources


def main():
    ap = argparse.ArgumentParser(description="Detect doc/memory pointers to nonexistent files")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    report = {}  # tier -> {source: [missing]}
    total_missing = 0
    scanned = 0
    for fp, memory_mode, tier in collect_sources():
        scanned += 1
        missing = scan_file(fp, memory_mode)
        if missing:
            total_missing += len(missing)
            label = str(fp).replace(str(ROOT) + os.sep, "").replace(str(Path.home()), "~")
            report.setdefault(tier, {})[label] = missing

    if args.json:
        print(json.dumps({"scanned": scanned, "missing": total_missing, "report": report}, indent=1))
    elif args.quiet:
        print(f"scanned: {scanned} sources · missing pointers: {total_missing}")
    else:
        print(f"\n{'='*62}\n  CITATION INTEGRITY — {scanned} sources scanned\n{'='*62}")
        if not total_missing:
            print("  All cited paths resolve. Clean.")
        for tier in ("BINDING", "MEMORY", "SOLUTIONS"):
            if tier not in report:
                continue
            print(f"\n  [{tier}] — {sum(len(v) for v in report[tier].values())} missing")
            for src, items in report[tier].items():
                print(f"    {src}")
                for it in items:
                    print(f"      ✗ {it}")
        if total_missing:
            print(f"\n  {total_missing} missing pointer(s). A live doc citing a missing file")
            print("  is a LOSS SIGNAL — check `git log --all -- <path>` for orphaned")
            print("  commits BEFORE repointing (docs/solutions/2026-07-13-divergent-"
                  "branch-work-silently-lost.md).")
        print(f"{'='*62}\n")

    sys.exit(1 if total_missing else 0)


if __name__ == "__main__":
    main()
