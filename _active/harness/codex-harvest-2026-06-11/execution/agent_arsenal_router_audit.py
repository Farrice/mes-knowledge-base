#!/usr/bin/env python3
"""Audit and migrate Antigravity agents to the arsenal routing contract."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = ROOT / "agents"
WORKFLOWS_DIR = ROOT / ".agent" / "workflows"

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


def write_text(path: Path, text: str, apply: bool) -> bool:
    old = read_text(path)
    if old == text:
        return False
    if apply:
        path.write_text(text, encoding="utf-8")
    return True


def normalize_blank_lines(text: str) -> str:
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.rstrip() + "\n"


def all_agent_paths() -> list[Path]:
    return sorted(AGENTS_DIR.glob("*/AGENT.md"))


def operator_agent_path(slug: str) -> Path:
    return AGENTS_DIR / slug / "AGENT.md"


def operator_workflow_path(slug: str) -> Path:
    direct = WORKFLOWS_DIR / f"{slug}.md"
    if direct.exists():
        return direct
    return WORKFLOWS_DIR / f"{slug.replace('-agent', '')}.md"


def insert_before_section(text: str, section: str, fallback_append: bool = True) -> str:
    preferred = [
        "## Handoff Protocol",
        "## Memory Reference",
        "## Knowledge Sources",
        "## Calibration",
        "## Activation Triggers",
    ]
    for heading in preferred:
        idx = text.find(f"\n{heading}")
        if idx != -1:
            return text[:idx] + "\n\n" + section.rstrip() + "\n" + text[idx:]
    if fallback_append:
        return text.rstrip() + "\n\n" + section.rstrip() + "\n"
    return text


def dynamic_routing_section(slug: str) -> str:
    copywriting_extra = ""
    if slug == "copywriting-agent":
        copywriting_extra = (
            "\nCopywriting route coverage must include offer, buyer-belief, proof, story, VSL, "
            "LinkedIn, research, design, and publishable-copy paths when the objective calls for them. "
            "`/publishable-copy-gate` is mandatory only for public, revenue-critical, publishable, "
            "outreach, checkout, marketplace, or client-facing copy.\n"
        )
    return f"""## Dynamic Routing Protocol

Run the local routers before choosing a workflow, expert, skill, gate, or handoff. Treat the seed list below as a starting map, not a boundary. Choose the route that best fits the objective, retrieved context, stacking evidence, and risk level.

Required lookup surfaces: `execution/command_menu.py`, `execution/workflow_router.py`, `execution/expert_router.py route`, `execution/expert_router.py compounds`, `execution/context_retriever.py`, `execution/tool_router.py`, and `semantic_libraries/antigravity/stacking/agent-stacking-registry.json`.

Prefer one strong route or stack over broad expert soup. Use real Codex subagents only when the user explicitly authorizes delegation, parallel agents, or subagents.
{copywriting_extra}"""


def routing_trace_section() -> str:
    fields = "\n".join(f"- **{field}**:" for field in TRACE_FIELDS)
    return f"""## Routing Trace Fields

When this agent recommends or executes a path, expose the compact trace below unless the answer is tiny or the user requested only the direct answer:

```markdown
## Routing Trace
{fields}
```"""


def operator_interop_section() -> str:
    return """## Routing Interop

This is a function-owner operator, not a closed execution silo. It should route into adjacent operators, expert personas, skill workflows, context retrieval, tools, and gates when those assets better serve the objective.

- Activate this operator when the objective belongs primarily to its function.
- Pair with stacking candidates only when the combination changes the output or covers a named blind spot.
- Hand off when offer, research, design, proof, delivery, quality, red-team, mission, or evolution ownership is stronger elsewhere.
- Real Codex subagents require explicit user authorization for delegation, parallel agents, or subagents."""


def persona_interop_section() -> str:
    return """## Routing Interop

Use this agent as expertise context inside the larger Antigravity arsenal, not as a standalone control plane.

