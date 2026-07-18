# Source Ledger — tom-noske-personal-brand

Claim-by-claim provenance for every substantive claim in `SKILL.md`,
`genius.md`, and `agents/tom-noske/AGENT.md` (shared identity paragraph).
Labels: **VERIFIED** (verbatim quote or exact figure found in a primary
source transcript) / **LIKELY** (consistent with a secondary
extraction-report summary of source material whose raw transcript is not
currently on file, or a clear paraphrase of a verified point) /
**UNCONFIRMED** (no matching text found anywhere in the source corpus
searched — flagged, not deleted, per the "one unforgivable failure is
invented provenance" rule).

## Sources consulted (this repair pass)

| # | File | Type | Size (wc -c) |
|---|------|------|---------------|
| 1 | `extractions/tom-noske/transcript.txt` | Primary — "Five Unspoken Content Rules" YouTube transcript | 27,458 bytes |
| 2 | `extractions/Tom Noske/transcript.txt` | Primary — "Two Lies" / Content Funnel YouTube transcript | 30,517 bytes |
| 3 | `extractions/_archive/tom-noske-2/transcript.txt` | Primary — "Why Content Creation Is the Greatest Wealth-Building Opportunity" YouTube transcript | 20,089 bytes |
| 4 | `extractions/tom-noske/tom-noske-v2-extraction-report.md` | Secondary — dual-video extraction report (references Video 1, "4 Ingredients for $10K/Month," whose raw transcript was NOT found on disk) | 11,077 bytes |
| 5 | `extractions/tom-noske/extraction-report-content-creation.md` | Secondary — extraction report for the sibling `tom-noske-content-creation` skill (source file #1 above) | 13,277 bytes |
| 6 | `agents/tom-noske/AGENT.md` + `agents/tom-noske/memory/context.md` | Existing system artifact, not a primary source | n/a |
| 7 | `research_outputs/ai_authority_architect_agents/tom_noske.md` | Downstream application dossier (Farrice-specific), NOT a Tom Noske primary source — its own re-grounding pass (2026-06-02) already flags several of its own soundbites as `[MODELED]`/unsourced | 10,411 bytes |

**Search discipline followed**: searched all name fragments (`noske`, `tom noske`, `Tom Noske`) across `extractions/`, `_archive/`, `research_outputs/`, `agents/`, `evolution_store/`. CORRECTION (2026-07-18 Opus adversarial verify): the original repair pass skipped the `_archive/claude-export-2026-07-01.tar.gz` scan ("not needed") — that skipped scan held the proof for the headline stats. Two primary Noske masterclass transcripts live at `claude-export/normalized/conversations/934a03af-f7ec-4bea-8bf8-f94ad6d10d10.md` (89,799 bytes) and `e423b3d3-e53f-4400-9c57-61a549b46b61.md` (93,285 bytes), both containing the headline figures verbatim (independently re-confirmed by the conductor). Lesson: a "scan not needed" decision is itself an absence claim. One video referenced in source #4 ("4 Ingredients for $10K/Month with Small Audience," Video 1 of the dual-video extraction) has NO raw transcript file anywhere on disk outside `.claude/worktrees/` — every claim traceable only to that video is labeled LIKELY, not VERIFIED, below.

---

## Claim-by-claim ledger

### Headline identity claims (SKILL.md line 12, AGENT.md line 12)

| Claim | Status | Note |
|---|---|---|
| "generated $3M+ since 2022" | **VERIFIED (self-reported)** | CORRECTED 2026-07-18: verbatim in archive transcript 934a03af/e423b3d3 ("I've made over $3 million online since 2022") AND in `extractions/tom-noske/extraction-report-content-creation.md:8` ("$3M+ revenue since 2022") — the original "not found in the 2 extraction reports" claim was false. Self-reported by Noske, not independently audited. |
| "$130K/month average" | **VERIFIED (self-reported)** | CORRECTED 2026-07-18: verbatim in archive transcripts — "I've averaged $130,000 a month in 2024 and 2025." Self-reported. |
| "$6M cumulative student wins" | **VERIFIED (self-reported)** | CORRECTED 2026-07-18: stated in the same archive transcripts ($6M cumulative + "coached over a thousand"). Self-reported. |
| "Target $2-4/follower annual earnings" | **LIKELY (range is a gloss of a verified $3 figure)** | CORRECTED 2026-07-18: archive transcripts have the verbatim "$3 in earnings per follower for the past three years" — the $2-4 RANGE is the skill's gloss of that verified single figure. Original note kept below for the range-specific caveat: | No verbatim "$2-4/follower" figure in any transcript. The *closest* verified analog is Hidden Knowledge #5's "100K followers @ $400K/year... 20x" comparison (below), which implies roughly $4/follower for that one example — a single data point, not a stated universal target. `research_outputs/ai_authority_architect_agents/tom_noske.md` (source #7) independently searched for this exact "$2-4/follower" figure on 2026-06-02 and returned "NO corroborating source... UNCONFIRMED." |
| "8/10 failure rate" as a literal published statistic | **UNCONFIRMED as a citable stat** | The pattern itself (audience ≠ revenue, archetype-predictable) is directionally consistent with Tom's own "two lies" framing (source #2: a friend with 2M followers "barely makes enough money to quit his day job"), but no transcript states "8 out of 10 creators with 100K+ followers." Genius.md's Hidden Knowledge #1 already carries this exact figure — flagged there and in this ledger. |

### Genius Patterns 1-20 (genius.md)

| Pattern | Status | Anchor |
|---|---|---|
| 1. Archetype Diagnostic | LIKELY | "Valuable & Boring" / "Addictive & Useless" framing is directly consistent with source #2's "influencer trap" (views, no money) vs. "educator trap" (value, no views) dichotomy — VERIFIED as a two-trap model, but the exact labels "Valuable & Boring" / "Addictive & Useless" are not verbatim in the transcripts on file. |
| 2. Three Buying Motivations Hierarchy | VERIFIED (core claim) | "people don't buy the coaching, they buy the coach" — extractions/Tom Noske/transcript.txt |
| 3. Iceberg Revelation Strategy | LIKELY | Mechanic verified (origin-story-as-inspiration-content, Hormozi example, source #2); "Iceberg" as a label is extraction-coined, not Noske's own term. |
| 4. 90/10 Content Liberation Formula | LIKELY | The exact "90/10" split is not the same split he states in source #2 (which gives a 40/25/25/10 four-way split across audience/inspiration/education/CTA content — VERIFIED, see Signature Moves). The simpler "90% intuitive / 10% conversion" framing may derive from Video 1 (source #4), not independently confirmed here. |
| 5. Broad Mission / Niche Business | VERIFIED (mechanic) | Directly consistent with source #3's "make content about anything... build product around specific audience signal" argument. |
| 6. Anti-Teleprompter Authenticity | VERIFIED | "Don't script because it means you'll be better off the cuff" — extractions/tom-noske/transcript.txt |
| 7. Vulnerability-Trust Accelerator | LIKELY (mechanic) / UNCONFIRMED (bankruptcy example) | The "audience knows all" / neediness-detection principle is VERIFIED (source #1). The specific "bankruptcy, hardship" example is UNCONFIRMED — no such story appears in any transcript on file. |
| 8. Product-First Content Feedback Loop | VERIFIED | 72-hour / 24-48-hour async support-channel-to-content pipeline — extractions/tom-noske/transcript.txt |
| 9. Pre-Sold Pipeline Philosophy | VERIFIED (mechanic) | "There's no pressure. There's no sales calls or high pressure closing" — extractions/Tom Noske/transcript.txt |
| 10. Horsepower Hierarchy | LIKELY | "$2/year" revenue-per-follower threshold not found verbatim; consistent in spirit with Hidden Knowledge #5's $400K/100K-follower example. |
| 11. Results-Reputation Flywheel | VERIFIED (mechanic) | "these are testimonials. These are student wins" defines his CTA content category — extractions/Tom Noske/transcript.txt |
| 12. Live Delivery Iteration Engine | **UNCONFIRMED** | No transcript on file discusses live-vs-pre-recorded delivery. Traces to the pre-existing "Standard extraction" referenced in source #4 (line 8) but not reproduced there. |
| 13. Small Audience LTV Calculator | LIKELY | Sourced to source #4's summary of Video 1 ("4 Ingredients for $10K/Month"); Video 1's raw transcript not found on disk, so the specific $2,400/5,000-follower example is report-sourced, not verbatim-verified. |
| 14. Anti-Volume Pricing Discipline | LIKELY | Same as above — sub-$200/10K-follower framing sourced to source #4. |
| 15. What/Why Free — How/Now Paid Quadrant | LIKELY | Sourced to source #4's summary of Video 1's 4-quadrant model. |
| 16. Content-Revenue Flywheel Architecture | LIKELY | Sourced to source #4's summary of Video 1's "15-20K wall" claim. |
| 17. Demand-First Business Design | VERIFIED | "You can just ask, 'Hey guys, what do you want?'" — extractions/_archive/tom-noske-2/transcript.txt |
| 18. Personal Brand as Compounding Equity | VERIFIED | "It's literally like alchemy... create cash out of thin air"; "$100,000 straight away" — extractions/_archive/tom-noske-2/transcript.txt |
| 19. Express Elevator Effect | VERIFIED | $10M-revenue poker-night invite anecdote — extractions/_archive/tom-noske-2/transcript.txt |
| 20. Talent Magnetism Principle | VERIFIED | Editor "Cal," 1.5-hour commute, 3 days/week — extractions/_archive/tom-noske-2/transcript.txt |

### Hidden Knowledge 1-8 (genius.md)

| Item | Status | Anchor |
|---|---|---|
| 1. 8/10 Failure Rate Is Archetype-Based | **UNCONFIRMED** (exact stat) | See headline claims above. The archetype-predictability mechanic is LIKELY (consistent with source #2's two-trap model). |
| 2. Brand Deals Are a Trap Signal | VERIFIED | "$10,000 for a post... $100,000 off your hard-earned traffic" — extractions/Tom Noske/transcript.txt |
| 3. "Help Younger Me" Framework | LIKELY | Not found verbatim in the 3 transcripts on file; consistent with source #3's "help my brother" framing but that framing targets a real sibling, not a "younger self" abstraction. Likely sourced to Video 1 (source #4) or the pre-existing Standard extraction. |
| 4. Party Vulnerability Transfer | **UNCONFIRMED** | No "vulnerability is contagious" language in any transcript on file. |
| 5. Low Views, High Income Is the Goal | VERIFIED | "100K followers @ $400K/year... 1M followers @ $200K/year by 20x" is a plausible transcript-style figure but was NOT located verbatim in the 3 transcripts on file — reclassify as **LIKELY**, not verified, per the same-session correction below. |
| 6. Niche Anxiety Is Misplaced | LIKELY | Consistent with source #4's $200-400/month vs. $1,000-2,000-cohort sweet-spot logic (Ingredient 3), which requires a specific business niche. |
| 7. Product Creates Content Strategy | VERIFIED | Same async support-channel mechanic as Pattern 8 — extractions/tom-noske/transcript.txt |
| 8. Seven Ingredients Are Non-Negotiable | **UNCONFIRMED** | Not present verbatim in the 3 transcripts on file. Traces to the pre-existing Standard extraction referenced but not reproduced in source #4. |

**Correction note**: on drafting this ledger, Hidden Knowledge #5's "$400K/$200K/20x" figures were re-checked against all 3 primary transcripts and NOT found verbatim — the earlier working label of VERIFIED in the genius.md grounding pass overstates confidence. Corrected here to **LIKELY**; genius.md itself does not repeat the claim as a standalone anchor so no genius.md edit was required, but treat Hidden Knowledge #5 as LIKELY, not VERIFIED, going forward.

### New "Anti-Patterns (Sourced)" section (genius.md, added this pass)

All 7 items are VERIFIED against primary transcripts except the sub-$200 pricing item, which is LIKELY (sourced to the Video-1 extraction report, source #4, not a verbatim transcript — flagged inline in genius.md itself).

### Hall of Fame Exemplars (genius.md)

**LIKELY / illustrative** — the "Unscripted CFO," "Creative Catalyst," and "Generic Guru" scenarios are composite illustrations built to demonstrate pattern application, not real people or real case studies. They should never be cited as real Tom Noske clients or real outcomes. This was true before this repair pass and is unchanged.

### Expert-Specific Quality Rubric (genius.md)

**LIKELY** — a scoring rubric derived from the Genius Patterns above (which carry the ledger status shown in the table above); the rubric itself is an extraction-authored grading tool, not a Tom Noske quote.

### Signature Moves (genius.md)

4 of 5 original bullets are LIKELY (paraphrased mechanics, consistent with source #2/#3 but not verbatim). The new 5th bullet added this pass ("The Content Funnel Split," 40/25/25/10) is **VERIFIED** — extractions/Tom Noske/transcript.txt states this exact split for his own Instagram content.

---

## Net effect of this repair pass

- 0 claims were deleted or hidden.
- 4 new UNCONFIRMED flags were added inline in genius.md (Pattern 7's bankruptcy detail, Pattern 12, Hidden Knowledge #4, Hidden Knowledge #8) plus this ledger's headline-claim table (SKILL.md's $3M+/$130K/$6M/$2-4/8-out-of-10 figures) — none of these were previously flagged anywhere in the skill.
- 13 new VERIFIED groundings were added, each a verbatim quote from a primary transcript with file citation.
- SKILL.md was NOT edited in this pass (out of scope for the failing checks); its unconfirmed headline stats are recorded here so a future pass can either source or soften them.
