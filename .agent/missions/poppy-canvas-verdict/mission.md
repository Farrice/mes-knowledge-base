# Mission: Tool build-vs-buy verdict

## Charter
- Slug: poppy-canvas-verdict
- Mode: system
- Status: active
- Goal: A working /canvas he can use for a week in place of Poppy, a parity test on his real workflow, a true monthly cost table, and a build-vs-buy verdict he can act on
- Created: 2026-09-10T13:03:59+00:00
- Updated: 2026-09-10T13:15:49+00:00
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
| L1 | claude | Reachable now | complete | the local version serves on a port he can open today; the "can't reach the server" class of failure is closed with a receipt (curl 200) | curl http://127.0.0.1:8766/canvas → 200 (lane server, --idle 0); 8765 = main, no /canvas until merge — that was the 'cannot reach the server' |  |  | L7 lands it on 8765 after the absorb packet |
| L2 | claude | Parity spec | complete | the exact job he runs in the paid tool (his tab, or his URLs + ask), written as a fixture: inputs, the ask, what a good answer contains | .agent/missions/poppy-canvas-verdict/parity-fixture.md (stand-in: Hormozi 4 latest → hooks; his real fixture arrives via packet 1) |  |  |  |
| L3 | claude | Parity run | complete | the fixture through the local version; time, tokens, cost, and the answer beside the paid tool's | parity-fixture.md Run 1: ingest 16s, reply 15.2s Sonnet est 0.32 USD on plan, 34,380 ctx tokens, first lines quoted, garble flagged; board .agent/canvas/boards/hormozi-test.json |  |  |  |
| L4 | claude | Ingestion edges | complete | every input type the paid tool takes (YouTube, TikTok, IG, PDF, article, voice note, profile page) tried once; pass / fail / needs-vendor per row | ingestion-edges.md: YouTube video PASS 1-11s · YouTube channel list PASS 1s · TikTok profile list PASS 1s · TikTok video FAIL (yt-dlp format/impersonation; vendor = vidIQ watch) · IG profile FAIL yt-dlp / PASS vidIQ 5cr · IG reel FAIL yt-dlp / vendor vidIQ · PDF PASS · article PASS · voice note PASS 2.5s local whisper |  |  |  |
| L5 | claude | Cost table | complete | keep vs build vs hybrid, monthly, with the marginal cost of one heavy session; build hours so far and remaining polish named | .agent/missions/poppy-canvas-verdict/cost-table.md — keep $66-90/mo vs canvas $0-2/mo; heavy session $0 marginal on plan; build 1 session spent, ~1 left for option A |  |  |  |
| L6 | claude | Verdict memo | complete | Do / Don't / Wrong-if in his words' plain register; what would reverse it | .agent/missions/poppy-canvas-verdict/verdict-memo.md — Do: one real job this week, let the trial lapse; Don't: chase parity; Wrong-if: IG/TikTok-heavy, latency kills the feel, or the tab habit never forms |  |  |  |
| L7 | claude | Land it | active | merge the lane so the always-on server has it; Homebase tile live; needs the merge-over-dirty-main approval | worktree_lane.py merge → LANE PARKED (main dirty, 71 tracked changes) |  | packet 3 — absorb main + merge is his to run; 8766 serves meanwhile | absorb main, then worktree_lane.py merge --lane worktree-poppy-canvas |

## Execution Receipt
- Planned lanes: L1, L2, L3, L4, L5, L6, L7
- Executed lanes: L1, L2, L3, L4, L5, L6
- Skipped or blocked lanes: L7: packet 3 — absorb main + merge is his to run; 8766 serves meanwhile
- Proof artifacts: curl http://127.0.0.1:8766/canvas → 200 (lane server, --idle 0); 8765 = main, no /canvas until merge — that was the 'cannot reach the server', .agent/missions/poppy-canvas-verdict/parity-fixture.md (stand-in: Hormozi 4 latest → hooks; his real fixture arrives via packet 1), parity-fixture.md Run 1: ingest 16s, reply 15.2s Sonnet est 0.32 USD on plan, 34,380 ctx tokens, first lines quoted, garble flagged; board .agent/canvas/boards/hormozi-test.json, ingestion-edges.md: YouTube video PASS 1-11s · YouTube channel list PASS 1s · TikTok profile list PASS 1s · TikTok video FAIL (yt-dlp format/impersonation; vendor = vidIQ watch) · IG profile FAIL yt-dlp / PASS vidIQ 5cr · IG reel FAIL yt-dlp / vendor vidIQ · PDF PASS · article PASS · voice note PASS 2.5s local whisper, .agent/missions/poppy-canvas-verdict/cost-table.md — keep $66-90/mo vs canvas $0-2/mo; heavy session $0 marginal on plan; build 1 session spent, ~1 left for option A, .agent/missions/poppy-canvas-verdict/verdict-memo.md — Do: one real job this week, let the trial lapse; Don't: chase parity; Wrong-if: IG/TikTok-heavy, latency kills the feel, or the tab habit never forms, worktree_lane.py merge → LANE PARKED (main dirty, 71 tracked changes)
- Validators run: [none]
- Resume command: /mission resume poppy-canvas-verdict

## Fresh Session Packet
- Required: False
- Fresh session packet: `[none]`
- Resume command: `/mission resume poppy-canvas-verdict`
- Next command: `python3 execution/job_board.py next poppy-canvas-verdict`
- State sources: .agent/missions/poppy-canvas-verdict/mission.json, .agent/intent-memory/current.json, .agent/system-cohesion-state.json
- Notes: [none]

## Handoffs
- None yet