- Activate this expert when the task matches its domain, patterns, or source evidence.
- Before relying on this expert alone, check router results and the stacking registry for stronger workflows, pairings, or handoffs.
- Pair with adjacent experts only when the combination creates a specific compound effect.
- Hand off to an operator agent when the next step is delivery, research, copy, design, offers, client work, proof, quality, red team, mission, or system evolution.
- Real Codex subagents require explicit user authorization for delegation, parallel agents, or subagents."""


def migrate_operator_agent(path: Path, apply: bool) -> tuple[bool, list[str]]:
    text = read_text(path)
    changes = []
    if not text:
        return False, ["missing or unreadable"]

    slug = path.parent.name
    new = text

    if "## Dynamic Routing Protocol" not in new:
        marker = "\n## Available Workflows"
        idx = new.find(marker)
        if idx != -1:
            new = new[:idx] + "\n\n" + dynamic_routing_section(slug).rstrip() + "\n" + new[idx:]
        else:
            new = insert_before_section(new, dynamic_routing_section(slug))
        changes.append("dynamic routing")

    if "## Routing Trace Fields" not in new:
        marker = "\n## Tool Permissions"
        idx = new.find(marker)
        if idx != -1:
            new = new[:idx] + "\n\n" + routing_trace_section().rstrip() + "\n" + new[idx:]
        else:
            new = insert_before_section(new, routing_trace_section())
        changes.append("trace fields")

    if "## Routing Interop" not in new:
        new = insert_before_section(new, operator_interop_section())
        changes.append("routing interop")

    if "## Available Workflows" in new:
        new = new.replace("## Available Workflows", "## Seed Workflows")
        changes.append("seed workflows heading")

    if "## Seed Workflows\n\nThese are seed candidates" not in new:
        new = new.replace(
            "## Seed Workflows\n\n",
            "## Seed Workflows\n\nThese are seed candidates, not a closed menu. Confirm the final path through router lookup, stacking evidence, and objective fit.\n\n",
            1,
        )
        changes.append("seed workflow note")

    if "## Expert Stack" in new:
        new = new.replace("## Expert Stack", "## Stacking Candidates")
        changes.append("stacking heading")

    if "## Stacking Candidates\n\nUse these as declared" not in new:
        new = new.replace(
            "## Stacking Candidates\n\n",
            "## Stacking Candidates\n\nUse these as declared starting candidates. Confirm pairings through `execution/expert_router.py compounds`, the stacking registry, and task-specific fit.\n\n",
            1,
        )
        changes.append("stacking note")

    new = re.sub(
        r"Core workflow for ([^|\n]+?)\s*(?=\|)",
        r"Seed candidate for \1; confirm by router lookup ",
        new,
    )

    new = normalize_blank_lines(new)
    return write_text(path, new, apply), changes


def migrate_persona_agent(path: Path, apply: bool) -> tuple[bool, list[str]]:
    text = read_text(path)
    if not text:
        return False, ["missing or unreadable"]
    if "## Routing Interop" in text:
        return False, []
    section = operator_interop_section() if path.parent.name in OPERATOR_SLUGS else persona_interop_section()
    new = normalize_blank_lines(insert_before_section(text, section))
    return write_text(path, new, apply), ["routing interop"]


def migrate_operator_workflow(path: Path, apply: bool) -> tuple[bool, list[str]]:
    text = read_text(path)
    changes = []
    if not text:
        return False, ["missing or unreadable"]

    new = text
    if "## Core Workflows to Consider" in new:
        new = new.replace("## Core Workflows to Consider", "## Seed Workflows to Consider")
        changes.append("seed workflow heading")

    if "## Seed Workflows to Consider\n\nThese are seed candidates" not in new:
        new = new.replace(
            "## Seed Workflows to Consider\n\n",
            "## Seed Workflows to Consider\n\nThese are seed candidates, not a closed menu. Confirm the final path through router lookup, stacking evidence, and objective fit.\n\n",
            1,
        )
        changes.append("seed workflow note")

    if "python3 execution/tool_router.py route" not in new and "python3 execution/context_retriever.py search" in new:
        new = new.replace(
            'python3 execution/context_retriever.py search "[goal/context]" --top 8',
            'python3 execution/context_retriever.py search "[goal/context]" --top 8\npython3 execution/tool_router.py route "[goal/context]"',
            1,
        )
        changes.append("tool router")

    if "## Arsenal Routing Contract" not in new:
        contract = """## Arsenal Routing Contract

