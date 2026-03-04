#!/usr/bin/env python3
"""
Parallel Swarm Orchestrator — True parallel agent execution for Antigravity.

Fires multiple Gemini API calls concurrently using asyncio, with safety rails
to prevent loop disasters and token budget overruns.

Usage:
    python parallel_swarm.py "Analyze the top 3 competitors in AI consulting"
    python parallel_swarm.py --plan-only "Design a content strategy for LinkedIn"
    python parallel_swarm.py --agents "cardinal-mason,harry-dry,seena-rez" "Write 5 hook variations"
    python parallel_swarm.py --grounded "Research current AI consulting market trends"
"""

import asyncio
import json
import sys
import time
import argparse
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, field

# Shared clients
sys.path.insert(0, str(Path(__file__).parent))
from gemini_client import GeminiClient, load_env
from perplexity_client import PerplexityClient, BudgetExhaustedError

load_env()

import os

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

BASE_PATH = Path(__file__).parent.parent
AGENTS_PATH = BASE_PATH / "agents"
SKILLS_PATH = BASE_PATH / "skills"
OUTPUT_DIR = BASE_PATH / "swarm_outputs"

MAX_RETRIES = int(os.environ.get("SWARM_MAX_RETRIES", "1"))
TOKEN_BUDGET = int(os.environ.get("SWARM_TOKEN_BUDGET", "500000"))
MAX_PARALLEL = int(os.environ.get("SWARM_MAX_PARALLEL", "10"))


# --------------------------------------------------------------------------
# Data Classes
# --------------------------------------------------------------------------

@dataclass
class WorkOrder:
    """A single unit of work for one expert agent."""
    agent_name: str
    objective: str
    context: str
    mandate: List[str]
    output_schema: str = "standard"
    constraints: Dict = field(default_factory=dict)
    depends_on: List[str] = field(default_factory=list)
    batch: int = 0


@dataclass
class AgentResult:
    """Result from a single agent execution."""
    agent_name: str
    status: str  # "success", "failed", "skipped"
    output: str
    tokens_used: int
    estimated_cost: float
    duration_seconds: float
    model_used: str = ""
    thinking_tokens: int = 0
    grounding_queries: int = 0
    retries: int = 0
    error: Optional[str] = None


@dataclass
class SwarmResult:
    """Aggregate result from the full swarm."""
    objective: str
    agent_results: List[AgentResult]
    synthesis: str
    total_tokens: int
    total_duration: float
    total_cost_usd: float


# --------------------------------------------------------------------------
# Expert Registry
# --------------------------------------------------------------------------

EXPERT_DOMAINS = {
    "cardinal-mason": "AI copywriting, conversion, direct response",
    "harry-dry": "Copy evaluation, concrete language, marketing",
    "seena-rez": "TikTok commerce, viral content, hooks",
    "samuel-thompson": "AI info products, launches, unit economics",
    "jim-oshaughnessy": "Philosophy, finance, cross-domain synthesis",
    "jeremy-miner": "Sales, identity persuasion, NEPQ",
    "michael-bernoff": "Identity engineering, mindset transformation",
    "shaan-puri": "Storytelling, narrative architecture, content",
    "kallaway": "Content psychology, viral engineering, retention",
    "oren": "Creative direction, taste development, quality judgment",
    "dan-koe": "One-person business, multipassionate, creator economy",
    "lara-acosta": "LinkedIn content, positioning, ghostwriting",
    "erica-mallet": "Brand magnetism, belief architecture, tribal branding",
    "lulu-cheng-meservey": "Communications strategy, PR, founder narrative",
    "seth-godin": "Viral marketing, ideavirus engineering",
    "tobias-allen": "Direct response marketing, email systems, growth",
    "nicolas-cole": "Digital writing, sentence craft",
    "nathan-gotch": "AI SEO, retrieval layer optimization",
    "adam-enfroy": "Affiliate marketing, topical authority",
    "daniel-priestley": "Oversubscribed methodology, waitlist marketing",
    "tom-noske": "Magnetic personal brand, archetype positioning",
    "sabri-suby": "AI advertising, paid traffic, conversion",
    "rory-sutherland": "Behavioral marketing, psychological reframing",
    "monk-ai": "AI consulting offers, sales psychology",
    "ali-abdaal": "Action bias, overthinking recovery",
    "nick-saraev": "Agentic workflows, self-annealing, MCP",
    "david-bayer": "Elite communication, presence, power dynamics",
    "fareed-zakaria": "Non-fiction writing, argument architecture",
    "jonathan-franzen": "Literary storytelling, compression",
    "lucas-alpay": "Fiction writing, business storytelling",
    "donald-miller": "StoryBrand, culture turnaround, messaging",
    "tommy-clark": "B2B founder content, How I narratives, stealth hooks",
    "jasmin-alic": "LinkedIn organic growth, emotional hooks, rhythmic cadence",
    "josh-sanders": "LinkedIn format arbitrage, depth metrics, outlier engineering",
    "caleb-ralston": "Trust-based personal brand, contrarian positioning, credibility",
    "linkedin-2026-format-arbitrage": "LinkedIn algorithm, format selection, platform optimization",
}


