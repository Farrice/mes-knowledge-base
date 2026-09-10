# Mission: Listing launch package

## Charter
- Slug: rosita-listing-hooks
- Mode: client
- Status: active
- Goal: Hooks and short intro scripts for 19225 Rosita that stop the scroll, sound like Jen, and she would actually film: one text she picks from
- Created: 2026-09-10T18:20:42+00:00
- Updated: 2026-09-10T18:27:13+00:00
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
| L1 | claude | Intake | complete | detect URL/address/paste, mint slug; Playwright fetch → paste fallback; `execution/listing_intel.py parse|diff|ledger --slug <s>` | _active/clients/jen-listings/19225-rosita-tarzana/claims-ledger.json |  |  |  |
| L2 | claude | Market read | complete | `python3 execution/research.py "<area + segment>" --depth standard --json` | _active/clients/jen-listings/19225-rosita-tarzana/19225-rosita-SHOOT-SHEET.md |  |  |  |
| L3 | claude | Strategy | complete | register + buyer map from `listing-package.md` (Quiet Flex Elite vs FTHB calm-warm), no script yet | _active/clients/jen-listings/19225-rosita-tarzana/19225-rosita-SHOOT-SHEET.md |  |  |  |
| L4 | claude | Generate hooks | complete | six via `skills/jen-santulan-listing-content/references/prompts-v2/listing-hook-set.md` | _active/clients/jen-listings/19225-rosita-tarzana/hooks-v3-pen.md |  |  |  |
| L5 | claude | Package | complete | `listing-send-package.md` → `<slug>/SEND-TO-JEN-text.md`; Gigi family: `engine/gen_slides.py` → `render.py` → `review_sheet.py` → `build_canvas.py` | _active/clients/jen-listings/19225-rosita-tarzana/SEND-TO-JEN-text.md |  |  |  |
| L6 | claude | Gates | complete | `execution/fair_housing_lint.py check`, `execution/client_package_lint.py`, `execution/prose_classifier.py check`, in-run Blind Bar self-check | .agent/fair-housing-lint.jsonl |  |  |  |
| L7 | claude | Finalize | complete | `execution/chain_runner.py finalize … --content-file <slug>/SEND-TO-JEN-text.md` | .agent/session-state.md |  |  |  |

## Execution Receipt
- Planned lanes: L1, L2, L3, L4, L5, L6, L7
- Executed lanes: L1, L2, L3, L4, L5, L6, L7
- Skipped or blocked lanes: [none]
- Proof artifacts: _active/clients/jen-listings/19225-rosita-tarzana/claims-ledger.json, _active/clients/jen-listings/19225-rosita-tarzana/19225-rosita-SHOOT-SHEET.md, _active/clients/jen-listings/19225-rosita-tarzana/hooks-v3-pen.md, _active/clients/jen-listings/19225-rosita-tarzana/SEND-TO-JEN-text.md, .agent/fair-housing-lint.jsonl, .agent/session-state.md
- Validators run: [none]
- Resume command: /mission resume rosita-listing-hooks

## Fresh Session Packet
- Required: True
- Fresh session packet: `[none]`
- Resume command: `/mission resume rosita-listing-hooks`
- Next command: `python3 execution/job_board.py next rosita-listing-hooks`
- State sources: .agent/missions/rosita-listing-hooks/mission.json, .agent/intent-memory/current.json, .agent/system-cohesion-state.json
- Notes: [none]

## Handoffs
- None yet
