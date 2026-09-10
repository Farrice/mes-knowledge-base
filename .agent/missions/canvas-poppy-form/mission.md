# Mission: Tool build-vs-buy verdict

## Charter
- Slug: canvas-poppy-form
- Mode: code
- Status: active
- Goal: Make /canvas look, feel and operate like Poppy so Farrice actually uses it: rail, thumbnail cards, profile card, chat panel with conversations + fullscreen, rendered replies with copy; every control proven in the browser, then landed on 8765
- Created: 2026-09-10T16:23:45+00:00
- Updated: 2026-09-10T16:26:25+00:00
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
| L1 | claude | Reachable now | complete | the local version serves on a port he can open today; the "can't reach the server" class of failure is closed with a receipt (curl 200) | lane server 8766 serves the Poppy-form page (curl 200); 8765 gets it on merge |  |  |  |
| L2 | claude | Parity spec | complete | the exact job he runs in the paid tool (his tab, or his URLs + ask), written as a fixture: inputs, the ask, what a good answer contains | spec = his Poppy board read in full: rail, thumbnail cards, profile card, chat panel w/ conversations + skill chip + fullscreen, dotted wires, zoom rail, rendered replies w/ copy (.agent/missions/poppy-canvas-verdict/jen-poppy-thread-raw.md) |  |  |  |
| L3 | claude | Parity run | complete | the fixture through the local version; time, tokens, cost, and the answer beside the paid tool's | browser test in the Claude Browser pane: + new conversation, new chat, note, fullscreen, theme, compose send → Gemini reply landed + markdown table rendered; server test canvas_ui_actions_test.py 19/19 actions ok incl. loop refusal |  |  |  |
| L4 | claude | Ingestion edges | complete | every input type the paid tool takes (YouTube, TikTok, IG, PDF, article, voice note, profile page) tried once; pass / fail / needs-vendor per row | profile card (YouTube channel / TikTok profile → latest N via yt-dlp, 4 posts in ~3 s; IG refused with a clear message), md renderer (tables, bold, lists, code blocks w/ copy, details), transcript expand, thumbnails via i.ytimg / favicon |  |  |  |
| L5 | claude | Cost table | complete | keep vs build vs hybrid, monthly, with the marginal cost of one heavy session; build hours so far and remaining polish named | cost unchanged: $0 build spend beyond the plan; one Gemini test turn ≈ $0.001 |  |  |  |
| L6 | claude | Verdict memo | complete | Do / Don't / Wrong-if in his words' plain register; what would reverse it | readout in chat; remaining polish listed (streaming impossible on plan; IG profile via vidIQ later) |  |  |  |
| L7 | claude | Land it | blocked | merge the lane so the always-on server has it; Homebase tile live; needs the merge-over-dirty-main approval |  |  | merge parked: main dirty — needs `python3 execution/main_drift_absorb.py` (his), then `worktree_lane.py merge --lane worktree-poppy-canvas` + `launchctl kickstart -k gui/501/com.antigravity.pulse-serve` |  |

## Execution Receipt
- Planned lanes: L1, L2, L3, L4, L5, L6, L7
- Executed lanes: L1, L2, L3, L4, L5, L6
- Skipped or blocked lanes: L7: merge parked: main dirty — needs `python3 execution/main_drift_absorb.py` (his), then `worktree_lane.py merge --lane worktree-poppy-canvas` + `launchctl kickstart -k gui/501/com.antigravity.pulse-serve`
- Proof artifacts: lane server 8766 serves the Poppy-form page (curl 200); 8765 gets it on merge, spec = his Poppy board read in full: rail, thumbnail cards, profile card, chat panel w/ conversations + skill chip + fullscreen, dotted wires, zoom rail, rendered replies w/ copy (.agent/missions/poppy-canvas-verdict/jen-poppy-thread-raw.md), browser test in the Claude Browser pane: + new conversation, new chat, note, fullscreen, theme, compose send → Gemini reply landed + markdown table rendered; server test canvas_ui_actions_test.py 19/19 actions ok incl. loop refusal, profile card (YouTube channel / TikTok profile → latest N via yt-dlp, 4 posts in ~3 s; IG refused with a clear message), md renderer (tables, bold, lists, code blocks w/ copy, details), transcript expand, thumbnails via i.ytimg / favicon, cost unchanged: $0 build spend beyond the plan; one Gemini test turn ≈ $0.001, readout in chat; remaining polish listed (streaming impossible on plan; IG profile via vidIQ later)
- Validators run: [none]
- Resume command: /mission resume canvas-poppy-form

## Fresh Session Packet
- Required: False
- Fresh session packet: `[none]`
- Resume command: `/mission resume canvas-poppy-form`
- Next command: `python3 execution/job_board.py next canvas-poppy-form`
- State sources: .agent/missions/canvas-poppy-form/mission.json, .agent/intent-memory/current.json, .agent/system-cohesion-state.json
- Notes: [none]

## Handoffs
- None yet
