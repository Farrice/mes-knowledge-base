#!/usr/bin/env python3
"""
Routing Enforcer — Runtime validation of mandatory workflow bindings.

Source of truth for the "Mandatory Workflow Routing" table in CLAUDE.md.
This module exists because the 2026-04-21 incident proved that routing
guidance in markdown alone is advisory — Claude can read CLAUDE.md and
still pick the wrong workflow when the user's conversational ask points
elsewhere. This module makes the binding deterministic: code-checked,
not norm-checked.

Two modes:
    1. Pre-flight check (Claude calls before producing):
        python3 execution/routing_enforcer.py check \\
            --request "next parallax substack" --workflow writers-room
       Returns non-zero exit + JSON if invalid; logs the decision.

    2. Post-hoc validation (auto-fires from chain_runner.py finalize()
       when --workflow is supplied; flags violations into traces).

Both modes append a JSONL entry to:
    evolution_store/traces/routing_decisions.jsonl

Update BINDINGS to add new mandatory routes. Pattern: a domain signal
(set of keyword phrases) maps to ONE mandatory workflow and a list of
workflows that must NEVER substitute.
"""

import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

TRACE_DIR = Path(__file__).parent.parent / "evolution_store" / "traces"
ROUTING_LOG = TRACE_DIR / "routing_decisions.jsonl"

# ─────────────────────────────────────────────────────────
# MANDATORY BINDINGS — Source of truth for routing enforcement
# Mirror of CLAUDE.md "Mandatory Workflow Routing" table.
# Update both together; reference https://example/audit if adding new bindings.
# ─────────────────────────────────────────────────────────

BINDINGS = [
    {
        "id": "parallax_editions",
        "signal_phrases": [
            "parallax edition",
            "parallax substack",
            "next substack",
            "parallax prompt pack",
            "parallax post",
            "parallax draft",
        ],
        "mandatory_workflow": "parallax",
        "forbidden_workflows": ["writers-room"],
        "reason": (
            "Parallax editions require Phase 2.5 GROUND + ZEITGEIST and the full "
            "/parallax production sequence. writers-room is diagnostic-on-draft, "
            "not production-from-raw-take. Edition 02 shipped 7 fabrications when "
            "this binding was violated (2026-04-21)."
        ),
        "override_flag": "--no-ground",
        "override_warning": (
            "Only use --no-ground when the edition has zero external factual surface "
            "(pure memoir with no public figures, events, brands, or stats)."
        ),
    },
    {
        "id": "linkedin_from_scratch",
        "signal_phrases": [
            "linkedin post from scratch",
            "write a linkedin post",
            "draft a linkedin post",
            "new linkedin post",
            "linkedin content from scratch",
            "linkedin post production",
        ],
        "mandatory_workflow_any_of": [
            "ghostwrite",
            "lara-acosta-linkedin-ghostwriting",
            "high-dwell",
        ],
        "forbidden_workflows": ["writers-room"],
        "reason": (
            "LinkedIn post production from scratch requires Lara Acosta's pattern "
            "library (engineered virality, SLAY format, headline=pain+for-whom+proof). "
            "writers-room is for refinement of an existing draft, not first-pass production."
        ),
    },
    {
        "id": "writers_room_refinement",
        "signal_phrases": [
            "refine this draft",
            "improve this draft",
            "polish this draft",
            "writers room",
            "writer's room",
            "diagnose this content",
            "fix this draft",
        ],
        "mandatory_workflow": "writers-room",
        "forbidden_workflows": ["parallax", "ghostwrite", "high-dwell"],
        "reason": (
            "Writers' room is the diagnosis-and-treatment workflow for an EXISTING "
            "draft. Production workflows (/parallax, /ghostwrite) are for first-pass "
            "creation from raw input. Wrong direction = wrong tool."
        ),
    },
]


def _normalize_workflow(name: str) -> str:
    """Strip leading slashes/at-signs and lowercase for comparison."""
    return name.lower().lstrip("/@").strip()


def _request_hits_signal(request: str, signal_phrases: List[str]) -> Optional[str]:
    """Return the first signal phrase that appears in the request, or None."""
    request_lower = request.lower()
    for phrase in signal_phrases:
        if phrase.lower() in request_lower:
            return phrase
    return None


