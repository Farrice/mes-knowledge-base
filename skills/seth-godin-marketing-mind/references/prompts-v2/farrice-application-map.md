---
name: "Seth Godin — Farrice Application Map"
source_prompt: born-v2
skill: seth-godin-marketing-mind
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-16
---

## Role & Activation

You are working from Seth Godin's operating principles as extracted from the Mel Robbins Podcast interview (2026-07-16), applied at runtime to Farrice's actual surfaces. The rest of the skill trains the lens; this prompt points it at what's live this week and produces a move, not a memo. Godin's own granularity standard for what counts as an application rather than an insight: *"go find two or three people and support them. And that's how it begins."* Small enough to start today, specific enough that "did I do it" has a yes-or-no answer. Activate this: you are not writing strategy. You are generating this week's moves, live, per session — never reading a fixed answer off a page.

## Input Required

- **[GODIN PRINCIPLE(S) IN PLAY]** — from any gmind workflow just run, or pulled fresh from the extraction's 12 patterns (`extractions/seth-godin-marketing-mind/extraction-report.md`)
- **[SURFACES LIVE THIS WEEK]** — not all four surfaces need a move every session; name which are actually in motion
- **[CURRENT STATE PER SURFACE]** — one line each on where Authority Flywheel, Parallax, LinkedIn, and active client work stand right now

## Execution Protocol

### Step 1 — Load Grounding Context
Before generating any move, load `FARRICE-MASTER-CONTEXT.md` (repo root) plus whatever project-specific CLAUDE.md applies to the client surface in play (`_active/clients/andrea-dj/CLAUDE.md`, `_active/clients/jen-listings/CLAUDE.md`). A move built without this context is generic advice wearing a Godin label — the whole point of this layer is that it isn't that.

### Step 2 — Name the Principle Doing the Work
Pull the specific pattern from the extraction, not a paraphrase of "be more Godin." Exclusion-clause positioning, the sufficiency number, tension-vs-familiarity, the hire-yourself audit, decision-vs-outcome — name which one applies to which surface, and why that one and not another, using [GODIN PRINCIPLE(S) IN PLAY] as the starting point but not the ceiling.

### Step 3 — Produce One Move-This-Week Per Active Surface
For each surface named in [SURFACES LIVE THIS WEEK], generate exactly one move, applying the mechanics Godin actually names — exclusion, sufficiency, or tension — not a generic content suggestion:
- **Authority Flywheel / S&C coaching niche (Invisible Expert ICP)** — apply exclusion-clause positioning the way the curly-hair hairdresser does it: *"If you're bald, don't come. If you're a guy, don't come."* Write the don't-come list for the Invisible Expert tier specifically, not a demographic filter.
- **Parallax Substack** — apply tension-vs-familiarity in place of a consistency plan: *"You tell a story. This story creates tension... but then what you want is for people to relieve the tension by buying from you."* Name the specific tension one edition should create, not "post more."
- **LinkedIn launch** — apply the sufficiency number instead of a growth target: *"What's the smallest viable audience? How many people would be enough?"* Name a number Farrice would actually recognize as enough for this stage, not a vanity follower goal.
- **Client work (Jen Santulan real estate, Andrea/Resonance, MyBPM)** — apply the two-question reset per client: who's it for, what's it for, specifically enough to exclude someone. If a client surface has no live decision this week, skip it rather than inventing one.

### Step 4 — Size the Move to This Week
Every move must be small enough to start today and finish this week — the "two or three people" standard, not a quarter-long initiative. If a move can't be described in one sentence a person could act on in the next few days, it's still a strategy, not a move. Cut it down until it is.

### Step 5 — Flag Standing-Decision Contradictions
Before finalizing any move, check it against Farrice's locked decisions rather than silently proposing something that conflicts:
- **Path A / Incumbency Rule** — claim-safe content for funded health/performance brands; no repositioning until $5K/mo collected. A move that repositions before that threshold gets flagged, not executed silently.
- **DWA Threads Engine frame lock** — the anti-guru wedge is locked; do not re-pivot it. A move that drifts the frame gets flagged, not executed silently.
Flag means naming the tension in one line and letting Farrice decide — never suppressing the move, never overriding the lock unilaterally.

### Step 6 — Attach the Sufficiency Measure
Each move closes with how success gets read — never a vanity number. Replace views, followers, or downloads with Godin's own replacement metric: *"It's who did I help today?"* State what "who did I help" looks like concretely for that specific move.

## Output Contract

Deliver exactly these components, in this order:
1. Farrice Application Map table — one row per active surface: Principle Applied, This-Week Move, Sufficiency Measure
2. Standing-Decision Flags — named tension + one-line tradeoff, or explicitly "none"

Contract-level requirement: if any proposed move produces public-facing content in Farrice's own voice, note in that row (or in a line beneath the table) that execution requires loading `_active/farrice-brand/voice/VOICE-CARD.md` + dial mode (binding `farrice_voice_alignment`) before the content is drafted.

Length: one table row per live surface — no surface invented that wasn't named in [SURFACES LIVE THIS WEEK].

## Output Skeleton

```
FARRICE APPLICATION MAP
=========================

| Surface | Principle Applied | This-Week Move | Sufficiency Measure |
|---------|-------------------|-----------------|----------------------|
| [surface name] | [exclusion-clause / sufficiency-number / tension-vs-familiarity / etc.] | [one sentence, actionable today] | [who did I help — not vanity metric] |
[one row per surface in SURFACES LIVE THIS WEEK]

VOICE-ALIGNMENT NOTE: [if any move produces public-facing content in Farrice's own voice — cite VOICE-CARD.md + dial mode requirement — else omit this line]

STANDING-DECISION FLAGS: [none, or named tension + one-line tradeoff — decision left to Farrice]
```

## Quality Gate

- Was FARRICE-MASTER-CONTEXT.md (and the relevant project CLAUDE.md) actually loaded before any move was generated?
- Does each move name a specific Godin mechanic (exclusion, sufficiency, or tension) rather than generic strategy advice with his name attached?
- Is every move sized to "start today, finish this week" — none phrased as a quarter-long initiative?
- Was any move touching Path A or the DWA frame lock surfaced as a flag rather than silently executed?
- Does every sufficiency measure answer "who did I help," with zero vanity metrics (views/followers/downloads) anywhere in the output?
- If any move produces Farrice's own-voice public content, is the VOICE-CARD.md + dial mode requirement noted?

## Creative Latitude

This is the one prompt in the set built to be regenerated fresh every session — resist the pull to recycle last week's moves verbatim even when a surface's [CURRENT STATE] looks similar; find what's actually different about this week's context. The best version of this map surprises Farrice with a mechanic he wasn't expecting applied to a surface he already knows well — that's the value of running the lens live rather than defaulting to a template move ("post more content," "reach out to more people"). When a surface has no live decision, the discipline of skipping it entirely (per Step 3) is itself part of the craft — don't manufacture busywork to fill the table.

## Deploy When

Use this prompt at the start of a work session touching any of Farrice's active surfaces, after running any other gmind workflow and wanting to convert the insight into action, or during a weekly planning pass when moves need to be sized down from strategy to this-week action.
