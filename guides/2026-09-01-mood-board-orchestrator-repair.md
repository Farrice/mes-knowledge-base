---
date: 2026-09-01
session: mood-board-orchestrator-repair
tier: operator-guide
status: enriched
---

# Mood-Board Orchestrator — What We Built 2026-09-01 and How to Use It

> This session replaced a text-only `/mood-board` brief with a connected visual-board conductor: reference acquisition, three materially different visual territories, actual boards, one comparative proving surface, blind selection, and winner-only downstream handoff. After reconciliation with newer main authority, discovery-backed brand direction is parented by `/andrew-lane-design-systems`, which may compose `/mood-board` for board construction. The acceptance gate is both dedicated verifiers.

## ⚡ If you only read 10 lines

- Start standalone campaign, shoot, event, product, or non-brand board work with `/mood-board`; start discovery-backed brand direction with `/andrew-lane-design-systems`.
- The front door coordinates existing capabilities; it does not introduce a new moodboard expert or duplicate skill.
- A finished run contains three actual visual boards, not three paragraphs of adjectives.
- Each board needs 8–12 references or crops and at least three inspectable references.
- At least four of five creative-direction layers must differ materially between territories.
- All three territories face the same proving surface, so the choice tests direction rather than format.
- Direction labels stay hidden until Farrice makes the blind `Choose / Keep / Kill` decision.
- A text-only moodboard is `PARTIAL`; a described-but-unbuilt proving surface is `UNBUILT`.
- Only the selected winner moves into `DESIGN.md`, art direction, storyboards, or production assets.
- Run `python3 execution/verify_mood_board_orchestrator.py` after any workflow or routing edit.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `/mood-board [visual brief]` | Three reference-locked visual boards, shared proving surface, blind decision, winner handoff | The job is standalone board construction rather than discovery-backed brand direction |
| `/andrew-lane-design-systems [discovery evidence]` | Three client-ready brand directions, proving-surface decision, and ledger | Discovery evidence must become an approved brand direction |
| `python3 execution/verify_mood_board_orchestrator.py` | Positive-route, rejection-control, structure, bridge, and ownership proof | The workflow, command wrapper, creative-direction skill, or routing binding changes |
| `python3 execution/command_menu.py search "turn my discovery notes into three moodboards"` | Ranked command candidates | You suspect natural-language discoverability has drifted |
| `python3 execution/workflow_router.py route "turn my discovery notes into three moodboards"` | Ranked workflow route with binding evidence | You need to prove the live router selects the front door rather than a component |
| `python3 execution/worktree_lane.py merge --lane codex/mood-board-orchestrator-repair` | Guarded integration attempt | Main is reconciled and clean enough to accept the parked repair |
| `/resume mood-board-orchestrator-repair` | The verified handoff and next action | Returning in a fresh session |

## The mental model

### A moodboard is a decision instrument

The old front door described palette, type, imagery, layout, and texture. Those are useful ingredients, but prose alone cannot answer the decision that matters: “Which world should we commit to?” The repaired workflow treats a moodboard as a comparative visual experiment. Three territories are built, each is applied to the same surface, and the operator chooses without being steered by names or rationale.

That changes the quality standard. A board is not complete because its language sounds tasteful. It is complete when its references, composition, layer choices, and applied behavior are inspectable.

### One owner, bounded specialists

`creative-direction` remains the function owner for direct `/mood-board` runs. Reference tools find evidence; Oren contributes taste and reference-edge judgment; the visual executor constructs boards and the proving surface; downstream owners receive only the winner.

Andrew Lane is the parent front door for discovery-backed brand direction and may compose `/mood-board` as a bounded board builder. `/moodboard-sweep` stays separate: it characterizes an existing visual library after production rather than choosing a new direction.

### Route proof needs rejection controls

Natural-language discoverability was the control-plane failure. The integrated repair now uses two narrow bindings: discovery-backed brand direction routes to Andrew Lane; standalone visual-board construction routes to `/mood-board`; negative signals protect adjacent work.

The verifier therefore tests both sides. Eight positive phrases must reach `/mood-board`; four negative controls must not. A broad match on the word “moodboard” would pass the happy path and still break approved-board production, library sweeps, and full Brand Operating System builds.

## `/mood-board` — connected visual-direction front door

### What it is

A seven-phase conductor:

