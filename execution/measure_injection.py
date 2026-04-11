#!/usr/bin/env python3
"""
Context Injection Measurement — Baseline + Post-Optimization Token Audit.

Purely read-only. Measures the system-prompt injection footprint of the three
biggest fixed-cost sources in the Antigravity system:

    1. .claude/commands/*.md — slash command registrations injected by the
       Claude Code harness as the skills listing. THIS IS THE TRUE INJECTION
       SOURCE. Each file is a single-line delegator like:
           "Read and execute the workflow at `.agent/workflows/X.md` — desc"
       The system reminder shows these as truncated entries.
    2. CLAUDE.md — project instructions loaded every turn
    3. MEMORY.md — auto-memory index loaded every turn

NOTE: Earlier versions of this script measured `.agent/workflows/*.md` frontmatter
`description:` fields, which was wrong. The actual injection comes from
`.claude/commands/`. Files in `.agent/workflows/` are the workflow content
that loads on invocation — they cost zero injection tokens. There may be
many more workflow files than registered slash commands; the unregistered
ones are dormant on disk with zero per-turn cost.

Usage:
    python3 execution/measure_injection.py                    # print to stdout
    python3 execution/measure_injection.py --report out.md    # write markdown report
    python3 execution/measure_injection.py --json             # emit JSON for diffing

Token estimates use the standard 4-chars-per-token approximation. Actual
tokenization varies per model but this is accurate within ~5% for English
markdown text and sufficient for tracking deltas.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Optional

# Paths are resolved relative to the repo root (parent of execution/).
REPO_ROOT = Path(__file__).parent.parent
COMMANDS_DIR = REPO_ROOT / ".claude" / "commands"          # ACTUAL injection source
WORKFLOWS_DIR = REPO_ROOT / ".agent" / "workflows"          # workflow content (not injected)
CLAUDE_MD = REPO_ROOT / "CLAUDE.md"
MEMORY_MD = Path.home() / ".claude" / "projects" / "-Users-farricecain-Google-Antigravity" / "memory" / "MEMORY.md"

CHARS_PER_TOKEN = 4  # standard approximation


def chars_to_tokens(chars: int) -> int:
    return chars // CHARS_PER_TOKEN


def measure_commands_dir(root: Path) -> dict:
    """Measure the .claude/commands/ slash-command registrations.

    Each file is a single-line delegator that the Claude Code harness reads
    and injects as a registered skill. Format observed in system reminders:
        - <slug>: <file content (truncated to ~80-100 chars)>

    We measure both untruncated cost (worst case) and a 100-char-truncated
    estimate (closer to what Claude actually sees).
    """
    if not root.exists():
        return {
            "path": str(root),
            "file_count": 0,
            "total_chars_untruncated": 0,
            "total_tokens_untruncated": 0,
            "total_chars_truncated_100": 0,
            "total_tokens_truncated_100": 0,
            "top_20_by_chars": [],
        }

    entries = []
    for f in sorted(root.iterdir()):
        if f.is_file() and f.suffix == ".md":
            try:
                content = f.read_text(encoding="utf-8").strip()
            except (OSError, UnicodeDecodeError):
                continue
            slug = f.stem
            untrunc_line = f"- {slug}: {content}"
            trunc_line = untrunc_line[:100]
            entries.append({
                "slug": slug,
                "raw_chars": len(content),
                "untrunc_chars": len(untrunc_line),
                "trunc_chars": len(trunc_line),
                "content": content,
            })

    entries.sort(key=lambda e: -e["untrunc_chars"])
    total_untrunc = sum(e["untrunc_chars"] + 1 for e in entries)  # +1 for newline
    total_trunc = sum(e["trunc_chars"] + 1 for e in entries)

    return {
        "path": str(root),
        "file_count": len(entries),
        "total_chars_untruncated": total_untrunc,
        "total_tokens_untruncated": chars_to_tokens(total_untrunc),
        "total_chars_truncated_100": total_trunc,
        "total_tokens_truncated_100": chars_to_tokens(total_trunc),
        "top_20_by_chars": entries[:20],
    }


def measure_workflow_content_dir(root: Path) -> dict:
    """Measure .agent/workflows/ as a content store (NOT an injection source).

    These files contain the actual workflow bodies. They cost zero injection
    tokens — they only load when a workflow is invoked. We track the count
    and total content size purely as informational context, not as a cost.
    """
    if not root.exists():
        return {"path": str(root), "file_count": 0, "total_chars": 0}

    file_count = 0
    total_chars = 0
    for f in sorted(root.iterdir()):
        if f.is_file() and f.suffix == ".md":
            file_count += 1
            try:
                total_chars += f.stat().st_size
            except OSError:
                pass

    return {
        "path": str(root),
        "file_count": file_count,
        "total_chars": total_chars,
        "note": "INFORMATIONAL ONLY — these files load on invocation, not on every turn. Zero per-turn injection cost.",
    }


def find_orphans(commands_dir: Path, workflows_dir: Path) -> dict:
    """Identify mismatches between .claude/commands/ and .agent/workflows/.

    - registered_no_workflow: a slash command exists but its target workflow file does not
    - workflow_no_registration: a workflow file exists but has no slash command (dormant)
    """
    if not commands_dir.exists() or not workflows_dir.exists():
        return {"registered_no_workflow": [], "workflow_no_registration": []}

    cmd_slugs = {f.stem for f in commands_dir.iterdir() if f.is_file() and f.suffix == ".md"}
    wf_slugs = {f.stem for f in workflows_dir.iterdir() if f.is_file() and f.suffix == ".md"}

    return {
        "registered_no_workflow": sorted(cmd_slugs - wf_slugs),
        "workflow_no_registration": sorted(wf_slugs - cmd_slugs),
    }


def measure_single_file(path: Path, label: str) -> dict:
    """Measure a single fully-injected file (CLAUDE.md, MEMORY.md)."""
    if not path.exists():
        return {
            "label": label,
            "path": str(path),
            "exists": False,
            "line_count": 0,
            "char_count": 0,
            "token_count": 0,
        }

    text = path.read_text(encoding="utf-8", errors="replace")
    return {
        "label": label,
        "path": str(path),
        "exists": True,
        "line_count": text.count("\n") + 1,
        "char_count": len(text),
        "token_count": chars_to_tokens(len(text)),
    }


def build_report(measurements: dict) -> str:
    """Render a human-readable markdown baseline report."""
    cmds = measurements["commands"]
    wf_content = measurements["workflows_content"]
    claude_md = measurements["claude_md"]
    memory_md = measurements["memory_md"]
    orphans = measurements["orphans"]

    # The "real" injection cost — what costs tokens every turn
    total_chars = (
        cmds["total_chars_truncated_100"]
        + claude_md["char_count"]
        + memory_md["char_count"]
    )
    total_tokens = chars_to_tokens(total_chars)

    lines = []
    lines.append("# Context Injection Baseline Audit (Corrected)")
    lines.append("")
    lines.append(f"> Measured: {measurements['timestamp']}")
    lines.append(f"> Branch: {measurements['git_branch']}")
    lines.append(f"> Script: `execution/measure_injection.py`")
    lines.append("")
    lines.append("## What This Measures")
    lines.append("")
    lines.append("The Antigravity / Claude Code harness injects three things into the system prompt on every turn:")
    lines.append("")
    lines.append("1. **`.claude/commands/*.md`** — slash command registrations. Each file is a single-line delegator. Listed in the system reminder as the available skills/workflows. **THIS is the actual workflow injection source**, not `.agent/workflows/`.")
    lines.append("2. **`CLAUDE.md`** — project instructions, loaded as part of the system prompt.")
    lines.append("3. **`MEMORY.md`** — auto-memory index, loaded by the auto-memory system every turn.")
    lines.append("")
    lines.append("Files in `.agent/workflows/` are workflow CONTENT — they load on invocation, not every turn. They cost zero per-turn injection.")
    lines.append("")
    lines.append("## Summary (per-turn fixed injection)")
    lines.append("")
    lines.append("| Source | Files | Chars (truncated) | Est. Tokens | Notes |")
    lines.append("|---|---|---|---|---|")
    lines.append(
        f"| `.claude/commands/` slash command registrations | {cmds['file_count']} | {cmds['total_chars_truncated_100']:,} | ~{cmds['total_tokens_truncated_100']:,} | each entry capped ~100 chars in actual injection |"
    )
    lines.append(
        f"| `CLAUDE.md` | 1 | {claude_md['char_count']:,} | ~{claude_md['token_count']:,} | full file always loaded |"
    )
    lines.append(
        f"| `MEMORY.md` | 1 | {memory_md['char_count']:,} | ~{memory_md['token_count']:,} | full file always loaded |"
    )
    lines.append(
        f"| **Total fixed injection per turn** | | **{total_chars:,}** | **~{total_tokens:,}** | |"
    )
    lines.append("")
    lines.append("### For reference (NOT injected, no per-turn cost)")
    lines.append("")
    lines.append("| Source | Files | Total Chars | Notes |")
    lines.append("|---|---|---|---|")
    lines.append(
        f"| `.claude/commands/` untruncated | {cmds['file_count']} | {cmds['total_chars_untruncated']:,} | ~{cmds['total_tokens_untruncated']:,} tokens if no truncation |"
    )
    lines.append(
        f"| `.agent/workflows/` (workflow content) | {wf_content['file_count']} | {wf_content['total_chars']:,} | content store — loads on invocation only |"
    )
    lines.append("")

    lines.append("## Registration vs Content Mismatch")
    lines.append("")
    lines.append(f"- Slash commands registered in `.claude/commands/`: **{cmds['file_count']}**")
    lines.append(f"- Workflow files present in `.agent/workflows/`: **{wf_content['file_count']}**")
    lines.append(f"- Workflows with NO slash command registration (dormant on disk): **{len(orphans['workflow_no_registration'])}**")
    lines.append(f"- Slash commands pointing to MISSING workflow files (broken delegators): **{len(orphans['registered_no_workflow'])}**")
    lines.append("")
    if orphans["registered_no_workflow"]:
        lines.append("### Broken delegators (slash command exists but workflow file is missing)")
        lines.append("")
        for slug in orphans["registered_no_workflow"][:30]:
            lines.append(f"- `/{slug}`")
        if len(orphans["registered_no_workflow"]) > 30:
            lines.append(f"- ... and {len(orphans['registered_no_workflow']) - 30} more")
        lines.append("")
    if orphans["workflow_no_registration"]:
        lines.append("### Dormant workflows (file exists but no slash command — zero injection cost)")
        lines.append("")
        lines.append(f"First 30 of {len(orphans['workflow_no_registration'])}:")
        lines.append("")
        for slug in orphans["workflow_no_registration"][:30]:
            lines.append(f"- `{slug}`")
        if len(orphans["workflow_no_registration"]) > 30:
            lines.append(f"- ... and {len(orphans['workflow_no_registration']) - 30} more")
        lines.append("")

    lines.append("## Top 20 Heaviest Slash Commands (by untruncated injection length)")
    lines.append("")
    lines.append("| Slug | Untruncated Chars | Content (first 80 chars) |")
    lines.append("|---|---|---|")
    for e in cmds["top_20_by_chars"]:
        content_short = e["content"][:80].replace("\n", " ").replace("|", "\\|")
        suffix = "…" if len(e["content"]) > 80 else ""
        lines.append(f"| `/{e['slug']}` | {e['untrunc_chars']} | {content_short}{suffix} |")
    lines.append("")

    lines.append("## Notes on Methodology")
    lines.append("")
    lines.append("- Token counts use the 4-chars-per-token approximation (accurate within ~5% for English markdown).")
    lines.append("- Each `.claude/commands/X.md` file is a single-line delegator: `Read and execute the workflow at .agent/workflows/X.md — <desc>`.")
    lines.append("- The system reminder displays each entry as `- <slug>: <content>` truncated at ~100 chars with `…`. We use a 100-char cap for the realistic injection cost.")
    lines.append("- Files in `.agent/workflows/` are workflow content. They load on invocation, not every turn. Zero per-turn cost. The historical '524 workflows' count is real but only ~199 of those have a `.claude/commands/` registration.")
    lines.append("- This report is regenerated after each optimization step to track progress losslessly.")
    lines.append("")
    return "\n".join(lines)


def get_git_branch() -> str:
    try:
        import subprocess
        result = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "branch", "--show-current"],
            capture_output=True, text=True, timeout=5,
        )
        return result.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def get_timestamp() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def collect_measurements() -> dict:
    return {
        "timestamp": get_timestamp(),
        "git_branch": get_git_branch(),
        "commands": measure_commands_dir(COMMANDS_DIR),
        "workflows_content": measure_workflow_content_dir(WORKFLOWS_DIR),
        "claude_md": measure_single_file(CLAUDE_MD, "claude_md"),
        "memory_md": measure_single_file(MEMORY_MD, "memory_md"),
        "orphans": find_orphans(COMMANDS_DIR, WORKFLOWS_DIR),
    }


def main():
    parser = argparse.ArgumentParser(description="Measure context injection footprint")
    parser.add_argument("--report", type=str, help="Write markdown report to this path")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of markdown")
    args = parser.parse_args()

    measurements = collect_measurements()

    if args.json:
        print(json.dumps(measurements, indent=2))
        return

    report = build_report(measurements)

    if args.report:
        out_path = Path(args.report)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report, encoding="utf-8")
        print(f"Report written to: {out_path}")
        # Also print a summary to stdout
        cmds = measurements["commands"]
        claude_md = measurements["claude_md"]
        memory_md = measurements["memory_md"]
        total_tokens = (
            cmds["total_tokens_truncated_100"]
            + claude_md["token_count"]
            + memory_md["token_count"]
        )
        print(f"Summary: ~{total_tokens:,} tokens/turn fixed injection "
              f"(slash commands: ~{cmds['total_tokens_truncated_100']:,}, "
              f"CLAUDE.md: ~{claude_md['token_count']:,}, "
              f"MEMORY.md: ~{memory_md['token_count']:,})")
    else:
        print(report)


if __name__ == "__main__":
    main()
