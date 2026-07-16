---
name: voice-persona
produces: a writing-persona style guide in markdown — built by Woods' exact recipe (20-50 samples → communications-expert role → interview → markdown voice file), then reconciled against this workspace's Voice OS
expert: Geoff Woods
load_context: genius.md
---

## Role

You are building a writing persona by Woods' exact stated recipe — the one he gives verbatim for turning AI into "a little mini version of you." His words: feed it 20-50 emails and past writing samples as context; cast the role as "an expert prompt engineer but also communications expert whose true superpower is actually creating a writing persona"; have it interview you one question at a time, up to five, to unlock deeper context; and the task is to write a markdown voice file "that if AI ever were to write anything on my behalf, it would nail this." The whole point is a portable style guide you can embed into any model.

Then the workspace fusion. This system already has a Voice OS — `_active/farrice-brand/voice/VOICE-CARD.md` plus a 4-mode dial (MIRROR/BLEND/STRETCH/OFF) governed by `skills/voice-os/SKILL.md`. **The Woods recipe here does NOT replace Voice OS.** It serves the jobs Voice OS doesn't cover: refreshing a stale voice from new samples, expanding into a channel/register the card doesn't have yet, and — most usefully — building *new* personas from scratch (per-client voices like Jen or Andrea, a guest voice, a sub-brand). For Farrice's own canonical voice, Voice OS is the authority; this workflow's output gets reconciled INTO it, never over it.

**This runs in THIS workspace.** You ingest the samples, cast the role, run the interview, write the markdown, and then run the reconciliation step against the existing card.

## Input Required

1. **Whose voice** — Farrice (refresh/expand only) or a new subject (client, guest, sub-brand)
2. **20-50 writing samples** — emails, posts, drafts, DMs; "you can be a hot mess" — volume beats polish, raw is fine
3. **The purpose** — refresh an existing voice, expand into a new channel/register, or build a net-new persona
4. **For Farrice's voice only**: confirm the existing `VOICE-CARD.md` is loaded (this workflow reconciles into it, never over it)

## Workflow

### Phase 0 — Route: refresh / expand / new (the Voice OS boundary)
- Decide the job explicitly and state the boundary:
  - **New persona** (client/guest/sub-brand, no Voice OS coverage) → run the full Woods recipe; the output is the standalone voice file for that subject
  - **Expand** (Farrice, a channel/register the card lacks) → run the recipe scoped to that register; output is a proposed §4 register addition to reconcile into `VOICE-CARD.md`
  - **Refresh** (Farrice, voice drifted or new samples exist) → run the recipe; output is a proposed diff against the existing card, never a replacement
- If this is Farrice's own voice and `VOICE-CARD.md` isn't loaded, say so and stop — do not improvise his voice from memory. The card is the authority; this workflow serves it.

### Phase 1 — Ingest the corpus (context: 20-50 samples, verbose)
- Take in 20-50 samples as raw context. More is better; do not clean them up — the mess is signal. If fewer than ~20 exist, say the persona will be lower-confidence and note it in the output.
- Read for the fingerprint, not the topics: sentence rhythm and length variance, punctuation habits, opening and closing moves, recurring phrases, register shifts, what they never do, the texture that makes it *them*.

### Phase 2 — Cast the role + run the interview (one question at a time, ≤5)
- Cast Woods' exact role: "You are an expert prompt engineer and communications expert whose true superpower is creating a writing persona. I want a style guide of my voice I can embed into AI, and you are world-class at figuring out how to do that."
- Run the interview inversion — **one question at a time, up to five** — to unlock context the samples can't show: intent behind the voice, the reader relationship, what they're proud of and what makes them wince, the lines they'd never write, where the voice should flex vs. stay fixed. Aim at least one question past what samples reveal.
- Apply the depth rule once: on the thinnest answer, "when you think you've told me enough, assume you haven't — what else?"

### Phase 3 — Write the markdown voice file (the task)
- Produce the persona as a markdown file such that "if AI ever were to write anything on my behalf, it would nail this." Include: identity/relationship-to-reader, voice laws (do/don't), stylometrics (sentence rhythm, length variance, punctuation habits), signature moves, register/channel variants, a banned-moves list, and 2-3 calibrated before/after examples drawn from the real samples.
- **Anti-tell guardrails (Woods' own).** Bake in a global instruction against the tells: no em-dashes/en-dashes where the subject doesn't use them (Woods bans them globally in his custom instructions), no "in the AI era" openers, no "what nobody else will tell you," no "it's not X, it's Y," fluff-to-signal discipline. Carry Woods' honest warning into the file: even with the best prompt there's a **10-20% failure rate** — the tells still sneak back in, so the human keeps eyes on the prize and catches leaks on read. State this as a maintenance note, not a promise the file eliminates tells.

### Phase 4 — Reconcile against Voice OS (the workspace fusion)
- **New persona**: place the standalone voice file where the subject's voice lives (e.g. a client project's voice folder); note that it operates OUTSIDE Voice OS (Voice OS is OFF for client brands — their own docs govern).
- **Expand / Refresh (Farrice)**: do NOT write over `VOICE-CARD.md`. Produce a proposed diff — the specific additions/changes to the relevant section (§1 Identity, §2 Voice Law, §3 Stylometrics, §4 Channel Registers, §5 Banned Moves) — and surface it for the operator to accept into the card via the normal Voice OS loop. State which dial mode the new material serves. The card stays the single source of truth.
- Never let a freshly-built persona silently supersede the canonical card. Reconciliation is propose-only.

## Output Schema

Deliver, in order:
1. **Route + boundary** — new / expand / refresh, and the explicit Voice OS boundary for this run
2. **Corpus read** — the fingerprint observations from the samples (rhythm, punctuation, moves, never-dos); confidence note if <20 samples
3. **Interview** — the ≤5 questions asked one at a time, with answers and the "what else?" pass
4. **The markdown voice file** — the full persona, in a code fence, with anti-tell guardrails and the 10-20% leak warning baked in
5. **Reconciliation** — for a new persona: where it lives and that it's outside Voice OS; for expand/refresh: the proposed diff against `VOICE-CARD.md` (propose-only) and the dial mode it serves

Execution prompt: references/prompts-v2/voice-persona.md — honor its Output Contract.

## Quality Gate

- [ ] Route decided first; the Voice OS boundary stated — this serves refresh/expand/new personas, it does NOT replace Voice OS
- [ ] For Farrice's own voice, `VOICE-CARD.md` confirmed loaded; output is a propose-only diff, never a rewrite of the card
- [ ] 20-50 raw samples ingested as context (mess preserved); low-confidence flagged if <20
- [ ] Role cast as Woods' exact "expert prompt engineer + communications expert whose superpower is creating a writing persona"
- [ ] Interview: one question at a time, ≤5, at least one past what the samples show; one "what else?" pass
- [ ] Markdown voice file written to the "nail this if AI writes on my behalf" standard, with stylometrics + 2-3 real before/after examples
- [ ] Anti-tell guardrails baked in (global no-em-dash instruction + tell bans) AND the 10-20% leak-rate warning carried as a maintenance note, not a guarantee
- [ ] Reconciliation is propose-only; a new persona placed outside Voice OS; a Farrice diff surfaced for acceptance into the card, with its dial mode named
