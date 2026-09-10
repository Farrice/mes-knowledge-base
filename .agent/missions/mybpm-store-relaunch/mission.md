# Mission: MyBPM store relaunch (premium Shopify v2)

## Charter
- Slug: mybpm-store-relaunch
- Mode: general
- Status: active
- Goal: Take the built, unpublished MyBPM v2 theme live as a store that sells a four-piece drop, with his and Jen's approval on the look and every checkout check passed
- Created: 2026-09-10T12:48:03+00:00
- Updated: 2026-09-10T12:48:03+00:00
- Librarian: not_applicable

## Validation Contract
- Define correctness before execution.
- Assign every feature or workstream to at least one assertion.
- Run scrutiny and user-outcome validators at milestone boundaries.

| ID | Assertion | Covered by | Validator | Pass signal |
|---|---|---|---|---|
| - | No assertions recorded yet | - | - | - |

## Artifact Contract
- Type: none


## Approved Package Load Set
- None recorded.


## Mission Activation Queue
| ID | Owner | Workflow/Skill | Status | Expected artifact | Evidence path | Assertion | Blocker | Next action |
|---|---|---|---|---|---|---|---|---|
| L1 | claude | Look review packet | planned | desktop + mobile screenshots of the unpublished preview (`https://mybpm.store/?preview_theme_id=158270324891`) beside `preview/design-board.html`; the three things to look at, in his and Jen's words |  |  |  |  |
| L2 | claude | Capsule proof | planned | per `03-capsule-selection.md`: Sublevel tee leads; hoodie, bucket hat, Defined tee need physical samples; list what each still needs (sample, measurements, material claim, photos) |  |  |  |  |
| L3 | claude | Store config | planned | per `05-build-and-launch.md` §3: collection `DROP 001 / SUBLEVEL`, menu New Drop / Shop / Editorial / About, metafields from `04-content-and-data.md`, populate from `data/product-data-packet.json`, real social links only |  |  |  |  |
| L4 | claude | Cleanup | planned | remove the dead `thisnew` / `popcustoms` supplier scripts, hide mockup-only products from primary nav, reconcile policy pages |  |  |  |  |
| L5 | claude | Transactional QA | planned | `06-qa.md` blocking checks: test order through payment sandbox, tax, shipping, fulfillment route, purchase events fire once, rollback copy of the live Ira theme identified |  |  |  |  |
| L6 | claude | Sourcing + unit economics | planned | the unsolved part (memory 2026-07-25): a blank/supplier whose silhouettes read as real streetwear, landed cost per piece, price, margin per the four products; DTG ruled out |  |  |  |  |
| L7 | claude | Publish packet | planned | everything green → one packet: publish v2, keep Ira as rollback |  |  |  |  |

## Execution Receipt
- Planned lanes: L1, L2, L3, L4, L5, L6, L7
- Executed lanes: [none]
- Skipped or blocked lanes: [none]
- Proof artifacts: [none]
- Validators run: [none]
- Resume command: /mission resume mybpm-store-relaunch

## Fresh Session Packet
- Required: True
- Fresh session packet: `[none]`
- Resume command: `/mission resume mybpm-store-relaunch`
- Next command: `python3 execution/job_board.py next mybpm-store-relaunch`
- State sources: .agent/missions/mybpm-store-relaunch/mission.json, .agent/intent-memory/current.json, .agent/system-cohesion-state.json
- Notes: [none]

## Handoffs
- None yet
