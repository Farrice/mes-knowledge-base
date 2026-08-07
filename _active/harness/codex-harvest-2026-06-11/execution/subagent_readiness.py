#!/usr/bin/env python3
"""Dry-run readiness matrix for approved Codex subagent delegation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "semantic_libraries" / "antigravity" / "indexes" / "codex-subagent-candidates.json"

TARGET_CANDIDATES = (
    "deep-research",
    "fact-verifier",
    "competitive-intel",
    "icp-deep-canvasser",
    "adversarial-reviewer",
    "prose-doctor",
    "content-finalizer",
)

OUTPUT_CONTRACTS = {
    "deep-research": "claim-labeled synthesis, source ledger, confidence, unresolved gaps",
    "fact-verifier": "claim inventory with VERIFIED / LIKELY / UNCONFIRMED labels",
    "competitive-intel": "positioning map, pricing/source evidence, gaps, opportunity brief",
    "icp-deep-canvasser": "identity-level ICP profile, resistance map, bridge messaging",
    "adversarial-reviewer": "top risks, counterarguments, must-fix issues, ship/no-ship verdict",
    "prose-doctor": "AI-tell scan, voice risks, exact rewrite recommendations",
    "content-finalizer": "finalize checklist, quality scores, log/register actions to run after approval",
}


def load_index() -> dict[str, Any]:
    try:
        return json.loads(INDEX.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"items": []}


def build_matrix() -> dict[str, Any]:
    data = load_index()
    by_slug = {item.get("slug") or item.get("name"): item for item in data.get("items", [])}
    items = []
    for slug in TARGET_CANDIDATES:
        item = by_slug.get(slug, {})
        path = ROOT / str(item.get("path", ""))
        verdict = item.get("codex_verdict", "")
        ready = verdict == "subagent candidate" and path.exists()
        items.append(
            {
                "slug": slug,
                "name": item.get("name", slug),
                "spec_path": item.get("path", ""),
                "spec_exists": path.exists(),
                "codex_verdict": verdict or "missing",
                "callable_now": False,
                "readiness": "ready-for-approved-delegation" if ready else "not-ready",
                "activation_boundary": item.get(
                    "activation_boundary",
                    "requires explicit user authorization for real Codex subagents",
                ),
                "input_contract": "one bounded slice, exact source/context packet, stop condition, no file writes unless explicitly allowed",
                "output_contract": OUTPUT_CONTRACTS[slug],
                "failure_mode": "do not spawn; run locally or keep as workflow/protocol" if not ready else "return receipt and let main thread integrate",
            }
        )
    return {
        "schema_version": "subagent-readiness/v1",
        "source": str(INDEX.relative_to(ROOT)),
        "dry_run": True,
        "real_subagents_spawned": False,
        "integration_owner": "main Codex thread",
        "items": items,
        "delegation_receipt_template": {
            "worker": "",
            "reason_used": "",
            "exact_slice": "",
            "context_read": [],
            "output_accepted": "",
            "output_rejected": "",
            "risk_notes": "",
            "integration_owner": "main Codex thread",
        },
    }


def render_text(matrix: dict[str, Any]) -> str:
    lines = [
        "# Codex Subagent Readiness",
        "",
        f"- Dry run: {matrix['dry_run']}",
        f"- Real subagents spawned: {matrix['real_subagents_spawned']}",
        f"- Integration owner: {matrix['integration_owner']}",
        "",
        "| Candidate | Readiness | Spec | Boundary | Output |",
        "|---|---|---|---|---|",
    ]
    for item in matrix["items"]:
        spec = item["spec_path"] if item["spec_exists"] else "missing"
        lines.append(
            f"| `{item['slug']}` | {item['readiness']} | {spec} | {item['activation_boundary']} | {item['output_contract']} |"
        )
    lines.extend(
        [
            "",
            "## Delegation Receipt Template",
            "",
            "- **Worker**:",
            "- **Reason used**:",
            "- **Exact slice**:",
            "- **Context read**:",
            "- **Output accepted**:",
            "- **Output rejected**:",
            "- **Risk notes**:",
            "- **Integration owner**: main Codex thread",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Show Codex subagent delegation readiness without spawning workers.")
    parser.add_argument("--dry-run", action="store_true", help="Explicitly confirm no real subagents should be spawned.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    matrix = build_matrix()
    if args.json:
        print(json.dumps(matrix, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        print(render_text(matrix))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
