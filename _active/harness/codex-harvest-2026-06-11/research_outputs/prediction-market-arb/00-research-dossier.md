# Prediction Market Trading: Research Dossier

**Compiled**: April 13, 2026
**Sources**: 3 parallel research agents, 9 web searches, 4 article extractions, 6 open-source repo analyses
**Purpose**: Knowledge foundation for Phase 0 agent/skill creation

---

## CRITICAL FINDING: Strategy Viability Has Shifted

The research uncovered a major correction to the plan:

| Strategy | Status (April 2026) | Why |
|---------|---------------------|-----|
| **Latency Arb (Crypto)** | DEAD | Polymarket introduced dynamic taker fees (~3.15% at 50c) that exceed the typical arb margin. The $515K/month bot went to zero overnight. |
| **AI Sports/Event Analysis** | HIGHEST CEILING | sovereign2013: $1→$3.3M. Methodology opaque but likely cross-references sportsbook odds vs. Polymarket prices using Claude for validation. |
| **Cross-Platform Arb** | MARGINAL | Round-trip costs 2.5-3.5%. Gross spreads >5% occur only 15-20% of the time. 78% of low-volume arb opportunities fail due to execution inefficiencies. |
| **Market Making** | VIABLE | $150-300/day per market. Polymarket distributes $5M+/month in liquidity rewards. Adverse selection is the primary risk. |
| **Weather/Niche** | BEST CURRENT OPPORTUNITY | Lowest competition, free data edge, small capital ($20-50 to start). $1K→$24K documented. Open-source bot available. |

**Recommended strategy mix (revised)**:
1. **Weather/Niche markets** — Start here. Lowest risk, proven edge, open-source codebase available
2. **AI Sports/Event Analysis** — Build toward this. Highest ceiling. Requires sportsbook odds API access
3. **Market Making** — Steady income layer. Requires $10K+ capital, adverse selection risk management
4. ~~Latency Arb~~ — Dead. Do not pursue.
5. **Cross-Platform Arb** — Supplementary only. Marginal after fees.

---

## Architecture: The Two-Layer Rule (Universal Pattern)

Every successful implementation separates LLM reasoning from trade execution:

```
Layer 1: Intelligence (Claude/LLM)
├── Market analysis and probability assessment
├── Contract matching and semantic parsing
├── News/event interpretation
├── Trade proposal generation
└── Post-trade reasoning and learning

Layer 2: Execution (Deterministic Code)
├── Order placement and management
├── Risk limit enforcement
├── Kill switch logic
├── Position tracking
└── Audit logging
```

**The LLM NEVER holds API keys or executes trades directly.** The LLM proposes; deterministic code validates and executes. This aligns perfectly with Antigravity's architecture (Layer 1 = You/orchestration, Layer 3 = execution scripts).

---

## Strategy Deep Dives

### Weather/Niche Markets (Priority 1)

**The hidden edge**: Every Polymarket weather market resolves on a specific airport weather station, NOT city center coordinates. Using city centers produces 3-8 degrees F error — fatal on 1-2 degree F bucket markets. Correct airport ICAO codes: KLGA (NYC), KDAL (Dallas — NOT DFW).

**Data sources** (all free):
- Open-Meteo API: ECMWF global + HRRR US hourly models (no key required)
- METAR Aviation Network: real-time airport station observations
- Visual Crossing: historical temperature validation
- api.weather.gov: NWS forecasts

**Open-source implementation**: `alteregoeth-ai/weatherbot` on GitHub — full pipeline from forecast aggregation to execution.

**Risk management config** (from weatherbot):
```json
{
  "balance": 10000.0, "max_bet": 20.0, "min_ev": 0.05,
  "max_price": 0.45, "min_volume": 2000, "min_hours": 2.0,
  "max_hours": 72.0, "kelly_fraction": 0.25,
  "max_slippage": 0.03, "scan_interval": 3600, "calibration_min": 30
}
```

**Self-calibration**: Bot stores per-city forecast accuracy. After 30+ samples, adjusts confidence scoring per city. The bot gets better at specific cities over time.

**Results**: $1K→$24K (London weather). Another: $65K profit across NYC, London, Seoul.

**Market volume**: Single weather markets clear $300K-$400K in 24-hour volume.

### AI Sports/Event Analysis (Priority 2)

**sovereign2013 profile**:
- $1 → $3.3M since August 2025
- 37,247 predictions (sports: NBA, college basketball, college football, ATP tennis)
- Daily gains: ~$144K, Weekly: ~$416K, Monthly: ~$1.54M
- Largest win: $1.73M on Utah State vs. Arizona Wildcats ($179K pure profit)
- Bets multiple times per minute

**Inferred strategy** (not publicly disclosed):
- Cross-references professional sportsbook odds (DraftKings, FanDuel, Pinnacle) against Polymarket prices
- Polymarket participants are less sophisticated than Vegas on sports
- Uses Claude to validate the edge before executing
- Kelly-style bankroll growth implies aggressive but disciplined position sizing

