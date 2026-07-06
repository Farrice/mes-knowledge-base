---
description: The generative front door — defines the communication problem, the target feeling, and the viewing context/distance before any composition begins, and compresses them into a one-paragraph brief every downstream decision is checked against.
---

# 15 — Communication-Problem Intake (/satori-comms-brief)

> The atomic intake that comes before composition. Three decisions — what is the communication problem, what feeling do we want, where/how is this actually seen — compressed into one paragraph the whole pipeline is checked against.

This is the generative FRONT DOOR to every Satori design. Before a single element is placed, three things get fixed: (1) the communication problem, (2) the target feeling, (3) the viewing context and distance. Every other workflow in this skill audits or composes *after* these are locked. Skip this and you are decorating a problem you never named.

## Pre-Flight Gate

**Use this when**:
- Starting any design from scratch — poster, logo, UI, social tile, package, ad
- A brief arrived as a vibe ("make it pop", "modern but warm") and needs converting into decisions
- A previous design came back "looking fine but not working" — the communication problem was never stated
- You are about to open a canvas and the honest answer to "what is the problem here?" is fuzzy
- Feeding the `/satori-design-think` pipeline — this is the intake it composes first

**Do NOT use this when**:
- The three fields are already locked and documented (skip; go straight to concept/composition)
- You are auditing a finished layout, not originating one (use `/satori-lift-audit` or `/satori-why-before-what`)
- The task is pure typography selection (use Kittl per genius.md "When NOT to Use Satori Tools")
- It is production-only work with the thinking already done (go direct to `/satori-poster-think` → `fantastic-posters`)

This workflow enforces genius.md's underlying belief: **design is decision-making before it is expression.** The comms brief is the first decision audit — machinery upstream of every aesthetic move.

## Skill Acquisition

```
Load: skills/satori-graphics/genius.md
  ├─ GP-01  Why-Before-What Decision Gate     (the problem is the rent ruler)
  ├─ GP-02  Predictive Empathy                (target feeling = engineered NEXT emotion)
  ├─ GP-06  LIFT System — L + T               (recognition-at-distance seeds Leverage + Transferability)
  ├─ GP-08  One-Sentence Brief Reduction      (sibling compression — sits downstream of this)
  └─ HK-06  Transferability ≠ Responsive       (distance ladder is conceptual, not just px)

Load (optional): references/source-quotes.md   — verbatim Satori/Apple phrasing
```

No other reference files required. The three decisions are self-contained; deeper context only matters once you move to composition.

## Execution

Four steps. Each forces a decision before any output. Nothing is skippable — a blank field is a stop, not a shrug.

### Step 1 — State the COMMUNICATION PROBLEM

Do not open with "how do I make this look good." Open with the reframe:

> *"rather than asking, 'How can I make this look better?' I'm going to ask, 'What is the communication problem here?'"*

The Apple lens is the model. Every decision starts from a question about the viewer, not the artwork:

> *"every design decision here with Apple starts with a question. What helps people understand and desire this product?"*

> *"Apple starts with a communication problem first and only adds what's necessary to solve it."*

Write the problem as a **gap**, not a task. Name two things explicitly:

1. **What must the viewer UNDERSTAND?** — the single idea that has to land. (e.g. "this recovery drink is for athletes, not casual gym-goers")
2. **What ACTION or FEELING do you want them to leave with?** — desire, trust, urgency, a click, a memory.

**Decision forced**: rewrite the request as a problem statement of the form *"The problem is that [audience] don't yet [understand X / desire Y], and this design has to close that gap."*

**Reject test**: if your statement names an aesthetic goal ("make it feel premium", "look modern"), you have not stated a communication problem — you have jumped to Step 2's feeling. Push the aesthetic goal down to Step 2 and re-state the actual understanding/desire gap here. "Only add what's necessary to solve it" is impossible until the "it" is named.

### Step 2 — Name the TARGET FEELING

Before information transfers, a feeling has already landed. This is a fact of perception, not a nicety:

> *"Every design creates a feeling before it communicates information, fact."*

On a busy platform, a street, a shelf, the feeling is decided in roughly two seconds — before a single word is read:

> *"your brain has already decided whether this feels premium, healthy, playful, cheap, or whatever."*

