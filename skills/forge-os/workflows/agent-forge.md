---
description: "/forge agent <concept or skill> — Agent Forge lane: an existing skill (or a raw concept that resolves to one) → agents/<name>/ deployable agent with a /[name] front-door command."
---

# Agent Forge — Skill → `agents/<name>/` Deployable Agent

Dispatches `skills/forge-os/references/prompts-v2/agent-forge.md` (the engine). Status: **LIVE
(Wave 2)**. Promotion mechanics follow `.agent/workflows/create-agent.md` exactly — this lane adds
no new promotion machinery.

## Invocation

`/forge agent <concept or existing skill name>`. A bare concept with no owning corpus stops at
**SKILL-FIRST** (run Skill Forge first) rather than manufacturing a costume persona.

## Stages

1. **Corpus check** — does an owning skill with real grounding already exist? No →
   verdict SKILL-FIRST, name the prerequisite `/forge skill <concept>` command, stop.
2. **Persona build** — every characterization traces to the skill's own material (genius.md
   sections, verbatim quotes, worked examples) — zero training-memory characterization of "how
   this expert would sound."
3. **Convention files** — `agents/<name>/AGENT.md` + `memory/context.md`, following
   `.agent/workflows/create-agent.md`'s layout exactly; agents live under `agents/`, **never**
   `.claude/agents/` (standing repo rule).
4. **Off-scope refusal block** — AGENT.md carries an explicit block naming what the agent will
   decline and route elsewhere.
5. **Register** — `sync_registries.py` + `generate_slash_commands` produce the `/[name]`
   front-door command.

## Output Schema

The package `agent-forge.md`'s own Output Skeleton names exactly: `agents/<name>/AGENT.md`
(persona from corpus, scope block, context plan, fixtures) + `agents/<name>/memory/context.md`
(scaffold per convention) + a `skills` symlink to `skills/<source>/references/prompts-v2` — plus a
verdict line (`PROMOTED (from <skill>)` or `SKILL-FIRST (→ /forge skill <concept>)`) and a 5-8
line Forge Receipt (corpus verified, convention files followed, which genius.md sections fed the
persona, scope-block summary, fixtures, registration status). `agents/forge-os/AGENT.md` itself
(this skill's own Wave 2 self-promotion) is the working proof this shape ships correctly.

## Quality Gate

- Corpus check ran first; a no-corpus concept is stopped at SKILL-FIRST, never forged anyway.
- Every persona claim is traceable to the skill's material — zero training-memory
  characterization.
- AGENT.md carries an explicit off-scope refusal block.
- `.agent/workflows/create-agent.md` was actually read and its layout followed — agent lands in
  `agents/`, never `.claude/agents/`.
- Both fixtures present, including the off-scope one (an input the agent should correctly refuse).