# --------------------------------------------------------------------------
# Agent Context Loading
# --------------------------------------------------------------------------

def load_agent_context(agent_name: str, tier: int = 1,
                       extra_files: Optional[List[str]] = None) -> str:
    """
    Load expert context at the specified tier level.

    Tier 1 (default): AGENT.md + SKILL.md
    Tier 2: AGENT.md + SKILL.md + genius.md + specified workflow files
    """
    agent_dir = AGENTS_PATH / agent_name
    context_parts = []

    agent_file = agent_dir / "AGENT.md"
    if agent_file.exists():
        context_parts.append(agent_file.read_text())

    matched_skill_dir = None
    for skill_name in SKILLS_PATH.iterdir():
        if agent_name in skill_name.name:
            matched_skill_dir = skill_name
            break

    if matched_skill_dir:
        skill_file = matched_skill_dir / "SKILL.md"
        if skill_file.exists():
            context_parts.append(skill_file.read_text())

        if tier >= 2:
            genius_file = matched_skill_dir / "genius.md"
            if genius_file.exists():
                context_parts.append(genius_file.read_text())

            if extra_files:
                for rel_path in extra_files:
                    full_path = matched_skill_dir / rel_path
                    if full_path.exists():
                        context_parts.append(full_path.read_text())
                    else:
                        print(f"  ⚠️  Extra file not found: {full_path}")

    if not context_parts:
        raise FileNotFoundError(
            f"CRITICAL: Failed to load context for agent '{agent_name}'. "
            f"Neither AGENT.md nor SKILL.md could be found. "
            f"To prevent hallucination, script execution is halted."
        )

    return "\n\n---\n\n".join(context_parts)


# --------------------------------------------------------------------------
# Agent Selection
# --------------------------------------------------------------------------

def auto_select_agents(objective: str, max_agents: int = 5) -> List[str]:
    """Simple keyword-based agent selection."""
    objective_lower = objective.lower()
    scores = {}
    for agent, domain in EXPERT_DOMAINS.items():
        score = 0
        for keyword in domain.lower().split(", "):
            if keyword in objective_lower:
                score += 2
            for word in keyword.split():
                if word in objective_lower:
                    score += 1
        if score > 0:
            scores[agent] = score

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    selected = [agent for agent, _ in ranked[:max_agents]]

    if len(selected) < 2:
        defaults = ["cardinal-mason", "jim-oshaughnessy", "shaan-puri"]
        for d in defaults:
            if d not in selected:
                selected.append(d)
            if len(selected) >= 2:
                break

    return selected[:max_agents]


# --------------------------------------------------------------------------
# Work Order Generation
# --------------------------------------------------------------------------

def generate_work_orders(objective: str, agents: List[str],
                         research_brief: str = "") -> List[WorkOrder]:
    """Generate work orders for each agent. All are parallel (batch 0) by default."""
    orders = []
    for agent in agents:
        domain = EXPERT_DOMAINS.get(agent, "general")
        context = f"You are contributing to a multi-expert analysis. Your domain: {domain}."
        if research_brief:
            context += f"\n\n{research_brief}"
        orders.append(WorkOrder(
            agent_name=agent,
            objective=objective,
            context=context,
            mandate=[
                "Apply your specific frameworks and methodology",
                "Provide concrete, actionable recommendations",
                "Flag any dissenting views or contrarian perspectives",
                "Be specific — no generic advice",
            ],
            batch=0,
        ))
    return orders


# --------------------------------------------------------------------------
# Mini-Brief Work Order Generation
# --------------------------------------------------------------------------

MINI_BRIEF_EXPERTS = {
    "story-driven":  {"pain": "kallaway", "hook": "tommy-clark", "asset": "josh-sanders", "platform": "linkedin-2026-format-arbitrage", "taste": "oren"},
    "contrarian":    {"pain": "kallaway", "hook": "kallaway", "asset": "josh-sanders", "platform": "linkedin-2026-format-arbitrage", "taste": "oren"},
    "recognition":   {"pain": "jasmin-alic", "hook": "jasmin-alic", "asset": "kallaway", "platform": "linkedin-2026-format-arbitrage", "taste": "oren"},
    "educational":   {"pain": "kallaway", "hook": "harry-dry", "asset": "josh-sanders", "platform": "linkedin-2026-format-arbitrage", "taste": "oren"},
    "authority":     {"pain": "caleb-ralston", "hook": "caleb-ralston", "asset": "caleb-ralston", "platform": "linkedin-2026-format-arbitrage", "taste": "oren"},
    "vulnerability": {"pain": "kallaway", "hook": "caleb-ralston", "asset": "kallaway", "platform": "linkedin-2026-format-arbitrage", "taste": "oren"},
}

