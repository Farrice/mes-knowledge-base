---
description: "/jen — the ONE front door for Jen Santulan (@_jiing) content. Nine steps in a fixed order, a receipt written into the week folder after each, no step skipped silently: LOAD → READ → RESEARCH → WRITE → AMPLIFY → CHECK → RENDER → DELIVER → LEARN. The run folder is the state (run.yaml + pipeline-log.md, 2026-09-09). Operating model: _active/clients/jen-listings/06-system/ENGINE-V2.md. Replaces /jen-engine, /jen-full-pipeline, /listing-content, /buyer-education-story, /neighborhood-deep-dive-carousel as entry points (2026-09-02 reset)."
---

# /jen — one spine, one order, one run folder

Why this exists (2026-09-02): three engines claimed Jen's pipeline, none was the front door, and the shipped weeks stamped her verbatim close on nine of nine posts. Farrice: "they haven't been firing in the order of operations that they should be... we're just getting sloppy messes versus actually high-quality content that's research data-driven and translated into her voice and then amplified." This file IS the order.

Why the run folder (2026-09-09, IMPORT-LIST.md #1): the receipts used to be printed to chat and lost, and the page he judges was regenerated from hand-edited tables. Now every step writes its receipt into `<week>/pipeline-log.md`, RENDER writes `<week>/run.yaml`, and the page reads both. Same three shell commands on Claude Code and on Codex; no harness-specific tool is needed for any step except the final publish (marked below).

## When to use / Never for

Use: "jen week <date>", "build Jen's week", "one Jen post about <topic>", "what is Jen's account doing this month", "re-run week N through the spine".
Never for: a listing URL drop with no week context (that is Convert district inside a week, or `/listing-package` for a one-off send package). Never a new generator, never a new skill, never a recurring ask on Jen (her deal is a thumbs-up and same-evening replies, ENGINE-V2 §2). Never `/social-carousel` for her weekly posts (that door is for Scrapes-rendered carousels; her weekly cards and reels render through `build_weeks.py`).

Usage:

```
/jen week <YYYY-MM-DD>        # build (or re-run) one week: three posts end to end
/jen post <district> <topic>  # one post through the same nine steps
/jen read                     # steps 0–1 only: what the account is doing this month
```

`WEEK` below = `_active/clients/jen-listings/04-deliverables/2026-09-06-engine-v2-weeks-1-2/week-of-<monday>` (the Monday of the week the posts land). State the scale in one line before starting: one week, three posts, one brand.

## The order (Phase · Owner · Action · Skipped when)

| # | Step | Owner | Action | Skipped when |
|---|---|---|---|---|
| 0 | LOAD | us | the eight canon files, in order, with the load level per row | never |
| 1 | READ | us | the data decides the three slots and the running experiment | never |
| 2 | RESEARCH | us | every claim ledgered in FACTS.md; realism gate on every topic | a `/jen post` on a Connect topic with no number (log it as skipped with why) |
| 3 | WRITE | us | one pen, her seat first, the voice bank drawn once | never |
| 4 | AMPLIFY | us | one pen sharpens (Alyssa placement + Luke grip), one check reverts | never |
| 5 | CHECK | script | fair-housing (hard) · classifier (nudge) · stamp-lint (hard) | never |
| 6 | RENDER | script | `build_weeks.py` → cards, reel stills, captions, run.yaml | `/jen read` |
| 7 | DELIVER | us | the Valley OS page from run.yaml; the Drive folder; the posting checklist; the Triad | `/jen read` |
| 8 | LEARN | us | pulse, vault rows, calibration rows, one learnings line | when nothing is due (say so in the receipt, never silently) |

Boundary line at every step: the receipt IS the boundary. Write it with the command below, then print exactly what it printed. A skipped step is written with `--skip`, never left out.

```bash
python3 execution/run_log.py receipt "$WEEK" <STEP> "<receipt text>" [--reason "<why>"] [--skip]
python3 execution/run_log.py check   "$WEEK"      # the gate: nine receipts, in order, plus run.yaml; exit 1 = not done
python3 execution/run_log.py status  "$WEEK"      # one line, any time
```

Done = `check` passes. A week whose gate fails is not delivered, whatever the chat says.

### 0 · LOAD — hard prerequisite

Read, in this order. The load level says how much (Full / the named section / Tone only), so the same eight files cost the same on every run and on both harnesses.

| # | File | Load level | What it shapes |
|---|---|---|---|
| 1 | `_active/clients/jen-listings/06-system/ENGINE-V2.md` | §1–3, §7, §16 in full; the rest as headings | identity, the deal, realism gate, photos, the order |
| 2 | `_active/clients/jen-listings/06-system/CONTENT-MIX.md` | Full | the shares, the hook rule, the experiment |
| 3 | `_active/clients/jen-listings/06-system/VAULT.md` | headings + the rows for this week's districts | what already exists; month two is assembled, not re-invented |
| 4 | `skills/jen-santulan-listing-content/references/jen-real-voice-profile.md` | Full | THE voice source: register, lexicon, verbatim lines |
| 5 | `skills/jen-santulan-listing-content/references/jen-calibration-log.md` | last 10 rows + every PASS row | his and her verdicts; outranks defaults |
| 6 | `_active/clients/jen-listings/CLAUDE.md` | Override List + anti-patterns | register ladder, fair-housing floor |
| 7 | `_active/clients/jen-listings/06-system/pulse/latest.md` | the header line + the table | what the account did last |
| 8 | `_active/clients/jen-listings/06-system/WINNERS.md` | Full | the evidence sheet: the approved specimen, the reel look, verified references |

On first write the log takes the door and the brand lock line: add `--door jen --brand-lock "BRAND LOCK: jen (client) · brand_context=_active/clients/jen-listings/brand_context"` to the first receipt.

Receipt: `LOAD: 8/8 · voice source = jen-real-voice-profile.md · calibration rows = N · winners = N rows`

### 1 · READ — the data decides the slots

From `CONTENT-MIX.md` + the latest pulse + `04-deliverables/jen-outlier-audit.md`, write ONE line and put it at the top of `WEEK/READ.md`:

> this month the account moves on ___ (evidence: post, number). the week's slots are: tue ___ · thu ___ · sat ___. the running experiment is ___ (window: ___).

Rules: shares come from `CONTENT-MIX.md`, never from taste; one experiment per month, held across its slots; Convert takes a slot only while a listing is active, otherwise Attract takes it. A week that deviates from the mix says so in READ.md and in the receipt, with the reason, so Farrice can tap it.

Receipt: `READ: slots = attract / connect / position · experiment = <name> · evidence = <post, number>`

### 2 · RESEARCH — facts before words

Open the facts ledger (`04-deliverables/<week-set>/FACTS.md`; extend it, never a second ledger). For every claim the week will carry: date, source, label (VERIFIED / LIKELY / UNCONFIRMED / HERS / Jen-seat), re-check column. Run the realism gate on every topic (ENGINE-V2 §3: would she say it to a client in these words; can a stranger act on it at their stage; is every fact dated and sourced or hers). Any "no" kills the topic. UNCONFIRMED never reaches copy. Comps for "what $X buys" are pulled the week they post; a re-run states the re-check date in the receipt instead of pretending the number was read today.

Sources in order: her listing data (MLS via Jen), Redfin/Freddie Mac/CDI pages read today, `RESEARCH-PACK.md`, the deep-research record (LIKELY until re-verified).

Receipt: `RESEARCH: N claims ledgered · UNCONFIRMED = 0 in copy · realism gate: N topics passed, N killed · re-check due <dates>`

### 3 · WRITE — one pen, her seat first

Before a word: name the WINNERS.md row (or Jen's own outlier) the post is built on and the on-screen line that carries 80% of the attention; the caption is the payoff and the preview of working with her (Farrice 2026-09-09). No inspected complete source = no post.

The copy lives in ONE place: the `WEEKS` list in `build_weeks.py` (beats, slides, captions, reply routing). `COPY.md` and `captions.txt` are rendered from it at step 6; never edit them by hand. One post at a time. Jen-as-herself seat writes first (her register from the voice profile: lowercase, ellipses, soft landings, one emoji max, invitation asks). Then the hook rule from `CONTENT-MIX.md`: the hook opens on her or the reader's situation; the number or the house is beat 2. One job per post. The door open at the end with a concrete thing to send (a street, a number, a photo, "hi").

**The voice bank, never a stamp.** Her verbatim lines are a bank: "i'm here for you. that's my job. i do this to protect you and your best interest." · "everything works out exactly the way it's supposed to." · "just breathe. take a step back. let's sleep on it." · "we're gonna do this, this, and this, and we'll go from there." · "lipstick remodel." · "i've got you." · "let's chat." · "my DMs are open" · "or just say hi". Draw each at most ONCE per week and at most twice per month. A post with no bank line is normal. The close varies: sometimes a question, sometimes "or just say hi," sometimes nothing but the ask. `jen_stamp_lint.py` enforces this at step 5; a hand line on the frame counts.

Receipt: `WRITE: 3 posts · bank lines used = <list> · no line used twice`

### 4 · AMPLIFY — the craft room (Farrice's definition, 2026-09-02)

"Amplified means enhanced and improved with our best copywriters and experts for writing to make her voice more impactful and get people attention and provide value and more."

**Phase 1 shape (Farrice, 2026-09-02, second pass: "expert soup... orchestration poorly executed"): ONE pen, ONE check. No room.**

Dispatch contract (what goes in, what comes back):

| Pass | Loads exactly | Gets | Returns |
|---|---|---|---|
| the pen | `skills/alyssa-stalker-agent-content-playbook/workflows/03-hook-reframe.md` (Topic + Who + Lens on the hook) and `skills/luke-iha-vicious-hooks/genius.md` (the assumption the hook breaks; delete the throat-clearing; short words) | one post's beats/slides + caption | the sharpened post + one line: `N lines changed: <which>` |
| the check (Jen-as-herself) | `jen-real-voice-profile.md` + `jen-calibration-log.md` + `06-system/jen-chatgpt-outputs/` when it exists | the sharpened post | the post with any line she would not say reverted + `reverted N: <which>` |

One sharpening pass per post: the hook names the fear or the wish, the middle holds attention, the close is hers. Never jargon without a six-word gloss. Never "top producer," never credentials, never urgency, never an attack hook. Light edits (one line) stay with whoever is conducting; a hook that still opens on the number goes back through the pen once, then stops (two rejected takes = back to the input, never a third). More seats return only if her numbers say the copy is the problem (Phase 2+, `06-system/PHASES.md`). Write the pass into `WEEK/AMPLIFY.md`: per post, what the pen changed and what the check reverted.

**The hook room for the on-screen line (Farrice's decision, 2026-09-09 evening; confirmed by his round-2 tap 2026-09-11).** His words: "we're not bringing our best social media experts to write compelling hooks and on-screen text… missing the craftsmanship." The on-screen line carries 80% of the post, so it gets pens, not one pass. Before the pens write: harvest overheard buyer sentences (her DMs, her own comments, r/SFV, a comment sample); beat 1 is one of those sentences in quotes, never a line invented from a concept. Two pens (Forsyth `skills/mark-forsyth-rhetoric/genius.md`, Kallaway `skills/kallaway-hook-mastery/genius.md`; Luke Iha and Harding lost 14 of 14 entries across two rooms and sit out unless a later tap says otherwise) each write beat 2 for every harvested sentence: her reply with a stake or a permission, a complete plain sentence she would say, never a pitch, forecast, credential, or price+place offer. One integrator culls in context against the approved specimen (`directives/blind-bar-protocol.md`: set each beside the specimen, drop what is instantly weaker, record every cut and why); the survivors go to a blind judging surface with the specimen seeded unlabeled and shuffled (`week-of-*/build_hook_surface.py`, key in a sidecar); Farrice taps; his verdicts ratchet (`voice_ratchet.py add --client jen`). One pair goes to the slot; the other passing pairs bank in `06-system/VAULT.md` ("Approved on-screen lines") and `WINNERS.md` §1. Pens write, never critique; no room of commentators (the Sept 2 "expert soup" was critics). Record: `week-of-*/HOOK-ROOM-<id>.md`. The caption stays one pen. If the specimen is not among his picks, the room failed: back to the input, never a third take.

Receipt: `AMPLIFY: one pen on the caption · N lines sharpened · hook room: 2 pens · N sentences harvested · N pairs to the surface + specimen · Farrice PASS n FAIL m · Jen check reverted N lines`

### 5 · CHECK — mechanical, in this order

```bash
python3 execution/fair_housing_lint.py check --file "$WEEK/COPY.md"   # hard: any hit = fix before render
python3 execution/prose_classifier.py check "$WEEK/COPY.md"          # nudge: report the score (COPY.md's list shape reads as "parallel"; the captions alone are the real read)
python3 execution/jen_stamp_lint.py "$WEEK/COPY.md"                  # hard: a sentence in two posts of one week = fix
```

COPY.md is a render output, so CHECK runs after a `--no-video` render of the edited `WEEKS` data (step 6 fast loop), then step 6 renders for real. A hard failure goes back to step 3 for that post; the receipt records the fix.

Receipt: `CHECK: fair-housing PASS · classifier N/10 · stamp-lint PASS (0 repeats)`

### 6 · RENDER — one generator family

Cards, reel stills, captions, day plan, saved replies, COPY.md and **run.yaml**: `python3 04-deliverables/2026-09-06-engine-v2-weeks-1-2/build_weeks.py` (imports `gen_photo.py`; `--no-video` for the fast loop and for lanes without ffmpeg; the mp4s land in Drive only). Editions: `06-system/valley-editions/editions.py`. Never a third generator (ENGINE-V2 §15). Photos per ENGINE-V2 §7; placeholders are mapped in `PHOTO-SWAP.md`; nothing goes to Drive on placeholders. `run.yaml` is written by the renderer from the same data it rendered (posts, hooks, captions, photos, routing); status and receipts are yours and survive re-renders.

Receipt: `RENDER: N PNG · N reel spec · N cover stills · run.yaml N posts · placeholders = N (mapped)`

### 7 · DELIVER — a page he can judge in sixty seconds

```bash
python3 execution/jen_os_page_thumbs.py .tmp/valley-os/thumbs
python3 execution/jen_os_page.py .tmp/valley-os/thumbs .tmp/valley-os/the-valley-os.html
python3 execution/run_log.py manifest "$WEEK" --set status=delivered
```

The page reads every week's `run.yaml` and receipts; nothing per week is typed into it. **Claude Code:** publish with the Artifact tool to the existing Valley OS page (same URL, read it first). **Codex/Astra:** there is no Artifact tool; the HTML file is the deliverable. Put its path in the receipt with `publish pending`, and the next Claude session republishes to the same URL. Never a markdown wall as the deliverable (memory: Readout OS; his 9/2 words: "the markdown files are impossible to read").

Posting checklist in the week folder (`day-plan.txt`, one line per post): day and time · story slide (the first frame, reposted to stories the same morning) · collab tag `@myhousesellers` when it is a team listing · first comment (the ask, restated in one line) · reply routing from the saved replies. Then the Feedback Triad on the page (like / don't like / top changes). Two rejected takes on one post = back to the input, never a third take.

Receipt: `DELIVER: page <URL or path> · N posts · status=delivered · triad pending`

### 8 · LEARN — the loop

Monday: `python3 execution/jen_pulse.py` (appends to `06-system/pulse/`). 1st of month: `/alyssa-stalker-outlier-audit` on the month → the attribute → next month's READ line; four numbers from Farrice into `FUNNEL-MATH.md`; `FACTS.md` re-check column; VAULT rows for everything that shipped; his verdicts into `jen-calibration-log.md`. On any day: one dated line under `## /jen` in `context/learnings.md` if the run taught something that transfers. When nothing is due, the receipt says so with `--skip`.

Receipt: `LEARN: pulse appended|not due · vault rows +N · calibration rows +N · learnings +N` then `python3 execution/run_log.py check "$WEEK"`.

## When Farrice corrects something, the fix lands in the file that owns it

| His correction is about | The file that owns it | Not here |
|---|---|---|
| her words, a line she would not say | `skills/jen-santulan-listing-content/references/jen-real-voice-profile.md` | the door, the caption alone |
| a verdict on a post (PASS / FAIL, in his words) | `skills/jen-santulan-listing-content/references/jen-calibration-log.md` | memory, chat |
| the order of operations, a missing receipt | this file | ENGINE-V2 (it points here) |
| the look of a card or reel | `build_reel.py` / `gen_photo.py` spec + `WINNERS.md` (the reel-look PASS row) | the post's copy |
| a fact, a number, a street | `FACTS.md` (the row, its label, its re-check date) | the caption |
| which slots a week gets | `CONTENT-MIX.md` | READ.md of one week |

## What this workflow refuses

- Writing before RESEARCH has a receipt. Rendering before CHECK has a receipt. Delivering as markdown. Calling a week done while `run_log.py check` fails.
- A second generator, a second facts ledger, a second voice file, a parallel Jen lane, a hand-edited COPY.md or captions.txt.
- Any recurring ask on Jen: her deal is a thumbs-up and same-evening replies (ENGINE-V2 §2).
- Talking-head reels, an intake questionnaire, a template she fills.

## Handoff

- Source evidence: FACTS.md rows (dated), pulse, outlier audit
- Output produced: one week folder (run.yaml, pipeline-log.md, COPY.md, READ.md, AMPLIFY.md, PNGs, reel specs + cover stills, captions.txt, day-plan.txt, saved-replies.txt) + the Valley OS page
- Validation: `python3 execution/run_log.py check "$WEEK"` → PASS
- Open risk: placeholders until her listing shoots land in Drive folder 01

## Rules (dated; edit in place when he corrects the door)

- 2026-09-09 · the run folder is the state: receipts via `run_log.py`, manifest from the renderer, page from the manifest. Chat is not a record.
- 2026-09-09 · a re-run of an already-built week is a real run: every step fires, the copy changes where the rules say it must (hook rule, voice bank), and the receipts say what was re-checked and what is due on send day.
- 2026-09-02 · one pen, one check in AMPLIFY (his "expert soup" correction).
- 2026-09-02 · the voice bank is drawn, never stamped; a hand line on the frame counts.
- 2026-09-11 · **the on-screen line is judged first, blind, against the specimen; harvested sentence + her plain reply; Forsyth and Kallaway pens.** Farrice's round-2 tap put four pairs at the bar and rejected every Luke Iha and Harding pair ("too disjointed, forced, and contrived"). Detail in step 4; record `week-of-2026-09-14/HOOK-ROOM-11.md`; calibration log rows 2026-09-09 and 2026-09-11.
