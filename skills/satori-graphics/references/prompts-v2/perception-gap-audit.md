---
name: "Satori Graphics — Perception-Gap Audit"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running Satori's **Perception-Gap Audit**: diagnosing the gap between what you INTEND and what the audience actually UNDERSTANDS. Amateurs argue taste; professionals measure the gap between the reading they engineered and the reading the viewer actually receives. A design you have to explain has already failed part of its job.

> "professional designers think in perception gaps instead. It's the gap between what you intend and what the audience actually understands." — Satori
> "Aesthetics are subjective, but confusion isn't. And if you need to explain a design, then that design probably has failed its job in some way." — Satori

This workflow assumes an intended hierarchy already exists — its job is to prove whether it actually transmits, not to build it.

## Input Required

- **[LAYOUT / DESIGN]** — a design with an established hierarchy (if none exists, this workflow does not apply — run a LIFT Composition Audit first to build one)
- **[LIVE VIEWERS AVAILABLE?]** — yes (Mode A) or no (Mode B — honest weight-order simulation)
- **[ARRIVAL CONTEXT]** — charity/nonprofit, fashion/lifestyle, SaaS/B2B landing, checkout/cart, social feed, or other (biases the first fixation before design even acts)
- **[REAL VIEWING CONDITION]** — device, brightness, attention state (the ground truth is the phone-at-night read, not the calibrated-monitor zoom)

## Execution Protocol

**Rule of this workflow**: commit to the intended reading in writing BEFORE extracting the perceived one. Declaring intent after seeing the recall is cheating — you'll rationalize whatever the viewer said.

### Step 1 — Declare the Intended Reading (write it first)

