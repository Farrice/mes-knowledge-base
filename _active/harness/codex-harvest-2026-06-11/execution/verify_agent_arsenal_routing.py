#!/usr/bin/env python3
"""Verify agent arsenal routing, stacking, and interop migration coverage."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CONTRACT = ROOT / "semantic_libraries" / "antigravity" / "primitives" / "agent-arsenal-routing-contract.md"
REGISTRY = ROOT / "semantic_libraries" / "antigravity" / "stacking" / "agent-stacking-registry.json"
REGISTRY_MD = ROOT / "semantic_libraries" / "antigravity" / "stacking" / "agent-stacking-registry.md"
CODEX = ROOT / "CODEX.md"
AGENTS_DIR = ROOT / "agents"
WORKFLOWS_DIR = ROOT / ".agent" / "workflows"
RECOMMEND_STACK = ROOT / "execution" / "recommend_stack.py"

OPERATOR_SLUGS = [
    "ideation-agent",
    "content-media-agent",
    "marketing-agent",
    "creative-design-agent",
    "copywriting-agent",
    "writing-agent",
    "messaging-positioning-agent",
    "revenue-offer-agent",
    "client-delivery-agent",
    "proof-case-study-agent",
    "extraction-governor-agent",
    "research-intelligence-agent",
    "data-analysis-agent",
    "ground-truth-agent",
    "red-team-agent",
    "quality-judge",
    "evolution-agent",
]

TRACE_FIELDS = [
    "Objective",
    "Router candidates",
    "Seed workflows considered",
    "Stacking candidates",
    "Chosen route",
    "Gates",
    "Skipped and why",
    "Verification",
    "First action",
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def workflow_path(slug: str) -> Path:
    direct = WORKFLOWS_DIR / f"{slug}.md"
    if direct.exists():
        return direct
    return WORKFLOWS_DIR / f"{slug.replace('-agent', '')}.md"


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def run_stack_json(query: str, failures: list[str]) -> dict[str, object]:
    result = subprocess.run(
        [sys.executable, str(RECOMMEND_STACK), query, "--json"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        failures.append(f"recommend_stack.py failed for {query!r}: {result.stderr.strip()}")
        return {}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        failures.append(f"recommend_stack.py did not return valid JSON for {query!r}: {exc}")
        return {}


def check_contract(failures: list[str]) -> None:
    text = read_text(CONTRACT)
    codex = read_text(CODEX)
    require(CONTRACT.exists(), "missing agent arsenal routing contract", failures)
    for snippet in [
        "Seed lists are not constraints",
        "Stack only when it compounds",
        "Visible Routing Trace",
        "Real Codex subagents require explicit user authorization",
    ]:
        require(snippet in text, f"contract missing: {snippet}", failures)
    require("agent-arsenal-routing-contract.md" in codex, "CODEX.md does not reference agent arsenal routing contract", failures)


def check_registry(failures: list[str]) -> None:
    require(REGISTRY.exists(), "missing generated stacking registry json", failures)
    require(REGISTRY_MD.exists(), "missing generated stacking registry markdown", failures)
    if not REGISTRY.exists():
        return
    try:
        data = json.loads(read_text(REGISTRY))
    except json.JSONDecodeError as exc:
        failures.append(f"stacking registry is not valid JSON: {exc}")
        return
    counts = data.get("counts", {})
    require(counts.get("expert_router_compounds", 0) >= 20, "stacking registry has too few expert-router compounds", failures)
    require(counts.get("skill_stacking_guides", 0) >= 10, "stacking registry has too few skill stacking guides", failures)
    require("selection_policy" in data, "stacking registry missing selection policy", failures)


def check_operator_agents(failures: list[str]) -> None:
    for slug in OPERATOR_SLUGS:
        agent_path = AGENTS_DIR / slug / "AGENT.md"
        text = read_text(agent_path)
        require(agent_path.exists(), f"{slug}: missing AGENT.md", failures)
        require("## Dynamic Routing Protocol" in text, f"{slug}: missing Dynamic Routing Protocol", failures)
        require("## Seed Workflows" in text, f"{slug}: missing Seed Workflows", failures)
        require("## Routing Interop" in text, f"{slug}: missing Routing Interop", failures)
        require("## Routing Trace Fields" in text, f"{slug}: missing Routing Trace Fields", failures)
        require("Core workflow for" not in text, f"{slug}: still says Core workflow for", failures)
        require("## Available Workflows" not in text, f"{slug}: still has Available Workflows heading", failures)
        require("Real Codex subagents require explicit user authorization" in text, f"{slug}: missing subagent approval boundary", failures)

        workflow = workflow_path(slug)
        wtext = read_text(workflow)
        require(workflow.exists(), f"{slug}: missing operator workflow", failures)
        require("## Arsenal Routing Contract" in wtext, f"{slug}: workflow missing contract reference", failures)
        require("## Seed Workflows to Consider" in wtext, f"{slug}: workflow missing Seed Workflows to Consider", failures)
        require("python3 execution/tool_router.py route" in wtext, f"{slug}: workflow missing tool_router route", failures)
        require("## Routing Trace" in wtext, f"{slug}: workflow missing Routing Trace output", failures)
        for field in TRACE_FIELDS:
            require(f"**{field}**" in wtext, f"{slug}: workflow missing trace field {field}", failures)


def check_all_agents(failures: list[str]) -> None:
    paths = sorted(AGENTS_DIR.glob("*/AGENT.md"))
    require(len(paths) >= 160, f"expected broad agent library, found {len(paths)}", failures)
    missing = [str(path.relative_to(ROOT)) for path in paths if "## Routing Interop" not in read_text(path)]
    if missing:
        failures.append("agents missing Routing Interop: " + ", ".join(missing[:20]))


def check_copywriting_exemplar(failures: list[str]) -> None:
    text = read_text(AGENTS_DIR / "copywriting-agent" / "AGENT.md")
    workflow = read_text(WORKFLOWS_DIR / "copywriting-agent.md")
    combined = f"{text}\n{workflow}".lower()
    for term in ["offer", "buyer-belief", "proof", "story", "vsl", "linkedin", "research", "design", "publishable-copy"]:
        require(term in combined, f"copywriting exemplar missing route coverage term: {term}", failures)
    require("mandatory only" in combined, "copywriting gate boundary should say mandatory only", failures)


def check_router_samples(failures: list[str]) -> None:
    sys.path.insert(0, str(ROOT / "execution"))
    import command_menu  # type: ignore
    import workflow_router  # type: ignore

    menu_index = command_menu.build_index()

    unresolved = "unclear service offer needs positioning before copy"
    menu_unresolved = [wf.name for _, wf in command_menu.search(menu_index, unresolved, 10)]
    router_unresolved = [wf["name"] for _, wf in workflow_router.search_workflows(unresolved, 10)]
    require(menu_unresolved and menu_unresolved[0] == "offer-positioning-north-star", "command_menu should route unclear offer before copy to /offer-positioning-north-star", failures)
    require(router_unresolved and router_unresolved[0] == "offer-positioning-north-star", "workflow_router should route unclear offer before copy to /offer-positioning-north-star", failures)

    publishable = "public LinkedIn revenue copy needs punch voice and tension"
    menu_publishable = [wf.name for _, wf in command_menu.search(menu_index, publishable, 10)]
    router_publishable = [wf["name"] for _, wf in workflow_router.search_workflows(publishable, 10)]
    require(menu_publishable and menu_publishable[0] == "publishable-copy-gate", "command_menu should route public revenue copy to /publishable-copy-gate", failures)
    require(router_publishable and router_publishable[0] == "publishable-copy-gate", "workflow_router should route public revenue copy to /publishable-copy-gate", failures)


def check_recommended_stack_surface(failures: list[str]) -> None:
    require(RECOMMEND_STACK.exists(), "missing recommended stack presenter script", failures)

    autopilot = read_text(WORKFLOWS_DIR / "autopilot.md")
    require('python3 execution/recommend_stack.py "[raw context]" --json' in autopilot, "autopilot workflow does not run recommend_stack.py", failures)
    require("**Recommended Stack**" in autopilot, "autopilot trace missing Recommended Stack field", failures)
    require("**Recommended stack**" in autopilot, "autopilot Chosen Path missing Recommended stack field", failures)

    orchestrate = read_text(WORKFLOWS_DIR / "orchestrate.md")
    require('python3 execution/recommend_stack.py "[goal/context]" --json' in orchestrate, "orchestrate workflow does not run recommend_stack.py", failures)
    require("**Recommended stack**" in orchestrate, "orchestrate menu schema missing Recommended stack field", failures)
    require("strongest compound/council stack" in orchestrate, "orchestrate Path 3 does not require strongest supported compound/council stack", failures)

    autopilot_agent = read_text(AGENTS_DIR / "operator-autopilot" / "AGENT.md")
    orchestrator_agent = read_text(AGENTS_DIR / "antigravity-orchestrator" / "AGENT.md")
    require("Recommended Stack Surfacing" in autopilot_agent, "operator-autopilot agent missing recommended stack behavior", failures)
    require("Recommended Stack Surfacing" in orchestrator_agent, "antigravity-orchestrator agent missing recommended stack behavior", failures)

    linkedin = run_stack_json("LinkedIn revenue copy needs reach conversion and proof", failures)
    require(linkedin.get("recommended_stack") == "lara-acosta + cardinal-mason", "LinkedIn revenue query should recommend lara-acosta + cardinal-mason", failures)
    require("LinkedIn revenue engine" in str(linkedin.get("compound_effect", "")), "LinkedIn revenue query has wrong compound effect", failures)
    require("expert_router.py" in str(linkedin.get("evidence_source", "")), "LinkedIn revenue stack missing expert_router evidence source", failures)
    require(linkedin.get("trigger_match") == "linkedin revenue", "LinkedIn revenue stack missing trigger match", failures)

    weak = run_stack_json("weak generic file cleanup no specialist stack", failures)
    require(weak.get("recommended_stack") == "No recommended stack", "weak/no-match query should return No recommended stack", failures)
    require(bool(weak.get("skip_reason")), "weak/no-match query should include skip reason", failures)


def main() -> int:
    failures: list[str] = []
    check_contract(failures)
    check_registry(failures)
    check_operator_agents(failures)
    check_all_agents(failures)
    check_copywriting_exemplar(failures)
    check_router_samples(failures)
    check_recommended_stack_surface(failures)

    if failures:
        print("AGENT ARSENAL ROUTING VERIFICATION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("AGENT ARSENAL ROUTING VERIFICATION PASS")
    print(f"- contract: {CONTRACT.relative_to(ROOT)}")
    print(f"- registry: {REGISTRY.relative_to(ROOT)}")
    print(f"- operator agents checked: {len(OPERATOR_SLUGS)}")
    print(f"- agent profiles checked: {len(list(AGENTS_DIR.glob('*/AGENT.md')))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