EXPERT_WORKFLOW_FILES = {
    "kallaway": ["workflows/hook-engineering-matrix.md"],
    "tommy-clark": ["workflows/founder-narrative-extraction-system.md"],
    "jasmin-alic": [],
    "josh-sanders": [],
    "caleb-ralston": [],
    "harry-dry": [],
    "linkedin-2026-format-arbitrage": ["workflows/viral-lead-generation-funnel.md"],
    "lara-acosta": [],
    "oren": [],
}


def generate_mini_brief_work_orders(
    concept: str,
    research_brief: str,
    mode: str = "story-driven",
    platform: str = "linkedin",
    agents_override: Optional[Dict[str, str]] = None,
) -> List[WorkOrder]:
    """Generate specialized work orders for the /mini-brief v2.0 workflow."""
    experts = MINI_BRIEF_EXPERTS.get(mode, MINI_BRIEF_EXPERTS["story-driven"])
    if agents_override:
        experts = {**experts, **agents_override}

    shared_context = f"""## CONCEPT SKELETON
{concept}

## RESEARCH BRIEF
{research_brief}

## TARGET PLATFORM: {platform.upper()}
## CONCEPT MODE: {mode.upper()}
"""

    orders = []

    # WO1: Pain & Truth Agent
    pain_agent = experts["pain"]
    orders.append(WorkOrder(
        agent_name=pain_agent,
        objective=f"Forge Elements 1-4 (Shadow Market Pain, Flawed Belief, Contrarian Truth, Stakes) for this concept.",
        context=shared_context,
        mandate=[
            "Apply the Dopamine Ladder (L1-L2: Stimulation → Captivation) to the Shadow Market Pain",
            "Use Curiosity Loop Engineering to forge the Contrarian Truth",
            "The pain MUST use VERBATIM language from the research brief — not LLM abstractions",
            "The contrarian truth must SHATTER a specific flawed belief identified in research",
            "Apply stakes escalation: emotional AND practical consequences",
            "Output: 4 numbered elements with patterns applied noted",
        ],
        output_schema="mini-brief-elements",
        constraints={"tier": 2, "workflow_files": EXPERT_WORKFLOW_FILES.get(pain_agent, [])},
        batch=0,
    ))

    # WO2: Narrative Hook Agent
    hook_agent = experts["hook"]
    orders.append(WorkOrder(
        agent_name=hook_agent,
        objective=f"Forge Element 5 (Narrative Hook) — produce 3 variations ranked by tension strength.",
        context=shared_context,
        mandate=[
            "Hook must open with a SCENE — a person, a moment, a conversation, a feeling",
            "Must survive the 3-line truncation test (LinkedIn mobile cuts at line 3)",
            "Include a Stealth Hook variant that bypasses AI/ad detection filters",
            "Produce 3 variations: A (highest tension), B (recognition play), C (data/authority)",
            "Each variation must create tension that DEMANDS resolution",
            "Output: 3 hook variations with truncation test results",
        ],
        output_schema="mini-brief-hook",
        constraints={"tier": 2, "workflow_files": EXPERT_WORKFLOW_FILES.get(hook_agent, [])},
        batch=0,
    ))

    # WO3: Asset & Funnel Agent
    asset_agent = experts["asset"]
    orders.append(WorkOrder(
        agent_name=asset_agent,
        objective=f"Forge Element 6 (Recommended Asset) — design a diagnostic/interactive prompt kit.",
        context=shared_context,
        mandate=[
            "Design the asset as a DIAGNOSTIC or INTERACTIVE tool — not a static PDF",
            "The asset must generate saves, not just likes (depth-first monetization)",
            "The reader must be able to EXPERIENCE the concept (diagnose, calculate, mine, score)",
            "Include: asset name, description, keyword CTA, and 3-phase prompt kit outline",
            "Trust test: reader can use this WITHOUT hiring Farrice",
            "Gap test: using the tool naturally reveals a gap that Farrice's service fills",
            "Output: Full asset spec with trust/gap test results",
        ],
        output_schema="mini-brief-asset",
        constraints={"tier": 2, "workflow_files": EXPERT_WORKFLOW_FILES.get(asset_agent, [])},
        batch=0,
    ))

    # WO4: Platform Optimization Agent
    platform_agent = experts["platform"]
    orders.append(WorkOrder(
        agent_name=platform_agent,
        objective=f"Generate Platform Optimization Spec for {platform.upper()}.",
        context=shared_context,
        mandate=[
            "Apply Niche Bending Formula: what format would be novel for this concept?",
            "Apply Commitment Escalation Loop: if carousel, design slide progression",
            "Apply Trapdoor Hook test: ensure hook survives 3-line mobile truncation",
            "Apply Costly Signaling Theory: recommend visual strategy",
            "Apply Comment-to-Download Flywheel: design velocity engineering",
            "Specify: optimal format, character count, posting window, CTA architecture, depth metric targets",
            "Output: Complete platform spec ready to integrate into the brief",
        ],
        output_schema="mini-brief-platform",
        constraints={"tier": 2, "workflow_files": EXPERT_WORKFLOW_FILES.get(platform_agent, [])},
        batch=0,
    ))

    # WO5: Oren Taste Gate (Batch 1 — runs after WO1-4)
    orders.append(WorkOrder(
        agent_name="oren",
        objective="Run the Oren Taste Check on the assembled Mini-Brief elements.",
        context=shared_context + "\n\n## NOTE: You will receive assembled outputs from other agents. Evaluate each element.",
        mandate=[
            "Does this sound like a PREMIUM thought leader or a desperate service provider?",
            "Is the tone 'unbothered authority' — calm, diagnostic, slightly detached?",
            "Would this concept still be valuable if you never mentioned your service?",
            "Check for template slop — generic phrases any coach could sign",
            "Pass/fail EACH element with specific revision notes if fail",
            "Output: Taste verdict table with pass/fail per element",
        ],
        output_schema="mini-brief-taste",
        constraints={"tier": 2, "workflow_files": []},
        depends_on=[pain_agent, hook_agent, asset_agent, platform_agent],
        batch=1,
    ))

    return orders