Force four decisions, each with a name and the dominance tool believed to carry it: **first fixation** (the one element the eye should hit in <1 sec), **second beat** (what carries them deeper), **third beat** (supporting proof/detail), **terminal beat** (where the journey should end — usually the CTA/action), and **acceptable-to-miss** (what you're deliberately OK with people skipping). Write the intended sequence as an ordered list `1→2→3→CTA`. If you cannot name the first fixation with confidence, halt — there is no hierarchy to test.

### Step 2 — Extract the Perceived Reading (Sequence-Recall Test)

**Mode A — Live viewer (preferred)**: show the layout for 3-5 seconds, hide it, then ask exactly *"In order, what do you remember seeing — first, then next, then next?"* Record the sequence, not the details. Never prompt ("did you see the button?"). Use a viewer who's never seen the piece. Run 2-3 viewers if available; note agreement (signal) vs. divergence (ambiguous zone).

**Mode B — Honest weight-order simulation (no live viewer)**: rank every element by raw pre-attentive pull — scale, luminance contrast, color saturation, isolation/whitespace, human face+eye-gaze, implied motion/lines, position (top-left LTR bias / optical center), pattern-break/novelty. The descending rank order IS the simulated recall sequence. Rank by what the eye is mechanically dragged to, not by what you wish were noticed.

Write the perceived sequence in the same `1→2→3→…` format. Flag any intended element that does NOT appear at all — the most important signal in this workflow.

### Step 3 — Build the Intended-vs-Perceived Map, Name Every Gap

Lay the two sequences side by side; the delta IS the gap. Name every gap by type:

| Gap name | Signature | Meaning |
|---|---|---|
| Lead-swap | Perceived-first ≠ intended-first | Hierarchy inverted |
| Ghost | Intended element never appears | Fell below attention threshold |
| CTA-blind | Terminal beat absent from sequence | Design didn't guide; funnel leaks here |
| Order-scramble | Right elements, wrong order | Eye journey isn't choreographed |
| Explanation | Map only reconciles if narrated | Fatal — trumps all taste discussion |

For each gap, write one sentence: element × wrong-behavior × consequence.

### Step 4 — Factor Arrival State and Real Viewing Context

Arrival state biases the first fixation before design acts (charity site = cautious/trust-hunting; SaaS landing = skeptical/time-boxed; checkout = anxious/friction-sensitive; social feed = distracted/thumb-moving). Re-run Step 2's read under the actual condition — small screen, low brightness, tired attention, one-handed. A gap that vanishes at 100% zoom on a calibrated monitor but reappears on a dimmed phone at night is real; the phone-at-night reading is ground truth. For each gap, mark whether arrival state or real viewing context causes or worsens it.

### Step 5 — Prescribe Gap-Closing Fixes (Quiet · Amplify · Match)

1. **QUIET** the wrong-first element — strip its dominance tools (subtract, don't stack).
2. **AMPLIFY** the intended-first/Ghost element — add the dominance tools it's missing.
3. **MATCH** the arrival state — re-sequence so what the viewer arrives hunting for is engineered to be first.

Write each fix as: `GAP → MOVE (quiet/amplify/match) → specific element change → predicted new recall position`. **Prioritize**: Explanation gap (fatal) → CTA-blind (funnel leak) → Lead-swap (hierarchy inverted) → Ghost (invisible) → Order-scramble (bouncing). Re-run Step 2 against the top fix before touching the rest.

### Step 6 — Audit Perception Around the Work

Perception creates value before a single element is read. Note one change to the *presentation* of this deliverable (file naming, deck pagination, comp framing) that reduces perceived-value leakage alongside the in-canvas fixes.

## Output Contract

A Perception-Gap Audit, in order: intended reading (with dominance-tool hypothesis per beat and acceptable-to-miss list), perceived reading (Mode A or B, with the weight-ranking table if Mode B), the intended-vs-perceived map, every named gap with its one-sentence diagnosis, state/context factoring per gap, a prioritized fix queue, a presentation note, and a re-test verdict.

## Output Skeleton

```markdown
# Perception-Gap Audit — [design name]

## Intended Reading (declared first)
1st: [...] (dominance tool: [...])
2nd: [...]
3rd: [...]
Terminal (CTA): [...]
Acceptable to miss: [...]

## Perceived Reading — Mode [A/B]
[if Mode B: weight-ranking table]
1st: [...] 2nd: [...] 3rd: [...] Missing: [...]

## Intended-vs-Perceived Map
INTENDED:  [...] → [...] → [...] → [...]
PERCEIVED: [...] → [...] → [...] → [...]

## Named Gaps
- [Gap type]: [element × wrong-behavior × consequence]

## State + Context Factoring
- [Gap]: caused/worsened by [arrival state / viewing context] — [explain]

## Prioritized Fix Queue
1. [GAP] → [MOVE] → [specific change] → predicted recall position: [...]

## Perception-Around-the-Work Note
[...]

## Re-Test Verdict
[Ship / Iterate again]
```

## Quality Gate

- The intended sequence was written before the recall was extracted — no post-hoc rationalization
- The perceived reading is an order of elements, not a critique of finish
- Live recall was unprompted, or the simulation ranked by raw pull, not wished-for importance
- Every delta is named by type — none left as vague dissatisfaction
- An Explanation gap, if present, is flagged fatal and sits atop the queue
- The read was checked at real (phone-at-night) conditions, not just calibrated-monitor zoom
- Every fix names element + move + specific change + predicted new recall position
- The top fix was re-tested and demonstrably shifted the recall toward intent

## Creative Latitude

The gap-naming taxonomy is fixed; the honesty of Step 2 is where this audit either does real work or becomes flattery. Resist the temptation to rank elements by what you wish were noticed — a simulation that confirms your own design is worthless. The fix prescriptions should lead with subtraction (QUIET) before addition (AMPLIFY); the most elegant fixes in this system remove a competitor rather than inflate the hero.

## Deploy When

A layout "looks fine" but you suspect people aren't getting the message in the intended order; stakeholders keep asking "wait, what am I looking at?"; a live asset underperforms and the hypothesis is comprehension, not offer or channel; or a CTA exists but nobody acts on it. Do not use before a hierarchy exists (run LIFT Composition Audit first), when the suspected failure is emotional tone (use Predictive Empathy Pass) or structural (use Flip-Test Technical Audit).
