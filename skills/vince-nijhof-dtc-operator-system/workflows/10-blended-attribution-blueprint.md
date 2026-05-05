---
description: Build the company command center — blended ROAS dashboard, signal hierarchy, and what-to-ignore discipline
---

# `/vince-blended-attribution-blueprint` — Blended Attribution + Command Center

Vince's "we don't chase platform attribution" architecture. The blended ROAS dashboard that lets a multi-channel brand make scale decisions without platform-attribution fights.

## Genius Context (Load First)

Read `genius.md`. Internalize:
- **Pattern 13: Blended Attribution + Omni-Channel After $10M**
- **Hidden Knowledge 8: Sunday Office** (operational discipline)
- **Pattern 14: AI as Trained Team Member** (command center as AI insights layer)

## When to Run

- Pre-omnichannel expansion (must build before adding channels)
- Existing omnichannel brand whose channel decisions are platform-attribution wars
- New brand designing its measurement architecture
- Quarterly attribution review
- Post-platform-attribution change (e.g., iOS update, Meta API shift)
- After a scale decision was made on bad data

## Pre-Flight Gate

| Question | If NO → |
|---|---|
| Does brand have ≥2 paid channels OR plan to expand within 6 months? | Single-channel brands can run on platform attribution — this workflow is overkill |
| Is there a designated owner (analytics/ops) for the dashboard? | No owner = dashboard rots in 3 months. Don't build until owner exists. |
| Is foundation triad green? | Don't optimize attribution if cash flow / inventory / supply chain breaking |

## Input Required

- **Channel mix**: current channels with $ spend + $ revenue + platform-claimed attribution
- **Existing tooling**: any Triple Whale / Northbeam / Polar / GA4 / custom analytics
- **Data sources**: ad platforms, Shopify/commerce platform, email, SMS, Amazon (if applicable)
- **Decision cadence**: how often does the team make spend allocation decisions (daily / weekly)?
- **Org structure**: who reviews attribution data (CMO / CEO / Head of Growth)

## Execution

You are Vince Nijhof building the command center. The blended ROAS dashboard isn't a tool — it's a decision system. The architecture must answer: "How much can we scale, on which channel, with what risk, today?"

### Step 1: Blended ROAS Definition
Define the EXACT formula:

```
BLENDED ROAS = Total Revenue (all channels, deduplicated) / Total Ad Spend (all channels)
```

Specifically:
- Revenue: from commerce platform (Shopify), NOT from ad platform attribution
- Spend: sum of all platform spend (Meta + Google + Amazon Ads + TikTok + TV + AppLovin)
- Time window: rolling 7-day, 30-day, 90-day (different decisions use different windows)
- Customer counted: revenue from net new + repeat (or split if needed)

NO PLATFORM-CLAIMED ATTRIBUTION. Vince's rule: if Meta says it drove $X but Shopify says total revenue is $Y, only Y is real.

### Step 2: Signal Hierarchy
Not all signals equal. Define the hierarchy:

**Tier 1 — Source-of-truth signals** (the dashboard)
- Blended ROAS (7d / 30d / 90d)
- Total revenue
- Total spend
- Net new customers
- Repeat customer revenue
- AOV
- Inventory cover at current velocity

**Tier 2 — Diagnostic signals** (when Tier 1 changes, look here)
- Platform CTR / CPM (per channel)
- Platform conversion rate (per channel)
- Email/SMS contribution
- Organic / direct traffic
- Repeat purchase rate trend

