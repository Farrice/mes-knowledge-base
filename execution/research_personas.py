#!/usr/bin/env python3
"""
Research Personas + Swarm Plan — the expert-casting layer for the native deep-
research swarm.

The Kimi-style model: don't fan out N identical agents — fan out N agents each
wearing a DIFFERENT world-class expert lens, so the converged synthesis is deeper
than any single call. This module maps each research angle (from
deep_research_engine.DECOMPOSITION_TEMPLATES: market_data / competitive /
psychology / contrarian / general) to a roster of real expert personas, then
builds a depth-tiered swarm plan: decompose → cast → per-agent briefs.

Pure planning logic (no network). Consumed by `research.py plan` and the
deep-research-swarm workflow.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "execution"))

try:
    from deep_research_engine import decompose_query, detect_research_intent
except ImportError:
    from execution.deep_research_engine import decompose_query, detect_research_intent


# How many expert agents to fan out per depth tier (user-locked).
# Workflow runs ~16 concurrent; the rest queue. These are TOTAL agents.
DEPTH_AGENT_COUNT = {"quick": 3, "standard": 6, "deep": 11, "max": 36}

# Each research angle → a roster of world-class expert lenses (real personas from
# agents/_framework/invocation-cards.md + parallel_swarm.ENSEMBLE_FALLBACKS where
# they fit). Diversity of lens per angle is what makes the swarm deep.
RESEARCH_PERSONAS: Dict[str, List[Dict[str, str]]] = {
    "market_data": [
        {"role": "Market Analyst",
         "expert": "McKinsey-grade market analyst",
         "lens": "market size, growth rate, timing windows, structural trends — hard numbers with dated primary sources"},
        {"role": "Data Forensics Researcher",
         "expert": "quant primary-source researcher",
         "lens": "verifiable statistics, original reports, government/industry data — distrust secondary citations, find the source"},
        {"role": "Trend Scout",
         "expert": "Grace Beverley (new-media trend reading)",
         "lens": "emerging signals, what's accelerating right now, leading indicators the mainstream hasn't priced in"},
    ],
    "competitive": [
        {"role": "Positioning Strategist",
         "expert": "April Dunford (obviously awesome positioning)",
         "lens": "how players position, their wedge, category design, where the positioning gaps are"},
        {"role": "Business-Model Reverse-Engineer",
         "expert": "operator/strategist (Sharran Srivatsaa lens)",
         "lens": "revenue architecture, unit economics, growth engines, what actually makes the money"},
    ],
    "psychology": [
        {"role": "Buyer Psychologist",
         "expert": "Alen Sultanic (deep buyer psychology)",
         "lens": "hidden purchase drivers, objection layers, the real (often unspoken) reason people buy"},
        {"role": "Voice-of-Customer Miner",
         "expert": "Luke Iha (proof + VOC)",
         "lens": "verbatim language from Reddit, reviews, forums, comments — exact phrasing, not paraphrase"},
        {"role": "Belief & Identity Analyst",
         "expert": "David McRaney (deep canvassing)",
         "lens": "identity-level resistance, worldview, what belief must shift before they act"},
    ],
    "contrarian": [
        {"role": "Contrarian Scout",
         "expert": "Harry Dry (skeptic / three-rules rigor)",
         "lens": "what the mainstream gets wrong, failed approaches, counter-narratives backed by evidence"},
        {"role": "Risk Auditor",
         "expert": "adversarial analyst",
         "lens": "downside, regulatory/structural risk, why this fails, the strongest argument against"},
    ],
    "general": [
        {"role": "Domain Synthesist",
         "expert": "generalist senior analyst",
         "lens": "core facts, expert consensus, the key frameworks a newcomer must know"},
        {"role": "Case-Study Investigator",
         "expert": "evidence-first researcher",
         "lens": "concrete examples, case studies, real results with named sources"},
    ],
}


def _personas_for(angle: str) -> List[Dict[str, str]]:
    return RESEARCH_PERSONAS.get(angle) or RESEARCH_PERSONAS["general"]


def build_swarm_plan(query: str, depth: str = "deep") -> Dict:
    """Decompose the query and cast a depth-tiered roster of expert agents.

    Returns a JSON-serializable plan: {query, intent, depth, agent_count,
    agents:[{id, angle, role, expert, lens, question, search_queries}], waves}.
    Each agent wears a distinct expert lens — the diversity is the point.
    """
    intent = detect_research_intent(query)
    base = decompose_query(query, intent)  # ResearchSubQuestion[] with filled search_queries
    target = DEPTH_AGENT_COUNT.get(depth, DEPTH_AGENT_COUNT["deep"])

    # Build (sub-question × persona) candidates, cycling personas so each angle's
    # agents wear different lenses.
    candidates = []
    for sq in base:
        for persona in _personas_for(sq.angle):
            candidates.append((sq, persona))

    agents = []
    if target <= len(candidates):
        chosen = candidates[:target]
        for i, (sq, persona) in enumerate(chosen):
            agents.append({
                "id": f"agent-{i+1:02d}",
                "angle": sq.angle,
                "role": persona["role"],
                "expert": persona["expert"],
                "lens": persona["lens"],
                "question": sq.question,
                "search_queries": list(sq.search_queries),
            })
    else:
        # Need MORE agents than (subq × persona): expand by splitting each
        # candidate's search_queries into per-query agents (max-tier depth).
        expanded = []
        for sq, persona in candidates:
            qs = sq.search_queries or [query]
            for q in qs:
                expanded.append((sq, persona, q))
        # If expansion still falls short of target, fewer agents is fine (no padding).
        for i, (sq, persona, q) in enumerate(expanded[:target]):
            agents.append({
                "id": f"agent-{i+1:02d}",
                "angle": sq.angle,
                "role": persona["role"],
                "expert": persona["expert"],
                "lens": persona["lens"],
                "question": sq.question,
                "search_queries": [q] + [x for x in (sq.search_queries or []) if x != q][:1],
            })

    # Suggested wave structure: ~16 concurrent, rest queue.
    wave_size = 16
    waves = [agents[i:i + wave_size] for i in range(0, len(agents), wave_size)]

    return {
        "query": query,
        "intent": intent,
        "depth": depth,
        "agent_count": len(agents),
        "wave_count": len(waves),
        "agents": agents,
    }


def persona_research_prompt(agent: Dict, query: str) -> str:
    """Render the research brief an individual swarm agent receives. It ADOPTS
    the expert persona and is bound to the no-source-no-finding rule."""
    qs = "\n".join(f"   - {q}" for q in agent.get("search_queries", []))
    return (
        f"You are a **{agent['role']}** — research this through the lens of "
        f"**{agent['expert']}**.\n\n"
        f"## Overall research question\n{query}\n\n"
        f"## Your assigned angle: {agent['angle']}\n{agent['question']}\n\n"
        f"## Your expert lens (use it — this is why YOU are on this)\n{agent['lens']}\n\n"
        f"## How to research (all $0 — tools you already have)\n"
        f"1. `tvly search` / `tvly research` for cited multi-source grounding on your angle.\n"
        f"2. `WebSearch` across these queries, then `WebFetch` (or `tvly extract`) the 2-3\n"
        f"   strongest sources for FULL-page reads — not snippets:\n{qs}\n"
        f"3. Mine real human language where your lens calls for it (Reddit, reviews, forums).\n"
        f"4. Adversarially check: would a skeptic find a contradicting source? Drop what you\n"
        f"   cannot stand behind.\n\n"
        f"## Output (STRICT)\n"
        f"Return 5-12 findings as JSON. EVERY finding MUST have a real `source_url` — a claim\n"
        f"with no URL is not a finding, omit it. Schema per finding:\n"
        f'  {{"claim": "...", "source_url": "https://...", "excerpt": "verbatim snippet", '
        f'"confidence": "high|medium|low", "finding_type": "data|quote|statistic|opinion|case_study"}}\n'
        f"Plus a 2-3 sentence `angle_insight` — the non-obvious thing your expert lens surfaced."
    )


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(prog="research_personas.py")
    p.add_argument("query")
    p.add_argument("--depth", default="deep", choices=["quick", "standard", "deep", "max"])
    a = p.parse_args()
    print(json.dumps(build_swarm_plan(a.query, a.depth), indent=2))
