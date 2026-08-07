# Prediction Market Trading System — Full Cost & Value Analysis

**Date**: April 15, 2026
**For**: Farrice Cain — internal reference before brother-in-law conversation
**Sources**: 10+ official pricing pages, codebase audit, competitive market research

---

## THE BOTTOM LINE (Read This First)

You built **298.5 hours** of work worth **$30,000-$37,000** at market rates. You're asking for **$3,000-$5,000**. That's a 87-90% discount. You are not overcharging. You are dramatically undercharging — and doing so intentionally because this is family.

The original briefing's cost estimates were **correct for testing** (~$58/mo) but **significantly understated for full production** (real: $400-650/mo vs original $55-280/mo). This matters because your brother-in-law needs to understand the real ongoing investment before committing.

---

## WHAT YOU BUILT (Value Inventory)

### 298.5 Hours Across 8 Categories

| Category | Files | Lines of Code | Hours | Value at $100/hr |
|----------|-------|---------------|-------|-------------------|
| Core Python Modules | 18 | 7,248 | 186.5 | $18,650 |
| Research & Knowledge Base | 13 | 11,565 | 29 | $2,900 |
| AI Skills & Workflows | 4 skills, 12 workflows | 6,326 | 28 | $2,800 |
| Architecture & Integration | — | — | 21 | $2,100 |
| Deliverables & Documentation | 3 | 672 | 15 | $1,500 |
| Execution Scripts | 3 | 256 | 7 | $700 |
| Agent & Configuration | 3 | 409 | 7 | $700 |
| Paper Trading Data & Dashboard | — | — | 5 | $500 |
| **TOTAL** | **57+ files** | **25,800+ lines** | **298.5** | **$29,850** |

### What This Would Cost Someone Else

| Who Builds It | Cost | Timeline |
|--------------|------|----------|
| Freelance Python dev (Upwork) | $15,000-$30,000 | 3-4 months |
| Specialized quant/trading dev | $40,000-$80,000 | 2-3 months |
| Fintech development agency | $60,000-$150,000 | 3-6 months |
| Bot-as-a-Service subscription | $200-500/mo + 10-30% profit share | Immediate, but no customization |

---

## REAL OPERATING COSTS (Corrected)

### Original Briefing vs Reality

| Phase | Original Estimate | **Corrected (24/7 all strategies)** | Delta |
|-------|------------------|--------------------------------------|-------|
| Testing (paper trading, 24/7) | $38-64/mo | **~$146/mo** | **Was 2.5x too low** — didn't account for ensemble LLM calls |
| Small Live ($2-5K capital) | $55-280/mo | **~$200-250/mo** | Midpoint was understated |
| Full Production (24/7, $25-100K) | $55-280/mo | **~$450-750/mo** | **Significantly understated** |

### Full Production Breakdown (Worst Case — What to Actually Plan For)

