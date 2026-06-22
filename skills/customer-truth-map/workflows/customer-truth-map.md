---
description: Front-door conductor for the Customer Truth Map — runs the whole voice-of-customer arc end-to-end (BUILD a map · APPLY it to copy/content/offers · REFRESH it) by orchestrating the 12 subroutine workflows, grounded by memory + Recall and gated by verbatim integrity.
---

# /customer-truth-map — The Voice-of-Customer Conductor

**This is the end-to-end engine** (alias `/ctm`). Point it at a customer + problem and it walks the six phases in order — *gather real language → clean to signal → build the map → find the deeper job + the gaps → put the map to work → keep it fresh* — and hands you a finished, refreshable map plus the first map-grounded outputs. It **orchestrates** the granular workflows (`/ctm-scope`, `/ctm-gather`, `/ctm-clean`, `/ctm-map`, `/ctm-jobs`, `/ctm-gaps`, the `/ctm-to-*` put-to-work trio, `/ctm-triangulate`, `/ctm-refresh`, `/ctm-deepen`); it does **not** reimplement them. Reach for a single subroutine when one phase needs surgery; reach for this when someone needs the whole arc built.

## Pre-Flight Gate

Load `../genius.md` if it is not already hot in this conversation, then read the canonical source ([../references/customer-truth-map-guide.md](../references/customer-truth-map-guide.md)) where the guide ever disagrees with genius.md — the guide wins. Do not produce a single line of output before the six Decision-Framework questions are answered on paper. This conductor owns the whole pipeline, so it needs every one.

