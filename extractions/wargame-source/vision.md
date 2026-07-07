# Extraction Vision — Mark Kashef: Wargame OS

**Date**: 2026-07-07 · **Mode**: /extract-forge (expansion of existing expert `mark-kashef`) · **Creative latitude**: 3 (Autonomous, per forge default — Farrice directed: orchestrator mode, full system integration)

## Source Inventory

| Source | Size | Role |
|---|---|---|
| YouTube nuwlyQXrADg (13:58) | 2,946-word transcript + 45 frames | Conceptual layer: plan-vs-wargame, action/reaction/counteraction, knowns/unknowns elicitation |
| `fable-wargame-kit/README.md` | 2KB | System framing: "bank its judgment... pay for the genius once, keep it forever" |
| `The Laundry List.pdf` | 28 pages | Visual guide, 10 optimized wargame orders |
| `fable-last-week/tasks/01-10` | 10 mission files | The operational template: WARGAME ORDER header + mission brief, per domain |
| `SUCCESS.md` | 8-point standard | The quality gate — what "properly wargamed" means |
| `LEDGER.md` + `wargames/README.txt` | — | Self-grading + blocked-inputs discipline |

**Gate-first check (When NOT to Use)**: transcript alone is 2,946 words (< 5,000 threshold), but the combined kit is a complete operational system — 10 structured prompts, an 8-point rubric, a folder contract, and a refinement loop. Combined source clears forge richness on methodology density, not raw word count. Proceeding at forge tier; noting the word-count caveat honestly.

## The Core Concept (one sentence)

**A wargame is not a plan: a plan assumes linearity and a blue-sky scenario; a wargame simulates the executor's route move by move — expected observation, likely failure + cause + counter-move, forks with triggers, RECON NEEDED flags, abort conditions, and verification runs — written so a cheaper model can execute it blind without asking a single question.**

The economics: pay for frontier-model judgment ONCE as an artifact, execute forever with cheap models. "You pay for the genius once. You keep it forever."

## Uniqueness Audit

What no one else in the roster does:
- **mark-kashef-agent-orchestration** covers agent teams, phase-gated builds, replicate-anything transfer — but everything there is *execution-time* structure. Nothing simulates failure *before* execution.
- **superpowers:writing-plans** produces plans — exactly the artifact Kashef argues is insufficient (linear, blue-sky).
- **adversarial-review / adversarial-reviewer** stress-tests *finished deliverables*. Wargaming stress-tests *the route before anyone walks it*.
- **The Chain Step 5.5** verifies facts post-production. Wargame is pre-hoc failure simulation — a missing tier: plan → **WARGAME** → execute → verify.

Net-new capability: **pre-execution adversarial simulation + judgment banking**.

## Business Leverage Map

| Application | Leverage |
|---|---|
| Client missions (Jen listing engine, Andrea POC, MyBPM launch) | Wargame once at frontier tier → repeat execution at Sonnet cost. Directly serves the Path A "$5K collected" constraint: cheaper delivery of already-sold work. |
| Opus Fallback Policy (memory: never pin Opus, degrade a tier) | Wargaming is the *mechanism that makes degrading safe* — the tier-degrade policy currently has no artifact to catch the intelligence gap. |
| /swarm + /supercomputer + Workflow engine | Wargame layer slots as an optional pre-flight before mission execution (per no-forced-wiring: an option, never a pipeline step). |
| Handoff/resume system | A wargame IS a superior handoff artifact — executable blind is exactly the handoff bar. |

## Cross-Expert Stacking

- × **mark-kashef-ai-councils** — red-team pass (SUCCESS point 7) run as an adversarial council.
- × **nick-saraev-bottleneck-thinking** — pick WHICH mission earns a wargame (highest time-saved-per-week first, per task 10).
- × **nate-b-jones-trust-architecture / agent-deployment-strategy** — executor-fit tailoring via model docs/system cards.
- × **luke-iha / copy-engine** — mission briefs for copy domains already encode ICP/state-of-mind/CTA discipline (task 02 is a compressed copy brief).

## Gap Fill

Adds the missing middle tier of the execution stack. Also imports 3 transferable sub-patterns usable outside wargaming: (1) expected-observation discipline ("exactly what you should see if it worked"), (2) evidence-or-it-doesn't-exist rule ("if you cannot quote it, it does not exist" — tasks 06/07/09), (3) blocked-inputs ledger (placeholders surfaced, never silently assumed).

## Decision

- **Skill**: `skills/mark-kashef-wargame-os/` — new sibling skill under the existing mark-kashef expert (expansion, not new agent).
- **Depth**: Mastery — 10 workflows in 3 tiers, prefix `/wargame-*`.
- **Naming**: domain term is "wargame" (his language, kept verbatim per their-thinking-not-their-terminology... his terminology IS the framework name).
