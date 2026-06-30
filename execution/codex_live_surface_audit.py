#!/usr/bin/env python3
"""Audit the Codex-native live skill surface.

Single-tree topology (canonical, 2026-06-30): the workspace is one live tree.
Every source-command wrapper lives in .agents/skills (no cold quarantine), and
the full workflow arsenal stays in .agent/workflows. The hot control-plane
commands must all be LIVE; the strict gate verifies that they are present and
that no live wrapper is missing its SKILL.md, rather than asserting the retired
two-tree split (small live surface + a 700-dir cold quarantine).
"""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LIVE_SKILLS = ROOT / ".agents" / "skills"
COLD_WRAPPERS = ROOT / ".agents" / "cold-skills" / "source-command-wrappers"
WORKFLOWS = ROOT / ".agent" / "workflows"
CLAUDE_COMMANDS = ROOT / ".claude" / "commands"
PREFIX = "source-command-"

HOT_COMMANDS = {
    "autopilot",
    "artifact-router",
    "buyer-trigger-os",
    "extract",
    "extract-amplify",
    "extract-forge",
    "extract-vision",
    "sam-parr-copywriting-mechanics",
    "video-source-extract",
    "video-transcript-ledger",
    "ai-employee-os",
    "end-session",
    "system-audit",
    "orchestrate",
    "mission",
    "repeatability-spine",
    "expert-composition-governor",
    "health-check",
    "routing-intelligence",
    "virtuoso",
    "self-evolve",
    "skill-anneal",
    "knowledge-librarian",
    "source-to-skill-system",
    "extraction-governor-agent",
    "session-calibrate",
    "project-coordinate",
    "project-onboard",
    "align",
    "devil",
    "burst",
    "tweak",
}

DUAL_MODE_COMMANDS = {
    "extract",
    "extract-amplify",
    "extract-forge",
    "extract-vision",
    "sam-parr-copywriting-mechanics",
    "video-source-extract",
    "video-transcript-ledger",
}