1. **One customer, one problem cluster?** Is the target narrow enough — the *"solo bookkeeper who just lost a big client"* test, not "small business owners"? Broad → narrow it, or split into one map per customer (they won't blur). This decides scope before anything is gathered.
2. **Do we already know this audience?** Front-load Recall + `memory_facade.py` (Layer 0 below) — we may already hold real language or a prior map. Never re-gather what we have.
3. **Real sources named?** Specific communities/threads/own-data, not "the internet." Unprompted talk (reviews, threads, DMs) prioritized over interview answers.
4. **Verbatim discipline armed?** The word-for-word rule (genius.md Pattern 4) is stated and will be re-issued on drift. This is the unbreakable line — fabricated or paraphrased customer language is an automatic fail.
5. **Which output is this feeding?** Copy / content / positioning / offer — so the map is *put to work*, not admired. Determines the APPLY branch.
6. **Fresh or stale?** Existing map to refresh/compare, or a cold build? Determines the mode.

**Mode routing (the answer to Q5/Q6 picks the branch):**
| Mode | When | Runs |
|---|---|---|
| **BUILD** | No usable map yet | Layer-0 ground → Phases 1–4 → finished map |
| **APPLY** | A map exists, you need deliverables | Phase 5 only (`/ctm-to-*`) on the existing map |
| **REFRESH** | A map exists and may be stale | Phase 6 (`/ctm-refresh`, optional `/ctm-triangulate`) |

A cold start that also wants outputs runs **BUILD → APPLY** in one arc. Default for an unspecified ask is BUILD.

## Skill Acquisition

- **Always:** `../genius.md` (the six phases, 12 patterns, honesty spine, 9-criterion rubric) + the prompt library [../references/prompt-library.md](../references/prompt-library.md) (P1–P11) + the tool wiring [../references/tool-wiring.md](../references/tool-wiring.md) (Layers 0–4, budgets, fallback chain).
- **Each phase:** the matching subroutine workflow — `./ctm-scope.md`, `./ctm-gather.md`, `./ctm-clean.md`, `./ctm-map.md`, `./ctm-jobs.md`, `./ctm-gaps.md`, `./ctm-to-copy.md`, `./ctm-to-content.md`, `./ctm-to-offer.md`, `./ctm-triangulate.md`, `./ctm-refresh.md`, `./ctm-deepen.md`. Load the one you are running; do not preload all twelve.
- **Heavy mining at scale:** `/buyer-sourcer` (luke-iha-avatar-machine) — `/ctm-gather` delegates the mine.
- **Surface → identity-level depth:** `/mcraney-deep-canvass` + consumer-posture — via `./ctm-deepen.md`.
- **Put-to-work hand-offs:** `/copy-engine`, `/ghostwrite`, master-copywriter (copy); `/novelty-forge`, `/parallax`, `/diandra-*` (content); `/build-bos`, positioning skills (offer).
- **Fact-bearing outputs:** the Step 5.5 Verification protocol (`directives/verification-agent-protocol.md`) — any real-world claim riding with the language.

## Execution

Run the modes below. Each phase is **delegated to its subroutine** — this conductor sequences, grounds, and gates; it does not rewrite the phase logic. A worked thread runs through BUILD: the **solo bookkeeper who just lost a big client** (the guide's own narrowness exemplar).

> **Honesty note for every worked line here:** any example customer quote in this file is tagged `[illustrative]` and stands in for the structure only. **Real runs use harvested verbatim quotes only** — word-for-word, source-tagged, never invented (genius.md, the honesty spine).

### Layer 0 — Ground before anything (free, always first)
Before BUILD/APPLY/REFRESH, run both — we may already hold this map or its language:
```bash
python3 execution/memory_facade.py "<customer + problem>" --top 10
```
Plus Recall via MCP: `mcp__recall__search { "query": "<customer + problem>" }`. Report every store that was degraded/skipped (never silently drop one). Feed the results into Pre-Flight Q2 and into `/ctm-scope` P1 so each named problem is tagged `[assumed]` vs `[evidenced: source]`.

### Mode BUILD — cold start → finished map (Phases 1–4)
1. **`/ctm-scope`** (Phase 1.1–1.2). Produces the narrowed customer definition, 15–20 problems in the customer's voice (each `[assumed]`/`[evidenced]`), the 2–3 to research deeply, and the sourced list of *where they talk* with candor scores + recommended capture tools. Worked: target locked to *solo bookkeeper who just lost a big client*; problems include `[illustrative]` *"I'm scared I built my whole income on one client."*
2. **`/ctm-gather`** (Phase 1.3, the wired one). Collects raw, unedited verbatim language down the fallback chain (Apify Reddit → NotebookLM → Playwright → WebFetch → research.py → manual paste) plus own-data ingest. **Cost-gate honesty:** before any paid call, surface the projected $ and get an explicit yes; never retry a denied call. Output: one raw corpus with source tags + permalinks.
3. **`/ctm-clean`** (Phase 2). Verbatim signal extraction (P3) + the verbatim-integrity gate: every kept line is a substring of its source chunk; drift → discard + re-issue the word-for-word rule.
4. **`/ctm-map`** (Phase 3). Sort into Say/Think/Feel/Do + Pains/Gains, name 2–3 patterns each, flag vivid/repeated quotes, circle every Do-category workaround as an unmet-need flag.
5. **`/ctm-jobs`** (Phase 4.1). Reframe each pain to a Job: *"When [situation], I want to [motivation], so I can [desired outcome]."* (genius.md exemplar: *"I keep forgetting to follow up with leads"* → *"When a promising lead goes quiet, I want to stay on their radar without feeling pushy, so I can win the work without nagging"* — a feature request promoted to a positioning angle).
6. **`/ctm-gaps`** (Phase 4.2). Pain/Job → Current Fix → The Gap (+ Gap-Width 1–5, sorted descending). The widest rows are the shortlist passed to Phase 5.
7. **(Optional) `/ctm-deepen`.** When surface patterns aren't enough, hand the map to `/mcraney-deep-canvass` + consumer-posture for identity-level resistance. Run only when the deliverable needs belief-level depth.

### Mode APPLY — existing map → deliverables (Phase 5)
Take the finished map (Q5 names the target). Run the matching put-to-work subroutine — never write the copy/content/offer from scratch here; hand the grounded payload to the production engine:
- **`/ctm-to-copy`** → 10 quotes mapped to slots (headline/subhead/objection/proof) + 8 headlines in the customer's register → `/copy-engine` / master-copywriter.
- **`/ctm-to-content`** → 15 grounded content ideas (each carrying its source quote) + a long-form outline from the widest gap → `/novelty-forge` / `/parallax` / `/diandra-*` (the map supplies the held belief + the real language).
- **`/ctm-to-offer`** → 3–5 positioning angles + 3 offer extensions tied to specific gaps (simple vs. major flagged) → `/build-bos` / positioning skills.

### Mode REFRESH — keep the map alive (Phase 6)
- **`/ctm-refresh`** — quarterly light pass / 1–2× yearly deep rebuild; add new quotes (word-for-word, source-tagged), flag new phrasing/worries/wishes, note what dropped out, write a dated change-log entry. *What changes is itself the signal.* Register the recurring job via `/schedule`.
- **`/ctm-triangulate`** (when built across 2+ communities) — merge maps into Consistent Truths (high-confidence) vs Source-Specific (lower-confidence, labeled by source).

### Close-out (every mode)
Save the map as a plain markdown file the user keeps open (a project file for live maps, `../references/worked-exemplar-<audience>.md` for shipped examples). Schedule the refresh. Run the QA gate below, then finalize.

## Content-Type Adaptations

The map is asset-agnostic; the *put-to-work* branch changes by what the map feeds. This is the domain-agnostic key (full version: [../references/cross-domain-adaptations.md](../references/cross-domain-adaptations.md)).

| Deliverable the map feeds | How the conductor routes |
|---|---|
| **Landing / sales page** | APPLY → `/ctm-to-copy` (quote→slot: widest-gap quote = headline; objection quotes = the FAQ) → `/copy-engine`. |
| **Content series / newsletter** | APPLY → `/ctm-to-content` (one idea per source quote) → `/novelty-forge` / `/parallax`; the map's held belief seeds each angle. |
| **Positioning / new offer** | APPLY → `/ctm-gaps` first, then `/ctm-to-offer` (widest gap → angle); `/ctm-deepen` if the wedge needs identity-level proof → `/build-bos`. |
| **Cold outreach / DMs** | BUILD with own-data (DMs/sales calls) weighted heaviest, then `/ctm-to-copy` for the opening line in their exact words. |
| **Ad / VSL** | `/ctm-to-copy` for the hook + objection-handlers; route any stat in the script through the Step 5.5 Verification protocol before shipping. |
| **Multi-community / B2B with sub-segments** | run BUILD per community → `/ctm-triangulate` → APPLY only off Consistent Truths for core messaging. |
| **Living competitive-intel artifact** | REFRESH on a `/schedule` cadence; the dated change-log becomes the asset competitors don't have. |

## Output Requirements

Return, scoped to the mode:
1. **Pre-Flight header** — the six answered Decision-Framework questions + the chosen mode and the Layer-0 grounding receipt (what memory/Recall already held; degraded stores reported).
2. **The artifact** — BUILD: the finished six-category map (Say/Think/Feel/Do + Pains/Gains) with named patterns, circled workarounds, JTBD reframes, and the gap-width shortlist, every quote source-tagged. APPLY: the grounded deliverable payload + the named hand-off engine. REFRESH: the updated map + a dated change-log entry.
3. **The run receipt** — which subroutines fired, which tools fired and their cost (honest fallback-chain log), and any cost-gate pauses surfaced for approval.

## Quality Gate

Score with the **9-criterion rubric in `../genius.md`** (full instrument: [../references/quality-rubric.md](../references/quality-rubric.md)). Score 1–10; name the matching anchor for any score ≥8 — can't name it, lower it.
- **Verbatim Integrity** — every quote real, word-for-word, source-traceable; zero paraphrase/invention.
- **Unprompted Sourcing** — language mostly unsolicited (reviews/threads/DMs/own-data), not survey-shaped.
- **Narrowness** — target specific enough to produce non-blurry patterns (the bookkeeper test).
- **Map Completeness** — all six categories populated; 2–3 named patterns each; vivid/repeated flagged.
- **Do-Category Mining** — workarounds surfaced and circled as unmet-need signals.
- **Job Depth** — pains reframed to outcome-level jobs that open positioning, not just features.
- **Gap Ranking** — gap table built; widest rows named as the shortlist with a reason.
- **Put-to-Work Fidelity** — outputs carry the customer's voice; each grounded in a named quote/pattern.
- **Freshness Discipline** — dated change-log present (or scheduled); cross-source confidence labels applied.

**Verbatim-Integrity veto (non-negotiable).** A single fabricated or paraphrased customer quote is an **automatic fail**, regardless of every other score. The whole advantage of this system is real language in, organized language out. AI sorts the gold; it never mints it. If any quote can't be traced to a source line, the map fails until it's pulled or replaced with a real one.

**Self-check (one line):** *Could the customer read this map back and say "yes, that's exactly how I'd put it" — because every word is theirs?* If yes, ship. If no, the failing phase goes back to its subroutine.
