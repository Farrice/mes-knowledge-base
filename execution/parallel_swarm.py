#!/usr/bin/env python3
"""
Parallel Swarm Orchestrator — True parallel agent execution for Antigravity.

Fires multiple Gemini API calls concurrently using asyncio, with safety rails
to prevent loop disasters and token budget overruns.

Usage:
    python parallel_swarm.py "Analyze the top 3 competitors in AI consulting"
    python parallel_swarm.py --plan-only "Design a content strategy for LinkedIn"
    python parallel_swarm.py --config swarm_config.json
    python parallel_swarm.py --agents "cardinal-mason,harry-dry,seena-rez" "Write 5 hook variations"
"""

import asyncio
import json
import os
import sys
import time
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

BASE_PATH = Path(__file__).parent.parent
AGENTS_PATH = BASE_PATH / "agents"
SKILLS_PATH = BASE_PATH / "skills"
DOMAIN_REGISTRY = BASE_PATH / "DOMAIN_REGISTRY.md"
OUTPUT_DIR = BASE_PATH / "swarm_outputs"

# Load .env
ENV_PATH = BASE_PATH / ".env"
if ENV_PATH.exists():
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())

API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL = os.environ.get("GEMINI_MODEL", "gemini-3-flash-preview")
MAX_RETRIES = int(os.environ.get("SWARM_MAX_RETRIES", "1"))
TOKEN_BUDGET = int(os.environ.get("SWARM_TOKEN_BUDGET", "500000"))
MAX_PARALLEL = int(os.environ.get("SWARM_MAX_PARALLEL", "10"))

from google import genai
from google.genai import types


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
    duration_seconds: float
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
# Expert Registry (lightweight — full details read from agent files)
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
# API Client
# --------------------------------------------------------------------------

async def call_gemini(prompt: str, system_instruction: str = "", 
                      retries: int = MAX_RETRIES) -> Tuple[str, int]:
    """Make a single Gemini API call via async SDK. Returns (response_text, tokens_used)."""
    client = genai.Client(api_key=API_KEY)
    
    config = types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=4096,
    )
    if system_instruction:
        config.system_instruction = system_instruction
        
    for attempt in range(retries + 1):
        try:
            response = await client.aio.models.generate_content(
                model=MODEL,
                contents=prompt,
                config=config
            )
            # Extract token usage if available; otherwise use 0
            tokens = 0
            if response.usage_metadata:
                tokens = response.usage_metadata.total_token_count
            return response.text, tokens

        except Exception as e:
            if attempt < retries:
                wait = 2 ** attempt
                print(f"  ⚠️  Retry {attempt + 1}/{retries} for API call (waiting {wait}s): {e}")
                await asyncio.sleep(wait)
            else:
                raise


# --------------------------------------------------------------------------
# Agent Context Loading
# --------------------------------------------------------------------------

def load_agent_context(agent_name: str, tier: int = 1,
                       extra_files: Optional[List[str]] = None) -> str:
    """
    Load expert context at the specified tier level.

    Tier 1 (default): AGENT.md + SKILL.md (~1,350 tokens)
    Tier 2: AGENT.md + SKILL.md + genius.md + specified workflow files (~2,550 tokens)

    extra_files: Additional file paths (relative to skill dir) to load at Tier 2.
    """
    agent_dir = AGENTS_PATH / agent_name

    context_parts = []

    # Agent persona
    agent_file = agent_dir / "AGENT.md"
    if agent_file.exists():
        content = agent_file.read_text()
        context_parts.append(content)

    # Find matching skill directory
    matched_skill_dir = None
    for skill_name in SKILLS_PATH.iterdir():
        if agent_name in skill_name.name:
            matched_skill_dir = skill_name
            break

    if matched_skill_dir:
        # Tier 1+: Always load SKILL.md
        skill_file = matched_skill_dir / "SKILL.md"
        if skill_file.exists():
            context_parts.append(skill_file.read_text())

        # Tier 2: Also load genius.md + specified workflow files
        if tier >= 2:
            genius_file = matched_skill_dir / "genius.md"
            if genius_file.exists():
                context_parts.append(genius_file.read_text())

            # Load extra workflow/prompt files if specified
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
    """
    Simple keyword-based agent selection. For more sophisticated selection,
    use the swarm-planning prompt with a planning LLM call.
    """
    objective_lower = objective.lower()

    scores = {}
    for agent, domain in EXPERT_DOMAINS.items():
        score = 0
        for keyword in domain.lower().split(", "):
            if keyword in objective_lower:
                score += 2
            # Partial match
            for word in keyword.split():
                if word in objective_lower:
                    score += 1
        if score > 0:
            scores[agent] = score

    # Sort by score descending
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    selected = [agent for agent, _ in ranked[:max_agents]]

    # Always include at least 2 agents
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

