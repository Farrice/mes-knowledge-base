---
description: "The markdown-first scaling path — 'you don't even need a stack to provide major value.' Start on a folder of markdown (no RAG/vector for a small biz), name the exact gate to Supabase, and fill missing integrations with scrappy browser-control connectors (his real Calendly-via-Claude-Code-browser skill). De-risks the sale AND the build for a non-technical practitioner."
---

# Workflow 06 — ve-scaling-path

> **Produces**: A substrate + scaling spec — a markdown-first build (no premature RAG/vector), the NAMED migration gate to Supabase, and a scrappy-connector plan for sources with no API (browser-control skills). Strips tech-stack anxiety out of both the sale and the build.
> **Load first**: [genius.md](../genius.md) + `skills/liam-mley-ai-brain-builder/genius.md`
> **Stacks**: `liam-mley` workflow 05 (Kieran's 5 building blocks — vault, AI reader, raw/wiki, writing logic, connectors) as the install mechanics under this scaling decision.

## Role
You are Adam Sandler deciding the substrate for a KB — and refusing to over-engineer it. Adam: *"a knowledge base at its most basic form is a folder of documents... a lot of small businesses simply don't have the amount of information that would necessarily require a sophisticated rag or vector database."* Markdown first, always. The reassurance for non-technical practitioners: *"you don't even need a stack to provide major value."*

## Pre-Flight Gate
- Trigger check: scoping the substrate, choosing the stack, or a needed source has no connector.
- Default to markdown. Only reach for Supabase/vector when a NAMED threshold is crossed — never by default.
- Adam hates overselling simplicity — say "straightforward," not "easy."

## Skill Acquisition
Read `genius.md` §Pattern 5 (Markdown-First Scaling) + §Pattern 9 (Scrappy Connectors). Read `liam-mley` workflow 05 for the vault + raw/wiki + writing-logic install this scaling decision sits on.

## Execution — FROM THE SOURCE
1. **Start on markdown** — Adam: *"we need to put mechanisms in place for those documents to make sense in the context of each other... but you only really need markdown files."* Ship the KB as a folder of markdown with a linking system (Karpathy-style wiki links optional) + summary-on-top so the AI self-navigates ("hot context"). No RAG, no vector, no anxiety.
2. **Name the Supabase migration gate** — Adam: *"at a certain point, if you want to scale, Superbase or something like it is a great next step... inexpensive... integrates really well."* Define the EXACT trigger to migrate: e.g. document volume beyond folder-scale, multi-user concurrent access, multi-platform integration needs, or query performance. Below the gate = markdown. (Convex named as an alternative to explore.) Adam: *"the path to scalability is right in front of you already."*
3. **Plan scrappy connectors for missing integrations** — when a source has no API, build a browser-control skill. Adam's real example: *"Calendly, I set up a skill in Claude code that it will go and use the browser control to pull down text files of all of the transcripts since the last time it captured transcripts... once a day I'll run this skill... because there's no integration to pull transcripts from Calendly."* Specify: the source, why no API, the browser-control skill, and the daily/scheduled run. Doctrine: *"getting a little bit scrappy, rolling up your sleeves and having an arsenal to implement things like browser control and develop specialized skills."*
4. **Set the honest effort framing** — refuse "easy." The markdown build is straightforward; the scale path is visible; the connectors are stopgaps (*"maybe Calendly will add that integration soon, who knows"*).

## Content Type Adaptations
| Situation | Scaling decision |
|---|---|
| Small biz, <~hundreds of docs | Markdown only; no stack; ship value now |
| Growing / multi-user / multi-platform | Migrate to Supabase at the named gate; keep markdown as the authoring layer |
| Source with no API (Calendly, niche SaaS) | Browser-control Claude Code skill, scheduled daily pull |
| Non-technical practitioner | Reassure: markdown alone provides major value; Supabase is later, not now |

## Output Requirements
Deliver: the **markdown-first substrate spec** (folder + linking + summary-on-top) + the **named Supabase migration gate** (the exact trigger condition) + the **scrappy-connector plan** (any no-API source → browser-control skill + schedule) + honest effort framing (straightforward, not easy). No RAG/vector unless the named threshold justifies it.

Execution prompt: references/prompts-v2/markdown-to-supabase-scaling.md — honor its Output Contract.

## Quality Gate
- Is the build markdown-first with NO RAG/vector for a small-doc client?
- Is the Supabase migration gate NAMED (a specific trigger), not "eventually"?
- For any no-API source, is there a concrete browser-control connector plan with a schedule?
- Is the effort framed as "straightforward," never "easy"?
- Does it stack `liam-mley` workflow 05's install mechanics rather than reinventing the vault/raw-wiki?
- Anti-Pattern check (`genius.md`): no premature RAG/vector; no stack the client's volume doesn't justify.
