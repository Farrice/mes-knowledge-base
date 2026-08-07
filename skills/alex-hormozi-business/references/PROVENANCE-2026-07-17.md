# Provenance — alex-hormozi-business repair

Anchor → source file+location table for every new quote/claim added in this repair pass.

| Anchor (in new genius.md Anti-Patterns section) | Source file | Location | Label |
|---|---|---|---|
| "No offer? No business. No life. Bad offer?..." offer ladder | `_active/harness/elevation-track/e3/real-pieces.json` | idx 1, skill "alex-hormozi-business" | LIKELY |
| "If you want to feel terrible— Remember, there's always someone doing better." | `_active/harness/elevation-track/e3/real-pieces.json` | idx 2, "10 Truths I live by," Truth #2 | VERIFIED |
| "Failure is to be expected, not avoided. Failure is feedback, not judgment." | `_active/harness/elevation-track/e3/real-pieces.json` | idx 2, "10 Truths I live by," Truth #5 | VERIFIED |
| "Super real talk: If you're working all the time..." | `_active/harness/elevation-track/e3/real-pieces.json` | idx 3, skill "alex-hormozi-business" | VERIFIED |
| Steakhouse mistake (upsell-at-satiety anti-pattern) | `skills/alex-hormozi-business/genius.md` (pre-repair) | Pattern: Sell at the Point of Greatest Deprivation, ¶1 | UNCONFIRMED (skill-internal, no external primary source located) |
| Bundling-the-upsell anti-pattern | `skills/alex-hormozi-business/genius.md` (pre-repair) | Pattern: Psychological Wallets, ¶1 | UNCONFIRMED (skill-internal) |
| Discounting-instead-of-removing-features anti-pattern | `skills/alex-hormozi-business/genius.md` (pre-repair) | Pattern: Sell the Transformation, Not the Membership, ¶1 | UNCONFIRMED (skill-internal) |

## Absence-verification receipts (real file reads + recorded sizes)

- `ls extractions/ | grep -i hormozi` → 0 matches (grep exit code 1); `extractions/` has 193 total entries, scanned in full.
- `find . -iname "*hormozi*"` (repo root, excludes `.git/`) → only scaffolding (agents/alex-hormozi, .claude/commands/alex-hormozi*.md, skill dir itself, evolution trace, elevation-track gen file, this audit's own files) — no raw source material.
- `agents/alex-hormozi/memory/context.md` — 366 bytes (`wc -c`), unpopulated template.
- `agents/alex-hormozi/AGENT.md` — 4,522 bytes (`wc -c`), persona summary derived from the same unverified claims, not an independent source.
- `evolution_store/v2_traces/trace_20260701_180736_alex-hormozi-business.json` — 1,860 bytes (`wc -c`), a chain-finalize telemetry record (quality scores, notes), not source material.
- `_active/harness/elevation-track/e3/gen-alex-hormozi-business.json` — 1,320 bytes (`wc -c`); confirmed via `_active/harness/elevation-track/e3/README.md` this is **AI-generated** blind-test material ("Generators saw ONLY their skill dir + task briefs — never the real pieces, extractions, or sibling skills"), explicitly NOT used as a source anchor.
- `_active/harness/elevation-track/e3/real-pieces.json` — 12,667 bytes (`wc -c`); per the same README, this is the **human-and-provenance-verified** counterpart corpus ("Real pieces: verbatim, provenance-verified; 13/15 VERIFIED, 2 LIKELY"). This is the only externally-sourced Hormozi material in the repo and is what the new Anti-Patterns section draws its 4 VERIFIED/LIKELY quotes from.

No source under `extractions/` exists for Alex Hormozi. All quotes not traceable to `real-pieces.json` are labeled UNCONFIRMED in `references/source-ledger.md` and left as skill-internal, non-invented reformattings of pre-existing genius.md text.
