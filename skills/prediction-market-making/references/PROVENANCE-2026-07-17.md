# Provenance — prediction-market-making repair

Anchor → source file + location, for every new claim added in this repair. All extraction files live under `extractions/prediction-market-trading/`; verbatim line numbers were confirmed by direct `grep -n`/`Read` during this repair (2026-07-17), not carried over unverified from the extraction's own citations.

| Anchor (used in) | Source file | Location | Verification |
|---|---|---|---|
| `mm_enabled: false` / "markets too efficient" (genius.md How-to-Use, Anti-Patterns) | `raw-sources/polymarket-arbitrage-source.md` | line 85 | Confirmed verbatim via grep this repair |
| Poly-maker materiality threshold (`price_diff > 0.005`, `size_diff > order['size']*0.1`) (Anti-Patterns) | `raw-sources/poly-maker-source.md` | lines 220-233 | Confirmed verbatim via grep this repair |
| Poly-maker stop-loss `sleep_period` logic (Anti-Patterns) | `raw-sources/poly-maker-source.md` | lines 431-440 | Confirmed verbatim via grep this repair |
| Poly-maker position-merge logic (`amount_to_merge`, `MIN_MERGE_SIZE`) (Anti-Patterns) | `raw-sources/poly-maker-source.md` | lines 312-321, 675-677 | Confirmed verbatim via grep this repair |
| Poly-maker 0.10-0.90 price-range hard block (Anti-Patterns) | `raw-sources/poly-maker-source.md` | lines 243, 254 | Confirmed verbatim via grep this repair |
| "Inventory caps: never exceed 30% exposure on one side" (Anti-Patterns) | `raw-sources/sovereign-trader-analysis-source.md` | line 221 | Confirmed verbatim via grep this repair |
| Reward pool figures, NBA $7,700 / Champions League QF $24,000 (source-ledger) | `raw-sources/polymarket-docs-source.md` | lines 627, 629 | Confirmed verbatim via grep this repair |
| Single-sided quoting failure mode (Anti-Patterns bullet 1) | `market-making-extraction.md` | lines 496-507 (Anti-Exemplar) | Read directly this repair |
| `mm_enabled: false` narrative framing (Anti-Patterns bullet 2) | `market-making-extraction.md` | lines 327-334 (Hidden 9) | Read directly this repair |
| HTTP 425 / Tuesday restart "what most bots get wrong" (Anti-Patterns bullet 3) | `market-making-extraction.md` | lines 88-98 (Pattern 7) | Read directly this repair |
| "Most beginner bots requote on every tick" (Anti-Patterns bullet 4) | `market-making-extraction.md` | line 208 (Pattern 15) | Read directly this repair |
| Stop-loss death-spiral framing (Anti-Patterns bullet 5) | `market-making-extraction.md` | lines 210-224 (Pattern 16) | Read directly this repair |
| 30% inventory rule framing (Anti-Patterns bullet 6) | `market-making-extraction.md` | lines 120-128 (Pattern 9) | Read directly this repair |
| Position merging framing (Anti-Patterns bullet 7) | `market-making-extraction.md` | lines 226-238 (Pattern 17) | Read directly this repair |

## Negative finding (verified absence, not fabricated)

The quote **"In today's market, this bot is not profitable and will lose money"** — used pre-existing in `genius.md` Hidden Knowledge 10 and `SKILL.md`'s Core Principle line, both out of scope for this repair (passing content, untouched) — could **not** be verified:
- `raw-sources/poly-maker-source.md` (2,101 lines) lists `README.md` in the repo tree but contains no `### File: README.md` section; `grep -in profitable` across the full file returns zero hits.
- A live fetch of `github.com/warproxxx/poly-maker`'s current README (2026-07-17, via WebFetch) returned a related-but-different sentence: "Market making on Polymarket is competitive and can lose money. This is a reference implementation and a research harness, not a guaranteed-profitable product."

This repair does not restate that quote as a new verified anchor anywhere in the added content — it is flagged UNCONFIRMED in `references/source-ledger.md` and reported to the conductor in REPAIR-NOTES.md. Per the additive-first rule, the pre-existing SKILL.md/genius.md lines using it were left untouched (not one of the 4 failing checks, and editing them risked rewriting passing content beyond this task's scope).

## Confirmed-absent (not used)

`extractions/prediction-market-strategies/` — checked via `ls -la`, contains zero files (only `.`/`..`). Not used as a source; all grounding drawn from `extractions/prediction-market-trading/` instead.