# --------------------------------------------------------------------------
# Single Agent Execution
# --------------------------------------------------------------------------

async def execute_agent(work_order: WorkOrder, client: GeminiClient,
                        grounded: bool = False) -> AgentResult:
    """Execute a single agent's work order via Gemini API."""
    start_time = time.time()
    agent = work_order.agent_name

    # Check token budget
    if client.total_tokens_used >= TOKEN_BUDGET:
        return AgentResult(
            agent_name=agent, status="skipped", output="",
            tokens_used=0, estimated_cost=0, duration_seconds=0,
            error=f"Token budget exceeded ({client.total_tokens_used}/{TOKEN_BUDGET})"
        )

    print(f"  🚀 Launching {agent}{'  [grounded]' if grounded else ''}...")

    # Load expert context
    tier = work_order.constraints.get("tier", 1)
    extra_files = work_order.constraints.get("workflow_files", None)
    system_instruction = load_agent_context(agent, tier=tier, extra_files=extra_files)

    # Build prompt
    prompt = f"""## WORK ORDER

### OBJECTIVE
{work_order.objective}

### CONTEXT
{work_order.context}

### MANDATE
Before completing, you MUST:
{chr(10).join(f'- {m}' for m in work_order.mandate)}

### OUTPUT FORMAT
Respond with:

**SUMMARY** (2-3 sentences)

**KEY FINDINGS**
- Finding 1
- Finding 2
- Finding 3

**RECOMMENDATIONS**
- Recommendation 1
- Recommendation 2
- Recommendation 3

**CONFIDENCE**: High/Medium/Low

**DISSENT**: Any contrarian views or reservations
"""

    try:
        text, meta = await client.generate(
            prompt,
            system_instruction=system_instruction,
            temperature=0.7,
            max_output_tokens=4096,
            grounding=grounded,
            retries=MAX_RETRIES,
        )

        duration = time.time() - start_time
        print(f"  ✅ {agent} complete ({meta.total_tokens:,} tokens, ${meta.estimated_cost_usd:.4f}, {duration:.1f}s)")

        return AgentResult(
            agent_name=agent, status="success", output=text,
            tokens_used=meta.total_tokens, estimated_cost=meta.estimated_cost_usd,
            duration_seconds=duration, model_used=meta.model,
            thinking_tokens=meta.thinking_tokens,
            grounding_queries=meta.grounding_queries,
        )

    except Exception as e:
        duration = time.time() - start_time
        print(f"  ❌ {agent} failed: {e}")
        return AgentResult(
            agent_name=agent, status="failed", output="",
            tokens_used=0, estimated_cost=0, duration_seconds=duration,
            error=str(e),
        )


# --------------------------------------------------------------------------
# Parallel Execution Engine
# --------------------------------------------------------------------------

