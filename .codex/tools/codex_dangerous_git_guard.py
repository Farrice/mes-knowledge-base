#!/usr/bin/env python3
"""Codex PreToolUse guard for destructive git commands.

This mirrors the Claude Code dangerous-git hook without depending on
CLAUDE_PROJECT_DIR or editing the `.claude/` surface.
"""

from __future__ import annotations

import json
import re
import sys


# Destructive only. Plain `git push` was in this list until 2026-07-27 and was
# the one Codex-only divergence from .claude/hooks/block-dangerous-git.sh — it
# blocked ordinary shipping while the operating rules say commit and push main
# every session (feedback_all-work-on-main). Force-push stays blocked; a normal
# push is how work leaves the machine, not a destructive act.
DANGEROUS_PATTERNS = (
    r"\bgit\s+push\b.*(--force|-f\b)",
    r"\bgit\s+reset\s+--hard\b",
    r"\bgit\s+clean\s+-fd\b",
    r"\bgit\s+clean\s+-f\b",
    r"\bgit\s+branch\s+-D\b",
    r"\bgit\s+checkout\s+\.",
    r"\bgit\s+restore\s+\.",
    r"\bpush\s+--force\b",
    r"\breset\s+--hard\b",
)


def main() -> int:
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
    except Exception:
        return 0

    if payload.get("tool_name") != "Bash":
        return 0

    command = str((payload.get("tool_input") or {}).get("command") or "")
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, command):
            print(
                f"BLOCKED: '{command}' matches dangerous git pattern '{pattern}'.",
                file=sys.stderr,
            )
            return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
