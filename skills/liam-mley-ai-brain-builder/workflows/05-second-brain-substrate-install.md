---
description: "The client second-brain install — bridge Business DNA (liam-mley discovery) into a live self-improving substrate (Simon's raw/wiki + ingest), wired to Kieran Flanagan's 5 building blocks and his writing-logic routing recipe. Turns the AIOS Context Layer concept into a sellable, buildable deliverable."
---

# Workflow 05 — Second-Brain Substrate Install

> **Produces**: A deployed, self-improving second-brain substrate for a business — vault + AI-reader + raw/wiki folders + tuned writing logic + connectors/habit — bridging the Context Layer (Workflow 02) into a compounding asset.
> **Load first**: [genius.md](../genius.md) + `skills/simon-intellectual-library-os/genius.md`
> **Prerequisite**: Business DNA from Workflow 01 (Discovery); Context Layer from Workflow 02 if it exists.

## Role
You are Liam Mley installing the substrate that makes the Context Layer *compound*. Workflow 02 builds a rich static BRAIN.md; this makes it a living system that ingests, enriches, and gets smarter with use. The methodology is Kieran Flanagan's 5 building blocks, wired onto Simon's raw/wiki substrate, with the writing logic tuned to this specific business's DNA.

> Kieran: "the second brain can be customized to how you work... it's a very personal operating model." The generic install ships the 5 default signals; the bespoke value is tuning the writing logic to how THIS business runs — which is exactly what the 8-dimension Business DNA already surfaced.

## Pre-Flight Gate
- Run the **Decision Framework** in `genius.md` § Decision Framework — confirm the Business DNA / discovery profile exists (Workflow 01). No DNA = stop; you'd tune the writing logic on guesses.
- Load Simon's substrate model (`simon-intellectual-library-os/genius.md` §Two Substrates + §Lifecycle) — this workflow does NOT reinvent raw/wiki; it wires DNA into it.
- Sequencing: personal/founder brain first, then team/company via `/library-brain-ladder`. Do not architect a company brain before the founder's loop is proven.

## Skill Acquisition
Read this skill's `genius.md` + `simon-intellectual-library-os` genius.md and `workflows/library-second-brain.md`. The install is: DNA → derive writing logic → stand up Simon substrate → wire connectors + habit.

## Execution
**Kieran's 5 building blocks are the install checklist** (verbatim structure):

1. **Vault** — "a folder of plain text files... it can be any folder on your desktop with Markdown files in it, and that's where your knowledge lives and that's what the AI system is writing to." Create the business vault (or reuse the Context Layer folder from Workflow 02).
2. **An AI that can read the vault** — "I use Claude Code. You can use Codex. You can use Claude desktop with MCP connections." Tooling note (demo, frame t=10:01): the prototype runs on a **Claude project surface** — "Create a new project → Use an existing folder: give Claude a folder you already work from." Pick the surface the client already works in.
3. **Two basic folders** — "one where you can store things, and then one where you can write that intelligence... into your wiki folder." = Simon's `raw/` + `wiki/`. Add `outputs/` for the compounding loop.
4. **The writing logic (the routing recipe — THE customization surface)** — "What do you want the AI to look for in all those files?" **Ship these 5 default signals, then tune each to the Business DNA:**
   > Verbatim recipe: "Hey, look for blockers. Look for updated experiments. Look for decisions that were made. Look for places where people seem to be struggling to hit their goals. Look for places where people seem to have real clear articulation on the opportunities that they believe can help accelerate the business."
   - **Blockers** → typed folder `<project>/blockers/*.md`, metadata: owner · age · severity · next-action.
   - **Updated experiments** → `<project>/experiments/*.md`: status · result · what-it-updates.
   - **Decisions made** (+ reasoning — the Dalio move) → `<project>/decisions/*.md`: decision · reasoning · dependants · date.
   - **Goal-struggle / risk signals** → where people are missing goals.
   - **Opportunity articulations** → "opportunities they believe can help accelerate the business."
   Also derive the stakeholder + cross-team dependency graph per project ("who are the stakeholders... the cross-team dependencies... what documents are applicable to this update... Build you a little knowledge graph"). Tune the signals + weights to the DNA (a sales-led business weights blockers/decisions; a content business weights experiments/opportunities).
5. **Connectors + the habit** — "then it can connect to your Slack... Google Docs... auto ingest those things and wick them into your vault." Wire the connectors the DNA named, and install the ingest habit: "you need to get into the habit of continually updating it cuz it gets better the more that you use it." Ship a scheduled or ritualized ingest trigger — the habit is the retention mechanism, not optional.

**Then**: run `/library-second-brain` to stand up the loops on the wired vault, and `/library-ingest-triage` for the confidence-gated review lane so writes are adjudicated, not blind.

## Content Type Adaptations
| Business type | Writing-logic tuning |
|---|---|
| Agency / services | Weight blockers + decisions + client-project stakeholder graphs; connectors = Slack + project docs |
| SaaS / product | Weight experiments + opportunity articulations + goal-gap; connectors = analytics + CRM + docs |
| Content / media | Weight experiments + opportunities; light on blockers; connectors = Docs + performance data |
| Solo founder | Personal brain only; defer team/company tiers to `/library-brain-ladder` as a dormant spec |

## Output Requirements
Deliver: the deployed vault (paths) + `raw/`/`wiki/`/`outputs/` + the **tuned writing-logic file** (the 5 signals customized to this business, with typed target folders + metadata contracts) + stakeholder/dependency graph per tracked project + connector list wired + the ingest habit trigger (scheduled or ritual) + one demonstrated ingest→triage→wiki round-trip. Set the honest day-1/day-100 expectation (Kieran: "the more I use the system, the more knowledge it's acquiring").

Execution prompt: references/prompts-v2/second-brain-substrate-install.md — honor its Output Contract.

## Quality Gate
- Is the writing logic TUNED to the Business DNA (not the 5 generic defaults shipped raw)?
- Are decisions + blockers first-class TYPED folders with their metadata contracts (owner/age/severity/next), not free text?
- Is the ingest HABIT installed (scheduled/ritual trigger) — the compounding won't start without it?
- Was one full ingest→triage→wiki round-trip demonstrated live, landing in `outputs/`?
- Does it stack onto Simon's substrate rather than reinventing raw/wiki? Anti-Pattern check (`genius.md` § Anti-Patterns + Simon's §Anti-Patterns: bookmark graveyard, human-as-librarian).

> **🛡️ Anti-Pattern Check**: review output against **Anti-Patterns** in both `genius.md` files. Flag and fix violations. A static Context Layer that never ingests is the exact "storage, not a brain" failure Kieran rejects.

## Stacking
Bridges `liam-mley` Workflow 01/02 (Business DNA + Context Layer) → `simon-intellectual-library-os` (`/library-second-brain`, `/library-ingest-triage`, `/library-compound-loop`). Team/company tiers → `/library-brain-ladder`. Pre-sale diagnostic on a prospect's existing setup → `/library-retrieval-audit`.
