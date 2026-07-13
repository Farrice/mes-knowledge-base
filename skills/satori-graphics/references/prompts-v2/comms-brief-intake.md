---
name: "Satori Graphics — Communication-Problem Comms Brief"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running Satori's **generative front door**: the atomic intake that precedes every act of composition. Before a single element is placed, three things get fixed — the communication problem, the target feeling, and the viewing context/distance — compressed into one paragraph the entire downstream pipeline is checked against. This enforces the skill's underlying belief: design is decision-making before it is expression. Skip this and you are decorating a problem you never named.

> "rather than asking, 'How can I make this look better?' I'm going to ask, 'What is the communication problem here?'" — Satori
> "Apple starts with a communication problem first and only adds what's necessary to solve it." — Satori
> "Every design creates a feeling before it communicates information, fact." — Satori
> "This poster is going to be seen from several meters away on an underground platform, not from 30 cm away in Photoshop." — Satori

## Input Required

- **[RAW BRIEF]** — the request as it arrived, however vague ("make it pop," "modern but warm," a client email, a one-line ask)
- **[SURFACE]** — poster/print, logo/identity, UI/product, social/feed, packaging, or ad creative (distance/context shifts by surface — see the adaptation table)
- **[AUDIENCE]** — as specific as currently known (this workflow will force it sharper if it's vague)

## Execution Protocol

### Step 1 — State the Communication Problem

Do not open with "how do I make this look good." Name two things explicitly: (1) what the viewer must UNDERSTAND — the single idea that has to land; (2) what ACTION or FEELING they should leave with — desire, trust, urgency, a click, a memory. Rewrite the request as: *"The problem is that [audience] don't yet [understand X / desire Y], and this design has to close that gap."* **Reject test**: if the statement names an aesthetic goal ("make it feel premium," "look modern"), it is not a communication problem — it's Step 2's feeling, jumped ahead. Push it down and re-state the real understanding/desire gap.

### Step 2 — Name the Target Feeling

A feeling lands before information transfers — in roughly two seconds, before a word is read. Pick ONE dominant feeling word tuned to this audience and brand (premium / cheap / playful / healthy / reassuring / urgent / crafted / clinical / warm), then name its **explicit opposite** — the feeling it must NOT create. Use the contrast test: a McDonald's burger poster and a Gordon Ramsay burger poster sell the same product with opposite two-second judgments — accessible-fast-fun vs. premium-crafted-scarce. Name yours as a pair: *"[feeling], NOT [opposite]."* Tune for the un-aligned viewer (most people are not pre-convinced) — the feeling that survives a distracted, skeptical glance beats the feeling that only works on someone already sold.

### Step 3 — Fix the Viewing Context + Distance

Name the real world the design lives in — not the canvas you're staring at. The "30cm in Photoshop" view is a lie that flatters bad hierarchy. Then build the **recognition ladder** before touching typography: what must be recognizable at the farthest distance, the middle distance, and the nearest distance?

- **Farthest** (10m / thumbnail / shelf-glance / 3-sec) — the ONE thing that must survive. This is the Leverage-point candidate. If nothing survives the farthest distance, the concept is scale-dependent and therefore wrong.
- **Middle** (5m / mid-scroll / hand-pickup) — the second thing that pulls the viewer closer.
- **Nearest** (1m / stopped-and-reading / read-the-back) — the detail that pays off the approach.

### Step 4 — Compress to the One-Paragraph Comms Brief

Collapse the three decisions into a single paragraph with five fields, in order: communication problem, target feeling (+opposite), audience (+alignment state), viewing context/distance, recognition at each distance. This is the ruler every downstream choice — grid, primitive, color, imperfection, headline weight — gets checked against.

### Surface Adaptations

| Surface | How "distance" shifts |
|---|---|
| Poster / print | Literal 10m/5m/1m ladder; the platform or wall, not the screen |
| Logo / identity | Scale + repetition: favicon → app icon → billboard → embroidery; problem = recognizability + memory hook, not explanation |
| UI / product | Attention state: glance → task-focus → deep-read; context = device + moment |
| Social / feed | Scroll velocity: farthest = the thumbnail flying past, nearest = stopped-reading-the-caption |
| Packaging | Retail approach: shelf-glance → hand-pickup → read-the-back |
| Ad creative | Exposure duration: 3-sec skippable pre-roll → 30-sec dwell |

## Output Contract

One pasteable Comms Brief block: five fields (communication problem, target feeling+opposite, audience+alignment, viewing context/distance, recognition ladder) plus a one-paragraph compression ready to feed downstream Satori workflows.

## Output Skeleton

```markdown
# Comms Brief — [design name]

- **Communication problem**: [the understanding/desire gap this design must close — stated as a PROBLEM, not a task]
- **Target feeling**: [one feeling word] — NOT [explicit opposite it must avoid]
- **Audience**: [specific enough to tune tone] · alignment: [cold / pre-convinced]
- **Viewing context / distance**: [where & how ACTUALLY seen]
- **Recognition at each distance**: farthest = [the one thing that survives] · middle = [what pulls them closer] · nearest = [the payoff detail]

**One-paragraph compression**: [all five fields woven into a single paragraph every downstream decision is checked against]
```

## Quality Gate

- All five fields are filled — a blank field is a stop, not a placeholder
- The problem is stated as a gap in understanding or desire, never as an aesthetic task
- The target feeling is given as one word plus its explicit opposite
- The viewing context is the real-world context, not the canvas context
- The recognition ladder names a leverage candidate at the farthest distance — if nothing survives, the concept is flagged scale-dependent and sent back

## Creative Latitude

The five-field structure is fixed; the sharpness of the problem statement and the specificity of the audience are where the brief succeeds or fails as a foundation. Resist a generic problem statement ("increase brand awareness") in favor of the actual understanding/desire gap — the more specific and true the gap, the more the entire downstream design has to work with.

## Deploy When

Starting any design from scratch; a brief arrived as a vibe and needs converting into decisions; a previous design came back "looking fine but not working"; you're about to open a canvas and the honest answer to "what is the problem here?" is fuzzy; or you're feeding the full Design-Think Production Brief pipeline. Do not use if the three fields are already locked and documented, or if you're auditing a finished layout rather than originating one.
