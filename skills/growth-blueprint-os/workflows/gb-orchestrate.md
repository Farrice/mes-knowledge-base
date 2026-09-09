---
name: "gb-orchestrate"
description: "Route-by-invoking: reads growth-lab state + manifest, finds the deepest completed step, confirms in one line proving context, and invokes the next workflow. Staleness surfaced at routing time. Never makes the operator re-explain."
expert: "Growth Blueprint OS"
produces: "routing — invokes the right workflow with context loaded"
---

# Growth Blueprint OS — Orchestrate

This workflow writes no strategy itself — it navigates (his orchestrator pattern, adopted) and adds what his couldn't: staleness and drift awareness at routing time (schema'd manifest, ours). It diagnoses where the engagement is and invokes the right specialist with context already loaded.

## The mental model (give it to a new operator in one breath)

A **strategy phase** you run once per engagement (`gb-interview → gb-whitespace → gb-bullseye → gb-topic-scan → gb-format-find → gb-blueprint`), a **maintenance loop** (`gb-refresh` monthly and on any positioning change), and — Wave 2 — a **production loop** per 7-video batch (until it ships natively, the `kallaway-*` roster carries substance: hooks, scripts, retention).

## The map

| Step | Workflow | Produces | Cadence |
|---|---|---|---|
| 1 | `gb-interview` | `positioning-dossier.md` | once · refresh ~90d |
| 2 | `gb-whitespace` | `whitespace-map.md` + wheel | once · refresh ~90d |
| 3 | `gb-bullseye` | `bullseye.md` + 3 viz | once · on positioning change |
| 4 | `gb-topic-scan` | `topic-buckets.md` + `top-50.md` | refresh ~45d |
| 5 | `gb-format-find` | `format-playbook.md` + matrix | once · revisit at hero-format call |
| 6 | `gb-blueprint` | `growth-blueprint.md` + client HTML/PDF | per engagement · reassemble on drift |
| loop | `gb-refresh` | drift report | monthly + on change |

Dependencies that actually matter (enforce these; ignore ceremony): dossier before whitespace; bullseye before the scan's overlay + conversion columns; `top-50.md` before format-find; all five before the blueprint. Everything else flexes around the operator's energy.

## How to route

1. **Read the folder.** `growth-lab/<niche-slug>/` + `manifest.json`. Missing entirely → new engagement: confirm the slug and the mode (self / client / lead-magnet), state the one-breath model, route to `gb-interview`. Partial → find the deepest completed step.
2. **Check state before routing.** Any `stale` / `drifted` artifact on the path (or a STALE/ABSENT pack for a data-heavy next step) → surface in ONE line with the fix ("Pack is 9 days old — scan will date-stamp; `outlier_radar.py refresh` fixes it in minutes. Proceed or refresh first?"). Flag and offer; never block, never silently proceed on rotten inputs either.
3. **Route = invoke.** Don't describe the next workflow — Read its file and run it, with one sentence of handoff context that PROVES the folder was read ("Your bullseye centers filler-fatigued women 45–65 with the revenue overlay on the consult offer — the scan will price the pool against that"). Never make the operator re-explain anything the folder already knows.
4. **Confirm in one line, then go.** "You've got dossier, whitespace, and bullseye — next is the topic scan. Say go." The cost of continuing is one word.
5. **Off-map asks** (thumbnails, paid ads, long-form): answer plainly, then return them to their place in the map. Wave-2 substance asks (hooks, scripts, retention) → offer the `kallaway-*` roster stack as an option, never forced.

## Standing rules for every routed session

- Data tiers are declared out loud before any data-consuming step; the ABSENT tier's zero-fabrication rule travels everywhere.
- Cost transparency: any step that would spend money states the bill first (the radar is $0 — say that too; free is a feature worth naming).
- Plain-English glossing: every term of art defined at first use; the artifacts need no external glossary.
- Voice-first invitation on interview steps; menu-not-verdict on every recommendation.
- Mode is sticky: self / client / lead-magnet was set at engagement start (`manifest.json.engagement.mode`) and shapes every artifact's adaptations row — don't re-ask.

## Output Contract

Routing itself — no artifact. On every route: the one-line state confirmation + the invoked workflow. On request ("where am I / status"), print the map with per-step ✓/○/stale/drifted marks from `manifest.json` and the next action in one line.

## Quality Gate

- The handoff line proves the folder was read (names a real detail from state — never generic).
- No re-asking of anything on disk; no describing-instead-of-invoking.
- Staleness/drift surfaced at most once per routing, in one line, with the fix quoted.
- One question maximum per routing turn; the continue cost is one word.
