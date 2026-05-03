---
name: Composite Influence Audit
command: /hughes-influence-audit
expert: Chase Hughes
category: Stacking
description: Run all 5 Hughes techniques against any piece of copy, media, content, or argument. Produces a layered diagnosis surfacing where conclusions are stated, where archetypes are named instead of primed, where adjacent claims need ethics review, where camera angle is locked, and where empathy is generic.
inputs: A finished or draft artifact (copy, ad, sales page, content piece, courtroom argument, pitch, profile, founder origin, conflict situation)
outputs: A 5-axis diagnostic scoring each Hughes pattern (engineered self-conclusion, archetype priming, empathy specificity, manipulation ethics, camera angle), with prescribed rewrites for each fail
---

# Composite Influence Audit (`/hughes-influence-audit`)

You are running all five Chase Hughes techniques as a single composite audit against a finished or in-progress artifact. The output is a 5-axis diagnosis with concrete rewrites for each axis that fails. Use this as the **final gate before publishing/sending high-stakes persuasive work** — copy, courtroom arguments, founder narratives, premium-offer pages, sensitive client communications.

## When This Fires

Run this workflow whenever:
- Final-pass review on copy, content, or argument that has measurable stakes
- A draft "feels off" and you can't name why — the composite audit usually surfaces the structural issue
- Diagnosing why a competitor's persuasive content is outperforming yours
- Building a pre-publish quality gate for high-leverage work
- Auditing your own back catalog for places where Hughes-grade rewrites could compound

## Skill Acquisition

Load `genius.md` in full — all five patterns. Also load all five practitioner workflows (`hughes-feel-clever`, `hughes-archetype-prime`, `hughes-empathy-ladder`, `hughes-two-ideas-detector`, `hughes-camera-angle`) as the audit runs each in turn.

## Execution

### Step 1 — Capture the Artifact

Paste or fetch the full artifact text. Audit-grade analysis requires the artifact, not a summary.

### Step 2 — Audit Axis 1: Engineered Self-Conclusion (Pattern 4)

For each persuasive moment in the artifact, ask:
- Is the conclusion stated explicitly, or engineered through component placement?
- Are there connector words ("therefore," "this is why," "what this means is…") that close the gap for the audience?
- Is the audience left to make the click, or are they being told what to conclude?

**Score (1-10)**: 10 = no conclusions stated, all conclusions emerge in the reader's mind from component placement. 1 = every conclusion stated, every connection explicit.

**Prescribed rewrite if low**: For each stated conclusion, identify the two components that could replace it. Stage them. Cut the explicit conclusion. See `/hughes-feel-clever` for the construction protocol.

### Step 3 — Audit Axis 2: Archetype Priming (Pattern 5)

For any narrative element in the artifact (origin story, case study, testimonial, scene-setting, opening anecdote), ask:
- Is an archetype primed via environmental components, or is the archetype named?
- Is the resolution stated, or left for the audience's brain to complete?
- Does the construction explain itself ("this is a David and Goliath story") or perform itself?

**Score (1-10)**: 10 = archetype emerges from components without ever being named. 1 = archetype labeled and resolution stated.

**Prescribed rewrite if low**: Identify which archetype the narrative is (or could be) priming. Build a 3-5 component inventory specific to the actor. Replace named-archetype language with primed-component language. See `/hughes-archetype-prime`.

### Step 4 — Audit Axis 3: Empathy Specificity (Pattern 1)

Wherever the artifact addresses or describes the audience, ask:
- Is the audience addressed via specific fears or via generic pain points?
- Does the language produce a flinch of recognition, or does it sound like every other piece in the genre?
- Are demographic descriptors doing the work that a fear hypothesis should be doing?

**Score (1-10)**: 10 = the audience is addressed via a specific fear that produces recognition. 1 = the audience is described via demographics, status labels, or generic pain points ("busy entrepreneurs," "high-performers," "scaling founders").

**Prescribed rewrite if low**: Run `/hughes-empathy-ladder` on the audience to surface the actual fear. Replace demographic language with fear-specific recognition language.

### Step 5 — Audit Axis 4: Manipulation Ethics (Pattern 3)

Run the two-ideas-no-string detector across the artifact, then evaluate:
- Are there adjacent claims with no explicit connector that engineer inferences?
- Are those engineered inferences supported by the underlying facts?
- Would the author defend each implied connection if challenged directly?

**Score (1-10)**: 10 = every implied connection is true, supported, and defensible if surfaced. 1 = the artifact engineers inferences via proximity that the author would not defend if asked directly.

**Prescribed rewrite if low**: For each manipulative pair, choose: (a) add an explicit connector if the implication is true, (b) cut one of the two claims if the implication is unsupported, (c) restructure to break the proximity. See `/hughes-two-ideas-detector`.

### Step 6 — Audit Axis 5: Camera Angle (Pattern 2)

For the artifact as a whole, ask:
- What zoom level is the camera at?
- Is the zoom appropriate for the persuasive goal? Or is the artifact stuck at a fiber-level zoom when it needs the room or building level?
- Does the camera move during the artifact, or stay locked?

