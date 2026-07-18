# Source Ledger — Prediction Market Risk Management

Claim-by-claim provenance for SKILL.md, genius.md, and the three workflows. Ground truth is the MES 3.0 extraction (`extractions/prediction-market-trading/risk-management-extraction.md`, dated 2026-04-13) and the six raw source files it was built from (`extractions/prediction-market-trading/raw-sources/`). Every VERIFIED row below was re-checked against the raw source file directly in this repair pass, not taken on the extraction's word alone (per envelope rule 2 — absence and presence both confirmed by real file reads, with grep line numbers recorded).

## Sources Consulted

| Source | Path | Lines | Status |
|--------|------|-------|--------|
| WeatherBot codebase | `extractions/prediction-market-trading/raw-sources/weatherbot-source.md` | 2,009 | VERIFIED — present, non-empty, read directly |
| Sovereign Trader Analysis (11-source compilation, incl. Jung-Hua Liu Medium post, PolySwarm arXiv paper) | `extractions/prediction-market-trading/raw-sources/sovereign-trader-analysis-source.md` | 607 | VERIFIED — present, non-empty, read directly |
| Polymarket Official Docs | `extractions/prediction-market-trading/raw-sources/polymarket-docs-source.md` | 634 | VERIFIED — present, non-empty, read directly |
| Polymarket Arbitrage Bot (`ImMike/polymarket-arbitrage`) | `extractions/prediction-market-trading/raw-sources/polymarket-arbitrage-source.md` | 608 | VERIFIED — present, non-empty, read directly |
| Poly-Maker Market Making Bot (`warproxxx/poly-maker`) | `extractions/prediction-market-trading/raw-sources/poly-maker-source.md` | 2,101 | VERIFIED — present, non-empty, read directly |
| Polymarket Agents Framework (`Polymarket/agents`) | `extractions/prediction-market-trading/raw-sources/polymarket-agents-source.md` | 1,322 | VERIFIED — present, non-empty, read directly (referenced for the "LLM proposes, code validates" architecture only — not independently line-checked in this pass) |
| MES 3.0 extraction (synthesis layer) | `extractions/prediction-market-trading/risk-management-extraction.md` | 992 | VERIFIED — present, read in full |

## Claims — VERIFIED (re-checked against raw source, line number recorded)

