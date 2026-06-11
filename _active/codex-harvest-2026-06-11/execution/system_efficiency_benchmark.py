#!/usr/bin/env python3
"""Measure Antigravity routing efficiency before broad plugin packaging."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from plugin_readiness_audit import BUNDLE_CANDIDATES, routing_counts, score_candidate


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "deliverables" / "system-efficiency"
ROUTING_DATA = ROOT / ".agent" / "routing-intelligence.json"
PERFORMANCE_LOG = ROOT / ".agent" / "performance-log.jsonl"

PLUGIN_OPERATOR_CORE = {
    "autopilot",
    "mission",
    "orchestrate",
    "extraction-governor-agent",
    "knowledge-librarian",
    "health-check",
    "routing-intelligence",
    "self-evolve",
    "plugin-readiness-audit",
}


@dataclass(frozen=True)
class PromptCase:
    name: str
    prompt: str
    expected: tuple[str, ...]
    family: str


@dataclass
class RouterResult:
    routes: list[str]
    elapsed_ms: float
    ok: bool
    error: str = ""


PROMPT_CASES = [
    PromptCase(
        name="messy raw context",
        prompt="I have messy raw notes and I do not know which workflow to use. Verify intent, route it, and start safely.",
        expected=("autopilot",),
        family="system",
    ),
    PromptCase(
        name="revenue sprint",
        prompt="I need the fastest legitimate path to make 500 to 1000 dollars in the next 48 hours with a client offer.",
        expected=("first-10k", "revenue-offer-agent", "client-acquire", "zero-to-client-sprint", "service-first-productization"),
        family="revenue",
    ),
    PromptCase(
        name="extraction source",
        prompt="Turn this source material into reusable Antigravity commands, extract the hidden mechanics, and avoid duplicate systems.",
        expected=("extraction-governor-agent", "extract-forge", "convert-extraction", "compile-knowledge"),
        family="extraction",
    ),
    PromptCase(
        name="creative brief",
        prompt="Build a strong creative brief and anti-slop visual direction before we generate images or videos.",
        expected=("creative-brief-gen", "design-brief", "creative-design-agent", "higgsfield-studio"),
        family="creative",
    ),
    PromptCase(
        name="client audit",
        prompt="Create a client audit and delivery plan that turns diagnosis into a paid implementation path.",
        expected=("client-delivery-agent", "24-assets-client-audit", "client-interview", "draft-proposal"),
        family="client",
    ),
    PromptCase(
        name="system health",
        prompt="Run a quick Antigravity system health check and tell me what is active, stale, or blocked.",
        expected=("health-check",),
        family="system",
    ),
    PromptCase(
        name="plugin readiness",
        prompt="Audit whether this workflow family should become a Codex plugin or stay as workflows and skills.",
        expected=("plugin-readiness-audit",),
        family="system",
    ),
    PromptCase(
        name="command bloat",
        prompt="Tell me if this system has command bloat, too many skills, or routing overhead, and what to tighten first.",
        expected=("system-efficiency-benchmark", "bloat-optimizer", "context-audit", "system-hygiene"),
        family="system",
    ),
    PromptCase(
        name="self evolution",
        prompt="Use the system's feedback and failure history to improve the workflow without adding unnecessary bloat.",
        expected=("self-evolve", "routing-intelligence"),
        family="system",
    ),
    PromptCase(
        name="knowledge retrieval",
        prompt="Search the Antigravity knowledge library for prior decisions and retrieve the best reusable context.",
        expected=("knowledge-librarian", "knowledge-search", "compile-knowledge"),
        family="system",
    ),
]


def run_router(script: str, query: str) -> RouterResult:
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            [sys.executable, f"execution/{script}", "search", query],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
    except OSError as exc:
        return RouterResult(routes=[], elapsed_ms=0.0, ok=False, error=str(exc))

    elapsed_ms = (time.perf_counter() - started) * 1000
    output = completed.stdout + completed.stderr
    if script == "command_menu.py":
        routes = parse_command_menu(output)
    else:
        routes = parse_workflow_router(output)
    return RouterResult(
        routes=routes,
        elapsed_ms=elapsed_ms,
        ok=completed.returncode == 0,
        error="" if completed.returncode == 0 else output.strip()[:500],
    )


def parse_command_menu(output: str) -> list[str]:
    routes = []
    for match in re.finditer(r"^\d+\.\s+`/([^`]+)`", output, re.MULTILINE):
        routes.append(match.group(1))
    return routes


def parse_workflow_router(output: str) -> list[str]:
    routes = []
    for match in re.finditer(r"^\s+/([a-z0-9][a-z0-9-]*)\s+", output, re.MULTILINE):
        routes.append(match.group(1))
    return routes


def rank(routes: list[str], expected: tuple[str, ...]) -> int | None:
    for index, route in enumerate(routes, start=1):
        if route in expected:
            return index
    return None


def quality_from_rank(position: int | None) -> int:
    if position == 1:
        return 10
    if position is not None and position <= 3:
        return 7
    if position is not None and position <= 5:
        return 5
    if position is not None and position <= 10:
        return 3
    return 0


def projected_cleanup_quality(current_rank: int | None, routes: list[str], expected: tuple[str, ...]) -> int:
    if current_rank == 1:
        return 10
    if current_rank is not None:
        return 10
    if any((ROOT / ".agent" / "workflows" / f"{name}.md").exists() for name in expected):
        return 7
    if routes:
        return 3
    return 0


def projected_plugin_quality(current_quality: int, case: PromptCase) -> int:
    if any(name in PLUGIN_OPERATOR_CORE for name in case.expected):
        return max(current_quality, 10)
    return current_quality


def dir_size(path: Path) -> int:
    total = 0
    if not path.exists():
        return total
    for root, _, files in os.walk(path):
        for name in files:
            file_path = Path(root) / name
            try:
                total += file_path.stat().st_size
            except OSError:
                continue
    return total


def human_size(size: int) -> str:
    value = float(size)
    for unit in ["B", "KB", "MB", "GB"]:
        if value < 1024 or unit == "GB":
            return f"{value:.1f} {unit}"
        value /= 1024
    return f"{value:.1f} GB"


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def workflow_names() -> list[str]:
    return sorted(path.stem for path in (ROOT / ".agent" / "workflows").glob("*.md"))


def command_skill_names() -> list[str]:
    skill_dir = ROOT / ".agents" / "skills"
    return sorted(path.name.removeprefix("source-command-") for path in skill_dir.glob("source-command-*") if path.is_dir())


def root_skill_names() -> list[str]:
    skill_dir = ROOT / "skills"
    return sorted(path.name for path in skill_dir.iterdir() if path.is_dir() and (path / "SKILL.md").exists())


def routing_feedback_summary() -> dict[str, int | float]:
    data = read_json(ROUTING_DATA)
    decisions = data.get("routing_decisions", [])
    feedback_log = data.get("feedback_log", [])
    inline_feedback = [item for item in decisions if item.get("feedback")]
    total_feedback = len(feedback_log) + len(inline_feedback)
    total_decisions = len(decisions)
    coverage = round((total_feedback / total_decisions) * 100, 1) if total_decisions else 0.0
    return {
        "decisions": total_decisions,
        "feedback": total_feedback,
        "coverage": coverage,
    }


def performance_entries() -> int:
    if not PERFORMANCE_LOG.exists():
        return 0
    try:
        return sum(1 for line in PERFORMANCE_LOG.read_text(encoding="utf-8", errors="ignore").splitlines() if line.strip())
    except OSError:
        return 0


def bundle_scores() -> list[dict[str, object]]:
    route_counts = routing_counts()
    rows = []
    for bundle_name in sorted(BUNDLE_CANDIDATES):
        scores = [score_candidate(name, route_counts) for name in BUNDLE_CANDIDATES[bundle_name]]
        avg = round(sum(score.total for score in scores) / len(scores), 1) if scores else 0.0
        missing = sum(1 for score in scores if not score.workflow_exists)
        package_now = sum(1 for score in scores if score.total >= 80)
        improve_first = sum(1 for score in scores if 65 <= score.total < 80)
        if avg >= 85 and missing == 0:
            recommendation = "package candidate"
        elif avg >= 70:
            recommendation = "harden first"
        else:
            recommendation = "keep as workflows"
        rows.append(
            {
                "bundle": bundle_name,
                "avg": avg,
                "missing": missing,
                "package_now": package_now,
                "improve_first": improve_first,
                "recommendation": recommendation,
            }
        )
    return rows


def hot_cold_tiers(case_rows: list[dict[str, object]]) -> dict[str, object]:
    route_counts = routing_counts()
    workflows = set(workflow_names())
    hot = set(PLUGIN_OPERATOR_CORE)
    hot.update(route_counts)
    for row in case_rows:
        hot.update(row["command_menu_routes"][:3])
        hot.update(row["workflow_router_routes"][:3])
        hot.update(row["expected"])
    warm = set()
    for candidates in BUNDLE_CANDIDATES.values():
        warm.update(candidates)
    cold = sorted(name for name in workflows if name not in hot and name not in warm and route_counts.get(name, 0) == 0)
    return {
        "hot": sorted(name for name in hot if name in workflows),
        "warm_count": len([name for name in warm if name in workflows and name not in hot]),
        "cold_count": len(cold),
        "cold_sample": cold[:25],
    }


def run_cases() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in PROMPT_CASES:
        command = run_router("command_menu.py", case.prompt)
        workflow = run_router("workflow_router.py", case.prompt)
        command_rank = rank(command.routes, case.expected)
        workflow_rank = rank(workflow.routes, case.expected)
        current_quality = max(quality_from_rank(command_rank), quality_from_rank(workflow_rank))
        cleanup_quality = max(
            projected_cleanup_quality(command_rank, command.routes, case.expected),
            projected_cleanup_quality(workflow_rank, workflow.routes, case.expected),
        )
        plugin_quality = projected_plugin_quality(current_quality, case)
        rows.append(
            {
                "case": case.name,
                "family": case.family,
                "prompt": case.prompt,
                "expected": list(case.expected),
                "command_menu_routes": command.routes,
                "workflow_router_routes": workflow.routes,
                "command_rank": command_rank,
                "workflow_rank": workflow_rank,
                "command_ms": command.elapsed_ms,
                "workflow_ms": workflow.elapsed_ms,
                "current_quality": current_quality,
                "cleanup_quality": cleanup_quality,
                "plugin_quality": plugin_quality,
                "command_ok": command.ok,
                "workflow_ok": workflow.ok,
                "error": command.error or workflow.error,
            }
        )
    return rows


def avg(values: list[float]) -> float:
    return round(sum(values) / len(values), 1) if values else 0.0


def rank_label(value: int | None) -> str:
    return str(value) if value is not None else "miss"


def route_label(routes: list[str]) -> str:
    return f"/{routes[0]}" if routes else "none"


def build_report(rows: list[dict[str, object]]) -> str:
    generated = datetime.now().strftime("%Y-%m-%d %H:%M")
    feedback = routing_feedback_summary()
    bundles = bundle_scores()
    tiers = hot_cold_tiers(rows)
    workflows = workflow_names()
    command_skills = command_skill_names()
    root_skills = root_skill_names()

    current_quality = avg([float(row["current_quality"]) for row in rows])
    cleanup_quality = avg([float(row["cleanup_quality"]) for row in rows])
    plugin_quality = avg([float(row["plugin_quality"]) for row in rows])
    command_latency = avg([float(row["command_ms"]) for row in rows])
    workflow_latency = avg([float(row["workflow_ms"]) for row in rows])
    first_choice_hits = sum(
        1
        for row in rows
        if row["command_rank"] == 1 or row["workflow_rank"] == 1
    )
    reconstruction_burden = len(rows) - first_choice_hits

    if plugin_quality > cleanup_quality:
        verdict = "Selective packaging is worth testing for the operator core, but broad packaging still needs proof."
    elif cleanup_quality > current_quality:
        verdict = "Router and metadata cleanup should come before more plugin packaging."
    else:
        verdict = "Current routing is functional; the next bottleneck is feedback coverage, not packaging volume."

    if current_quality >= 9.5 and reconstruction_burden == 0:
        cleanup_recommendation = "Already achieved"
        plugin_recommendation = "Hold; fresh-session test only"
        next_steps = [
            "1. Log feedback on real routing outcomes so cold-tier decisions stop being guesswork.",
            "2. Fresh-session test `antigravity-operator-core` before expanding packaging.",
            "3. Re-run this benchmark after at least 10 new routing decisions with feedback.",
            "4. Keep revenue, creative, content, and client bundles as workflows until usage evidence changes.",
            "5. Use this benchmark as the regression gate before future router or plugin changes.",
        ]
    else:
        cleanup_recommendation = "Do first"
        plugin_recommendation = "Test selectively"
        next_steps = [
            "1. Tighten router metadata for missed or low-rank benchmark cases.",
            "2. Improve `knowledge-librarian` before packaging more bundles.",
            "3. Log feedback on real routing outcomes so cold-tier decisions stop being guesswork.",
            "4. Re-run this benchmark after metadata cleanup.",
            "5. Package only a bundle that beats the cleanup-only projection.",
        ]

    lines = [
        "# System Efficiency Benchmark",
        "",
        f"Generated: {generated}",
        "",
        "## Verdict",
        "",
        f"- {verdict}",
        "- Do not package the whole Antigravity system in this pass.",
        "- Treat plugin packaging as one optimization beside router weighting, metadata cleanup, skill description tightening, deterministic checks, and workflow consolidation.",
        "- Archive nothing from this report alone; cold workflows need usage evidence before removal.",
        "",
        "## Benchmark Summary",
        "",
        f"- Prompt cases: {len(rows)}",
        f"- First-choice route hits: {first_choice_hits}/{len(rows)}",
        f"- Reconstruction burden: {reconstruction_burden}/{len(rows)} cases were not clean first-choice wins.",
        f"- Command menu average latency: {command_latency} ms",
        f"- Workflow router average latency: {workflow_latency} ms",
        f"- Current quality score: {current_quality}/10",
        f"- Router/metadata cleanup projection: {cleanup_quality}/10",
        f"- Operator-core plugin projection: {plugin_quality}/10",
        "",
        "## Variant Comparison",
        "",
        "| Variant | Quality | Speed Expectation | Reconstruction Burden | Recommendation |",
        "|---|---:|---|---|---|",
        f"| Current state | {current_quality}/10 | Measured: {command_latency} ms menu, {workflow_latency} ms router | {reconstruction_burden}/{len(rows)} | Keep as baseline |",
        f"| Router/metadata cleanup only | {cleanup_quality}/10 | Same or slightly faster | Lower where expected routes already exist | {cleanup_recommendation} |",
        f"| Plugin-packaged bundle | {plugin_quality}/10 | Not assumed faster | Helps only bundled operator-core routes | {plugin_recommendation} |",
        "",
        "## Route Results",
        "",
        "| Case | Expected | Command Top | Cmd Rank | Router Top | Router Rank | Current | Cleanup | Plugin |",
        "|---|---|---|---:|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        expected = ", ".join(f"/{item}" for item in row["expected"])
        lines.append(
            f"| {row['case']} | {expected} | {route_label(row['command_menu_routes'])} | "
            f"{rank_label(row['command_rank'])} | {route_label(row['workflow_router_routes'])} | "
            f"{rank_label(row['workflow_rank'])} | {row['current_quality']} | "
            f"{row['cleanup_quality']} | {row['plugin_quality']} |"
        )

    lines.extend(
        [
            "",
            "## Context Footprint",
            "",
            f"- Workflows: {len(workflows)}",
            f"- Claude source commands: {len(list((ROOT / '.claude' / 'commands').glob('*.md')))}",
            f"- Codex command skills: {len(command_skills)}",
            f"- Root skills: {len(root_skills)}",
            f"- Repo-local plugins: {len(list((ROOT / 'plugins').glob('*')))}",
            f"- `.agent/workflows` size: {human_size(dir_size(ROOT / '.agent' / 'workflows'))}",
            f"- `.agents/skills` size: {human_size(dir_size(ROOT / '.agents' / 'skills'))}",
            f"- `skills` size: {human_size(dir_size(ROOT / 'skills'))}",
            f"- `plugins` size: {human_size(dir_size(ROOT / 'plugins'))}",
            "",
            "## Feedback Coverage",
            "",
            f"- Routing decisions logged: {feedback['decisions']}",
            f"- Feedback entries logged: {feedback['feedback']}",
            f"- Feedback coverage: {feedback['coverage']}%",
            f"- Performance log entries: {performance_entries()}",
            "- Broad packaging should stay blocked until routing feedback is meaningfully higher.",
            "",
            "## Bundle Readiness",
            "",
            "| Bundle | Avg | Package Now | Improve First | Missing | Recommendation |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    for bundle in bundles:
        lines.append(
            f"| `{bundle['bundle']}` | {bundle['avg']} | {bundle['package_now']} | "
            f"{bundle['improve_first']} | {bundle['missing']} | {bundle['recommendation']} |"
        )

    lines.extend(
        [
            "",
            "## Hot/Cold Tier Recommendation",
            "",
            f"- Hot surfaced workflows: {', '.join('/' + name for name in tiers['hot'][:40])}",
            f"- Warm bundle candidates still on disk: {tiers['warm_count']}",
            f"- Cold workflow count: {tiers['cold_count']}",
            f"- Cold sample: {', '.join('/' + name for name in tiers['cold_sample']) if tiers['cold_sample'] else 'None'}",
            "",
            "Recommendation: keep hot workflows surfaced, leave cold workflows on disk, and do not archive until routing logs or repeated benchmark misses prove they are dead weight.",
            "",
            "## Next Optimization Order",
            "",
            *next_steps,
        ]
    )

    errors = [row for row in rows if row["error"]]
    if errors:
        lines.extend(["", "## Router Errors", ""])
        for row in errors:
            lines.append(f"- {row['case']}: {row['error']}")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Benchmark Antigravity routing efficiency before plugin expansion.")
    parser.add_argument("--out", help="Markdown report path. Defaults to deliverables/system-efficiency/system-efficiency-baseline.md.")
    args = parser.parse_args()

    rows = run_cases()
    report = build_report(rows)

    out_path = Path(args.out) if args.out else OUTPUT_DIR / "system-efficiency-baseline.md"
    if not out_path.is_absolute():
        out_path = ROOT / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")
    print(report)
    print(f"Benchmark written to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