**Decision forced**: pick ONE dominant feeling word tuned to *this* audience and *this* brand — premium / cheap / playful / healthy / reassuring / urgent / crafted / clinical / warm. Then name its **explicit opposite** — the feeling it must NOT create.

Use the contrast test to keep it honest: a McDonald's burger poster and a Gordon Ramsay burger poster sell the *same product* and engineer *opposite feelings* — accessible-fast-fun vs premium-crafted-scarce. Same object, opposite two-second judgment. So name yours as a pair: *"[feeling], NOT [opposite]."* ("Premium, NOT fast-food-cheap." "Accessible-playful, NOT fine-dining-cold.")

**Tune for the un-aligned viewer** (GP-02 Predictive Empathy): most people are not pre-convinced. The target feeling is the *next* emotion you want them carrying, not the loudest note you can hit. When in doubt, the feeling that survives a distracted, skeptical glance beats the feeling that only works on someone already sold.

### Step 3 — Fix the VIEWING CONTEXT + DISTANCE

Where and how is this *actually* seen? Not the canvas you are staring at — the real world it lives in.

> *"This poster is going to be seen from several meters away on an underground platform, not from 30 cm away in Photoshop."*

The 30cm-in-Photoshop view is a lie that flatters bad hierarchy. Name the real context: an underground platform at several meters; a phone at night, half-tired, brightness turned down; a supermarket shelf glanced at across an aisle; a 3-second pre-roll before the skip button.

Then build the **recognition ladder** — what must be recognizable at each falling distance — *before* you touch type:

> *"before I touch the typography, I want to ask myself what somebody needs to recognize from 10 m, 5 m, and finally 1 m."*

**Decision forced**:
- **Farthest (10m / thumbnail / shelf-glance / 3-sec)** — the ONE thing that must survive. This is your Leverage-point candidate (GP-06 L). If nothing survives the farthest distance, the concept is scale-dependent and therefore wrong (HK-06).
- **Middle (5m / mid-scroll / hand-pickup)** — the second thing that pulls them closer.
- **Nearest (1m / stopped-and-reading / read-the-back)** — the detail that pays off the approach.

This ladder pre-determines element sizing and dominance before a single font decision — which is exactly the point. Type serves the ladder; the ladder does not wait on type.

### Step 4 — Compress to the ONE-PARAGRAPH COMMS BRIEF

Collapse the three decisions into a single paragraph with five fields. This is the ruler. Every downstream choice — grid, primitive, color, imperfection, headline weight — gets checked against it. If a choice does not serve the brief, the choice is wrong (not the brief).

Five fields, in order:
1. **Communication problem** — the understanding/desire gap (Step 1)
2. **Target feeling** — one word + its explicit opposite (Step 2)
3. **Audience** — specific enough to tune tone; note their alignment state (cold vs pre-convinced)
4. **Viewing context / distance** — the real context, not the Photoshop context (Step 3)
5. **Recognition at each distance** — what survives farthest → middle → nearest (Step 3)

This is the sibling of GP-08's one-sentence brief, and it sits *upstream* of it: the comms brief names the communication problem, feeling, and viewing reality; the one-sentence reduction then compresses the *concept* that solves it. Comms brief first, concept sentence second.

## Content-Type Adaptations

The three decisions are constant; "distance" is what shifts by surface.

| Surface | How the method shifts |
|---|---|
| **Poster / print** | The canonical case — distance ladder is literal (10m / 5m / 1m), context is the platform or wall, not the screen. Leverage element must read at several meters before a stride carries the viewer past. Feeling lands before the pedestrian's second glance. |
| **Logo / identity** | "Distance" becomes **scale + repetition**: 16px favicon → app icon → billboard → embroidery. The problem is recognizability + memory hook (GP-10), *not* explanation — a logo that tries to communicate the whole brand fails Step 1. Feeling compresses into shape psychology (GP-09), decided in one glance. |
| **UI / product** | "Distance" becomes **attention state**: glance → task-focus → deep-read, not meters. Context is device + moment (phone at night, brightness down, half-tired). Feeling is usually trust / reassurance for an anxious first-time user. Recognition ladder = above-the-fold → scan → read. |
| **Social / feed** | "Distance" becomes **scroll velocity**. Farthest = the thumbnail flying past in a fast feed; nearest = stopped, reading the caption. Feeling *is* the two-second thumb-stop judgment. Frame the problem for a distracted, un-aligned scroller (GP-02) — pre-convinced viewers are the exception, not the plan. |
| **Packaging** | "Distance" becomes the **retail approach**: shelf-glance across the aisle → hand-pickup → read-the-back. Premium / healthy / cheap is decided at shelf-glance, before pickup. Map the recognition ladder to those three physical moments; the back panel is the 1m payoff, never the leverage point. |
| **Ad creative** | "Distance" becomes **exposure duration**: 3-second skippable pre-roll → 30-second dwell. The Apple frame bites hardest here — understand AND *desire*, fast. Front-load the feeling; the CTA must be recognizable at the *shortest* exposure the placement allows. |