def generate_work_orders(objective: str, agents: List[str]) -> List[WorkOrder]:
    """Generate work orders for each agent. All are parallel (batch 0) by default."""
    orders = []
    for agent in agents:
        domain = EXPERT_DOMAINS.get(agent, "general")
        orders.append(WorkOrder(
            agent_name=agent,
            objective=objective,
            context=f"You are contributing to a multi-expert analysis. Your domain: {domain}.",
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

# Default expert assignments per concept mode (maps to the workflow matrix)
MINI_BRIEF_EXPERTS = {
    "story-driven":  {"pain": "kallaway", "hook": "tommy-clark", "asset": "josh-sanders", "platform": "linkedin-2026-format-arbitrage", "taste": "oren"},
    "contrarian":    {"pain": "kallaway", "hook": "kallaway", "asset": "josh-sanders", "platform": "linkedin-2026-format-arbitrage", "taste": "oren"},
    "recognition":   {"pain": "jasmin-alic", "hook": "jasmin-alic", "asset": "kallaway", "platform": "linkedin-2026-format-arbitrage", "taste": "oren"},
    "educational":   {"pain": "kallaway", "hook": "harry-dry", "asset": "josh-sanders", "platform": "linkedin-2026-format-arbitrage", "taste": "oren"},
    "authority":     {"pain": "caleb-ralston", "hook": "caleb-ralston", "asset": "caleb-ralston", "platform": "linkedin-2026-format-arbitrage", "taste": "oren"},
    "vulnerability": {"pain": "kallaway", "hook": "caleb-ralston", "asset": "kallaway", "platform": "linkedin-2026-format-arbitrage", "taste": "oren"},
}

# Tier 2 workflow files per expert (relative to skill dir)
EXPERT_WORKFLOW_FILES = {
    "kallaway": ["workflows/hook-engineering-matrix.md"],
    "tommy-clark": ["workflows/founder-narrative-extraction-system.md"],
    "jasmin-alic": [],  # genius.md covers core patterns
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
    """
    Generate specialized work orders for the /mini-brief v2.0 workflow.

    Produces 5 work orders:
      Batch 0 (parallel): WO1-Pain&Truth, WO2-Hook, WO3-Asset, WO4-Platform
      Batch 1 (sequential): WO5-TasteGate (Oren)

    Args:
        concept: The concept skeleton from Phase 2
        research_brief: The research brief from Phase 1
        mode: Concept mode (story-driven, contrarian, recognition, educational, authority, vulnerability)
        platform: Target platform (linkedin, youtube, substack)
        agents_override: Optional dict to override default expert assignments
    """
    # Select experts based on mode
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
        constraints={
            "tier": 2,
            "workflow_files": EXPERT_WORKFLOW_FILES.get(pain_agent, []),
        },
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
        constraints={
            "tier": 2,
            "workflow_files": EXPERT_WORKFLOW_FILES.get(hook_agent, []),
        },
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
        constraints={
            "tier": 2,
            "workflow_files": EXPERT_WORKFLOW_FILES.get(asset_agent, []),
        },
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
        constraints={
            "tier": 2,
            "workflow_files": EXPERT_WORKFLOW_FILES.get(platform_agent, []),
        },
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
        constraints={
            "tier": 2,
            "workflow_files": [],
        },
        depends_on=[pain_agent, hook_agent, asset_agent, platform_agent],
        batch=1,
    ))

    return orders


# --------------------------------------------------------------------------
# Single Agent Execution
# --------------------------------------------------------------------------

async def execute_agent(work_order: WorkOrder, token_tracker: dict) -> AgentResult:
    """Execute a single agent's work order via Gemini API."""
    start_time = time.time()
    agent = work_order.agent_name

    # Check token budget
    if token_tracker["used"] >= TOKEN_BUDGET:
        return AgentResult(
            agent_name=agent,
            status="skipped",
            output="",
            tokens_used=0,
            duration_seconds=0,
            error=f"Token budget exceeded ({token_tracker['used']}/{TOKEN_BUDGET})"
        )

    print(f"  🚀 Launching {agent}...")

    # Load expert context (Tier 2 if specified in work order constraints)
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
        response, tokens = await call_gemini(prompt, system_instruction)
        token_tracker["used"] += tokens

        duration = time.time() - start_time
        print(f"  ✅ {agent} complete ({tokens:,} tokens, {duration:.1f}s)")

        return AgentResult(
            agent_name=agent,
            status="success",
            output=response,
            tokens_used=tokens,
            duration_seconds=duration,
        )

    except Exception as e:
        duration = time.time() - start_time
        print(f"  ❌ {agent} failed: {e}")

        return AgentResult(
            agent_name=agent,
            status="failed",
            output="",
            tokens_used=0,
            duration_seconds=duration,
            error=str(e),
        )


# --------------------------------------------------------------------------
# Parallel Execution Engine
# --------------------------------------------------------------------------

async def _execute_swarm_with_orders(objective: str, work_orders: List[WorkOrder],
                                     plan_only: bool = False) -> SwarmResult:
    """Execute a swarm with pre-built work orders (used by mini-brief mode)."""
    agents = [wo.agent_name for wo in work_orders]
    start_time = time.time()
    token_tracker = {"used": 0}

    print(f"\n{'='*60}")
    print(f"🐝 SWARM COMMANDER — Mini-Brief Production Engine")
    print(f"{'='*60}")
    print(f"📋 Objective: {objective[:100]}...")
    print(f"👥 Agents: {', '.join(dict.fromkeys(agents))}")
    print(f"🔧 Model: {MODEL}")
    print(f"🛡️  Safety: max {MAX_RETRIES} retries, {TOKEN_BUDGET:,} token budget")
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

        tasks = [execute_agent(wo, token_tracker) for wo in batch]
        results = await asyncio.gather(*tasks)
        all_results.extend(results)

        successful = sum(1 for r in results if r.status == "success")
        print(f"\n   ✅ Batch {batch_num + 1} complete: {successful}/{len(batch)} succeeded")

    # Synthesis (mini-brief assembly)
    print(f"\n{'='*60}")
    print(f"🧬 ASSEMBLING Mini-Brief from {len(all_results)} agent outputs...")
    print(f"{'='*60}\n")

    synthesis = await synthesize_results(objective, all_results, token_tracker)

    total_duration = time.time() - start_time
    total_tokens = token_tracker["used"]
    cost_per_million = 0.10
    total_cost = (total_tokens / 1_000_000) * cost_per_million

    save_outputs(objective, all_results, synthesis, total_tokens, total_duration, total_cost)

    print(f"\n{'='*60}")
    print(f"🎯 MINI-BRIEF SWARM COMPLETE")
    print(f"{'='*60}")
    print(f"⏱️  Duration:   {total_duration:.1f}s")
    print(f"📊 Tokens:     {total_tokens:,}")
    print(f"💰 Est. Cost:  ${total_cost:.4f}")
    print(f"📂 Output:     {OUTPUT_DIR / 'latest'}")
    print(f"{'='*60}\n")

    return SwarmResult(
        objective=objective, agent_results=all_results, synthesis=synthesis,
        total_tokens=total_tokens, total_duration=total_duration, total_cost_usd=total_cost,
    )


async def execute_swarm(objective: str, agents: List[str],
                        plan_only: bool = False) -> SwarmResult:
    """
    Execute a full swarm: generate work orders, run agents in parallel,
    synthesize results.
    """
    start_time = time.time()
    token_tracker = {"used": 0}

    print(f"\n{'='*60}")
    print(f"🐝 SWARM COMMANDER — Parallel Orchestration Engine")
    print(f"{'='*60}")
    print(f"📋 Objective: {objective}")
    print(f"👥 Agents: {', '.join(agents)}")
    print(f"🔧 Model: {MODEL}")
    print(f"🛡️  Safety: max {MAX_RETRIES} retries, {TOKEN_BUDGET:,} token budget")
    print(f"{'='*60}\n")

    # Generate work orders
    work_orders = generate_work_orders(objective, agents)

    if plan_only:
        print("\n📝 Plan-only mode. Work orders generated but not executed.")
        plan_text = "\n\n".join(
            f"### {wo.agent_name}\n**Objective:** {wo.objective}\n**Mandate:** {', '.join(wo.mandate)}"
            for wo in work_orders
        )
        return SwarmResult(
            objective=objective,
            agent_results=[],
            synthesis=plan_text,
            total_tokens=0,
            total_duration=0,
            total_cost_usd=0,
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

        # TRUE PARALLEL EXECUTION — all agents fire simultaneously
        tasks = [execute_agent(wo, token_tracker) for wo in batch]
        results = await asyncio.gather(*tasks)
        all_results.extend(results)

        successful = sum(1 for r in results if r.status == "success")
        print(f"\n   ✅ Batch {batch_num + 1} complete: {successful}/{len(batch)} succeeded")

    # Synthesis
    print(f"\n{'='*60}")
    print(f"🧬 SYNTHESIZING {len(all_results)} agent outputs...")
    print(f"{'='*60}\n")

    synthesis = await synthesize_results(objective, all_results, token_tracker)

    total_duration = time.time() - start_time
    total_tokens = token_tracker["used"]

    # Estimate cost (Gemini 3 Flash pricing)
    cost_per_million = 0.10  # $0.10/M for input on gemini-3-flash
    total_cost = (total_tokens / 1_000_000) * cost_per_million

    # Save outputs
    save_outputs(objective, all_results, synthesis, total_tokens, total_duration, total_cost)

    print(f"\n{'='*60}")
    print(f"🎯 SWARM COMPLETE")
    print(f"{'='*60}")
    print(f"⏱️  Duration:   {total_duration:.1f}s")
    print(f"📊 Tokens:     {total_tokens:,}")
    print(f"💰 Est. Cost:  ${total_cost:.4f}")
    print(f"📂 Output:     {OUTPUT_DIR / 'latest'}")
    print(f"{'='*60}\n")

    return SwarmResult(
        objective=objective,
        agent_results=all_results,
        synthesis=synthesis,
        total_tokens=total_tokens,
        total_duration=total_duration,
        total_cost_usd=total_cost,
    )


# --------------------------------------------------------------------------
# Synthesis
# --------------------------------------------------------------------------

async def synthesize_results(objective: str, results: List[AgentResult],
                             token_tracker: dict) -> str:
    """Synthesize all agent outputs into a unified deliverable."""
    successful = [r for r in results if r.status == "success"]

    if not successful:
        return "❌ No agents completed successfully. Cannot synthesize."

    # Build synthesis prompt
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
        response, tokens = await call_gemini(prompt, system)
        token_tracker["used"] += tokens

        # Challenge round: pressure-test conflicts when 2+ agents contributed
        if len(successful) >= 2:
            challenge = await run_challenge_round(
                response, successful, objective, token_tracker
            )
            if challenge:
                response += f"\n\n---\n\n{challenge}"

        return response
    except Exception as e:
        return f"❌ Synthesis failed: {e}\n\nRaw agent outputs preserved in individual files."


# --------------------------------------------------------------------------
# Challenge Round (Adversarial Synthesis)
# --------------------------------------------------------------------------

async def run_challenge_round(initial_synthesis: str, results: List[AgentResult],
                              objective: str, token_tracker: dict) -> str:
    """
    Identify conflicts from the initial synthesis and run a targeted debate
    resolution. One additional API call — not one per conflict.

    Returns challenge round text to append, or empty string if no meaningful
    conflicts or budget is exhausted.
    """
    if token_tracker["used"] >= TOKEN_BUDGET:
        print("  ⚠️  Skipping challenge round — token budget exhausted")
        return ""

    print("  🔥 Running challenge round...")

    # Truncate each agent's output to keep the challenge call lean
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
        response, tokens = await call_gemini(prompt, system)
        token_tracker["used"] += tokens
        print(f"  🔥 Challenge round complete ({tokens:,} tokens)")
        return response
    except Exception as e:
        print(f"  ⚠️  Challenge round failed (non-critical): {e}")
        return ""


# --------------------------------------------------------------------------
# AUTO-REFINEMENT (future scaling hook)
# --------------------------------------------------------------------------
# TODO: When high-volume client work requires automated quality control,
# implement an auto-refinement loop here:
#   1. Run synthesis through a validation prompt that scores output quality
#   2. If score < threshold, identify the weakest agent output
#   3. Re-run ONLY that agent with feedback from the validator
#   4. Re-synthesize with the improved output
# This avoids re-running the entire swarm for one weak link.
# See: ESOS analysis in implementation_plan.md for design rationale.
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# File Output
# --------------------------------------------------------------------------

def save_outputs(objective: str, results: List[AgentResult], synthesis: str,
                 total_tokens: int, duration: float, cost: float):
    """Save all outputs to the swarm_outputs directory."""
    # Create timestamped directory
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    run_dir = OUTPUT_DIR / timestamp
    agents_dir = run_dir / "agent_outputs"
    agents_dir.mkdir(parents=True, exist_ok=True)

    # Also maintain a "latest" symlink
    latest = OUTPUT_DIR / "latest"
    if latest.is_symlink():
        latest.unlink()
    elif latest.exists():
        import shutil
        shutil.rmtree(latest)
    latest.symlink_to(run_dir)

    # Save individual agent outputs
    for result in results:
        agent_file = agents_dir / f"{result.agent_name}.md"
        status_emoji = "✅" if result.status == "success" else "❌"
        content = f"""# {result.agent_name} {status_emoji}

**Status:** {result.status}
**Tokens:** {result.tokens_used:,}
**Duration:** {result.duration_seconds:.1f}s
"""
        if result.error:
            content += f"**Error:** {result.error}\n"
        if result.output:
            content += f"\n---\n\n{result.output}\n"
        agent_file.write_text(content)

    # Save synthesis
    synthesis_file = run_dir / "synthesis.md"
    synthesis_file.write_text(synthesis)

    # Save run metadata
    metadata = {
        "objective": objective,
        "timestamp": timestamp,
        "model": MODEL,
        "total_tokens": total_tokens,
        "duration_seconds": round(duration, 1),
        "estimated_cost_usd": round(cost, 4),
        "agents": [
            {
                "name": r.agent_name,
                "status": r.status,
                "tokens": r.tokens_used,
                "duration": round(r.duration_seconds, 1),
                "error": r.error,
            }
            for r in results
        ]
    }
    meta_file = run_dir / "metadata.json"
    meta_file.write_text(json.dumps(metadata, indent=2))


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
  python parallel_swarm.py --plan-only "Design a LinkedIn strategy"
  python parallel_swarm.py --max-agents 8 "Full product launch analysis"
        """
    )
    parser.add_argument("objective", help="The task/objective for the swarm")
    parser.add_argument("--agents", help="Comma-separated agent names (auto-selects if omitted)")
    parser.add_argument("--max-agents", type=int, default=5, help="Max agents for auto-selection (default: 5)")
    parser.add_argument("--plan-only", action="store_true", help="Show plan without executing")
    parser.add_argument("--model", help=f"Override model (default: {MODEL})")
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

    # Validate API key
    if not API_KEY or API_KEY == "PASTE_YOUR_KEY_HERE":
        print("❌ ERROR: No Gemini API key found.")
        print(f"   Set GEMINI_API_KEY in {ENV_PATH}")
        print("   Get your key at: https://aistudio.google.com")
        sys.exit(1)

    # Override model if specified via CLI
    if args.model:
        _apply_model_override(args.model)

    # Mini-brief mode: use specialized work orders
    if args.mode == "mini-brief":
        research_brief = ""
        if args.context:
            ctx_path = Path(args.context)
            if ctx_path.exists():
                research_brief = ctx_path.read_text()
                print(f"\n📄 Loaded research brief from {args.context}")
            else:
                print(f"⚠️  Context file not found: {args.context}")

        work_orders = generate_mini_brief_work_orders(
            concept=args.objective,
            research_brief=research_brief,
            mode=args.concept_mode,
            platform=args.platform,
        )
        agents = [wo.agent_name for wo in work_orders]
        print(f"\n🎯 Mini-Brief Mode: {args.concept_mode} | Platform: {args.platform}")
        print(f"👥 Expert constellation: {', '.join(dict.fromkeys(agents))}")

        # Run with pre-built work orders (bypass generate_work_orders)
        result = asyncio.run(
            _execute_swarm_with_orders(args.objective, work_orders, plan_only=args.plan_only)
        )
    else:
        # Default mode: select agents and generate generic work orders
        if args.agents:
            agents = [a.strip() for a in args.agents.split(",")]
            for a in agents:
                if a not in EXPERT_DOMAINS:
                    print(f"⚠️  Unknown agent: {a} (will use fallback context)")
        else:
            agents = auto_select_agents(args.objective, args.max_agents)
            print(f"\n🤖 Auto-selected agents: {', '.join(agents)}")

        result = asyncio.run(execute_swarm(args.objective, agents, plan_only=args.plan_only))


def _apply_model_override(model_name: str):
    """Apply a model override at module level."""
    pass


if __name__ == "__main__":
    main()
