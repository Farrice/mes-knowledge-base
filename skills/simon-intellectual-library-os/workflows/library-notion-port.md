---
description: "Port any knowledge system (extractions, logs, file KBs) into a glanceable Notion Intellectual Library — hub + 5 databases + advisors — via Notion AI deployment prompts or direct API build."
---

# Library Notion Port

Turn messy/append-only knowledge into Simon's glanceable Notion architecture: hub dashboard, atomized entry DB with views, expert/source registries, grounded advisor pages, session memory.

## Pre-Flight Gate
- Load `genius.md` §Two Substrates + `references/notion-port-blueprint.md` (the canonical target architecture).
- Inventory what's being ported: which extractions/logs/KBs, roughly how many entry candidates, which categories they'll need.
- Choose build path: **(A) Notion AI builds it** from a deployment prompt pack (default — exercises the system natively, gets views/dashboards right) or **(B) direct API** via `execution/notion_api.py` (pinned 2022-06-28; never the JS client) when Notion AI is unavailable.

## Skill Acquisition
Read `genius.md` + `references/notion-port-blueprint.md` + `references/kb-schema.md`.

## Execution
1. **Tune the blueprint**: adapt the 5-DB architecture's Category lanes, Type options, and Confidence definitions to the user's actual corpus (don't ship someone else's lanes).
2. **Produce the deployment prompt pack** (path A) — sequenced prompts, each self-contained, written meta-agent style (plan-lock built in, AskUserQuestion-friendly):
   - **Prompt 1 — Build the system**: hub + 5 DBs + properties + views + dashboard + global instructions page. Instructs the AI to propose a plan and confirm before building.
   - **Prompt 2 — Create a grounded advisor**: instruction page with mandatory entry gate, filtered linked view, boundaries, registration in global instructions, then the empty-view refusal test.
   - **Prompt 3 — Ingestion run**: chapter-map-first → Extract → Atomize → Normalize into DB1.
   - **Prompt 4 — Monthly health check**: the 7-stage audit as a reusable skill page.
   Each prompt ends with verification steps the user can eyeball.
3. **Or execute path B**: create DBs/properties via API; views and dashboards need manual/AI finish — say so honestly.
4. **Seed strategically**: bridge 2-3 highest-value knowledge sets first (via `/library-extraction-bridge`) so the glance test is meaningful on day 1 — never launch an empty library.
5. **Run the acceptance tests** (or hand them to the user as a checklist): glance test (<30s state read), filter test (advisor cites entries by lane), refusal test (empty filtered view → honest refusal).

## Content Type Adaptations
| Source system | Adaptation |
|---|---|
| Antigravity extractions | Genius patterns/hidden knowledge → DB1 entries; roster → DB2; per blueprint mapping table |
| Notion prose logs | Health-check-style pass: mine reusable lessons → entries; leave operational noise behind |
| File KB (raw/wiki/outputs) | wiki articles → DB1 entries; outputs → session memory or entries; raw stays local |
| Client knowledge | Add a who-we-are context page; advisors load it with the KB |

## Output Requirements
The tuned blueprint + the 4-prompt deployment pack (copy-paste ready, sequenced, each with verification steps) + seeding plan + acceptance checklist. If path B: built DBs + honest list of what still needs Notion AI/manual finish.

## Quality Gate
`genius.md` §Rubric Glanceability — ≥8 = hub dashboard specified AND the glance test is passable on day-1 seed data. §Anti-Patterns: porting the mess (wholesale copy without atomization) = fail; empty launch = bookmark graveyard in new clothes.
