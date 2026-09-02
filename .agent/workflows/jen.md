---
description: "/jen — the ONE front door for Jen Santulan (@_jiing) content. Nine steps in a fixed order, a receipt line after each, no step skipped: LOAD → READ → RESEARCH → WRITE → AMPLIFY → CHECK → RENDER → DELIVER → LEARN. Operating model: _active/clients/jen-listings/06-system/ENGINE-V2.md. Replaces /jen-engine, /jen-full-pipeline, /listing-content, /buyer-education-story, /neighborhood-deep-dive-carousel as entry points (2026-09-02 reset)."
---

# /jen — one spine, one order

Why this exists (2026-09-02): three engines claimed Jen's pipeline, none was the front door, and the shipped weeks stamped her verbatim close on nine of nine posts. Farrice: "they haven't been firing in the order of operations that they should be... we're just getting sloppy messes versus actually high-quality content that's research data-driven and translated into her voice and then amplified." This file IS the order. Every step prints a receipt line. If a receipt is missing, the next step does not start.

Usage:

```
/jen week <YYYY-MM-DD>        # build one week (three posts) end to end
/jen post <district> <topic>  # one post through the same nine steps
/jen read                     # steps 0–1 only: what the account is doing this month
```

Never for: a listing URL drop with no week context (that is Convert district inside a week, or `/listing-package` for a one-off send package). Never a new generator, never a new skill, never a recurring ask on Jen.

## The order (receipts are mandatory; print them as you go)

### 0 · LOAD — hard prerequisite

Read, in this order, and print `LOAD: 7/7` (or the count you actually read; below 7 = stop and say why):

1. `_active/clients/jen-listings/06-system/ENGINE-V2.md` (identity, the deal, realism gate, districts, formats, look, cadence, reply layer)
2. `_active/clients/jen-listings/06-system/CONTENT-MIX.md` (the extraction-derived shares and the hook rule)
3. `_active/clients/jen-listings/06-system/VAULT.md` (what already exists; month two is assembled, not re-invented)
4. `skills/jen-santulan-listing-content/references/jen-real-voice-profile.md` (her register, lexicon, verbatim lines: THE voice source)
5. `skills/jen-santulan-listing-content/references/jen-calibration-log.md` (his and her PASS/FAIL verdicts; outranks defaults)
6. `_active/clients/jen-listings/CLAUDE.md` (register ladder, fair-housing floor, anti-patterns)
7. `_active/clients/jen-listings/06-system/pulse/latest.md` (what the account did last)

Receipt: `LOAD: 7/7 · voice source = jen-real-voice-profile.md · calibration rows = N`

### 1 · READ — the data decides the slots

From `CONTENT-MIX.md` + the latest pulse + `04-deliverables/jen-outlier-audit.md`, write ONE line and put it at the top of the week folder's `READ.md`:

> this month the account moves on ___ (evidence: post, number). the week's slots are: tue ___ · thu ___ · sat ___. the running experiment is ___ (window: ___).

Rules: shares come from `CONTENT-MIX.md`, never from taste; one experiment per month, held across its slots; Convert takes a slot only while a listing is active, otherwise Attract takes it.

Receipt: `READ: slots = attract / connect / position · experiment = <name> · evidence = <post, number>`

### 2 · RESEARCH — facts before words

Open the facts ledger (`04-deliverables/<week-set>/FACTS.md`; extend it, never a second ledger). For every claim the week will carry: date, source, label (VERIFIED / LIKELY / UNCONFIRMED / HERS / Jen-seat), re-check column. Run the realism gate on every topic (ENGINE-V2 §3: would she say it to a client in these words; can a stranger act on it at their stage; is every fact dated and sourced or hers). Any "no" kills the topic. UNCONFIRMED never reaches copy.

Sources in order: her listing data (MLS via Jen), Redfin/Freddie Mac/CDI pages read today, `RESEARCH-PACK.md`, the deep-research record (LIKELY until re-verified). Comps for "what $X buys" are pulled the week they post.

Receipt: `RESEARCH: N claims ledgered · UNCONFIRMED = 0 in copy · realism gate: N topics passed, N killed`

### 3 · WRITE — one pen, her seat first

One post at a time. Jen-as-herself seat writes first (her register from the voice profile: lowercase, ellipses, soft landings, one emoji max, invitation asks). Then the hook rule from `CONTENT-MIX.md`: the hook opens on her or the reader's situation; the number or the house is beat 2. One job per post. The door open at the end with a concrete thing to send (a street, a number, a photo, "hi").

**The voice bank, never a stamp.** Her verbatim lines are a bank: "i'm here for you. that's my job. i do this to protect you and your best interest." · "everything works out exactly the way it's supposed to." · "just breathe. take a step back. let's sleep on it." · "we're gonna do this, this, and this, and we'll go from there." · "lipstick remodel." · "i've got you." · "let's chat." Draw each at most ONCE per week and at most twice per month. A post with no bank line is normal. The close varies: sometimes a question, sometimes "or just say hi," sometimes nothing but the ask.

