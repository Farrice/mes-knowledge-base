---
date: 2026-07-13
session: wargame-os (Kashef extraction, shipped 2026-07-07)
tier: operator-guide
status: enriched
---

# Wargame OS — What We Built 2026-07-07 and How to Use It

> The Mark Kashef forge extraction (video nuwlyQXrADg + his fable-wargame-kit) produced `skills/mark-kashef-wargame-os/` — 10 `/wargame-*` workflows that convert frontier-model judgment into a **failure-map a cheap executor runs blind**. Companions: the 8-point standard at `skills/mark-kashef-wargame-os/references/eight-point-standard.md`, verbatim /goal + /loop operating prompts at `references/goal-and-loop-contracts.md`, extraction artifacts at `extractions/wargame-source/` (do not re-extract).

## ⚡ If you only read 10 lines

- Front door: `/wargame-order <mission>` — scaffolds `.agent/missions/<slug>/{tasks,wargames}/` + `SUCCESS.md` + `LEDGER.md`.
- The loop is always order → `/wargame-run` (bank judgment at highest tier) → `/wargame-grade` → `/wargame-execute` (cheap model, blind).
- A wargame is not a plan: every Move carries Expect / most-likely Fail + the cause it signals / Counter; every fork has an observable Trigger.
- Unsettled assumptions get `RECON NEEDED` with an **exact runnable check** — a command, a URL, a file — never "verify this."
- DONE = all 8 points of the standard hold **AND one honest attempt to break it failed**. No executor touches an ungraded wargame.
- The economics: "You pay for the genius once. You keep it forever." This is the artifact form of Fable-orchestrates-Sonnet-executes and what makes tier-degrade safe.
- Laundry list of missions → `/wargame-batch` (breadth-first /goal contract, then /loop refinement to DONE/BLOCKED).
- Repeatable sold work (Jen listings, Andrea, MyBPM) → `/wargame-client`: wargame once at frontier tier, execute per-instance cheap.
- Don't wargame trivial missions — if a wrong turn costs less than the simulation, just execute.
- Landmine: never ask a reasoning model to expose its thinking in output (can silently reroute the session) — request artifacts, findings, quotes, rewrites.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/wargame-order` | Complete wargame order (preamble + executor mission brief) in a scaffolded mission folder | Front door — any single mission entering the system |
| `/wargame-run` | The fought-on-paper wargame file (spec → RECON NEEDED → Moves/Expect/Fail/Trigger → aborts → verification) | An order exists; bank the judgment at highest tier/effort |
| `/wargame-grade` | Point-by-point 8-point grade + recorded red-team attack + patch + DONE/NOT-DONE/BLOCKED in the ledger | Every draft, before ANY executor touches it |
| `/wargame-execute` | Cheap-model blind execution + expected-vs-observed ledger entry | Wargame is DONE; time to spend cheap tokens |
| `/wargame-batch` | All missions drafted breadth-first via /goal, refined via /loop to DONE/BLOCKED | A laundry list of missions, not one |
| `/wargame-recon` | Recon dossier — unknown-knowns elicited, unknown-unknowns enumerated, frozen-choice list | Before an order on anything ambiguous |
| `/wargame-executor-fit` | Wargame rewritten in a named executor model's dialect, re-graded | The executor model is known and behaves differently |
| `/wargame-brief` | Mission brief passing the executable-blind bar (frozen choices, physical constraints, evidence rules, scope clamp) | The brief itself is the weak link |
| `/wargame-mission` | Optional wargame pre-flight on a /swarm or /supercomputer mission | High-stakes multi-agent work — an OPTION, never forced |
| `/wargame-client` | Client deliverable wargamed once, executed per-instance cheap | Repeatable sold work |

Each `/wargame-*` command loads `skills/mark-kashef-wargame-os/genius.md` first, then executes the matching file in `skills/mark-kashef-wargame-os/workflows/`.

## The mental model

1. **Plans assume blue sky; wargames fight the mission on paper.** A plan lists steps. A wargame states, per move, what you should observe if it worked, what most likely breaks, what that break tells you about the world, and the counter-move — so failure mid-run is a routed branch, not an improvisation.
2. **Judgment is expensive to generate, nearly free to replay.** The frontier model's job is not execution — it's banking every decision into the document so nothing lands back on the expensive tier at 80% complete. If an executor would have to *decide* rather than *observe*, the judgment isn't banked yet.
3. **Wargaming is the layer ABOVE orchestration.** It produces the failure-map; `mark-kashef-agent-orchestration` (fan-out, tollbooths, files-are-truth) executes it. Critiquing a *finished output* is a different job — that's `adversarial-review`. Choosing *between options* is `/convene`.
4. **The recognition test:** "Wargamed means it survives contact." If you can't name the attack it survived (point 7 requires the attack + patch recorded IN the document), it's a plan wearing a costume.

## The single-mission loop (order → run → grade → execute)

**What it is.** Four workflows that take one mission from raw intent to cheap blind execution. `/wargame-order` writes the order and executor brief into a fresh mission folder. `/wargame-run` fights it on paper — the judgment-banking step, run at the highest tier and effort you have. `/wargame-grade` scores it against all 8 points and red-teams it; the grade is point-by-point in the ledger, never one blended score, and "do not soften the grading to finish faster." `/wargame-execute` hands the DONE route to a cheaper model with an expected-vs-observed ledger.

**When to reach for it.** A cheaper model/session will execute what a smarter one should route; a wrong turn mid-run is expensive (client work, launches, migrations); a handoff must be executable with zero questions from the receiving session; a plan keeps dying at 80% with the last 20% landing back on the expensive model.

**When NOT to.** Trivial/cheap missions (wargaming has real token cost at high effort — just execute). Executing an already-DONE wargame's steps (the file IS the route). Agent-team structure and phase gates → `mark-kashef-agent-orchestration`.

**How to invoke.** `/wargame-order <the mission>`, then follow the loop. References load on demand: `eight-point-standard.md`, `goal-and-loop-contracts.md`, `mission-brief-library.md`. Ambiguous mission? `/wargame-recon` first — "the wargame drags the other three boxes into the light."

**Honest edges.** Skill is B-tier; A-tier waits on Farrice's blind-pass judgment (EVAL-033). As of 2026-07-13 no mission folder under `.agent/missions/` has been through the full order→run→grade→execute loop — the standard and contracts are verbatim from Kashef's kit, but the live-fire proof is still owed.

## `/wargame-batch` — the laundry list

**What it is.** Breadth-first drafting of many missions under the verbatim **/goal contract** ("Every mission file in ./tasks has a first-draft wargame in ./wargames, logged in LEDGER.md with a self-grade against SUCCESS.md… Draft all ten before polishing any"), then the **/loop refinement prompt** ("Loop through every first draft… until all eight points of SUCCESS.md hold, no exceptions"), taking the weakest draft first each cycle. Stop when every wargame is DONE or BLOCKED, or two consecutive cycles improve nothing.

**When / when not.** A batch of meaty projects to draft before any gets polished. One mission → just the single loop. Which mission even deserves a wargame → stack with `nick-saraev-bottleneck-thinking` (highest time-saved-per-week first).

## `/wargame-client` — sold work, wargamed once

**What it is.** A client deliverable class (a Jen listing sheet, an Andrea event asset) wargamed once at frontier tier; every subsequent instance executes at cheap tier along the banked route. This is where the "pay once, keep forever" economics turn into margin on real revenue.

**When / when not.** Repeatable sold work with a stable shape. One-off client deliverables → normal Chain + `adversarial-reviewer`, no wargame needed.

## Composition (options, never pipeline steps)

| Stack | What it buys | Earns its cost when |
|---|---|---|
| × `mark-kashef-agent-orchestration` | Wargame = failure-map, orchestration executes it | Multi-agent execution of a DONE wargame |
| × `mark-kashef-ai-councils` | Red-team pass (point 7) run as an adversarial council | High-stakes wargames |
| × `/swarm`, `/supercomputer` | `/wargame-mission` pre-flight | High-stakes multi-agent missions — optional |
| × `claude-code-guide` agent | Executor-fit tailoring from model docs | `/wargame-executor-fit` on a named model |
| × `luke-iha` / `copy-engine` | Copy-domain mission briefs (ICP, state of mind, one CTA) | The mission is copy |
