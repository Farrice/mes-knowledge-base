---
description: The Forge front door — raw intent → production-grade prompt / workflow / skill / agent / plugin via one classifying door, five lanes, and the shared forge spine
---

# /forge — Raw Intent → Production-Grade Artifact

`/forge <raw intent>` is the cornerstone generation door. It takes a bare concept — no source
transcript, no existing prompt required — and produces a production-grade artifact through the
Forge OS spine. Skill: `skills/forge-os/SKILL.md` (load it first; its prompts-v2 menu carries the
execution layer).

## Invocation

```text
/forge <messy concept>                  → front door classifies lane + routes
/forge prompt <concept>                 → Prompt Forge lane directly
/forge workflow|skill|agent <concept>   → named lane (Wave 2: routes to interim door)
/forge dialect <model>                  → P1–P8 probe battery → directives/model-dialects/ card
                                          (engine: references/prompts-v2/dialect-probe.md)
```

## Stage 0 — Front Door (always)

Run `references/prompts-v2/intent-translation-card.md`: Translation Card (felt standard verbatim,
sharpened line for routing) → classify HAS-axis (bare concept / source / prompt / extraction /
exemplar / skill) and WANTS-axis (prompt / workflow / skill / agent / plugin) → route.

**Artifact-in-hand always outranks a Forge lane** (never rebuild the crown jewels):

| Operator has | Route |
|---|---|
| Source material (video/transcript/article/course) | `/extract-forge` or `/source-to-skill-system` |
| Battle-tested existing prompt | `/convert-prompt` |
| Finished MES extraction | `/convert-extraction` |
| Perfected, approved exemplar + iteration log | `/design-skill-enshrine` |
| Existing skill wanting an agent | `/create-agent` |
| Bare concept only | Forge lane (below) |

## Lanes

- **Prompt Forge (LIVE)** — run `references/prompts-v2/prompt-forge.md`. Spine: translate →
  ground (prompt_library search + skill match + Recall; no corpus → receipts-backed grounding
  sprint or `fidelity: low`) → forge 8 sections per `directives/prompt-forging-spec.md` → audit →
  fixtures → place in owning skill's prompts-v2 → wiring trio.
- **Workflow Forge (Wave 2)** — interim: `/create-skill` Step 1 → Workflow Command branch, with
  the forge spine (F1 grounding + F5 cold-start proof + F7 fixtures) as the contract.
- **Skill Forge (Stage 1 LIVE)** — bare concept → run `references/prompts-v2/grounding-sprint.md`:
  negative check (owning skill exists? route to it) → multi-modal source hunt → receipts-backed
  corpus at `extractions/grounding/` → readiness verdict (FORGE-READY / THIN / NO-BUILD /
  ROUTE-EXISTING) → existing `/extract-forge` pipeline runs on the corpus. New stage, existing
  machinery.
- **Agent Forge (Wave 2)** — skill exists → `/create-agent`; no skill → Skill Forge first, then
  promote. From-scratch personas without corpus are prohibited (provenance guard).
- **Plugin Forge (DEFERRED)** — packaging stays deferred per standing decision. Lift requires
  Farrice's explicit approval + cold-start proof pass. Until then: report the boundary, build
  nothing.

## Gates (every lane)

`renaissance_audit.py` 0-fail → `prompt_library.py build` → `wire_prompt_pointers.py --write` →
live cold-start proof (fresh context, real fixture) before registration → blind-pass vs the best
in-library artifact of the same class for any top-1% claim → register (SLASH_COMMANDS.md, cards).
Existence ≠ done; audit-pass + proof = done.

## Evolution & Portability (inherited spines)

Every forged artifact ships born-instrumented (2–3 golden fixtures + failure-log pointer → the
existing `/skill-anneal` / `/self-evolve` / daily `evolution_orchestrator.py` loop). Model quirks
live only in `directives/model-dialects/` cards; artifacts stay contract-based and model-agnostic.
Harness-specific wiring stays in the thin outer layer `execution/platform_compiler.py` manages —
the methodology core ports anywhere.

## Boundaries

Local + reversible by default; no global writes, no plugin marketplace edits, no external
publishing. The Forge serves the whole system — it is never bounded by a single revenue goal
(compass, never cage). Chain still runs: forged deliverables finalize per CLAUDE.md Step 6.