Write into `COPY.md` in the week folder, one section per post: hook · beats or slides · caption · fact labels table · reply routing.

Receipt: `WRITE: 3 posts · bank lines used = <list> · no line used twice`

### 4 · AMPLIFY — the craft room (Farrice's definition, 2026-09-02)

"Amplified means enhanced and improved with our best copywriters and experts for writing to make her voice more impactful and get people attention and provide value and more."

**Phase 1 shape (Farrice, 2026-09-02, second pass: "expert soup... orchestration poorly executed"): ONE pen, ONE check. No room.**

The pen loads exactly two craft files and nothing else: `skills/alyssa-stalker-agent-content-playbook/workflows/03-hook-reframe.md` (Topic + Who + Lens on the hook) and `skills/luke-iha-vicious-hooks/genius.md` (the assumption the hook breaks; delete the throat-clearing; short words). It makes one sharpening pass per post: the hook names the fear or the wish, the middle holds attention, the close is hers. Never jargon without a six-word gloss. Never "top producer," never credentials, never urgency, never an attack hook.

Then the Jen-as-herself check, from `jen-real-voice-profile.md` + `jen-calibration-log.md` + the ChatGPT extraction outputs (`06-system/jen-chatgpt-outputs/`, when they exist): read each post aloud as her; any line she would not say reverts. That is the whole step. More seats return only if her numbers say the copy is the problem (Phase 2+, `06-system/PHASES.md`).

Receipt: `AMPLIFY: one pen · N lines sharpened · Jen check reverted N lines`

### 5 · CHECK — mechanical, in this order

```bash
python3 execution/fair_housing_lint.py check <week>/COPY.md     # hard: any hit = fix before render
python3 execution/prose_classifier.py check <week>/COPY.md      # nudge: report the score
python3 execution/jen_stamp_lint.py <week>/COPY.md              # hard: a sentence in two posts of one week = fix
```

Receipt: `CHECK: fair-housing PASS · classifier N/10 · stamp-lint PASS (0 repeats)`

### 6 · RENDER — one generator family

Cards and reels: extend the `WEEKS` list in `04-deliverables/2026-09-06-engine-v2-weeks-1-2/build_weeks.py` (imports `gen_photo.py`; `--no-video` for the fast loop). Editions: `06-system/valley-editions/editions.py`. Never a third generator (ENGINE-V2 §15). Photos per ENGINE-V2 §7; placeholders are mapped in `PHOTO-SWAP.md`; nothing goes to Drive on placeholders.

Receipt: `RENDER: N PNG · N reel spec · placeholders = N (mapped)`

### 7 · DELIVER — a page he can judge in sixty seconds

```bash
python3 execution/jen_os_page_thumbs.py .tmp/valley-os/thumbs
python3 execution/jen_os_page.py .tmp/valley-os/thumbs .tmp/valley-os/the-valley-os.html
```

Publish with the Artifact tool to the existing Valley OS page (same URL). Every post as it will look, caption beside it. Never a markdown wall as the deliverable (memory: Readout OS; his 9/2 words: "the markdown files are impossible to read").

Posting checklist in the week folder (`day-plan.txt`, one line per post): day and time · story slide (the first frame, reposted to stories the same morning) · collab tag `@myhousesellers` when it is a team listing · first comment (the ask, restated in one line) · reply routing from the saved replies.

Then the Feedback Triad on the page (like / don't like / top changes). Two rejected takes on one post = back to the input, never a third take.

Receipt: `DELIVER: page URL · N posts · triad pending`

### 8 · LEARN — the loop

Monday: `python3 execution/jen_pulse.py` (appends to `06-system/pulse/`). 1st of month: `/alyssa-stalker-outlier-audit` on the month → the attribute → next month's READ line; four numbers from Farrice into `FUNNEL-MATH.md`; `FACTS.md` re-check column; VAULT rows for everything that shipped; his verdicts into `jen-calibration-log.md`.

Receipt: `LEARN: pulse appended · vault rows +N · calibration rows +N`

## What this workflow refuses

- Writing before RESEARCH has a receipt. Rendering before CHECK has a receipt. Delivering as markdown.
- A second generator, a second facts ledger, a second voice file, a parallel Jen lane.
- Any recurring ask on Jen: her deal is a thumbs-up and same-evening replies (ENGINE-V2 §2).
- Talking-head reels, an intake questionnaire, a template she fills.

## Handoff

- Source evidence: FACTS.md rows (dated), pulse, outlier audit
- Output produced: one week folder (COPY.md, READ.md, PNGs, reel specs, captions.txt, day-plan.txt, saved-replies.txt) + the Valley OS page
- Validation: the nine receipt lines, in order, in the session
- Open risk: placeholders until her listing shoots land in Drive folder 01
