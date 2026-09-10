---
job: research-brief-paid-demand
name: Research brief with paid-demand evidence
family: harvest-research
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
A receipt-carrying research brief that answers one question with paid-demand evidence (who pays, how much, where), every claim labeled, rendered in the Briefing Room, $0 unless he approves a paid pull.

## Sub-jobs / lanes
- L1 Scope + mode — the question in one line; `research.py run --mode auto` ($0 Codex-native) vs `--mode gemini` (paid, budget ledger) [parallel]
- L2 Zeitgeist check — today's brief per `directives/live-data-grounding-protocol.md`; `zeitgeist_engine.py run` if stale [parallel]
- L3 Foundation research — `python3 execution/research.py run --mode codex-native --query "…" --depth standard --max-total-provider-spend 10`; copy the Research Receipt verbatim [after: L1]
- L4 Specialist fanout — three angles (Pattern Hunter / Psychology Miner / Contrarian Scout) on free tiers; `research.py ingest --findings <jsonl> --query "…" --depth deep` [after: L3]
- L5 Verification — VERIFIED / LIKELY / UNCONFIRMED per claim; URL-less claims dropped at ingest [after: L4]
- L6 Compose — `.agent/workflows/briefs.md` schema: trust header, evidence rows (source_url + confidence), decision, deploy blocks, caveats, ledger [after: L2, L5]
- L7 Render + index — `execution/render_brief.py <json> --open`, `brief_library.py`, `brief_library.py verify`, `verify_briefing_room_portability.py` [after: L6]

## Ask me first
- Q: The decision this brief must move (what changes if the answer is X vs Y)? · look first: the open mission line, `.agent/cos/goals.json`
- Q: Any private fact the market can't tell us (your pricing, your capacity)? · look first: `FARRICE-MASTER-CONTEXT.md`, CAMPAIGN.md

## Handles alone
Scoping, free research, fan-out, ingest, labeling, composing, rendering, indexing, receipts.

## Comes back when
- A paid pull would change the answer (cost gate — never assumed)
- Sources disagree on the number the decision hinges on
- The question turns out to be a verdict, not a fact

## Needs approval
Any Gemini Deep Research or Perplexity spend · Monid cross-provider spend.

## Needs
The question · `.venv` · research.py · Briefing Room scripts · zeitgeist brief.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| paid run prints receipt but loses body (2026-09-02 scar) | body is written to `.tmp/research/` first; recover via `pending[]`, never re-run | recovery fails |
| claim has no URL | drop at ingest | the brief is empty without it |
| sources disagree | carry both with confidence labels | it moves the decision |
| Briefing Room verify fails | fix the JSON, re-render | second fail |

## Done means
Research Receipt in the header · `brief_library.py verify` + portability check pass · brief renders and opens · context pack generated · spend ledger line.

## Ratchet log
- none yet
