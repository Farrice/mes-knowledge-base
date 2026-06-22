---
description: Phase 6 freshness — keep the map a living document with a quarterly light pass + 1–2× yearly deep rebuild, add new word-for-word quotes, flag new phrasing/worries/wishes, write a dated change-log at the top (which becomes its own asset), and optionally register a recurring refresh job via /schedule.
---

# /ctm-refresh — Keep the Map Alive (Freshness Is the Edge)

**This is the map's living-document discipline** ([../references/customer-truth-map-guide.md](../references/customer-truth-map-guide.md), Phase 6; prompt P11 in [../references/prompt-library.md](../references/prompt-library.md)). A Customer Truth Map is not a document you finish — it's one you keep. Language drifts: new tools change what people complain about, new fears surface, old phrasings drop out. This workflow pulls a fresh batch of recent quotes into an existing map, flags what's *new*, notes what's *gone*, and writes a **dated change-log entry at the top** — because over time that log is the asset.

The anchor, word for word from the expert:

> **"A map you refresh is worth ten times a map you build once and forget. The freshness is the edge."**

The discipline has two cadences. A **quarterly light pass** — a short session pulling recent quotes from your 1–2 best sources, watching for new phrasing, new worries, new wishes. A **1–2× yearly deep rebuild** (or on a big market shift) — a fuller re-gather on fresh material, comparing the new map to the old, where **what changed is itself the signal**: a read-out of where the customer's world is moving that competitors aren't tracking. The change-log captures both, and that dated record of how the language shifted becomes a competitive-intelligence artifact nobody else has.

> **Honesty spine.** The quotes in the worked thread below are tagged `[illustrative]` to teach the moves. In a real run every added line is a **harvested**, word-for-word, source-tagged quote — the same verbatim discipline as the original build. A refresh never invents a "trend" quote to make the change-log look interesting; if the language didn't shift, the honest entry says so.

## Pre-Flight Gate

Load [../genius.md](../genius.md) if it is not already hot in this conversation. Do not add a single quote before all six questions below are answered on paper. These are the Decision Framework from [../genius.md](../genius.md), scoped to the refresh job.

1. **Is there an existing map to refresh?** Refresh operates *on* a prior map. No prior map → this is a cold build; run `/customer-truth-map` BUILD instead.
2. **Light pass or deep rebuild?** Quarterly light (recent quotes from 1–2 best sources, watch for new) vs. annual/shift deep (full re-gather, new-vs-old comparison). Pick before you start; they're different scopes.
3. **When was the last refresh?** Read the date at the top of the map. It sets the comparison window and goes into the new change-log entry. No date on the map → add one now as the baseline.
4. **Which 1–2 best sources for the light pass?** The highest-candor, highest-signal rooms from the original build — don't re-sweep everything for a light pass; that's what the deep rebuild is for.
5. **Verbatim discipline armed?** Same as the build — every new line word-for-word, source-tagged, re-issue the rule on drift.
6. **One-shot or recurring?** Is this a single refresh, or should it become a standing quarterly job? If recurring, you'll register it via `/schedule` in Step 4.

## Skill Acquisition

- **Always:** [../genius.md](../genius.md) (Pattern 11 freshness-as-the-edge, Signature Move 7 "date the top of the map", the rubric) + the existing map.
- **Gathering the fresh batch:** [../references/tool-wiring.md](../references/tool-wiring.md) — Apify Reddit (budget-gated) → NotebookLM → Playwright → WebFetch → own-data, then `/ctm-clean` on the returns. Same fallback chain as the build.
- **The deep rebuild surfaces a genuinely new audience split:** consider `/ctm-triangulate` if you're now pulling from multiple distinct sources.
- **The refresh reveals new real-world claims** (a new tool everyone names, a new stat): the Step 5.5 Verification protocol (`directives/verification-agent-protocol.md`) before any output asserts them.
- **Make it recur:** `/schedule` (the scheduled-routine skill) to register a quarterly cloud job — see Step 4 and [../references/tool-wiring.md](../references/tool-wiring.md) Layer 4.