def command_skill_names(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {
        item.name.removeprefix(PREFIX)
        for item in path.glob(f"{PREFIX}*")
        if item.is_dir() and (item / "SKILL.md").exists()
    }


def source_command_dirs_missing_skill(path: Path) -> list[str]:
    if not path.exists():
        return []
    return sorted(
        item.name
        for item in path.glob(f"{PREFIX}*")
        if item.is_dir() and not (item / "SKILL.md").exists()
    )


def nonempty_dirs(path: Path, names: list[str]) -> list[str]:
    nonempty = []
    for name in names:
        item = path / name
        if item.exists() and any(item.iterdir()):
            nonempty.append(name)
    return nonempty


def dir_names(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {item.name for item in path.iterdir() if item.is_dir()}


def workflow_names() -> set[str]:
    if not WORKFLOWS.exists():
        return set()
    return {item.stem for item in WORKFLOWS.glob("*.md")}


def claude_command_names() -> set[str]:
    if not CLAUDE_COMMANDS.exists():
        return set()
    return {item.stem for item in CLAUDE_COMMANDS.glob("*.md")}


def build_report() -> dict[str, object]:
    live_all = dir_names(LIVE_SKILLS)
    live_commands = command_skill_names(LIVE_SKILLS)
    cold_commands = command_skill_names(COLD_WRAPPERS)
    live_missing_skill = source_command_dirs_missing_skill(LIVE_SKILLS)
    cold_missing_skill = source_command_dirs_missing_skill(COLD_WRAPPERS)
    workflows = workflow_names()
    claude_commands = claude_command_names()
    native_live = sorted(name for name in live_all if not name.startswith(PREFIX))

    return {
        "live_skill_count": len(live_all),
        "live_source_command_count": len(live_commands),
        "live_native_utility_count": len(native_live),
        "cold_source_command_count": len(cold_commands),
        "live_source_command_dirs_missing_skill_md": live_missing_skill,
        "cold_source_command_dirs_missing_skill_md": cold_missing_skill,
        "live_nonempty_source_command_dirs_missing_skill_md": nonempty_dirs(LIVE_SKILLS, live_missing_skill),
        "cold_nonempty_source_command_dirs_missing_skill_md": nonempty_dirs(COLD_WRAPPERS, cold_missing_skill),
        "workflow_count": len(workflows),
        "claude_legacy_command_count": len(claude_commands),
        "hot_expected": sorted(HOT_COMMANDS),
        "hot_live": sorted(live_commands & HOT_COMMANDS),
        "hot_missing": sorted(HOT_COMMANDS - live_commands),
        "hot_in_cold": sorted((HOT_COMMANDS & cold_commands) - DUAL_MODE_COMMANDS),
        "non_hot_live_commands": sorted(live_commands - HOT_COMMANDS),
        "native_live_skills": native_live,
        "cold_wrappers_with_workflows": len(cold_commands & workflows),
        "cold_wrappers_without_workflows": sorted(cold_commands - workflows),
        "workflows_without_live_or_cold_wrapper": len(workflows - live_commands - cold_commands),
        "claude_legacy_overlaps_workflows": len(claude_commands & workflows),
    }


def render_report(report: dict[str, object]) -> str:
    lines = [
        "# Codex Live Surface Audit",
        "",
        "## Summary",
        "",
        f"- Live skills: {report['live_skill_count']}",
        f"- Live source-command wrappers: {report['live_source_command_count']}",
        f"- Live native utility skills: {report['live_native_utility_count']}",
        f"- Cold source-command wrappers: {report['cold_source_command_count']}",
        f"- Live source-command dirs missing SKILL.md: {', '.join(report['live_source_command_dirs_missing_skill_md']) or 'none'}",
        f"- Cold source-command dirs missing SKILL.md: {', '.join(report['cold_source_command_dirs_missing_skill_md']) or 'none'}",
        f"- Workflows preserved: {report['workflow_count']}",
        f"- Legacy Claude commands preserved: {report['claude_legacy_command_count']}",
        f"- Cold wrappers with matching workflows: {report['cold_wrappers_with_workflows']}",
        f"- Claude legacy commands that overlap workflows: {report['claude_legacy_overlaps_workflows']}",
        "",
        "## Hot Control Plane",
        "",
        f"- Expected hot wrappers: {', '.join('/' + name for name in report['hot_expected'])}",
        f"- Live hot wrappers: {', '.join('/' + name for name in report['hot_live'])}",
        f"- Missing hot wrappers: {', '.join(report['hot_missing']) or 'none'}",
        f"- Hot wrappers accidentally cold: {', '.join(report['hot_in_cold']) or 'none'}",
        f"- Non-hot command wrappers still live: {', '.join(report['non_hot_live_commands']) or 'none'}",
        "",
        "## Native Utility Skills Still Live",
        "",
        f"- {', '.join(report['native_live_skills']) or 'none'}",
        "",
        "## Policy",
        "",
        "- .agent/workflows remains the executable arsenal.",
        "- .agents/skills is the live Codex control surface (single-tree: every wrapper lives here).",
        "- Hot control-plane commands must all be live; there is no cold quarantine.",
        "- Dual-mode command wrappers are allowed only when explicitly listed and validated.",
        "- .claude/commands remains legacy/source reference only.",
    ]

    cold_missing = report["cold_wrappers_without_workflows"]
    if cold_missing:
        lines.extend(
            [
                "",
                "## Cold Wrappers Without Matching Workflows",
                "",
            ]
        )
        lines.extend(f"- {name}" for name in cold_missing[:50])
        if len(cold_missing) > 50:
            lines.append(f"- ... {len(cold_missing) - 50} more")

    return "\n".join(lines)


def strict_failures(report: dict[str, object]) -> list[str]:
    """Strict gate for the canonical single-tree surface.

    The retired two-tree invariants (small live surface == len(HOT_COMMANDS), a
    700-dir cold quarantine, and "any non-hot wrapper live is a failure") no
    longer describe reality and have been dropped. The single-tree gate keeps
    the checks that still mean something: the hot control-plane commands must
    all be LIVE, no live wrapper may be missing its SKILL.md, and the workflow
    arsenal must be intact.
    """

    failures: list[str] = []
    # Hot control-plane commands must all be present and live.
    if report["hot_missing"]:
        failures.append(f"missing hot wrappers: {', '.join(report['hot_missing'])}")
    # Every live source-command dir must carry a SKILL.md.
    if report["live_nonempty_source_command_dirs_missing_skill_md"]:
        failures.append(
            "non-empty live source-command dirs missing SKILL.md: "
            + ", ".join(report["live_nonempty_source_command_dirs_missing_skill_md"])
        )
    # Single-tree: all source-command wrappers live here. The live wrapper count
    # must at least cover every hot command (the meaningful floor), not equal a
    # retired small-surface target.
    if report["live_source_command_count"] < len(HOT_COMMANDS):
        failures.append(
            f"live source-command wrapper count is {report['live_source_command_count']}, "
            f"expected at least {len(HOT_COMMANDS)} (all hot commands live)"
        )
    if report["workflow_count"] < 900:
        failures.append("workflow arsenal is unexpectedly small")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit the Codex-native live skill surface.")
    parser.add_argument("--strict", action="store_true", help="Fail if the live surface is not clean.")
    args = parser.parse_args()

    report = build_report()
    print(render_report(report))

    if not args.strict:
        return 0

    failures = strict_failures(report)
    if failures:
        print("\nStrict result: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nStrict result: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
