---
description: View the routing intelligence dashboard
---

# /routing-intelligence — Routing Analytics Dashboard

View how your routing system is performing. See which experts get used, which domains get the most requests, and where routing decisions are landing well or falling short.

## Operator Core Alignment

This workflow is the canonical source of truth for Routing-intelligence
behavior. Global and local Routing-intelligence wrappers must stay thin
compatibility wrappers that point back here, not competing behavior contracts.

Preserve these invariants:

- `/routing-intelligence` is read-only analytics by default.
- Start with `python3 execution/routing_intelligence.py scoreboard` for the dashboard.
- Use subcommands for focused read-only views: `python3 execution/routing_intelligence.py utilization`, `python3 execution/routing_intelligence.py unused`, `python3 execution/routing_intelligence.py domain-dist`, `python3 execution/routing_intelligence.py top-combos`, and `python3 execution/routing_intelligence.py underperforming`.
- `python3 execution/routing_intelligence.py misroute` is write-capable.
- Only write routing feedback through `misroute` when the user explicitly reports a wrong route or asks to record a correction.
- Do not auto-optimize routes, mutate workflows, sync Notion, mutate Mission, perform cleanup, or mirror global files from `/routing-intelligence`.
- Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`; use `/routing-intelligence` for explicit routing analytics and scoreboard questions.
- Real Codex subagents require explicit authorization.

## Usage

```
/routing-intelligence
```

## Steps

### 1. Generate Report

Run the routing intelligence scoreboard:

```bash
python3 execution/routing_intelligence.py scoreboard
```

### 2. Present Dashboard

Display the generated report to the user. The report includes:

| Section | What It Shows |
|---------|---------------|
| **Overview** | Total routings, feedback count, positive rate |
| **Expert Utilization** | Who's been deployed, how often, with what ratings |
| **Domain Distribution** | Which domains get the most requests |
| **Top Performers** | Highest-rated ensemble combinations |
| **Underperformers** | Routes with negative feedback and corrections |
| **Unused Experts** | Agents with zero deployments (opportunity flags) |
| **Suggestions** | Dormant experts, strong pairings, recurring corrections |

### 3. Offer Follow-Up Actions

After presenting the dashboard, offer read-only interpretation:

- "Want me to try deploying [unused expert] on your next [domain] task?"
- "The [pairing] combination has been working well — want to use it for [current context]?"
- "Route [domain] had negative feedback — want me to record this as a `misroute` correction?"

Do NOT auto-optimize. Present observations and let the user decide.

### 4. Subcommands (Optional)

For quick lookups without the full dashboard:

```bash
python3 execution/routing_intelligence.py utilization      # Expert usage table
python3 execution/routing_intelligence.py unused           # Agents never deployed
python3 execution/routing_intelligence.py domain-dist      # Domain breakdown
python3 execution/routing_intelligence.py top-combos       # Best ensembles
python3 execution/routing_intelligence.py underperforming  # Negative feedback routes
```

## When to Use

- **Weekly review** — Check routing health alongside `/weekly-pulse`
- **After a busy period** — See which experts carried the load
- **When something feels off** — Identify if wrong experts are being routed
- **Curiosity** — "Who have I been using most?"
- **Before consulting calls** — Show tangible proof of system usage and performance
