---
description: Diagnose the gap between intended reading and actual understanding — declare the intended sequence, run the sequence-recall test, map intended-vs-perceived, name the gaps, prescribe prioritized fixes
---

# 18 — Perception-Gap Audit

> **/satori-perception-gap** — Diagnose the gap between what you INTEND and what the audience actually UNDERSTANDS. A design you have to explain has already failed part of its job.

Amateurs argue taste. Professionals measure the gap between the reading they engineered and the reading the viewer actually receives.

> *"professional designers think in perception gaps instead. It's the gap between what you intend and what the audience actually understands."* — Satori

Taste is where the argument stalls; the perception gap is where it gets settled. This workflow makes the gap **measurable** — you write down the reading you intended, you extract the reading the viewer actually got, and you close the delta with specific moves. It is the decision audit applied to comprehension, not aesthetics.

## Pre-Flight Gate

**Use this when**:
- A layout "looks fine" but you suspect people aren't getting the message in the order you meant
- Stakeholders keep asking "wait, what am I looking at?" — the design needs explaining to work
- A live asset underperforms and the leading hypothesis is *comprehension*, not offer or channel
- You're comparing two comps and want a comprehension verdict, not a beauty-contest verdict
- The CTA / key element exists on the page but nobody seems to act on it

**Do NOT use this when**:
- The layout has no established hierarchy yet — run `/satori-lift-audit` first; you can't measure a gap against an intended reading you never declared
- The suspected failure is emotional tone, not comprehension order — route to `/satori-predictive-empathy`
- The failure is structural/technical (drifting baselines, misalignment) — route to `/satori-flip-test`
- The brief itself is unclear — fix the brief via `/satori-why-before-what` before auditing perception
- It's pure typography selection (use Kittl) or DESIGN.md token work (use Jack Roberts)

This workflow assumes an intended hierarchy exists. Its job is not to *build* hierarchy — it's to prove whether the built hierarchy actually transmits. See genius.md GP-06 (LIFT) for the hierarchy layer this sits on top of.

## Skill Acquisition

```
Load: skills/satori-graphics/genius.md
  ├─ GP-06 (LIFT System — the intended hierarchy a perception gap exposes as real or fake)
  ├─ GP-04 (Movement & Flow Ladder — the eye journey you declared and are now testing)
  ├─ GP-02 (Predictive Empathy — the arrival state that biases the very first fixation)
  └─ HK-03 (Two Pairs of Eyes — fresh perception is the entire mechanism of the recall test)
Load: skills/satori-graphics/references/lift-system-decision-criteria.md   # dominance/visual-weight scoring for the simulation
Load: skills/satori-graphics/references/source-quotes.md                    # verbatim Satori grounding
```

If already hot on genius.md this conversation, skip the reload — read only `lift-system-decision-criteria.md` for the weight-scoring rubric used in Step 2.

## Execution

The rule of this workflow: **you must commit to the intended reading in writing before you extract the perceived one.** Declaring intent after seeing the recall is cheating — you'll rationalize whatever the viewer said. Decision before output, always.

### Step 1 — Declare the Intended Reading (write it down FIRST)

Before any testing, state the sequence you *engineered*. Force three decisions:

> *"Where does the eye land first? What gets noticed second? And what gets missed completely?"* — Satori

| Slot | Decision to commit | Example |
|---|---|---|
| **First fixation** | The one element the eye should hit in <1 sec | "The 3-word headline" |
| **Second beat** | What carries them deeper | "The product shot" |
| **Third beat** | The supporting proof / detail | "The stat line" |
| **Terminal beat** | Where the journey should *end* (usually the CTA / action) | "Book a call button" |
| **Acceptable-to-miss** | What you're deliberately OK with people skipping | "The legal footer" |

Write the intended sequence as an ordered list: `1 → 2 → 3 → CTA`. Note which dominance tool you *believe* is carrying each beat (scale / contrast / color / isolation / face-gaze / directional line). This is your hypothesis. Do not edit it after Step 2.

**Decision forced**: If you cannot name the first fixation with confidence, there is no hierarchy to test — halt and route to `/satori-lift-audit`.

### Step 2 — Extract the Perceived Reading (the Sequence-Recall Test)

Now get the reading the audience *actually* receives. Two modes.

**Mode A — Live viewer (preferred).**

> *"showing a layout for a few seconds and asking someone to describe what they remember in order. Not the details, but the sequence."* — Satori