| Claim | Source File | Location |
|-------|-------------|----------|
| 92.4% of Polymarket wallets are unprofitable | `sovereign-trader-analysis-source.md` | Lines 126, 550, 588 |
| Human traders underperform bots by ~18% | `sovereign-trader-analysis-source.md` | Line 130 |
| Arbitrage windows compressed 12.3s (2024) -> 2.7s (2026) | `sovereign-trader-analysis-source.md` | Lines 107, 551 |
| PolySwarm swarm-disagreement uncertainty gate at 30% std dev | `sovereign-trader-analysis-source.md` | Line 338 |
| Paper-to-live: simulation 522x, live v2 -49.5%, live v3 -13% | `sovereign-trader-analysis-source.md` | Lines 429 (source attribution: "Medium — Jung-Hua Liu, March 2026"), 440, 446, 473-475 |
| `KELLY_FRACTION = 0.25`, `calc_kelly()` quarter-Kelly formula | `weatherbot-source.md` | Lines 679, 754-758 |
| `MAX_BET=$20`, `MIN_EV=0.10`, `MAX_PRICE=0.45`, `MIN_VOLUME=500`, `MIN_HOURS=2.0`, `MAX_HOURS=72.0`, `MAX_SLIPPAGE=0.03` | `weatherbot-source.md` | Lines 673-680 |
| Time-horizon take-profit: $0.85 at 24-48h, $0.75 at 48h+ | `weatherbot-source.md` | Lines 1551, 1553 |
| 8-check `RiskManager.check_order()`, `_trigger_kill_switch()`, `kill_switch_triggered` state | `polymarket-arbitrage-source.md` | Lines 206, 243, 276, 282, 313-320, 339 |
| `auto_unwind_on_breach` defaults to `False` | `polymarket-arbitrage-source.md` | Lines 116, 196 |
| Arbitrage bot "Key Warnings": dry-run first, minimal capital, monitor actively / don't leave unattended, "rare and fleeting" | `polymarket-arbitrage-source.md` | Lines 593-597 |
| Compound stop-loss (`pnl < stop_loss_threshold and spread <= spread_threshold`) OR volatility exit | `poly-maker-source.md` | Line 431 |
| Risk-off `sleep_period` cooldown after stop/volatility trigger | `poly-maker-source.md` | Lines 439-440, 475-477 |
| Smart order cancellation thresholds (price diff > $0.005 or size diff > 10%) | `poly-maker-source.md` | Lines 220-233, 264-268 |
| Position merging (YES+NO -> USDC) | `poly-maker-source.md` | Lines 312-323 (plus `poly_merger/` module files) |
| Heartbeat: 10s window, 5s buffer, cancels all open orders on miss | `polymarket-docs-source.md` | Line 358 |
| Matching engine restarts Tuesdays 7 AM ET, ~90s downtime, HTTP 425 | `polymarket-docs-source.md` | Lines 385, 564, 573 |
| Fee formula `fee = C * feeRate * p * (1-p)` | `polymarket-docs-source.md` | Line 182 |
| Rate limits: orders 3,500/10s (36,000/10min), cancel-all 250/10s (6,000/10min) | `polymarket-docs-source.md` | Lines 249, 253 |
| Inventory cap "never exceed 30% exposure on one side"; position limit "never >10% capital in one market"; correlation rebalance at 30% | `sovereign-trader-analysis-source.md` | Lines 221, 296 |
| "Execution is 70% of success. Strategy is only 30%." | `sovereign-trader-analysis-source.md` | Line 302 |

## Claims — LIKELY (consistent with sources but not pinned to one exact line, or lightly paraphrased/combined from adjacent material)

| Claim | Basis | Note |
|-------|-------|------|
| "Always start in dry-run mode before live trading... Monitor actively; don't leave unattended" presented as one continuous quote in SKILL.md/genius.md item 19 | `polymarket-arbitrage-source.md` lines 593, 595, 597 | These are three separate bullet points in the README ("Always start in dry-run mode before live trading" / "Begin with minimal capital ($50-100)" / "Monitor actively; don't leave unattended"), not one sentence. The extraction and this skill compress them for readability. Anti-pattern item #6 in genius.md Section 23 quotes them as three separate fragments to avoid inventing a merged sentence. |
| Cross-platform arbitrage requiring ~5.5% gross edge to clear fees | `polymarket-arbitrage-source.md` `CrossPlatformArbEngine` fee-accounting logic (not independently re-derived from raw fee constants in this pass) | Numerically consistent with Polymarket 1.5% + Kalshi ~1% + gas x2, but the exact 5.5% figure is the extraction's calculation, not a literal source string. |
| Matching engine restart downtime "~90 seconds" | `polymarket-docs-source.md` line 385 states "~90 seconds downtime" directly — VERIFIED, listed here only because the figure is an approximation in the source itself, not a hard SLA. |

## Claims — UNCONFIRMED (checked and not found)

| Claim | Where it would be | Result |
|-------|-------------------|--------|
| Poly-maker author states the production bot is "not profitable" (this claim appears in `extractions/prediction-market-trading/INDEX.md` item 7, not in this skill's SKILL.md/genius.md/workflows) | `poly-maker-source.md` | Grepped for "not profitable" and "profitable" (case-insensitive) across the full 2,101-line file — zero matches. This claim is NOT used anywhere in `skills/prediction-market-risk-management/` and should not be cited from this skill; flagging here only because it appears in the sibling INDEX.md and a future pass could be tempted to import it without checking. |

## Method

For every VERIFIED row, the cited file was opened directly (`grep -n` against the exact figure or code identifier) during this repair pass and the line number recorded above matches what is actually in the file at time of writing. No claim was marked VERIFIED on the extraction's citation alone.
