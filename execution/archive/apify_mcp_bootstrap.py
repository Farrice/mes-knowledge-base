#!/usr/bin/env python3
"""
apify_mcp_bootstrap.py — SessionStart hook.

Keeps the Apify MCP server registered so mcp__apify__* tools are always
available in Claude Code, even in fresh/ephemeral containers.

Behaviour (defensive by design — a SessionStart hook must NEVER block a session):
- If APIFY_TOKEN is absent (e.g. remote web env with no .env) → silent no-op.
- If the 'claude' CLI is missing → silent no-op.
- If .mcp.json already registers 'apify' → silent no-op.
- Otherwise → run execution/apify_setup.sh in the background and print one line.

Registration writes .mcp.json, which Claude Code reads at session start, so the
tools become live on the NEXT session (or immediately after a session reload).
Exit code is always 0.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]


def _env_token() -> str:
    tok = os.environ.get("APIFY_TOKEN", "")
    if tok:
        return tok
    env_path = BASE / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line.startswith("APIFY_TOKEN=") and not line.startswith("#"):
                return line.partition("=")[2].strip()
    return ""


def _already_registered() -> bool:
    mcp = BASE / ".mcp.json"
    if not mcp.exists():
        return False
    try:
        return "apify" in json.loads(mcp.read_text()).get("mcpServers", {})
    except (json.JSONDecodeError, OSError, AttributeError):
        return False


def main() -> int:
    try:
        if _already_registered():
            return 0
        if not _env_token():
            return 0
        from shutil import which
        if not which("claude"):
            return 0
        setup = BASE / "execution" / "apify_setup.sh"
        if not setup.exists():
            return 0
        # Fire-and-forget: don't hold up session start on npx/network.
        subprocess.Popen(
            ["bash", str(setup)],
            cwd=str(BASE),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print("[apify] registering MCP tools in the background — "
              "mcp__apify__* available next session.")
    except Exception:
        # Never let a bootstrap error block the session.
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
