---
description: "Scan active Polymarket sports/event markets against professional sportsbook odds to identify price gaps exceeding fee drag. Outputs a ranked opportunity list with implied probability gaps, confidence levels, and action recommendations."
---

# Odds Discrepancy Scanner

> **Crown Jewel 1** — From GP-1 (Vegas Anchor), HK-1 (Why Sports), HK-8 (Gambot Principle), SM-1 (Line Movement Detector), SM-5 (Gap Explanation Protocol)

## Purpose

Identify markets where Polymarket price deviates from sportsbook-implied true probability by enough to survive fee drag, slippage, and the paper-to-live haircut. This is sovereign2013's core edge: not predicting outcomes, but detecting when Polymarket is wrong relative to Vegas.

---

## Prerequisites

Before running this workflow, you need:

1. **Active Polymarket sports markets** — current YES/NO prices for each market
2. **Corresponding sportsbook odds** — preferably from Pinnacle (sharpest book, lowest vig). DraftKings/FanDuel acceptable as secondary reference but less reliable due to higher margins and sharp bettor limits
3. **Current bankroll figure** — for position sizing calculations
4. **Active positions list** — for correlation checking

If you don't have sportsbook odds yet: use The Odds API (free tier), OddsJam, or manually pull from Pinnacle.com. Always prefer Pinnacle over other books.

---

## Step 1: Convert Sportsbook Odds to True Probabilities

For each sportsbook line, strip the vig to get true implied probability.

### American Odds Conversion

**Negative odds** (favorite): Implied% = |odds| / (|odds| + 100)
**Positive odds** (underdog): Implied% = 100 / (odds + 100)

### Vig Stripping

Both sides will sum to >100% (the overround). Normalize:

```
True_Prob_A = Raw_Implied_A / (Raw_Implied_A + Raw_Implied_B)
True_Prob_B = Raw_Implied_B / (Raw_Implied_A + Raw_Implied_B)
```

**Example**: Pinnacle Lakers -150 / Opponents +130
- Raw implied: 60% / 43.5% = 103.5% total (3.5% vig)
- Stripped: 60/103.5 = 57.97% and 43.5/103.5 = 42.03%
- These are the reference probabilities

### Why Pinnacle

Pinnacle runs 2-3% vig on major sports and accepts sharp bettors without limiting them. Their lines most closely approximate true probabilities. DraftKings/FanDuel run higher margins and limit sharps, making lines less reliable as truth. If Pinnacle unavailable, average across 3+ sharp books.

---

## Step 2: Pull Polymarket Current Prices

For each corresponding market, record:
- Current YES price (= implied probability in cents)
- Current NO price
- 24h volume
- Order book depth (if available)
- Time to event resolution

### Data Integrity Checks (MUST PASS)

- [ ] Polymarket price is current (within last 60 seconds)
- [ ] Sportsbook odds are current (within last 5 minutes)
- [ ] Both prices reference the SAME event with SAME rules (overtime included? extra innings?)
- [ ] No known data feed issues or exchange outages

**If any check fails**: Flag the market as DATA ISSUE and skip. Do not trade on stale or mismatched data.

### Negation Pair Check

YES + NO should sum to ~$1.00. If they sum to less than $0.97 or more than $1.03, flag as potential arbitrage or pricing anomaly. Pure negation pair arbitrage is nearly exhausted by 2026, but significant deviations still signal market dysfunction worth investigating.

---

## Step 3: Calculate Raw Gap

For each market:

```
Raw_Gap = Sportsbook_True_Prob - Polymarket_Implied_Prob
```

Positive gap = Polymarket is underpricing (BUY YES opportunity)
Negative gap = Polymarket is overpricing (BUY NO opportunity)

---

## Step 4: Apply Fee Drag

### Fee Schedule

| Market Type | Taker Fee | Maker Fee | Rotation Cost (entry + exit) |
|-------------|-----------|-----------|------------------------------|
| Sports | 0.75% | 0% (may not fill) | 1.5% |
| Non-sports | 2% | 0% (may not fill) | 4% |

### Slippage Estimate

Based on market liquidity:
- High volume (>$100K daily): +0.5-1% slippage
- Medium volume ($10K-$100K): +1-3% slippage
- Low volume (<$10K): +3-5% slippage

### Net Edge Calculation

```
Fee_Drag = Entry_Fee + Exit_Fee (if rotating) or Entry_Fee only (if holding to resolution)
Slippage = estimate from volume tier
Net_Edge = Raw_Gap - Fee_Drag - Slippage
```

