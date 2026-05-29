#!/usr/bin/env python3
"""
Dream — File-memory consolidation scanner (local equivalent of Claude Code auto-dream).

Targets the FILE memory layer (MEMORY.md + topic files), NOT the sovereign DB.
The sovereign DB has its own dream-equivalent (memory_distill.py + memory_review.py);
this is the missing piece: the append-only MEMORY.md index has no prune/merge pass,
which is why it grows past the context-load ceiling.

Design contract (mirrors directives + the native Dreams API):
  - DETERMINISTIC DETECTION. This scan runs standalone, no model in the loop.
    (feedback rule: "no AI-memory-dependent observability" — detection must not
     depend on Claude remembering to think about it.)
  - NON-DESTRUCTIVE. This script NEVER mutates MEMORY.md or topic files. It only
    reports findings. The /dream-local workflow writes a *proposed* rebuild to .tmp/dream/
    for human review; applying is a separate, gated, backed-up step.
    (feedback rule: "auto-evolution can't substitute for ground truth.")

Usage:
    python3 execution/dream.py scan                 # human-readable report
    python3 execution/dream.py scan --json          # machine-readable
    python3 execution/dream.py scan --memory-dir <path>   # override target dir

Exit codes:
    0 = scan ran (findings may exist; presence of findings is not an error)
    1 = error (dir missing, MEMORY.md unreadable)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

# Default to THIS project's file-memory directory.
DEFAULT_MEMORY_DIR = Path(
    "/Users/farricecain/.claude/projects/"
    "-Users-farricecain-Google-Antigravity/memory"
)

# --- Tunables --------------------------------------------------------------
INDEX_LINE_MAX_CHARS = 200      # MEMORY.md bullet ceiling (matches CLAUDE.md guidance)
NEAR_DUP_RATIO = 0.82           # SequenceMatcher ratio above which two index lines are "near-dup"
MEMORY_SECTION_BLOAT_LINES = 18 # a MEMORY.md ## section longer than this likely belongs in a topic file

# Relative-date phrases the native auto-dream converts to absolute dates.
RELATIVE_DATE_RE = re.compile(
    r"\b(today|yesterday|tomorrow|last (?:week|month|night|session)|"
    r"this (?:week|month|morning|session)|recently|just (?:now|released|shipped)|"
    r"\d+\s+(?:day|week|month)s?\s+ago|currently|right now)\b",
    re.IGNORECASE,
)

# MEMORY.md index pointer: - [Title](file.md) — hook
POINTER_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")


@dataclass
class Findings:
    memory_dir: str
    scanned_at: str
    inventory: dict = field(default_factory=dict)
    relative_dates: list = field(default_factory=list)
    oversized_index_lines: list = field(default_factory=list)
    orphan_pointers: list = field(default_factory=list)
    unindexed_files: list = field(default_factory=list)
    near_duplicate_index: list = field(default_factory=list)
    stale_candidates: list = field(default_factory=list)
    bloated_sections: list = field(default_factory=list)


# --- CONTRIBUTION POINT (pruning / staleness policy) -----------------------
# This is the one judgment call /dream-local can't infer: when is a memory "stale
# enough" to flag for archival? Too aggressive and you lose hard-won lessons;
# too lax and bloat returns. The sensible default below already works — tune
# the constants or the logic to match how YOU actually use memory.
STALE_AGE_DAYS = 75               # not touched in this many days → candidate
NEVER_PRUNE_PREFIXES = ("feedback_", "user_")  # lessons + identity: keep regardless of age


def classify_stale(path: Path, age_days: int, is_indexed: bool) -> str | None:
    """Return an archival recommendation string, or None to keep.

    Default policy:
      - feedback_*/user_* files are never stale-flagged (load-bearing lessons/identity).
      - A file untouched > STALE_AGE_DAYS AND no longer pointed to by MEMORY.md
        is a strong archival candidate (drifted out of the index AND cold).
      - A file untouched > STALE_AGE_DAYS but still indexed is a *soft* candidate
        (review the pointer; the topic may have merged elsewhere).
    """
    if path.name.startswith(NEVER_PRUNE_PREFIXES):
        return None
    if age_days <= STALE_AGE_DAYS:
        return None
    if not is_indexed:
        return f"cold {age_days}d + unindexed → archive candidate"
    return f"cold {age_days}d (still indexed) → review pointer"
# --- end contribution point ------------------------------------------------


def _read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return ""


def scan(memory_dir: Path) -> Findings:
    if not memory_dir.is_dir():
        print(f"error: memory dir not found: {memory_dir}", file=sys.stderr)
        sys.exit(1)

    memory_md = memory_dir / "MEMORY.md"
    if not memory_md.is_file():
        print(f"error: MEMORY.md not found in {memory_dir}", file=sys.stderr)
        sys.exit(1)

    now = datetime.now(timezone.utc)
    f = Findings(
        memory_dir=str(memory_dir),
        scanned_at=now.isoformat(timespec="seconds"),
    )

    index_text = _read(memory_md)
    index_lines = index_text.splitlines()
    topic_files = sorted(
        p for p in memory_dir.glob("*.md") if p.name != "MEMORY.md"
    )

    f.inventory = {
        "memory_md_bytes": memory_md.stat().st_size,
        "memory_md_lines": len(index_lines),
        "topic_file_count": len(topic_files),
        "total_bytes": sum(p.stat().st_size for p in memory_dir.glob("*.md")),
    }

    # --- pointers in the index ---
    pointed_files: set[str] = set()
    bullet_lines: list[tuple[int, str]] = []
    for i, line in enumerate(index_lines, 1):
        for m in POINTER_RE.finditer(line):
            pointed_files.add(m.group(1))
        if line.lstrip().startswith(("- ", "* ")):
            bullet_lines.append((i, line.strip()))
            if len(line) > INDEX_LINE_MAX_CHARS:
                f.oversized_index_lines.append(
                    {"line": i, "chars": len(line), "text": line.strip()[:120] + "…"}
                )

    # --- orphan pointers (index → missing file) ---
    existing = {p.name for p in topic_files}
    for ref in sorted(pointed_files):
        if ref not in existing:
            f.orphan_pointers.append(ref)

    # --- unindexed files (file exists, no pointer) ---
    for p in topic_files:
        if p.name not in pointed_files:
            f.unindexed_files.append(p.name)

    # --- near-duplicate index bullets ---
    for a in range(len(bullet_lines)):
        for b in range(a + 1, len(bullet_lines)):
            la, ta = bullet_lines[a]
            lb, tb = bullet_lines[b]
            ratio = SequenceMatcher(None, ta, tb).ratio()
            if ratio >= NEAR_DUP_RATIO:
                f.near_duplicate_index.append(
                    {"ratio": round(ratio, 2), "line_a": la, "line_b": lb,
                     "a": ta[:90], "b": tb[:90]}
                )

    # --- relative dates across MEMORY.md + topic files ---
    for p in [memory_md, *topic_files]:
        for i, line in enumerate(_read(p).splitlines(), 1):
            for m in RELATIVE_DATE_RE.finditer(line):
                f.relative_dates.append(
                    {"file": p.name, "line": i, "phrase": m.group(0),
                     "context": line.strip()[:100]}
                )

    # --- stale candidates (policy-driven) ---
    for p in topic_files:
        age_days = (now - datetime.fromtimestamp(p.stat().st_mtime, timezone.utc)).days
        rec = classify_stale(p, age_days, p.name in pointed_files)
        if rec:
            f.stale_candidates.append({"file": p.name, "age_days": age_days, "rec": rec})

    # --- bloated sections in MEMORY.md (content that belongs in a topic file) ---
    cur_head, cur_start, cur_len = None, 0, 0
    for i, line in enumerate(index_lines, 1):
        if line.startswith("## "):
            if cur_head and cur_len > MEMORY_SECTION_BLOAT_LINES:
                f.bloated_sections.append(
                    {"section": cur_head, "start_line": cur_start, "body_lines": cur_len}
                )
            cur_head, cur_start, cur_len = line[3:].strip(), i, 0
        elif cur_head:
            cur_len += 1 if line.strip() else 0
    if cur_head and cur_len > MEMORY_SECTION_BLOAT_LINES:
        f.bloated_sections.append(
            {"section": cur_head, "start_line": cur_start, "body_lines": cur_len}
        )

    return f


def _print_human(f: Findings) -> None:
    inv = f.inventory
    kb = inv["memory_md_bytes"] / 1024
    print(f"\n  DREAM SCAN — {f.memory_dir}")
    print(f"  {f.scanned_at}\n")
    print(f"  MEMORY.md ...... {kb:.1f}KB, {inv['memory_md_lines']} lines")
    print(f"  topic files .... {inv['topic_file_count']}")
    print(f"  total .......... {inv['total_bytes']/1024:.1f}KB\n")

    def section(title, items, fmt):
        flag = "  " if not items else "→ "
        print(f"{flag}{title}: {len(items)}")
        for it in items[:12]:
            print(f"      {fmt(it)}")
        if len(items) > 12:
            print(f"      … +{len(items)-12} more")

    section("Relative dates (→ convert to absolute)", f.relative_dates,
            lambda x: f"{x['file']}:{x['line']}  '{x['phrase']}'  {x['context']}")
    section(f"Oversized index lines (>{INDEX_LINE_MAX_CHARS} chars)", f.oversized_index_lines,
            lambda x: f"L{x['line']} ({x['chars']}c)  {x['text']}")
    section("Orphan pointers (index → missing file)", f.orphan_pointers, lambda x: x)
    section("Unindexed topic files (file → no pointer)", f.unindexed_files, lambda x: x)
    section("Near-duplicate index bullets", f.near_duplicate_index,
            lambda x: f"{x['ratio']}  L{x['line_a']}↔L{x['line_b']}  {x['a']}")
    section("Bloated MEMORY.md sections (→ move to topic file)", f.bloated_sections,
            lambda x: f"L{x['start_line']}  ## {x['section']}  ({x['body_lines']} body lines)")
    section("Stale candidates", f.stale_candidates,
            lambda x: f"{x['file']}  {x['rec']}")

    total = (len(f.relative_dates) + len(f.oversized_index_lines) + len(f.orphan_pointers)
             + len(f.unindexed_files) + len(f.near_duplicate_index)
             + len(f.bloated_sections) + len(f.stale_candidates))
    print(f"\n  {total} findings. Non-destructive — nothing changed.")
    print("  Run /dream-local to consolidate (manual fallback; native /dream supersedes).\n")


def main() -> None:
    ap = argparse.ArgumentParser(description="File-memory consolidation scanner")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sc = sub.add_parser("scan", help="report consolidation findings (read-only)")
    sc.add_argument("--memory-dir", type=Path, default=DEFAULT_MEMORY_DIR)
    sc.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.cmd == "scan":
        f = scan(args.memory_dir)
        if args.json:
            print(json.dumps(asdict(f), indent=2))
        else:
            _print_human(f)


if __name__ == "__main__":
    main()
