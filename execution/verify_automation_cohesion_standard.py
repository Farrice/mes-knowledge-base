#!/usr/bin/env python3
"""Verify Codex app automations follow the Antigravity cohesion standard.

The automations live in the user's Codex home, while the standard lives in
this workspace. This verifier is read-only and intentionally checks prompts
instead of rewriting automation files.
"""

from __future__ import annotations

import os
import re
import sys
import tomllib
from datetime import date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AUTOMATION_ROOT = Path.home() / ".codex" / "automations"
WORKSPACE = "/Users/farricecain/Google Antigravity"
RUNNER = ROOT / "execution" / "recurring_ops.py"


EXPECTED = {
    "daily-antigravity-health": {
        "status": "ACTIVE",
        "schedule": ("BYHOUR=8", "BYMINUTE=0"),
        "memory_max_age_days": 2,
        "phrases": (
            "execution/recurring_ops.py daily-health",
            ".agent/intent-memory/current.json",
            ".agent/system-cohesion-state.json",
            "Activation Governor",
            "/autopilot",
            "/system-audit",
            "Do not apply upgrades",
            "promote performance entries",
            "write external systems",
        ),
    },
    "weekly-system-pulse": {
        "status": "ACTIVE",
        "schedule": ("BYDAY=MO", "BYHOUR=8", "BYMINUTE=30"),
        "memory_max_age_days": 8,
        "phrases": (
            "execution/recurring_ops.py weekly-system-pulse",
            "System Cohesion Platter",
            "intent memory",
            "shared cohesion state",
            "Activation Governor",
            "Pantry -> Prep -> Plate",
            "one chosen route",
            "Do not apply upgrades",
            "write external systems",
        ),
    },
    "monthly-hygiene-evolution-review": {
        "status": "ACTIVE",
        "schedule": ("BYDAY=MO", "BYHOUR=9", "BYMINUTE=0"),
        "memory_max_age_days": 8,
        "phrases": (
            "execution/recurring_ops.py monthly-hygiene-review",
            "automation drift",
            "current cohesion standard",
            "/autopilot",
            "intent memory",
            "shared system-cohesion state",
            "Activation Governor",
            "weekly System Cohesion Platter",
            "Queue no unsupervised repo changes",
        ),
    },
    "system-governor-queue": {
        "status": "ACTIVE",
        "schedule": ("BYDAY=MO", "BYHOUR=9", "BYMINUTE=30"),
        "memory_max_age_days": 8,
        "phrases": (
            "execution/recurring_ops.py system-governor",
            ".agent/intent-memory/current.json",
            ".agent/system-cohesion-state.json",
            "weekly System Cohesion Platter",
            "Activation Governor",
            "supervised upgrade queue",
            "one chosen next route",
            "Do not apply upgrades automatically",
            "without explicit approval",
        ),
    },
    "hybrid-morning-signal-radar": {
        "status": "PAUSED",
        "schedule": ("BYHOUR=6", "BYMINUTE=30"),
        "paused_memory_phrases": (
            "Pause Decision",
            "paused, not deleted",
            "Resume condition",
            "one clear daily action",
        ),
        "phrases": (
            "execution/hybrid_morning_signal_radar.py",
            "intent memory",
            "cohesion state",
            "Rendered Conversation Document",
            "Do not publish",
            "send outreach",
            "scrape LinkedIn",
            "write external systems",
            "local fallback brief",
        ),
    },
}

RUNNER_REQUIRED_PHRASES = (
    "Automation Cohesion",
    "automation_cohesion_status",
    "intent-memory",
    "current.json",
    "system-cohesion-state.json",
    "verify_automation_cohesion_standard.py",
    "activation_queue",
    "weekly_platter",
    "automation drift",
    "global_dry_run",
    "TimeoutExpired",
)

UNSAFE_MUTATION_PATTERNS = (
    "activate all protocols",
    "mass activate",
    "auto-activate",
    "automatically activate protocols",
    "promote performance entries automatically",
    "auto-promote performance",
    "write external systems automatically",
    "publish automatically",
    "send outreach automatically",
    "create new automations automatically",
)


def automation_root() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home) / "automations"
    return DEFAULT_AUTOMATION_ROOT


def load_automation(path: Path) -> dict:
    with path.open("rb") as file:
        return tomllib.load(file)


