---
description: "/meg-trigger-audit — score any design/product/concept on the 10-criterion Heckman rubric, isolate the weakest trigger, and return kill/revise/lead verdicts with a concrete revision directive per concept. 'Nice doesn't open the wallet.'"
---

# Trigger Audit

A hand-drawn woodblock with mountains, an eagle, a van, a waterfall — the better piece of art, the one that wins the design competition — sold zero in four months. A hiker with bold text sold 3,714 (her claim). The difference was never craft. This workflow judges work the way she judges it: not "is it pretty?" but "what does this let the buyer say about themselves, and how fast?" Every concept leaves with a verdict and the single revision that would move it — because a scorecard without a directive is just a prettier way to stall.

## Pre-Flight
Read these files before executing:
1. `skills/meg-heckman-buyer-trigger-os/genius.md` (the Six Triggers, Rubric, Anti-Patterns)
2. `skills/meg-heckman-buyer-trigger-os/references/genius-patterns.md` (Patterns 1–10)

> **🔒 Pre-Flight Gate**: Run the **Decision Framework** in `genius.md` — for EACH concept under audit, you must be able to attempt all seven questions. If the concept's target buyer is unknown, stop and get it (or run `/meg-sub-identity-map` first). Auditing against "everyone" is auditing nothing.

## Input Required
- The concepts: design files, mockups, text descriptions, or product listings (1–12 per audit)
- The intended buyer per concept (best available description — the audit will sharpen it to a behavioral moment)
- Where it sells: marketplace, own store, drop, in-person (affects Wearability + Social Currency read)
- Anything already known about performance (sales, CPC, comments) — optional but sharpens verdicts

---

## Workflow

### Step 1: Mirror-or-Poster Gate (before any scoring)
Classify each concept first — her reflexive opening move. A **poster** describes a category ("loves the outdoors," "EDM fan," "dog mom"). A **mirror** reflects a specific person's lived behavior ("the one at the back of the group who needs a water break every 10 minutes").

| Concept | What it says about the wearer (one sentence, first person) | Mirror or Poster? |
|---|---|---|
| (concept 1) | "I ___" | |

Posters do not proceed to scoring with a passing grade ceiling above REVISE — a poster can only be revised toward a mirror or killed. Note WHO the mirror reflects as a behavioral moment, not a demographic.

### Step 2: The 50ms Pass
For each survivor: count focal elements and run the 5-word test. "One thing loudly rather than three things quietly." If you cannot describe the design in 5 words, the buyer's brain meets chaos in the first 50 milliseconds and the rest of the rubric never gets a chance to matter.

### Step 3: Score the 10-Criterion Rubric
Score 1–5 per criterion (anchors in `genius.md § Quality Rubric`): **Identity Signal · Recognition Speed · Specificity · Social Currency · Familiar/Twist · Emotion First · Wearability · IP Safety · 50ms Clarity · Evergreen Index.**

Scoring discipline:
- Score from the BUYER's seat, cold, scrolling — not from the brief's intentions.
- Social Currency is scored on the involuntary forward: would someone send this to a SPECIFIC person within 10 seconds? Name that person ("the friend who always...").
- Familiar/Twist: name both halves explicitly. Missing half = max 2.
- A concept that produces "that's nice" at any point is an automatic FAIL regardless of arithmetic — flag it.

### Step 4: Verdicts + Revision Directives
Apply her decision rules: **avg <3 = KILL · 3–4 = REVISE · ≥4 with no criterion <3 = LEAD** (gets spend/production).

For every REVISE: identify the **weakest trigger** and write ONE concrete revision directive that attacks it — a new lead line, a sharpened twist, a narrowed person, a decluttered layout. Pattern her real moves: "Add bridge copy: 'Social floor is production. Test the chaos in rehearsal'" — the directive is copy/design-ready, not advice.

For every LEAD: write the recognition lead line it should ship with (the "For the dancer who stops overthinking and sends the count" move).

### Step 5: Portfolio Read (if 3+ concepts)
- Which ONE leads the test and why (strongest involuntary-forward moment wins ties, not highest average).
- Evergreen mix: flag if the set leans trend-dependent ("trend-based designs spike and die").
- Collection cohesion: do any concepts naturally pair for multi-item orders? (Feeds `/meg-aov-architect`.)

## Content Type Adaptations
| Format | Adaptation |
|--------|-----------|
| Apparel / POD design | Full rubric as-is; Wearability = worn in public, wants to be noticed |
| Physical product (mug, sticker, print) | Wearability → Display-ability: visible in the buyer's space to OTHER people |
| Offer / landing page | Wearability → Shareability of the claim; 50ms = above-the-fold single message; run via `/meg-trigger-transfer` for full treatment |
| Content hook / thumbnail | Social Currency = tag/DM impulse; Evergreen Index still applies — personality beats trend |
| Logo / brand mark | Score the NAME + mark as identity statement (Sloth Hiking Club IS the joke); Specificity = sub-identity it claims |

## Output Format
```
TRIGGER AUDIT — [brand/project] — [date]

GATE RESULTS: [n] mirrors / [n] posters (posters capped at REVISE)

SCORECARD
| Concept | IdS | RcS | Spc | SoC | F/T | EmF | Wear | IP | 50ms | Ever | Avg | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

PER-CONCEPT:
• [name] — [MIRROR/POSTER] — [verdict]
  Weakest trigger: ___ 
  Revision directive: "___" (copy/design-ready)
  Lead line (if LEAD): "___"
  Future social moment: [who reacts, how]

PORTFOLIO READ: lead candidate ___ · evergreen mix [ok/lean-trend] · natural pairs: ___
NEXT: [/meg-concept-sprint to replace kills | /meg-design-handoff for leads | /meg-listing-copy]
```

## Quality Gate
> **🛡️ Anti-Pattern Check**: review against `genius.md § Anti-Patterns` before delivering.
- No concept was judged on prettiness; every verdict traces to a trigger, not taste.
- Every buyer is named as a behavioral moment, not a demographic (HK-2).
- Every REVISE carries ONE concrete, executable directive — no "make it more emotional" slop.
- Social Currency scores name the specific person who gets the forward (HK-3).
- "That's nice" reactions were flagged as automatic fails — "Nice doesn't open the wallet."
- Her numbers, if cited, carry UNCONFIRMED labels.

## Common Pitfalls
- **Scoring the brief instead of the artifact.** The concept's intention doesn't scroll a feed; its surface does. Recovery: re-score cold, as a stranger.
- **Average-worship.** A 4.2 with a dead Social Currency beats nothing — the forward impulse IS the scale mechanism. Recovery: tie-break by involuntary forward, always.
- **Directive inflation.** Three suggestions per concept = zero decisions. Recovery: one weakest trigger, one directive.
- **Auditing posters politely.** A poster with great craft is still a greeting card. Recovery: gate first, score second.
