# Oracle Research Brief — 2026-08-06 (Gemini Deep Research, 52 sources, receipt REAL)

Full report + source list: `_active/knowledge/mastery-forge/01-research/deep-research-2026-08-06-full.md`. Confidence labels per source-backed claims; anything the projection engine adopts from here must be re-verified against live data before staking.

## 1. Where NBA prop edge lives in 2025-26 (VERIFIED against cited sources)

- **Line origination timing**: Bet365 posts props 30-60 min before DraftKings; early lines skew to season-long averages with no situational adjustment. First-mover window = ingest openers, model, hit before the market shapes.
- **Positional matchup blindspots**: books price vs aggregate team defense; models that isolate defense by position/play-type (e.g. vs pick-and-roll ball-handlers) find repeatable guard points/assists value.
- **Fourth-quarter pace compression**: books apply linear pace adjustments; close games decelerate late → systematic "under" value on scoring lines.
- **Rebounds/assists under-optimization**: lower-liability markets anchored to season averages with minimal matchup adjustment.
- **Injury usage-redistribution latency**: when a high-usage player sits, books lag on redistributing usage; absorption follows team hierarchy, not equal split — brief windows of deeply underpriced secondary-player props.
- Soft books run -115/-120 vig on props and accept looser pricing by design; sharp-vs-soft line discrepancies (~1.0 pt) = free EV via line shopping.

## 2. CLV methodology (adopt into bet_tracker/paper_trader)

- **Measure CLV in no-vig probability points, not raw line points.** Convert both secured odds and no-vig closing odds to implied probabilities; CLV = the percentage-point difference. Raw-line CLV (current `closes` implementation) is a usable v1 proxy for prop LINES, but odds-based no-vig CLV is the standard — upgrade when closing odds capture is added.
- **300+ tracked bets** before firm conclusions on model efficacy (also ~265 games to separate a 60% model from a 55% one at 95% confidence). Our gate's 200-bet floor stands, but treat CLV verdicts as provisional until ~300. Do not silently change the gate; flag at graduation review.
- Verify identical grading rules (stat source, void language, timing) before benchmarking against another book's close.

## 3. The calibration fix (answers the inverted C5 problem: C3=62% > C5=50%)

Diagnosis order:
1. **Feature leakage check first** — fit a shallow decision tree over the projection features; a single dominating feature suggests post-hoc information leaking in (classic cause of "high-confidence = coin-flip").
2. If clean, it's overfit confidence scoring.

Fix: **post-hoc calibration layer.** With <1,000 samples (we have 264), **Platt scaling** is the right tool (isotonic regression needs >1,000; temperature scaling is for NN logits). Metric: **Expected Calibration Error** over 10 bins; ECE > 0.05 = recalibrate, > 0.10 = unsafe to stake on. Visual: reliability diagram.

Why it matters (the single strongest receipt in the report): a University of Bath NBA study found calibration-optimized models returned **+34.69% ROI** while accuracy-optimized models lost **−35.17%** — same domain, opposite outcomes. Accuracy is not the objective; calibration is. This retroactively explains our C5 failure: the confidence scorer was never calibrated against outcomes.

## 4. Aug→Oct exam lane assessment (for the season-gap decision — LIKELY tier, analyst-weighted)

| Lane | Edge case | Cost to stand up | Verdict |
|---|---|---|---|
| **WNBA** | Thin market, high prop dispersion across books, few oddsmaker resources; regular season + playoffs run Aug-Oct; documented systemic pricing errors (rested underdogs cover 61%, big favorites 41%) | Lowest — same sport family, The Odds API supports it, projection architecture ports | **Recommended interim lane** |
| MLB props | Pitcher-fatigue + September call-up mispricing; best data of any sport | High — entirely new projection engine (pitch-level) | Viable but expensive |
| CFB (from late Aug) | July 2026 realignment invalidated books' priors, esp. Group of Five | Medium-high; 138 teams, heavy data cleaning | Opportunistic only |
| Tennis (US Open) | Ace lines priced on surface-blended 52-wk averages | Medium; but exchange liquidity deteriorating, account limits | Pass |
| Kalshi/Polymarket | Information arb, not stats modeling | Different skill entirely; regulatory volatility | Separate decision, not the Oracle's exam |

## Era-bound note (2026-08)
Book names, posting-latency specifics, vig levels, WNBA trend percentages, and realignment details are 2025-26 era facts — re-verify each season. The durable core: origination-timing asymmetry, calibration-over-accuracy, no-vig CLV discipline, thin-market edge logic.
