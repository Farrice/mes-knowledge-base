# Source Ledger — Alex Hormozi Business Skill

Claim-by-claim provenance for `skills/alex-hormozi-business/genius.md` and `SKILL.md`. Labels: **VERIFIED** (matched against a primary/external source this session), **LIKELY** (matched against a source with a minor unconfirmable segment), **UNCONFIRMED** (no primary source located this session — plausible but not independently checked; treat as skill-authored synthesis, not sourced fact).

## Absence check performed (2026-07-17, this repair)

- `ls extractions/ | grep -i hormozi` → **0 matches** (193 total entries in `extractions/`, scanned in full; command exit code 1 = no match). No Hormozi-specific extraction folder or transcript exists in this repo.
- `find . -iname "*hormozi*"` (repo-wide, excluding `.git/`) → only agent/skill/command scaffolding and this audit's own files; no raw source material (transcript, book excerpt, article) found anywhere in the repo.
- `agents/alex-hormozi/memory/context.md` — read in full, **366 bytes** (`wc -c`), contents are unpopulated template placeholders ("(to be populated...)"). No usable source material.
- `agents/alex-hormozi/AGENT.md` — read in full, **4,522 bytes** (`wc -c`), a persona/routing summary derived from the same claims as SKILL.md/genius.md, not an independent source.
- `skills/alex-hormozi-business/SKILL.md` frontmatter states `source: claude.ai export 2026-07-01` — i.e., the skill was originally authored from an AI-assisted conversation export, not a verbatim transcript or book-page capture. This is the honest root cause of the pre-repair `source_ledger` FAIL: no ledger existed because no primary-source discipline was applied at authoring time.
- `_active/harness/elevation-track/e3/real-pieces.json` (12,667 bytes, `wc -c`) — a human-and-provenance-verified corpus built for a separate blind bake-off exercise; it independently contains 3 Hormozi excerpts with real external sources (book + 2 LinkedIn posts). These are the only externally-verified Hormozi material found in the repo and are used below as the basis for the new Anti-Patterns section.

## VERIFIED / LIKELY claims (external source located)

| Claim / Quote | Label | Source | Location |
|---|---|---|---|
| "No offer? No business. No life. Bad offer? Negative profit. No business. Miserable life. Decent offer? No profit. Stagnating business. Stagnating life. Good offer? Some profit. Okay business. Okay life. Grand Slam Offer? Fantastic profit. Insane business. Freedom." | LIKELY | *$100M Offers* (2021), Ch. 2 offer ladder | `_active/harness/elevation-track/e3/real-pieces.json` idx 1 (skill: alex-hormozi-business) — recorded caveat: "first rungs double-confirmed, full ladder single-source" |
| "10 Truths I live by" (10-item list; used here: #2 comparison, #5 failure-as-feedback) | VERIFIED | LinkedIn @alexhormozi, activity-7057390440928432128 | `_active/harness/elevation-track/e3/real-pieces.json` idx 2 |
| "Super real talk: If you're working all the time, and you're not making progress, you're doing the wrong stuff. Most people don't need to solve more problems, they just need to pick better problems to solve." | VERIFIED | LinkedIn @alexhormozi, activity-7080243902582005761 | `_active/harness/elevation-track/e3/real-pieces.json` idx 3 |

## UNCONFIRMED claims (genius.md / SKILL.md content, no primary source located this session)

These are pre-existing in the skill (authored 2026-07-01 from a claude.ai export) and are preserved per the additive-first, non-destructive repair boundary — they are plausible and consistent with widely-reported public facts about Hormozi's career, but this repair pass could not independently verify them against a transcript, book page, or dated post. Treat as **UNCONFIRMED** until a primary source is attached.

| Claim | Label | genius.md / SKILL.md location |
|---|---|---|
| Gym Launch 0 → $2.2M/month in 20 months | UNCONFIRMED | SKILL.md line 12 (source line); genius.md, Pattern: Client-Financed Acquisition |
| Prestige Labs ~$1.5M/month in six months | UNCONFIRMED | SKILL.md line 12 |
| "The Golden Number" — 30-day gross profit ≥ 2x (CAC + COGS) as his named framework | UNCONFIRMED (concept is publicly associated with *Money Models*; verbatim framing not independently checked this session) | genius.md, Pattern: Client-Financed Acquisition; SKILL.md Quick Reference |
| Grandmother "main stomach's full, dessert stomach's empty" quote | UNCONFIRMED | genius.md, Pattern: Psychological Wallets |
| Salt Lake City $16K suit / committed-anchor story | UNCONFIRMED | genius.md, Pattern: The Committed Anchor |
| "Do you want anything else?" / no-based upsell scripting, 80-90% take-rate figure | UNCONFIRMED | genius.md, Pattern: No-Based Upsell Scripting |
| "We don't get customers to make sales. We make sales to get customers." | UNCONFIRMED (widely circulated attribution, not matched to a dated primary source this session) | genius.md, Insight: Sales Exist to Buy Customers; SKILL.md Quick Reference |
| Waived-fee ($10K upfront / waived for a year) continuity close example | UNCONFIRMED | genius.md, Insight: The Waived-Fee Continuity Close |
| Giveaway/raffle attraction-offer mechanic | UNCONFIRMED | genius.md, Insight: The Giveaway Attraction Offer Qualifies at the Top |
| TOC-first book-writing process, 20+ books outlined | UNCONFIRMED | genius.md, Insight: Table of Contents Is the Product |
| "Season of No" / Zeigarnik-effect writing routine | UNCONFIRMED | genius.md, Insight: Season of No |
| Bottom-10%-days / utilitarian-test resilience framing | UNCONFIRMED | genius.md, Insight: The Math of Bad Days |
| 24 portfolio companies cut to 10 (14 dumped at a loss) | UNCONFIRMED | genius.md, Pattern: Focus = What You Say No To; Insight: Prune the Portfolio, Feed the Stallions |
| "Cool. Don't do it. I'm the boss. It's fine if you just do this." | UNCONFIRMED | genius.md, Pattern: Focus = What You Say No To |
| "Validity x Utility" / "how do I break this?" self-testing framework | UNCONFIRMED | genius.md, Pattern: Validity x Utility |
| "Skills are the hedge against inflation..." / "lottery ticket's free" quotes | UNCONFIRMED | genius.md, Pattern: Skills Are the Ultimate Hedge |
| 1M+ books sold across the $100M Offers/Leads/Money Models trilogy | UNCONFIRMED | SKILL.md line 12 |

## Repair-session rule applied

No quote in the new Anti-Patterns section (genius.md) was invented — the 4 VERIFIED/LIKELY items are copied verbatim from `real-pieces.json`; the 3 UNCONFIRMED items reformat pre-existing skill sentences (never a new claim) and are explicitly labeled UNCONFIRMED in both genius.md and here, per the "unforgivable failure is invented provenance" rule.
