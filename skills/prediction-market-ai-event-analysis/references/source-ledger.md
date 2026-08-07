# Source Ledger — Prediction Market AI Event Analysis

Every source consulted for this repair pass, plus a claim-by-claim status for
the Genius Patterns / Hidden Knowledge items already in `genius.md` and the
three workflow files. Labels: **VERIFIED** (the specific figure or quote is
present, verbatim or near-verbatim, in a source file read directly during
this pass, cited with a line anchor) / **LIKELY** (consistent with the
verified material and the extraction's own synthesis, but not itself a
verbatim match to a primary source) / **UNCONFIRMED** (no supporting text
located; flagged, not silently dropped — this is a real gap, not an
oversight).

This is a **composite extraction**, not a single named practitioner's
teaching. There is no one "expert" whose transcript can be checked line by
line; the ground truth is a multi-source research compilation (financial
news, one academic paper, one live-trading postmortem, open-source
repositories, wallet analytics) synthesizing a real trader's (sovereign2013)
on-chain behavior. Anything about sovereign2013's actual internal
methodology is explicitly marked INFERRED in the extraction itself — that
label is preserved here, not upgraded to VERIFIED.

## Sources Consulted (this pass, files read directly)

| File | Size | What it is | Status |
|---|---|---|---|
| `extractions/prediction-market-trading/ai-event-analysis-extraction.md` | 62,098 bytes | The MES 3.0 deep extraction this skill was built from — 12 GPs, 10 HKs, 3 exemplars + 1 anti-exemplar, 7 signature moves, 5 crown-jewel prompts, Appendix source index (11 sources) | VERIFIED — read in full, confirmed non-empty, matches skill content near-verbatim |
| `extractions/prediction-market-trading/raw-sources/sovereign-trader-analysis-source.md` | 27,847 bytes | The actual 11-source research compilation (financial news + arXiv paper + live-trading postmortem + GitHub repos + leaderboard data) that the extraction above synthesizes. Contains `## Source 1` through `## Source 11` headers with the raw reporting. | VERIFIED — read in full, all 11 source sections confirmed present with line anchors below |
| `extractions/prediction-market-trading/raw-sources/polymarket-docs-source.md` | 28,454 bytes | Official Polymarket documentation scrape (fee structure, maker/taker mechanics, CLOB API) | VERIFIED — read (fee section); used to cross-check the flat-percentage fee schedule used in the workflows (see Fee Schedule Caveat below) |
| `extractions/prediction-market-trading/raw-sources/poly-maker-source.md` | 81,357 bytes | Open-source market-making bot code/docs | VERIFIED — exists, grepped for fee/reward terms; not the basis for any GP/HK claim below |
| `extractions/prediction-market-trading/raw-sources/polymarket-agents-source.md` | 44,828 bytes | Polymarket's official agents framework source | VERIFIED — exists on disk; not independently re-read claim-by-claim this pass (Source 8 in the compilation covers the same ground) |
| `extractions/prediction-market-trading/raw-sources/polymarket-arbitrage-source.md` | 21,015 bytes | Open-source arbitrage bot reference | VERIFIED — exists, grepped ("net edge = gross edge - (taker fees + gas costs)") |
| `extractions/prediction-market-trading/raw-sources/weatherbot-source.md` | 85,946 bytes | Weather-market bot source (belongs primarily to the sibling `prediction-market-weather-trading` skill, not this one) | VERIFIED — exists; out of scope for this skill's claims |
| `_active/wagering/prediction-market-arb/` (polymarket_client.py, market_selector.py, polymarket_ws.py) | — | Farrice's own live project implementing a Polymarket client | VERIFIED to exist; confirms this skill has an active downstream consumer, not cited as a content source for any GP/HK claim |

No claude.ai export, transcript, podcast, or interview underlies this
skill — it is grounded entirely in written research artifacts, all present
on disk and read directly during this pass.

## Claim-by-Claim Ledger (`genius.md` — Genius Patterns & Hidden Knowledge)

