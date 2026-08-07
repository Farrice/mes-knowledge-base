#!/usr/bin/env python3
"""Codex-native Kimi swarm packet compiler.

This is the thin bridge between Kimi-style context packs and the Antigravity
owners that should actually run the work:

- research mode delegates shape to /deep-research-os and research.py planning
- general mode delegates shape to /convene and council_cast.py planning
- real Codex subagents are never spawned here; packets and receipts are emitted
  for approved-per-run delegation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional


ROOT = Path(__file__).resolve().parents[1]
EXEC = ROOT / "execution"
sys.path.insert(0, str(EXEC))

try:
    from council_cast import build_council_plan, council_member_prompt
    from research_personas import build_swarm_plan, persona_research_prompt
except ImportError:  # imported as execution.kimi_swarm
    from execution.council_cast import build_council_plan, council_member_prompt
    from execution.research_personas import build_swarm_plan, persona_research_prompt


DEPTHS = {"quick", "standard", "deep", "max"}
MODES = {"research", "general", "auto"}
CONVENE_MODES = {"wide", "tight", "strike", "deploy"}


@dataclass
class ContextPack:
    path: str = ""
    raw: str = ""
    title: str = ""
    objectives: List[str] | None = None
    guardrails: List[str] | None = None
    worker_briefs: List[str] | None = None
    synthesis_criteria: List[str] | None = None
    context: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self.path,
            "title": self.title,
            "objectives": self.objectives or [],
            "guardrails": self.guardrails or [],
            "worker_briefs": self.worker_briefs or [],
            "synthesis_criteria": self.synthesis_criteria or [],
            "context": self.context,
            "raw_chars": len(self.raw),
        }


def slugify(value: str, limit: int = 64) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return (slug[:limit].strip("-") or "kimi-swarm")


def _bullets(section: str) -> List[str]:
    out = []
    for line in section.splitlines():
        line = line.strip()
        if not line:
            continue
        line = re.sub(r"^[-*]\s+", "", line)
        line = re.sub(r"^\d+[.)]\s+", "", line)
        if line:
            out.append(line)
    return out


def _section(text: str, *names: str) -> str:
    for name in names:
        pattern = re.compile(
            rf"^#+\s*{re.escape(name)}\s*$([\s\S]*?)(?=^#+\s+|\Z)",
            re.IGNORECASE | re.MULTILINE,
        )
        match = pattern.search(text)
        if match:
            return match.group(1).strip()
    return ""


def load_context_pack(path: Optional[str]) -> Optional[ContextPack]:
    if not path:
        return None
    p = Path(path).expanduser()
    if not p.is_absolute():
        p = ROOT / p
    raw = p.read_text(encoding="utf-8", errors="ignore")
    try:
        data = json.loads(raw)
        return ContextPack(
            path=str(p),
            raw=raw,
            title=str(data.get("title") or data.get("name") or p.stem),
            objectives=list(data.get("objectives") or []),
            guardrails=list(data.get("guardrails") or []),
            worker_briefs=list(data.get("worker_briefs") or data.get("workers") or []),
            synthesis_criteria=list(data.get("synthesis_criteria") or data.get("quality_bar") or []),
            context=str(data.get("context") or data.get("brief") or ""),
        )
    except Exception:
        pass

    title = ""
    title_match = re.search(r"^#\s+(.+)$", raw, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
    objectives = _bullets(_section(raw, "Objectives", "Locked Objectives", "Goal"))
    guardrails = _bullets(_section(raw, "Guardrails", "Rules", "Constraints"))
    worker_briefs = _bullets(_section(raw, "Worker Roles", "Worker Briefs", "Workers"))
    synthesis_criteria = _bullets(_section(raw, "Synthesis Criteria", "Quality Bar", "Acceptance Criteria"))
    context = _section(raw, "Context Pack", "Context", "Brief")
    return ContextPack(
        path=str(p),
        raw=raw,
        title=title or p.stem,
        objectives=objectives,
        guardrails=guardrails,
        worker_briefs=worker_briefs,
        synthesis_criteria=synthesis_criteria,
        context=context,
    )


def objective_from_pack(objective: str, pack: Optional[ContextPack]) -> str:
    if objective:
        return objective
    if pack and pack.objectives:
        return pack.objectives[0]
    if pack and pack.title:
        return pack.title
    return "Kimi swarm task"


def detect_mode(objective: str, requested: str) -> str:
    if requested in {"research", "general"}:
        return requested
    lowered = objective.lower()
    research_terms = (
        "research", "market", "competitor", "sources", "cite", "evidence",
        "trend", "landscape", "icp", "buyer psychology", "analysis",
    )
    return "research" if any(term in lowered for term in research_terms) else "general"


def build_research_packet(
    objective: str,
    *,
    depth: str = "standard",
    allow_subagents: bool = False,
    pack: Optional[ContextPack] = None,
) -> Dict[str, Any]:
    swarm = build_swarm_plan(objective, depth)
    packets = []
    for agent in swarm.get("agents", []):
        packets.append({
            "worker_id": agent["id"],
            "worker_type": "research-angle",
            "role": agent["role"],
            "expert": agent["expert"],
            "angle": agent["angle"],
            "question": agent["question"],
            "search_queries": agent.get("search_queries", []),
            "prompt": persona_research_prompt(agent, objective),
            "output_contract": {
                "format": "json",
                "required": ["findings", "angle_insight"],
                "finding_required_fields": ["claim", "source_url"],
                "source_rule": "No source_url means the claim is not a finding.",
            },
        })
    slug = slugify(objective)
    return {
        "schema_version": "kimi-swarm/v1",
        "mode": "research",
        "owner": "/deep-research-os",
        "composer": "/virtuoso",
        "bridge": "/kimi-swarm",
        "objective": objective,
        "depth": depth,
        "context_pack": pack.to_dict() if pack else None,
        "phase_sequence": [
            "Cast: research.py plan decomposes the query and casts expert lenses.",
            "Fan-out: each worker gathers only sourced findings for its assigned angle.",
            "Gap-fill: critic identifies missing angles; extra packets fill them for deep/max.",
            "Verify: adversarial check refutes or drops weak factual claims.",
            "Synthesize: ingest JSONL through research.py to produce a Research Receipt.",
        ],
        "swarm_plan": {
            "intent": swarm.get("intent"),
            "agent_count": swarm.get("agent_count"),
            "wave_count": swarm.get("wave_count"),
        },
        "worker_packets": packets,
        "source_rules": [
            "Every persisted finding must carry a real URL.",
            "Unsourced worker claims are quarantined, not synthesized as facts.",
            "Paid/current research providers remain budget-gated and approval-aware.",
            "Use grounding_guard.py before shipping factual strategy or client work.",
        ],
        "commands": {
            "plan": f"python3 execution/research.py plan --query {json.dumps(objective)} --depth {depth}",
            "gemini_start": f"python3 execution/research.py gemini-start --query {json.dumps(objective)} --mode standard",
            "ingest": f"python3 execution/research.py ingest --findings .tmp/research/{slug}/native-findings.jsonl --query {json.dumps(objective)} --depth {depth} --swarm",
        },
        "delegation": {
            "allow_subagents_requested": allow_subagents,
            "real_subagents_spawned": False,
            "activation_boundary": "real Codex subagents require explicit approval per run",
            "integration_owner": "main Codex thread",
            "delegation_receipt_required": True,
        },
        "receipt": {
            "research_receipt": "produced by execution/research.py ingest or run",
            "packet_count": len(packets),
            "synthesis_owner": "main Codex thread",
            "what_we_would_have_missed": "required in final synthesis when angle insights diverge",
        },
        "verification": [
            "python3 execution/verify_kimi_swarm.py",
            "python3 execution/verify_deep_research_os.py",
            "python3 execution/verify_subagent_readiness.py",
        ],
    }


def build_general_packet(
    objective: str,
    *,
    convene_mode: str = "wide",
    allow_subagents: bool = False,
    pack: Optional[ContextPack] = None,
) -> Dict[str, Any]:
    council = build_council_plan(objective, convene_mode)
    packets = []
    for member in council.get("roster", []):
        packets.append({
            "worker_id": slugify(member["name"], 40),
            "worker_type": "council-voice",
            "name": member["name"],
            "domain_group": member["domain_group"],
            "lens": member["lens"],
            "core_method": member["core_method"],
            "genius_path": member.get("genius_path"),
            "wildcard": bool(member.get("wildcard")),
            "is_user_lens": bool(member.get("is_user")),
            "prompt": council_member_prompt(member, objective),
            "output_contract": {
                "format": "json",
                "required": ["take", "signature_angle", "the_move"],
                "grounding_rule": "Facts and numbers must be sourced or flagged as assumptions.",
            },
        })
    slug = slugify(objective, 48)
    return {
        "schema_version": "kimi-swarm/v1",
        "mode": "general",
        "owner": "/convene",
        "composer": "/virtuoso",
        "bridge": "/kimi-swarm",
        "objective": objective,
        "convene_mode": convene_mode,
        "context_pack": pack.to_dict() if pack else None,
        "phase_sequence": [
            "Convene: council_cast.py selects diverse voices, domain caps, wildcards, and Farrice's lens.",
            "Diverge: every voice produces an independent take before seeing others.",
            "Inner Council: select complementary tension, not merely the most agreeable voices.",
            "Deliberate: run two rounds of build/challenge/cross-pollination and preserve forks.",
            "Synthesize: produce one integrated outcome plus grounding_guard.py verdict.",
            "Learn: write How the Masters Thought digest and append one mental model to the rubric.",
        ],
        "council_plan": {
            "roster_size": council.get("roster_size"),
            "domains_represented": council.get("domains_represented", []),
            "domain_count": council.get("domain_count"),
            "inner_council_size": council.get("inner_council_size"),
            "wildcards": council.get("wildcards", []),
        },
        "worker_packets": packets,
        "inner_council_rule": {
            "selection": "choose the most complementary voices after divergent takes",
            "minimum_tension": "at least one productive disagreement or fork must survive synthesis",
            "fallback": "if matching is weak, seat the highest-signal takes and include a wildcard when available",
        },
        "synthesis_contract": {
            "sections": [
                "The Outcome",
                "Why It Is More Than The Parts",
                "Forks For Farrice",
                "Next Moves We Make Together",
                "What We Would Have Missed",
            ],
            "grounding_guard": f"python3 execution/grounding_guard.py .tmp/council/{slug}-outcome.md --task-type Strategy",
            "learning_digest_path": f"knowledge/council-sessions/<date>-{slug}.md",
            "rubric_path": "knowledge/council-rubric.md",
        },
        "delegation": {
            "allow_subagents_requested": allow_subagents,
            "real_subagents_spawned": False,
            "activation_boundary": "real Codex subagents require explicit approval per run",
            "integration_owner": "main Codex thread",
            "delegation_receipt_required": True,
        },
        "receipt": {
            "convene_receipt": "packet plan produced; real deliberation occurs in main thread or approved workers",
            "packet_count": len(packets),
            "synthesis_owner": "main Codex thread",
            "learning_required": True,
        },
        "verification": [
            "python3 execution/verify_convene.py",
            "python3 execution/verify_kimi_swarm.py",
            "python3 execution/verify_virtuoso_orchestration.py",
        ],
    }


def build_plan(
    objective: str,
    *,
    mode: str = "auto",
    depth: str = "standard",
    convene_mode: str = "wide",
    allow_subagents: bool = False,
    from_pack: Optional[str] = None,
) -> Dict[str, Any]:
    pack = load_context_pack(from_pack)
    objective = objective_from_pack(objective, pack)
    resolved = detect_mode(objective, mode)
    if resolved == "research":
        return build_research_packet(objective, depth=depth, allow_subagents=allow_subagents, pack=pack)
    return build_general_packet(objective, convene_mode=convene_mode, allow_subagents=allow_subagents, pack=pack)


def render_markdown(plan: Dict[str, Any]) -> str:
    lines = [
        f"# Kimi Swarm Plan: {plan['objective']}",
        "",
        f"Owner: `{plan['owner']}`",
        f"Composer: `{plan['composer']}`",
        f"Mode: `{plan['mode']}`",
        f"Real subagents spawned: `{str(plan['delegation']['real_subagents_spawned']).lower()}`",
        "",
        "## Phase Sequence",
    ]
    lines += [f"- {phase}" for phase in plan["phase_sequence"]]
    lines += ["", "## Worker Packets"]
    for packet in plan["worker_packets"]:
        label = packet.get("role") or packet.get("name")
        detail = packet.get("angle") or packet.get("domain_group")
        lines.append(f"- `{packet['worker_id']}` - {label} ({detail})")
    lines += ["", "## Verification"]
    lines += [f"- `{cmd}`" for cmd in plan.get("verification", [])]
    return "\n".join(lines)


def _cli() -> int:
    parser = argparse.ArgumentParser(prog="kimi_swarm.py")
    sub = parser.add_subparsers(dest="cmd")
    plan_cmd = sub.add_parser("plan", help="Compile a Kimi-style swarm packet plan")
    plan_cmd.add_argument("objective", nargs="?", default="")
    plan_cmd.add_argument("--mode", default="auto", choices=sorted(MODES))
    plan_cmd.add_argument("--depth", default="standard", choices=sorted(DEPTHS))
    plan_cmd.add_argument("--convene-mode", default="wide", choices=sorted(CONVENE_MODES))
    plan_cmd.add_argument("--allow-subagents", action="store_true")
    plan_cmd.add_argument("--from-pack", default="")
    plan_cmd.add_argument("--json", action="store_true")

    args = parser.parse_args()
    if args.cmd in (None, "plan"):
        if args.cmd is None:
            parser.error("subcommand required: plan")
        result = build_plan(
            args.objective,
            mode=args.mode,
            depth=args.depth,
            convene_mode=args.convene_mode,
            allow_subagents=args.allow_subagents,
            from_pack=args.from_pack or None,
        )
        print(json.dumps(result, indent=2) if args.json else render_markdown(result))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(_cli())
