---
job: mybpm-store-relaunch
name: MyBPM store relaunch (premium Shopify v2)
family: revenue-launch
tier_default: T2
runs: 0
last_ratchet: never
---

## The job
Take the MyBPM v2 theme (uploaded unpublished, Theme Check clean, but far from finished and with the acid signal removed) through a real review of design, layout, and how the store functions, then to a live store that can sell a first drop — with Farrice and Jen's approval on the look, every checkout check passed, and no publish or spend he didn't say yes to. Runs in its own dedicated session with the Shopify context loaded.

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
- 2026-09-10 — first open (parked same day, his call): the "built" v2 theme is NOT near ready — the Sublevel tee was a concept, never a real product linked on the site; **acid signal (#D7FF2F) is OUT** — drop it from `DESIGN.md` and every section before any review; the store needs its own dedicated session with the Shopify context loaded (the Shopify MCP tools ARE available in Claude Code: shop info, products, collections, GraphQL — use them to review the live store and the unpublished theme instead of trusting the receipt); budget undecided → run sourcing + margin math free first; supplier → research. Ask-me-first Q1 is answered NO; re-ask only after a rebuilt look.
