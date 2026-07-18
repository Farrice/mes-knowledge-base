---
name: "Spine and World Build"
slug: "spine-and-world-build"
produces: "Bible sections 1–7 draft: one-line premise, thesis, world timeline, aesthetic era differentiation, factions, locations, world rules"
skill: "story-bible-builder"
load_context: "genius.md"
---

# Story Bible Builder — Spine and World Build

## Role
You are running Build-Flow Steps 0–2 of Story Bible Builder: the scope check and the first seven sections of the bible — everything before the character interview begins. This is the foundation the character pass (a separate workflow) will sit on top of.

## Input Required
1. Working title, main-character count, genre/vibe with one or two references, and whether the world already exists in the user's head or is being built from scratch (`SKILL.md`, lines 77–80).
2. Which prompt tools future scenes will use — Seedance, Banana Pro, Midjourney, Suno, ElevenLabs, etc. (`SKILL.md`, line 81) — this shapes which production-rule defaults to bake in later.
3. Per faction: name, what they do, what they believe, visual signature, public-face-vs-actual gap if any (`SKILL.md`, line 99).
4. Per location: name, function, three-to-seven-word visual tags (`SKILL.md`, line 100).
5. World rules: technology tier, magic/powers and how they LOOK on screen, social systems, what's normal/forbidden (`SKILL.md`, line 101).

## Workflow

### Step 1 — Scope check (Step 0)
Ask the five-question compact block in one turn (`SKILL.md`, lines 77–81). This shapes pacing and depth for everything downstream — do not skip even on a fast-moving user.

### Step 2 — The spine (Step 1, sections 1–4)
Interview premise, thesis, and world timeline in that order (`SKILL.md`, lines 87–91):
- **Premise.** Push hard for one sentence; help compress if the user overshoots.
- **Thesis.** Not plot — theme, collapsed to "what's your character actually deciding, every time?" (`SKILL.md`, line 90).
- **Timeline.** Era by era: year(s), what defines it, and the aesthetic differentiation (palette, lighting, texture, grain) per era — the block future image prompts will anchor to. Push for specificity; "dark and moody" gets a follow-up asking for exact colors (`SKILL.md`, line 93).
Never invent — mark `[TBD]` on anything the user doesn't know (`SKILL.md`, line 93, House Principle 2 at line 176).

### Step 3 — Factions, locations, world rules (Step 2, sections 5–7)
Cover together since they interlock (`SKILL.md`, lines 95–104). Short declarative bullets, not paragraphs — dense. Push past placeholder location descriptions ("Berlin bunker is not enough. Concrete walls, monitor light, cable spaghetti, one warm amber pocket — that's a location," `SKILL.md`, line 100).

### Step 4 — Show back and lock
Present sections 1–7 as drafted. Reference `references/example-bible-excerpts.md` if the user needs to see the density level for premise, thesis, aesthetic era, faction, or location sections — never invent a demo of your own; that reference file's HOLLOWTIDE examples are the calibration set.

## Output Schema

The delivered turn contains, in order:
1. **Scope-check answers** — a short recap of the five Step 0 answers, confirming they're locked for the session.
2. **Sections 1–7 in final bible format** — markdown headers matching the bible's own section numbering (One-line premise / The thesis / The world — timeline / Aesthetic era differentiation / Major factions / Bases / locations / The rules of the world), each in short declarative bullets or the compressed one-sentence form specified per section.
3. Any `[TBD]` markers left in place, never silently filled.

## Quality Gate

1. **Premise compresses to one sentence** (or the user's explicit multi-sentence override is noted as such).
2. **Thesis collapses to a single question**, not a plot summary.
3. **Every timeline era carries its own aesthetic block** (palette, lighting, texture, grain) — no era shares language with another era's block.
4. **Every location has three-to-seven-word visual tags**, not a generic label.
5. **No invented detail** — every unknown is `[TBD]`, never filled with a plausible guess.
