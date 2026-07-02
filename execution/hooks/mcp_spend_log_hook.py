#!/usr/bin/env python3
"""
MCP Spend Fire-Log — PostToolUse hook (observe-only, never blocks).

Closes the 2026-07-02 audit's MCP budget blind spot: paid-API calls made via
MCP tools (Perplexity, Higgsfield, Recall) bypass cost_gate_hook.py (Bash-only)
and every .agent/*-usage.json tracker. This hook records each paid-MCP fire to
.agent/mcp-spend.jsonl so spend is at least visible. Approach B per the approved
plan: log at the seam, no gate surgery. Escalate to a PreToolUse gate only if
real overspend shows up in this log.

Payload: PostToolUse hook JSON on stdin (tool_name, tool_input, ...).
Always exits 0 — telemetry must never break tool flow.
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SPEND_LOG = PROJECT_ROOT / ".agent" / "mcp-spend.jsonl"

# service id -> (tool-name regex, billable regex within that service)
SERVICES = {
    "perplexity": (re.compile(r"^mcp__perplexity-ask__"), re.compile(r".")),
    "recall": (re.compile(r"^mcp__recall__"), re.compile(r".")),
    "higgsfield": (
        re.compile(r"^mcp__claude_ai_Higgsfield__"),
        re.compile(
            r"(generate_|upscale_|dubbing|motion_control|outpaint_image|"
            r"remove_background|reframe|explainer_video|shorts_studio_create|"
            r"video_analysis_create|personal_clipper_create|create_voice)"
        ),
    ),
}


def classify(tool_name: str):
    for service, (svc_pattern, billable_pattern) in SERVICES.items():
        if svc_pattern.search(tool_name):
            billable = bool(billable_pattern.search(tool_name))
            return service, billable
    return None, False


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    tool_name = payload.get("tool_name", "")
    service, billable = classify(tool_name)
    if service is None:
        return 0

    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "tool": tool_name,
        "service": service,
        "billable": billable,
        "session_id": payload.get("session_id", ""),
    }
    try:
        SPEND_LOG.parent.mkdir(parents=True, exist_ok=True)
        with SPEND_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
