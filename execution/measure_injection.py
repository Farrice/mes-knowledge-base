#!/usr/bin/env python3
"""
Context Injection Measurement — Baseline + Post-Migration Token Audit.

Purely read-only. Measures the system-prompt injection footprint of the three
biggest fixed-cost sources in the Antigravity system:

    1. .agent/workflows/*.md — frontmatter descriptions injected as slash commands
    2. CLAUDE.md — project instructions loaded every turn
    3. MEMORY.md — auto-memory index loaded every turn

Does NOT read full workflow bodies (those only load on invocation). Only the
frontmatter `description:` field is counted, because that's what the harness
injects into the skills/commands listing.

Usage:
    python3 execution/measure_injection.py                    # print to stdout
    python3 execution/measure_injection.py --report out.md    # write markdown report
    python3 execution/measure_injection.py --json             # emit JSON for diffing

The output is deterministic: run it before a change, run it after a change,
diff the reports to prove the savings (or catch an unexpected regression).

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
WORKFLOWS_DIR = REPO_ROOT / ".agent" / "workflows"
WORKFLOWS_LIBRARY_DIR = WORKFLOWS_DIR / "_library"
CLAUDE_MD = REPO_ROOT / "CLAUDE.md"
MEMORY_MD = Path.home() / ".claude" / "projects" / "-Users-farricecain-Google-Antigravity" / "memory" / "MEMORY.md"

CHARS_PER_TOKEN = 4  # standard approximation


def chars_to_tokens(chars: int) -> int:
    return chars // CHARS_PER_TOKEN


def extract_description(md_path: Path) -> Optional[str]:
    """Pull the `description:` field from a workflow file's YAML frontmatter.

    Returns None if no frontmatter or no description field. Reads only the
    first 600 bytes to stay fast on a 500-file sweep.
    """
    try:
        with open(md_path, "r", encoding="utf-8") as fh:
            head = fh.read(600)
    except (OSError, UnicodeDecodeError):
        return None

    m = re.search(r"description:\s*(.+)", head)
    if not m:
        return None
    return m.group(1).strip()


def measure_workflow_dir(root: Path, label: str) -> dict:
    """Measure a workflow directory (non-recursive).

    Simulates the injection format each workflow contributes to the
    system-prompt skills listing:
        - /{slug} (path): {description}

    This matches the pattern observed in live system-reminder output.
    """
    if not root.exists():
        return {
            "label": label,
            "path": str(root),
            "file_count": 0,
            "with_description": 0,
            "total_chars": 0,
            "total_tokens": 0,
            "top_20_by_chars": [],
        }

    entries = []
    for f in sorted(root.iterdir()):
        if f.is_file() and f.suffix == ".md":
            desc = extract_description(f)
            if desc is None:
                continue
            slug = f.stem
            injection_line = f"- /{slug} (path): {desc}"
            entries.append({
                "slug": slug,
                "chars": len(injection_line),
                "description": desc,
            })

    entries.sort(key=lambda e: -e["chars"])
    total_chars = sum(e["chars"] for e in entries)
    file_count = sum(1 for f in root.iterdir() if f.is_file() and f.suffix == ".md")

    return {
        "label": label,
        "path": str(root),
        "file_count": file_count,
        "with_description": len(entries),
        "total_chars": total_chars,
        "total_tokens": chars_to_tokens(total_chars),
        "top_20_by_chars": entries[:20],
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
    wf_top = measurements["workflows_toplevel"]
    wf_lib = measurements["workflows_library"]
    claude_md = measurements["claude_md"]
    memory_md = measurements["memory_md"]

    total_chars = (
        wf_top["total_chars"]
        + wf_lib["total_chars"]
        + claude_md["char_count"]
        + memory_md["char_count"]
    )
    total_tokens = chars_to_tokens(total_chars)

    lines = []
    lines.append("# Context Injection Baseline Audit")
    lines.append("")
    lines.append(f"> Measured: {measurements['timestamp']}")
    lines.append(f"> Branch: {measurements['git_branch']}")
    lines.append(f"> Script: `execution/measure_injection.py`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Source | Files | Chars | Est. Tokens |")
    lines.append("|---|---|---|---|")
    lines.append(
        f"| `.agent/workflows/` (top-level, auto-injected) | {wf_top['file_count']} | {wf_top['total_chars']:,} | ~{wf_top['total_tokens']:,} |"
    )
    lines.append(
        f"| `.agent/workflows/_library/` (deferred) | {wf_lib['file_count']} | {wf_lib['total_chars']:,} | ~{wf_lib['total_tokens']:,} |"
    )
    lines.append(
        f"| `CLAUDE.md` | 1 | {claude_md['char_count']:,} | ~{claude_md['token_count']:,} |"
    )
    lines.append(
        f"| `MEMORY.md` | 1 | {memory_md['char_count']:,} | ~{memory_md['token_count']:,} |"
    )
    lines.append(
        f"| **Total fixed injection per turn** | | **{total_chars:,}** | **~{total_tokens:,}** |"
    )
    lines.append("")
    lines.append(f"Top-level workflow scan: {wf_top['file_count']} `.md` files, "
                 f"{wf_top['with_description']} with a `description:` frontmatter field.")
    lines.append("")

    lines.append("## Top 20 Heaviest Top-Level Workflows (by injection line length)")
    lines.append("")
    lines.append("| Slug | Chars | Description |")
    lines.append("|---|---|---|")
    for e in wf_top["top_20_by_chars"]:
        desc_short = e["description"][:80] + ("…" if len(e["description"]) > 80 else "")
        lines.append(f"| `{e['slug']}` | {e['chars']} | {desc_short} |")
    lines.append("")

    if wf_lib["file_count"] > 0:
        lines.append("## Library (Deferred) Workflows")
        lines.append("")
        lines.append(
            f"`.agent/workflows/_library/` contains {wf_lib['file_count']} workflows "
            f"totaling {wf_lib['total_chars']:,} chars (~{wf_lib['total_tokens']:,} tokens). "
            f"These are NOT injected into the system prompt — they load on demand via "
            f"the `/run` router or the CLAUDE.md fallback rule."
        )
        lines.append("")

    lines.append("## Notes on Methodology")
    lines.append("")
    lines.append("- Token counts use the 4-chars-per-token approximation (accurate within ~5% for English markdown).")
    lines.append("- Only the `description:` frontmatter field is counted for workflows — full bodies only load on invocation.")
    lines.append("- Injection format simulated: `- /<slug> (path): <description>` (matches observed system-reminder output).")
    lines.append("- MEMORY.md is loaded by the auto-memory system on every turn; CLAUDE.md by the harness project-instructions loader.")
    lines.append("- This report is regenerated after each Phase 1 batch to track lossless deferral progress.")
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
        "workflows_toplevel": measure_workflow_dir(WORKFLOWS_DIR, "workflows_toplevel"),
        "workflows_library": measure_workflow_dir(WORKFLOWS_LIBRARY_DIR, "workflows_library"),
        "claude_md": measure_single_file(CLAUDE_MD, "claude_md"),
        "memory_md": measure_single_file(MEMORY_MD, "memory_md"),
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
        wf_top = measurements["workflows_toplevel"]
        claude_md = measurements["claude_md"]
        memory_md = measurements["memory_md"]
        total_tokens = (
            wf_top["total_tokens"]
            + claude_md["token_count"]
            + memory_md["token_count"]
        )
        print(f"Summary: ~{total_tokens:,} tokens/turn fixed injection "
              f"(workflows top-level: ~{wf_top['total_tokens']:,}, "
              f"CLAUDE.md: ~{claude_md['token_count']:,}, "
              f"MEMORY.md: ~{memory_md['token_count']:,})")
    else:
        print(report)


if __name__ == "__main__":
    main()
