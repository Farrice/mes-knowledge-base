---
name: "Chase Hughes — Composite Influence Audit"
source_prompt: born-v2
skill: chase-hughes-conversational-influence
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running all five Chase Hughes conversational-influence patterns as a single composite audit against a finished or in-progress artifact — copy, ad, sales page, content piece, courtroom argument, pitch, profile, founder origin, or conflict situation. Hughes's own quality bar, stated once and applied everywhere: **the audience cannot point to where you persuaded them, because the conclusion appeared inside their own mind.** If they can name the moment you closed them, the persuasion was visible — and visible persuasion triggers resistance. This audit surfaces exactly where that visibility is leaking, axis by axis, and prescribes the rewrite for each leak.

## Input Required

- `[ARTIFACT]` — the full text to audit, pasted or fetched in full (audit-grade analysis requires the actual artifact, not a summary)
- `[CONTEXT]` — what the artifact is for, who it's addressed to, and what stakes ride on it landing

## Execution Protocol

Walk the artifact against each of the five patterns in turn. For each axis, use the tier description below to name where the artifact currently sits — do not invent a numeric score; name the tier and say why.

### Axis 1 — Engineered Self-Conclusion (Pattern 4)

- **Acceptable**: the conclusion is stated and the audience is asked to agree
- **Good**: the conclusion is implied via one example, but still gestured at explicitly
- **Hughes-grade**: two components are placed close together; the conclusion is never stated; the audience produces it spontaneously

For each persuasive moment, check for connector words ("therefore," "this is why," "what this means is…") that close the gap for the audience instead of leaving it open.
**If not Hughes-grade**: identify the two components that could replace the stated conclusion, stage them, cut the explicit conclusion. (See `/hughes-feel-clever`.)

### Axis 2 — Archetype Priming (Pattern 5)

- **Acceptable**: story metaphors are used decoratively, with no real archetype structure
- **Good**: an archetype is named explicitly ("this is a David and Goliath story")
- **Hughes-grade**: archetype components are primed; the archetype is never named; the audience advocates for the resolution on its own

For any narrative element (origin story, case study, testimonial, scene-setting), check whether the construction explains itself or performs itself.
**If not Hughes-grade**: identify which archetype the narrative is or could be priming, build a small inventory of environmental components specific to the actor, replace named-archetype language with primed-component language. (See `/hughes-archetype-prime`.)

### Axis 3 — Empathy Specificity (Pattern 1)

- **Acceptable**: surface judgment only ("they're annoying," "busy entrepreneurs")
- **Good**: some perspective-taking attempt, still generic
- **Hughes-grade**: the two-question ladder has clearly been run; a specific fear is named, not a generic pain point

Check whether demographic or status descriptors are doing the work that a fear hypothesis should be doing.
**If not Hughes-grade**: run the two-question ladder ("What does this person want me to think about them?" → "What would they be afraid of if that were true?") on the audience and replace demographic language with the resulting fear-specific language. (See `/hughes-empathy-ladder`.)

### Axis 4 — Manipulation Ethics (Pattern 3)

- **Acceptable**: misses obvious claim pairs placed close together with no explicit connector
- **Good**: catches some manipulative pairs, but only after the fact
- **Hughes-grade**: every adjacent claim pair with an implied-but-unstated connection has been identified in real time, and the implication is true, supported, and defensible if the author were challenged on it directly

For each adjacent claim pair with no explicit causal connector, ask whether the implied connection is legitimate inference-work or an unsupported nudge.
**If not Hughes-grade**: for each manipulative pair, either add an explicit connector (if the implication is true), cut one of the two claims (if unsupported), or restructure to break the proximity. (See `/hughes-two-ideas-detector`.)

### Axis 5 — Camera Angle (Pattern 2)

- **Acceptable**: the artifact stays at its default zoom throughout
- **Good**: multiple perspectives are acknowledged intellectually, but the zoom doesn't actually move
- **Hughes-grade**: the zoom level fits the persuasive goal, and the camera moves deliberately at the moments that need it

Check whether the artifact is locked at a fiber-level zoom (single moment, single client, single anecdote) when the goal needs a room- or building-level altitude, or vice versa.
**If not Hughes-grade**: identify the zoom level the goal actually needs, and restage the opening, closing, or a key transition at that altitude. (See `/hughes-camera-angle`.)

### Final Pass — Apply the Single Quality Bar

Set the five tier findings aside and apply Hughes's actual test directly to the artifact as a whole: **could the audience point to the exact moment they were persuaded?** If yes, name that moment. If no, say so. This is the real pass/fail — the five axes exist to locate *where* a "yes" answer is coming from, not to be averaged into one.

## Output Contract

- Per-axis finding: which tier the artifact currently sits at, with the specific textual evidence
- Per-axis prescribed rewrite for any axis not at Hughes-grade, pointing to the matching practitioner workflow
- The final single-bar verdict: can the audience name the moment they were persuaded — yes or no, with the moment named if yes
- A ranked list (not scored) of which 1-2 axes would move the artifact furthest if fixed first

## Output Skeleton

```
ARTIFACT AUDITED:
[type / context / length]

AXIS 1 — Engineered Self-Conclusion: [Acceptable / Good / Hughes-grade]
- Evidence: [specific lines/moments]
- Prescribed rewrite: [if not Hughes-grade]

AXIS 2 — Archetype Priming: [Acceptable / Good / Hughes-grade]
- Evidence: [...]
- Prescribed rewrite: [...]

AXIS 3 — Empathy Specificity: [Acceptable / Good / Hughes-grade]
- Evidence: [...]
- Prescribed rewrite: [...]

AXIS 4 — Manipulation Ethics: [Acceptable / Good / Hughes-grade]
- Evidence: [...]
- Prescribed rewrite: [...]

AXIS 5 — Camera Angle: [Acceptable / Good / Hughes-grade]
- Evidence: [...]
- Prescribed rewrite: [...]

FINAL QUALITY BAR:
- Could the audience name the moment they were persuaded? [yes / no]
- If yes: [name the exact moment]

PRIORITY FIX (1-2 axes, ranked by leverage, not score):
1. [axis] — [why fixing this one moves the artifact furthest]
2. [axis] — [...]
```

## Quality Gate

- Is every axis finding backed by specific textual evidence, not a vibe judgment?
- Are all five axes evaluated against the three named tiers only — no numeric scores, percentages, or invented thresholds anywhere in the output?
- Is the final verdict the single stated Hughes bar (can the audience name the moment), kept separate from and not averaged out of the five axis findings?
- Does the priority fix name genuine leverage reasoning, not just "the lowest axis"?
- Does every "not Hughes-grade" axis carry a prescribed rewrite tied to its matching practitioner workflow?

## Deploy When

- Final-pass review on copy, content, or an argument that has measurable stakes
- A draft "feels off" and you can't name why
- Diagnosing why a competitor's persuasive content is outperforming yours
- Building a pre-publish quality gate for high-leverage persuasive work
- Auditing back-catalog content for places a Hughes-grade rewrite would compound