**Multi-model ensemble pattern** (from other documented bots):
- GPT-4o: 40% weight
- Claude 3.5 Sonnet: 35% weight
- Gemini 1.5 Pro: 25% weight
- Models forecast independently; results aggregated
- Claude's specific strength: source credibility evaluation

### Market Making (Priority 3)

**Polymarket rewards** (April 2026):
- $5M+/month distributed across sports and esports markets
- Scoring: S(v,s) = ((v-s)/v)^2 * b (quadratic — tighter spreads score exponentially better)
- Two-sided liquidity boosted; single-sided scores at 1/3 rate
- Sampled every minute across 10,080-sample epoch

**Per-game reward pools**: Champions League $24K, EPL $10K, NBA $7.7K, CS2 $5.5K, IPL Cricket $4.5K

**Realistic returns**: $150-300/day per market with $100K+ volume. Early: $200-300 USDC/day on $10K capital (now compressed).

**Adverse selection** (the primary killer): News moves a market 40-50 points instantly. If quoting 0.50/0.52 and market should be 0.90, stale offers get filled before you can cancel. Inventory limit: never >30% on one side.

---

## Technical Infrastructure

### Polymarket API
- **CLOB**: `https://clob.polymarket.com`
- **Gamma**: `https://gamma-api.polymarket.com` (market metadata)
- **WebSocket Market**: `wss://ws-subscriptions-clob.polymarket.com/ws/market`
- **WebSocket User**: `wss://ws-subscriptions-clob.polymarket.com/ws/user`
- **Auth**: EIP-712 signature (L1) → HMAC-SHA256 (L2). Signature type 2 (GNOSIS_SAFE) standard.
- **Rate limits**: 3,500 orders/10s burst, 1,500 market data reads/10s
- **Heartbeat required**: Missing heartbeats auto-cancel all orders
- **Fees**: Makers 0%. Takers variable by category. Maker rebates: 20-25% of taker fees, paid daily.

### Key Open-Source Repos

| Repo | Language | Best For | Production Ready? |
|------|----------|---------|------------------|
| `Polymarket/agents` | Python | Auth patterns, Gamma API client | No (execution commented out) |
| `warproxxx/poly-maker` | Python | WebSocket handling, order management, market making | Reference only (author says unprofitable) |
| `ImMike/polymarket-arbitrage` | Python | Risk management module, config pattern, cross-platform arb | Partial |
| `alteregoeth-ai/weatherbot` | Python | Full weather trading pipeline | Yes (documented $24K) |
| `CarlosIbCu/polymarket-kalshi-btc-arbitrage-bot` | Python+TS | Arb math, dashboard pattern | Detection only |
| `realfishsam/prediction-market-arbitrage-bot` | Node.js | Capital rotation logic, pmxt wrapper | Educational |

### Recommended Foundation
- **Trading infra**: poly-maker's WebSocket handling + order management
- **API layer**: polymarket-agents' auth setup + Gamma API client
- **Risk controls**: polymarket-arbitrage's risk manager + config pattern
- **Weather strategy**: Fork alteregoeth-ai/weatherbot directly
- **py-clob-client**: Use v0.28.0+ (not the older v0.17.5 from polymarket-agents)

---

## Tacit Knowledge (Hidden Patterns)

1. **Kelly fraction 0.25 is consensus** — Full Kelly too aggressive. Quarter-Kelly across all implementations.
2. **Capital rotation beats buy-and-hold** — Exit when spread closes, rotate to next opportunity. Dramatically improves annualized returns vs. holding to resolution.
3. **Paper-to-live gap is REAL** — One developer reported $20/minute paper gains becoming $130 net loss over five live sessions. Slippage and minimum size requirements destroy paper trading assumptions.
4. **Wallet must have done at least one manual trade** before API trading works (per poly-maker docs).
5. **92.4% of Polymarket wallets are unprofitable** — Only 7.6% profit. Top 20 profitable wallets: 14 are bots.
6. **Edge compression is measurable** — Latency arb windows: 12.3s (2024) → 2.7s (Q1 2026) → dead (dynamic fees killed it).
7. **Weather is the "quiet alpha"** — Airport coordinates, not city centers. Most competing bots get this wrong.
8. **MCP integration exists** — SimpleFunctions offers a 29-tool MCP server for Polymarket (15M free tokens/month). Tool: `get_world_state` returns 800-token digest of 9,706 markets.
9. **Heartbeat management is critical** — Missed heartbeats cancel ALL open orders. Must be architected in from day one.

---

## Risks Confirmed

1. **Dynamic fees can kill strategies overnight** — Happened to latency arb. Can happen to others.
2. **Adverse selection destroys market makers** — News events move markets before you can cancel stale orders.
3. **Paper-to-live gap** — Expect 30-50% performance degradation from paper to live.
4. **State-level regulatory uncertainty** — 11 states have cease-and-desist orders.
5. **Only 7.6% of wallets profit** — This is a competitive market, not free money.
