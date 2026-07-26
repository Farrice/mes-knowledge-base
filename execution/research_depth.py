#!/usr/bin/env python3
"""
Research Depth Contract — THE single source of truth for what each research
depth tier requires. Every module that used to carry its own local copy of
these numbers imports from here instead:

    execution/native_floor.py      (was: DEPTH_MIN_SOURCES / DEPTH_MIN_DOMAINS)
    execution/research_personas.py (was: DEPTH_AGENT_COUNT)
    execution/swarm_conductor.py   (was: RESEARCH_FAN_OUT / RESEARCH_DEPTH_LABEL)
    execution/research_quality_gate.py (depth floors for artifact validation)
    .agent/workflows/*.workflow.js  (reads via `python3 execution/research_depth.py --json`)

Born 2026-07-26 out of the shallow-research audit: depth config had drifted
across 3+ files (code said deep=6 sources while directives/research-protocol.md
said 15), so "deep" runs could legally be six Tavily snippets. One table ends
that. If a number here changes, every consumer moves together.

Fields per tier:
    sources   — minimum distinct source URLs for the tier to count as met
    domains   — minimum distinct domains among those sources
    agents    — total research agents a swarm run fans out
    fan_out   — subtopic fan-out for the conductor (per-wave breadth)
    rounds    — gap-fill rounds AFTER the initial sweep (0 = single pass)
    verify    — "topN" (int) or "all" load-bearing claims get an independent
                adversarial verifier (never the agent that found the claim)
    extracts  — full-page extractions (tavily_extract / WebFetch) required per
                subtopic; snippets alone never satisfy this
    verify_cap— runaway stop when verify == "all"

CLI:
    python3 execution/research_depth.py --json            # full table
    python3 execution/research_depth.py --depth deep      # one tier
"""

from __future__ import annotations

import json
from typing import Any, Dict

# Aligned to directives/research-protocol.md (which now defers to THIS file).
DEPTH: Dict[str, Dict[str, Any]] = {
    "quick":    dict(sources=3,  domains=2, agents=3,  fan_out=3,  rounds=0, verify=4,     extracts=0, verify_cap=4),
    "standard": dict(sources=8,  domains=4, agents=6,  fan_out=6,  rounds=1, verify="all", extracts=2, verify_cap=20),
    "deep":     dict(sources=15, domains=6, agents=11, fan_out=10, rounds=2, verify="all", extracts=3, verify_cap=20),
    "max":      dict(sources=25, domains=8, agents=36, fan_out=12, rounds=3, verify="all", extracts=3, verify_cap=20),
}

VALID_DEPTHS = tuple(DEPTH.keys())


def contract(depth: str) -> Dict[str, Any]:
    """The contract for one tier; unknown depths fall back to standard."""
    return dict(DEPTH.get(depth, DEPTH["standard"]))


def min_sources(depth: str) -> int:
    return contract(depth)["sources"]


def min_domains(depth: str) -> int:
    return contract(depth)["domains"]


def agent_count(depth: str) -> int:
    return contract(depth)["agents"]


def gap_rounds(depth: str) -> int:
    return contract(depth)["rounds"]


def extracts_per_subtopic(depth: str) -> int:
    return contract(depth)["extracts"]


def verify_count(depth: str, claim_count: int) -> int:
    """How many claims MUST get an independent adversarial verifier."""
    c = contract(depth)
    if c["verify"] == "all":
        return min(claim_count, c["verify_cap"])
    return min(claim_count, int(c["verify"]))


# Effort → depth mapping for the swarm conductor (was RESEARCH_DEPTH_LABEL).
EFFORT_TO_DEPTH = {"low": "standard", "medium": "standard", "high": "deep"}


def _cli() -> int:
    import argparse
    p = argparse.ArgumentParser(prog="research_depth.py")
    p.add_argument("--depth", choices=VALID_DEPTHS, default=None)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    payload = contract(args.depth) if args.depth else DEPTH
    print(json.dumps(payload, indent=None if args.json else 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
