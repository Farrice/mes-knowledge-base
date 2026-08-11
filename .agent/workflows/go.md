---
description: The front door — translate a raw dump into a sharpened intent without losing his words, load the experts, and run it in place
---

# /go - The Front Door (v4, 2026-08-10)

`/go "<messy thought>"` turns a raw dump into finished work. One rule governs
everything below: **nothing stands between his intent and the execution of it.**
You translate his words, you load what the work needs, and the same context that
heard him does the work.

## Why v4 exists (read this before "improving" the flow)

v1-v3 each lost to `/raw-intent-bridge` on the same complaint, three weeks apart
(2026-07-21 and again 2026-08-10: *"I've been getting way better results with
raw-intent-bridge"*). The 2026-08-10 audit found the mechanical cause:

- **v3 compiled his raw words directly.** `codex_operator_preflight.py` routes
  **lexically**. Vision-speech carries no route keywords, so it mis-routes. Proof
  (cold A/B, 2026-08-10): his ICP-imagery dump compiled to
  `/want-vs-need-mapper` — a film-narrative workflow — because the words "want"
  and "need" appeared in the sentence, then self-blocked on a phantom
  external-write risk. The bridge had already carried this scar since 2026-07-02
  (a warehouse-rave merch intent → `/albom-gravedigger-angle` raw; → `/merch-os`
  once sharpened) and therefore made translation mandatory BEFORE the compiler.
  v3 inverted the one thing that worked.
- **v3 added a middleman.** Compile a card → stage a sign-off → hand a packet to
  a conductor who re-interprets it. The bridge executes its own first action in
  the same context. Every /go rebuild made the middle richer; the middle was the
  defect.
- **The ceremony steered nothing.** 151 compiled vs 124 closed missions; verdict
  captured on **8 of 306** entries despite a templated ask. The one /go he called
  good (2026-08-10) ran none of it.

So: the machinery a weaker model needed as rails is not what this one needs.
It needs his words protected, the right files loaded, and awareness of what's
already open. **Do not re-add a compile-first stage, a conductor handoff by
default, or mandatory paperwork. That is the failure, three times over.**

**His verdict on v4's first cut was `marginal` — "smaller, not amazing"** (the
first non-good verdict ever captured in 306 mission entries). He was right:
subtracting the middleman only stops /go being wrong. Stage 0.7 is the addition —
the bar, the depth ladder, and preserved dissent — and it is the reason to type
`/go` rather than just start working. **Cut Stage 0.7 and this is a diet, not a
front door.**

## Stage -1 — CONTINUITY (one command, then move)

```bash
python3 execution/pulse_dashboard.py --open
```

If the intent matches an OPEN mission, say so in one line and ask:
**continue / adjust / park / new**. Continue = resume where it stopped, never
recompile. **Park = `/park <slug> "<reason>"`** — a first-class close that writes
a resumable handoff; parking is a good outcome.

At 3+ open missions, offer to finish or park one — one line, never a block,
"open it anyway" always works.

## Stage 0 — TRANSLATE (mandatory; model-side; before any script)

Build the Translation Card from his raw words. This is the stage that makes /go
work; it cannot be delegated to a script, because the thing being translated is
exactly what scripts can't read.

- **Anchor** — which project/client/system this belongs to (Parallax, Jen/FTHB,
  MyBPM, Andrea, Carbon Torch, harness…). Match against memory and the repo;
  never guess across projects.
- **Deliverable** — the concrete artifact implied.
- **Audience** — who receives it.
- **Felt standard** — his vision phrases, **quoted verbatim**. This is the
  creative payload. Never paraphrase it away, never compile it away, and carry it
  into the work itself — not just the card.
- **Sharpened line** — ONE sentence: `<verb> <deliverable> for <anchor> using
  <owning OS/expert> — <felt standard, compressed>`. It must contain
  route-findable keywords. **This line is for the router. The verbatim quotes are
  for the expert. Both travel together.**

If Anchor or Deliverable can't be filled from the payload plus memory, ask
exactly ONE question covering both gaps, then proceed. One round, never an
interrogation of flow-state. Close your own gaps first (Partner Posture 2) —
grep and web-check before spending one of his answers.

## Stage 0.5 — SECOND OPINION (suggestion, never the reasoning surface)

Run the engines on the **sharpened line only** — never the raw dump:

```bash
python3 execution/codex_operator_preflight.py "<sharpened line>" --plain
python3 execution/expert_router.py route "<sharpened line>"
python3 execution/recommend_stack.py "<sharpened line>"
```

Read what comes back as a **second opinion you may overrule in one line**. It is
evidence, not a verdict — the same standing as router bindings (scar 2026-07-27:
force-routing a prose question into a rhetoric workflow). When the engine's route
contradicts your read of the anchor, say so in one line and take yours.

**Questions gate:** if the launchpad surfaces "questions that change execution",
ask them now, before producing. A confident-feeling intent never suppresses one.

**Goal spine:** name the goal served from `.agent/cos/goals.json`; no match =
`ORPHAN ⚑`, one line, never a block. If `campaign_beacon.py` shows an open
campaign and this serves something else, say so in one line and keep going.

## Stage 0.7 — THE BAR (this is the part that makes /go worth having)

Stages -1 through 0.5 only stop /go being wrong. This stage is what makes it
good, and it's the answer to his 2026-08-10 verdict on v4's first cut:
*"smaller, not amazing."* Removing the middleman was necessary and insufficient.
Three moves, each extending machinery already proven on disk — never a new engine.

**1. Name the bar before producing** (`directives/blind-bar-protocol.md`, approved
2026-08-05). Every taste-bearing deliverable carries a one-line Bar clause:

> **Bar**: `<named reference artifact — path or exact exemplar>`. Nothing else counts as done.

Adjectives orient; only a named artifact decides. "High quality" and "on-brand"
are not a bar. No real reference exists → write `Bar: none` and say so — never
improvise one. Then run the blind side-by-side before he sees it: if the
deliverable is instantly distinguishable as the weaker piece, it fails, repair the
**single biggest gap**, hard cap two rounds. Deterministic lints
(`prose_classifier.py`, `voice_evaluator.py`) run first — they're free. This is
in-context reasoning, never a subagent, never a critic fleet (four separate scars).
**His taste should enter at a high baseline, not be spent QA-ing floor defects.**

**2. Load to depth, and say what you loaded.** "Expert named" is the v2 failure;
"two files opened" is a floor, not a ceiling. State the ladder in one line:

| Work type | Minimum real load |
|---|---|
| Anything in his voice | `_active/farrice-brand/voice/VOICE-CARD.md` + register per the Voice Atlas |
| Content / copy | 2+ skill files, and `genius.md` — not just `SKILL.md` (Tier-1-only is a logged defect) |
| Creative generation | the master per `skills/generate/references/craft-map.md` — freehand = slop, proven A/B |
| Identity / offer / brand | `FARRICE-MASTER-CONTEXT.md` before asking him anything |
| Buyer-facing claims | the ICP's researched words **verbatim** — paraphrase kills credibility silently |
| Real people, dates, stats | grounding protocols auto-fire; label VERIFIED / LIKELY / UNCONFIRMED |

**3. Preserve dissent; never blend.** When the loaded stack genuinely disagrees on
approach, surface the fork in one line and let him pick, or pick and name what you
overrode. Averaging two experts into a consensus take is the documented failure
mode — it produces work with no author. One pen per body, always.

## Stage 1 — LOAD, THEN RUN IN PLACE

Execute the ladder from Stage 0.7 — expert files opened, not names dropped.

**Then run it here.** The context that heard him executes. Hand off ONLY when the
work is genuinely that shape:

| Genuinely hand off when | To |
|---|---|
| 10+ parallel units or 3+ independent workstreams | workflow engine (scout → agents → gate) |
| Multi-domain panel → tiered roadmap | `/assemble` |
| Decision with real tradeoffs needing dissent preserved | `/convene` |
| Plan authored here, executed by a cheaper seat | `/wargame-run` |
| A second, genuinely separate deliverable | its own conductor |

Everything else — a post, a page, a brief, a build, a repair — runs here. Routing
a single deliverable to a conductor costs a re-interpretation and buys nothing.

**Sign-off scales with blast radius, not with ceremony.** T1 (local, reversible):
state the shape in 1-3 lines and go — his reply is the correction loop. T2/T3
(outward-facing, paid, destructive, or many files): brief back and WAIT; plan
mode is the right surface when the manifest is long. The cost gate and factual
veto are unchanged and absolute.

**Lock gate** (merge-discipline Law 0): fleet/swarm/long autonomous runs claim the
tree — `python3 execution/session_lock.py claim "<mission>"`. Blocked on a foreign
lock = take a lane (EnterWorktree), never wait. Solo work skips this.

**Work in visible beats.** Surface a shaping question at a genuine fork rather
than disappearing for an hour — he prefers the back-and-forth (2026-07-29).

## Stage 2 — LOG (one line each end)

Append to `.agent/missions.jsonl` at start and at close:

```json
{"ts":"<iso>","mission":"<one-liner>","slug":"<slug>","serves":"<goal-id|orphan>","tier":"T1|T2|T3","status":"compiled|done|stopped","verdict":"<good|marginal|off|null>","outcome":"<one line at close>"}
```

An unlogged mission is invisible to the pulse board; an unclosed one is a debt
Stage -1 surfaces next time. `contract.json` and `portable.md` are written **on
request** — `raw_intent_run_packet.py "<sharpened line>" --plain` still generates
the portable version whenever he wants the mission paste-able into another
harness. They are not a tax on every run.

## Stage 3 — DELIVER + CLOSE

1. Ship the work.
2. Close the mission line with the outcome, and carry the bar receipt into
   finalize notes: `BlindBar: PASS | FAIL(gap: …) | N/A(no ref) — <n> rounds`.
   A skipped bar is written `N/A`, never implied — a silent pass is the
   rubber-stamp failure (2026-07-16).
3. **One-tap verdict** — the delivery's last line is verbatim
   `Verdict on this one — good / marginal / off?`. Unanswered is his call; unasked
   is a session defect. Log felt verdicts with `voice_ratchet.py add` when they
   touch voice.
4. **Next Moves** — Deepen / Adjacent / Act, naming the specific active goal.
5. Substantive builds may close as a brief in the Briefing Room
   (`.agent/workflows/briefs.md` § Mission reports).

## Universal Harness (Claude Code + Codex)

This file is the single source of truth for `/go` in BOTH harnesses, and since
v4 it is also the canon for `/raw-intent-bridge` — the two surfaces now run one
flow (`.agent/workflows/raw-intent-bridge.md` keeps the Codex invocation contract
and boundaries, and points here for the stages). Never fork a Codex copy; thin
trigger bridges only, per the global AGENTS.md contract.

Shared spine, identical on both sides: `.agent/cos/goals.json` (goals),
`.agent/missions.jsonl` (log), `chain_runner.py` (finalize), `workflow_router.py`
(second opinion).

Codex adaptations — everything else runs as written:

- Fleet/swarm patterns plan and receipt via `execution/codex_dynamic_workflow.py`;
  real Codex subagents stay approval-gated per run.
- Conductor Ladder seating does not apply — Codex seats its own models.
- GOLDEN RULE stands: one tool per working tree.
