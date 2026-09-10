# JOB PACKET — mybpm-store-relaunch · for claude · generated 2026-09-10T05:54:33-07:00 on claude (branch worktree-manager-loop-harvest)

## Resume
- `python3 execution/job_board.py resume mybpm-store-relaunch` then follow `skills/nate-b-jones-manager-loop/workflows/manager-loop-run.md`
- end the turn only when `python3 execution/job_board.py next mybpm-store-relaunch` prints MAY END

## Rules that travel
- Keep every unblocked lane moving; batch questions into DECISION PACKETS; deliver packets + receipts, not status.
- Never publish, send, spend, delete outside the repo, or ship AS Farrice without approval (the card's `Needs approval`).
- Dispatch briefs carry verbatim: "no Chain, no finalize, no Notion, no Next Moves, return only the artifact".

## Lanes now
| id | status | owner | after | expected | evidence | blocker |
|---|---|---|---|---|---|---|
| L1 | blocked | claude | — | Look review packet |  | parked for a dedicated MyBPM session (his call 202 |
| L2 | blocked | claude | — | Capsule proof |  | parked for a dedicated MyBPM session (his call 202 |
| L3 | blocked | claude | L1 | Store config |  | parked for a dedicated MyBPM session (his call 202 |
| L4 | blocked | claude | L1 | Cleanup |  | parked for a dedicated MyBPM session (his call 202 |
| L5 | blocked | claude | L3,L4 | Transactional QA |  | parked for a dedicated MyBPM session (his call 202 |
| L6 | blocked | claude | — | Sourcing + unit economics |  | parked for a dedicated MyBPM session (his call 202 |
| L7 | blocked | claude | L2,L5,L6 | Publish packet |  | parked for a dedicated MyBPM session (his call 202 |
runnable: none · waiting on deps: none · blocked on Farrice: L1, L2, L3, L4, L5, L6, L7 · done: none

## Decision packets open
none

## Decisions answered
## Packet 1 — L1 · answered · 2026-09-10T05:54:33-07:00
Choice: Look direction as built (white canvas, black structure, acid signal, Kith restraint) — approve, review, or rebuild?
Irreversible? no
Options: A approve / B review with Jen / C rebuild
Recommend: B — review with Jen first
If no answer: nothing downstream starts

Answer (Farrice, 2026-09-10T05:54:33-07:00): Not ready. The build from Codex/Work is far from finished; the Sublevel tee was a concept, not a real product linked on the site. Acid signal is OUT — no lime green, no tackiness. The store needs a dedicated session with its own context; we are not finishing it here. This session = the usefulness of recipe cards + manager loop.
## Packet 2 — L6 · answered · 2026-09-10T05:54:33-07:00
Choice: Sample/photo budget and supplier for the drop
Irreversible? no
Options: A tee only / B fund four / C math first; supplier: research vs named
Recommend: C — margin math first; research the supplier
If no answer: sourcing lane runs free research only

Answer (Farrice, 2026-09-10T05:54:33-07:00): Budget: not sure yet — run the sourcing and margin math first (free). Supplier: research it.

## Card
<!-- instance of recipes/mybpm-store-relaunch.md · opened 2026-09-10T05:48:03-07:00 by claude on claude · goal: Take the built, unpublished MyBPM v2 theme live as a store that sells a four-piece drop, with his and Jen's approval on the look and every checkout check passed -->
---
job: mybpm-store-relaunch
name: MyBPM store relaunch (premium Shopify v2)
family: revenue-launch
tier_default: T2
runs: 0
last_ratchet: never
---

## The job
Take the already-built MyBPM v2 theme (uploaded, unpublished, Theme Check clean) from staging to a live store that can sell a four-piece drop, with Farrice and Jen's approval on the look and every checkout check passed, without a single publish or spend he didn't say yes to.

## Sub-jobs / lanes
- L1 Look review packet — desktop + mobile screenshots of the unpublished preview (`https://mybpm.store/?preview_theme_id=158270324891`) beside `preview/design-board.html`; the three things to look at, in his and Jen's words [parallel]
- L2 Capsule proof — per `03-capsule-selection.md`: Sublevel tee leads; hoodie, bucket hat, Defined tee need physical samples; list what each still needs (sample, measurements, material claim, photos) [parallel]
- L3 Store config — per `05-build-and-launch.md` §3: collection `DROP 001 / SUBLEVEL`, menu New Drop / Shop / Editorial / About, metafields from `04-content-and-data.md`, populate from `data/product-data-packet.json`, real social links only [after: L1]
- L4 Cleanup — remove the dead `thisnew` / `popcustoms` supplier scripts, hide mockup-only products from primary nav, reconcile policy pages [after: L1]
- L5 Transactional QA — `06-qa.md` blocking checks: test order through payment sandbox, tax, shipping, fulfillment route, purchase events fire once, rollback copy of the live Ira theme identified [after: L3, L4]
- L6 Sourcing + unit economics — the unsolved part (memory 2026-07-25): a blank/supplier whose silhouettes read as real streetwear, landed cost per piece, price, margin per the four products; DTG ruled out [parallel]
- L7 Publish packet — everything green → one packet: publish v2, keep Ira as rollback [after: L2, L5, L6]

## Ask me first
- Q: Is the look direction approved as built (white canvas, black structure, one acid signal, Kith restraint) — or does Jen's logo-on-every-design view change it? · look first: memory `mybpm-streetwear-brand` (unresolved), `02-brand-direction.md`, `DESIGN.md`
- Q: Sample and photography budget for the drop, and who shoots? · look first: `09-night-society-photography.md`, `03-capsule-selection.md`
- Q: Which supplier/blank do you already trust for the Sublevel tee (330 gsm)? · look first: `01-live-audit.md`, `04-listings.md` in merch-os-run-1

## Handles alone
Screenshots and review packet, capsule gap list, Shopify Admin configuration on the UNPUBLISHED theme, dead-script cleanup, metafields, policy drafts, QA runs in sandbox, sourcing research with landed-cost math, the publish packet.

## Comes back when
- Look approval (his + Jen's) — nothing downstream starts without it
- A blocking QA item fails twice
- Sourcing math shows a product cannot clear margin at a sellable price
- Any spend (samples, photography, apps) or the publish itself

## Needs approval
Publishing the theme (`shopify theme publish` — real revenue surface) · any spend · deleting products or policies · any change to the live Ira theme · outward messages to suppliers in his name.

## Needs
Shopify CLI auth to `mybpm.store` (his login) · the relaunch package `_active/mybpm/premium-shopify-relaunch/` · payment sandbox access · Jen in the room for the look call.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| Shopify rejects a template import (scar: `custom.short_description`) | remove the fragile dynamic block, re-push, re-verify MD5 | second rejection |
| supplier scripts still referenced | disable in Admin, log the app | the app is operationally required |
| sample not in hand | keep the product sample-gated; ship the drop with the Sublevel tee alone | he wants the four-piece drop on day one |
| purchase event fires twice | fix the pixel config, retest | second fail |
| Jen and Farrice disagree on the look | present both as A/B on the design board, one packet | always — it is theirs |

## Done means
Unpublished theme reviewed and approved on desktop + mobile · `06-qa.md` blocking list all checked with evidence · collection + menu + metafields live on the staging theme · sourcing sheet with landed cost and margin per product · publish packet answered, and if yes: v2 published, Ira identified as rollback, first test order receipt.

## Ratchet log
- none yet

