---
date: 2026-07-19
session: nathan-gotch-forge
tier: operator-guide
status: enriched
---

# Nathan Gotch AI SEO — What We Built 2026-07-19 and How to Use It

> Extract-forge expansion of `skills/nathan-gotch-ai-seo/` from Gotch's 2026-07-15 video — his complete live category teardown on a real brand (JerkyGent). The skill jumped from strategy-layer theory to an operational playbook: 9 new workflows (06-14), 9 `/gotch-*` commands, 6 born-v2 prompts (29-34), and the repo's **first primary Gotch source** (until now every pattern was flagged UNCONFIRMED). Companions: `references/jerkygent-case-study.md` (the calibration anchor), `references/linkbait-prompt-bank.md` (his verbatim prompts), `extractions/nathan-gotch/visual-context.md` (26-frame screen ledger).

## ⚡ If you only read 10 lines

1. `/gotch-visibility-gap` first — the diagnosis is a COUNT: "X of Y AI citations mention you, n self-serving." Never a vibe.
2. Good SEO ≠ AI visibility: JerkyGent ranked #3 in Google with **0% AI mentions** (SPI 76/7/0/37). Check both layers separately, always.
3. The AI recommends by **consensus across its sources** — the unit of work is a third-party mention, not an on-site tweak.
4. `/gotch-citation-mine`: export every citation → hand-classify earned / owned / distribution. ~20 earned opportunities per few topics; ×10-20 topics = hundreds.
5. Marketplaces inside the citation set (Amazon/Target/Walmart) that the brand isn't on = double-value targets (sales + citations).
6. `/gotch-alternatives-ladder`: "[Competitor] alternatives" → "[X] vs [Y]" → "vs us." Self takes ONE honest Quick-Picks slot — that's what survives the AI's sniff test.
7. One category, 90-180 days, mile deep. Strategy in one day (`/gotch-category-sprint`); execution is the moat.
8. Tracking: benchmark → annotate shipped work → scan. Never pay for daily tracking on unworked categories (`/gotch-benchmark-scan`).
9. Linkbait: prompt at CATEGORY granularity, 25 grounded ideas, build 5, deep-research the flagship, adopt the most defensible lead stat, design-agent handoff, magic is in the edit (`/gotch-linkbait-engine`).
10. Client receipts on $0 tooling: `/gotch-shadow-receipts` — Proof-to-Market Shadow module; A-tier promotion still awaits Farrice's blind-pass verdict.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/gotch-category-sprint` | One-day category strategy: split diagnosis + citation autopsy + opportunity map + one-page doc | Starting a 90-180 day category push (flagship) |
| `/gotch-visibility-gap` | Counted "good SEO ≠ AI visibility" audit | "Why doesn't ChatGPT recommend us?" / prospect audits |
| `/gotch-citation-mine` | Every citation URL classified earned/owned/distribution + action list | Turning audit data into an outreach/build program |
| `/gotch-alternatives-ladder` | Alternatives → vs → vs-us page set per competitor | Competitors dominate the category's citations |
| `/gotch-topic-gap-map` | Green-boxed coverage + granular-gap inventory as one map | Coverage looks done but paleo/zinc-level intents are unbuilt |
| `/gotch-benchmark-scan` | Work-correlated tracking protocol | Installing tracking discipline; killing wasted tracking spend |
| `/gotch-linkbait-engine` | 25 grounded angles → top-5 → flagship via research→design chain | Informational content that earns links/PR, not generic posts |
| `/gotch-owned-echo` | Topic × channel echo plan, format-native | Site topics tapped out; YouTube/FB/IG expansion |
| `/gotch-shadow-receipts` | Client-facing AI-visibility receipts deck, $0 tooling | Proof-to-Market Shadow module; pre-sale audits |

## The mental model

**1. Two layers, one decision-maker.** Traditional search ranks pages; AI answers synthesize *sources*. A brand can win the first and not exist in the second — and the second is where recommendations (and sales) increasingly happen. Diagnose them separately or the strong layer masks the dead one.

**2. Consensus is the algorithm.** "Imagine you're the AI… working through these different sources and looking for consensus" (3:40). Whoever is mentioned across the most cited sources gets recommended. So the work is source-occupation: get mentioned (linked or not) in the places the AI already reads — the citation export tells you exactly where those are.

**3. Category focus is the enabling constraint.** Everything — the export, the gap map, the ladder, the linkbait — only works at single-category depth ("if you try to be super broad, it's just too hard"). One category, 90-180 days, then the next.

**4. Generate wide, build narrow, edit hard.** 25 ideas → 5 builds. Full-scope AI generation → human hours on the edit. "You don't ever need to start with a blank canvas basically ever. The magic is in the edit."

## The audit → mine → sprint spine (workflows 07, 08, 06)

