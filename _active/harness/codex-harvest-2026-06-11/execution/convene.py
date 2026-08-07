#!/usr/bin/env python3
"""Codex-native /convene helper.

The original Google workflow used Claude Workflow JS primitives. In Codex this
helper emits the same council contract as concrete packets and receipts while
keeping real subagents approval-gated.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

try:
    from kimi_swarm import build_general_packet, render_markdown
except ImportError:
    from execution.kimi_swarm import build_general_packet, render_markdown


def _cli() -> int:
    parser = argparse.ArgumentParser(prog="convene.py")
    sub = parser.add_subparsers(dest="cmd")
    plan = sub.add_parser("plan", help="Compile a Collective Genius Council packet plan")
    plan.add_argument("task")
    plan.add_argument("--mode", default="wide", choices=["wide", "tight", "strike", "deploy"])
    plan.add_argument("--allow-subagents", action="store_true")
    plan.add_argument("--json", action="store_true")

    args = parser.parse_args()
    if args.cmd != "plan":
        parser.error("subcommand required: plan")
    result = build_general_packet(args.task, convene_mode=args.mode, allow_subagents=args.allow_subagents)
    print(json.dumps(result, indent=2) if args.json else render_markdown(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
