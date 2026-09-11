---
job: listing-launch-package
name: Listing launch package
family: client-content
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
From a listing URL, address, or paste to a complete, forwardable launch package (hooks, register, send text) the agent can paste to her buyers, gates clean, in one run with no mid-run stops.

## Sub-jobs / lanes
- L1 Intake — detect URL/address/paste, mint slug; Playwright fetch → paste fallback; `execution/listing_intel.py parse|diff|ledger --slug <s>` [parallel]
- L2 Market read — `python3 execution/research.py "<area + segment>" --depth standard --json` [parallel]
- L3 Strategy — register + buyer map from `listing-package.md` (Quiet Flex Elite vs FTHB calm-warm), no script yet [after: L1, L2]
- L4 Generate hooks — six via `skills/jen-santulan-listing-content/references/prompts-v2/listing-hook-set.md` [after: L3]
- L5 Package — `listing-send-package.md` → `<slug>/SEND-TO-JEN-text.md`; Gigi family: `engine/gen_slides.py` → `render.py` → `review_sheet.py` → `build_canvas.py` [after: L4]
- L6 Gates — `execution/fair_housing_lint.py check`, `execution/client_package_lint.py`, `execution/prose_classifier.py check`, in-run Blind Bar self-check [after: L5]
- L7 Finalize — `execution/chain_runner.py finalize … --content-file <slug>/SEND-TO-JEN-text.md` [after: L6]

## Ask me first
- Q: Which agent and which register? · look first: client `CLAUDE.md`, memory `feedback_jen-listing-send-package-shape`
- Q: Live numbers (price, HOA, dates) confirmed? · look first: the listing source, `<slug>/README-FIRST.txt`

## Handles alone
Fetching, parsing, market read, register call, hooks, package, all lints, finalize, canvas build. His 2026-08-05 rule: no mid-run taste gates — judgment happens on the finished brief.

## Comes back when
- All three fetch rungs fail → packet asking for a paste (never invent a fact)
- Live numbers unconfirmed and the send text quotes them
- Which of the six hooks gets filmed (his or the client's pick)

## Needs approval
Sending anything to the client or her buyers (sends stay human) · any paid fetch (Apify is retired — never route there).

## Needs
Listing source · `execution/listing_intel.py` · research.py · the client's skill dir · Claude Design canvas access for the Gigi family.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| fetch blocked | Playwright per `directives/browser-automation-safety.md`, then paste request | after both fail |
| fair-housing lint exit 2 | rewrite; hard stop on shipping over it | never |
| numbers changed since intake | `listing_intel.py diff`, flag every changed field in the send text | a changed number changes the hook |
| Blind Bar self-check fails twice | back to the brief, not a third take | second miss |

## Done means
Both lints clean · finalize has no `QUALITY GATE BLOCKED` · `<slug>/SEND-TO-JEN-text.md` complete in one shot · canvas or slides rendered where the family needs them.

## Ratchet log
- none yet