Follow `semantic_libraries/antigravity/primitives/agent-arsenal-routing-contract.md`. Route before committing, treat fixed lists as seed candidates, use evidence-weighted stacking, preserve hot/cold context, and expose the chosen route.

"""
        marker = "\n## Seed Workflows to Consider"
        idx = new.find(marker)
        if idx != -1:
            new = new[:idx] + "\n" + contract.rstrip() + "\n" + new[idx:]
        else:
            new = insert_before_section(new, contract, fallback_append=False)
        changes.append("contract reference")

    new = new.replace(
        "**Route the arsenal**: use local routers and the workflow list below before loading full files.",
        "**Route the arsenal**: use local routers, stacking evidence, and the seed workflow list before loading full files.",
    )

    if "## Routing Trace" not in new:
        trace = "\n".join(f"- **{field}**:" for field in TRACE_FIELDS)
        new = new.replace(
            "## Recommended Path\n",
            f"## Routing Trace\n{trace}\n\n## Recommended Path\n",
            1,
        )
        changes.append("output trace")

    new = new.replace("- Expert stack:", "- Stacking candidates:")

    new = normalize_blank_lines(new)
    return write_text(path, new, apply), changes


def audit(apply: bool, operators: bool, all_agents: bool) -> int:
    changed = 0
    reports = []

    if operators:
        for slug in OPERATOR_SLUGS:
            agent_path = operator_agent_path(slug)
            workflow_path = operator_workflow_path(slug)
            did_agent, agent_changes = migrate_operator_agent(agent_path, apply)
            did_workflow, workflow_changes = migrate_operator_workflow(workflow_path, apply)
            if did_agent or did_workflow:
                changed += int(did_agent) + int(did_workflow)
            reports.append((slug, agent_changes, workflow_changes, did_agent, did_workflow))

    if all_agents:
        for path in all_agent_paths():
            did, changes = migrate_persona_agent(path, apply)
            if did:
                changed += 1
                reports.append((path.parent.name, changes, [], True, False))

    mode = "APPLY" if apply else "PLAN-ONLY"
    print(f"Agent arsenal routing audit: {mode}")
    print(f"Operator slugs: {len(OPERATOR_SLUGS)}")
    print(f"Agent profiles: {len(all_agent_paths())}")
    print(f"Files that would change" if not apply else "Files changed", f": {changed}", sep="")

    for slug, agent_changes, workflow_changes, did_agent, did_workflow in reports:
        if not agent_changes and not workflow_changes:
            continue
        status = []
        if agent_changes:
            status.append("agent=" + ", ".join(agent_changes))
        if workflow_changes:
            status.append("workflow=" + ", ".join(workflow_changes))
        changed_flag = "changed" if did_agent or did_workflow else "already covered"
        print(f"- {slug}: {changed_flag}; {'; '.join(status)}")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit or migrate agent arsenal routing contract coverage")
    parser.add_argument("--plan-only", action="store_true", help="Show planned changes without writing")
    parser.add_argument("--apply", action="store_true", help="Apply the migration")
    parser.add_argument("--operators", action="store_true", help="Include the operator suite")
    parser.add_argument("--all-agents", action="store_true", help="Include all agent profiles")
    args = parser.parse_args()

    if args.plan_only == args.apply:
        parser.error("Choose exactly one of --plan-only or --apply")
    if not args.operators and not args.all_agents:
        parser.error("Choose --operators, --all-agents, or both")

    return audit(apply=args.apply, operators=args.operators, all_agents=args.all_agents)


if __name__ == "__main__":
    raise SystemExit(main())