def check_routing(request: str, chosen_workflow: str) -> Dict[str, Any]:
    """
    Validate a routing decision against mandatory bindings.

    Args:
        request: The user's original request (or sharpened intent).
        chosen_workflow: The workflow Claude proposes to run (with or without /).

    Returns:
        {
            "valid": bool,
            "binding_matched": str | None,    # binding id that fired
            "matched_signal": str | None,     # which phrase matched
            "mandatory_workflow": str | list | None,
            "chosen_workflow": str,
            "violation_reason": str | None,   # why it's invalid (if invalid)
            "advisory": str | None,           # informational notes (e.g., override flag)
        }

    A request that doesn't match any binding is automatically valid —
    bindings only fire when the signal is present.
    """
    chosen_norm = _normalize_workflow(chosen_workflow)
    result = {
        "valid": True,
        "binding_matched": None,
        "matched_signal": None,
        "mandatory_workflow": None,
        "chosen_workflow": chosen_norm,
        "violation_reason": None,
        "advisory": None,
    }

    for binding in BINDINGS:
        matched_signal = _request_hits_signal(request, binding["signal_phrases"])
        if not matched_signal:
            continue

        # Signal matched — this binding applies.
        result["binding_matched"] = binding["id"]
        result["matched_signal"] = matched_signal

        mandatory = binding.get("mandatory_workflow")
        mandatory_any_of = binding.get("mandatory_workflow_any_of")
        forbidden = [_normalize_workflow(w) for w in binding.get("forbidden_workflows", [])]

        # Is the chosen workflow forbidden for this signal?
        if chosen_norm in forbidden:
            result["valid"] = False
            result["mandatory_workflow"] = mandatory or mandatory_any_of
            result["violation_reason"] = (
                f"Signal '{matched_signal}' triggers binding '{binding['id']}'. "
                f"Workflow '{chosen_norm}' is forbidden for this domain. "
                f"Required: {result['mandatory_workflow']}. "
                f"Reason: {binding['reason']}"
            )
            if binding.get("override_flag"):
                result["advisory"] = (
                    f"Override available via {binding['override_flag']}. "
                    f"{binding.get('override_warning', '')}"
                )
            return result

        # Does the chosen workflow match the mandatory one?
        if mandatory:
            if chosen_norm != _normalize_workflow(mandatory):
                result["valid"] = False
                result["mandatory_workflow"] = mandatory
                result["violation_reason"] = (
                    f"Signal '{matched_signal}' triggers binding '{binding['id']}'. "
                    f"Mandatory workflow is '{mandatory}', got '{chosen_norm}'. "
                    f"Reason: {binding['reason']}"
                )
                return result

        if mandatory_any_of:
            allowed = [_normalize_workflow(w) for w in mandatory_any_of]
            if chosen_norm not in allowed:
                result["valid"] = False
                result["mandatory_workflow"] = mandatory_any_of
                result["violation_reason"] = (
                    f"Signal '{matched_signal}' triggers binding '{binding['id']}'. "
                    f"Workflow must be one of {mandatory_any_of}, got '{chosen_norm}'. "
                    f"Reason: {binding['reason']}"
                )
                return result

        # Signal matched + workflow valid — record for trace, return ok.
        result["mandatory_workflow"] = mandatory or mandatory_any_of
        return result

    # No binding fired — request doesn't match any signal.
    return result


def log_decision(request: str, chosen_workflow: str, validation: Dict[str, Any],
                 source: str = "cli", override_used: Optional[str] = None) -> None:
    """Append a routing decision to evolution_store/traces/routing_decisions.jsonl."""
    try:
        TRACE_DIR.mkdir(parents=True, exist_ok=True)
        entry = {
            "timestamp": datetime.now().isoformat(),
            "source": source,
            "request": request[:500],
            "chosen_workflow": chosen_workflow,
            "valid": validation["valid"],
            "binding_matched": validation.get("binding_matched"),
            "matched_signal": validation.get("matched_signal"),
            "mandatory_workflow": validation.get("mandatory_workflow"),
            "violation_reason": validation.get("violation_reason"),
            "override_used": override_used,
        }
        with open(ROUTING_LOG, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception:
        # Logging is non-fatal — never block a chain on observability.
        pass


def list_bindings() -> List[Dict[str, Any]]:
    """Return all mandatory bindings (for inspection / sync with CLAUDE.md)."""
    return BINDINGS


def main():
    parser = argparse.ArgumentParser(description="Routing Enforcer — validate workflow choices against mandatory bindings.")
    sub = parser.add_subparsers(dest="command")

    chk = sub.add_parser("check", help="Validate a routing decision")
    chk.add_argument("--request", required=True, help="The user's original request or sharpened intent")
    chk.add_argument("--workflow", required=True, help="The chosen workflow name (with or without leading /)")
    chk.add_argument("--source", default="cli", help="Caller identifier for trace log (default: cli)")
    chk.add_argument("--override", default=None, help="Override flag the model invoked (e.g. --no-ground)")
    chk.add_argument("--quiet", action="store_true", help="Only print on violation; exit non-zero on invalid")

    sub.add_parser("list", help="Print all mandatory bindings as JSON")

    args = parser.parse_args()

    if args.command == "check":
        result = check_routing(args.request, args.workflow)
        log_decision(args.request, args.workflow, result, source=args.source, override_used=args.override)
        if not result["valid"]:
            print(json.dumps(result, indent=2))
            sys.exit(2)  # Non-zero exit on violation
        if not args.quiet:
            print(json.dumps(result, indent=2))
        sys.exit(0)

    if args.command == "list":
        print(json.dumps(BINDINGS, indent=2))
        sys.exit(0)

    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
