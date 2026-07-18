---
description: "Run independent analysis through 3 weighted perspectives (analytical 40%, credibility 35%, contrarian 25%), aggregate via Bayesian mixture with 30% market weight, output probability estimate with confidence, disagreement analysis, and trade recommendation."
---

# Multi-Model Ensemble Forecast

> **Crown Jewel 2** — From GP-2 (Ensemble Independence), GP-5 (Bayesian Swarm 70/30), GP-11 (Hallucination-Correlation Risk), HK-2 (Why Claude at 35%), SM-2 (Ensemble Credibility Arbiter)

## Purpose

For markets where a clean sportsbook reference price doesn't exist (political events, economic indicators, complex multi-factor outcomes) or where the Odds Discrepancy Scanner flagged a market as INVESTIGATE, this workflow generates a calibrated probability estimate by running three independent analytical perspectives and aggregating them with Bayesian market integration.

This is the PolySwarm-inspired approach adapted for single-operator use: instead of 50 LLM personas, we use 3 distinct analytical frames that map to the strengths of GPT-4o (40%), Claude (35%), and Gemini (25%). The independence requirement is absolute — each perspective must be generated without knowledge of the others.

---

## When to Use This Workflow

| Scenario | Use Ensemble? |
|----------|--------------|
| Sports market with clear sportsbook reference | NO — use Odds Discrepancy Scanner. Sportsbook is a better reference than any ensemble. |
| Sports market where sportsbook lines are stale or unavailable | YES — ensemble provides probability estimate as substitute reference. |
| Political/election market | YES — no clean reference price exists. Ensemble is primary tool. |
| Economic indicator market (GDP, employment, inflation) | YES — economic models are noisy. Ensemble triangulates. |
| Complex event (merger approval, regulatory decision, geopolitical) | YES — these require credibility evaluation and contrarian analysis. |
| Odds Scanner flagged INVESTIGATE | YES — ensemble provides deeper analysis to resolve ambiguity. |

---

## Prerequisites

1. **Market question** — exact phrasing from Polymarket (resolution criteria matter)
2. **Current market price** — Polymarket YES price (= implied probability)
3. **Relevant context** — any data, news, reports that inform the probability
4. **Resolution criteria** — exact conditions under which YES/NO resolves (critical for avoiding structural mismatches)

---

## Step 1: Define the Question Precisely

Before running any perspective, lock down exactly what is being evaluated:

```
MARKET QUESTION: [exact Polymarket phrasing]
RESOLUTION SOURCE: [who/what determines the outcome]
RESOLUTION DATE: [when]
RESOLUTION CRITERIA: [exact conditions for YES vs NO]
CURRENT PRICE: $[X] ([X]% implied probability)
```

**Critical**: Ensure all three perspectives evaluate the SAME question with the SAME resolution criteria. A common failure mode is one perspective interpreting the question differently than the others.

---

## Step 2: Perspective 1 — Analytical (Weight: 40%)

This perspective maps to GPT-4o's strength: broad analytical reasoning and statistical pattern recognition.

### Instructions

Analyze using ONLY:
- Statistical reasoning and base rates
- Historical reference classes (how often has this type of event occurred?)
- Quantitative data (polls, economic indicators, betting markets, statistical models)
- Mathematical relationships between variables

### Do NOT Consider (Save for Other Perspectives)
- Source credibility or information quality
- Contrarian angles or consensus challenges
- Narrative or sentiment

### Output Required

```
PERSPECTIVE 1 — ANALYTICAL (40%)
Probability: [X]%
Confidence: [1-10]
Reference class: [what historical data informs this]
Key data points: [2-3 most relevant numbers]
Reasoning: [2 sentences maximum — what the numbers say]
Key assumption: [single most important assumption, stated explicitly]
```

### Confidence Calibration

| Confidence | Meaning |
|------------|---------|
| 9-10 | Strong historical base rate with large sample, current data aligns |
| 7-8 | Reasonable base rate with moderate sample, some uncertainty |
| 5-6 | Limited historical precedent, must extrapolate |
| 3-4 | Very limited data, estimate is largely uncertain |
| 1-2 | Essentially guessing — no meaningful statistical foundation |

---

## Step 3: Perspective 2 — Credibility (Weight: 35%)

This perspective maps to Claude's strength: source credibility evaluation and nuanced reasoning under uncertainty.

### Instructions

