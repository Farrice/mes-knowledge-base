---
description: Phase 6 merge — consolidate 2+ maps built from different sources about the same customer into ONE confidence-labeled map that splits Consistent Truths (high-confidence, build core messaging here) from Source-Specific (lower-confidence, hold loosely, name the source).
---

# /ctm-triangulate — Merge the Maps Without Flattening Them

**This is the map's confidence layer** ([../references/customer-truth-map-guide.md](../references/customer-truth-map-guide.md), Phase 6; verbatim prompt P10 in [../references/prompt-library.md](../references/prompt-library.md)). You have two or more Customer Truth Maps built from *different* sources about the *same* customer and problem — say a Reddit map, a review-site map, and a sales-call map. This workflow merges them into one consolidated map, but the merge is not a pile: it **separates what's consistent across sources (high-confidence) from what showed up in only one (lower-confidence)** and labels every pattern accordingly.

The reason the split matters is the whole point of triangulating: a map from a single community can mislead, because **every forum has its own culture, its loud voices, and its blind spots.** A pain that's screamed about on one subreddit may be invisible on a review site not because it isn't real, but because that crowd self-selects for it. Consolidate naively and you over-weight one room's obsessions and call them the market. The signature move here — **confidence-label every pattern, never flatten** — is what turns three partial views into one honest one.

> **Honesty spine.** The quotes in the worked thread below are tagged `[illustrative]` to teach the moves. In a real run every line is a **harvested**, word-for-word, source-tagged quote carried over from the maps being merged. Triangulating never invents a "consensus" quote to bridge sources; if a pattern only appears in one source, it is labeled Source-Specific — it does not get promoted to a truth because it would be convenient.

## Pre-Flight Gate

Load [../genius.md](../genius.md) if it is not already hot in this conversation. Do not merge a single category before all six questions below are answered on paper. These are the Decision Framework from [../genius.md](../genius.md), scoped to the merge job.

1. **Two or more maps, same customer, same problem cluster?** Triangulation needs ≥2 maps about the *one* narrow audience. Maps of different audiences don't merge — they stay separate. One map only → there's nothing to triangulate; go run the build across a second source first.
2. **Is each source named and distinct?** Every map must carry its provenance (which community / own-data set it came from) and represent a genuinely different room. Two maps from the same subreddit aren't triangulation; they're one source twice.
3. **Are the maps verbatim-clean?** Each map being merged must already have passed `/ctm-clean` (real quotes, source tags intact). Garbage in poisons the consensus — confirm before merging.
4. **Same six categories across all maps?** Say / Think / Feel / Do + Pains / Gains. Merge happens category-by-category; mismatched structures get normalized first.
5. **What's the "most/all" threshold?** Decide before you start what counts as Consistent — present in *all* sources, or in *most* (e.g. 2 of 3). State it; it sets the confidence bar.
6. **Which output does the consolidated map feed?** Copy / content / positioning / offer — the Consistent Truths are where core messaging gets built, so know what's downstream before you label.

## Skill Acquisition

- **Always:** [../genius.md](../genius.md) (Pattern 10 triangulation, Signature Move 6 "confidence-label everything cross-source", the rubric) + every map being merged.
- **A source map is thin or stale:** `/ctm-refresh` it before merging — a stale source drags the consensus toward last year's language.
- **You only have one map:** `/ctm-scope` → `/ctm-gather` a second, *different* source first, then come back; there's no triangulating a single view.
- **A real-world claim rides along with a pattern** (a stat, a named competitor, an event quoted across sources): the Step 5.5 Verification protocol (`directives/verification-agent-protocol.md`) before any output asserts it — cross-source agreement on *language* is not cross-source verification of *fact*.
- **The consolidated map then needs depth:** `/ctm-deepen` (belief/posture/verified-claim layer); to put it to work: `/ctm-to-copy` · `/ctm-to-content` · `/ctm-to-offer`.

## Execution

Walk the merge category by category, then label. A worked example threads through — audience: **first-time homebuyers in the San Fernando Valley who keep getting outbid**, merged from three maps: a **Reddit** map, a **Zillow/review-site** map, and a **sales-call-transcript** (own-data) map. The quotes below are tagged `[illustrative]`; a real run uses harvested lines carried from each source map with its tag intact.

### Step 1 — Normalize and stack the sources
**Move.** Lay the maps side by side, category by category. Confirm all use the same six categories and that every quote still carries its source tag. Do **not** start merging language yet — first make the three columns comparable. Run prompt **P10** with each map pasted under a clear header naming its source.

**Diagnostic:**
1. Is every quote still traceable to its origin source? (If a tag got lost in transit, restore it before merging — provenance is the input to confidence.)
2. Are the sources actually different rooms, or did two of them sample the same community?

### Step 2 — Split Consistent Truths from Source-Specific (the core move, P10)
**Move.** Within each category, sort every pattern into one of two buckets:
- **CONSISTENT TRUTHS** — the pattern/language appears across most or all sources (per your Pre-Flight threshold). Treat as **high-confidence. This is where you build core messaging** — the headline, the lead, the positioning spine. When the same fear or wish surfaces in three different rooms that don't talk to each other, that's not noise; that's the market.
- **SOURCE-SPECIFIC** — the pattern shows up in only one source. Treat as **lower-confidence: note it, name the source, hold it loosely.** It's not worthless — a single-source insight is often the seed of a **sub-group play** (a message for exactly the crowd that room represents) — but you do not build the core on it, because it may be one community's culture, not the customer's truth.

