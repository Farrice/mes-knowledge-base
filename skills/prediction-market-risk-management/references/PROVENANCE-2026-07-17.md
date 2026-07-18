# PROVENANCE — prediction-market-risk-management repair

Anchor → source file + location. All entries re-verified by direct `grep -n` against the raw source file during this repair pass (envelope rule 2 — no "source is absent" claim made without a real file read; no source is absent here, all six raw-source files exist and are non-empty, see `references/source-ledger.md`).

## genius.md — Section 23 "Anti-Patterns — Sourced"

| Anti-pattern item | Anchor quote | Source file + location |
|---|---|---|
| Full Kelly sizing on first backtest | "Deploy with full Kelly sizing ($1,000 bet on a $5,000 account)" | `extractions/prediction-market-trading/risk-management-extraction.md` line 460 (extraction dated 2026-04-13, "Anti-Exemplar: The 92.4% Pattern," step 2) |
| Overriding/never setting stops | "Override stops or never set them" / "it'll come back" | `extractions/prediction-market-trading/risk-management-extraction.md` line 463 |
| Paper P&L as live expectation | "simulation showed 522x returns" / Live v2 -49.5%, Live v3 -13% | `extractions/prediction-market-trading/raw-sources/sovereign-trader-analysis-source.md` lines 429, 440, 446, 473-475 (source attribution "Medium — Jung-Hua Liu, March 2026" at line 429) |
| Single-strategy dependence | "12.3 seconds (2024) to 2.7 seconds (2026)" | `extractions/prediction-market-trading/raw-sources/sovereign-trader-analysis-source.md` lines 107, 551 |
| Revenge-sizing after a loss | "Increase size to recover losses (revenge trading, anti-Kelly)" | `extractions/prediction-market-trading/risk-management-extraction.md` line 464 |
| Unattended automation | "Always start in dry-run mode before live trading" / "Begin with minimal capital ($50-100)" / "Monitor actively; don't leave unattended" | `extractions/prediction-market-trading/raw-sources/polymarket-arbitrage-source.md` lines 593-597 |
| Auto-liquidating on kill switch | `auto_unwind_on_breach: false` / "automatic unwinding during market stress can lock in losses that would have recovered" | `extractions/prediction-market-trading/raw-sources/polymarket-arbitrage-source.md` lines 116, 196; `extractions/prediction-market-trading/risk-management-extraction.md` "Signature Move 4" |

## genius.md — "How to Use This Skill (Model Calibration)" section

Not a verbatim-source claim — this is original craft-standard framing written for this skill, modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per the envelope's ALSO instruction. Grounded in the actual sequential-design facts already verified elsewhere in genius.md (8-check chain ordering — Section 3; kill switch state machine — Section 4), not a new factual claim requiring its own citation.

## Workflow contract additions (Output Schema / Quality Gate, all 3 workflows)

Not new factual claims — these formalize output shapes and gate criteria that were already present as prose/examples inside each workflow file (e.g., position-sizing.md's existing "Step 7: Generate Output" APPROVED/REJECTED formats, portfolio-risk-audit.md's existing 8 numbered sections, kill-switch-protocol.md's existing Part A/B/C structure). No external source consulted beyond the workflow's own pre-existing content.

## references/source-ledger.md

Built by re-grepping every major numeric/architectural claim in SKILL.md and genius.md against the six raw source files. See that file for the full claim table with line numbers. One claim was checked and found ABSENT from this skill's material (the poly-maker "not profitable" author quote, which lives only in the sibling `extractions/prediction-market-trading/INDEX.md` and is not used anywhere in this skill) — logged as UNCONFIRMED-and-unused rather than silently omitted, per envelope rule 2.
