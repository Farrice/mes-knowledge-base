---
description: "/jcin-story-15s — the 3-shot/15-second micro-story: spine intake (or stack /stanton-premise-sentence · /bw-log-line upstream), grab → emotional payoff → unresolved questions judged by question count, one costed production prompt with timestamped beats and a native-resolution decision"
---

# Story in 15 Seconds (Joey Cinema OS)

Joey's story contest brief is one sentence long: *"What's a story that you can tell in 15 seconds that grabs the attention, gives an emotional payoff, and leaves us wanting more?"* Three shots. Fifteen seconds. Literally one prompt. When he judged the last round, the fantasy-castle winner didn't win on render quality — it won because it made him ask four questions: why does the knight barge in? why was he ordered to kill the princess? why does he back down? why does she help him? Unresolved tension is the win condition. Resolution is not. This workflow builds that artifact: a micro-story engineered for question count, compiled into ONE block-structured Seedance prompt with timestamped beats, costed before anything generates (~330 credits observed for a 15s Seedance 2.0 run), with the resolution decision made at generation time — because native 4K "is much different than 720p upscaled to 4K."

## Pre-Flight

Read before executing:
1. `skills/joey-cinema-os/genius.md` (judgment layer — esp. patterns 8, 10, 14, 21; Hidden Knowledge § 3-shot/15-second story test)
2. `skills/cinema-worldbuilder-pro/SKILL.md` (§ CUTS & TIMING PRECISION SCALE, § RUNTIME & PER-SHOT TIMING, § block order — the LOCKED grammar this compiles into)
3. `extractions/joey-cinema-os/reference-corpus/joey-character-prompt-and-seedance-prompt.md` (§3 — the real 330-credit rooftop-runner prompt: "heels hit the ledge at 7.0s... again at 11.0s")
4. `extractions/joey-cinema-v1/visual-context.md` (§3 contest mechanics + winner judging logic, verbatim)

> 🔒 **Pre-Flight Gate** — three checks, in order:
> 1. **The Existence Question.** Does the character/subject already exist as a locked reference? Unbuilt character in a 15s ask → kick to `/jcin-character-lock` first (or run character-free: environment, object, vehicle). Never generate a story on an unlocked identity.
> 2. **Spine check.** Is there an actual story — a character, a want, a turn — or just a vibe? A vibe produces "coherent action," which scores 4 on the rubric. If the spine is fuzzy, the stacking pre-steps below sharpen it before a single beat gets timed.
> 3. **Cost gate is live.** This workflow's job ends at the code block. Any real generation runs through `python3 execution/higgsfield_budget_guard.py check` (MCP surface) or the Fal guard — never auto-fired, and seedance-1080p on Fal is HARD-BLOCKED.

## Input Required

