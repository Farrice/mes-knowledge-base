# Farrice Application Map Architecture

> **Expert**: Seth Godin | **Skill**: seth-godin-marketing-mind | **Tier**: Application
> **Produces**: Farrice Application Map
> **Slash Command**: `/gmind-farrice-map`

---

## Purpose

The rest of this skill trains the lens. This workflow points it at Farrice's actual surfaces and produces something he can do before the week ends — not a strategy memo, a move. Godin's own granularity standard for what counts as an application, not an insight: *"go find two or three people and support them. And that's how it begins."* Small enough to start today, specific enough that "did I do it" has a yes-or-no answer. This is a runtime workflow — the executor generates the map live, per session, rather than reading a fixed answer off the page.

---

## Inputs Required

1. **The Godin Principle(s) In Play** — from any gmind workflow just run, or pulled fresh from the extraction's 12 patterns (`extractions/seth-godin-marketing-mind/extraction-report.md`).
2. **Which Surfaces Are Live This Week** — not all four surfaces need a move every session; name which ones are actually in motion.
3. **Current State Per Surface** — one line each on where Authority Flywheel, Parallax, LinkedIn, and active client work stand right now.

---

## Workflow

### Step 1: Load Grounding Context

Before generating any move, load `FARRICE-MASTER-CONTEXT.md` (repo root) plus whatever project-specific CLAUDE.md applies to the client surface in play (`_active/clients/andrea-dj/CLAUDE.md`, `_active/clients/jen-listings/CLAUDE.md`). A move built without this context is generic advice wearing a Godin label — the whole point of this layer is that it isn't that.

### Step 2: Name the Principle Doing the Work

Pull the specific pattern from the extraction, not a paraphrase of "be more Godin." Exclusion-clause positioning, the sufficiency number, tension-vs-familiarity, the hire-yourself audit, decision-vs-outcome — name which one applies to which surface, and why that one and not another.

### Step 3: Produce One Move-This-Week Per Active Surface

For each of Farrice's active surfaces, generate exactly one move, applying the mechanics Godin actually names — exclusion, sufficiency, or tension — not a generic content suggestion:

- **Authority Flywheel / S&C coaching niche (Invisible Expert ICP)** — apply exclusion-clause positioning the way the curly-hair hairdresser does it: *"If you're bald, don't come. If you're a guy, don't come."* Write the don't-come list for the Invisible Expert tier specifically, not a demographic filter.
- **Parallax Substack** — apply tension-vs-familiarity in place of a consistency plan: *"You tell a story. This story creates tension... but then what you want is for people to relieve the tension by buying from you."* Name the specific tension one edition should create, not "post more."
- **LinkedIn launch** — apply the sufficiency number instead of a growth target: *"What's the smallest viable audience? How many people would be enough?"* Name a number Farrice would actually recognize as enough for this stage, not a vanity follower goal.
- **Client work (Jen Santulan real estate, Andrea/Resonance, MyBPM)** — apply the two-question reset per client: who's it for, what's it for, specifically enough to exclude someone. If a client surface has no live decision this week, skip it rather than inventing one.

### Step 4: Size the Move to This Week

Every move must be small enough to start today and finish this week — the "two or three people" standard, not a quarter-long initiative. If a move can't be described in one sentence a person could act on in the next few days, it's still a strategy, not a move. Cut it down until it is.

### Step 5: Flag Standing-Decision Contradictions

Before finalizing any move, check it against Farrice's locked decisions rather than silently proposing something that conflicts:

- **Path A / Incumbency Rule** — claim-safe content for funded health/performance brands; no repositioning until $5K/mo collected. A move that repositions before that threshold gets flagged, not executed silently.
- **DWA Threads Engine frame lock** — the anti-guru wedge is locked; do not re-pivot it. A move that drifts the frame gets flagged, not executed silently.

Flag means naming the tension in one line and letting Farrice decide — never suppressing the move, never overriding the lock unilaterally.

### Step 6: Attach the Sufficiency Measure

Each move closes with how success gets read — never a vanity number. Replace views, followers, or downloads with Godin's own replacement metric: *"It's who did I help today?"* State what "who did I help" looks like concretely for that specific move.

---

## Output Schema

```
FARRICE APPLICATION MAP
=========================

| Surface | Principle Applied | This-Week Move | Sufficiency Measure |
|---------|-------------------|-----------------|----------------------|
| Authority Flywheel / S&C (Invisible Expert) | [exclusion-clause / etc.] | [one sentence, actionable today] | [who did I help — not vanity metric] |
| Parallax Substack | [tension-vs-familiarity / etc.] | [one sentence] | [who did I help] |
| LinkedIn launch | [sufficiency number / etc.] | [one sentence] | [who did I help] |
| Client work — [Jen / Andrea / MyBPM, named] | [two-question reset / etc.] | [one sentence] | [who did I help] |

STANDING-DECISION FLAGS: [none, or named tension + one-line tradeoff — decision left to Farrice]
```

---

Execution prompt: `references/prompts-v2/farrice-application-map.md` — honor its Output Contract.

## Quality Gate

| Dimension | Minimum Standard |
|-----------|-----------------|
| Grounded in Context | FARRICE-MASTER-CONTEXT.md and relevant project CLAUDE.md loaded before any move is generated |
| Mechanically Godin | Each move names exclusion, sufficiency, or tension explicitly — not generic strategy advice with a name attached |
| This-Week Sized | Every move is a single sentence a person could start today and finish within the week |
| Contradiction Flagged, Not Suppressed | Any move touching Path A or the DWA frame lock is surfaced as a flag, never silently executed |
| No Vanity Sufficiency | Every measure answers "who did I help," never views/followers/downloads |

---

## Cross-Expert Stacking

| Stack With | Compound Effect |
|-----------|----------------|
| `/godin-lens` | Application map is the natural landing point after a live lens session on any of Farrice's own questions |
| `/cos` | This-week moves feed directly into the Chief of Staff daily brief and weekly board as tracked commitments |
| `/gmind-two-questions` | Client-work rows can be expanded into full Positioning Cards when a client decision needs more than one sentence |
| `/authority-flywheel` | Authority Flywheel row hands off to the dedicated workflow once the exclusion-clause move needs full positioning work |