**Critical threshold**: Net edge must exceed 2% after ALL costs to be actionable. Below 2%, the edge is within noise range and doesn't survive the paper-to-live haircut (GP-3).

---

## Step 5: Apply Paper-to-Live Haircut

Even after fee and slippage adjustments, multiply remaining edge by 0.5-0.7:

```
Realistic_Edge = Net_Edge * 0.6  (midpoint of 0.5-0.7 range)
```

If Realistic_Edge < 1%, this market is NOT worth trading. The paper-to-live gap will consume it.

---

## Step 6: Classify the Gap

For each market with surviving edge, explain WHY the gap exists. **Never trade an unexplained gap.**

| Explanation | Classification | Action |
|-------------|---------------|--------|
| **Information asymmetry**: Sportsbook has info Polymarket doesn't (line moved on injury, sharp money) | VALID EDGE | EXECUTE |
| **Narrative mispricing**: Public sentiment inflating/deflating (big-name team overvalued) | VALID EDGE | EXECUTE (may correct fast) |
| **Low liquidity**: Stale price, thin order book | VALID BUT FRAGILE | EXECUTE CAREFULLY (your order IS the move) |
| **Data error**: Feed lag, wrong odds, different event | INVALID | DO NOT TRADE — verify first |
| **Structural difference**: Different rules (overtime, extra innings) | INVALID | DO NOT TRADE — comparing different products |
| **Unknown**: Can't explain the gap | TREAT AS INVALID | DO NOT TRADE until explained |

### Line Movement Context

Check if the sportsbook line has moved in the last 2 hours. A moving line is a signal:
- **Line moved toward your position**: Sharp money agrees. Higher confidence.
- **Line moved against your position**: Something may be happening you don't know about. Investigate before trading.
- **Line stable for 12+ hours**: Polymarket gap likely reflects persistent retail mispricing. Standard edge.

---

## Step 7: Preliminary Position Sizing

For markets that pass all checks:

```
Edge = Realistic_Edge (from Step 5)
Kelly_Fraction = Edge / (1 - Market_Price)
Quarter_Kelly = 0.25 * Kelly_Fraction * Bankroll
Position = min(Quarter_Kelly, 0.05 * Bankroll)
```

Check correlation: if other active positions cover the same sport/date/league, total correlated exposure must stay under 15% of bankroll.

---

## Step 8: Assign Confidence and Action

### Confidence Levels

| Level | Criteria |
|-------|----------|
| **HIGH** | Net edge > 5% after all costs, gap explained by information asymmetry or narrative mispricing, multiple sportsbooks confirm |
| **MEDIUM** | Net edge 2-5%, gap exists but explanation has some uncertainty, or only one sportsbook reference |
| **LOW** | Net edge 1-2%, within noise range, or gap classification is LOW LIQUIDITY |
| **SKIP** | Net edge < 1%, or gap explained by structural difference/data error/unknown |

### Action Recommendations

| Action | When |
|--------|------|
| **EXECUTE** | HIGH confidence, net edge > 3% after all adjustments |
| **INVESTIGATE** | MEDIUM confidence — route to Multi-Model Ensemble workflow for deeper analysis |
| **MONITOR** | Edge exists but too thin or timing not optimal (>48h to event) |
| **SKIP** | No actionable edge, or gap is invalid |

### Suspicious Flag

If any market shows >10% raw gap, flag as SUSPICIOUS. Investigate whether it's a data error, structural difference, or genuine extreme mispricing BEFORE recommending action. Extreme gaps are more often errors than opportunities.

---

## Output Format

```
ODDS DISCREPANCY SCAN
Scan time: [timestamp]
Markets scanned: [N]
Sportsbook reference: [Pinnacle / DraftKings / etc.]
Bankroll: $[X]
Active positions: [list or "none"]

OPPORTUNITIES (ranked by realistic edge, highest first):

| # | Market | Book Implied | Poly Price | Raw Gap | Fee+Slip | Net Edge | Realistic Edge (0.6x) | Confidence | Gap Type | Action |
|---|--------|-------------|-----------|---------|----------|----------|----------------------|------------|----------|--------|
| 1 | [name] | [X]% | $[X] ([X]%) | [X]% | [X]% | [X]% | [X]% | HIGH/MED/LOW | [type] | EXECUTE/INVESTIGATE/MONITOR/SKIP |

POSITION SIZING (for EXECUTE recommendations only):

| Market | Realistic Edge | Quarter-Kelly | Position Cap (5%) | Recommended Size | Correlated? |
|--------|---------------|---------------|-------------------|-----------------|-------------|

ALERTS:
- [Any SUSPICIOUS flags]
- [Any DATA ISSUE flags]
- [Correlation warnings]
- [Circuit breaker status]

TIMING CONTEXT:
| Market | Time to Event | Timing Posture |
|--------|--------------|----------------|
(per SM-6 timing matrix: >48h = monitor, 24-48h = scan, 6-24h = primary window, 1-6h = peak, <1h = exit)

NEXT ACTIONS:
1. [EXECUTE markets — proceed to Edge Validation workflow]
2. [INVESTIGATE markets — proceed to Multi-Model Ensemble workflow]
3. [MONITOR markets — set alerts for price movement]
```