async def _execute_swarm_with_orders(objective: str, work_orders: List[WorkOrder],
                                     client: GeminiClient,
                                     plan_only: bool = False,
                                     grounded: bool = False) -> SwarmResult:
    """Execute a swarm with pre-built work orders (used by mini-brief mode)."""
    agents = [wo.agent_name for wo in work_orders]
    start_time = time.time()

    print(f"\n{'='*60}")
    print(f"🐝 SWARM COMMANDER — Mini-Brief Production Engine")
    print(f"{'='*60}")
    print(f"📋 Objective: {objective[:100]}...")
    print(f"👥 Agents: {', '.join(dict.fromkeys(agents))}")
    print(f"🔧 Model: {client.default_model}")
    print(f"🛡️  Safety: max {MAX_RETRIES} retries, {TOKEN_BUDGET:,} token budget")
    if grounded:
        print(f"🌐 Grounding: ENABLED (agents will search the web)")
    print(f"{'='*60}\n")

    if plan_only:
        print("\n📝 Plan-only mode. Work orders generated but not executed.")
        plan_text = "\n\n".join(
            f"### {wo.agent_name} (Batch {wo.batch})\n**Objective:** {wo.objective}\n**Mandate:** {', '.join(wo.mandate[:2])}..."
            for wo in work_orders
        )
        return SwarmResult(
            objective=objective, agent_results=[], synthesis=plan_text,
            total_tokens=0, total_duration=0, total_cost_usd=0,
        )

    # Group by batch
    batches: Dict[int, List[WorkOrder]] = {}
    for wo in work_orders:
        batches.setdefault(wo.batch, []).append(wo)

    all_results: List[AgentResult] = []

    for batch_num in sorted(batches.keys()):
        batch = batches[batch_num]
        batch_agents = [wo.agent_name for wo in batch]
        print(f"\n⚡ BATCH {batch_num + 1}: Launching {len(batch)} agents in PARALLEL")
        print(f"   Agents: {', '.join(batch_agents)}")

        # For Batch 1+ (Oren), inject assembled outputs from previous batches
        if batch_num > 0 and all_results:
            assembled = "\n\n---\n\n".join(
                f"## {r.agent_name} Output:\n{r.output}"
                for r in all_results if r.status == "success"
            )
            for wo in batch:
                wo.context += f"\n\n## ASSEMBLED OUTPUTS FROM PREVIOUS AGENTS\n{assembled}"

        tasks = [execute_agent(wo, client, grounded=grounded) for wo in batch]
        results = await asyncio.gather(*tasks)
        all_results.extend(results)

        successful = sum(1 for r in results if r.status == "success")
        print(f"\n   ✅ Batch {batch_num + 1} complete: {successful}/{len(batch)} succeeded")

    # Synthesis
    print(f"\n{'='*60}")
    print(f"🧬 ASSEMBLING Mini-Brief from {len(all_results)} agent outputs...")
    print(f"{'='*60}\n")

    synthesis = await synthesize_results(objective, all_results, client, grounded=grounded)

    total_duration = time.time() - start_time
    usage = client.usage_summary()

    save_outputs(objective, all_results, synthesis, usage, total_duration, client.default_model)

    print(f"\n{'='*60}")
    print(f"🎯 MINI-BRIEF SWARM COMPLETE")
    print(f"{'='*60}")
    print(f"⏱️  Duration:   {total_duration:.1f}s")
    print(f"📊 Tokens:     {usage['total_tokens']:,}")
    print(f"💰 Est. Cost:  ${usage['total_cost_usd']:.4f}")
    print(f"📂 Output:     {OUTPUT_DIR / 'latest'}")
    print(f"{'='*60}\n")

    return SwarmResult(
        objective=objective, agent_results=all_results, synthesis=synthesis,
        total_tokens=usage["total_tokens"], total_duration=total_duration,
        total_cost_usd=usage["total_cost_usd"],
    )


async def execute_swarm(objective: str, agents: List[str], client: GeminiClient,
                        plan_only: bool = False, grounded: bool = False,
                        research_brief: str = "") -> SwarmResult:
    """Execute a full swarm: generate work orders, run agents in parallel, synthesize."""
    start_time = time.time()

    print(f"\n{'='*60}")
    print(f"🐝 SWARM COMMANDER — Parallel Orchestration Engine")
    print(f"{'='*60}")
    print(f"📋 Objective: {objective}")
    print(f"👥 Agents: {', '.join(agents)}")
    print(f"🔧 Model: {client.default_model}")
    print(f"🛡️  Safety: max {MAX_RETRIES} retries, {TOKEN_BUDGET:,} token budget")
    if grounded:
        print(f"🌐 Grounding: ENABLED (agents will search the web)")
    if research_brief:
        print(f"🔬 Research: PRE-RESEARCH INJECTED (Perplexity)")
    print(f"{'='*60}\n")

    work_orders = generate_work_orders(objective, agents, research_brief=research_brief)

    if plan_only:
        print("\n📝 Plan-only mode. Work orders generated but not executed.")
        plan_text = "\n\n".join(
            f"### {wo.agent_name}\n**Objective:** {wo.objective}\n**Mandate:** {', '.join(wo.mandate)}"
            for wo in work_orders
        )
        return SwarmResult(
            objective=objective, agent_results=[], synthesis=plan_text,
            total_tokens=0, total_duration=0, total_cost_usd=0,
        )

    # Group by batch
    batches: Dict[int, List[WorkOrder]] = {}
    for wo in work_orders:
        batches.setdefault(wo.batch, []).append(wo)

    all_results: List[AgentResult] = []

    for batch_num in sorted(batches.keys()):
        batch = batches[batch_num]
        batch_agents = [wo.agent_name for wo in batch]
        print(f"\n⚡ BATCH {batch_num + 1}: Launching {len(batch)} agents in PARALLEL")
        print(f"   Agents: {', '.join(batch_agents)}")

        tasks = [execute_agent(wo, client, grounded=grounded) for wo in batch]
        results = await asyncio.gather(*tasks)
        all_results.extend(results)

        successful = sum(1 for r in results if r.status == "success")
        print(f"\n   ✅ Batch {batch_num + 1} complete: {successful}/{len(batch)} succeeded")

    # Synthesis
    print(f"\n{'='*60}")
    print(f"🧬 SYNTHESIZING {len(all_results)} agent outputs...")
    print(f"{'='*60}\n")

    synthesis = await synthesize_results(objective, all_results, client, grounded=grounded)

    total_duration = time.time() - start_time
    usage = client.usage_summary()

    save_outputs(objective, all_results, synthesis, usage, total_duration, client.default_model)

    print(f"\n{'='*60}")
    print(f"🎯 SWARM COMPLETE")
    print(f"{'='*60}")
    print(f"⏱️  Duration:   {total_duration:.1f}s")
    print(f"📊 Tokens:     {usage['total_tokens']:,}")
    print(f"💰 Est. Cost:  ${usage['total_cost_usd']:.4f}")
    print(f"📂 Output:     {OUTPUT_DIR / 'latest'}")
    print(f"{'='*60}\n")

    return SwarmResult(
        objective=objective, agent_results=all_results, synthesis=synthesis,
        total_tokens=usage["total_tokens"], total_duration=total_duration,
        total_cost_usd=usage["total_cost_usd"],
    )


