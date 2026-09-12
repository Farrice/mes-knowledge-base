---
job: jen-listing-reel
name: Jen listing reel from the winners storehouse
family: client-content
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
From a listing to a reel built off a cleared winner in the storehouse — approved register, on-screen line, caption payoff, assembled and gate-clean — nothing sent to Jen or her buyers.

## Sub-jobs / lanes
- L1 Winners read — `_active/clients/jen-listings/06-system/WINNERS.md`, `CANON.md` [parallel]
- L2 Listing intake — the address folder under `_active/clients/jen-listings/` (e.g. `1654-moonseed-simi-valley`) [parallel]
- L3 Register call — approved specimen register from WINNERS.md section 1, buyer stage [after: L1, L2]
- L4 Onscreen line — pens per the on-screen-line doctrine, 80/20 rule (text carries attention, caption carries payoff) [after: L3]
- L5 Caption payoff — conversational caption carrying the recognition beat [after: L4]
- L6 Assembly — `skills/video-studio` pipeline: transcribe, cutlist, broll ladder, captions per `_active/farrice-brand/voice/video-style.md` [after: L5]
- L7 Gates — `execution/fair_housing_lint.py check`, `execution/client_package_lint.py`, `execution/prose_classifier.py check` [after: L6]

## Ask me first
- Q: Which agent register — her verbatim voice or drafted? · look first: `_active/clients/jen-listings/06-system/WINNERS.md` §1, `_active/clients/jen-santulan/` voice notes
- Q: Live numbers (price, HOA, dates) confirmed for this listing? · look first: the listing source, the listing folder's own files

## Handles alone
Winners read, intake, register call, on-screen line drafts, caption, assembly, all lints.

## Comes back when
- No reference in WINNERS.md clears both checks (relevance + complete execution) for this listing's angle
- Live numbers are unconfirmed and the caption quotes them
- Which on-screen line gets filmed (his or Jen's pick)

## Needs approval
Sending anything to Jen or her buyers (sends stay human) · publishing to her channels.

## Needs
`_active/clients/jen-listings/06-system/WINNERS.md` · the listing folder · `skills/video-studio` · `execution/fair_housing_lint.py`.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| no winner clears both checks | list the rejected candidates, hold for a fresh reference | never invent a reference |
| fair-housing lint exits nonzero | rewrite; hard stop on shipping over it | never |
| a number changed since intake | recheck the listing source, flag every changed field | a changed number changes the hook |

## Done means
Fair-housing, client-package, and prose lints all clean · reel assembled and captioned · nothing sent to Jen.

## Ratchet log
- none yet