Protocol:
1. Show the layout for **3–5 seconds only**, then hide it (close the tab, flip the phone, cover the print).
2. Ask exactly: *"In order, what do you remember seeing — first, then next, then next?"*
3. Record the **sequence**, not the details. "Big word, then a face, then a button" is the data. "The kerning on the subhead" is noise.
4. Do NOT prompt, hint, or ask "did you see the button?" — a prompted recall is a contaminated recall. Use a viewer who has never seen the piece (HK-03: fresh perception is the mechanism).
5. Run 2–3 viewers if available; note where their sequences agree (signal) and diverge (ambiguous zone).

**Mode B — Honest weight-order simulation (no live viewer).**

When there's no viewer, do not guess and do not flatter the design. Rank every element by raw pre-attentive visual weight, then read the ranking off as the predicted recall order. Score each element on these pulls (high pull first):

| Weight factor | Pulls the eye when… |
|---|---|
| **Scale** | It's physically the largest mass |
| **Luminance contrast** | It's the sharpest light/dark break against its ground |
| **Color saturation** | It's the one saturated accent in a quiet field |
| **Isolation / whitespace** | It's surrounded by emptiness (isolation reads as importance) |
| **Human face + eye-gaze** | A face is present (strongest pull); gaze direction then redirects |
| **Implied motion / lines** | Directional lines, arrows, or gradients point at it |
| **Position** | Top-left first-fixation bias (LTR reading); optical center for symmetry |
| **Pattern-break / novelty** | It's the one thing different from everything around it |

Rank elements by summed pull → **that descending order is your simulated recall sequence.** The discipline: rank by what the eye is mechanically dragged to, **not** by what you wish were noticed. If your intended-first element is third in the weight ranking, the simulation just told you the truth your eye had gone blind to.

**Decision forced**: Write the perceived sequence as an ordered list in the same format as Step 1: `1 → 2 → 3 → …`. Flag any intended element that does **not** appear in the recall at all — that is a missed element, the most important signal in this workflow.

### Step 3 — Build the Intended-vs-Perceived Map and Name the Gap

Lay the two sequences side by side. The delta between them IS the perception gap.

```
INTENDED:   Headline → Product → Stat → CTA
PERCEIVED:  Product → Headline → (CTA missed) → Stat
```