## Execution

Walk the refresh in four steps via prompt **P11**. A worked example threads through — audience: **first-time homebuyers in the San Fernando Valley who keep getting outbid**, doing a quarterly light pass against the original map (dated 2026-03). The quotes below are tagged `[illustrative]`; a real run uses harvested lines.

### Step 1 — Gather the fresh batch (verbatim, source-tagged)
**Move.** For a light pass, pull recent quotes (last quarter) from your 1–2 best sources; for a deep rebuild, re-gather broadly on fresh material. Run them through `/ctm-clean` so every new line is word-for-word with a source tag and a date. Keep the batch separate from the prior map for now — you need to *compare*, not just absorb.

**Diagnostic:**
1. Is every new line recent (inside the comparison window) and source+date tagged?
2. Did I pull from the same best sources as the baseline, so I'm comparing like with like?

### Step 2 — Merge, then flag NEW and note GONE (P11 core)
**Move.** Run prompt **P11** against the prior map + the new batch. Four instructions, in order: (1) add the new quotes to the right categories, keeping original wording and source tags; (2) **flag NEW phrasing, NEW worries, and NEW wishes** that weren't in the prior map; (3) **note anything in the prior map that now seems dated** or has dropped out of the language; (4) hold the comparison for the change-log in Step 3. The flags are the whole value — a refresh that just appends quotes without marking what shifted has wasted the pass.

