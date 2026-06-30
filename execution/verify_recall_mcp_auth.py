#!/usr/bin/env python3
"""Verify Recall MCP OAuth status from `codex mcp list --json`.

Run this verifier outside the Codex sandbox when possible. A sandboxed MCP list
can report streamable HTTP auth as "unsupported" even after OAuth succeeds.
"""

from __future__ import annotations

import json
import subprocess
from typing import Any


def fail(message: str) -> int:
    print("RECALL MCP AUTH VERIFICATION FAIL")
    print(f"- {message}")
    return 1


def extract_json_array(output: str) -> list[dict[str, Any]]:
    start = output.find("[")
    end = output.rfind("]")
    if start == -1 or end == -1 or end < start:
        raise ValueError("could not find JSON array in command output")
    data = json.loads(output[start : end + 1])
    if not isinstance(data, list):
        raise ValueError("MCP list output was not a JSON array")
    return data


def main() -> int:
    proc = subprocess.run(
        ["codex", "mcp", "list", "--json"],
        text=True,
        capture_output=True,
    )
    combined_output = "\n".join(part for part in (proc.stdout, proc.stderr) if part)
    if proc.returncode != 0:
        return fail(f"`codex mcp list --json` exited {proc.returncode}: {combined_output.strip()}")

    try:
        servers = extract_json_array(combined_output)
    except Exception as exc:  # noqa: BLE001 - verifier should report parse context.
        return fail(f"could not parse MCP list JSON: {exc}")

    recall = next((server for server in servers if server.get("name") == "recall"), None)
    if not recall:
        return fail("recall server missing from MCP list")

    if recall.get("enabled") is not True:
        return fail(f"recall server is not enabled: {recall!r}")

    auth_status = recall.get("auth_status")
    if auth_status != "o_auth":
        print("RECALL MCP AUTH VERIFICATION FAIL")
        print(f"- recall auth_status: {auth_status!r}; expected 'o_auth'")
        if auth_status == "unsupported":
            print("- Rerun outside the Codex sandbox; sandboxed MCP reads can show a false unsupported state.")
        else:
            print("- Run `codex mcp login recall`, approve the browser flow, then rerun this verifier.")
        return 1

    enabled_count = sum(1 for server in servers if server.get("enabled") is True)
    print("RECALL MCP AUTH VERIFICATION PASS")
    print(f"- servers_enabled: {enabled_count}")
    print("- recall auth_status: o_auth")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
