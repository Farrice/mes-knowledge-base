#!/usr/bin/env python3
"""Prompt-menu hook — deterministic v2-prompt wiring at skill-load time.

PostToolUse(Read): when the model reads a skill's SKILL.md (Tier 1/2 load),
inject a pointer menu of that skill's structure-pure v2 execution prompts
from .agent/prompt-index.json. Pointer-menu style (Farrice 2026-07-13):
one line per prompt, model reads the chosen file on demand — near-zero
token cost, deterministic discoverability.

Skills with NO v2 prompts get a one-line forge flag (lazy-backfill signal).
"""
import json
import os
import re
import sys

MAX_MENU = 8
PROJECT = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
INDEX = os.path.join(PROJECT, ".agent", "prompt-index.json")
SKILL_RE = re.compile(r"skills/([^/]+)/SKILL\.md$")


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return
    if payload.get("tool_name") != "Read":
        return
    file_path = (payload.get("tool_input") or {}).get("file_path", "")
    m = SKILL_RE.search(file_path.replace("\\", "/"))
    if not m:
        return
    skill = m.group(1)

    try:
        entries = json.load(open(INDEX)).get("entries", [])
    except Exception:
        return
    v2 = [e for e in entries if e.get("kind") == "prompt-v2" and e.get("skill") == skill]

    if not v2:
        # only flag skills that are real skill dirs (avoid noise on archived paths)
        msg = (
            f"EXECUTION PROMPTS (deterministic, from prompt_menu_hook.py): skill '{skill}' has NO "
            "structure-pure v2 prompts yet. If this task produces expert-domain output, note the gap — "
            "the prompt-forging backfill covers it (directives/prompt-forging-spec.md); do not invent a v2 ad hoc."
        )
    else:
        lines = []
        for e in v2[:MAX_MENU]:
            title = e.get("title", os.path.basename(e.get("path", "?")))
            lines.append(f"  • {title} — {e.get('path')}")
        more = f"\n  … +{len(v2) - MAX_MENU} more: python3 execution/prompt_library.py find \"<need>\" --skill {skill}" if len(v2) > MAX_MENU else ""
        msg = (
            f"EXECUTION PROMPTS (deterministic, from prompt_menu_hook.py): skill '{skill}' has {len(v2)} "
            "structure-pure v2 prompts — deterministic Output Contract / Skeleton / Quality Gate per deliverable. "
            "Before producing this skill's expert output, Read the one matching the deliverable and honor its contract:\n"
            + "\n".join(lines) + more
        )

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": msg,
        }
    }))


if __name__ == "__main__":
    main()