**What it is**: The diagnosis pipeline. 07 counts the gap (split scorecard + mention autopsy + consensus verdict). 08 turns the citation export into a classified opportunity sheet (earned/owned/distribution, every URL judged by hand). 06 wraps both plus the gap map and sequencing into the one-day category strategy.
**When to reach for it**: any new category push, any "we rank but AI ignores us" complaint, any prospect audit.
**When NOT to**: multi-category briefs (make the operator pick one first — the workflows enforce this); categories with zero commercial intent. For pure AEO structural work (schema, extractability), ethan-smith-aeo is the cheaper tool.
**How to invoke**: `/gotch-visibility-gap` with query set + citation pulls; `/gotch-citation-mine` with the export (schema: Keyword | URL | Platforms | Avg. position | Opportunity); `/gotch-category-sprint` for the whole spine. Execution prompts 29-31 carry the output contracts.
**Worked example**: the JerkyGent teardown itself — #3 organic, 4-of-82 citations (3 self-serving), ~20 earned targets, Amazon/Target/Walmart cited-but-absent, one Canva map. Full walkthrough: `references/jerkygent-case-study.md`.
**Honest edges**: with no tracker, the pull protocol is manual (ChatGPT/Perplexity/Gemini/Copilot by hand + dated screenshots) — works, but budget an hour per query set. Mention counts must be counted, never estimated; the prompts refuse clean-number smells.

## The comparison ladder (workflow 09)

**What it is**: "[Competitor] alternatives" as seed → "[X] vs [Y]" → "[X] vs [Y] vs us." Ranks for competitor queries AND places the brand inside the answer. Template from the screen: honest intro conceding competitor strength, Quick Picks where self takes ONE checkable slot, disclosed "What We Looked For" criteria.
**When to reach for it**: competitors' press keeps showing up in AI citations; competitor-name queries convert.
**When NOT to**: when the brand has no genuinely defensible slot — a page that crowns you at everything fails retrieval credibility and the workflow's gate. Fix the product story first.
**How to invoke**: `/gotch-alternatives-ladder` with competitors + criteria; prompt 32 contracts the output. Slot names are positioning moves ("Best overall for craft discovery") — that's the creative-latitude surface.
**Honest edges**: untested on services/personal brands in live use (adaptations table exists, no live run yet).

## Linkbait engine + design chain (workflow 12)

**What it is**: The verbatim category-focused ideation prompt (25 data-driven ideas with PR hooks + named data seeds) → prioritize 5 → deep research the flagship (his run: 12m 10s) → read the limitations, adopt the **most defensible lead statistic** → structured asset → auto-generated design-agent brief → full visual system in the brand's design system → edit pass. Verbatim prompts: `references/linkbait-prompt-bank.md`.
**When to reach for it**: the brand's informational content is "why X is great" generic (his named anti-exemplar); a PR/outreach program has nothing worth pitching.
**When NOT to**: before commercial topics are covered — this is topic *support*, sequenced after the money pages. Don't run it brand-level; category-level only.
**How to invoke**: `/gotch-linkbait-engine`; prompt 33. Phase 4 hands to the design stack — route per `creative_router.py` pre-flight (this maps 1:1 onto /fantastic-studio).
**Honest edges**: deep-research step costs real tool time/budget (Gemini Deep Research per budget policy; Tavily floor is free but shallower). The defensibility QA step (read limitations, reframe title) is judgment — don't delegate it to the generator.

## Tracking discipline + echo + receipts (workflows 11, 13, 14)

**What they are**: 11 installs benchmark→annotate→scan (scans fire after shipped work, never on calendars — kills wasted tracking spend). 13 echoes tapped-out site topics to YouTube-first then FB/IG, format-native, only to channels the citation data shows in retrieval, with influencer outreach as the second front. 14 packages the audit as a client-facing receipts deck on $0 tooling — the Proof-to-Market "AI-Search Shadow" module (module and hook, never the offer lead — binding 2026-07-18).
**When NOT to**: 13 before site authority exists (gate routes you back to 06/10); 14 as a standalone offer lead.
**Honest edges**: 14's decks name real brands and real counts — fact-verifier before anything ships is mandatory, and the deck stays ≤2 pages + exhibits per client-spec bindings. No live client run yet; first proof pending.

## Composition options (never forced)

| This | Stacks with | When it earns its cost |
|---|---|---|
| 07/14 receipts | proof-to-market sprint, fact-verifier | Brand-buyer prospecting with counted evidence |
| 08 target list | jeremy-haynes cold-offer, lulu-cheng comms | Outreach asks that convert, not template blasts |
| 09 + 12 pages | luke-iha/copy-engine, dara-denney | Agency-grade execution of the page set |
| 12 Phase 4 | fantastic-studio, creative_router | The design handoff inside the existing creative stack |
| 13 echo | kallaway-content-os, jenny-hoyos-shorts, platform constitutions | Channel-native production at volume |
| 06 sprint | jensen-gotch-retrieval, ethan-smith-aeo | LinkedIn/AEO structural layers under the category push |

## Session receipts

Blind pass: independent adversarial-reviewer PASS (EVAL-046) vs two *unseen* published Gotch transcripts (`extractions/nathan-gotch-ai-seo/reference-corpus/`); heartbeat 6/6; finalize 8.75 anchored. Provenance upgrade: 3 anti-patterns UNCONFIRMED→VERIFIED with timestamps (`references/source-ledger.md` 2026-07-19 section). Pending: **Farrice's blind-pass verdict for A-tier** (specimen: `extractions/nathan-gotch-ai-seo/blind-pass-specimen-07.md`) and the Notion finalize-log row (skipped — worktree had no `.env`; local ledgers complete).
