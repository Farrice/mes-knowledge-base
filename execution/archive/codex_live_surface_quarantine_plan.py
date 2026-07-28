#!/usr/bin/env python3
"""Write a dry-run plan for quarantining non-hot source-command wrappers."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import codex_live_surface_audit as live_surface


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / ".tmp" / "codex-live-surface-quarantine-plan.json"


def build_plan() -> dict[str, Any]:
    report = live_surface.build_report()
    moves = []
    for name in report["non_hot_live_commands"]:
        source = live_surface.LIVE_SKILLS / f"{live_surface.PREFIX}{name}"
        destination = live_surface.COLD_WRAPPERS / f"{live_surface.PREFIX}{name}"
        moves.append(
            {
                "command": name,
                "source": str(source),
                "destination": str(destination),
                "action": "move_to_cold_quarantine",
                "requires_approval": True,
            }
        )

    return {
        "schema_version": "codex-live-surface-quarantine-plan/v1",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "mode": "dry_run",
        "policy": "Do not apply without explicit approval. Hot wrappers remain live; workflows remain executable.",
        "hot_expected": report["hot_expected"],
        "hot_live": report["hot_live"],
        "hot_missing": report["hot_missing"],
        "non_hot_live_count": len(report["non_hot_live_commands"]),
        "cold_source_command_count": report["cold_source_command_count"],
        "moves": moves,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a dry-run non-hot wrapper quarantine plan.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Plan JSON output path.")
    parser.add_argument("--json", action="store_true", help="Print the plan JSON after writing it.")
    args = parser.parse_args()

    plan = build_plan()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if args.json:
        print(json.dumps(plan, indent=2, sort_keys=True))
    else:
        print(f"Dry-run quarantine plan written: {output}")
        print(f"Non-hot live wrappers: {plan['non_hot_live_count']}")
        print("No files were moved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