**Diagnostic:**
1. What language is in this batch that was *not* in the prior map? (That's a NEW flag.)
2. What did the prior map lead with that nobody is saying anymore? (That's a GONE note — and often the sharpest signal.)

**Template (vary the rows; never invent a "trend"):**

| Change type | The shift (harvested) | Category | What it signals |
|---|---|---|---|
| **NEW worry** | *"now they want me to waive the appraisal too"* `[illustrative]` | PAINS | escalation of the outbid problem → new objection to handle |
| **NEW phrasing** | "rate-locked" replacing "high interest" `[illustrative]` | THINK | the customer's vocabulary moved; copy should follow |
| **GONE** | the 2026-03 "is now even a good time to buy" doubt has dropped off | FEEL | that fear resolved or normalized → stop leading with it |

### Step 3 — Write the dated change-log entry (the asset)
**Move.** At the **top of the map**, write a dated entry: what was added, what shifted, what dropped out, and — in one or two lines — **what it signals about where this customer's world is moving.** Stack it above the prior entries; never overwrite them. The running, dated log is the competitive-intelligence artifact: anyone can build a map once, but the *trajectory* of the language is what competitors aren't tracking.

**Diagnostic:**
1. Does the entry say what *changed*, not just what the map now contains?
2. Is there a one-line "what this signals" read — the part that turns a log into intelligence?

**Template (vary; keep the dated-stacked structure):**
```
## Change Log
### 2026-06 — quarterly light pass (sources: r/FirstTimeHomeBuyer, Zillow reviews)
ADDED: 14 new lines. NEW worry: appraisal-waiving now a recurring objection (PAINS).
NEW phrasing: "rate-locked" displacing "high interest" (THINK). GONE: the "is it even a
good time to buy" doubt has dropped off (FEEL) — that fear has normalized.
SIGNAL: the fight has moved from *whether* to buy to *how* to win the bid — lead the next
quarter's copy on the bid, not the decision.
### 2026-03 — initial build (cold)
[prior entry retained]
```

### Step 4 — Optional: register the recurring refresh job
**Move.** "The freshness is the edge" only pays off if the refresh actually happens — so make it a standing job, not a good intention. Use **`/schedule`** (the scheduled-routine skill) to register a recurring quarterly run that re-fires this workflow. Per [../references/tool-wiring.md](../references/tool-wiring.md) (Layer 4) and the system scheduling directives, scheduled routines are **cloud cron agents and are user-triggered to set up** — you propose the cadence and command, Farrice confirms, and the routine runs on its own thereafter. State it explicitly rather than promising a refresh you have no mechanism to deliver.

**Diagnostic:**
1. Did I register a real recurring job (or honestly flag that it's a one-shot), rather than just *saying* "refresh quarterly"?
2. Does the scheduled command point at the right map file and the right 1–2 best sources?

> *Proposed routine: quarterly `/ctm-refresh` on the FTHB map, sources r/FirstTimeHomeBuyer + Zillow reviews, first run 2026-09. Register via `/schedule`? (cloud cron, user-confirmed.)*

## Content-Type Adaptations

The two cadences are universal; **how often and how deep** you refresh shifts by how fast the audience's language churns. Use this to set the cadence per map, not a blanket "quarterly."

| Refresh cadence | When it fits | What the pass looks like |
|---|---|---|
| **Quarterly light** (default) | Stable audience, steady market | 1–2 best sources, recent quotes, flag NEW/GONE, change-log entry. ~30–45 min. |
| **Monthly light** | Fast-moving niche (AI tools, crypto, trending consumer) | Same light scope, tighter window; vocabulary moves monthly here. Schedule monthly. |
| **Event-triggered** | A known catalyst (rate change, competitor launch, season) | Fire on the event, not the calendar — the shift *is* the reason to refresh. |
| **1–2× yearly deep rebuild** | Every map, at least annually | Full re-gather on fresh material; build a new map, compare to old; *what changed is the signal*. May invoke `/ctm-triangulate`. |
| **On a big market shift** | Macro change reshapes the whole problem | Deep rebuild out of cycle; expect large GONE notes — old fears resolved, new ones born. |
| **Pre-launch spot-refresh** | About to ship copy/content/an offer off the map | Targeted light pass on the exact gap you're building on, so you launch on current language. |

## Output Requirements

Return three artifacts (four if scheduling):
1. **The updated map** — prior map + new word-for-word, source+date-tagged quotes sorted into the six categories; original wording preserved throughout.
2. **The change-flags** — explicit NEW phrasing / NEW worries / NEW wishes and the GONE notes (what dropped out), each tied to a category.
3. **The dated change-log entry** — stacked at the top above prior entries: added / shifted / gone + the one-line "what this signals" read.
4. **(If recurring) the scheduled-job proposal or confirmation** — the `/schedule` routine (cadence, command, sources, first run), flagged as cloud / user-confirmed.

## Quality Gate

Score against the [../genius.md](../genius.md) rubric; name the matching anchor for any dimension ≥8 (can't name it → lower it).
- **Verbatim Integrity (the veto)** — every newly added line is real, word-for-word, source-traceable; *no "trend" quote was invented to make the change-log look alive.* Any fabricated or paraphrased line is an automatic fail, regardless of every other score.
- **Freshness Discipline** — a dated change-log entry exists at the top (stacked, not overwritten), with NEW flags, GONE notes, and a "what this signals" read; a refresh that only appends quotes caps the score.
- **Unprompted Sourcing** — the fresh batch is mostly unsolicited recent language, pulled from the established best sources, not survey-shaped.
- **Signal Honesty** — the "what this signals" read is grounded in the actual NEW/GONE evidence; if nothing meaningfully shifted, the entry honestly says so rather than manufacturing movement.
- **Mechanism Reality** — if the refresh is claimed to be recurring, a real `/schedule` job is registered (or it's honestly flagged one-shot); no promising a quarterly cadence with no mechanism behind it.

**Self-check (one line):** *Could a skeptic compare the prior map to the updated one, find every NEW/GONE flag backed by a real dated quote, and read the change-log as an honest record of how the language actually moved?* If yes, ship. If no, the unbacked flag goes back to Step 2 for a real line — and if "recurring" was claimed, confirm the `/schedule` job actually exists.