def contains_all(text: str, phrases: tuple[str, ...]) -> list[str]:
    lowered = text.lower()
    return [phrase for phrase in phrases if phrase.lower() not in lowered]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def latest_date(text: str) -> date | None:
    dates: list[date] = []
    for match in re.findall(r"\b20\d{2}-\d{2}-\d{2}\b", text):
        try:
            dates.append(datetime.strptime(match, "%Y-%m-%d").date())
        except ValueError:
            continue
    return max(dates) if dates else None


def unsafe_mutation_hits(text: str) -> list[str]:
    lowered = text.lower()
    hits: list[str] = []
    for pattern in UNSAFE_MUTATION_PATTERNS:
        start = lowered.find(pattern)
        while start != -1:
            before = lowered[max(0, start - 180) : start]
            after = lowered[start : start + len(pattern) + 96]
            guarded = (
                "do not" in before
                or "don't" in before
                or "without explicit approval" in after
                or "requires explicit approval" in after
            )
            if not guarded:
                hits.append(pattern)
                break
            start = lowered.find(pattern, start + len(pattern))
    return hits


def check_runner_contract(failures: list[str]) -> None:
    if not RUNNER.exists():
        failures.append("recurring_ops.py: missing runner")
        return
    text = read_text(RUNNER)
    for phrase in contains_all(text, RUNNER_REQUIRED_PHRASES):
        failures.append(f"recurring_ops.py: missing runner cohesion phrase {phrase!r}")
    unsafe = unsafe_mutation_hits(text)
    for phrase in unsafe:
        failures.append(f"recurring_ops.py: unsafe unsupervised mutation phrase {phrase!r}")


def check_memory_contract(root: Path, automation_id: str, spec: dict, failures: list[str]) -> None:
    memory_path = root / automation_id / "memory.md"
    if not memory_path.exists():
        failures.append(f"{automation_id}: missing automation memory.md")
        return
    text = read_text(memory_path)
    if spec["status"] == "PAUSED":
        for phrase in contains_all(text, spec.get("paused_memory_phrases", ())):
            failures.append(f"{automation_id}: paused memory missing {phrase!r}")
        return
    if "Last run" not in text:
        failures.append(f"{automation_id}: active memory missing 'Last run'")
    latest = latest_date(text)
    if latest is None:
        failures.append(f"{automation_id}: active memory missing YYYY-MM-DD run date")
        return
    max_age = int(spec.get("memory_max_age_days", 8))
    age_days = (date.today() - latest).days
    if age_days > max_age:
        failures.append(
            f"{automation_id}: automation memory is stale ({age_days} days old; max {max_age})"
        )


def main() -> int:
    root = automation_root()
    failures: list[str] = []
    if not root.exists():
        print(f"Automation root not found: {root}")
        return 1

    check_runner_contract(failures)

    for automation_id, spec in EXPECTED.items():
        path = root / automation_id / "automation.toml"
        if not path.exists():
            failures.append(f"{automation_id}: missing automation.toml")
            continue
        data = load_automation(path)
        prompt = str(data.get("prompt", ""))
        rrule = str(data.get("rrule", ""))
        cwds = data.get("cwds", [])

        if data.get("kind") != "cron":
            failures.append(f"{automation_id}: kind should be cron")
        if data.get("status") != spec["status"]:
            failures.append(f"{automation_id}: status should be {spec['status']}")
        if WORKSPACE not in cwds:
            failures.append(f"{automation_id}: cwd should include {WORKSPACE}")
        for token in spec["schedule"]:
            if token not in rrule:
                failures.append(f"{automation_id}: schedule missing {token}")
        missing = contains_all(prompt, spec["phrases"])
        for phrase in missing:
            failures.append(f"{automation_id}: prompt missing {phrase!r}")
        for phrase in unsafe_mutation_hits(prompt):
            failures.append(f"{automation_id}: unsafe unsupervised mutation phrase {phrase!r}")
        check_memory_contract(root, automation_id, spec, failures)

    if failures:
        print("Automation cohesion standard: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Automation cohesion standard: PASS")
    print(f"- checked {len(EXPECTED)} automations under {root}")
    print("- prompts preserve intent memory, cohesion state, proof spine, activation queue, and approval boundaries")
    print("- runner prints Automation Cohesion context for recurring reports")
    print("- automation memories meet active freshness or paused-rationale expectations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
