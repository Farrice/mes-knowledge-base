---
job: offer-copy-with-floor-gate
name: Offer or sales page copy through the copy floor gate
family: revenue-launch
tier_default: T2
runs: 0
last_ratchet: never
---

## The job
Cold prompt to publishable offer or sales copy — market grounded once, drafted through the copy stack, cleared through the publishable-copy gate — nothing sent or published without him.

## Sub-jobs / lanes
- L1 Intent — product, market, objective, asset type, awareness guess [parallel]
- L2 Ground — `execution/avatar_manifold_runner.py ground`; WARM reuse or a cost-previewed cold start [after: L1]
- L3 Assemble — copy stack draft via `.agent/workflows/copy-engine.md` [after: L2]
- L4 Owner wrap — high-stakes wrap when client, founder, or public facing [after: L3]
- L5 Gate — `.agent/workflows/publishable-copy-gate.md` checklist, claim-safety pass, `execution/prose_classifier.py check` [after: L4]
- L6 Finalize — `execution/chain_runner.py finalize` [after: L5]

## Ask me first
- Q: Cold market or warm cache — approve the cost-gated cold start? · look first: `.tmp/copy-engine/` cached slugs
- Q: Which asset type and objective? · look first: the ask itself, the client or brand's own CLAUDE.md for register

## Handles alone
Intent parse, grounding cache check, assembly, owner wrap, gate checklist, prose lint, finalize.

## Comes back when
- A cold start would spend money (cost gate — approve only via `cost_gate.py approve`)
- Two rejected renditions of the copy → back to the brief, no third take
- Claim-heavy copy needing his sign-off on a specific number

## Needs approval
The cold-start spend · sending or publishing the copy anywhere.

## Needs
`.agent/workflows/copy-engine.md` · `.agent/workflows/publishable-copy-gate.md` · `execution/avatar_manifold_runner.py` · `execution/prose_classifier.py` · `directives/ai-slop-ban-bank.md`.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| cache miss on a market he thought was warm | run `estimate` first, present the cost before spending | any cost above $0 |
| gate flags an AI tell (generic thesis, "not X it's Y") | rewrite once from the gate checklist | second miss |
| a claim cannot be sourced | soften, label, or remove it | it is a client or public-facing claim |

## Done means
Gate checklist all clean · `execution/prose_classifier.py check` clean · finalize carries no QUALITY GATE BLOCKED · nothing sent or published.

## Ratchet log
- none yet