# --------------------------------------------------------------------------
# Synthesis
# --------------------------------------------------------------------------

async def synthesize_results(objective: str, results: List[AgentResult],
                             client: GeminiClient, grounded: bool = False) -> str:
    """Synthesize all agent outputs into a unified deliverable."""
    successful = [r for r in results if r.status == "success"]

    if not successful:
        return "❌ No agents completed successfully. Cannot synthesize."

    agent_outputs = "\n\n---\n\n".join(
        f"## {r.agent_name} (Confidence: inferred from output)\n\n{r.output}"
        for r in successful
    )

    prompt = f"""## SYNTHESIS TASK

You are the Swarm Synthesizer. You have received outputs from {len(successful)} expert agents
working on the following objective:

**OBJECTIVE:** {objective}

Below are their individual outputs. Your job is to:
1. Identify AGREEMENTS (where agents converge)
2. Identify CONFLICTS (where agents disagree)
3. Preserve MINORITY POSITIONS (dissenting views that deserve consideration)
4. Produce a UNIFIED RECOMMENDATION with confidence rating

## AGENT OUTPUTS

{agent_outputs}

## OUTPUT FORMAT

# Swarm Synthesis: {objective}

## Executive Summary
[3-5 sentences]

## Unanimous Agreements
| Finding | Supporting Agents |
|---------|------------------|
| ... | ... |

## Key Recommendations
| Recommendation | Confidence | Lead Agent |
|----------------|------------|------------|
| ... | ... | ... |

## Conflicts & Minority Report
[Any disagreements + conditions where minority views may be correct]

## Next Steps
1. [Immediate action]
2. [Follow-up action]
3. [Decision point requiring human input]

## Provenance
| Section | Primary Contributors |
|---------|---------------------|
| ... | ... |
"""

    system = (
        "You are a master synthesizer. Your job is to merge multiple expert perspectives "
        "into actionable intelligence. Preserve attribution. Highlight disagreements honestly. "
        "Be concise and specific."
    )

    try:
        text, meta = await client.generate(
            prompt,
            system_instruction=system,
            model="pro",
            thinking_budget=2048,
            grounding=grounded,
        )

        # Challenge round: pressure-test conflicts when 2+ agents contributed
        if len(successful) >= 2:
            challenge = await run_challenge_round(
                text, successful, objective, client
            )
            if challenge:
                text += f"\n\n---\n\n{challenge}"

        return text
    except Exception as e:
        return f"❌ Synthesis failed: {e}\n\nRaw agent outputs preserved in individual files."


# --------------------------------------------------------------------------
# Challenge Round (Adversarial Synthesis)
# --------------------------------------------------------------------------

async def run_challenge_round(initial_synthesis: str, results: List[AgentResult],
                              objective: str, client: GeminiClient) -> str:
    """Run a targeted debate resolution. One additional API call."""
    if client.total_tokens_used >= TOKEN_BUDGET:
        print("  ⚠️  Skipping challenge round — token budget exhausted")
        return ""

    print("  🔥 Running challenge round...")

    agent_positions = "\n\n".join(
        f"**{r.agent_name}**:\n{r.output[:800]}"
        for r in results
    )

    prompt = f"""## CHALLENGE ROUND — Conflict Resolution

You are the Swarm Arbiter. You've received an initial synthesis from {len(results)} expert agents.

**OBJECTIVE:** {objective}

**INITIAL SYNTHESIS:**
{initial_synthesis}

**ORIGINAL AGENT POSITIONS (truncated):**
{agent_positions}

## YOUR TASK

1. **Identify the top 2-3 MEANINGFUL conflicts** — places where agents genuinely disagree on approach, priority, or conclusion. Ignore surface-level wording differences.

2. **For each conflict**, present:
   - The competing positions (which agents hold which view)
   - The strongest argument FOR each side
   - Your **VERDICT**: Which position is stronger and WHY, or why both are valid in different contexts

3. If there are NO meaningful conflicts (agents largely agree), say so clearly and skip to Strengthened Conclusions.

## OUTPUT FORMAT

# Challenge Round Results

## Conflicts Identified: [N]

### Conflict 1: [Topic]
- **Position A** ([Agent(s)]): [Their argument]
- **Position B** ([Agent(s)]): [Their argument]
- **Verdict**: [Resolution with reasoning]

### Conflict 2: [Topic]
[Same format]

## Strengthened Conclusions
[2-3 sentences on what the challenge round confirmed, changed, or nuanced]

## Revised Confidence
[Did the challenge round increase or decrease overall confidence? Why?]
"""

    system = (
        "You are a debate arbiter. Find genuine disagreements between experts, "
        "pressure-test both sides, and deliver clear verdicts. Be direct. "
        "Don't manufacture conflicts that don't exist, but don't paper over real ones either."
    )

    try:
        text, meta = await client.generate(prompt, system_instruction=system, model="pro")
        print(f"  🔥 Challenge round complete ({meta.total_tokens:,} tokens)")
        return text
    except Exception as e:
        print(f"  ⚠️  Challenge round failed (non-critical): {e}")
        return ""