- The story seed — a premise, a comment-length pitch, a brand moment, or "generate candidates for X"
- Who/what is in frame, and the lock status of each (built reference + tag name, or "needs building")
- Where it runs (contest / brand teaser / LinkedIn / series beat) — this sets aspect ratio, resolution honesty, and how hard shot 1 must grab
- Runtime confirmation (default 15s for the contest format; never assume — the worldbuilder rule is ask, don't default)
- Tag names for every reference, user-supplied (never invented on their behalf)

## Skill Acquisition (optional stacking pre-steps — offers, never pipeline steps)

The visual pipeline renders whatever spine you hand it; these partners make the spine worth 330 credits. Each is one command, each is skippable when the story already grips:

- **`/stanton-premise-sentence`** (`.agent/workflows/stanton-premise-sentence.md`) — distill to one true premise sentence (character + conflict + conclusion), then use it as the litmus for all three shots. Strongest when the story feels "almost there."
- **`/bw-log-line`** (`.agent/workflows/bw-log-line.md`) — customer-as-hero log line + the 30-second subtraction cut. Strongest for BRAND teasers, where the viewer must be the hero and the product the bridge.
- **`/stanton-spine`** or **`/stanton-30sec-arc`** (`.agent/workflows/`) — when the 15s piece is one beat of a longer series and the arc has to escalate across episodes.

Take the premise/log line back as the **Scene & Mood seed** — their thinking enters the prompt as observable action, never as their terminology.

## Execution

### Step 1: Intake or generate the story — three shots, named as questions
Write the micro-story as exactly three beats, and for each beat write down the question it plants in a cold viewer:

| Shot | Job | The question it must plant |
|---|---|---|
| 1 | **Grab** — attention seized inside the first beat | "wait — what is happening?" |
| 2 | **Payoff** — the emotional turn (the knight's crying, bloodshot eyes) | "why did that land on me?" |
| 3 | **Unresolved** — the door left open | "why does he back down? why does she help him?" |

**The judge is question count.** Read the three beats to yourself as a stranger and tally the "why"s. Fewer than 2 → the story resolves too cleanly or never grabbed; rework the beats before touching the prompt. Joey's winner produced four. If you're generating candidates instead of intaking one, draft 3–5 three-beat stories and score each by tally; the winner is the one you can't stop interrogating, not the prettiest.

### Step 2: Beat sheet — time, action, speed treatment
Convert the three shots into a timestamped beat sheet summing to 15.0s. Every beat gets three columns, per the production exemplar ("a slow-motion beat interval at the moment her heels hit the ledge at 7.0s and again as she comes up over the ledge at 11.0s"):

| Beat | Time window | Action (write the visible — muscle, km/h, %, meters) | Speed treatment |
|---|---|---|---|
| 1 | 0.0s → Xs | | real-time / slow-motion (fps + 180° shutter) |
| 2 | Xs — HARD CUT → Ys | | |
| 3 | Ys — HARD CUT → 15.0s | | |

Rules from the locked grammar, non-negotiable:
- **Hard cut at every speed change.** One speed per beat; never blend speeds inside a continuous shot.
- 12–15s carries **2–3 simple beats maximum** — one dominant action per beat. A fourth beat means this isn't a 15s piece; split it.
- Close the door: *"the camera does not add any additional cuts, edits happen only at the marks written above."*
- Emotion in muscle, speed in km/h, atmosphere in % and meters. A word that doesn't produce a visible pixel gets cut.

### Step 3: Compile ONE production prompt (worldbuilder grammar, mode-matched)
Hand the beat sheet + spine + locked references to the cinema-worldbuilder grammar and compile a single prompt in full block order (Scene & Mood → Frame Map → Subject Lock(s) → Cross-Frame Rules → Movement → Last Frame → World Plate → Sound Bed → Capture Realism → Camera Capture). Pick the mode (M1–M5) from the mode-select table; FOV from the degree ladder only; the timed-multishot format carries the beats inside Movement. Run the worldbuilder's pre-prompt confirmation (tags first, runtime last) before the prompt writes. Contest register = the prompt must stand alone: no names, no brands, no platform words, references carrying identity, prompt carrying framing. Multi-shot ceiling: 600 words.

### Step 4: Cost + resolution decision — BEFORE generate
- **Cost:** declare the duration in the title and Camera Capture line (both must match). Observed economics: **~330 credits for a 15s Seedance 2.0 generation** (~117 credits/13s at 1080p as the baseline unit). Budget takes honestly — the win condition is 2–3 takes, never one-shot magic. State the take budget: `15s × N takes ≈ credits`.
- **Resolution:** decide native resolution NOW. **Seedance 4K native ≠ 720p upscaled to 4K** — resolution is a generation-time decision, not a post decision. Contest/showcase pieces and anything a client sees full-screen → 4K native and cost it; feed-only short-form → 1080p is honest.
- Surface the guard pre-flight command with the plan. Generation is Farrice's trigger, not the workflow's.

### Step 5: The stranger replay
Before delivering, replay the prompt as the finished 15 seconds in your head, cold. Tally the questions again — the compile step loves to accidentally ANSWER shot 3's question with a too-explicit Last Frame. The Last Frame holds the unresolved image (dagger on the floor, hand reaching), never the explanation.

## Content Type Adaptations

| Format | Adaptation |
|---|---|
| **Brand teaser** | Run `/bw-log-line` upstream; the customer is the hero of shot 1–2, the product appears as the bridge — never the protagonist. Shot 3's unresolved question should be answerable only by the brand ("where do I get that?" counts as a why). Product in frame → `/jcin-product-lock` reference attached, canonical-over-plate. |
| **Contest-format content** | The literal Joey format: 3 shots / 15s / ONE prompt, judged on question count. Go 4K native — judges see it full-screen. Brief must stay "brief enough without sacrificing the details." |
| **LinkedIn / short-form video hook** | The 15s piece IS the hook above a text post; shot 1 must grab inside 1.5s (scroll physics beat cinema physics). 9:16 or 1:1 framing declared in Frame Map; captions live in the post, never rendered in-frame (Last Frame suppression line stays). 1080p native is usually the honest spend. |
| **Series beat** | Stack `/stanton-series-escalation` upstream; each 15s episode ends on a bigger unresolved question than the last. Identity locks carry across episodes unchanged — that's the pipeline's whole point. |

## Output Requirements

Deliver in this order, nothing else:
1. **The three-beat story** (3 lines) + **question tally** with the questions written out verbatim (must be ≥2).
2. **Beat sheet table** — time / action / speed treatment, hard cuts marked, summing to 15.0s.
3. **ONE production prompt** — bolded title with runtime (`**Seedance prompt — 15s**`), then a single fenced code block in full worldbuilder block order with the user's `@tags` inline.
4. **Cost + resolution card** — credits per take (~330/15s observed), take budget, native-resolution call with one-line rationale, and the guard pre-flight command.
5. Optional pre-steps used (if any) named in one line — never presented as required stages.

Execution prompt: references/prompts-v2/micro-story-15s.md — honor its Output Contract.

```
15-SECOND STORY — [working title]

THE THREE BEATS:
  1. GRAB:       __________
  2. PAYOFF:     __________
  3. UNRESOLVED: __________
QUESTION TALLY (≥2 required): "why ______?" · "why ______?" · [...]

BEAT SHEET (sums to 15.0s, hard cut at every speed change):
  0.0s → _s   — [action, visible] — [real-time / 96fps slow-motion, 180° shutter]
  _s — HARD CUT
  _s → _s     — [action] — [speed]
  _s — HARD CUT
  _s → 15.0s  — [closing action; Last Frame holds the question] — [speed]

**Seedance prompt — 15s**
[single fenced code block: Scene & Mood → Frame Map → Subject Lock(s) →
 Cross-Frame Rules → Movement (timecoded beats + no-additional-cuts line) →
 Last Frame → World Plate → Sound Bed → Capture Realism → Camera Capture]

COST CARD: ~330 credits/take at 15s · take budget: __ takes ≈ __ credits
RESOLUTION: [4K native / 1080p] because __________ (decided at generation, not post)
GUARD: python3 execution/higgsfield_budget_guard.py check   ← human-triggered
PRE-STEPS USED: [none / /stanton-premise-sentence / /bw-log-line / ...]
```

The rooftop-runner exemplar is the calibration artifact for beat grammar — one sprint, one leap at 7.0s, one rise over the ledge at 11.0s, slow-motion intervals tied to both marks, restricted warm accents "as the ONLY warm" against a cool grade. Three beats, two timestamps, one prompt, 330 credits. Match that shape, not its content.

## Quality Gate

> 🛡️ Anchor against `genius.md § Quality Rubric` — this workflow lives or dies on **Story grip** (10 = grab → payoff → unresolved "why"s) and **Credit economy** (10 = 2–3 takes, budgeted knowingly).

- **Question count ≥2, written out.** If you can't quote the viewer's "why"s, the story resolves too neatly — a coherent story that answers itself scores 4, not 10.
- **Exactly 3 shots, exactly 15.0s, exactly one prompt.** Beat times sum; title runtime = Camera Capture runtime.
- **Every speed change sits on a HARD CUT**, and the no-additional-cuts line closes the door.
- **Write-the-visible holds** — no mood words, emotion in muscle, speeds in km/h, atmosphere in % / meters.
- **No names, no brands, no ages, no platform words** in the prompt body; references carry identity, prompt carries framing; no re-description of what an attached reference shows.
- **Costed before generate** — credits stated, take budget stated, resolution decided natively, guard command surfaced. A prompt delivered without its cost card is unfinished.
- **Unbuilt identity never shipped** — any character in frame traces to a locked reference or the workflow kicked to `/jcin-character-lock` first.

## Common Pitfalls

- **Resolving shot 3.** The instinct to "land the ending" kills the format — Joey's winner ends on the princess reaching toward the knight who came to kill her, not on an explanation. Recovery: rewrite the Last Frame as the unresolved image and delete every clause that answers a tallied question.
- **Four beats in fifteen seconds.** Overloaded action is the worldbuilder's top repair-pass flag; a fourth beat means the model rushes all of them. Recovery: subtraction — cut to the three that carry the questions, push the rest to a sequel prompt (that's a series, and it's a feature).
- **Vibes instead of timestamps.** "She leaps in slow motion near the end" drifts; "heels hit the ledge at 7.0s, 96fps slow-motion interval holding 180° shutter" holds. Timestamps not vibes; degrees not millimeters.
- **Patching a bloated prompt on take 4.** Past ~3 failed iterations the prompt has accreted — cut it, reset it, let it breathe, re-add only what's necessary. The post-reset prompt should be SHORTER and hit in ≤3 takes.
- **Skipping the cost card because "it's just one prompt."** One 15s prompt is ~330 credits per take × real takes. Cost Before Generate is a signature move precisely because single prompts feel free.
