---
name: "Prediction Market Making"
description: "Liquidity provision on Polymarket — spread optimization, quadratic reward maximization, adverse selection defense via real-time WebSocket monitoring, two-sided quoting with inventory management"
version: "1.0"
format: "completion-engine"
workflows: 3
source: "MES 3.0 Deep Extraction — Polymarket docs + poly-maker + polymarket-agents + polymarket-arbitrage + ecosystem analysis (5 sources, 5,200 lines)"
---

# Prediction Market Making

> Polymarket distributes $5M+/month in liquidity rewards via a quadratic scoring formula: `S(v,s) = ((v-s)/v)^2 * b`. This skill turns that reward pool into systematic income through two-sided quoting, adverse selection defense, and reward score optimization. The quadratic structure means a 1-cent quoter earns 3.24x the reward of a 5-cent quoter — small spread improvements yield exponential gains. Two-sided quoting earns 3x vs single-sided (c=3.0 divisor penalty). The poly-maker author confirms the bot is "unprofitable" — adverse selection destroys spread capture. Only the rewards program makes market making viable. Every workflow optimizes around that reality.

**Core Principle: Reward harvesting is the business model, not spread capture. The ImMike config sets `mm_enabled: false` with the comment "markets too efficient." Without the rewards layer, you are paying infrastructure costs to lose money to informed traders.**

---

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| market-select | [Market Selection & Spread Design](workflows/market-selection-spread.md) | Market ranking by reward pool/competition + optimal spread parameters + deployment config | Choosing which markets to quote, how much capital to allocate, what spreads to post |
| adverse-defense | [Adverse Selection Defense](workflows/adverse-selection-defense.md) | Complete defense system: news monitoring, auto-cancel/widen rules, inventory thresholds, heartbeat management, kill switch config | Building the protection layer that makes profitable market making possible |
| reward-optimize | [Reward Optimization](workflows/reward-optimization.md) | Full Q chain calculation, spread/size tuning, reward vs adverse selection trade-off modeling, per-market tuning recommendations | Maximizing share of the $5M+/month reward pool after basic infrastructure is running |

---

## Quick Reference

### Reward Formula
- **Score**: `S(v,s) = ((v-s)/v)^2 * b` — quadratic, tighter is exponentially better
- **Two-sided boost**: Q_min uses `max(min(Q_one, Q_two), max(Q_one/c, Q_two/c))` where c=3.0
- **Extreme midpoints** (<0.10 or >0.90): strict `min(Q_one, Q_two)` — no c=3.0 safety net
- **Q chain**: Q_one -> Q_two -> Q_min -> Q_normal -> Q_epoch -> Q_final
- **Sampling**: 10,080 one-minute samples per weekly epoch, minimum payout $1
- **Distribution**: Daily at midnight UTC

### Reward Pools (April 2026)
| Sport | Pool/Game | Notes |
|-------|-----------|-------|
| Champions League QF | $24,000 | Highest pool, 3-day window |
| EPL | $10,000 | Weekend-heavy |
| NBA | $7,700 | Frequent events, high adverse selection |
| CS2 A-Tier | $5,500 | Lighter competition |
| IPL Cricket | $4,500 | Emerging market |
| UFC Main Card | $4,250 | Short event window |
| MLB | $1,650 | Low pool, skip unless competition minimal |
| NHL | $1,500 | Low pool |

### Infrastructure
- **CLOB REST**: `https://clob.polymarket.com`
- **Market WS**: `wss://ws-subscriptions-clob.polymarket.com/ws/market`
- **User WS**: `wss://ws-subscriptions-clob.polymarket.com/ws/user`
- **Sports WS**: `wss://sports-api.polymarket.com/ws`
- **RTDS WS**: `wss://ws-live-data.polymarket.com`
- **Auth**: EIP-712 (L1) -> HMAC-SHA256 (L2), Signature Type 2 (GNOSIS_SAFE)
- **Fees**: Makers 0%, takers 1.5% (crypto) / 0.3% (sports). Fee formula: `fee = C * feeRate * p * (1-p)`
- **Heartbeat**: 10-second window with 5-second buffer. Miss = ALL orders cancelled.
- **Rate limits**: POST /order 3,500/10s burst; POST /orders (batch, 15/req) 1,000/10s = 15,000 effective; DELETE /order 3,000/10s; DELETE /cancel-all 250/10s
- **Tuesday restart**: 7:00 AM ET, ~90s downtime, HTTP 425 (Too Early)
- **Post-Only orders**: Guaranteed maker status (0% fees), rejected if would cross spread
- **GTD minimum**: 60 seconds (`expiration = now + 60 + N`)

### Smart Contracts (Polygon)
| Contract | Address |
|----------|---------|
| CTF Exchange | `0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E` |
| Neg Risk CTF Exchange | `0xC5d563A36AE78145C45a50134d48A1215220f80a` |
| Neg Risk Adapter | `0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296` |
| Conditional Tokens (CTF) | `0x4D97DCd97eC945f40cF65F87097ACe5EA0476045` |
| USDC.e | `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174` |
| UMA Adapter | `0x6A9D222616C90FcA5754cd1333cFD9b7fb6a4F74` |
| UMA Optimistic Oracle | `0xCB1822859cEF82Cd2Eb4E6276C7916e692995130` |
| Gnosis Safe Factory | `0xaacfeea03eb1561c4e67d661e40682bd20e3541b` |
| Polymarket Proxy Factory | `0xaB45c5A4B0c941a2F231C04C3f49182e1A254052` |

### Risk Management Defaults (ImMike config)
- `maker_fee_bps: 0` / `taker_fee_bps: 150`
- `estimated_gas_per_order: 0.02` (~$0.02 on Polygon)
- `slippage_tolerance: 0.02` (2% for arb, use 1% for market making)
- `max_retries: 3` / `retry_delay_seconds: 1`
- `heartbeat_interval: 30` (bot internal, NOT Polymarket heartbeat)
- `mm_enabled: false` — "markets too efficient"

### Genius Context
Full extraction intelligence: [genius.md](genius.md) — 21 patterns, 13 hidden knowledge items, 7 signature moves, quality rubric, worked examples, API details

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

3 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Polymarket Market Maker — Adverse Selection Defense Configuration** — `skills/prediction-market-making/references/prompts-v2/adverse-selection-defense-config.md`
- **Polymarket Market Maker — Market Selection & Deployment Plan** — `skills/prediction-market-making/references/prompts-v2/market-selection-deployment-plan.md`
- **Polymarket Market Maker — Reward Optimization Tuning Report** — `skills/prediction-market-making/references/prompts-v2/reward-optimization-tuning-report.md`

<!-- END:execution-prompts -->