**Score (1-10)**: 10 = the camera is at the right altitude for the goal and moves deliberately when needed. 1 = the camera is locked at a zoom that is making the artifact feel either claustrophobic (too zoomed-in) or weightless (too zoomed-out).

**Prescribed rewrite if low**: Run `/hughes-camera-angle` on the artifact. Identify the right zoom for the goal. Restage opening, closing, or transition moments at the appropriate altitude.

### Step 7 — Composite Score and Verdict

Average the five axis scores. Apply this rubric:

| Composite | Verdict | Recommended Action |
|---|---|---|
| **9.0+** | Hughes-grade | Ship. The persuasion is invisible. |
| **7.5-8.9** | Strong but visible in places | Ship with named edits to the lowest-scoring axis only. |
| **6.0-7.4** | Mid-tier — works but leaves leverage on the table | Run prescribed rewrites for the two lowest axes before shipping. |
| **<6.0** | Below Hughes-grade — likely to underperform | Hold. Run prescribed rewrites for all axes scoring below 7. Re-audit. |

**Veto rule**: Any axis scoring below 4 vetoes the artifact regardless of composite. A single hard fail will compromise the whole.

## Output Format

```
ARTIFACT AUDITED:
[type / context / length]

AXIS 1 — Engineered Self-Conclusion: [score] / 10
- Findings: [specifics]
- Prescribed rewrite: [if needed]

AXIS 2 — Archetype Priming: [score] / 10
- Findings: [...]
- Prescribed rewrite: [...]

AXIS 3 — Empathy Specificity: [score] / 10
- Findings: [...]
- Prescribed rewrite: [...]

AXIS 4 — Manipulation Ethics: [score] / 10
- Findings: [...]
- Prescribed rewrite: [...]

AXIS 5 — Camera Angle: [score] / 10
- Findings: [...]
- Prescribed rewrite: [...]

COMPOSITE: [score] / 10
VERDICT: [Hughes-grade / Strong / Mid-tier / Below-grade]
VETO FLAGS: [any axis below 4]

RECOMMENDED ACTION: [specific next step]
```

## Example Output

**ARTIFACT AUDITED**: A 250-word LinkedIn post pitching a $5K coaching offer to mid-career executives.

**AXIS 1 — Engineered Self-Conclusion: 4/10**
- Findings: Five explicit "this is why you need to..." constructions. Every conclusion is stated. Reader is told what to think four times.
- Prescribed rewrite: Identify the strongest two components in the post (the 2:47 a.m. open and the client's voice memo) and let them sit in proximity without the conclusion-pushes.

**AXIS 2 — Archetype Priming: 7/10**
- Findings: A "Long Wait" archetype is implicitly being primed (years of grinding, then arrival), but the post then names it ("seven years of work paid off") which collapses the priming.
- Prescribed rewrite: Cut the labeling sentence. Let the components do the work.

**AXIS 3 — Empathy Specificity: 5/10**
- Findings: The audience is called "high-performing executives" three times. This is a tier descriptor, not a fear hypothesis. It mirrors the exact fear (structural replaceability) that the audience is trying to defend against.
- Prescribed rewrite: Replace "high-performing executive" language with the fear-specific recognition language from `/hughes-empathy-ladder` Output A: *"the operation runs whether or not you're the one running it."*

**AXIS 4 — Manipulation Ethics: 9/10**
- Findings: One borderline pair (testimonial proximity to ROI claim with no causal string) but the implication is true and defensible. No manipulation flags.
- Prescribed rewrite: None required.

**AXIS 5 — Camera Angle: 6/10**
- Findings: Post is locked at the fiber zoom (single conversation, single client, single moment). For a LinkedIn pitch, the room-zoom (the role of this kind of work in the reader's life trajectory) would land harder.
- Prescribed rewrite: Add a single sentence near the close that pulls the camera to the room zoom: *"Three years from now, you'll either be doing what you're doing now, or you'll be the person who took the call."*

**COMPOSITE: 6.2 / 10**
**VERDICT: Mid-tier**
**VETO FLAGS: none (lowest is 4, just clears)**

**RECOMMENDED ACTION**: Hold the post. Run prescribed rewrites for Axis 1 (most leverage) and Axis 3 (cheapest fix). Re-audit. Do not publish at current state — the post will underperform a Hughes-grade rewrite by an estimated 2-3x on the same offer.

**What elevates this audit**: The five-axis structure forces every persuasive failure mode to be named, scored, and addressed with a specific rewrite. It replaces "this feels off" with "Axis 1 is at 4/10 because of these specific stated conclusions." That precision is the difference between editing for vibes and editing for conversion.

## Pairs With

- All five Hughes pattern workflows (the audit invokes each)
- Adversarial-review skill — Hughes audit + adversarial review = pre-publish quality gate
- McRaney deep-canvass workflows — for axes 1 and 3, McRaney's belief-change moves can replace stated conclusions with question-based engineered ones
- Connelly subtext workflows — for axis 1 in narrative/dialogue contexts