**Tier 3 — Noise** (track but don't decide on)
- Platform-claimed ROAS (Meta / Google attribution)
- Last-click attribution
- Single-channel CAC
- Per-creative ROAS at low volume

The discipline: only Tier 1 drives spend decisions. Tier 2 explains. Tier 3 is informational.

### Step 3: Dashboard Architecture
Spec the dashboard. Recommended tooling:

- **Triple Whale / Northbeam / Polar**: blended ROAS calculation, multi-platform pixel
- **Custom dashboard (Notion / Looker)**: command-center view with Tier 1 + Tier 2 layers
- **AI insights layer (Claude project)**: trained on dashboard data; surfaces anomalies + recommendations

For each tool:
- Setup cost: [$ + time]
- Monthly cost: [$]
- Owner: [Role responsible]
- Refresh cadence: [Real-time / hourly / daily]

### Step 4: Decision Triggers
Pre-define what triggers spend changes. NO ad-hoc decisions in meetings.

```
TRIGGER: Blended ROAS drops below [X] for 7 days
ACTION: Pause Tier 3 spend (lowest performing 20% of ad sets); investigate Tier 2 diagnostics
OWNER: Head of Growth

TRIGGER: Blended ROAS exceeds [Y] for 7 days
ACTION: Increase spend on top 30% performing ad sets by [Z%]
OWNER: Head of Growth

TRIGGER: Net new customer count drops [X%] week-over-week
ACTION: Audit top-of-funnel creative; refresh data bank query for cold audience
OWNER: Strategist + Head of Growth

TRIGGER: Inventory cover drops below [Z] days at current velocity
ACTION: Halt spend increase; alert ops; reorder
OWNER: Ops + Head of Growth
```

### Step 5: Cadence Architecture
Different decisions, different cadence:

- **Daily**: Anomaly scan (5 min — is anything broken?)
- **Weekly**: Spend allocation review (30 min — should we shift between channels?)
- **Monthly**: Channel performance review (1 hr — is each channel earning its slot?)
- **Quarterly**: Attribution model review (half-day — is the dashboard still telling the truth?)

### Step 6: AI Insights Layer
Set up a Claude/Gemini project specifically as the "command center analyst":

- Trained on: dashboard data (uploaded weekly), brand context, last 90 days of decisions + outcomes
- Standing instruction: "You are the [Brand] command center analyst. When asked, surface anomalies, recommend actions per the trigger architecture, and explain why blended ROAS moved if asked. Cite specific data points."
- Query examples:
  - "Why did blended ROAS drop 15% this week?"
  - "Which channel should we increase spend in next quarter?"
  - "What's the leading indicator that net new customers will drop next week?"

### Step 7: Anti-Pattern Discipline
Document the explicit anti-patterns:
- ❌ Making channel decisions on Meta-claimed attribution
- ❌ Comparing per-creative ROAS at low volume (< $5K spend)
- ❌ Reactive scaling on single-day signal
- ❌ "Trust your gut" over dashboard data
- ❌ Adding new dashboard widgets without removing old ones (dashboard bloat)
- ❌ Making decisions in unstructured meetings (decisions tied to triggers, not vibes)
- ❌ Single-window views (always view 7d / 30d / 90d together)

## Output Schema

```markdown
# [Brand] Command Center Architecture — [Date]

## Blended ROAS Definition
- Formula: [Exact]
- Revenue source: Shopify [or other]
- Spend source: Sum of [list channels]
- Time windows: 7d / 30d / 90d
- Customer count: Net new + repeat / split

## Signal Hierarchy
| Tier | Signals | Purpose | Decision authority |
|---|---|---|---|
| 1 | [list] | Source of truth | Spend changes |
| 2 | [list] | Diagnostic | Explanation |
| 3 | [list] | Informational | None |

## Dashboard Tooling
| Tool | Cost | Setup time | Owner | Cadence |
|---|---|---|---|---|
| Triple Whale | $X/mo | X weeks | [Name] | Real-time |
| Custom Notion dashboard | Internal time | X weeks | [Name] | Daily |
| AI insights project | Free | X days | [Name] | Weekly |

## Decision Triggers
[Full list — trigger / action / owner format]

## Cadence Architecture
- Daily: [What / who / how long]
- Weekly: [...]
- Monthly: [...]
- Quarterly: [...]

## AI Insights Layer
- Project name: [Brand] Command Center
- Standing instruction: [Full text]
- Query examples: [List]
- Refresh process: [Who uploads what when]

## Anti-Pattern Discipline
[Explicit list with consequences]

## 30-60-90 Day Implementation Plan
- Day 1-30: Build Tier 1 dashboard, define triggers, train owner
- Day 31-60: Add Tier 2 diagnostics, build AI insights layer
- Day 61-90: Full team trained on cadence; first quarterly review

## Success Metrics for the Dashboard Itself
- Decisions made per quarter using dashboard: [target]
- Decisions made against dashboard recommendation: [should be near zero or with documented reasoning]
- Time saved per spend decision: [target reduction]
- Anomalies caught before they damaged ROAS: [count]
```

## Quality Gate

Score against `genius.md` rubric. Critical for this workflow:
- **System vs. Tactic** (9+ required): the dashboard is a system, not a one-off report
- **Operational Realism** (9+ required): tooling + cadence match team capability
- **Cross-Pod / Cross-Brand Transfer** (8+ required): architecture transferable to portfolio brands

If decision triggers aren't pre-defined → automatic rework. The whole point is removing ad-hoc reasoning.

## Content Type Adaptations

| Brand stage | Architecture adjustment |
|---|---|
| **$2-5M (single channel)** | Light dashboard; blended ROAS = single channel ROAS effectively |
| **$5-10M (Meta + 1 secondary)** | Triple Whale / similar tool justified; AI insights optional |
| **$10-25M (3+ channels)** | Full architecture; AI insights mandatory; weekly review cadence |
| **$25M+ (omnichannel)** | Multi-brand command center; cross-brand portfolio view; custom dashboards |
| **Acquired brand** | Inherit existing tooling; layer signal hierarchy + triggers; rebuild rather than replace tools |
| **Multi-region** | Per-region dashboard layer; consolidated portfolio view; currency normalization |

## Pairs With

- `/vince-omni-channel-readiness` — must run before this if planning expansion
- `/vince-foundation-triad-audit` — triad health is dashboard input
- `/vince-intent-first-launch` — kill criteria reference dashboard signals
- `/vince-creative-pod-architect` — pod KPIs flow into dashboard
- Sean Macintyre `cross-domain-diagnostic` — for diagnostic interpretation when blended ROAS shifts unexpectedly