Diagnose against these named gap types (name every gap you find — an unnamed gap can't be prioritized or fixed):

| Gap name | Signature in the map | What it means |
|---|---|---|
| **Lead-swap gap** | Perceived-first ≠ intended-first | Hierarchy is inverted — the wrong element is winning the dominance fight |
| **Ghost gap** | An intended element never appears in recall | It fell below the attention threshold — invisible, not just secondary |
| **CTA-blind gap** | The action/terminal beat is absent from the sequence | The design didn't guide — the whole funnel leaks here |
| **Order-scramble gap** | Right elements, wrong order | Flow is bouncing; the eye journey (GP-04) isn't choreographed |
| **Explanation gap** | The map only reconciles once *you narrate it* | The fatal one — the design requires a voiceover to be understood |

> *"Aesthetics are subjective, but confusion isn't. And if you need to explain a design, then that design probably has failed its job in some way."* — Satori

The Explanation gap is the tell that trumps all taste discussion. If reconciling the two sequences required you to say "well, what I *meant* was…", log it as fatal and move it to the top of the fix queue regardless of how the piece scores on beauty.

**Decision forced**: For each named gap, write one sentence — *element × wrong-behavior × consequence*. Example: "The CTA button (charcoal on charcoal) is a Ghost gap — it never enters recall, so no viewer is guided to act."

### Step 4 — Factor the Arrival State and the Real Viewing Context

A perception gap is not measured in a vacuum. The same layout reads differently depending on the psychological state the viewer arrives in and the physical context they view it in. Correct for both before you prescribe.

**Arrival state (psychological).** What emotional posture is the viewer in *when they land*? This biases the first fixation before design even acts (GP-02).

| Context | Typical arrival state | Consequence for first-read |
|---|---|---|
| Charity / nonprofit site | Cautious, seeking-trust, guarded | Eye hunts for a trust cue first, not your hero headline |
| Fashion / lifestyle magazine | Relaxed, browsing, unhurried | Eye wanders by image appeal; text is skipped unless it earns a stop |
| SaaS / B2B landing | Skeptical, time-boxed, scanning | Eye seeks the "what is this + what do I do" answer in 3 sec |
| Checkout / cart page | Anxious, friction-sensitive | Eye snaps to price and the proceed button; anything else is noise |
| Social feed | Distracted, thumb-moving, sound-off | First 0.5 sec decides scroll-past vs stop |

**Viewing context (physical).** Design for the real device and the real moment, not the studio.

> *"someone scrolling on their phone at night, half tired, brightness turned down. That's who you're designing for, not someone zooming into your dribbble shot and actually analyzing your kerning at the micro pixel level."* — Satori

Re-run the Step 2 read under the *actual* condition: small screen, low brightness, tired attention, one-handed, no sound, in motion. A gap that vanishes at 100% zoom on a calibrated monitor but reappears on a dimmed phone at night is a **real** gap — the phone-at-night reading is the ground truth, the Dribbble zoom is the vanity metric.

**Decision forced**: For each named gap, mark whether the arrival state or the real viewing context *causes* or *worsens* it. A Lead-swap gap driven by "viewer arrives cautious and hunts for trust" is fixed differently than one driven by "low-brightness kills the contrast that was carrying the headline."

### Step 5 — Prescribe Gap-Closing Fixes (Quiet · Amplify · Match)

Every gap closes with one of three moves. Prescribe at the element level — specific, executable, no "improve hierarchy."

1. **QUIET the wrong-first element.** Whatever is stealing the first fixation gets its dominance tools stripped: reduce scale, drop luminance contrast, desaturate, remove isolation, break the gaze line. (Guards against Anti-Pattern #6 *more-equals-better* — you subtract, you don't add another loud thing.)
2. **AMPLIFY the intended-first (and any Ghost) element.** Add the dominance tools it was missing: scale it up, raise contrast against its ground, give it the one saturated accent, isolate it with whitespace, point a directional line or gaze at it, or move it toward the first-fixation zone.
3. **MATCH the arrival state.** If Step 4 found the state biases the read, meet it: lead with the trust cue for a cautious charity visitor; lead with price+button for the anxious checkout; make the first 0.5-sec image do the work for the distracted feed. Re-sequence so the element the viewer *arrives hunting for* is the one you engineered to be first.

Write each fix as: `GAP → MOVE (quiet/amplify/match) → specific element change → predicted new recall position`.

Example:
```
CTA-blind gap → AMPLIFY → recolor button charcoal→signal-orange, +40% scale,
  add 24px whitespace ring → predicted recall: enters at beat 2–3
```

**Prioritize the fix queue** in this order (fix top-down, re-test after the top fix before touching the rest):
1. Explanation gap (fatal — design needs narration)
2. CTA-blind gap (funnel leak)
3. Lead-swap gap (hierarchy inverted)
4. Ghost gap (intended element invisible)
5. Order-scramble gap (flow bouncing)

Then re-run Step 2 against the fixed comp and confirm the perceived sequence has moved toward the intended one. A fix that doesn't shift the recall order didn't work — it just felt like progress (HK-02: "feeling efficient" is the danger zone).

### Step 6 — Output the Map, and Audit the Perception AROUND the Work

Assemble the deliverable (spec in Output Requirements). Then run one last check that most designers skip: the perception gap doesn't stop at the canvas edge.

**Perception creates value.** The experience *around* the work — how the file opens, how the deck is paged through, how the comp is framed in the email, how the portfolio is sequenced — shapes the perceived value of the work itself before a single element is read. A brilliant layout handed off as a messy 40MB attachment named `final_v7_REAL.png` arrives pre-discounted. Standardize the wrapper (HK-04): identical presentation frame per concept, clean open, one comp per view, the intended reading uninterrupted. The gap you just closed inside the canvas can be re-opened by a sloppy container around it.

**Decision forced**: Note one change to the *presentation* of this deliverable that reduces perceived-value leakage, alongside the in-canvas fixes.

## Content-Type Adaptations

| Surface | Real arrival context | How the perception-gap method shifts (typical gap it surfaces) |
|---|---|---|
| **Poster / print** | Glanced at from 3–5m, in motion, peripheral vision | Recall test at *distance + thumbnail*, not reading distance. Typical gap: **Order-scramble** — multiple loud elements with no clear first fixation. Fix by brutal QUIET on all-but-one. |
| **Logo / identity** | Seen for a fraction of a second, thousands of times | The "sequence" collapses to **one** beat: is the mark recognized, and as *what*? Typical gap: **Explanation gap** — the mark needs its story told. A logo that must be explained fails GP-10. Route co-audit to `/satori-logo-concept`. |
| **UI / product** | Task-focused, scanning for the next action, impatient | Terminal beat = the primary action, always. Typical gap: **CTA-blind** — the primary button loses the weight fight to nav/chrome. AMPLIFY the one action; QUIET the furniture. |
| **Social / feed** | Thumb-moving, distracted, sound-off, 0.5-sec verdict | Recall window shrinks to ~1 sec; only beats 1–2 exist. Typical gap: **Ghost gap** on everything below the hook. MATCH the scroll-state: the first frame must transmit alone. |
| **Packaging** | Shelf competition, peripheral, among rivals, held at arm's length | Test *on a crowded shelf mock*, not isolated. Typical gap: **Lead-swap** — the category cue or a competitor's louder pack wins first fixation. AMPLIFY the single differentiator; test at shelf distance. |
| **Ad creative** | Interruptive, unwanted, skimmed with intent to skip | Terminal beat (offer/CTA) must survive a hostile, skip-primed reader. Typical gap: **CTA-blind** buried under decoration (Anti-Pattern #1). QUIET the decoration, AMPLIFY the offer, MATCH the skeptical arrival state. |

## Output Requirements

The deliverable is a **Perception-Gap Audit** containing, in this order:

1. **Intended reading** — the ordered sequence `1 → 2 → 3 → CTA` committed in Step 1, with the dominance tool hypothesized per beat, plus the acceptable-to-miss list.
2. **Perceived reading** — the ordered sequence extracted in Step 2, labeled Mode A (live, N viewers) or Mode B (weight simulation). For Mode B, include the weight-ranking table so the sequence is auditable, not asserted.
3. **Intended-vs-Perceived map** — the two sequences side by side with the deltas visible.
4. **Named gaps** — every gap named by type, each with its one-sentence *element × wrong-behavior × consequence*.
5. **State + context factoring** — per gap, whether arrival state or real viewing context (phone-at-night read) causes or worsens it.
6. **Prioritized fix queue** — fixes ordered fatal-first, each written as `GAP → MOVE → specific element change → predicted new recall position`, executable by a second designer without re-asking.
7. **Perception-around-the-work note** — one presentation/container change that reduces perceived-value leakage.
8. **Re-test verdict** — after the top-priority fix, the re-run recall order and whether it moved toward intent (Ship / Iterate again).

Every gap must be *named* and every fix must be *executable*. A naked "hierarchy is off" is not an output.

## Quality Gate

Guards against these genius.md anti-patterns:
- **#7 Loud-by-default** — the audit assumes the viewer arrives cold and distracted (Step 4), never pre-aligned.
- **#6 More-equals-better layering** — fixes lead with QUIET (subtract), not with adding another loud element.
- **#8 Aesthetic-first decisions** — the verdict is comprehension order, not beauty; "confusion isn't subjective."
- **#10 Comfort coasting** — the recall test forces fresh perception (HK-03) against the designer's own snow-blindness (HK-02).

Pass criteria — all must hold before delivery:
- [ ] **Intent declared first** — the intended sequence was written *before* the recall was extracted (no post-hoc rationalization).
- [ ] **Sequence, not details** — the perceived reading is an *order* of elements, not a critique of finish.
- [ ] **Honest extraction** — live recall was unprompted (fresh viewer), OR the simulation ranked by raw pull, not by wished-for importance.
- [ ] **Every gap named** — each delta is typed (Lead-swap / Ghost / CTA-blind / Order-scramble / Explanation), not left as vague dissatisfaction.
- [ ] **Explanation gap flagged fatal** — if the map only reconciled with narration, it sits at the top of the queue.
- [ ] **Ground-truth context** — the read was re-checked at phone-at-night conditions, not just calibrated-monitor zoom.
- [ ] **Executable fixes** — each fix names element + move + specific change + predicted new recall position.
- [ ] **Re-test done** — the top fix was re-run through Step 2 and demonstrably shifted the recall toward intent.

If any check fails, the audit is not deliverable — revise before handoff.

## Related Workflows

- **`/satori-lift-audit`** (01) — the hierarchy layer this sits on. Run it *first* to build the intended reading; run perception-gap *after* to prove the hierarchy actually transmits.
- **`/satori-predictive-empathy`** (07) — the emotional-state partner. Perception-gap measures *comprehension order*; predictive-empathy engineers the *arrival emotion* that biases the first fixation. Pair them when a gap is state-driven (Step 4).
- **`/satori-movement-ladder`** (02) — fixes Order-scramble gaps: choose the right movement level (1–6) to choreograph the sequence you want recalled.
- **`/satori-flip-test`** (10) — run when a gap turns out to be structural (drifting alignment, weight imbalance) rather than comprehension-order.
- **`/satori-anti-ai-slop`** (09) — when the perceived reading is "too clean / forgettable," the gap is memorability; add human imperfection.
- **`/satori-memory-encoding`** (08) — when elements are recalled in order but nothing *sticks* past 60 seconds, the gap is encoding, not sequence.
- **`/satori-why-before-what`** (04) — upstream fix when the map reveals elements that shouldn't be competing for attention at all (evict, don't re-rank).
