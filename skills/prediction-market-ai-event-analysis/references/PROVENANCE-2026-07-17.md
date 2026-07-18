# Provenance — prediction-market-ai-event-analysis repair pass

Anchor table: every claim added or newly sourced in this pass, mapped to its
exact source file + location. Full source-by-source detail (VERIFIED /
LIKELY / UNCONFIRMED per claim) lives in `references/source-ledger.md`; this
file is the compact anchor-to-location index.

| Anchor (added content) | Source file | Location |
|---|---|---|
| genius.md "How to Use This Skill (Model Calibration)" — sovereign2013 discipline framing, $1→$3.3M, 37,247 bets | `extractions/prediction-market-trading/raw-sources/sovereign-trader-analysis-source.md` | Source 1, lines 22-45 |
| genius.md "How to Use This Skill" — "'I think the Lakers will win' is not an edge" (paraphrase of the anti-pattern) | `skills/prediction-market-ai-event-analysis/workflows/odds-discrepancy-scanner.md` | "Anti-Patterns (What NOT to Do)" section, item 1 |
| Anti-Pattern 1: "without checking whether the price already reflects that probability" | `extractions/prediction-market-trading/ai-event-analysis-extraction.md` | "Anti-Exemplar: The 92.4%", item 1 (root data at raw-sources/sovereign-trader-analysis-source.md, Source 3, lines 80-133) |
| Anti-Pattern 2: "they mistake certainty of feeling for certainty of edge" | `extractions/prediction-market-trading/ai-event-analysis-extraction.md` | "Anti-Exemplar: The 92.4%", item 2 |
| Anti-Pattern 3: "Humans enter ultra-short crypto binary options... capture 73% of profits" | `extractions/prediction-market-trading/ai-event-analysis-extraction.md` | "Anti-Exemplar: The 92.4%", item 3 (root data at raw-sources/sovereign-trader-analysis-source.md, Source 5, line 177; 73% figure also at line 591) |
| Anti-Pattern 4: "A 2% edge sounds good until 1.56% in fees and 2-4 cents in slippage consume it" | `extractions/prediction-market-trading/ai-event-analysis-extraction.md` | "Anti-Exemplar: The 92.4%", item 4 (1.56% fee figure verified at raw-sources/sovereign-trader-analysis-source.md, Source 9, ~line 468) |
| Anti-Pattern 5: "they hold hoping for reversal instead of cutting and rotating capital to the next opportunity" | `extractions/prediction-market-trading/ai-event-analysis-extraction.md` | "Anti-Exemplar: The 92.4%", item 5 |
| Anti-Pattern 6: "is how the 92.4% lose money. The market knows things you don't" | `skills/prediction-market-ai-event-analysis/workflows/multi-model-ensemble.md` | "Anti-Patterns" section, item 3 |
| Anti-Pattern 7: "Do not trade without a reference price." | `skills/prediction-market-ai-event-analysis/workflows/odds-discrepancy-scanner.md` | "Anti-Patterns (What NOT to Do)" section, item 1 |
| workflows/odds-discrepancy-scanner.md "## Quality Gate" (6 items) | `skills/prediction-market-ai-event-analysis/references/prompts-v2/odds-discrepancy-scan.md` | "## Quality Gate" section (already-written, structure-pure-v2 prompt covering the same deliverable) — ported verbatim, plus one added bullet on the "no market silently dropped" requirement already stated in that prompt's Output Contract |
| workflows/multi-model-ensemble.md "## Quality Gate" (6 items) | `skills/prediction-market-ai-event-analysis/references/prompts-v2/multi-model-ensemble-forecast.md` | "## Quality Gate" section — ported verbatim |
| workflows/edge-validation-sizing.md "## Quality Gate" (6 items) | `skills/prediction-market-ai-event-analysis/references/prompts-v2/edge-validation-trade-plan.md` | "## Quality Gate" section — ported verbatim |
| GPT-4o 40% / Claude 3.5 Sonnet 35% / Gemini 1.5 Pro 25% ensemble weights (pre-existing genius.md claim, now re-verified) | `raw-sources/sovereign-trader-analysis-source.md` | Source 10, lines 483-493 |
| Paper-to-live haircut data: 522x paper, -49.5% v2, -13% v3 (pre-existing claim, re-verified) | `raw-sources/sovereign-trader-analysis-source.md` | Source 9, lines 427-472 |
| 92.4% unprofitable / 50,000+ wallets / ~18% human underperformance (pre-existing claim, re-verified) | `raw-sources/sovereign-trader-analysis-source.md` | Source 3, lines 126-133 |
| Portfolio construction table (Conservative/Balanced/Aggressive) (pre-existing claim, re-verified) | `raw-sources/sovereign-trader-analysis-source.md` | Source 6, lines ~280-284 |
| PolySwarm 70/30 mixture, 25-of-50 sampling (pre-existing claim, re-verified) | `raw-sources/sovereign-trader-analysis-source.md` | Source 7, lines 306-345 |
| Arbitrage window 12.3s→2.7s, 73% sub-100ms capture (pre-existing claim, re-verified) | `raw-sources/sovereign-trader-analysis-source.md` | lines 107, 551, 582, 591 |
| **Fee schedule 0.75%/2% sports/non-sports split (pre-existing, all 3 workflows)** | **UNCONFIRMED** | No exact match found in `raw-sources/*`. Official Polymarket fee formula at `raw-sources/polymarket-docs-source.md`, line 182, is a variable formula, not a flat sports/non-sports split. See `references/source-ledger.md` "Fee Schedule Caveat" for full detail — flagged, not silently corrected or deleted. |
| HK-8 Gambot / Pinnacle vig-stripping mechanics (pre-existing genius.md claim) | **LIKELY** (corrected by Opus verify 2026-07-17) | Core claim anchored: `sovereign-trader-analysis-source.md` line 566 ("Gambot: Pulls odds from Pinnacle, removes house edge, calculates true probabilities"). Original pass falsely claimed no Gambot reference existed. Margin specifics (2-3% vig, -150/+130) remain unsourced. See `references/source-ledger.md` ledger row. |

All file paths above are relative to the repo root
`/Users/farricecain/Google Antigravity`. Line numbers for
`sovereign-trader-analysis-source.md` were confirmed via direct `grep -n`
and `sed -n` reads during this session (not estimated).
