---
job: client-readout-brief
name: Client readout brief (research brief system)
family: client-content
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
Turn a live thread into a readout brief the client or Farrice can act on — verified facts filled first, judged synthesis only in named slots, nothing sent until it clears the gates.

## Sub-jobs / lanes
- L1 Scope — which client or thread, and the decision the readout must support [parallel]
- L2 Evidence gather — deliverable paths, git log, prior brief state [parallel]
- L3 Fact meaning split — fill every number, path, date, link first; synthesis writes only the named slots per `python3 execution/mission_brief.py slots` [after: L2]
- L4 Build — `python3 execution/mission_brief.py build --slug <s>` renders md, html, json, share formats [after: L3]
- L5 Gate — `execution/prose_classifier.py check`, VERIFIED / LIKELY / UNCONFIRMED labels on every claim [after: L4]
- L6 Finalize — `execution/chain_runner.py finalize` [after: L5]

## Ask me first
- Q: Which decision must this readout actually change? · look first: the client's CLAUDE.md, the thread's prior brief
- Q: Zero-operator-language required for this reader? · look first: `feedback_client-artifacts-zero-operator-language.md`, `feedback_client-facing-implementation-grade.md`

## Handles alone
Scope, evidence gather, brief build, lints, finalize.

## Comes back when
- A claim only he can verify (a private or unconfirmable fact)
- Sources disagree on something that changes the recommendation
- A client-facing tone or disclosure call

## Needs approval
Sending the brief to the client · publishing it anywhere public.

## Needs
`deliverables/research-briefs/` · `execution/mission_brief.py` · `execution/prose_classifier.py` · `execution/chain_runner.py`.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| source bundle missing or stale | run the sweep first, note the gap in the receipt | the thread is client-facing |
| a fact is unconfirmed | label UNCONFIRMED, never restate as fact | it changes the recommendation |
| a chart has fewer than 3 points or no real variation | drop the chart and its section, note it | never force a flat chart |

## Done means
Brief file(s) exist under `deliverables/research-briefs/<slug>/` · prose lint clean · finalize carries no QUALITY GATE BLOCKED · nothing sent to the client yet.

## Ratchet log
- none yet
