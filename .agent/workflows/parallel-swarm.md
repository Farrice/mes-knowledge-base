---
description: Deploy a true parallel agent swarm using the Gemini API for simultaneous multi-expert execution
---

# /parallel-swarm — True Parallel Orchestration

This workflow fires multiple expert agents simultaneously via the Gemini API, then synthesizes their outputs into a unified deliverable.

## Prerequisites
- Gemini API key set in `.env` (`GEMINI_API_KEY=your_key`)
- Python 3.9+

## Quick Run

// turbo
1. Run the swarm with auto-selected agents:
```bash
python /Users/farricecain/Google\ Antigravity/execution/parallel_swarm.py "YOUR OBJECTIVE HERE"
```

2. Run with specific agents:
```bash
python /Users/farricecain/Google\ Antigravity/execution/parallel_swarm.py --agents "cardinal-mason,harry-dry,shaan-puri" "YOUR OBJECTIVE HERE"
```

3. Run with more agents (up to 10):
```bash
python /Users/farricecain/Google\ Antigravity/execution/parallel_swarm.py --max-agents 8 "YOUR OBJECTIVE HERE"
```

4. Preview the plan without executing:
```bash
python /Users/farricecain/Google\ Antigravity/execution/parallel_swarm.py --plan-only "YOUR OBJECTIVE HERE"
```

5. **Research-first mode** — ground the swarm in real data before firing:
```
/parallel-swarm --research "YOUR OBJECTIVE HERE"
```

## Research-First Mode (`--research`)

**Problem**: Standard Gemini swarm agents can't do web search or read files. They operate on injected skill context + training knowledge, which makes their output hypothetical — "what the expert would think" rather than "what the expert thinks given real market data."

**Solution**: When `--research` is specified, a pre-research phase runs BEFORE the Gemini swarm:

### How It Works

1. **Pre-Research Phase** (Tier 1 Claude agents, ~30-60 seconds):
   Spawn 2 Task tool sub-agents in a single message:

   **Research Agent 1: Market Intelligence**
   ```
   Use WebSearch to find current data (2025-2026) about: [objective]
   Focus on: market size, trends, recent developments, key players, pricing data.
   Write findings to: .tmp/swarm-research/market-intel.md
   Format: bullet points with source URLs. Aim for 10-15 data points.
   ```

   **Research Agent 2: Audience & Competitive Signals**
   ```
   Use WebSearch to find: [objective]-related audience discussions, competitor activity, and sentiment.
   Check: Reddit, Twitter/X, LinkedIn, forums, review sites.
   Write findings to: .tmp/swarm-research/audience-signals.md
   Format: bullet points with source URLs and direct quotes where available.
   ```

2. **Context Enrichment**:
   After both research agents return, read their findings. The orchestrator then injects the research data into each Gemini agent's prompt alongside their expert skill context:

   ```
   ## REAL MARKET DATA (from live research)
   [Inject contents of market-intel.md and audience-signals.md]

   ## YOUR EXPERT CONTEXT
   [Standard skill injection from parallel_swarm.py]

   ## YOUR TASK
   Analyze [objective] using your expert framework GROUNDED IN the market data above.
   Do NOT speculate when data exists. Reference specific findings.
   ```

3. **Grounded Swarm Execution**:
   Run `parallel_swarm.py` as normal, but with the enriched prompts.

### Cost Impact
- Standard swarm: ~$0.15 (5 agents)
- Research-first swarm: ~$0.15 + 2 Claude agent calls ≈ $0.30-0.50 total
- Still dramatically cheaper than running 5 Claude agents with full tool access

### When to Use `--research`
- Market analysis, competitive intelligence, trend assessment
- Any objective where "what's actually happening" matters more than "what the expert thinks in theory"
- Audience research, pricing decisions, product validation

### When Standard Mode is Fine
- Creative ideation (brainstorming names, angles, frameworks)
- Internal strategy (applying expert frameworks to YOUR known situation)
- Content generation (voice, style, format — not data-dependent)

### Output Files (Research-First Mode)
```
.tmp/swarm-research/
  market-intel.md
  audience-signals.md
swarm_outputs/latest/
  synthesis.md          (grounded synthesis)
  agent_outputs/*.md    (individual grounded expert outputs)
  metadata.json
```

## Output

All outputs are saved to `/Users/farricecain/Google Antigravity/swarm_outputs/`:
- `latest/synthesis.md` — The unified deliverable
- `latest/agent_outputs/[agent].md` — Individual expert outputs
- `latest/metadata.json` — Token usage, cost, timing

## Safety Rails
- **Max 1 retry per agent** (no infinite loops)
- **500K token budget ceiling** (auto-stops if exceeded)
- **Max 10 parallel agents** (configurable in .env)
- **Real-time cost tracking** printed to terminal

## Identity Firewall Rule
When generating content about Farrice Cain:
- ONLY reference FARRICE.md for personal background
- NEVER pull biographical details from client project directories
- Client projects (Coach Cooz, etc.) are CLIENT work, not Farrice's personal story

## Post-Generation Identity Check
Before finalizing any content that references Farrice's background:
1. Grep for: "trauma", "addiction", "clinical", "therapy", "therapist", "crisis"
2. If found: Flag and cross-reference against FARRICE.md
3. If not in FARRICE.md: Remove and replace with verified background

## Available Agents
cardinal-mason, harry-dry, seena-rez, samuel-thompson, jim-oshaughnessy, jeremy-miner, michael-bernoff, shaan-puri, kallaway, oren, dan-koe, lara-acosta, erica-mallet, lulu-cheng-meservey, seth-godin, tobias-allen, nicolas-cole, nathan-gotch, adam-enfroy, daniel-priestley, tom-noske, sabri-suby, rory-sutherland, monk-ai, ali-abdaal, nick-saraev, david-bayer, fareed-zakaria, jonathan-franzen, lucas-alpay, donald-miller

## Cost Estimate (Gemini 3 Flash)
- 5-agent swarm: ~$0.15
- 10-agent swarm: ~$0.35
- Even running 10 swarms/day ≈ $3.50/day max