# --------------------------------------------------------------------------
# File Output
# --------------------------------------------------------------------------

def save_outputs(objective: str, results: List[AgentResult], synthesis: str,
                 usage: dict, duration: float, model: str):
    """Save all outputs to the swarm_outputs directory."""
    import shutil
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    run_dir = OUTPUT_DIR / timestamp
    agents_dir = run_dir / "agent_outputs"
    agents_dir.mkdir(parents=True, exist_ok=True)

    latest = OUTPUT_DIR / "latest"
    if latest.is_symlink():
        latest.unlink()
    elif latest.exists():
        shutil.rmtree(latest)
    latest.symlink_to(run_dir)

    for result in results:
        agent_file = agents_dir / f"{result.agent_name}.md"
        status_emoji = "✅" if result.status == "success" else "❌"
        content = f"""# {result.agent_name} {status_emoji}

**Status:** {result.status}
**Model:** {result.model_used}
**Tokens:** {result.tokens_used:,}
**Cost:** ${result.estimated_cost:.4f}
**Duration:** {result.duration_seconds:.1f}s
**Thinking Tokens:** {result.thinking_tokens:,}
**Grounding Queries:** {result.grounding_queries}
"""
        if result.error:
            content += f"**Error:** {result.error}\n"
        if result.output:
            content += f"\n---\n\n{result.output}\n"
        agent_file.write_text(content)

    (run_dir / "synthesis.md").write_text(synthesis)

    metadata = {
        "objective": objective,
        "timestamp": timestamp,
        "model": model,
        "total_tokens": usage["total_tokens"],
        "total_cost_usd": usage["total_cost_usd"],
        "duration_seconds": round(duration, 1),
        "api_calls": usage["api_calls"],
        "agents": [
            {
                "name": r.agent_name,
                "status": r.status,
                "model": r.model_used,
                "tokens": r.tokens_used,
                "cost": r.estimated_cost,
                "duration": round(r.duration_seconds, 1),
                "thinking_tokens": r.thinking_tokens,
                "grounding_queries": r.grounding_queries,
                "error": r.error,
            }
            for r in results
        ]
    }
    (run_dir / "metadata.json").write_text(json.dumps(metadata, indent=2))


# --------------------------------------------------------------------------
# Pre-Research Phase (Perplexity)
# --------------------------------------------------------------------------

