#!/usr/bin/env python3
"""Run receipt generator for meaningful Antigravity executions."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
RECEIPT_DIR = ROOT / ".agent" / "run-receipts"
LATEST_MD = RECEIPT_DIR / "latest.md"
LATEST_JSON = RECEIPT_DIR / "latest.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def route_label(route: str) -> str:
    route = (route or "unrouted").strip()
    if not route:
        return "/unrouted"
    return route if route.startswith("/") else f"/{route}"


def filename_slug(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip().strip("/"))
    slug = re.sub(r"-{2,}", "-", slug).strip("-._")
    return slug or "unrouted"


def build_receipt(
    *,
    query: str,
    route: str,
    status: str,
    owner: str = "",
    support_gates: str = "",
    expert_lenses: str = "",
    subagent_boundary: str = "",
    subagents_requested: str = "",
    meta_intent: str = "",
    composition_owner: str = "",
    feedback_hook: str = "",
    changed: str = "",
    passed: str = "",
    failed: str = "",
    judgment: str = "",
    next_action: str = "",
) -> dict[str, Any]:
    return {
        "schema_version": "run-receipt/v2",
        "timestamp": now_iso(),
        "query": query,
        "route": route,
        "status": status,
        "owner": owner,
        "support_gates": support_gates,
        "expert_lenses": expert_lenses,
        "subagent_boundary": subagent_boundary,
        "subagents_requested": subagents_requested,
        "meta_intent": meta_intent,
        "composition_owner": composition_owner,
        "feedback_hook": feedback_hook,
        "changed": changed,
        "passed": passed,
        "failed": failed,
        "needs_judgment": judgment,
        "next_action": next_action,
    }


def render_markdown(receipt: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Run Receipt",
            "",
            f"- **Timestamp**: {receipt['timestamp']}",
            f"- **Route**: {route_label(str(receipt['route']))}",
            f"- **Status**: {receipt['status']}",
            f"- **Owner**: {receipt.get('owner') or 'none'}",
            f"- **Meta intent**: {receipt.get('meta_intent') or 'none'}",
            f"- **Composition owner**: {receipt.get('composition_owner') or 'none'}",
            f"- **Support gates**: {receipt.get('support_gates') or 'none'}",
            f"- **Expert lenses**: {receipt.get('expert_lenses') or 'none'}",
            f"- **Subagents requested**: {receipt.get('subagents_requested') or 'none'}",
            f"- **Subagent boundary**: {receipt.get('subagent_boundary') or 'none'}",
            f"- **Raw intent**: {receipt['query']}",
            f"- **What changed**: {receipt['changed'] or 'none'}",
            f"- **What passed**: {receipt['passed'] or 'not run'}",
            f"- **What failed**: {receipt['failed'] or 'none'}",
            f"- **Needs Farrice judgment**: {receipt['needs_judgment'] or 'none'}",
            f"- **Next action**: {receipt['next_action']}",
            f"- **Feedback hook**: {receipt.get('feedback_hook') or 'none'}",
        ]
    )


def write_receipt(receipt: dict[str, Any]) -> dict[str, str]:
    RECEIPT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = receipt["timestamp"].replace(":", "").replace("+", "Z")
    md_path = RECEIPT_DIR / f"{stamp}-{filename_slug(str(receipt['route']))}.md"
    json_path = md_path.with_suffix(".json")
    md = render_markdown(receipt)
    md_path.write_text(md + "\n", encoding="utf-8")
    json_path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    LATEST_MD.write_text(md + "\n", encoding="utf-8")
    LATEST_JSON.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {"markdown": str(md_path.relative_to(ROOT)), "json": str(json_path.relative_to(ROOT))}


def verify() -> None:
    if not LATEST_JSON.exists():
        return
    data = json.loads(LATEST_JSON.read_text(encoding="utf-8"))
    missing = [
        key
        for key in ("timestamp", "route", "status", "changed", "passed", "failed", "needs_judgment", "next_action")
        if key not in data
    ]
    if missing:
        raise ValueError("Latest run receipt missing: " + ", ".join(missing))


def main() -> int:
    parser = argparse.ArgumentParser(description="Create or verify an Antigravity run receipt.")
    parser.add_argument("--verify", action="store_true", help="Verify the latest receipt schema.")
    parser.add_argument("--query", default="")
    parser.add_argument("--route", default="autopilot")
    parser.add_argument("--status", default="Running now")
    parser.add_argument("--owner", default="")
    parser.add_argument("--support-gates", default="")
    parser.add_argument("--expert-lenses", default="")
    parser.add_argument("--subagent-boundary", default="")
    parser.add_argument("--meta-intent", default="")
    parser.add_argument("--composition-owner", default="")
    parser.add_argument("--feedback-hook", default="")
    parser.add_argument("--changed", default="")
    parser.add_argument("--passed", default="")
    parser.add_argument("--failed", default="")
    parser.add_argument("--judgment", default="")
    parser.add_argument("--next-action", default="Run the next verifier or approval gate.")
    args = parser.parse_args()

    if args.verify:
        verify()
        print("RUN RECEIPT VERIFICATION PASS")
        return 0

    receipt = build_receipt(
        query=args.query,
        route=args.route,
        status=args.status,
        owner=args.owner,
        support_gates=args.support_gates,
        expert_lenses=args.expert_lenses,
        subagent_boundary=args.subagent_boundary,
        meta_intent=args.meta_intent,
        composition_owner=args.composition_owner,
        feedback_hook=args.feedback_hook,
        changed=args.changed,
        passed=args.passed,
        failed=args.failed,
        judgment=args.judgment,
        next_action=args.next_action,
    )
    paths = write_receipt(receipt)
    print(json.dumps(paths, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