| Claim | Status | Evidence |
|---|---|---|
| sovereign2013: $1 → $3.3M, 37,247+ predictions, sports-focused, Claude-powered | **VERIFIED** | `sovereign-trader-analysis-source.md` Source 1, lines 22-45 (wallet address, Finbold + MEXC + KuCoin + CryptoNews.net cited, "Total Predictions: 37,247+", "Total Profit: ~$3.3 million (from $1 initial)") |
| Utah State vs. Arizona: $1.73M volume, $179,100 profit | **VERIFIED** | Same source, line 51: "Utah State Aggies vs. Arizona Wildcats... over $1.73 million total, $179,100 in pure profit" |
| GP-1 Vegas Anchor / reference-price arbitrage framing | **LIKELY** | The mechanic (sportsbook as ground truth) is the extraction's own synthesis of sovereign2013's sports-arbitrage behavior (Source 1) plus Source 5's market-segmentation insight (line 177-207: "Longer-dated markets... still retain more human-judgment opportunities"). No single source states the "Vegas Anchor" framing verbatim — it is a reasonable, well-grounded synthesis, not a direct quote. |
| GP-2 / HK-2: GPT-4o 40% / Claude 35% / Gemini 25% ensemble weights | **VERIFIED** | Source 10, lines 483-493: "GPT-4o: 40% weight / Claude 3.5 Sonnet: 35% weight / Gemini 1.5 Pro: 25% weight / Models forecast independently" (github.com/dylanpersonguy/Fully-Autonomous-Polymarket-AI-Trading-Bot) |
| GP-3 Paper-to-live haircut: 522x paper → -49.5% (v2) → -13% (v3) | **VERIFIED** | Source 9, lines 427-472: "Simulation: 522x returns... Live v2: -49.5% loss... Live v3: -13% loss." Exact win/loss records (4W/11L, 2W/2L) and root causes (65% signal weight on final 60s, 80% trades favored UP in downtrend) also verbatim-confirmed in the same block. |
| GP-3 fee/breakeven detail: "1.56% fee at $0.50 entry," breakeven win rate ~53% | **VERIFIED** | Source 9, line ~468: "Live win rates of 25-27% fell substantially below the ~53% breakeven threshold needed to overcome Polymarket's 1.56% fee at $0.50 entry plus 2-4 cent execution slippage." |
| GP-4 Quarter-Kelly convergence across bot architectures | **VERIFIED** | Confirmed independently in three sources: Source 6 line ~300 ("Kelly Criterion Sizing: Prevents over-betting"), Source 7 line ~370 ("Position Sizing: Quarter-Kelly / Formula: f = 0.25 x f*"), Source 9 line ~440 ("Fractional Kelly with quarter-Kelly cap"). |
| GP-5 PolySwarm 70/30 Bayesian mixture, 25-of-50 agent sampling | **VERIFIED** | Source 7, lines 306-345 (arXiv, April 2026): "25 agents sampled without replacement," "Stage 2: ... 70% swarm weight / 30% market weight," "Combined probability exceeds market-implied odds by 5% minimum threshold / Swarm standard deviation below 30%" |
| GP-6 Arbitrage window compression: 12.3s (2024) → 2.7s (2026), 73% captured by sub-100ms bots | **VERIFIED** | Confirmed at three separate points in the compilation: lines 107, 551, 582, 591 (Source 3 and Source 11 both cite "2.7 seconds... down from 12.3 seconds in 2024" and "73% captured by sub-100ms bots") |
| GP-6 0x8dxd: $313 → $438K, 98% win rate, 6,615 predictions | **VERIFIED** | Source 3, lines 91-96 ("Wallet 0x8dxd — The Legend... approximately $438,000 from initial $313... 98% win rate across 6,615 predictions"); corroborated independently at Source 4 line ~142 ("$313 into $414,000... 98% win rate") and Source 5 line ~189 ("~$300 into $400,000+") — the three figures cluster ($313-438K, $313-414K, $300-400K+) rather than matching exactly, consistent with multiple outlets reporting the same underlying wallet at slightly different snapshot times. |
| GP-7 Portfolio construction table (Conservative/Balanced/Aggressive %, return, drawdown, Sharpe) | **VERIFIED** | Source 6, lines ~280-284, table figures match genius.md exactly (Conservative 80/20 → 4.2%/0.8%/2.1 Sharpe; Balanced 50/30/20 → 11.7%/3.2%/1.6; Aggressive 30/50/20 → 23.4%/8.9%/1.1) |
| GP-8 Information-theoretic detectors (KL divergence, Jensen-Shannon, negation pairs, Bayesian network consistency) | **VERIFIED** | Source 7, lines ~336-341, all four named explicitly |
| GP-9 Market segmentation (ultra-short crypto = bot-dominated vs. longer-dated = human-judgment opportunity) | **VERIFIED** | Source 5, lines 177-207 (headed "Market Segmentation Insight" verbatim) |
| GP-10 v2-to-v3 iteration model, exact fixes (120s/240s lookback, 10-min trend filter, counter-trend rejection unless BTC >0.10%) | **VERIFIED** | Source 9, lines 427-472, all technical parameters confirmed verbatim, including "Reject signals opposing 15-minute trend unless BTC move >0.10%" |
| GP-11 Hallucination-correlation risk in ensembles | **VERIFIED** | Source 7, "Identified Challenges" section (~line 358): "Hallucination: LLMs may confidently assert false facts. Correlated errors across personas prevent error cancellation." |
| GP-12 Capital rotation vs. hold-to-resolution | **LIKELY / INFERRED** | The extraction itself labels this INFERRED — reasoned from sovereign2013's "multiple bets per minute" trading velocity (Source 1, line ~36), not a direct statement of strategy. Preserved as INFERRED, not upgraded. |
| HK-3 / 92.4% failure taxonomy (50,000+ wallets, oversized positions / late entries / inconsistent risk management) | **VERIFIED** | Source 3, "Critical Reality Check" (lines ~126-133): "Analysis of 50,000+ Polymarket wallets: 92.4% are unprofitable... Human traders underperform bots using identical strategies by ~18%, due to poor position sizing and inconsistent risk management" |
| HK-6 API cost trap ("thousands per day," 86.4M calls/day math) | **VERIFIED (quote)** / **LIKELY (arithmetic)** | "thousands per day in API costs at scale" is verbatim from Source 7 "Identified Challenges" #2. The 86.4M-calls/$86K/day extrapolation is the extraction author's own arithmetic built on Source 7's 25-agent/5-second-scan-loop architecture (lines 310-315) — reasonable derived math, not itself a quoted figure. |
| HK-8 Gambot / vig-stripping mechanics, Pinnacle as sharpest book | **LIKELY** (core claim sourced; margin specifics unconfirmed) | Core claim IS in `sovereign-trader-analysis-source.md` line 566: "**Gambot**: Pulls odds from Pinnacle, removes house edge, calculates true probabilities" — corrected 2026-07-17 by Opus adversarial verify after this pass originally mislabeled it UNCONFIRMED with a false "no Gambot reference" absence claim. The margin SPECIFICS (2-3% vig figure, -150/+130 conversion example) remain unsourced in this skill's research folder and stay unverified. |
| HK-10 $40M extraction figure, Apr 2024-Apr 2025 | **VERIFIED** | Confirmed independently at Source 4 (line ~176: "$40 million extracted by arbitrage traders (April 2024 - April 2025)") and Source 5 (line ~183: "Arbitrage traders extracted ~$40 million from Polymarket (April 2024 - April 2025)") |
| "14 of 20 top wallets are bots" | **VERIFIED** | Source 4 line ~140 and Source 5 line ~181, both verbatim |