def run_pre_research(objective: str, agents: List[str]) -> str:
    """
    Run Perplexity pre-research phase before firing the Gemini swarm.

    Generates 2-3 collapsed queries from the objective, runs them through
    Perplexity Sonar, and returns a formatted research brief that gets
    injected into each agent's context.
    """
    try:
        pplx = PerplexityClient()
    except ValueError as e:
        print(f"  ⚠️  Perplexity unavailable: {e}")
        print(f"  ⚠️  Falling back to swarm without pre-research.")
        return ""

    remaining = pplx.budget_remaining()
    print(f"\n🔬 PRE-RESEARCH PHASE (Perplexity)")
    print(f"   Budget remaining: ${remaining:.2f}")

    if remaining < 0.50:
        print(f"  ⚠️  Budget too low for pre-research. Skipping.")
        return ""

    # Use sonar-pro for richer research, downgrade if budget is tight
    model = "sonar-pro" if remaining >= 2.00 else "sonar"

    # Build collapsed queries (The Collapsing Rule from the policy)
    queries = [
        f"Analyze the current state of: {objective}. "
        f"Include: key trends, major players, market data, recent developments (2025-2026). "
        f"Cite specific sources.",
        f"What are the contrarian views, criticisms, and failure cases related to: {objective}? "
        f"Include Reddit/forum sentiment where available.",
    ]

    print(f"   Model: {model}")
    print(f"   Queries: {len(queries)}")

    brief_parts = []
    total_cost = 0

    for i, query in enumerate(queries, 1):
        print(f"   📡 Query {i}/{len(queries)}...")
        try:
            result = pplx.search(
                query,
                model=model,
                task_context=f"swarm-research: {objective[:80]}",
                query_type="research",
                search_recency_filter="month",
            )
            total_cost += result.estimated_cost
            if result.text:
                citations = ""
                if result.citations:
                    citations = "\n**Sources:** " + ", ".join(
                        f"[{i+1}]({url})" if url.startswith("http") else f"[{i+1}] {url}"
                        for i, url in enumerate(result.citations[:5])
                    )
                brief_parts.append(f"### Research Finding {i}\n{result.text}{citations}")
                print(f"   ✅ Query {i} complete (${result.estimated_cost:.2f}, {result.duration_seconds:.1f}s)")
            else:
                print(f"   ⚠️  Query {i} returned empty")
        except BudgetExhaustedError:
            print(f"   ⚠️  Budget exhausted during pre-research. Using partial results.")
            break
        except Exception as e:
            print(f"   ❌ Query {i} failed: {e}")

    if not brief_parts:
        return ""

    usage = pplx.usage_summary()
    print(f"\n   📊 Pre-research complete: {usage['session_queries']} queries, ${total_cost:.2f}")
    print(f"   💰 Budget remaining: ${usage['budget_remaining']:.2f}")

    research_brief = (
        f"## PRE-RESEARCH BRIEF (Perplexity — {model})\n\n"
        f"The following real-world data was gathered BEFORE your analysis. "
        f"Ground your response in these findings. Do NOT speculate when data exists.\n\n"
        + "\n\n".join(brief_parts)
    )

    return research_brief


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Parallel Swarm Orchestrator — True parallel agent execution",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python parallel_swarm.py "Analyze competitors in AI consulting"
  python parallel_swarm.py --agents "cardinal-mason,harry-dry" "Write 5 hooks"
  python parallel_swarm.py --grounded "Research current market trends in AI consulting"
  python parallel_swarm.py --research "Deep competitive intelligence on AI consulting"
  python parallel_swarm.py --plan-only "Design a LinkedIn strategy"
  python parallel_swarm.py --max-agents 8 "Full product launch analysis"
        """
    )
    parser.add_argument("objective", help="The task/objective for the swarm")
    parser.add_argument("--agents", help="Comma-separated agent names (auto-selects if omitted)")
    parser.add_argument("--max-agents", type=int, default=5, help="Max agents for auto-selection (default: 5)")
    parser.add_argument("--plan-only", action="store_true", help="Show plan without executing")
    parser.add_argument("--grounded", action="store_true",
                        help="Enable Google Search grounding — agents search the web for real-time data")
    parser.add_argument("--research", action="store_true",
                        help="Run Perplexity pre-research phase — grounds agents in cited real-world data")
    parser.add_argument("--mode", choices=["default", "mini-brief"], default="default",
                        help="Swarm mode: 'default' for generic, 'mini-brief' for 7-element brief production")
    parser.add_argument("--concept-mode", default="story-driven",
                        choices=["story-driven", "contrarian", "recognition", "educational", "authority", "vulnerability"],
                        help="Concept mode for mini-brief (default: story-driven)")
    parser.add_argument("--platform", default="linkedin",
                        choices=["linkedin", "youtube", "substack"],
                        help="Target platform for mini-brief (default: linkedin)")
    parser.add_argument("--context", help="Path to research brief or context file to include")

    args = parser.parse_args()

    client = GeminiClient()

    # Pre-research phase (Perplexity) — runs before the swarm if --research is set
    research_brief = ""
    if args.research and not args.plan_only:
        research_brief = run_pre_research(args.objective, [])

    # Mini-brief mode
    if args.mode == "mini-brief":
        ctx_brief = research_brief
        if args.context:
            ctx_path = Path(args.context)
            if ctx_path.exists():
                ctx_brief += "\n\n" + ctx_path.read_text()
                print(f"\n📄 Loaded research brief from {args.context}")
            else:
                print(f"⚠️  Context file not found: {args.context}")

        work_orders = generate_mini_brief_work_orders(
            concept=args.objective, research_brief=ctx_brief,
            mode=args.concept_mode, platform=args.platform,
        )
        agents = [wo.agent_name for wo in work_orders]
        print(f"\n🎯 Mini-Brief Mode: {args.concept_mode} | Platform: {args.platform}")
        print(f"👥 Expert constellation: {', '.join(dict.fromkeys(agents))}")

        result = asyncio.run(
            _execute_swarm_with_orders(args.objective, work_orders, client,
                                       plan_only=args.plan_only, grounded=args.grounded)
        )
    else:
        # Default mode
        if args.agents:
            agents = [a.strip() for a in args.agents.split(",")]
            for a in agents:
                if a not in EXPERT_DOMAINS:
                    print(f"⚠️  Unknown agent: {a} (will use fallback context)")
        else:
            agents = auto_select_agents(args.objective, args.max_agents)
            print(f"\n🤖 Auto-selected agents: {', '.join(agents)}")

        # Inject research brief into work orders if pre-research was run
        result = asyncio.run(
            execute_swarm(args.objective, agents, client,
                         plan_only=args.plan_only, grounded=args.grounded,
                         research_brief=research_brief)
        )


if __name__ == "__main__":
    main()