1. Lock intent, audience, constraints, evidence state, and proving surface.
2. Acquire and ledger references without silently treating inspiration as owned material.
3. Form three territory hypotheses with different strategic tensions and primary references.
4. Construct three actual visual boards across palette, typography, imagery, layout, and material or texture.
5. Apply each territory to the same representative proving surface.
6. Hide direction names and collect a blind `Choose / Keep / Kill` decision.
7. Lock the winner and hand only that direction to the appropriate production owner.

### When to reach for it

- Discovery or a brand brief exists, but visual direction is not chosen.
- A client needs choices that are genuinely different rather than three shades of the same premium aesthetic.
- The team is about to build identity, web, campaign, packaging, or content assets and needs one visual world first.
- Approval drift is likely because references and applied behavior have not been compared on equal terms.

### When not to

- You already have an approved board and need production assets: use the matching downstream production workflow.
- You need tokens from an approved direction: use `/design-md-synthesize`.
- You need to characterize a mature moodboard library: use `/moodboard-sweep`.
- You need the full Brand Operating System: use `/build-bos`; moodboards are one bounded component of that larger job.
- You have no discovery, audience, or objective and are only collecting loose inspiration: start with reference research, then return when the decision can be named.

### How to invoke

```text
/mood-board Turn these discovery notes into three unmistakably different visual directions for the brand. Use real references, build actual boards, apply all three to the same proving surface, and stop for my blind Choose / Keep / Kill decision.
```

The front door should continue safely when enough context is available. It should ask only for private facts, a felt-standard decision, or a real constraint that cannot be recovered from the workspace.

### Worked example from the repair

Before the patch, “turn my discovery notes into a high-taste moodboard” ranked generic brief commands above the existing moodboard owner. After the patch, eight ordinary phrasings route to `/mood-board`, including discovery notes, three visual territories, reference-locked boards, and a campaign moodboard. The rejection set confirms that an existing library sweep, an approved-board `DESIGN.md` handoff, approved-board campaign production, and a full BOS request remain with their native owners.

No new moodboard was generated during the repair. The example proves orchestration and discoverability, not taste quality.

### Honest edges

- Human blind acceptance is `UNTESTED` on the repaired front door.
- Revision-count reduction and client approval drift are `UNTESTED` until the same project is compared before and after.
- Reference acquisition still depends on available user assets, approved browsing, or installed research tools.
- A verifier cannot determine whether the three boards are beautiful, culturally alive, or personally right for Farrice. It only prevents known structural and routing regressions.
- The branch is committed as `5c277462d` but parked because main contains unrelated tracked changes. It is ready, not integrated.

## Composition options

| Capability | Role beside `/mood-board` | Use it when | Boundary |
|---|---|---|---|
| Refero or approved web/reference sources | Acquire concrete visual evidence | The brief lacks strong references | Research is not a delivered direction |
| Oren taste development | Sharpen reference edge and blind judgment | Territories feel generic or collapse toward one aesthetic | Oren advises taste; `creative-direction` conducts |
| Andrew Lane brand direction | Own discovery evidence, three client directions, the proving decision, and durable rules | Brand discovery must become a client-approved direction | May compose `/mood-board`; remains parent owner |
| `/design-md-synthesize` | Convert the winner into design tokens | The direction is approved | Do not synthesize all three territories |
| `/moodboard-sweep` | Characterize an existing board library | Production history exists | Not a discovery-to-direction workflow |
| `/build-bos` | Build the full Brand Operating System | Moodboards are one part of a broader engagement | Do not route every BOS request through `/mood-board` |

## The first real proof run

Use the current highest-value brand project. Preserve its discovery evidence, run all three territories against one representative surface, and record:

- whether the three boards are distinguishable with labels hidden;
- which direction Farrice chooses, keeps, and kills;
- what specific references or layer decisions caused the verdict;
- how many revision rounds occur before direction approval;
- whether downstream assets remain coherent without blending rejected territories.

The workflow earns promotion only if the real run produces a stronger foundation than the prior process. If it does not, use `/repeatability-spine`: preserve the best board, identify the primary failure class, repair the smallest owner or handoff, and replay the same proving surface.

## Retrieval and integration

Resume with `/resume mood-board-orchestrator-repair`. The exact handoff is `.agent/handoffs/2026-09-01-mood-board-orchestrator-repair.md`. Once main is clean, integrate through the lane manager rather than a manual or forced merge:

```bash
python3 execution/worktree_lane.py merge --lane codex/mood-board-orchestrator-repair
```

The branch, cold-start proof, verifier, workflow, and solution card are the durable record. Do not rebuild the system from chat history.
