---
job: linkedin-week-batch
name: LinkedIn week batch (cash launch campaign)
family: revenue-launch
tier_default: T2
runs: 0
last_ratchet: never
---

## The job
A week of gated, voice-true LinkedIn posts plus a qualified DM layer, queued in the campaign board, none of it sent without him.

## Sub-jobs / lanes
- L1 Research — daily zeitgeist / brandjack scan, `.agent/workflows/linkedin-daily.md` Step 1 [parallel]
- L2 Opportunity menu — surface options plus raw-take priming questions [after: L1]
- L3 Cook — 3 variants per day per `linkedin-daily.md`, voice-gate pass [after: L2]
- L4 Gate — `directives/ai-slop-ban-bank.md` via `execution/prose_classifier.py`, `.agent/workflows/publishable-copy-gate.md` [after: L3]
- L5 Queue — one row per post in `_active/linkedin/CAMPAIGN.md`, week batch table [after: L4]
- L6 DM layer — qualified DM drafts, send-before-build, held for approval [after: L1]

## Ask me first
- Q: His raw take for this week's angle (the mandatory HALT) · look first: `_active/linkedin/CAMPAIGN.md`, thought-bank inbox
- Q: Which days ship vs hold this week? · look first: `_active/linkedin/03-launch`

## Handles alone
Research, opportunity menu, drafting variants, voice gate, lint, queue rows, DM drafts.

## Comes back when
- The raw-take HALT (mandatory, once per week)
- Two rejected renditions of one post → the brief is the problem, no third take
- A post would name a client or a private number

## Needs approval
Publishing any post · sending any DM.

## Needs
`.agent/workflows/linkedin-daily.md` · `_active/linkedin/CAMPAIGN.md` · `_active/farrice-brand/voice/VOICE-CARD.md` · voice-gate check.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| research thin one day | `--topic` override with his named moment | never invent the moment |
| a post fails voice-gate | rewrite once from the brief | second miss |
| DM target list stale | re-pull from CAMPAIGN.md standing facts | the list is empty |

## Done means
5-7 day batch of gated posts queued in `CAMPAIGN.md` · DMs drafted, not sent · nothing auto-posted.

## Ratchet log
- none yet
