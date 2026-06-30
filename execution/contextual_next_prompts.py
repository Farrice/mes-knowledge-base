#!/usr/bin/env python3
"""Render contextual next prompts for Antigravity closeouts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def existing(paths: list[str]) -> list[str]:
    return [path for path in paths if (ROOT / path).exists()]


def compact(value: Any, fallback: str = "") -> str:
    if value is None:
        return fallback
    if isinstance(value, str):
        return value.strip() or fallback
    if isinstance(value, dict):
        for key in ("route", "chosen_route", "action", "goal", "query"):
            if key in value:
                nested = compact(value.get(key), "")
                if nested:
                    return nested
        return fallback
    return str(value).strip() or fallback


def state_context(objective: str) -> dict[str, Any]:
    intent = read_json(ROOT / ".agent" / "intent-memory" / "current.json")
    cohesion = read_json(ROOT / ".agent" / "system-cohesion-state.json")
    receipt = read_json(ROOT / ".agent" / "run-receipts" / "latest.json")

    inferred_objective = (
        objective
        or compact(intent.get("goal"))
        or compact(intent.get("active_intent", {}).get("goal"))
        or compact(receipt.get("query"))
        or "continue the current Google Antigravity work"
    )
    route = compact(
        intent.get("chosen_route")
        or intent.get("route", {}).get("chosen_route")
        or cohesion.get("chosen_route")
        or cohesion.get("route")
        or receipt.get("route"),
        "autopilot",
    )
    lowered_objective = inferred_objective.lower()
    if any(term in lowered_objective for term in ("steering", "next prompt", "next prompts", "operator lesson")):
        route = "steering-compass"
    elif any(term in lowered_objective for term in ("operator core", "not firing", "hooks", "harness", "operating alignment")):
        route = "system-audit"
    elif any(term in lowered_objective for term in ("source to skill", "source-to-skill", "skill system")):
        route = "source-to-skill-system"
    elif "handoff" in lowered_objective and any(
        term in lowered_objective for term in ("agent", "session", "conversation", "branch", "transfer")
    ):
        route = "handoff"
    next_action = compact(
        intent.get("next_move")
        or intent.get("next_move", {}).get("action")
        or cohesion.get("next_move")
        or receipt.get("next_action")
    )
    context_paths = existing(
        [
            ".agent/intent-memory/current.json",
            ".agent/system-cohesion-state.json",
            ".agent/run-receipts/latest.md",
            ".agent/session-state.md",
            "AGENTS.md",
            "GEMINI.md",
            "CLAUDE.md",
        ]
    )
    return {
        "objective": inferred_objective,
        "objective_provided": bool(objective.strip()),
        "route": route.lstrip("/"),
        "next_action": next_action,
        "context_paths": context_paths,
    }


def prompt_text(route: str, objective: str, instruction: str, context_paths: list[str]) -> str:
    context_clause = ""
    if context_paths:
        context_clause = " Load these context anchors first: " + ", ".join(context_paths[:4]) + "."
    clean_instruction = instruction.strip()
    if clean_instruction and clean_instruction[-1] not in ".!?":
        clean_instruction += "."
    return f"/{route} {clean_instruction} Objective: {objective}.{context_clause}"


def unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        clean = value.strip().lstrip("/")
        if not clean or clean in seen:
            continue
        seen.add(clean)
        result.append(clean)
    return result


WORK_PROFILES: dict[str, dict[str, Any]] = {
    "steering_persistence": {
        "use_route": "steering-compass",
        "harden_route": "system-audit",
        "expand_route": "source-to-skill-system",
        "skills": ["steering-compass", "system-audit", "source-to-skill-system"],
        "operator_insight": "A behavior repair becomes real only when it changes ordinary final answers, not just command outputs.",
        "hidden_gap": "The usual failure is that the contract exists in a file, but the visible answer surface still follows the old habit.",
        "capability": "Codex can verify behavior across global instructions, workspace instructions, renderer output, and final-answer shape.",
        "use_instruction": (
            "run a normal-answer smoke test for persistent per-exchange steering; show the visible answer surface with enriched fields"
        ),
        "harden_instruction": (
            "verify global and workspace instruction surfaces for always-on steering, then compare the rendered output against the visible-answer contract"
        ),
        "expand_instruction": (
            "turn the visible-answer proof into a reusable steering benchmark with good examples, failure cases, and verifier expectations"
        ),
    },
    "session_closeout": {
        "use_route": "end-session",
        "harden_route": "system-audit",
        "expand_route": "source-to-skill-system",
        "skills": ["end-session", "steering-compass", "system-audit"],
        "operator_insight": "A closeout is a launch surface for the next session, not a ceremonial ending.",
        "hidden_gap": "The visible final answer is where old behavior can leak back in even after the helper/runtime was repaired.",
        "capability": "Codex can turn a completed session into a retrieval handoff, smoke test, regression check, and reusable operating asset.",
        "use_instruction": (
            "produce the fresh-session smoke test and retrieval handoff for this session, preserving the Insightful Momentum fields"
        ),
        "harden_instruction": (
            "compare the visible closeout against the Insightful Momentum contract; identify any old-format leakage and patch the local source if safe"
        ),
        "expand_instruction": (
            "package the winning closeout behavior into a reusable operator benchmark with examples, failure cases, and verifier expectations"
        ),
    },
    "artifact_followup": {
        "use_route": "creative-assembly",
        "harden_route": "source-to-skill-system",
        "expand_route": "campaign-architect",
        "skills": ["creative-assembly", "source-to-skill-system", "campaign-architect"],
        "operator_insight": "A finished artifact can become multiple next surfaces: script, slides, webpage, sprint, skill, or offer asset.",
        "hidden_gap": "The missed value is often the transformation path: turning one completed piece into the next format or reusable process.",
        "capability": "Codex can convert one artifact into presentations, content packs, launch sprints, web pages, or reusable skill systems.",
        "use_instruction": "create the most useful presentation, briefing, or content asset from this artifact",
        "harden_instruction": "make the process behind this artifact reusable with a workflow, skill, or validation checklist",
        "expand_instruction": "develop a launch, campaign, or asset sprint that turns this artifact into a larger outcome",
    },
    "system_operator": {
        "use_route": "system-audit",
        "harden_route": "system-audit",
        "expand_route": "source-to-skill-system",
        "skills": ["system-audit", "steering-compass", "routing-intelligence"],
        "operator_insight": "System friction is usually an ownership and proof problem before it is a prompt problem.",
        "hidden_gap": "If the repair only changes the answer style, the old behavior can return in the next fresh session.",
        "capability": "Codex can turn a complaint into a routed repair loop: preflight, owner, verifier, and receipt.",
        "use_instruction": (
            "convert this operator problem into the next local proof-backed repair; name the owner, patch only the "
            "active surface, verify it, and write the receipt"
        ),
        "harden_instruction": (
            "run a steering-quality and routing-drift audit for this operator behavior; identify the one regression "
            "that would make the next session feel worse, patch it if local and safe, then verify"
        ),
        "expand_instruction": (
            "extract the durable operating primitive from this repair and decide whether it belongs as a workflow, "
            "semantic primitive, verifier, or global thin bridge"
        ),
    },
    "source_capability": {
        "use_route": "source-to-skill-system",
        "harden_route": "extraction-governor-agent",
        "expand_route": "knowledge-librarian",
        "skills": ["source-to-skill-system", "extraction-governor-agent", "knowledge-librarian"],
        "operator_insight": "A good source-to-system move preserves the hidden mechanic, not just the visible content.",
        "hidden_gap": "The missing decision is often build shape: reference, primitive, workflow, skill, command, or offer asset.",
        "capability": "Codex can route source into a reusable capability surface with validation instead of another summary.",
        "use_instruction": (
            "turn the source or session mechanic into the smallest reusable capability contract with one validation example"
        ),
        "harden_instruction": (
            "triage duplicate-system risk, source grounding, and build shape before adding any new skill or workflow"
        ),
        "expand_instruction": (
            "map the capability into the library: related routes, cold-start prompt, reuse hook, and future verifier"
        ),
    },
    "content_creative": {
        "use_route": "creative-assembly",
        "harden_route": "adversarial-review",
        "expand_route": "content-series",
        "skills": ["creative-assembly", "content-review-cycle", "steering-compass"],
        "operator_insight": "Creative work gets better when the next prompt names the taste move, not just the asset to make.",
        "hidden_gap": "The untapped move is usually a format, audience, or emotional-angle expansion beyond the first draft.",
        "capability": "Codex can run angle generation, critique, format adaptation, and quality gates as one production loop.",
        "use_instruction": (
            "produce the next publishable creative artifact, then explain the taste decision that made it stronger"
        ),
        "harden_instruction": (
            "run a quality and originality pass: identify the weakest hook, sameness risk, proof gap, and one rewrite path"
        ),
        "expand_instruction": (
            "expand the core idea into a higher-ceiling creative system: formats, angles, sequence, and reusable taste rules"
        ),
    },
    "revenue_client": {
        "use_route": "offer-stack",
        "harden_route": "adversarial-review",
        "expand_route": "client-acquire",
        "skills": ["offer-stack", "client-acquire", "business-intelligence"],
        "operator_insight": "Client and revenue work should move toward a sellable asset, not only a cleaner explanation.",
        "hidden_gap": "The gap is often proof, buyer trigger, packaging, or the next conversion surface.",
        "capability": "Codex can connect strategy, offer architecture, copy, proof, and delivery assets into one go-to-market packet.",
        "use_instruction": (
            "turn the current direction into the next client-facing asset with the buyer trigger, promise, and proof path visible"
        ),
        "harden_instruction": (
            "stress-test the offer or client artifact for belief gaps, proof gaps, objections, and unclear next action"
        ),
        "expand_instruction": (
            "expand this into a bigger commercial system: service ladder, acquisition asset, delivery workflow, and reuse hook"
        ),
    },
    "generic": {
        "use_route": "autopilot",
        "harden_route": "system-audit",
        "expand_route": "source-to-skill-system",
        "skills": ["autopilot", "steering-compass", "system-audit"],
        "operator_insight": "The best next prompt should change the work state and teach the operating move at the same time.",
        "hidden_gap": "The likely missing piece is choosing whether this is execution, hardening, or capability capture.",
        "capability": "Codex can route, execute, verify, and preserve the method when the next move is named clearly.",
        "use_instruction": (
            "choose the next concrete artifact for this objective, produce it, and state the operating move it teaches"
        ),
        "harden_instruction": (
            "audit the current result for missing proof, unclear owner, stale context, and one highest-value improvement"
        ),
        "expand_instruction": (
            "identify the reusable pattern inside this work and turn it into a small durable route, prompt, or verifier"
        ),
    },
}


def infer_work_type(objective: str, route: str, objective_provided: bool = False) -> str:
    objective_text = objective.lower()
    route_text = route.lower()
    if any(
        term in objective_text
        for term in (
            "per-exchange",
            "per exchange",
            "command-only",
            "command only",
            "visible answer surface",
            "persistent global",
            "always-on steering",
            "normal answer",
            "every meaningful final answer",
        )
    ):
        return "steering_persistence"
    if any(
        term in objective_text
        for term in (
            "end-session",
            "end session",
            "session closeout",
            "close out",
            "closeout",
            "session handoff",
            "wrap session",
        )
    ):
        return "session_closeout"
    if any(
        term in objective_text
        for term in (
            "operator",
            "codex",
            "harness",
            "hook",
            "routing",
            "workspace",
            "global",
            "system-audit",
            "operator core",
            "control plane",
            "operating alignment",
            "system repair",
            "system friction",
            "steering",
            "next prompt",
            "operator lesson",
            "execution bias",
            "preflight",
        )
    ):
        return "system_operator"
    if any(
        term in objective_text
        for term in (
            "portfolio",
            "playbook",
            "deck",
            "brief",
            "report",
            "prompt",
            "presentation",
            "dashboard",
            "spreadsheet",
            "data table",
            "analytics",
            "metrics",
            "website",
            "webpage",
            "web app",
            "prototype",
        )
    ):
        return "artifact_followup"
    if any(term in objective_text for term in ("client", "revenue", "offer", "sales", "funnel", "service", "buyer")):
        return "revenue_client"
    if any(term in objective_text for term in ("source", "skill", "capability", "workflow", "primitive", "extraction")):
        return "source_capability"
    if any(term in objective_text for term in ("content", "creative", "copy", "post", "article", "brand", "hook", "story")):
        return "content_creative"
    if objective_provided:
        return "artifact_followup"
    text = route_text
    if any(term in text for term in ("client", "revenue", "offer", "sales", "funnel", "service", "buyer")):
        return "revenue_client"
    if any(term in text for term in ("source", "skill", "capability", "workflow", "primitive", "extraction")):
        return "source_capability"
    if any(term in text for term in ("content", "creative", "copy", "post", "article", "brand", "hook", "story")):
        return "content_creative"
    if any(
        term in text
        for term in (
            "operator",
            "codex",
            "harness",
            "hook",
            "routing",
            "workspace",
            "global",
            "system",
            "steering",
            "next prompt",
            "operator lesson",
            "execution bias",
            "preflight",
        )
    ):
        return "system_operator"
    return "generic"


def route_for(profile: dict[str, Any], key: str, fallback: str) -> str:
    route = str(profile.get(key) or fallback).strip().lstrip("/")
    return route or fallback


def suggestion_family(name: str, route: str, title: str, work_type: str) -> str:
    lowered = f"{route} {title} {work_type}".lower()
    if route in {"deep-research", "business-intelligence"} or any(
        term in lowered for term in ("opportunit", "research", "evidence", "mechanism", "compare")
    ):
        return "Deepen"
    if route in {"source-to-skill-system", "repeatability-spine", "knowledge-librarian"} or any(
        term in lowered for term in ("reusable", "workflow", "skill", "primitive", "template")
    ):
        return "Compound"
    if name == "Harden" or any(term in lowered for term in ("audit", "stress-test", "fact check", "proof", "regression")):
        return "Harden"
    if any(term in lowered for term in ("launch", "ship", "website", "webpage", "app", "prototype", "live")):
        return "Ship"
    return "Transform"


def frontier_pattern(name: str, route: str, family: str) -> str:
    if route in {"deep-research", "business-intelligence"}:
        return "Perplexity-style contextual deepening: preserve the thread object, expose sources or evidence gaps, and go deeper without restating context."
    if family == "Harden":
        return "Information-gap hardening: compare the current answer with the fuller answer it could become, then close the gap that matters."
    if route in {"source-to-skill-system", "repeatability-spine", "knowledge-librarian"} or family == "Compound":
        return "Capability compounding: turn the winning process into a reusable workflow, skill, primitive, or library asset."
    if family == "Ship":
        return "Manus/Genspark-style shipping: transform the session object into an editable asset, build surface, launch path, or handoff."
    if name == "Use Now":
        return "Output-first transformation: convert context into a concrete artifact instead of asking for more chat."
    return "Frontier follow-up pattern: reveal the capability, bridge the gap, and make the next move concrete."


def enrich_item(
    *,
    name: str,
    route: str,
    objective: str,
    instruction: str,
    context_paths: list[str],
    suggested_skills: list[str],
    when_to_use: str,
    why: str,
    operator_insight: str,
    hidden_gap: str,
    capability: str,
    expected_output: str,
    quality_bar: str,
    skip_if: str,
    work_type: str,
    title_override: str = "",
) -> dict[str, Any]:
    title = title_override or followup_title(name, objective, work_type)
    family = suggestion_family(name, route, title, work_type)
    pattern = frontier_pattern(name, route, family)
    return {
        "name": name,
        "followup_title": title,
        "route": route,
        "suggestion_family": family,
        "frontier_pattern": pattern,
        "suggested_skills": unique(suggested_skills),
        "when_to_use": when_to_use,
        "why": why,
        "operator_insight": operator_insight,
        "hidden_gap_opportunity": hidden_gap,
        "capability_revealed": capability,
        "prompt": prompt_text(route, objective, instruction, context_paths),
        "entails": entailment(name, expected_output, capability),
        "expected_output": expected_output,
        "quality_bar": quality_bar,
        "skip_if": skip_if,
    }


def clean_objective_label(objective: str) -> str:
    cleaned = " ".join(objective.strip().strip(".").split())
    if len(cleaned) > 90:
        cleaned = cleaned[:87].rstrip() + "..."
    return cleaned or "this work"


def followup_title(name: str, objective: str, work_type: str) -> str:
    obj = clean_objective_label(objective)
    if work_type == "artifact_followup":
        return artifact_followup_title(name, obj)
    titles = {
        "system_operator": {
            "Use Now": f"Run a proof-backed steering repair for {obj}.",
            "Harden": f"Audit {obj} for drift, bypasses, and regression risk.",
            "Expand": f"Turn the winning move from {obj} into a reusable operating primitive.",
        },
        "session_closeout": {
            "Use Now": f"Run a fresh-session smoke test for {obj}.",
            "Harden": f"Compare {obj} against the Insightful Momentum closeout contract.",
            "Expand": f"Turn {obj} into a reusable operator benchmark and primitive.",
        },
        "steering_persistence": {
            "Use Now": f"Run a normal-answer smoke test for {obj}.",
            "Harden": f"Verify the global and workspace instruction surfaces for {obj}.",
            "Expand": f"Turn the visible-answer proof for {obj} into a reusable steering benchmark.",
        },
        "source_capability": {
            "Use Now": f"Turn {obj} into a reusable capability contract.",
            "Harden": f"Check {obj} for duplicate-system and grounding risk.",
            "Expand": f"Map {obj} into the library with a cold-start route.",
        },
        "content_creative": {
            "Use Now": f"Generate content assets from {obj}.",
            "Harden": f"Run an originality and quality pass on {obj}.",
            "Expand": f"Develop a campaign or series from {obj}.",
        },
        "revenue_client": {
            "Use Now": f"Create the next client-facing asset for {obj}.",
            "Harden": f"Stress-test {obj} for proof, objections, and buyer triggers.",
            "Expand": f"Build a service ladder or acquisition sprint around {obj}.",
        },
        "generic": {
            "Use Now": f"Produce the next concrete artifact for {obj}.",
            "Harden": f"Audit {obj} for the highest-value missing proof.",
            "Expand": f"Turn the useful pattern in {obj} into a reusable route.",
        },
    }
    return titles.get(work_type, titles["generic"]).get(name, f"Continue {obj}.")


def artifact_followup_title(name: str, obj: str) -> str:
    spec = artifact_followup_specs(obj).get(name, {})
    if spec.get("title"):
        return str(spec["title"])
    return f"Create the highest-leverage next asset from {obj}."


def prompt_source_label(obj: str) -> str:
    lowered = obj.lower()
    if "provided meta prompt" in lowered:
        return "the provided Meta Prompt"
    if "meta prompt" in lowered:
        return "the Meta Prompt"
    if "provided prompt" in lowered:
        return "the provided prompt"
    if len(obj.split()) > 8:
        return "the prompt"
    return obj


def prompt_asset_title(obj: str) -> str:
    lowered = obj.lower()
    marker = "using the provided meta prompt"
    if marker in lowered:
        before = obj[: lowered.index(marker)].strip()
        if before:
            if before.lower().startswith("generate "):
                return f"{before[0].upper() + before[1:]} with the provided Meta Prompt."
            return f"Generate {before} with the provided Meta Prompt."
    return f"Generate usable assets with {prompt_source_label(obj)}."


def artifact_followup_specs(obj: str) -> dict[str, dict[str, Any]]:
    lowered = obj.lower()
    if "portfolio" in lowered:
        return {
            "Use Now": {
                "title": f"Create a presentation script based on {obj}.",
                "route": "creative-assembly",
                "instruction": "create a presentation script based on this portfolio, with talk track, section beats, and speaker notes",
                "expected_output": "A presenter-ready script with narrative arc, talking points, and transitions.",
                "skills": ["creative-assembly", "brief", "steering-compass"],
            },
            "Harden": {
                "title": f"Generate slides from {obj}.",
                "route": "design-brief",
                "instruction": "turn this portfolio into a slide-by-slide deck plan with visual hierarchy, section titles, and proof moments",
                "expected_output": "A slide outline or deck brief with structure, visual direction, and proof placement.",
                "skills": ["design-brief", "creative-assembly", "steering-compass"],
            },
            "Expand": {
                "title": f"Create a webpage version of {obj}.",
                "route": "design-first-build",
                "instruction": "turn this portfolio into a webpage plan with sections, copy blocks, visual hierarchy, and conversion path",
                "expected_output": "A webpage blueprint with sections, copy modules, visual direction, and next-build path.",
                "skills": ["design-first-build", "component-build", "brand-guidelines"],
            },
        }
    elif "blue ocean" in lowered or "void" in lowered or "opportunit" in lowered:
        return {
            "Use Now": {
                "title": f"Show the specific opportunities inside {obj}.",
                "route": "business-intelligence",
                "instruction": "extract the specific opportunities, rank them by asymmetry, and name the first validation move",
                "expected_output": "A ranked opportunity map with why-now logic, validation step, and upside/risk notes.",
                "skills": ["business-intelligence", "asymmetric-bet-evaluator", "steering-compass"],
            },
            "Harden": {
                "title": f"Elaborate the highest-leverage methods and arbitrage paths in {obj}.",
                "route": "deep-research",
                "instruction": "elaborate the strongest methods, arbitrage paths, and evidence gaps, separating proven facts from hypotheses",
                "expected_output": "A deeper mechanism brief with evidence status, assumptions, and follow-up research questions.",
                "skills": ["deep-research", "business-intelligence", "adversarial-review"],
            },
            "Expand": {
                "title": f"Create a strategic deck or briefing from {obj}.",
                "route": "campaign-architect",
                "instruction": "turn the opportunity map into a strategic briefing or deck with narrative, recommendations, and decision path",
                "expected_output": "A strategic deck/briefing outline with thesis, opportunity stack, and next-decision path.",
                "skills": ["campaign-architect", "brief", "creative-assembly"],
            },
        }
    elif "playbook" in lowered:
        return {
            "Use Now": {
                "title": f"Generate content assets from {obj}.",
                "route": "creative-assembly",
                "instruction": "generate content assets from this playbook, including angles, hooks, asset formats, and a ship-ready first piece",
                "expected_output": "A content asset pack with angles, hooks, formats, and one publishable draft.",
                "skills": ["creative-assembly", "content-series", "steering-compass"],
            },
            "Harden": {
                "title": f"Make the process behind {obj} reusable with /source-to-skill-system.",
                "route": "source-to-skill-system",
                "instruction": "make the process behind this playbook reusable with a workflow, skill candidate, validation checklist, and cold-start prompt",
                "expected_output": "A reusable process packet with workflow/skill candidate, validation checklist, and cold-start prompt.",
                "skills": ["source-to-skill-system", "extraction-governor-agent", "repeatability-spine"],
            },
            "Expand": {
                "title": f"Develop a launch sprint plan based on {obj}.",
                "route": "campaign-architect",
                "instruction": "develop a launch sprint plan from this playbook with timeline, assets, channels, and quality gates",
                "expected_output": "A launch sprint plan with asset list, timeline, channels, and quality gates.",
                "skills": ["campaign-architect", "content-series-plan", "client-acquire"],
            },
        }
    elif "prompt" in lowered:
        prompt_label = prompt_source_label(obj)
        return {
            "Use Now": {
                "title": prompt_asset_title(obj),
                "route": "creative-assembly",
                "instruction": "use this prompt to generate the first usable asset set, then explain which prompt moves mattered",
                "expected_output": "A first asset set plus the prompt moves that drove the output.",
                "skills": ["creative-assembly", "convert-prompt", "steering-compass"],
            },
            "Harden": {
                "title": f"Turn {prompt_label} into a reusable prompt workflow with validation.",
                "route": "convert-prompt",
                "instruction": "turn this prompt into a reusable workflow with inputs, outputs, quality checks, and failure cases",
                "expected_output": "A reusable prompt workflow with validation criteria and failure modes.",
                "skills": ["convert-prompt", "source-to-skill-system", "adversarial-review"],
            },
            "Expand": {
                "title": f"Build a campaign or test sprint around {prompt_label}.",
                "route": "auto-experiment",
                "instruction": "design a test sprint around this prompt with variants, success criteria, and next asset decisions",
                "expected_output": "A prompt test sprint with variants, measurement plan, and next asset decisions.",
                "skills": ["auto-experiment", "creative-assembly", "content-series"],
            },
        }
    elif any(term in lowered for term in ("dashboard", "spreadsheet", "data table", "analytics", "metrics")):
        return {
            "Use Now": {
                "title": f"Create an insight brief from {obj}.",
                "route": "business-intelligence",
                "instruction": "turn this data or dashboard object into an insight brief with key findings, decision implications, and the next data cut",
                "expected_output": "An insight brief with findings, decision implications, and the next data question.",
                "skills": ["business-intelligence", "data-driven-ops", "steering-compass"],
            },
            "Harden": {
                "title": f"Audit {obj} for metric quality and decision risk.",
                "route": "adversarial-review",
                "instruction": "audit the metrics, assumptions, missing denominators, and decision risks before anyone acts on this dashboard",
                "expected_output": "A metric-quality audit with missing context, risks, and one safer decision path.",
                "skills": ["adversarial-review", "business-intelligence", "repeatability-spine"],
            },
            "Expand": {
                "title": f"Turn {obj} into an executive dashboard or operating review.",
                "route": "component-build",
                "instruction": "map this into an executive dashboard or operating review with views, filters, data sources, and review cadence",
                "expected_output": "A dashboard/review blueprint with views, filters, sources, and operating cadence.",
                "skills": ["component-build", "business-intelligence", "data-driven-ops"],
            },
        }
    elif any(term in lowered for term in ("website", "webpage", "web app", "app", "tool", "prototype")):
        return {
            "Use Now": {
                "title": f"Build the first usable prototype path for {obj}.",
                "route": "design-first-build",
                "instruction": "turn this into the first usable prototype path with screens, sections, interactions, and a local build plan",
                "expected_output": "A prototype path with screens, sections, interactions, and local build steps.",
                "skills": ["design-first-build", "component-build", "design-spec"],
            },
            "Harden": {
                "title": f"Stress-test {obj} for UX, proof, and responsive behavior.",
                "route": "design-taste-gate",
                "instruction": "stress-test this build surface for UX clarity, proof, responsive behavior, and conversion friction",
                "expected_output": "A build-quality review with UX risks, proof gaps, responsive checks, and priority fixes.",
                "skills": ["design-taste-gate", "adversarial-review", "component-build"],
            },
            "Expand": {
                "title": f"Turn {obj} into a launchable product or client handoff packet.",
                "route": "campaign-architect",
                "instruction": "map this build into a launchable product or client handoff packet with scope, assets, QA, and next release path",
                "expected_output": "A launch/handoff packet with scope, assets, QA gates, and next release path.",
                "skills": ["campaign-architect", "component-build", "client-acquire"],
            },
        }
    elif any(term in lowered for term in ("report", "white paper", "case study", "proposal", "briefing")):
        return {
            "Use Now": {
                "title": f"Create an executive summary and decision brief from {obj}.",
                "route": "brief",
                "instruction": "turn this artifact into an executive summary and decision brief with thesis, evidence, and recommended action",
                "expected_output": "An executive-ready brief with thesis, evidence, recommendation, and decision path.",
                "skills": ["brief", "business-intelligence", "creative-assembly"],
            },
            "Harden": {
                "title": f"Fact-check and source-audit {obj}.",
                "route": "adversarial-review",
                "instruction": "fact-check this artifact, separate evidence from inference, and flag claims needing stronger support",
                "expected_output": "A source and claim audit with confidence labels and required fixes.",
                "skills": ["adversarial-review", "deep-research", "accuracy-without-clickbait"],
            },
            "Expand": {
                "title": f"Turn {obj} into a deck, content series, or client asset package.",
                "route": "creative-assembly",
                "instruction": "map this report into the best next distribution surface: deck, content series, or client asset package",
                "expected_output": "A distribution plan with chosen format, section map, and production next step.",
                "skills": ["creative-assembly", "content-series", "campaign-architect"],
            },
        }
    elif "deck" in lowered or "presentation" in lowered:
        return {
            "Use Now": {
                "title": f"Create a presenter script from {obj}.",
                "route": "creative-assembly",
                "instruction": "create a presenter script with slide beats, transitions, and emphasis notes",
                "expected_output": "A presenter script with slide-by-slide talk track and emphasis notes.",
                "skills": ["creative-assembly", "brief", "steering-compass"],
            },
            "Harden": {
                "title": f"Stress-test {obj} for gaps, proof, and narrative flow.",
                "route": "adversarial-review",
                "instruction": "stress-test this deck for narrative gaps, proof gaps, audience confusion, and weak calls to action",
                "expected_output": "A deck critique with priority fixes and stronger narrative flow.",
                "skills": ["adversarial-review", "design-brief", "steering-compass"],
            },
            "Expand": {
                "title": f"Turn {obj} into a webpage, sales asset, or follow-up packet.",
                "route": "design-first-build",
                "instruction": "turn this deck into the best next public or client-facing surface: webpage, sales asset, or follow-up packet",
                "expected_output": "A follow-on asset plan with format choice, sections, and production path.",
                "skills": ["design-first-build", "offer-stack", "creative-assembly"],
            },
        }
    else:
        return {
            "Use Now": {
                "title": f"Create the highest-leverage next asset from {obj}.",
                "route": "autopilot",
                "instruction": "choose and create the highest-leverage next asset from this session object",
                "expected_output": "The next most useful asset with why-this-format rationale.",
                "skills": ["autopilot", "steering-compass", "creative-assembly"],
            },
            "Harden": {
                "title": f"Make the strongest process inside {obj} reusable.",
                "route": "source-to-skill-system",
                "instruction": "identify the strongest reusable process inside this object and package the smallest durable version",
                "expected_output": "A reusable process packet with route, checklist, and validation standard.",
                "skills": ["source-to-skill-system", "repeatability-spine", "knowledge-librarian"],
            },
            "Expand": {
                "title": f"Turn {obj} into a larger campaign, system, or capability.",
                "route": "campaign-architect",
                "instruction": "map this object into a larger campaign, system, or capability with the next three build surfaces",
                "expected_output": "A bigger-outcome map with campaign/system options and the best next surface.",
                "skills": ["campaign-architect", "source-to-skill-system", "business-intelligence"],
            },
        }


def entailment(name: str, expected_output: str, capability: str) -> str:
    if name == "Use Now":
        return f"{expected_output} Uses this capability: {capability}"
    if name == "Harden":
        return f"{expected_output} Focuses on the gap that would make the work fail later."
    return f"{expected_output} Pushes the session into a bigger reusable or creative container."


def expected_output_for(work_type: str, name: str) -> str:
    outputs = {
        "artifact_followup": {
            "Use Now": "A presentation script, briefing, slide outline, webpage brief, or content asset drawn from the artifact.",
            "Harden": "A reusable process packet with workflow/skill candidate, validation checklist, and cold-start prompt.",
            "Expand": "A launch, campaign, or content sprint with assets, timeline, and quality bar.",
        },
        "revenue_client": {
            "Use Now": "A client-facing asset with buyer trigger, promise, proof path, and next action.",
            "Harden": "A belief-gap, proof-gap, objection, and buyer-trigger review with one prioritized fix.",
            "Expand": "A commercial expansion map: service ladder, acquisition asset, delivery workflow, and reuse hook.",
        },
        "content_creative": {
            "Use Now": "A publishable content asset plus the taste choice that makes it stronger.",
            "Harden": "A quality review naming sameness risk, weak hook, proof gap, and rewrite path.",
            "Expand": "A campaign or series map with formats, angles, sequence, and reusable taste rules.",
        },
        "source_capability": {
            "Use Now": "A reusable capability contract with one source-grounded validation example.",
            "Harden": "A source-grounding and duplicate-system triage with the safest build shape.",
            "Expand": "A library map with related routes, cold-start prompt, reuse hook, and future verifier.",
        },
        "system_operator": {
            "Use Now": "A local proof-backed repair packet with owner, changed surface, verifier, and receipt.",
            "Harden": "A regression-focused audit with one prioritized repair or guard and verifier evidence.",
            "Expand": "An operating primitive, workflow, verifier, or global thin-bridge recommendation.",
        },
        "session_closeout": {
            "Use Now": "A fresh-session smoke prompt plus retrieval handoff that proves the next thread starts with the new behavior.",
            "Harden": "A closeout-format audit that catches old-template leakage and names the exact source to patch.",
            "Expand": "A reusable closeout benchmark with good/bad examples, verifier expectations, and a cold-start prompt.",
        },
        "steering_persistence": {
            "Use Now": "A normal-answer smoke test that shows the enriched final-answer surface without invoking a slash command.",
            "Harden": "A global/workspace instruction audit plus renderer comparison for always-on steering.",
            "Expand": "A reusable visible-answer benchmark with expected fields, failure cases, and verification commands.",
        },
        "generic": {
            "Use Now": "One concrete next artifact plus the operating move it teaches.",
            "Harden": "A missing-proof or unclear-owner audit with one highest-value improvement.",
            "Expand": "A reusable route, prompt, verifier, or larger outcome map.",
        },
    }
    return outputs.get(work_type, outputs["generic"]).get(name, outputs["generic"][name])


def build_prompts(objective: str = "", stage: str = "closeout") -> dict[str, Any]:
    state = state_context(objective)
    obj = state["objective"]
    route = state["route"]
    context_paths = state["context_paths"]

    if stage == "execute-next":
        return build_execute_next_payload(state)

    objective_provided = bool(state.get("objective_provided"))
    work_type = infer_work_type(obj, route, objective_provided)
    profile = WORK_PROFILES[work_type]
    if objective_provided and work_type not in {"system_operator"}:
        use_route = route_for(profile, "use_route", "autopilot")
    else:
        use_route = route if route not in {"", "unknown", "autopilot"} else route_for(profile, "use_route", "autopilot")
    artifact_specs = artifact_followup_specs(clean_objective_label(obj)) if work_type == "artifact_followup" else {}

    prompts = [
        enrich_item(
            name="Use Now",
            route=str(artifact_specs.get("Use Now", {}).get("route") or use_route),
            objective=obj,
            instruction=str(artifact_specs.get("Use Now", {}).get("instruction") or profile["use_instruction"]),
            context_paths=context_paths,
            suggested_skills=list(artifact_specs.get("Use Now", {}).get("skills") or [use_route, "steering-compass", *profile["skills"]]),
            when_to_use="Use when the session has enough direction and the best value is making the next artifact real.",
            why="It turns the current idea into a visible next-state while teaching the operating move behind it.",
            operator_insight=profile["operator_insight"],
            hidden_gap=profile["hidden_gap"],
            capability=profile["capability"],
            expected_output=str(artifact_specs.get("Use Now", {}).get("expected_output") or expected_output_for(work_type, "Use Now")),
            quality_bar="A cold reader can tell what changed, why it matters, and what capability was unlocked.",
            skip_if="Skip if the next move would require a taste, scope, risk, external, or approval decision first.",
            work_type=work_type,
            title_override=str(artifact_specs.get("Use Now", {}).get("title") or ""),
        ),
        enrich_item(
            name="Harden",
            route=str(artifact_specs.get("Harden", {}).get("route") or route_for(profile, "harden_route", "system-audit")),
            objective=obj,
            instruction=str(artifact_specs.get("Harden", {}).get("instruction") or profile["harden_instruction"]),
            context_paths=context_paths,
            suggested_skills=list(
                artifact_specs.get("Harden", {}).get("skills")
                or [route_for(profile, "harden_route", "system-audit"), "repeatability-spine", "steering-compass"]
            ),
            when_to_use="Use when the result is promising but the weakest proof, taste, routing, or repeatability link could quietly cap quality.",
            why="It protects momentum by finding the blind spot before it becomes rework.",
            operator_insight="The fastest way to improve output is often to identify the one failure mode that would make it non-reusable.",
            hidden_gap="If this step is skipped, the work may feel good in-session but fail as a cold-start asset later.",
            capability="Codex can run adversarial review, route checks, regression guards, and receipts as part of the same working loop.",
            expected_output=str(artifact_specs.get("Harden", {}).get("expected_output") or expected_output_for(work_type, "Harden")),
            quality_bar="The hardening pass should reduce a real risk, not add ceremony or broad caution.",
            skip_if="Skip if the output is intentionally disposable or the cost of proof is higher than the value of reuse.",
            work_type=work_type,
            title_override=str(artifact_specs.get("Harden", {}).get("title") or ""),
        ),
        enrich_item(
            name="Expand",
            route=str(artifact_specs.get("Expand", {}).get("route") or route_for(profile, "expand_route", "source-to-skill-system")),
            objective=obj,
            instruction=str(artifact_specs.get("Expand", {}).get("instruction") or profile["expand_instruction"]),
            context_paths=context_paths,
            suggested_skills=list(
                artifact_specs.get("Expand", {}).get("skills")
                or [route_for(profile, "expand_route", "source-to-skill-system"), "extraction-governor-agent", "knowledge-librarian"]
            ),
            when_to_use="Use when the session contains a mechanic, taste rule, offer angle, or workflow that could compound beyond today.",
            why="It pushes the work from task completion into a larger creative or operating asset.",
            operator_insight="Expansion is not doing more; it is finding the next container where the insight becomes reusable.",
            hidden_gap="The bigger opportunity may be a system, offer, content series, verifier, or library primitive hiding inside the current task.",
            capability="Codex can productize, systematize, route, and preserve a winning move instead of leaving it trapped in conversation.",
            expected_output=str(artifact_specs.get("Expand", {}).get("expected_output") or expected_output_for(work_type, "Expand")),
            quality_bar="The expansion should make the next session more powerful, not merely create more work.",
            skip_if="Skip if the current priority is shipping a narrow artifact and expansion would distract from delivery.",
            work_type=work_type,
            title_override=str(artifact_specs.get("Expand", {}).get("title") or ""),
        ),
    ]
    return {
        "stage": stage,
        "objective": obj,
        "work_type": work_type,
        "context_paths": context_paths,
        "prompts": prompts,
    }


def build_execute_next_payload(state: dict[str, Any]) -> dict[str, Any]:
    route = state["route"] if state["route"] not in {"", "unknown"} else "autopilot"
    objective = state["objective"]
    context_paths = state["context_paths"]
    verifier = (
        "python3 execution/verify_google_operator_core.py"
        if route in {"system-audit", "steering-compass", "mission", "source-to-skill-system"}
        else f"python3 execution/workflow_router.py search \"{objective}\""
    )
    return {
        "stage": "execute-next",
        "objective": objective,
        "context_paths": context_paths,
        "local_next_action": {
            "owner": route,
            "mode": "patch_and_verify",
            "action": (
                "Take the next safe workspace-local step now, keep edits narrow, run the verifier, "
                "and write a run receipt instead of handing back another prompt."
            ),
            "first_command": f"python3 execution/codex_operator_preflight.py \"{objective}\" --plain",
            "verifier_command": verifier,
            "receipt_required": True,
            "stop_conditions": [
                "external write, publishing, outreach, or connector write",
                "destructive cleanup or broad delete/archive/reset",
                "global ~/.codex or Codex Antigravity mutation",
                "paid or quota-heavy tool use without cost-gate approval",
                "real subagent edits or further subagent spawning without explicit authorization",
            ],
        },
    }


def render_markdown(payload: dict[str, Any]) -> str:
    if payload.get("stage") == "execute-next":
        action = payload["local_next_action"]
        lines = [
            "## Local Next Action",
            f"- **Owner:** /{action['owner']}",
            f"- **Mode:** {action['mode']}",
            f"- **Action:** {action['action']}",
            f"- **First command:** `{action['first_command']}`",
            f"- **Verifier:** `{action['verifier_command']}`",
            f"- **Receipt required:** {action['receipt_required']}",
            "- **Stop conditions:** " + "; ".join(action["stop_conditions"]),
        ]
        return "\n".join(lines)

    lines = ["## 3 Next Prompts", "", "Suggested follow-ups:"]
    for idx, item in enumerate(payload["prompts"], 1):
        lines.extend(
            [
                f"{idx}. **{item['followup_title']}**",
                f"   - **Path:** {item['name']}",
                f"   - **What it entails:** {item['entails']}",
                f"   - **Output/Capability Move:** {item['suggestion_family']} - {item['frontier_pattern']}",
                f"   - **Operator Insight:** {item['operator_insight']}",
                f"   - **Hidden Gap/Opportunity:** {item['hidden_gap_opportunity']}",
                f"   - **Capability Revealed:** {item['capability_revealed']}",
                f"   - **Prompt:** `{item['prompt']}`",
                f"   - **Quality bar:** {item['quality_bar']}",
                f"   - **Suggested skills/workflows:** {', '.join('/' + skill.lstrip('/') for skill in item['suggested_skills'])}",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render contextual next prompts.")
    parser.add_argument("--objective", default="", help="Override the inferred session objective.")
    parser.add_argument("--stage", default="closeout", help="Session stage label.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of Markdown.")
    args = parser.parse_args()

    payload = build_prompts(objective=args.objective, stage=args.stage)
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(render_markdown(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
