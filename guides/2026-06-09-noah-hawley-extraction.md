---
date: 2026-06-09
session: noah-hawley extract-forge + deep integration
tier: operator-guide
status: enriched
---

# Noah Hawley Extraction — What We Built 2026-06-09 and How to Use It

> The extract-forge session on Hawley's *How I Write* interview (~16,000 words) produced `skills/noah-hawley-storytelling-mastery/` — 20 workflows, 16 genius patterns, agent at `agents/noah-hawley/` — plus deep integration: 6 craft rules pinned to sovereign memory, `/convene` roster entry, DOMAIN_REGISTRY Domain 7, and a screenwriting ground-truth benchmark. Full workflow table: the skill's `SKILL.md`. Transcript + extraction record: `extractions/noah-hawley/`.

## ⚡ If you only read 10 lines

- Hawley is the **architecture layer** — he runs FIRST; Roth (scene), Connelly (detail), Wright Thompson (profile), Pressfield (physics), Segura (comedy) run *inside* his frame. Inverting the order = crafted scenes, no spine.
- Four root commitments: start with a **question** (the work is the answer) · the **ending** gives the story its meaning · **theme is the compass** (plot is downstream) · **tone is the real structure**.
- Breaking any story or content arc → `/hawley-theme-engine`. Starting any narrative → `/hawley-ending-first`.
- Piece "doesn't feel right" and you can't name why → `/hawley-room-debug`.
- Substack/newsletter run as a season → `/hawley-content-season` (built for Parallax).
- LinkedIn/X post that must grip cold → `/hawley-short-form-tension` (tension→release + moral mirror).
- Many makers or agents must sound like one voice → `/hawley-voice-bible`.
- Load `genius.md` before any workflow; run its Decision Framework (the question, the ending, the taken-for-granted assumption) as the pre-flight gate.
- 20 structure-pure v2 prompts live in `references/prompts-v2/` — when a deliverable matches one, honor its Output Contract instead of improvising.
- The 7.25 finalize composite was a conservative no-ground-truth cap, not a quality miss — don't re-finalize chasing a number; add benchmark samples.

## Command table (the load-bearing ten — all 20 in SKILL.md)

| Command | Produces | Reach for it when |
|---|---|---|
| `/hawley-theme-engine` | Question + theme spine + theme-broken beat map | Breaking any story/arc; planning collapses into plot-listing |
| `/hawley-ending-first` | A locked ending arced backward | Starting a narrative; a piece drifts with no destination |
| `/hawley-tonal-arc` | Season/piece-level tonal architecture | A multi-part arc must modulate comedy ↔ dread ↔ resolution |
| `/hawley-comedy-horror` | One tension→release unit on the comic↔dread dial | Any scene, hook, or beat that must grip |
| `/hawley-room-debug` | Diagnosis of "doesn't feel right" + the fix | Something is off and you can't name it |
| `/hawley-coherence-cut` | A pass that brooms service creep | Work bloated by elements serving assets, not the story |
| `/hawley-voice-bible` | Voice codification teaching generative logic | Many makers/AI agents must sound like one voice |
| `/hawley-content-season` | Theme spine + ending + edition-as-episode map | Planning a newsletter run as a show (Parallax) |
| `/hawley-short-form-tension` | High-tension short-form post | A LinkedIn/X post for cold readers |
| `/hawley-cross-genre` | Hawley-led stack with the scene-level roster | A piece needs architecture AND scene craft |

## The mental model

1. **He adapts feelings, not text.** Hawley built one of TV's most original reputations almost entirely on other people's IP by reconstructing the *feelings* a source produced and inducing them through a different story. That's the whole skill in one move — and it's why `/hawley-adapt-mode` works on any remix, format port, or "make this ours" job.
2. **Theme is a question you can't answer yet.** *Fargo* is "how can decency win?", never "decency matters." If you already know the answer, you have a lesson, not a story — and a lesson won't pull the work. Every beat is an angle on the question, not a domino.
3. **Architecture before craft, always.** Hawley decides why the season exists; the roster writes the scenes. This ordering is the stacking doctrine and the reason he earned a slot above an already-deep storytelling cluster.