## Fee Schedule Caveat (workflows/ — flagged, not silently presented as verified)

All three workflow files (and the corresponding `references/prompts-v2/*.md`
prompts) use a flat fee schedule: **0.75% taker (sports) / 2% taker
(non-sports), 1.5%/4% round trip**. This exact split by market category is
**UNCONFIRMED** against the sources in this skill's own research folder:

- Polymarket's actual documented fee mechanism (`raw-sources/polymarket-docs-source.md`,
  line 182) is a variable formula — `fee = C * feeRate * p * (1 - p)`,
  peaking at 50% probability and decreasing toward the extremes — not a
  flat percentage, and not split by sports vs. non-sports.
- The one verified flat-percentage figure in the research is Source 9's
  "1.56% fee at $0.50 entry" (round-trip, at p=0.5), which is roughly
  consistent with the variable formula's peak but does not itself establish
  a sports/non-sports split.

**Verdict**: LIKELY as a workable approximation (internally consistent, and
in the right order of magnitude versus the one verified data point), but
the specific 0.75%/2% split is not independently confirmed. Flagging here
rather than either deleting the numbers (which would break three
already-working workflows) or presenting them as VERIFIED.

## Anti-Pattern Quote Ledger (`genius.md` — "Anti-Patterns (Sourced)" section)

All seven items added to `genius.md`'s new "Anti-Patterns (Sourced)"
section are **VERIFIED**: five are verbatim quotes traced to
`extractions/prediction-market-trading/ai-event-analysis-extraction.md`'s
"Anti-Exemplar: The 92.4%" section (itself synthesizing the 92.4%-failure
finding documented at `raw-sources/sovereign-trader-analysis-source.md`
Source 3, lines 80-133); two are verbatim quotes already present in this
skill's own `workflows/multi-model-ensemble.md` and
`workflows/odds-discrepancy-scanner.md` Anti-Patterns sections. See
`PROVENANCE.md` for the full anchor table.

## Known Gaps (named, not hidden)

1. **HK-8 (Gambot / Pinnacle vig-stripping) is UNCONFIRMED** against this
   skill's own source files — see ledger row above. A future pass should
   locate the specific source (likely a GitHub README or betting-market
   explainer) this claim originated from, or downgrade the confidence
   language in `genius.md` if none can be found.
2. **The 0.75%/2% sports/non-sports fee split (all three workflows) is
   UNCONFIRMED** as a precise figure — see Fee Schedule Caveat above. The
   workflows remain usable (the approximation is directionally correct and
   internally consistent), but an operator relying on exact fee math for
   live capital should re-verify against Polymarket's live `/fee-rate`
   endpoint rather than trusting these flat percentages.
3. **No independent access to the 11 external sources themselves** (Finbold,
   Yahoo Finance, arXiv 2604.03888v1, the named GitHub repos) was performed
   this pass — verification is against the raw-sources compilation file
   already in this repo, which itself claims to be a direct research pull
   from those outlets. This ledger treats that compilation file as the
   primary source, consistent with how the skill was originally extracted;
   it does not re-fetch the live URLs.
4. **GP-12 (capital rotation) and GP-2's disagreement-tier language
   ("2 agree, 1 dissents") remain LIKELY/INFERRED**, exactly as the
   extraction itself already labeled them — this ledger does not upgrade
   any INFERRED claim to VERIFIED.
