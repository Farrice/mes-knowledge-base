# The Harness, In One Page

*For Farrice — what a /command actually is, what agents are, and which layer to
reach for. Written 2026-07-08 after "I still don't really have clarity on what our
/commands are."*

## The five layers

| Layer | What it physically is | What it's FOR | Example |
|---|---|---|---|
| **Slash command** | Just a trigger phrase | Pointing at one of the layers below | `/jam`, `/go` |
| **Workflow** (`.agent/workflows/*.md`) | A recipe Claude reads and follows in-conversation | Repeatable *procedure* — steps, gates, order | `/go`, `/jam`, `/autopilot` |
| **Skill** (`skills/*/SKILL.md`) | Knowledge + voice + sub-workflows of one expert | *Thinking* — how Lara writes hooks, how Miller cuts cognitive load | `/ghostwrite`, `/copy-engine` |
| **Agent** | A separate worker with its own fresh context | Grunt work in parallel, isolated from your session's context | builders, reviewers, scouts |
| **Hook** | Deterministic code that fires on events, no model judgment involved | Things that must NEVER depend on attention or memory | cost gate, placement advisory, steering loop |

Plus the **Workflow engine** (capital-W): a deterministic script that fans out
many agents with gates between phases — the "fleets" that built the Cooz package.
It's what you invoke when the job is bigger than one context window can hold.

## The mental model

- A **/command is a doorbell**. What answers the door is either a recipe
  (workflow) or an expert (skill).
- **Skills know things, workflows do things.** `/jam` is a workflow (a protocol
  for how we work together). `/nicolas-cole-*` is a skill (a way of thinking).
- **Agents are hired hands, not features.** Any workflow can hire them. More
  agents ≠ better — they're for parallel grunt work and independent judgment
  (reviewers who haven't seen my reasoning are honest reviewers).
- **Hooks are the guardrails bolted to the building.** Everything else persuades;
  hooks enforce.

## Which layer, when (the leverage rule)

- Judgment, taste, synthesis, talking to you → **main thread** (me, directly).
- Repeatable procedure you'll want again → **workflow**.
- A named person's expertise, reusable across projects → **skill**.
- 10+ files to read, N parallel builds, independent verification → **agents /
  Workflow engine**.
- "This must happen every time, even on a bad day" → **hook**.

Highest-leverage orchestration = the top of this list delegating downward:
you talk to me, I run judgment in-thread, procedures come from workflows, experts
get loaded as skills, fleets do volume, hooks catch everything that falls.

## Where /jam sits

A workflow — it choreographs how WE collaborate (takes → gut verdicts → taste
ledger). It hires no agents mid-session by design; it's the layer where the
human's taste is the scarce input and everything else stays out of the way.