---

## Quality Gate

- Does every opportunity carry a quantified sportsbook reference (not a narrative claim like "I think X will win")?
- Was the 0.6x paper-to-live haircut applied before any confidence/action was assigned?
- Does every EXECUTE/INVESTIGATE market have an explicit, non-"unknown" gap classification?
- Were fee drag and slippage both calculated (not estimated as zero or skipped)?
- Are correlated positions checked against the 15% cap before position sizing is shown?
- Is any market with a raw gap >10% flagged SUSPICIOUS rather than reported as a clean opportunity?
- Does the opportunities table include every scanned market, including SKIPs — no market silently dropped?

---

## Workflow Chaining

- Markets flagged **EXECUTE** -> Route to `edge-validation-sizing.md` for full validation before capital deployment
- Markets flagged **INVESTIGATE** -> Route to `multi-model-ensemble.md` for deeper probability analysis, then back to edge validation if ensemble confirms edge
- Markets flagged **MONITOR** -> Re-scan in next cycle, escalate if edge persists or widens

## Anti-Patterns (What NOT to Do)

1. **Do not trade without a reference price.** "I think the Lakers will win" is not an edge. "Pinnacle prices Lakers at 62% and Polymarket prices them at 55%" is an edge.
2. **Do not trade unexplained gaps.** Unknown gaps are traps more often than opportunities.
3. **Do not assume paper edge = live edge.** The 0.6x haircut is mandatory.
4. **Do not skip fee calculation.** A 2% edge minus 1.56% fees minus slippage = negative expected value.
5. **Do not ignore correlation.** Five NBA games on the same night are correlated. Cap exposure.
6. **Do not trade stale data.** Both prices must be current. Even 5-minute-old sportsbook odds can be dangerously stale near tip-off.

---

## Example Scan Output

```
ODDS DISCREPANCY SCAN
Scan time: 2026-04-13 18:30 UTC
Markets scanned: 12
Sportsbook reference: Pinnacle
Bankroll: $10,000
Active positions: none

| # | Market | Book Impl | Poly Price | Raw Gap | Fee+Slip | Net Edge | Real Edge | Conf | Gap Type | Action |
|---|--------|----------|-----------|---------|----------|----------|-----------|------|----------|--------|
| 1 | Utah State vs Arizona | 44.2% | $0.38 (38%) | 6.2% | 2.5% | 3.7% | 2.2% | HIGH | Info asymmetry | EXECUTE |
| 2 | Lakers vs Celtics G3 | 62.3% | $0.55 (55%) | 7.3% | 2.0% | 5.3% | 3.2% | HIGH | Info asymmetry | EXECUTE |
| 3 | Warriors vs Heat | 48.1% | $0.46 (46%) | 2.1% | 2.0% | 0.1% | 0.1% | SKIP | Below threshold | SKIP |
| 4 | Chiefs vs Eagles SB | 52.0% | $0.59 (59%) | -7.0% | 2.0% | -9.0% | n/a | MED | Narrative misprice | INVESTIGATE |

POSITION SIZING:
| Utah State vs Arizona | 2.2% | $89 (qK) | $500 (5%) | $89 | No |
| Lakers vs Celtics G3 | 3.2% | $178 (qK) | $500 (5%) | $178 | No |

ALERTS:
- Chiefs vs Eagles shows Polymarket OVERPRICED vs Pinnacle by 7%. Route to Ensemble for BUY NO analysis.

NEXT ACTIONS:
1. Route Utah State + Lakers to Edge Validation workflow
2. Route Chiefs vs Eagles to Multi-Model Ensemble
3. Re-scan in 30 minutes for new markets
```
