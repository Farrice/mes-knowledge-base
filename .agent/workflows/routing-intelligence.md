---
description: View the routing intelligence dashboard — expert utilization, domain distribution, feedback analytics, and suggestions.
---

# /routing-intelligence — Routing Analytics Dashboard

View how your routing system is performing. See which experts get used, which domains get the most requests, and where routing decisions are landing well or falling short.

## Usage

```
/routing-intelligence
```

## Steps

### 1. Generate Report

Run the routing intelligence scoreboard:

```bash
python execution/routing_intelligence.py scoreboard
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
python execution/routing_intelligence.py utilization      # Expert usage table
python execution/routing_intelligence.py unused           # Agents never deployed
python execution/routing_intelligence.py domain-dist      # Domain breakdown
python execution/routing_intelligence.py top-combos       # Best ensembles
python execution/routing_intelligence.py underperforming  # Negative feedback routes
```

## When to Use

- **Weekly review** — Check routing health alongside `/weekly-pulse`
- **After a busy period** — See which experts carried the load
- **When something feels off** — Identify if wrong experts are being routed
- **Curiosity** — "Who have I been using most?"
- **Before consulting calls** — Show tangible proof of system usage and performance
