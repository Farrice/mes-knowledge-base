---
description: View the routing intelligence dashboard
---

# /routing-intelligence — Routing Analytics Dashboard

View how your routing system is performing. See which experts get used, which domains get the most requests, and where routing decisions are landing well or falling short.

## Operator Core Alignment

This workflow is the canonical source of truth for Routing-intelligence behavior.
Global and local Routing-intelligence wrappers must stay thin compatibility
wrappers that point back here, not competing behavior contracts.

Preserve these invariants:

- `/routing-intelligence` is read-only analytics by default.
- Start with `python3 execution/routing_intelligence.py scoreboard` for the dashboard.
- Use subcommands for focused read-only views: utilization, unused, domain-dist, top-combos, and underperforming.
- Only write routing feedback through `misroute` when the user explicitly reports a wrong route or asks to record a correction.
- Do not auto-optimize routes, mutate workflows, sync Notion, mutate Mission, perform cleanup, or mirror global files from `/routing-intelligence`.
- Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`; use `/routing-intelligence` for explicit routing analytics and scoreboard questions.
- Real Codex subagents require explicit authorization.

## Usage

```
/routing-intelligence
routing intelligence dashboard
source-command-routing-intelligence
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

After presenting the dashboard, offer:

- "Want me to try deploying [unused expert] on your next [domain] task?"
- "The [pairing] combination has been working well — want to use it for [current context]?"
- "Route [domain] had negative feedback — should I adjust the default expert assignment?"

Do NOT auto-optimize. Present observations and let the user decide.

### 4. Subcommands (Optional)

For quick lookups without the full dashboard:

```bash
python3 execution/routing_intelligence.py utilization      # Expert usage table
python3 execution/routing_intelligence.py unused           # Agents never deployed
python3 execution/routing_intelligence.py domain-dist      # Domain breakdown
python3 execution/routing_intelligence.py top-combos       # Best ensembles
python3 execution/routing_intelligence.py underperforming  # Negative feedback routes
python3 execution/routing_intelligence.py misroute --request "[request]" --wrong "[wrong-workflow]" --correct "[right-workflow]" --notes "[why]"
```

Use `misroute` only when Farrice says a route was generic, useless, wrong, or
defaulted to the wrong workflow, or when he explicitly asks to record a
correction. This creates both the routing record and the correction feedback, so
the System Governor has evidence to queue a supervised routing fix. Do not infer
or write route feedback from vague dissatisfaction.

## When to Use

- **Weekly review** — Check routing health alongside `/weekly-pulse`
- **After a busy period** — See which experts carried the load
- **When something feels off** — Identify if wrong experts are being routed
- **Curiosity** — "Who have I been using most?"
- **Before consulting calls** — Show tangible proof of system usage and performance

## Verification

After changing this workflow, run:

```bash
python3 execution/sync_operator_core_routing_intelligence.py --check
python3 execution/verify_operator_core_routing_intelligence.py
python3 execution/validate_skill.py source-command-routing-intelligence
python3 execution/routing_intelligence.py scoreboard
python3 execution/operator_core_status.py --plain
python3 execution/verify_operator_core_status.py
python3 execution/verify_system_control_plane.py
python3 execution/codex_live_surface_audit.py --strict
python3 execution/codex_harness_check.py
```
