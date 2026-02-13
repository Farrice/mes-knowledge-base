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

## Available Agents
cardinal-mason, harry-dry, seena-rez, samuel-thompson, jim-oshaughnessy, jeremy-miner, michael-bernoff, shaan-puri, kallaway, oren, dan-koe, lara-acosta, erica-mallet, lulu-cheng-meservey, seth-godin, tobias-allen, nicolas-cole, nathan-gotch, adam-enfroy, daniel-priestley, tom-noske, sabri-suby, rory-sutherland, monk-ai, ali-abdaal, nick-saraev, david-bayer, fareed-zakaria, jonathan-franzen, lucas-alpay, donald-miller

## Cost Estimate (Gemini 3 Flash)
- 5-agent swarm: ~$0.15
- 10-agent swarm: ~$0.35
- Even running 10 swarms/day ≈ $3.50/day max
