#!/usr/bin/env python3
"""Verify contextual 3 Next Prompts and handoff routing."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


SURFACE_SNIPPETS = {
    "semantic_libraries/antigravity/primitives/collaborative-steering-compass.md": [
        "3 Next Prompts",
        "Use Now",
        "Harden",
        "Expand",
        "**Prompt**",
        "copy-paste prompt",
        "Suggested skills/workflows",
    ],
    "skills/semantic-document-library-os/workflows/steering-compass.md": [
        "## 3 Next Prompts",
        "**Use Now**",
        "**Harden**",
        "**Expand**",
        "**Prompt:**",
        "**Suggested skills/workflows:**",
    ],
    ".agent/workflows/steering-compass.md": [
        "3 Next Prompts",
        "copy-paste prompt",
        "contextual continuation prompts",
    ],
    ".agent/workflows/extraction-governor-agent.md": [
        "## 3 Next Prompts",
        "**Prompt:**",
        "**Suggested skills/workflows:**",
    ],
    ".agent/workflows/autopilot.md": [
        "Next Prompts (Insightful Momentum)",
        "**Use Now:**",
        "**Harden:**",
        "**Expand:**",
    ],
    ".agent/workflows/end-session.md": [
        "3 Next Prompts",
        "contextual_next_prompts.py",
    ],
    ".agent/workflows/handoff.md": [
        "# /handoff",
        "Suggested Skills / Workflows",
        "Exact Next Prompt",
        "Redact",
    ],
    "CODEX.md": [
        "contextual_next_prompts.py",
        "3 Next Prompts",
        "Focused transfer handoffs use `/handoff`",
    ],
}
# Note: the matt-pocock-handoff-skill reference surface was removed from
# semantic_libraries; Matt Pocock skills are managed globally (npx skills
# update), so the local attribution copy is no longer a required surface.


STEERING_QUERIES = [
    "three next prompts after final answer",
    "turn this output into contextual next prompts",
    "what should I ask you next to leverage this conversation",
    "elevate steering output with continuation prompts",
]

END_SESSION_QUERIES = [
    "wrap this session",
    "end session handoff closeout intelligence",
]

HANDOFF_QUERIES = [
    "prepare a handoff document for a fresh agent to continue this in another conversation",
    "handoff to prototype branch with suggested skills",
]


def run(args: list[str]) -> str:
    completed = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.returncode != 0:
        raise AssertionError(f"Command failed: {' '.join(args)}\n{completed.stdout}")
    return completed.stdout


def first_menu_route(output: str) -> str:
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("1. `/"):
            return stripped.split("`", 2)[1].strip("/").strip()
    return ""


def top_router_routes(output: str, limit: int = 3) -> list[str]:
    routes = []
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("/"):
            routes.append(stripped.split()[0].strip("/").strip())
        if len(routes) >= limit:
            break
    return routes


def verify_surfaces() -> list[str]:
    results = []
    for relative, snippets in SURFACE_SNIPPETS.items():
        path = ROOT / relative
        if not path.exists():
            raise AssertionError(f"Missing surface: {relative}")
        text = path.read_text(encoding="utf-8", errors="ignore")
        for snippet in snippets:
            if snippet not in text:
                raise AssertionError(f"Missing snippet in {relative}: {snippet}")
        results.append(f"surface contains contextual prompts contract: {relative}")
    return results


def verify_route(query: str, expected: str) -> list[str]:
    menu = run([sys.executable, "execution/command_menu.py", "search", query])
    router = run([sys.executable, "execution/workflow_router.py", "search", query])
    governor = run([sys.executable, "execution/routing_governor.py", "evaluate", query])
    menu_route = first_menu_route(menu)
    router_routes = top_router_routes(router)
    if menu_route != expected:
        raise AssertionError(f"command_menu expected {expected!r} for {query!r}, got {menu_route!r}\n{menu}")
    # workflow_router is a raw lexical list that new workflows legitimately
    # compete in; the binding decision layer is routing_governor below. Require
    # top-3 presence here instead of a brittle rank-1 pin.
    if expected not in router_routes:
        raise AssertionError(f"workflow_router expected {expected!r} in top 3 for {query!r}, got {router_routes!r}\n{router}")
    if f"Chosen route**: /{expected}" not in governor:
        raise AssertionError(f"routing_governor expected {expected!r} for {query!r}\n{governor}")
    return [f"route {query!r} -> /{expected}"]


def verify_helper() -> list[str]:
    output = run(
        [
            sys.executable,
            "execution/contextual_next_prompts.py",
            "--objective",
            "upgrade steering output into contextual next prompts",
            "--json",
        ]
    )
    payload = json.loads(output)
    prompts = payload.get("prompts", [])
    if len(prompts) != 3:
        raise AssertionError(f"expected 3 prompts, got {len(prompts)}")
    names = [item.get("name") for item in prompts]
    if names != ["Use Now", "Harden", "Expand"]:
        raise AssertionError(f"unexpected prompt names: {names}")
    required_fields = {
        "when_to_use",
        "why",
        "prompt",
        "expected_output",
        "quality_bar",
        "skip_if",
        "suggested_skills",
    }
    for item in prompts:
        missing = sorted(field for field in required_fields if not item.get(field))
        if missing:
            raise AssertionError(f"prompt {item.get('name')} missing fields: {missing}")

    markdown = run(
        [
            sys.executable,
            "execution/contextual_next_prompts.py",
            "--objective",
            "upgrade steering output into contextual next prompts",
        ]
    )
    for snippet in ("## 3 Next Prompts", "**Prompt:**", "**Suggested skills/workflows:**"):
        if snippet not in markdown:
            raise AssertionError(f"contextual prompt markdown missing {snippet!r}\n{markdown}")
    return ["contextual_next_prompts helper returns complete 3-prompt shape"]


def main() -> int:
    checks = []
    checks.extend(verify_surfaces())
    checks.extend(verify_helper())
    for query in STEERING_QUERIES:
        checks.extend(verify_route(query, "steering-compass"))
    for query in END_SESSION_QUERIES:
        checks.extend(verify_route(query, "end-session"))
    for query in HANDOFF_QUERIES:
        checks.extend(verify_route(query, "handoff"))

    print("CONTEXTUAL NEXT PROMPTS VERIFICATION PASS")
    for check in checks:
        print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