## Output Requirements

The deliverable is one pasteable Comms Brief block — five fields plus a one-paragraph compression:

```markdown
# Comms Brief — [design name]

- **Communication problem**: [the understanding/desire gap this design must close — stated as a PROBLEM, not a task; names what the viewer must understand + the action/feeling they leave with]
- **Target feeling**: [one feeling word] — NOT [explicit opposite it must avoid]
- **Audience**: [specific enough to tune tone] · alignment: [cold / pre-convinced]
- **Viewing context / distance**: [where & how ACTUALLY seen — the real context, not 30cm in Photoshop]
- **Recognition at each distance**: farthest = [the one thing that survives] · middle = [what pulls them closer] · nearest = [the payoff detail]

**One-paragraph compression**: [all five fields woven into a single paragraph every downstream /satori-* decision is checked against]
```

The block must:
1. Have all five fields filled — a blank field is a stop, not a placeholder (you are not ready to design).
2. State the problem as a **gap in understanding or desire**, never as an aesthetic task.
3. Give the target feeling as ONE word **plus its explicit opposite**.
4. Name the **real** viewing context, not the canvas context.
5. Put the leverage candidate (what survives farthest) in the recognition ladder — this becomes GP-06 L downstream.
6. Include the one-paragraph compression, ready to paste into any downstream workflow (`/satori-why-before-what`, `/satori-lift-audit`, `/satori-poster-think`).

## Quality Gate

Guards against these genius.md anti-patterns:

- [ ] **Aesthetic-first decisions (AP-8)** — the problem statement names an understanding/desire gap, not "make it premium." If it names a look, it was demoted to Step 2 and the real gap re-stated.
- [ ] **Loud-by-default (AP-7)** — the target feeling is tuned for an un-aligned viewer (GP-02), not one assumed pre-convinced. Alignment state is recorded.
- [ ] **Decoration without reason (AP-1)** — the brief exists to be the rent ruler; every later element will be checked against it, not against taste.
- [ ] **Transferability ≠ responsive (HK-06)** — the recognition ladder names what survives the *farthest* distance; if nothing does, the concept is flagged scale-dependent and sent back.

**Pass criteria**:
- All five fields present and non-empty.
- Problem framed as a gap, feeling paired with its opposite, context named as the real-world context.
- Recognition ladder names the leverage candidate at the farthest distance.
- One-paragraph compression reads as a single checkable sentence-set, not a list dump.

Fail any box → fix the brief before composition. A design built on a foundation-less brief cannot be rescued by aesthetics; it can only be stylized.

## Related Workflows

**This feeds (downstream)**:
- `/satori-why-before-what` — the comms brief *is* the ruler every rent-test element is measured against
- `/satori-lift-audit` — recognition-at-distance seeds L (Leverage) and T (Transferability) directly
- `/satori-predictive-empathy` — the target feeling is the engineered *next* emotion this workflow deepens
- `/satori-poster-think` — verb + primitive + memory hook all follow from a locked problem + feeling

**Composed by (pipeline)**:
- `/satori-design-think` — this is the atomic intake that pipeline composes first, before any concept move

**Sibling**:
- `/satori-why-before-what` uses GP-08's one-sentence reduction to compress the *concept*; the comms brief sits upstream and compresses the *communication problem* the concept must solve

**Production hand-off** (after the thinking is locked):
- `/satori-poster-think` → `fantastic-posters` (poster / print)
- `/satori-listing-frame` (real-estate listing surfaces)
- `/satori-logo-concept` (identity — where "distance" means scale + repetition)
