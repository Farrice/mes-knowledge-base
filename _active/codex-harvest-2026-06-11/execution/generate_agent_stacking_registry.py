#!/usr/bin/env python3
"""Generate a compact registry of declared Antigravity expert/skill stackings."""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
AGENTS_DIR = ROOT / "agents"
OUT_DIR = ROOT / "semantic_libraries" / "antigravity" / "stacking"
JSON_OUT = OUT_DIR / "agent-stacking-registry.json"
MD_OUT = OUT_DIR / "agent-stacking-registry.md"

STACKING_SECTION_PATTERNS = [
    re.compile(
        r"##+\s*(Stacking Guide|Skill Stacking|Cross-Expert Stacking|Cross-Skill Pairings|Stacking Defaults|Stacking|Pairs With)\s*\n(.*?)(?=\n##|\Z)",
        re.DOTALL | re.IGNORECASE,
    ),
]

TOKEN_PATTERN = re.compile(r"`([a-z0-9][a-z0-9\-]+)`|\[([a-z0-9][a-z0-9\-]+)\]")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def all_skill_names() -> set[str]:
    if not SKILLS_DIR.exists():
        return set()
    return {path.parent.name for path in SKILLS_DIR.glob("*/SKILL.md")}


def all_agent_names() -> set[str]:
    if not AGENTS_DIR.exists():
        return set()
    return {path.parent.name for path in AGENTS_DIR.glob("*/AGENT.md")}


def extract_sections(text: str) -> list[dict[str, str]]:
    sections = []
    for pattern in STACKING_SECTION_PATTERNS:
        for match in pattern.finditer(text):
            sections.append({
                "heading": match.group(1).strip(),
                "body": match.group(2).strip(),
            })
    return sections


def extract_declared_names(body: str, known: set[str]) -> list[str]:
    found = set()
    for match in TOKEN_PATTERN.findall(body):
        candidate = match[0] or match[1]
        if candidate in known:
            found.add(candidate)
    return sorted(found)


def skill_stacking_guides(known: set[str]) -> list[dict[str, Any]]:
    entries = []
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        text = read_text(skill_md)
        sections = extract_sections(text)
        if not sections:
            continue
        declared = sorted({
            name
            for section in sections
            for name in extract_declared_names(section["body"], known)
            if name != skill_md.parent.name
        })
        entries.append({
            "skill": skill_md.parent.name,
            "path": str(skill_md.relative_to(ROOT)),
            "section_headings": [section["heading"] for section in sections],
            "declared_partners": declared,
            "evidence_excerpt": sections[0]["body"][:700],
        })
    return entries


def agent_stacking_sections(known: set[str]) -> list[dict[str, Any]]:
    entries = []
    for agent_md in sorted(AGENTS_DIR.glob("*/AGENT.md")):
        text = read_text(agent_md)
        sections = extract_sections(text)
        if not sections:
            continue
        declared = sorted({
            name
            for section in sections
            for name in extract_declared_names(section["body"], known)
            if name != agent_md.parent.name
        })
        entries.append({
            "agent": agent_md.parent.name,
            "path": str(agent_md.relative_to(ROOT)),
            "section_headings": [section["heading"] for section in sections],
            "declared_partners": declared,
            "evidence_excerpt": sections[0]["body"][:700],
        })
    return entries


def expert_router_compounds() -> list[dict[str, Any]]:
    sys.path.insert(0, str(ROOT / "execution"))
    try:
        import expert_router  # type: ignore
    except Exception as exc:  # pragma: no cover - defensive CLI behavior
        return [{"error": f"Could not import expert_router: {exc}"}]

    return [
        {
            "pair": item.get("pair", []),
            "effect": item.get("effect", ""),
            "triggers": item.get("trigger", []),
            "source": "execution/expert_router.py",
        }
        for item in getattr(expert_router, "COMPOUNDS", [])
    ]


def routing_intelligence_ensembles() -> list[dict[str, Any]]:
    path = ROOT / ".agent" / "routing-intelligence.json"
    if not path.exists():
        return []
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError:
        return []

    feedback = {
        item.get("routing_id"): item.get("rating")
        for item in data.get("feedback_log", [])
    }
    ensembles: dict[str, dict[str, Any]] = {}
    for decision in data.get("routing_decisions", []):
        if not decision.get("ensemble"):
            continue
        pairing = decision.get("compound_pairing") or " + ".join(decision.get("experts_deployed", []))
        if not pairing:
            continue
        stats = ensembles.setdefault(pairing, {"pairing": pairing, "uses": 0, "positive": 0, "negative": 0, "mixed": 0})
        stats["uses"] += 1
        rating = feedback.get(decision.get("routing_id"))
        if rating in {"positive", "negative", "mixed"}:
            stats[rating] += 1
    return sorted(ensembles.values(), key=lambda item: (-item["positive"], -item["uses"], item["pairing"]))


