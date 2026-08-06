# Script Annotation — bare script/essay → beat-mapped shooting doc

"10 minutes of comments saves hours of back-and-forth." The agent stops guessing and reads.
Never assemble from an unannotated script — ambiguity is cheapest to kill here.

## Input
Any script, essay, LinkedIn post, or Parallax piece (for essay→video conversion, first restructure for the ear: shorter sentences, spoken cadence, hook inside 5 seconds — voice stays his; load VOICE-CARD if rewriting lines).

## Output
`_active/<slug>/05-assets/video/script.md` — beats of 1-4 sentences, each with an ID and inline annotations:

```markdown
## b01 — hook
[music: tense pulse, low] [camera: start tight, rapid zoom out] [graphic: cold-open title card]
Everyone tells you the packaging bar is too high to compete. Here's how I ship studio-grade video from a laptop.

## b02 — the problem
[broll: screen recording of a cluttered editing timeline] [ref: frames/premiere-mess.jpg]
The old way costs $150 to $3,000 a video and a week of turnaround...

## b03 — the reveal
[graphic: pipeline diagram, 6 stages, Premium Minimal] [gesture: on "six stages", count on fingers]
[sfx: soft whoosh on each stage appearing]
My system does it in six stages...
```

## Annotation grammar (mirror into cutlist.beats[].notes)
- `[music: <mood/track>]` — bed changes, stings
- `[broll: <what to show>]` — feeds the broll-ladder
- `[graphic: <type + content>]` — named graphic types from the style file (title-card, stat-card, lower-third, diagram, quote-card)
- `[camera: <behavior>]` — zooms, punches, reframes (talking-head mode)
- `[ref: <path/url>]` — reference image to incorporate
- `[sfx: <cue>]` — sound effects
- `[gesture: <cue>]` — what body/hand moment a graphic should sync to

## Rules
- Every beat gets ≥1 annotation; a beat with zero annotations is an unanswered direction question — ask Farrice OR decide from the style file and mark the decision.
- Hook beat (b01) always specifies its first-5-seconds treatment explicitly.
- Annotation density is the #1 predictor of one-shot success — front-load taste here, not in QA.
