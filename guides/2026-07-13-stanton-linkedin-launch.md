---
date: 2026-07-13
session: stanton-linkedin-launch
tier: operator-guide
status: enriched
---

# Stanton Deployment + LinkedIn Receipt Arc — What We Built 2026-07-13 and How to Use It

> The Stanton enrichment session shipped a conductor (`/stanton-produce`), a proof run (the Receipt Arc launch sequence for LinkedIn), and rewrote both dedicated Stanton guides. This is the **library entry point**, not the depth doc — the full leverage map lives in `skills/andrew-stanton-audience-engineering/USER-GUIDE.md` (how to use it) and `OPERATORS-GUIDE.md` (how the system runs it underneath you). Read those before extending anything. Commits: `17d613950` (guides), `301b25dc2` (launch sequence).

---

## The mental model (read this once, everything else follows)

Stanton is the **story-uncovering + audience-engagement layer**: what a piece is really about (the premise-sentence), who its protagonist is (the spine), where attention drops (the clamp), what to fix (the root, not the symptom). Three ideas from this session:

1. **Composition, never rebuild.** `/stanton-produce` conducts the engines you already own — it sets the architecture and runs QA, then routes line-writing to whichever engine owns the format. If it ever starts writing what copy-engine or parallax already write, it has failed by its own gate.
2. **"Pixar-level" is now operational, not aspirational.** The eight-point Stanton-Grade Gate (`references/exemplars.md`) runs as hard vetoes before delivery. Proven live: it caught two Receipt Arc loop lines that spoiled their own payoff — clean, on-voice lines the old pipeline would have shipped.
3. **A content batch is a hidden series.** Fourteen posts filed by topic pillar became one escalating argument with a finale once `/stanton-series-escalation` re-ordered them by the change each delivers. The series premise was already in the work; topic-bucket ordering was hiding it.

---

## 1. `/stanton-produce` — the end-to-end conductor

### What it is

Objective + raw material in, finished piece out: Runia story gate → Stanton architecture (premise / spine / change / arc) → routed to the production engine that owns the format → clamp-audit QA loop → Stanton-Grade Gate → voice/prose/fact gates → anchor-named finalize. Workflow wrapper: `.agent/workflows/stanton-produce.md`; full spec: `skills/andrew-stanton-audience-engineering/workflows/stanton-produce.md`.

### When to reach for it

- Launches and multi-post sequences — anything where architecture across pieces matters as much as any single piece.
- "Take this raw material and make it ship-ready" requests where you want the full gate stack run for you.

### When NOT to

- One flat draft → `/stanton-clamp-audit` alone is the cheapest quality lift in the system.
- Pure line-level work → the owning engine directly (copy-engine, linkedin-daily, parallax) — Stanton already fires inside all six wired engines without invocation (embedded map: OPERATORS-GUIDE §1).
- Not sure there's a story at all → `story-compass` (Runia) first.

### How to invoke

```
/stanton-produce — objective: sequence the 14 reviewed posts into a launch arc; material: _active/linkedin-launch/04-content-os/REVIEW-clean-posts.md
```

### Honest edges

- It composes; it doesn't review taste for you. Bodies still await your PASS/FAIL/FIX verdicts.
- First live run complete (8.33/10 finalize, gate 8/8 with two catches) — one proof, not a track record.

**Depth**: USER-GUIDE.md ("Three ways to use it," the 20-workflow situation table, the five proven plays) · OPERATORS-GUIDE.md (deployment map, quality system, failure-modes table).

---

## 2. The Receipt Arc — the launch sequence itself

### What it is

A 14-post, ~3-week LinkedIn launch sequence produced by the first live `/stanton-produce` run. **Series premise**: confidence is the costume an empty claim wears — the operator who learns to ask for the receipt stops paying for it. The ladder escalates from "the bottle lies" ($20 magnesium) through AI-answer failures, gym-metric lies, and persuasion cost, to the finale flip: the receipt that protects you from the regulator is the same receipt that wins AI search. Residue feeling: "I can't unsee it."

Three components:

- **The 14-post order** — each post's rung and its 5-second change (from → to), in a ladder where only slots 1 and 14 are immovable.
- **13 loop lines** — paste as the FIRST COMMENT on each post after the body ships. The series clamp lives in the comments: each opens a debt the next post pays. Bodies stay untouched.
- **The finale bookend** — first comment on P5-2 ($53,088): closes the series in one habit ("ask for the receipt") and opens the offer.

### Where the assets live

- Sequence + loop lines + watch-items: `_active/linkedin-launch/content-os/launch-sequence-stanton.md`
- Post bodies (awaiting verdicts): `_active/linkedin-launch/04-content-os/REVIEW-clean-posts.md`

### How to execute / resume the posting sequence

1. **Verdict pass first.** Bodies ship only after your PASS/FAIL/FIX per post. If a body changes in a FIX pass, re-read its loop line (lines introduce zero new factual claims by design — keep it that way).
2. **Post weekdays, 5 / 5 / 4 across three weeks**, in ladder order. First-hour reply window per the playbook.
3. **Paste the loop line as the first comment** once the body is up. Then the finale bookend on post 14.
4. **Newsjacks flex.** Slots 5, 10, 12, 13 carry `[VERIFY LIVE]` swaps — post when the news window is actually live, holding rung position where possible.
5. **Resuming mid-sequence**: open the launch-sequence file, find the last posted rung in the ladder table, continue from the next slot. The order survives interruptions; only 1 and 14 are fixed.

### Honest edges

- P3-1 and P3-2 are the closest pair (both training-metric corrections). If either draws a FAIL, cut one — never both.
- Newsjack timing can swap 12 ↔ 13; nothing else moves.

---

## 3. When Stanton vs your other content engines

| You have | Reach for |
|---|---|
| A batch of posts to sequence into a launch | `/stanton-series-escalation` or full `/stanton-produce` |
| One draft that's clean but nobody would finish | `/stanton-clamp-audit` (the anti-exemplar case: polished-but-flat) |
| A LinkedIn post from scratch | `/ghostwrite` / Lara — Stanton's premise litmus already fires inside `linkedin-daily` |
| A Parallax edition | `/parallax` — architecture pass + clamp-audit are embedded |
| Cold-start converting copy | `/copy-engine` — Stanton runs its Phase 6 clamp |
| Multi-part season/theme architecture | Hawley first; stack order never inverts: **Runia → Hawley → Stanton → Roth** |
| Prose voice, the line itself | Not Stanton — Roth, Cole, Vuong, or your voice rules |

Rule of thumb: Stanton is additive intelligence on top of the engines, not a substitute route. Invoke it directly when the *architecture or the audit* is the job; otherwise it's already there.

---

## 4. Where the depth lives (don't duplicate — read)

- **`skills/andrew-stanton-audience-engineering/USER-GUIDE.md`** — the 20-workflow situation table, the five highest-leverage proven plays, the two-source framework arsenal (Perell interview + TED layer), the Stanton-Grade Gate in plain terms, quick-start recipes.
- **`skills/andrew-stanton-audience-engineering/OPERATORS-GUIDE.md`** — the three-layer deployment map (six embedded engines with exact wiring points), the quality/exemplar/rubric system, source ground truth, the registration map, extend-never-rebuild rules, failure modes → fixes, session receipts.
- Memory anchor: `project_andrew-stanton-extraction.md`. Standing rule from it holds: **don't rebuild a storytelling/emotion engine — extend this; `/stanton-*` is the front door.**

## 5. Honest edges (session-wide)

- The exemplar bank compounds only if you feed it: every felt PASS from you should be appended to `references/exemplars.md`. Rules without exemplars = the 5/10 ceiling.
- Engine wiring can silently die in refactors — after editing any of the six wired engine files, grep it for `stanton` (checklist: OPERATORS-GUIDE §1).
- The Receipt Arc is sequenced but not shipped: the human verdict pass on the 14 bodies is the open loop, and the four newsjacks decay if their windows pass unwatched.

*Created 2026-07-13 (Stanton enrichment + Receipt Arc launch session). This entry points; the two dedicated guides carry the depth — extend those, and keep this one a map.*