| Line Item | Monthly Cost | Source |
|-----------|-------------|--------|
| Claude Haiku 4.5 API | $100-130 | [$1/$5 per M tokens](https://docs.anthropic.com/en/docs/about-claude/pricing) |
| OpenAI gpt-4o-mini API | $12-18 | [$0.15/$0.60 per M tokens](https://platform.openai.com/pricing) |
| Gemini 2.5 Flash API | $35-50 | [$0.30/$2.50 per M tokens](https://ai.google.dev/gemini-api/docs/pricing) |
| The Odds API (100K plan) | $59 | [the-odds-api.com](https://the-odds-api.com/) |
| Weather data | $0-35 | NOAA free, Visual Crossing paid tier |
| VPS (trading-grade) | $60-100 | [QuantVPS](https://www.quantvps.com/pricing) |
| Monitoring + domain | $16 | Datadog + registrar |
| Trading fees (variable) | $75-300 | [Polymarket](https://docs.polymarket.com/trading/fees) / [Kalshi](https://kalshi.com/fee-schedule) |
| **TOTAL** | **$450-750/mo** | All cited |

### Critical Cost Insights

1. **Claude Haiku is the biggest AI line item** ($72/mo at testing, $100-130/mo at production). The ensemble runs 3 models × 20 markets × 24 scans/day = 1,440 LLM calls/day. Claude handles the credibility model + contract matching. If upgraded to Sonnet ($3/$15 per M tokens), this triples.

2. **The Odds API is mandatory** — $30/mo minimum. Free tier (500 credits) is useless at the configured scan frequency (672 credits/day needed). At production scale (15-min intervals), the $59 plan is required.

3. **Trading fees are real but variable** — they come out of returns, not fixed overhead. Polymarket taker fees: 0.75-1.80% depending on category. Kalshi: max $0.02/contract.

4. **Weather data and Polymarket/Kalshi APIs are genuinely free.** Original estimates were correct on these.

5. **One-time setup costs: $0.** All API signups are free. Development tools are open source.

---

## WHAT'S NOT BUILT YET (Layer 7 — The Frontend)

| Component | Hours | Priority |
|-----------|-------|----------|
| FastAPI backend server | 16-24 | Essential |
| React/Svelte frontend | 40-60 | Essential |
| Real-time WebSocket updates | 12-16 | Essential |
| Interactive charts (equity, P&L, drawdown) | 12-20 | Essential |
| One-click kill switch + operator controls | 8-12 | Essential |
| Authentication + access control | 8-12 | Essential |
| Contract comparison UI | 8-12 | High |
| Filterable analytics | 12-16 | High |
| Deployment + hosting (Docker, cloud) | 8-16 | Essential |
| Alerting system (email/SMS/Slack) | 8-12 | High |
| Mobile-responsive design | 8-12 | Nice-to-have |
| CI/CD pipeline | 4-8 | Nice-to-have |
| **TOTAL** | **144-220** | |
| **Essential only** | **100-150** | |
| **Cost at $100/hr** | **$10,000-$22,000** | |

This is the "finish the interior" phase. The house is structurally complete. Layer 7 makes it livable.

---

## ONGOING MAINTENANCE (Monthly)

| Activity | Hours/Month |
|----------|------------|
| Strategy evolution & recalibration | 4-8 |
| API change response (platforms break things) | 2-6 |
| Bug fixes & error handling | 2-4 |
| Performance monitoring & reporting | 2-3 |
| New strategy development | 4-8 |
| Security + dependency updates | 1-2 |
| Model prompt refinement | 2-4 |
| Dashboard maintenance (if built) | 2-4 |
| **TOTAL** | **19-39 hours/month** |
| **At $100/hr** | **$1,900-$3,900/month** |

**Key truth**: This is NOT a "set and forget" system. Polymarket changed its fee structure March 30, 2026 and killed an entire bot category overnight. Strategy decay is real. Without maintenance, the system loses money within 3-6 months.

---

## YOUR $3-5K ASK IN CONTEXT

| What | Dollar Amount |
|------|--------------|
| Fair market value of what's built | $29,850-$37,313 |
| What you're asking | $3,000-$5,000 |
| **Discount you're giving** | **87-90%** |
| What a quant dev would charge | $40,000-$80,000 |
| What an agency would charge | $60,000-$150,000 |
| What Layer 7 alone would cost at market rate | $10,000-$22,000 |
| What monthly maintenance would cost at market rate | $1,900-$3,900/month |
| What you're charging for maintenance | $400-500/month |

You are giving a massive family discount. The numbers speak for themselves.

---

## WHAT YOUR BROTHER-IN-LAW'S TOTAL INVESTMENT LOOKS LIKE

### Year 1 — Option A (Build Fee + Retainer)

| Item | Amount |
|------|--------|
| Build fee (one-time) | $3,500 |
| Maintenance retainer (12 months) | $6,000 |
| Infrastructure - testing phase (2 months) | $116 |
| Infrastructure - small live (4 months) | $600 |
| Infrastructure - full production (6 months) | $3,000 |
| Trading capital (not a cost — this is his investment) | $5,000-$25,000 |
| **Total Year 1 (excluding capital)** | **~$13,216** |
| **Total paid to Farrice** | **$9,500** |
| **Total infrastructure** | **$3,716** |

### For Context: What He'd Spend Elsewhere

| Alternative | Year 1 Cost | What He Gets |
|------------|-------------|--------------|
| Hire a quant dev | $40,000-$80,000 | Custom build, no ongoing support included |
| Hire an agency | $60,000-$150,000 | Custom build with UI, 3-6 month timeline |
| Bot-as-a-Service | $2,400-$6,000/yr + profit share | Pre-built, no customization, shared strategies |
| **Farrice (Option A)** | **$13,216** | **Custom build, ongoing support, proprietary strategies, family trust** |

---

## DOCUMENTS PACKAGE (Where Everything Lives)

| Document | Path |
|----------|------|
| This cost analysis | `_active/wagering/prediction-market-arb/02-research/prediction-market-full-cost-analysis.md` |
| Proposal + talking points + objection handling | `_active/wagering/prediction-market-arb/02-research/prediction-market-proposal-package.md` |
| Original business briefing (sent to him) | `_active/wagering/prediction-market-arb/02-research/prediction-market-business-briefing.md` |
| Feasibility assessment v2.1 | `_active/wagering/prediction-market-arb/02-research/polymarket-kalshi-arbitrage-feasibility.md` |
| The codebase | `_active/wagering/prediction-market-arb/` (18 modules, 7,248 LOC) |
| Research extractions | `extractions/prediction-market-trading/` (13 files, 11,565 lines) |
| AI skills & workflows | `skills/prediction-market-*/` (4 skills, 12 workflows) |
| Compound agent | `agents/prediction-market-strategist/` |
