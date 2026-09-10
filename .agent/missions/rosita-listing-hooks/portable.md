# JOB PACKET — rosita-listing-hooks · for claude · generated 2026-09-10T11:27:14-07:00 on claude (branch worktree-rosita-listing-video)

## Resume
- `python3 execution/job_board.py resume rosita-listing-hooks` then follow `skills/nate-b-jones-manager-loop/workflows/manager-loop-run.md`
- end the turn only when `python3 execution/job_board.py next rosita-listing-hooks` prints MAY END

## Rules that travel
- Keep every unblocked lane moving; batch questions into DECISION PACKETS; deliver packets + receipts, not status.
- Never publish, send, spend, delete outside the repo, or ship AS Farrice without approval (the card's `Needs approval`).
- Dispatch briefs carry verbatim: "no Chain, no finalize, no Notion, no Next Moves, return only the artifact".

## Lanes now
| id | status | owner | after | expected | evidence | blocker |
|---|---|---|---|---|---|---|
| L1 | complete | claude | — | Intake | _active/clients/jen-listings/19225-rosita-tarzana/ |  |
| L2 | complete | claude | — | Market read | _active/clients/jen-listings/19225-rosita-tarzana/ |  |
| L3 | complete | claude | L1,L2 | Strategy | _active/clients/jen-listings/19225-rosita-tarzana/ |  |
| L4 | complete | claude | L3 | Generate hooks | _active/clients/jen-listings/19225-rosita-tarzana/ |  |
| L5 | complete | claude | L4 | Package | _active/clients/jen-listings/19225-rosita-tarzana/ |  |
| L6 | complete | claude | L5 | Gates | .agent/fair-housing-lint.jsonl |  |
| L7 | complete | claude | L6 | Finalize | .agent/session-state.md |  |
runnable: none · waiting on deps: none · blocked on Farrice: none · done: L1, L2, L3, L4, L5, L6, L7

## Decision packets open
## Packet 1 — L5 · open · 2026-09-10T11:27:05-07:00
Choice: Verdict on hook set v3 — which one goes to Jen, or what changes
Irreversible? no
Options: A send the text as-is, Jen picks / B swap the top pick to #1 (eleven cars, i counted) / C name the miss in your words and I go back to the input, not a fourth take
Recommend: A — #3 is the cleanest voice match per the Jen-as-herself read; #1 is the funnier scroll-stop; both are in the text so her pick decides
If no answer: text stays on disk unsent; nothing goes to Jen

## Decisions answered
none

## Card
---
job: rosita-listing-hooks
recipe: listing-launch-package
opened: 2026-09-10
serves: Jen Santulan
mode: client
---

## The job
Hooks and short intro scripts for 19225 Rosita St, Tarzana ($4,800,000, Marty Azoulay + Shane Zvulun listing, Equity Union) that stop the scroll, sound like Jen, and she would actually film. One text she picks from. Two prior takes rejected (2026-09-10: "terrible… don't catch my attention… don't sound like Jen"), so L4 reruns from the inputs with the named pen, not a third freehand variant.

## Decisions already on disk (no interview needed)
- Register: $4.8M → luxury → Quiet Flex Elite Advisor (her Armida pick), delivered in HER lexicon: calm, gently funny, ellipses, one emoji, invitation close. The Armida winner worked because it carried an image ("a driveway so long the city doesn't even know you're here"), not because it was a thesis.
- She films listings herself: first 15–20s on camera walking toward/through the thing, then b-roll (voice profile). Hooks must be walkable.
- Winners doc: open on a sentence the buyer could hear themselves saying; recognition ("damn, that's me"); specifics are the entertainment; never resolve the whole idea on screen.
- The pen (client CLAUDE.md, Amplify Phase 1): ONE pen = Alyssa Stalker hook-reframe + Luke Iha vicious hooks; ONE check = Jen-as-herself from the voice profile + calibration log. No expert room.
- Facts: `19225-rosita-tarzana/claims-ledger.json` (24 VERIFIED); don't-say list in the shoot sheet stands.
- Fair-housing floor hard; no schools, no who-it's-for.

## Lanes
- L1 Intake — DONE (ledger, photos, contact sheets)
- L2 Market read — DONE (Redfin closed-sale band, LIKELY; no paid research)
- L3 Strategy — DONE (shoot sheet strategy card)
- L4 Generate hooks — RERUN: Luke Iha identity-infiltration map for the $4–5M Valley buyer → 8–10 hooks → Hedge Execution + Germanic swap → Alyssa reframe (her life/feeling first, house second) → Jen-as-herself check → keep 5 [me, write]
- L5 Package — `SEND-TO-JEN-text.md` rewritten in place: 5 options (hook · on-screen · 50–65-word intro · film spot), one top pick, close take, confirms, don't-say [after L4]
- L6 Gates — fair-housing lint, client-package lint, prose classifier on spoken lines [after L5]
- L7 Finalize — chain_runner finalize with --content-file [after L6]

## Comes back when
- His verdict on the set (like / don't like / top changes) → packet 1
- Which hook Jen films → her pick, not ours
- Marty's clearance for Jen to post another agent's listing (T2, stays a packet)

## Needs approval
Sending anything to Jen or her buyers (sends stay human).

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| Jen-as-herself check fails a hook | cut it, don't patch it | never |
| fair-housing exit 2 | rewrite | never |
| third rejection | back to him with the input question, not a fourth take | on rejection 3 |

## Done means
Both lints clean · finalize has no QUALITY GATE BLOCKED · SEND-TO-JEN-text.md is one forwardable text · packet 1 open for his verdict.

