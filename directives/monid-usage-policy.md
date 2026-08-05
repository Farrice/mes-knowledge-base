# Monid AI Usage Policy

> **Monthly Budget Limit: $25.00 (estimated ceiling based on $5/run default)**
> This directive applies to ALL agents, workflows, and research tasks that use Monid.
> **Last Updated: 2026-08-05**

## Purpose

Monid is the **OpenRouter for AI agents**: a universal API gateway covering 1500+ tools from 13+ providers (Apify, Semrush, Reddit, X/Twitter, YouTube, web search, TikTok, LinkedIn, Instagram, Amazon, Google Reviews, blockchain data). One wallet, one MCP URL, agent discovers tools → checks price → executes → pays per call.

Key differentiator from Apify: **multi-provider router** (we pick provider, Monid optimizes cost). Complements Apify for cross-provider research queries; does NOT replace Apify for deep, single-provider dives (Reddit 50-post analysis is cheaper via Apify's per_result model).

> [!IMPORTANT]
> **Monid is for exploratory multi-provider research. Apify is for deep single-source dives. Use them as a team: route to Monid for discovery, route to Apify for depth.**

---

## When to Use Monid (PRIMARY)

- **Multi-provider research** — one query across X/Twitter, Reddit, YouTube, Semrush, web search in a single run
- **Quick insight discovery** — baseline signals before deeper Apify dives
- **Semrush keyword intelligence** — direct access to keyword metrics (routing to Google/Ahrefs is slower)
- **Real-time trending** — X/Twitter trending topics, community sentiment, YouTube topical video discovery
- **Breadth research** — when you need signals from 5+ sources, cost-optimized by Monid's router

## When to Use Apify Instead

- **Reddit deep dives** — thread mining, comment analysis, >50-item studies
- **Single-platform bulk extraction** — Instagram/TikTok profile audits, Amazon Best Sellers, Google Maps audits
- **Structured-data funnels** — when you need consistency across 100+ results from one source

## Per-Call Costs (Measured 2026-08-05)

Monid demonstrated cost:
- Eddy Ballesteros' full AI SEO research report (multi-provider): **$0.03**
- Per-call floor: ~$0.001 ("about a tenth of a cent each")
- Signup credit: $1 free (good for ~100 mid-size queries)
- Implication: $5/run cap ≈ 150+ full reports — runaway guard, not a constraint

**Cost Model**: pay-per-call (actual cost varies by query complexity + selected providers). No per-result pricing like Apify's original 7 actors.

---

## Setup (Three Surfaces)

### 1. claude.ai (easiest)
Settings → Connectors → Add custom connector
- Name: "Monid"
- MCP URL: `https://mcp.monid.ai/v1`
- Click Add → authorize Monid login → Allow

Account gets $1 free credit on signup (hundreds of calls).

### 2. Claude Code (this project)
`.mcp.json` (added automatically by this deployment):
```json
{
  "mcpServers": {
    "monid": {
      "type": "http",
      "url": "https://mcp.monid.ai/v1"
    }
  }
}
```

Reload the MCP service after edits:
```bash
# In Claude Code: activate Monid
open https://app.monid.ai  # dashboard (requires account + wallet funding)
```

### 3. Codex (CLI)
Add to `.mcp.json` or Codex's equivalent config. **Funding step**: wallet link at https://app.monid.ai (Farrice's manual step).

---

## Cost Tracking & Budget

| Metric | Value |
|--------|-------|
| **Monthly Budget** | $25.00 (estimated, based on $5/run cap) |
| **Soft Warn (Yellow)** | $17.50 (70%) — prefer Apify for repetitive work |
| **Hard Stop (Red)** | $22.50 (90%) — block new runs |
| **Per-Run Cap** | $5.00 default (override with approval token) |
| **Reset Cadence** | Calendar month (1st at 00:00) — auto-reset by wrapper |

### Tracking File

Usage is tracked in: `.agent/monid-usage.json`

Format: JSONL log of every call with cost extracted from Monid's response + auto-resets on month boundary.

### Realistic Monthly Capacity

At $25.00 budget, you can comfortably run:
- 10 multi-provider discovery runs (mixed X/Reddit/YouTube/Semrush) = ~$0.30
- 30 quick trend checks (single endpoint) = ~$0.03
- 5 full SEO audits (Eddy-scale, multi-provider) = ~$0.15
- **Total: ~$0.48 of $25.00 used (~2%)**

**You have massive headroom.** Monthly spend typically: <$1.00. The $5/run cap exists as a runaway guard for multi-provider batch work.

---

## The Fallback Contract

On budget exhaustion or error, Monid returns structured error JSON (no exception). Workflows MUST check `.status` and reroute:

```json
{
  "status": "budget_exhausted" | "error" | "cost_ceiling_exceeded",
  "fallback": true,
  "message": "...",
  "alternative": "Use Apify (apify_client.py) or web search instead.",
  "items": []
}
```

**Fallback chain:**
1. **Monid succeeds** — use the data
2. **Monid budget exhausted** → Apify for single-provider deep dives, OR Perplexity for synthesis
3. **Monid cost-exceeded** → approve token or route to Apify

---

## Pre-Run Checks

For queries expected to consume **>$0.5** (roughly multi-provider research):

```bash
python3 execution/monid_client.py budget-status
```

Cheap queries (single endpoint, <10 results) do NOT need a pre-check.

---

## Cost-Gate Integration

Every Monid run is gated by `cost_gate.py` with `service="monid"`. Default behavior:

- **< $5.00 est. cost** → auto-approve, log cost
- **$5.00–$25.00** → request approval token
- **> $25.00** → denied

Approval token usage:
```bash
python3 execution/cost_gate.py approve --service monid --minutes 15
python3 execution/monid_client.py "<query>"  # within 15 min
```

---

## Logging

Every call auto-logged to `.agent/monid-usage.json` by the wrapper:

```json
{
  "ts": "2026-08-05T22:00:00+00:00",
  "query_preview": "AI SEO tools trend...",
  "provider": "multi",
  "results": 42,
  "cost": 0.03
}
```

List is bounded to last 200 runs (FIFO).

---

## Override

To temporarily increase the monthly budget:

1. Edit `MONID_MONTHLY_BUDGET_USD` in `execution/monid_client.py` (if created)
2. OR manually bump the budget ceiling in `.agent/monid-usage.json`
3. Document the override in `.agent/session-state.md`

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-08-05 |
| **Activation Count** | 1 (cost-gate registration) |
| **30-Day Review Date** | 2026-09-05 |

*Effective: 2026-08-05 | Setup: MCP + cost-gate | Fallback chain: Apify → Perplexity | Monthly ceiling: $25.00 (90% hard stop)*
