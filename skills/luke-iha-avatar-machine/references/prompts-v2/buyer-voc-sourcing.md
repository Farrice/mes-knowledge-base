---
name: "Luke Iha — Buyer VOC Sourcing (Specific Language Pack)"
source_prompt: born-v2
skill: luke-iha-avatar-machine
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are working **Luke Iha's** Specific-Language / "4S" sourcing method. The system's genius patterns can predict the *structure* of a market's wound — but the **specific language** must be pulled directly from the market itself: reviews, forum comments, Reddit threads, YouTube comments, ad libraries. "When you know what the market will react to, you know what to look for, you find it more easily, you sell more." This workflow **executes real research** — it does not generate voice-of-customer from contextual/training knowledge. Invented VOC presented as pulled is an auto-fail; every soundbite must be verbatim with a source URL or handle.

## Input Required

- `[MARKET]` — the target market (required)
- `[SOURCES]` — at least one place to mine: product reviews (Amazon/ClickBank/Digistore), a competitor's offer/funnel, a subreddit, a YouTube channel's comments, an email list (if the user has audience access)
- `[TOOLS AVAILABLE]` — Perplexity (primary research engine) / Playwright (for JS-rendered or login-gated sources — FB Ad Library, gated forums) / Apify (optional, scale review-scraping) — note which are budget-gated per the relevant usage-policy directives

## Execution Protocol

### Phase A — Execute the mining (real tools, not recall)
1. Fire real research against the named sources. Recommended: dispatch as an isolated sub-agent (raw scraping pollutes a main context window) with a tight objective — mine ≥30 verbatim soundbites + 30–40 existing hooks, every line source-tagged, no invented language, no typo cleanup (raw phrasing is the gold).
2. **Perplexity** for synthesis across reviews/forums/comments — query for verbatim complaints, objections, failed solutions, and desires from real buyers; pull the cited source URLs.
3. **WebFetch** the top 3–8 cited pages in full — Perplexity summarizes, WebFetch gets the raw voice.
4. **Playwright** for JS-rendered/login-gated sources (FB Ad Library, gated forums, the offer's own funnel) — never WebFetch these.
5. **Apify** only at scale, budget-gated, falling back to Perplexity near budget limits.

### Phase B — Tag and harvest
6. **Tag every verbatim soundbite**: emotion · objection · failed-solution · desired-outcome · belief. Preserve raw phrasing, typos included.
7. **Survey option** — if the user has list/audience access, select 8–12 of the most relevant Master Survey Questions across the Problem / Solution / Past-Experience / Belief / Constraint groups.
8. **Hook harvest** — 30–40 existing high-performing hooks from the niche, each sourced.

### Phase C — Package
9. Assemble the **Specific-Language Pack**: soundbites grouped by tag + hook bank + survey raw data (if collected) + a full source list for traceability.
10. **Floor check** before delivery — the pack must have ≥15 distinct source URLs and zero unlabeled `[MODELED]` entries. If it doesn't, re-mine before handing off; do not pad with invented language to hit the count.

## Output Contract

- A tagged VOC soundbite bank (verbatim, ≥30 lines) grouped by tag (emotion/objection/failed-solution/desired-outcome/belief).
- A hook bank (30–40 lines), each sourced.
- Optional survey response data, if collected.
- A full source list (≥15 distinct URLs/handles) for traceability.
- Zero AI-generated or paraphrased lines presented as VOC.

## Output Skeleton

```
## Specific-Language Pack — [Market]

### Soundbites (verbatim, tagged)
| Soundbite | Source | Tag |
|---|---|---|
["verbatim phrase"] | [URL/handle] | [emotion/objection/failed-solution/desired-outcome/belief]
[... ≥30 rows]

### Hook Bank (30–40, sourced)
| Hook | Source |
|---|---|
[...]

### Survey Data (if collected)
[raw responses, grouped by question category]

### Source List
[≥15 distinct URLs/handles]

### Floor Check
Source URLs: [count] | [MODELED] flags: [count — must be 0]
```

## Quality Gate

- [ ] Every soundbite has a real, checkable source URL/handle — none presented as VOC without one?
- [ ] Raw phrasing preserved (typos, awkward grammar) rather than cleaned up into marketer-speak?
- [ ] At least 30 tagged soundbites and ≥15 distinct sources, with zero `[MODELED]` entries in the delivered pack?
- [ ] Sources actually mined via live tools (Perplexity/WebFetch/Playwright/Apify), not answered from training knowledge?
- [ ] JS-rendered or login-gated sources were pulled via Playwright, never WebFetch?

## Creative Latitude

There is no creative latitude on the language itself — the entire point is that it's pulled, not written. The craft here is in *sourcing strategy*: knowing where a given market actually talks in its rawest voice (Reddit for taboo fears, reviews for post-purchase disappointment, YouTube comments for beliefs-in-the-wild) and mining the right well rather than the convenient one.

## Deploy When

- Before any Manifold delivered to a client — this is the difference between a 6 and a 9 on the "specific language" rubric criterion.
- Feeding stage 1 (Build-a-Buyer) and stage 12 (Specific-Language pack) of `/avatar-manifold`.
- Any time existing copy reads as generic marketer-speak and needs re-grounding in real market voice.
