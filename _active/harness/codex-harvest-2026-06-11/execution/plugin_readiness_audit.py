#!/usr/bin/env python3
"""Plugin readiness scorecard for Antigravity workflows."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = ROOT / ".agent" / "workflows"
COMMAND_DIR = ROOT / ".claude" / "commands"
CODEX_SKILL_DIR = ROOT / ".agents" / "skills"
OUTPUT_DIR = ROOT / "deliverables" / "plugin-readiness"

DEFAULT_CANDIDATES = [
    "autopilot",
    "mission",
    "orchestrate",
    "extraction-governor-agent",
    "knowledge-librarian",
    "health-check",
    "routing-intelligence",
    "self-evolve",
]

BUNDLE_CANDIDATES = {
    "operator-core": DEFAULT_CANDIDATES,
    "revenue": [
        "first-10k",
        "revenue-offer-agent",
        "client-acquire",
        "zero-to-client-sprint",
        "service-first-productization",
        "cash-method",
        "profile-conversion",
        "ash-offer-test",
    ],
    "extraction": [
        "extraction-governor-agent",
        "extract-forge",
        "extract",
        "extract-vision",
        "extract-amplify",
        "video-context-ledger",
        "video-source-extract",
        "convert-extraction",
        "compile-knowledge",
        "knowledge-librarian",
    ],
    "creative": [
        "creative-brief-gen",
        "creative-design-agent",
        "design-brief",
        "higgsfield-studio",
        "mood-board",
        "creative-review",
        "anti-slop-audit",
        "design-taste-gate",
    ],
    "content": [
        "content-media-agent",
        "content-sprint",
        "content-orchestrate",
        "content-series-plan",
        "article-to-carousel",
        "ai-carousel-engine",
        "content-review-cycle",
        "platform-adapt",
    ],
    "client": [
        "client-delivery-agent",
        "client-acquire",
        "client-interview",
        "draft-proposal",
        "no-portfolio-client-landing",
        "blue-chip-client",
        "client-conversion",
        "24-assets-client-audit",
    ],
    "system": [
        "autopilot",
        "mission",
        "orchestrate",
        "plugin-readiness-audit",
        "health-check",
        "system-efficiency-benchmark",
        "routing-intelligence",
        "system-audit",
        "harness-audit",
        "context-audit",
        "bloat-optimizer",
        "self-evolve",
        "knowledge-librarian",
    ],
}

HOT_BASELINE = {
    "autopilot": (20, 20, 14, 15, 15, 15),
    "mission": (18, 18, 13, 15, 14, 12),
    "orchestrate": (17, 18, 12, 13, 14, 12),
    "extraction-governor-agent": (16, 18, 12, 14, 13, 13),
    "knowledge-librarian": (15, 17, 12, 14, 15, 12),
    "health-check": (15, 12, 14, 15, 14, 12),
    "routing-intelligence": (14, 14, 13, 14, 14, 13),
    "self-evolve": (13, 15, 13, 14, 12, 13),
}


@dataclass
class Score:
    name: str
    repetition: int
    reconstruction: int
    tool_needs: int
    verification: int
    portability: int
    failure_history: int
    workflow_exists: bool
    command_exists: bool
    codex_skill_exists: bool
    routing_count: int

    @property
    def total(self) -> int:
        return (
            self.repetition
            + self.reconstruction
            + self.tool_needs
            + self.verification
            + self.portability
            + self.failure_history
        )

    @property
    def decision(self) -> str:
        if self.total >= 80:
            return "PACKAGE NOW"
        if self.total >= 65:
            return "IMPROVE FIRST"
        if self.total >= 45:
            return "KEEP AS WORKFLOW"
        return "REFERENCE ONLY"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def routing_counts() -> dict[str, int]:
    path = ROOT / ".agent" / "routing-intelligence.json"
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    counts: dict[str, int] = {}
    for item in data.get("routing_decisions", []):
        workflow = item.get("workflow_used")
        if workflow:
            counts[workflow] = counts.get(workflow, 0) + 1
    return counts


def keyword_score(text: str, keywords: list[str], max_score: int) -> int:
    lowered = text.lower()
    hits = sum(1 for keyword in keywords if keyword in lowered)
    if not keywords:
        return 0
    return min(max_score, round((hits / len(keywords)) * max_score))


def score_candidate(name: str, route_counts: dict[str, int]) -> Score:
    workflow_path = WORKFLOW_DIR / f"{name}.md"
    command_path = COMMAND_DIR / f"{name}.md"
    skill_path = CODEX_SKILL_DIR / f"source-command-{name}" / "SKILL.md"

    workflow_exists = workflow_path.exists()
    command_exists = command_path.exists()
    codex_skill_exists = skill_path.exists()
    text = read_text(workflow_path)
    count = route_counts.get(name, 0)

    if name in HOT_BASELINE:
        repetition, reconstruction, tool_needs, verification, portability, failure_history = HOT_BASELINE[name]
    else:
        repetition = min(20, 4 + count * 5)
        reconstruction = keyword_score(
            text,
            ["intent", "pre-flight", "route", "clarity", "ask", "handoff", "state"],
            20,
        )
        tool_needs = keyword_score(
            text,
            ["python", "execution/", "mcp", "browser", "notion", "router", "workflow_router", "command_menu"],
            15,
        )
        verification = keyword_score(
            text,
            ["validate", "verify", "score", "health", "finalize", "test", "quality gate"],
            15,
        )
        portability = 3
        failure_history = keyword_score(
            text,
            ["failure", "risk", "misroute", "drift", "fallback", "missing", "stale"],
            15,
        )

    if workflow_exists:
        portability += 4
    if command_exists:
        portability += 4
    if codex_skill_exists:
        portability += 4
    portability = min(15, portability)

    if count:
        repetition = min(20, repetition + min(4, count * 2))

    if not workflow_exists:
        repetition = min(repetition, 4)
        reconstruction = min(reconstruction, 4)
        tool_needs = min(tool_needs, 4)
        verification = min(verification, 4)
        portability = min(portability, 4)
        failure_history = min(failure_history, 4)

    return Score(
        name=name,
        repetition=repetition,
        reconstruction=reconstruction,
        tool_needs=tool_needs,
        verification=verification,
        portability=portability,
        failure_history=failure_history,
        workflow_exists=workflow_exists,
        command_exists=command_exists,
        codex_skill_exists=codex_skill_exists,
        routing_count=count,
    )


def render(scores: list[Score], bundle_name: str = "operator-core") -> str:
    generated = datetime.now().strftime("%Y-%m-%d %H:%M")
    avg = round(sum(score.total for score in scores) / len(scores), 1) if scores else 0
    package_now = [score.name for score in scores if score.total >= 80]
    recommended = f"antigravity-{bundle_name}" if avg >= 80 else "improve workflow layer first"

    lines = [
        "# Plugin Readiness Scorecard",
        "",
        f"Generated: {generated}",
        f"Bundle: {bundle_name}",
        "",
        "## Verdict",
        "",
        f"- Bundle average: {avg}/100",
        f"- Package-now candidates: {', '.join(package_now) if package_now else 'None'}",
        f"- Recommended bundle: {recommended}",
        "",
        "## Score Table",
        "",
        "| Workflow | Rep | Rebuild | Tools | Verify | Port | Fail | Total | Decision | Bridge |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]

    for score in scores:
        bridge = "/".join(
            [
                "workflow" if score.workflow_exists else "no-workflow",
                "command" if score.command_exists else "no-command",
                "skill" if score.codex_skill_exists else "no-skill",
            ]
        )
        lines.append(
            f"| `{score.name}` | {score.repetition} | {score.reconstruction} | {score.tool_needs} | "
            f"{score.verification} | {score.portability} | {score.failure_history} | "
            f"{score.total} | {score.decision} | {bridge} |"
        )

    lines.extend(
        [
            "",
            "## Plugin Acceptance Tests",
            "",
            "1. Direct invocation names the plugin or bundled skill.",
            "2. Natural-language request triggers the operating layer without magic words.",
            "3. Missing information produces one small question or explicit assumptions.",
            "4. Local paths resolve after installation from the repo marketplace.",
            "5. A fresh Codex thread can use the plugin after restart.",
            "",
            "## Before/After Proof Protocol",
            "",
            "Use the same raw request before and after installation:",
            "",
            "> I have messy context and do not know which Antigravity workflow to use. Route it, state the plan, and start the first safe action.",
            "",
            "Before packaging, record whether the agent asks the user to reconstruct the system. After packaging, record whether it loads the operator-core route and names the checks without extra setup.",
            "",
            "## Notes",
            "",
            "- Scores are local decision support, not a public quality claim.",
            "- A plugin should only wrap stable workflow behavior; it should not replace the existing Antigravity routers.",
            "- Add MCP, apps, or hooks only after the base plugin can install and trigger.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_bundle_matrix(bundle_names: list[str]) -> str:
    route_counts = routing_counts()
    generated = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# Plugin Readiness Bundle Matrix",
        "",
        f"Generated: {generated}",
        "",
        "| Bundle | Avg | Package Now | Improve First | Missing Workflows | Recommendation |",
        "|---|---:|---:|---:|---:|---|",
    ]
    sections: list[str] = []
    for bundle_name in bundle_names:
        scores = [score_candidate(name, route_counts) for name in BUNDLE_CANDIDATES[bundle_name]]
        avg = round(sum(score.total for score in scores) / len(scores), 1) if scores else 0
        package_now = sum(1 for score in scores if score.total >= 80)
        improve_first = sum(1 for score in scores if 65 <= score.total < 80)
        missing = sum(1 for score in scores if not score.workflow_exists)
        if avg >= 85 and missing == 0:
            recommendation = "package candidate"
        elif avg >= 70:
            recommendation = "harden first"
        else:
            recommendation = "keep as workflows"
        lines.append(
            f"| `{bundle_name}` | {avg} | {package_now} | {improve_first} | {missing} | {recommendation} |"
        )
        sections.append(render(scores, bundle_name=bundle_name))

    lines.extend(["", "## Bundle Details", ""])
    lines.extend(sections)
    return "\n\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Score workflows for Codex plugin packaging readiness.")
    parser.add_argument("candidates", nargs="*", help="Workflow names to score. Defaults to the hot operating layer.")
    parser.add_argument("--bundle", choices=sorted(BUNDLE_CANDIDATES), help="Score a predefined workflow family.")
    parser.add_argument("--all-bundles", action="store_true", help="Score all predefined workflow families.")
    parser.add_argument("--stdout", action="store_true", help="Print only; do not write a scorecard file. This is the default.")
    parser.add_argument("--out", help="Write the markdown scorecard to this explicit path.")
    args = parser.parse_args()

    if args.all_bundles:
        report = render_bundle_matrix(sorted(BUNDLE_CANDIDATES))
    else:
        bundle_name = args.bundle or "operator-core"
        candidates = args.candidates or BUNDLE_CANDIDATES.get(bundle_name, DEFAULT_CANDIDATES)
        scores = [score_candidate(name, routing_counts()) for name in candidates]
        report = render(scores, bundle_name=bundle_name)

    if args.out:
        out_path = Path(args.out)
        if not out_path.is_absolute():
            out_path = ROOT / out_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report, encoding="utf-8")
        print(report)
        print(f"Scorecard written to: {out_path}")
    else:
        print(report)
        print("Scorecard write skipped: pass --out <path> to persist this report.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
