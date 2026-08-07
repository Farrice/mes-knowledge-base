#!/usr/bin/env python3
"""Verify the dry-run Codex subagent readiness surface."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import subagent_readiness  # type: ignore  # noqa: E402


EXPECTED = {
    "deep-research",
    "fact-verifier",
    "competitive-intel",
    "icp-deep-canvasser",
    "adversarial-reviewer",
    "prose-doctor",
    "content-finalizer",
}


def main() -> int:
    matrix = subagent_readiness.build_matrix()
    items = matrix.get("items", [])
    slugs = {item.get("slug") for item in items}
    missing = sorted(EXPECTED - slugs)
    if missing:
        raise AssertionError("missing subagent candidates: " + ", ".join(missing))
    if not matrix.get("dry_run") or matrix.get("real_subagents_spawned"):
        raise AssertionError("subagent readiness must be dry-run only")
    if matrix.get("integration_owner") != "main Codex thread":
        raise AssertionError("main thread must remain integration owner")
    for item in items:
        if item.get("slug") in EXPECTED:
            if not item.get("spec_exists"):
                raise AssertionError(f"{item.get('slug')} missing spec")
            if "explicit user authorization" not in item.get("activation_boundary", ""):
                raise AssertionError(f"{item.get('slug')} missing approval boundary")
            if not item.get("input_contract") or not item.get("output_contract"):
                raise AssertionError(f"{item.get('slug')} missing input/output contract")
    receipt = matrix.get("delegation_receipt_template", {})
    for key in ("worker", "reason_used", "exact_slice", "context_read", "output_accepted", "output_rejected", "risk_notes", "integration_owner"):
        if key not in receipt:
            raise AssertionError(f"delegation receipt missing {key}")
    print("SUBAGENT READINESS VERIFICATION PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