def build_registry() -> dict[str, Any]:
    known = all_skill_names() | all_agent_names()
    compounds = expert_router_compounds()
    skill_guides = skill_stacking_guides(known)
    agent_guides = agent_stacking_sections(known)
    ensembles = routing_intelligence_ensembles()

    return {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sources": [
            "execution/expert_router.py COMPOUNDS",
            "skills/*/SKILL.md stacking sections",
            "agents/*/AGENT.md stacking sections",
            ".agent/routing-intelligence.json ensemble feedback",
            "execution/cascade_detector.py downstream parser remains the live cascade source",
        ],
        "counts": {
            "expert_router_compounds": len(compounds),
            "skill_stacking_guides": len(skill_guides),
            "agent_stacking_sections": len(agent_guides),
            "routing_intelligence_ensembles": len(ensembles),
        },
        "expert_router_compounds": compounds,
        "skill_stacking_guides": skill_guides,
        "agent_stacking_sections": agent_guides,
        "routing_intelligence_ensembles": ensembles,
        "selection_policy": [
            "Prefer trigger-matched declared compounds.",
            "Use skill stacking guides when they name a partner or use case.",
            "Promote pairings with positive routing-intelligence feedback.",
            "Use cascade relationships for downstream risk and adjacent checks.",
            "Skip stacking when one workflow or expert is sufficient.",
        ],
    }


def write_markdown(registry: dict[str, Any]) -> None:
    lines = [
        "# Agent Stacking Registry",
        "",
        f"Generated: {registry['generated_at']}",
        "",
        "## Counts",
        "",
        "| Source | Count |",
        "|---|---:|",
    ]
    for key, value in registry["counts"].items():
        lines.append(f"| {key.replace('_', ' ')} | {value} |")

    lines.extend([
        "",
        "## Selection Policy",
        "",
    ])
    for item in registry["selection_policy"]:
        lines.append(f"- {item}")

    lines.extend([
        "",
        "## Expert Router Compounds",
        "",
        "| Pair | Effect | Triggers |",
        "|---|---|---|",
    ])
    for item in registry["expert_router_compounds"][:60]:
        pair = " + ".join(item.get("pair", []))
        effect = str(item.get("effect", "")).replace("|", "/")
        triggers = ", ".join(item.get("triggers", [])[:5]).replace("|", "/")
        lines.append(f"| {pair} | {effect} | {triggers} |")

    lines.extend([
        "",
        "## Skill Stacking Guides",
        "",
        "| Skill | Partners | Section |",
        "|---|---|---|",
    ])
    for item in registry["skill_stacking_guides"][:120]:
        partners = ", ".join(item.get("declared_partners", [])[:8]) or "declared in prose"
        headings = ", ".join(item.get("section_headings", []))
        lines.append(f"| {item['skill']} | {partners} | {headings} |")

    lines.extend([
        "",
        "## Agent Stacking Sections",
        "",
        "| Agent | Partners | Section |",
        "|---|---|---|",
    ])
    for item in registry["agent_stacking_sections"][:120]:
        partners = ", ".join(item.get("declared_partners", [])[:8]) or "declared in prose"
        headings = ", ".join(item.get("section_headings", []))
        lines.append(f"| {item['agent']} | {partners} | {headings} |")

    lines.extend([
        "",
        "## Routing Intelligence Ensembles",
        "",
        "| Pairing | Uses | Positive | Negative | Mixed |",
        "|---|---:|---:|---:|---:|",
    ])
    for item in registry["routing_intelligence_ensembles"][:80]:
        lines.append(
            f"| {item['pairing']} | {item['uses']} | {item['positive']} | {item['negative']} | {item['mixed']} |"
        )

    MD_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    registry = build_registry()
    JSON_OUT.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_markdown(registry)
    print(f"Wrote {JSON_OUT.relative_to(ROOT)}")
    print(f"Wrote {MD_OUT.relative_to(ROOT)}")
    print(json.dumps(registry["counts"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