Evaluate the INFORMATION LANDSCAPE:
- Which sources are reporting on this? Primary vs secondary vs derivative?
- Which sources have track records of accuracy in this specific domain?
- Is there information asymmetry? Do some participants know things others don't?
- Are insiders trading? (Large position changes without public catalyst = insider signal)
- When one journalist reports something and three others repeat it, that's 1 source, not 4.

### The Credibility Stack

| Source Type | Reliability | Weight |
|-------------|------------|--------|
| Primary data (official statistics, filings, confirmed quotes) | Highest | Anchor estimate here |
| Expert analysis with disclosed methodology | High | Adjust from anchor |
| Journalistic reporting (named sources) | Medium-High | Cross-reference |
| Journalistic reporting (unnamed sources) | Medium | Discount by 30% |
| Social media / pundit commentary | Low | Treat as sentiment signal, not information |
| Prediction market price itself | Medium | Already embedded in P_market (don't double-count) |

### Output Required

```
PERSPECTIVE 2 — CREDIBILITY (35%)
Probability: [X]%
Confidence: [1-10]
Primary sources identified: [N] (vs [N] derivative/secondary)
Information asymmetry: [YES/NO — who knows what others don't?]
Insider signal: [detected/not detected — basis for assessment]
Reasoning: [2 sentences — which sources to trust and why]
Key assumption: [single most important assumption]
```

### Why This Perspective at 35%

In event markets with information asymmetry — injury reports, insider leaks, conflicting sources — the critical question is not "what does the data say?" but "which data should we trust?" Claude identifies when a 3:1 ratio of sources is actually 1:0 real sources. This distinction can flip a probability estimate.

---

## Step 4: Perspective 3 — Contrarian (Weight: 25%)

This perspective maps to Gemini's strength: contrarian analysis and alternative data interpretation.

### Instructions

Challenge the likely consensus:
- What is the consensus missing?
- What scenario would make the consensus wrong?
- What information is being underweighted or overweighted?
- What second-order effects are being ignored?
- What has changed recently that historical base rates don't capture?
- Is the market in a bubble (everyone agrees for social reasons, not informational ones)?

### The Contrarian Checklist

- [ ] Is there a narrative driving price more than fundamentals?
- [ ] Has a recent salient event anchored people to an incorrect reference point?
- [ ] Are people extrapolating a short trend into a long trend?
- [ ] Is there a structural reason the market might be wrong (participant composition, liquidity)?
- [ ] What would surprise the consensus? How likely is that surprise?

### Output Required

```
PERSPECTIVE 3 — CONTRARIAN (25%)
Probability: [X]%
Confidence: [1-10]
Consensus challenge: [what the majority is getting wrong]
Surprise scenario: [what outcome would shock the consensus]
Surprise probability: [X]% (how likely is the surprise)
Reasoning: [2 sentences — the strongest argument against consensus]
Key assumption: [single most important assumption]
```

### When to Weight Contrarian Higher

If the contrarian perspective identifies a concrete, verifiable catalyst that others are ignoring (not just "anything could happen"), and confidence is 7+, consider weighting it at 30% and reducing analytical to 35%. This is a judgment call, not automatic.

---

## Step 5: Independence Verification

**BEFORE aggregating, verify independence.**

The single biggest threat to ensemble quality is contamination between perspectives. Check:

- [ ] Perspective 1 was generated without reference to Perspectives 2 or 3
- [ ] Perspective 2 was generated without reference to Perspectives 1 or 3
- [ ] Perspective 3 was generated without reference to Perspectives 1 or 2
- [ ] No perspective's reasoning mentions another perspective's conclusion
- [ ] Each perspective's key assumption is different

If running this in a single Claude session (common case), enforce independence by completing each perspective fully before moving to the next. Do not revise an earlier perspective based on a later one.

---

## Step 6: Aggregation

### Weighted Ensemble Average

```
P_ensemble = 0.40 * P1 + 0.35 * P2 + 0.25 * P3
```

### Market Integration (Bayesian Mixture)

```
P_final = 0.70 * P_ensemble + 0.30 * P_market
```

**Why 70/30**: The market price contains information the ensemble doesn't — other traders, other bots, insider knowledge. Ignoring it is arrogant. But deferring entirely means you can never find edge. 70/30 respects the market while asserting informational advantage.

### Disagreement Analysis

```
Disagreement = max(P1, P2, P3) - min(P1, P2, P3)
```

| Disagreement | Interpretation | Action |
|-------------|---------------|--------|
| < 5 points | LOW — perspectives converge | High confidence in ensemble. Proceed. |
| 5-15 points | MEDIUM — meaningful divergence | Investigate the dissent. Which perspective is the outlier and why? |
| > 15 points | HIGH — fundamental disagreement | NO TRADE unless the disagreement can be resolved. High disagreement = high uncertainty = unquantifiable edge. |

### Disagreement Triage (SM-2)

When perspectives diverge, the NATURE of the disagreement matters:

| Outlier | Likely Because | Resolution |
|---------|---------------|------------|
| P1 (Analytical) dissents | Data conflicts with credibility/contrarian | Check if the data is correct. If data is solid, weight P1 higher. |
| P2 (Credibility) dissents | Sources unreliable or asymmetric | Investigate source quality. If credibility concern is valid, weight P2 higher. |
| P3 (Contrarian) dissents | Consensus is missing something | Verify the contrarian catalyst. If it's concrete and verifiable, weight P3 higher. If it's abstract ("anything could happen"), maintain standard weights. |

---

## Step 7: Hallucination Check (GP-11)

Before finalizing, run a factual verification pass:

- [ ] All factual claims in all three perspectives are verifiable
- [ ] No statistics were cited without a source
- [ ] No events were referenced that may not have happened
- [ ] Team records, player stats, poll numbers, economic data are confirmed against authoritative sources

**The ensemble evaluates probability. Deterministic code verifies facts.** If any factual claim cannot be verified, flag it and adjust confidence downward.

Common hallucination patterns in prediction market analysis:
- Inventing player injury status
- Misremembering team records or historical outcomes
- Citing polls that don't exist
- Confusing similar events from different years

---

## Step 8: Edge Calculation

```
Edge_vs_Market = P_final - P_market (in percentage points)
```

### Fee Adjustment

```
For sports: Fee_Drag = 1.5% (round trip) + slippage estimate
For non-sports: Fee_Drag = 4.0% (round trip) + slippage estimate

Net_Edge = Edge_vs_Market - Fee_Drag
Realistic_Edge = Net_Edge * Haircut (0.5-0.7, per GP-3)
```

---

## Step 9: Trade Recommendation

| Condition | Recommendation |
|-----------|---------------|
| Realistic edge > 3% AND disagreement LOW | **TRADE** — proceed to Edge Validation workflow |
| Realistic edge > 3% AND disagreement MEDIUM | **TRADE WITH CAUTION** — reduced position (50% of Kelly) |
| Realistic edge 1-3% AND disagreement LOW | **MARGINAL** — only trade if other factors (timing, gap explanation) are strong |
| Realistic edge > 3% AND disagreement HIGH | **PASS** — edge exists but confidence is too low. Monitor for convergence. |
| Realistic edge < 1% | **PASS** — no actionable edge |
| Any condition with unresolved hallucination flag | **PASS** — factual foundation uncertain |

---

## Output Format

```
MULTI-MODEL ENSEMBLE FORECAST
==============================

MARKET: [exact Polymarket question]
CURRENT PRICE: $[X] ([X]% implied)
RESOLUTION: [date] via [source]

PERSPECTIVE 1 — ANALYTICAL (40%): [X]% | Confidence: [X]/10
  Reference class: [class]
  Reasoning: [2 sentences]
  Assumption: [key assumption]

PERSPECTIVE 2 — CREDIBILITY (35%): [X]% | Confidence: [X]/10
  Primary sources: [N] of [N total]
  Reasoning: [2 sentences]
  Assumption: [key assumption]

PERSPECTIVE 3 — CONTRARIAN (25%): [X]% | Confidence: [X]/10
  Challenge: [what consensus misses]
  Reasoning: [2 sentences]
  Assumption: [key assumption]

AGGREGATION:
  P_ensemble: [X]% (0.40 * [P1] + 0.35 * [P2] + 0.25 * [P3])
  P_final:    [X]% (0.70 * P_ensemble + 0.30 * P_market)
  
DISAGREEMENT: [X] points ([LOW/MEDIUM/HIGH])
  Outlier: Perspective [N] — [why it diverges]
  Resolution: [which perspective to trust more and why]

HALLUCINATION CHECK: [CLEAR / FLAGGED — detail]

EDGE ANALYSIS:
  Edge vs market:    [X] percentage points
  Fee drag:          [X]%
  Net edge:          [X]%
  Realistic edge:    [X]% (after [X]x haircut)

RECOMMENDATION: [TRADE / TRADE WITH CAUTION / MARGINAL / PASS]
  Direction: [BUY YES / BUY NO / NO TRADE]
  If TRADE: Route to Edge Validation workflow with P_final as reference price
  Reason: [1-2 sentences]

CONFIDENCE SUMMARY:
  Avg perspective confidence: [X]/10
  Ensemble reliability: [HIGH/MEDIUM/LOW] based on disagreement + hallucination check
  Overall conviction: [1-10]
```

---

## Example: Political Market

```
MULTI-MODEL ENSEMBLE FORECAST
==============================

MARKET: Will the Federal Reserve cut rates at the June 2026 FOMC meeting?
CURRENT PRICE: $0.62 (62% implied)
RESOLUTION: June 18, 2026 via Federal Reserve press release

PERSPECTIVE 1 — ANALYTICAL (40%): 55% | Confidence: 7/10
  Reference class: In 14 rate-cutting cycles since 1970, Fed cut at 78% of meetings once 
  a cycle started. But current cycle has only 1 cut so far — early cycles pause 40% of the time.
  Reasoning: Core PCE at 2.7% and unemployment at 4.1% create a mixed signal. Historical 
  base rate for cutting with these indicators is ~55% per meeting.
  Assumption: No major economic shock before June.

PERSPECTIVE 2 — CREDIBILITY (35%): 52% | Confidence: 6/10
  Primary sources: 2 (Fed minutes, Governors' speeches) of 8 total analyzed
  Reasoning: Fed minutes show "several participants" favored holding in April. Two 
  Governors gave hawkish speeches last week — these are primary signals. CME FedWatch 
  and pundit commentary are derivative, not additive.
  Assumption: Recent Governor speeches reflect current FOMC consensus.

PERSPECTIVE 3 — CONTRARIAN (25%): 45% | Confidence: 5/10
  Challenge: Market is pricing in a cut based on 2025 pattern-matching. But 2026 
  inflation dynamics are different — services inflation is stickier than expected.
  Reasoning: If April jobs report (May 3) comes in hot, the 62% market price will 
  look absurd in retrospect. Market is underweighting the sticky-services scenario.
  Assumption: April jobs report will show continued labor market tightness.

AGGREGATION:
  P_ensemble: 51.6% (0.40 * 55 + 0.35 * 52 + 0.25 * 45)
  P_final:    54.7% (0.70 * 51.6 + 0.30 * 62)
  
DISAGREEMENT: 10 points (MEDIUM)
  Outlier: Perspective 3 (Contrarian) at 45% vs 52-55% consensus
  Resolution: Contrarian raises a valid concern (sticky services) but the catalyst 
  (April jobs report) hasn't materialized yet. Maintain standard weights until data arrives.

HALLUCINATION CHECK: CLEAR
  Core PCE 2.7% verified via BLS. Unemployment 4.1% verified. Fed minutes language 
  cross-referenced. Governor speeches confirmed.

EDGE ANALYSIS:
  Edge vs market:    -7.3 percentage points (market overpriced at 62% vs our 54.7%)
  Fee drag:          4.5% (non-sports 4% round trip + 0.5% slippage)
  Net edge:          2.8%
  Realistic edge:    1.5% (after 0.55x haircut)

RECOMMENDATION: MARGINAL
  Direction: BUY NO at $0.38 (if edge were larger)
  Route to Edge Validation if edge widens after April jobs report
  Reason: 1.5% realistic edge is below the 2% threshold. The contrarian perspective 
  identifies a concrete catalyst (April jobs report May 3) that could widen the gap. 
  Set alert to re-run ensemble after that data release.

CONFIDENCE SUMMARY:
  Avg perspective confidence: 6.0/10
  Ensemble reliability: MEDIUM (10-point disagreement, all facts verified)
  Overall conviction: 5/10
```

---

## Example: Sports Market (Supplementing Scanner)

```
MULTI-MODEL ENSEMBLE FORECAST
==============================

MARKET: Will the Chiefs win Super Bowl LXI?
CURRENT PRICE: $0.59 (59% implied)
RESOLUTION: February 2027 via NFL game result

PERSPECTIVE 1 — ANALYTICAL (40%): 48% | Confidence: 6/10
  Reference class: No team has won 4 consecutive Super Bowls. Dynasty teams average 
  38% championship probability in year 4. Current odds imply regression is underpriced.
  Reasoning: ELO rating gives Chiefs 12% edge over field, but 59% market price implies 
  much stronger. Historical base rate caps repeat champions at ~35-45% range.
  Assumption: Current roster largely intact through February 2027.

PERSPECTIVE 2 — CREDIBILITY (35%): 52% | Confidence: 7/10
  Primary sources: 3 (Vegas futures consensus, advanced metrics, roster analysis)
  Reasoning: Pinnacle futures at -110 imply 52.4% after vig strip. Sharp money has been 
  flat — no insider accumulation. The 59% Polymarket price exceeds sharp consensus by 7 points.
  Assumption: Pinnacle line reflects professional assessment accurately.

PERSPECTIVE 3 — CONTRARIAN (25%): 42% | Confidence: 5/10
  Challenge: Dynasty narratives create betting premiums that persist beyond analytical 
  justification. The 59% includes "dynasty tax" — people betting on the story, not the stats.
  Reasoning: Key coaching coordinator left in offseason. Historically, coordinator departures 
  reduce championship probability by 5-8 points in year 1. Market hasn't priced this.
  Assumption: Coordinator departure impact is real and not yet compensated.

AGGREGATION:
  P_ensemble: 48.1% (0.40 * 48 + 0.35 * 52 + 0.25 * 42)
  P_final:    51.4% (0.70 * 48.1 + 0.30 * 59)
  
DISAGREEMENT: 10 points (MEDIUM)
  Outlier: Perspective 3 at 42% — concrete catalyst (coordinator departure)
  Resolution: Coordinator departure is verifiable and historically impactful. 
  But timing is too early (>48h rule amplified — months out). Standard weights held.

HALLUCINATION CHECK: CLEAR
  Coordinator departure confirmed via team press release. Pinnacle line verified.

EDGE ANALYSIS:
  Edge vs market:    -7.6 points (market overpriced — BUY NO side)
  Fee drag:          2.5% (sports 1.5% + 1.0% slippage)
  Net edge:          5.1%
  Realistic edge:    3.1% (0.6x haircut)

RECOMMENDATION: TRADE WITH CAUTION
  Direction: BUY NO at $0.41
  Route to Edge Validation workflow with P_final (51.4%) as reference
  Reason: 3.1% realistic edge with verifiable gap explanation (dynasty tax + 
  coordinator departure). BUT timing is suboptimal — months to resolution means 
  edge may expand or close. Enter with 50% position, scale if edge persists.

CONFIDENCE SUMMARY:
  Avg perspective confidence: 6.0/10
  Ensemble reliability: MEDIUM (verified facts, moderate disagreement)
  Overall conviction: 6/10
```

---

## Quality Gate

- Was each perspective generated without visible contamination from the other two (distinct assumptions, no cross-referencing)?
- Does the Credibility perspective actually count sources by independence (distinguishing "1 source repeated 3 times" from "4 independent sources"), not just cite a number?
- Does the Contrarian perspective name a specific, falsifiable scenario rather than a generic "things could change"?
- Was the hallucination check run and any unverifiable claim flagged, rather than assumed clean by default?
- Is the 30% market weight preserved in the final aggregation rather than overridden toward 100% ensemble?
- Does the recommendation match the stated edge/disagreement combination against the table (no HIGH-disagreement market recommended as TRADE)?

---

## Workflow Chaining

- **TRADE/TRADE WITH CAUTION**: Route to `edge-validation-sizing.md` with P_final as the reference probability. The ensemble output replaces sportsbook odds as the reference anchor for validation.
- **MARGINAL**: Set alerts for catalysts identified in the contrarian perspective. Re-run ensemble after catalyst materializes.
- **PASS**: Log the analysis. If market price moves >5 points toward your ensemble estimate, re-run — the market may be discovering what you found first.

## Anti-Patterns

1. **Do not let perspectives contaminate each other.** If you catch yourself adjusting P1 after seeing P2, you've broken independence. The ensemble is worthless without it.
2. **Do not use this workflow when a sportsbook reference exists.** Sportsbooks are better calibrated than any LLM ensemble. Use the scanner instead.
3. **Do not override the 30% market weight.** The temptation to go 100% ensemble ("I trust my analysis more than the market") is how the 92.4% lose money. The market knows things you don't.
4. **Do not trade on HIGH disagreement.** Three perspectives that fundamentally disagree means you don't understand the market well enough to have edge.
5. **Do not skip the hallucination check.** LLMs confidently invent facts. One hallucinated statistic can flip your entire probability estimate. Verify everything.