**Diagnostic:**
1. For each pattern: in how many sources does it appear? (That count is the confidence label — don't eyeball it.)
2. Is a single-source pattern genuinely customer truth, or is it that *room's* loud-voice obsession / blind spot? Name which, in the source note.

**Template (vary the rows; never invent a cross-source quote):**

| Category | CONSISTENT TRUTH (high-confidence — build here) | SOURCE-SPECIFIC (lower-confidence — name the source) |
|---|---|---|
| **PAINS** | *"we keep losing to all-cash offers"* `[illustrative]` — all 3 sources | *"the agent ghosted me after closing"* `[illustrative]` — review-site only (a Zillow-crowd grievance; useful for a post-close-trust sub-message) |
| **FEEL** | self-blame / "am I bad at this" — all 3 sources | *"my parents keep pressuring me"* `[illustrative]` — sales-calls only (own-data, said when guard is down; a real but sub-group emotion) |
| **GAINS** | "just want to stop renting" — Reddit + sales-calls | *"want a place my dog can run"* `[illustrative]` — Reddit only |

Fill across all six categories. Every row carries either an all/most tag or a named single source — **no pattern lands unlabeled.**

**Worked note (FTHB):** "we keep losing to all-cash offers" appears in the subreddit, the review site, *and* the sales calls — three rooms that never met. That's the highest-confidence pattern in the consolidated map, so it earns the headline. "Want a place my dog can run" is real but Reddit-only; it stays a Source-Specific note, good for one segment's ad, never the core promise.

### Step 3 — Write the consolidated map + confidence preamble
**Move.** Assemble the merged six-category map with the two-bucket structure intact, and open it with a short **confidence preamble**: which sources were merged, the most/all threshold used, and a one-line read on each source's known bias (the culture / loud voices / blind spots it brings). This preamble is what lets a downstream user trust the labels instead of re-litigating them.

**Diagnostic:**
1. Could a reader tell, for any pattern, how confident to be and why — without asking you?
2. Did anything get quietly flattened — a single-source line slipped into a "truth" because it was vivid? (If so, demote it.)

## Content-Type Adaptations

The two-bucket split is universal; **what a given source type tends to over- and under-represent** changes how you weight it. Use this to read each source's bias before you trust its single-source patterns.

| Source type | What it over-represents | What it tends to miss / how to weight it |
|---|---|---|
| **Reddit / forums** | Loud, emotional, edge-case grievances; the most articulate complainers | Quiet majority and satisfied users; treat unique-to-Reddit patterns as sub-group, not market, until a second source confirms. |
| **Review sites (G2 / Zillow / Amazon)** | Extremes — delighted or furious; post-purchase regret and praise | The pre-purchase confusion and mid-journey doubt; strong on outcomes, weak on the deciding moment. |
| **Sales / discovery-call transcripts (own-data)** | Candid, off-guard language; the real objection said out loud | Only your funnel's self-selected prospects; high candor, narrow sample — gold for FEEL, biased on reach. |
| **Support tickets / emails (own-data)** | Active, unresolved pain; the workaround-in-progress | Happy silent users and pre-sale fears; over-indexes on problems, under-indexes on gains. |
| **Social comments / DMs** | Reactive, in-the-moment takes; aspiration and identity signals | Depth and sequence; fragments, not narratives — confirm any single-source pattern elsewhere. |
| **YouTube comments** | Topic-triggered confusion ("wait, how do you…") | Anything off the video's frame; the source's blind spot is whatever the creator didn't cover. |

## Output Requirements

Return three artifacts:
1. **The confidence preamble** — sources merged, the most/all threshold used, and a one-line known-bias read per source.
2. **The consolidated map** — all six categories, each split into CONSISTENT TRUTHS (high-confidence) and SOURCE-SPECIFIC (lower-confidence, source named), every quote source-tagged and word-for-word.
3. **The build-here shortlist** — the 2–3 highest-confidence consistent patterns flagged as the core-messaging foundation, with a one-line note on which Source-Specific patterns are sub-group candidates.

## Quality Gate

Score against the [../genius.md](../genius.md) rubric; name the matching anchor for any dimension ≥8 (can't name it → lower it).
- **Verbatim Integrity (the veto)** — every quote in the consolidated map is real, word-for-word, source-traceable; *no "consensus" quote was invented to bridge sources.* Any fabricated or paraphrased line is an automatic fail, regardless of every other score.
- **Cross-Source Confidence (Freshness Discipline)** — every pattern is labeled Consistent (count the sources) or Source-Specific (name the source); nothing is flattened into one undifferentiated list. An unlabeled pattern caps the score.
- **Narrowness** — all merged maps cover the *same* narrow customer; no blended-audience mush.
- **Bias-Read Honesty** — each source's culture / loud-voice / blind-spot bias is named in the preamble, so single-source patterns are weighted, not trusted by default.
- **Build-Here Discipline** — the core-messaging shortlist is drawn only from high-confidence Consistent Truths; no single-source line was promoted because it was vivid.

**Self-check (one line):** *Could a skeptic pull any pattern from the consolidated map, count how many of the named sources it actually appears in, and find the label matches — with no invented consensus quote anywhere?* If yes, ship. If no, the mislabeled pattern goes back to Step 2 for an honest count.
