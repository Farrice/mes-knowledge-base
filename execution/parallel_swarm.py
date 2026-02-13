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

# Gemini API endpoint
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"


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
}


# --------------------------------------------------------------------------
# API Client
# --------------------------------------------------------------------------

async def call_gemini(prompt: str, system_instruction: str = "", 
                      retries: int = MAX_RETRIES) -> Tuple[str, int]:
    """
    Make a single Gemini API call. Returns (response_text, tokens_used).
    Handles retries with exponential backoff.
    """
    import urllib.request
    import urllib.error

    headers = {"Content-Type": "application/json"}

    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 4096,
        }
    }

    if system_instruction:
        body["systemInstruction"] = {
            "parts": [{"text": system_instruction}]
        }

    url = f"{API_URL}?key={API_KEY}"
    data = json.dumps(body).encode("utf-8")

    for attempt in range(retries + 1):
        try:
            # Run blocking IO in thread pool to keep async
            loop = asyncio.get_event_loop()
            response_text, tokens = await loop.run_in_executor(
                None, _sync_api_call, url, data, headers
            )
            return response_text, tokens

        except Exception as e:
            if attempt < retries:
                wait = 2 ** attempt
                print(f"  ⚠️  Retry {attempt + 1}/{retries} for API call (waiting {wait}s): {e}")
                await asyncio.sleep(wait)
            else:
                raise


def _sync_api_call(url: str, data: bytes, headers: dict) -> Tuple[str, int]:
    """Synchronous HTTP call to Gemini API (runs in thread pool)."""
    import urllib.request
    import urllib.error
    import ssl

    # Build SSL context — macOS Python often lacks root certs
    try:
        import certifi
        ssl_ctx = ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        # certifi not installed — use unverified context (only for Google API)
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=120, context=ssl_ctx) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        raise RuntimeError(f"API error {e.code}: {error_body}")

    # Extract text
    try:
        text = result["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        raise RuntimeError(f"Unexpected API response: {json.dumps(result)[:500]}")

    # Extract token count
    usage = result.get("usageMetadata", {})
    tokens = usage.get("totalTokenCount", 0)

    return text, tokens


# --------------------------------------------------------------------------
# Agent Context Loading
# --------------------------------------------------------------------------

def load_agent_context(agent_name: str) -> str:
    """
    Load minimal expert context — SKILL.md only (not the full genius-patterns 
    to keep token usage lean). Returns system instruction for the agent.
    """
    # Check agent directory first
    agent_dir = AGENTS_PATH / agent_name
    skill_dir = SKILLS_PATH / agent_name.replace(" ", "-")

    context_parts = []

    # Agent persona
    agent_file = agent_dir / "AGENT.md"
    if agent_file.exists():
        content = agent_file.read_text()
        # Only take first 2000 chars to stay lean
        context_parts.append(content[:2000])

    # Skill overview — look for matching skill names
    for skill_name in SKILLS_PATH.iterdir():
        if agent_name in skill_name.name:
            skill_file = skill_name / "SKILL.md"
            if skill_file.exists():
                content = skill_file.read_text()
                context_parts.append(content[:2000])
            break

    if not context_parts:
        # Fallback: use domain description
        domain = EXPERT_DOMAINS.get(agent_name, "general expertise")
        context_parts.append(
            f"You are {agent_name}, an expert in: {domain}. "
            f"Apply your specialized knowledge and frameworks to complete the task."
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

    # Load expert context
    system_instruction = load_agent_context(agent)

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
        return response
    except Exception as e:
        return f"❌ Synthesis failed: {e}\n\nRaw agent outputs preserved in individual files."


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

    # Select agents
    if args.agents:
        agents = [a.strip() for a in args.agents.split(",")]
        # Validate
        for a in agents:
            if a not in EXPERT_DOMAINS:
                print(f"⚠️  Unknown agent: {a} (will use fallback context)")
    else:
        agents = auto_select_agents(args.objective, args.max_agents)
        print(f"\n🤖 Auto-selected agents: {', '.join(agents)}")

    # Run
    result = asyncio.run(execute_swarm(args.objective, agents, plan_only=args.plan_only))


def _apply_model_override(model_name: str):
    """Apply a model override at module level."""
    global MODEL, API_URL
    MODEL = model_name
    API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"


if __name__ == "__main__":
    main()