## Capability 1 — The foundation engine (theme → ending → tone)

**What it is.** Five Tier-1 workflows that do the story-breaking a showrunner does before anyone writes a line: extract the question under the brief, state the theme *as* that question, lock the ending that gives the work meaning, design the tonal arc, and build individual tension→release units.

**When to reach for it.** Any story, content arc, campaign, or edition where you feel yourself listing "what happens" instead of knowing why it exists. `/hawley-theme-engine`'s anti-theme cut is the sleeper: it holds your beloved twist against the theme-question and kills it if it betrays the answer.

**When NOT to.** Single flat posts with a known point — `/ghostwrite` or the copy roster is cheaper. Refinement of an existing draft → `writers-room`.

**How to invoke.** `/hawley-theme-engine` with the raw brief, format, locked beats, and the twist you're in love with. The workflow pressure-tests three candidate seeds ("do I already know the answer?") before it lets you build.

**Honest edges.** The theme must stay *invisible to the audience* — if a character could say it aloud, the workflow makes you rewrite. That gate feels slow the first time; it's the point.

## Capability 2 — The diagnostic tier (debug, cut, withhold)

**What it is.** `/hawley-room-debug` (why a piece feels wrong), `/hawley-coherence-cut` (remove elements serving assets rather than story), `/hawley-imagination` (a withhold pass — what to underwrite and leave unseen), `/hawley-take-for-granted` (convert one accepted assumption into a wedge).

**When to reach for it.** Post-draft, pre-ship, when quality-gate scores stall below 7 and you can't locate the weakness. `/hawley-take-for-granted` doubles as a positioning tool when anything feels generic.

**When NOT to.** Mechanical prose problems (slop phrases, AI tells) → `prose_classifier.py` / prose-doctor first; Hawley diagnoses structure, not sentences.

## Capability 3 — Cross-domain deployment (the reason it was extracted)

**What it is.** Five Tier-3 workflows translating showrunning into your actual channels: `/hawley-content-season`, `/hawley-campaign-coherence` (one voice across many deliverables), `/hawley-short-form-tension`, `/hawley-velocity-draft` (his dual-media cadence applied to your output speed), `/hawley-cross-genre` (the conductor that seats Roth/Connelly/Wright/Pressfield/Segura inside his frame).

**When to reach for it.** Parallax season planning is the named deploy target for `/hawley-content-season`. Multi-deliverable brand or campaign work that risks sounding like five different writers → `/hawley-campaign-coherence` or `/hawley-voice-bible`.

**When NOT to.** A campaign that needs *selling* more than coherence → Ben Watkins (`/bw-story-selling-system`) owns the commercial layer; Hawley owns the architectural one.

**Worked example (from integration).** Six craft rules from this extraction are pinned to sovereign memory and fire automatically at Tier 1.5 on storytelling tasks: break-by-theme, ending-first, moral-mirror, coherence-over-continuity, imagination-over-explanation, take-for-granted/adapt-feelings. You get the doctrine even when you don't load the skill.

## Composition (options, never pipeline steps)

| Stack | When it earns its cost |
|---|---|
| Hawley → Eric Roth | Season spine set, then scene/edition-level visual prose |
| Hawley → Wright Thompson | Long-form narrative needing reporting depth inside a theme spine |
| Hawley → Connelly/Segura | Short-form needing telling detail + comic timing in a tension shape |
| Hawley → Ben Watkins | Architecture done, now sell it (pitch room / hooks) |

## Honest edges (system-wide)

- **Finalize composite was 7.25** — the taste-signature conservative cap for a no-ground-truth-yet expert; spot-checks were gold-standard and anti-slop 2/10. The screenwriting benchmark sample (sample-005) is what lets future scoring calibrate higher.
- **Architecture-first is a discipline, not a preference** — running scene experts before Hawley silently produces spineless work that still *looks* finished. The tell: every section is good and the whole is inert.
- The skill grades structure and tone; it will not catch factual errors or voice drift — Chain Step 5.5 and the voice layer still run.
