---
name: "Mark Kashef Wargame OS"
description: "Fire when a mission will be executed by a cheaper model/session than the one planning it, when a wrong turn mid-execution is expensive, or when Farrice says wargame/battle plan/pre-fight/judgment banking. Converts frontier-model judgment into a failure-map a cheap executor runs blind."
version: "1.0"
expert: mark-kashef
domain: "wargame, wargaming, battle plan, pre-execution simulation, failure map, plan vs wargame, executor brief, judgment banking, cheaper model execution, RECON NEEDED, abort conditions, expected observation, red-team the plan, blind executor, mission brief, breadth-first drafting, /goal contract, refinement loop, tier degrade, model handoff"
when_to_use:
  - "A deliverable/build will be executed by Sonnet/a cheaper tier and the route needs frontier judgment banked first"
  - "High-stakes mission where improvising mid-run is costlier than simulating first (client work, launches, migrations)"
  - "A plan keeps dying at 80% and the last 20% lands back on the expensive model"
  - "Batch of meaty projects to draft breadth-first before any gets polished"
  - "A handoff document must be executable blind — zero questions from the receiving session"
workflows: 10
routing: core-candidate
---

# Mark Kashef — Wargame OS

Pre-execution adversarial simulation. Not a plan: a plan assumes linearity and a blue-sky scenario; a wargame fights the mission on paper — every move with its expected observation, its likely failure + the cause it signals + the counter-move, every fork with a trigger, RECON NEEDED marks with exact settling checks, abort conditions, and verification runs — written so a cheaper model executes it blind, "without asking a single question."

**The economics**: "You pay for the genius once. You keep it forever." Judgment is expensive to generate, nearly free to replay. This skill is the artifact form of "Fable orchestrates, Sonnet executes" and the mechanism that makes the tier-degrade policy safe.

**Recognition test**: would Kashef see a route fought on paper — or a plan wearing a costume? "Wargamed means it survives contact." If you can't name the attack it survived, it isn't wargamed.

## Workflows

### Tier 1 — Foundation
| Workflow | Produces | Use when |
|---|---|---|
| [wargame-order](workflows/wargame-order.md) | A complete wargame order (WARGAME ORDER preamble + executor mission brief) in a scaffolded mission folder | Front door — any single mission entering the system |
| [wargame-run](workflows/wargame-run.md) | The fought-on-paper wargame file (mission spec → RECON NEEDED → Moves/Expect/Fail/Trigger → aborts → verification) | An order exists; bank the judgment at highest tier/effort |
| [wargame-grade](workflows/wargame-grade.md) | Point-by-point 8-point grade + recorded red-team attack + patch + DONE/NOT-DONE/BLOCKED verdict in the ledger | Every draft, before ANY executor touches it |
| [wargame-execute](workflows/wargame-execute.md) | Execution by a cheaper model following the route blind + expected-vs-observed ledger entry | Wargame is DONE; time to spend cheap tokens |

### Tier 2 — Practitioner
| Workflow | Produces | Use when |
|---|---|---|
| [wargame-batch](workflows/wargame-batch.md) | All missions drafted breadth-first via the /goal contract + /loop refinement to DONE/BLOCKED | A laundry list of missions, not one |
| [wargame-recon](workflows/wargame-recon.md) | Recon dossier — unknown-knowns elicited, unknown-unknowns enumerated, frozen-choice list | Before wargame-order on anything ambiguous ("the wargame drags the other three boxes into the light") |
| [wargame-executor-fit](workflows/wargame-executor-fit.md) | Wargame rewritten in a named executor model's dialect, re-graded | The executor model is known and its behavior differs from the wargamer's |
| [wargame-brief](workflows/wargame-brief.md) | A mission brief passing the executable-blind bar (frozen choices, physical constraints, evidence rules, scope clamp) | The brief itself is the weak link |

### Tier 3 — Stacking
| Workflow | Produces | Use when |
|---|---|---|
| [wargame-mission](workflows/wargame-mission.md) | Optional wargame pre-flight attached to a /swarm or /supercomputer mission | High-stakes multi-agent mission (an OPTION, never a forced pipeline step) |
| [wargame-client](workflows/wargame-client.md) | Client deliverable wargamed once at frontier tier, executed per-instance at cheap tier | Repeatable sold work (Jen listings, Andrea, MyBPM) |

## When NOT to Use

| Situation | Route instead |
|---|---|
| Executing an already-DONE wargame's build steps | The wargame file IS the route — just wargame-execute |
| Agent-team structure, tollbooths, phase-gated builds (execution-time orchestration) | `mark-kashef-agent-orchestration` — wargaming is the layer ABOVE it |
| Critiquing a finished deliverable | `adversarial-review` / adversarial-reviewer agent — wargames stress-test routes, not outputs |
| Trivial/cheap missions where a wrong turn costs less than the simulation | Just execute; wargaming has real token cost at high effort |
| Decision-making between options | `mark-kashef-ai-councils` / `/convene` |

## Stacking Guide

- **× mark-kashef-agent-orchestration** — wargame produces the failure-map; orchestration executes it (fan-out, tollbooths, files-are-truth all reappear downstream)
- **× mark-kashef-ai-councils** — run the red-team pass (8-point standard #7) as an adversarial council on high-stakes wargames
- **× nick-saraev-bottleneck-thinking** — choose WHICH mission earns a wargame: highest time-saved-per-week first
- **× claude-code-guide agent** — executor-fit tailoring via model docs/system cards
- **× luke-iha / copy-engine** — copy-domain mission briefs (task 02 pattern: ICP, state of mind, one CTA)
- **× /swarm, /supercomputer** — optional pre-flight layer (never forced)

## Quick Reference

- **Brain**: [genius.md](genius.md) — load before any workflow
- **Standard**: [references/eight-point-standard.md](references/eight-point-standard.md)
- **Operating prompts (verbatim /goal + /loop)**: [references/goal-and-loop-contracts.md](references/goal-and-loop-contracts.md)
- **Domain briefs**: [references/mission-brief-library.md](references/mission-brief-library.md)
- **Source ledger**: [references/source-quotes.md](references/source-quotes.md)
- **Folder template**: [assets/wargame-folder-template/](assets/wargame-folder-template/)
- **Mission folders land at**: `.agent/missions/<slug>/{tasks,wargames}/` + `SUCCESS.md` + `LEDGER.md`
