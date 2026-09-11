---
thread: poppy-canvas-verdict
status: mid-build
resume_hint: python3 execution/job_board.py resume poppy-canvas-verdict
unfinished: L2
branch: worktree-poppy-canvas
pin: false
---

# JOB PACKET — poppy-canvas-verdict · for claude · generated 2026-09-10T06:21:56-07:00 on claude (branch worktree-poppy-canvas)

## Resume
- `python3 execution/job_board.py resume poppy-canvas-verdict` then follow `skills/nate-b-jones-manager-loop/workflows/manager-loop-run.md`
- end the turn only when `python3 execution/job_board.py next poppy-canvas-verdict` prints MAY END

## Rules that travel
- Keep every unblocked lane moving; batch questions into DECISION PACKETS; deliver packets + receipts, not status.
- Never publish, send, spend, delete outside the repo, or ship AS Farrice without approval (the card's `Needs approval`).
- Dispatch briefs carry verbatim: "no Chain, no finalize, no Notion, no Next Moves, return only the artifact".

## Lanes now
| id | status | owner | after | expected | evidence | blocker |
|---|---|---|---|---|---|---|
| L1 | complete | claude | — | Reachable now | curl http://127.0.0.1:8766/canvas → 200 (lane serv |  |
| L2 | blocked | claude | — | Parity spec | stand-in fixture on disk; request_access(Google Ch | packet 1 answered A but macOS Screen Recording is  |
| L3 | complete | claude | L2 | Parity run | parity-fixture.md Run 1: ingest 16s, reply 15.2s S |  |
| L4 | complete | claude | — | Ingestion edges | ingestion-edges.md: YouTube video PASS 1-11s · You |  |
| L5 | complete | claude | L3,L4 | Cost table | .agent/missions/poppy-canvas-verdict/cost-table.md |  |
| L6 | complete | claude | L5 | Verdict memo | .agent/missions/poppy-canvas-verdict/verdict-memo. |  |
| L7 | complete | claude | L1 | Land it | worktree_lane.py merge → LANE MERGED 6 commits / 2 | packet 3 — absorb main + merge is his to run; 8766 |
runnable: none · waiting on deps: none · blocked on Farrice: L2 · done: L1, L3, L4, L5, L6, L7

## Decision packets open
none

## Decisions answered
## Packet 1 — L2 · answered · 2026-09-10T06:06:27-07:00
Choice: May I read your open Poppy tab (Claude in Chrome, read-only) so the parity fixture is your exact job, not the Hormozi stand-in?
Irreversible? no
Options: A: yes, read the tab | B: no — I paste the URLs + the ask here | C: the stand-in is enough
Recommend: A
If no answer: stand-in fixture stays; verdict rests on mechanism, not your exact job

Answer (Farrice, 2026-09-10T06:15:14-07:00): A — read the Poppy tab; the Jen social-content session pushed to Notion is the best use he's had of it
## Packet 2 — L6 · answered · 2026-09-10T06:06:30-07:00
Choice: What does 'worth it' mean here? It sets how much more gets built.
Irreversible? no
Options: A: replaces Poppy for creator-video analysis + drafting → cancel Poppy at trial end, build stops at polish | B: must match Poppy feature-for-feature (IG/TikTok transcripts, images, streaming) → more build + vidIQ credits | C: answer only → keep Poppy, park the canvas
Recommend: A
If no answer: A

Answer (Farrice, 2026-09-10T06:15:14-07:00): A — replace Poppy for creator-video analysis + drafting; build stops at polish
## Packet 3 — L7 · answered · 2026-09-10T06:06:33-07:00
Choice: Where does the canvas live for the trial week? Landing on the always-on 8765 needs main hygiene first (71 generated files from scheduled jobs, no hand work in them): python3 execution/main_drift_absorb.py then python3 execution/worktree_lane.py merge --lane worktree-poppy-canvas
Irreversible? no
Options: A: you run the absorb + merge now → /canvas on 8765 + Homebase tile | B: use the lane port 8766 for the week, merge later
Recommend: A
If no answer: B — 8766 stays up (--idle 0) until you say otherwise

Answer (Farrice, 2026-09-10T06:15:14-07:00): A — land it on 8765 (absorb + merge)

## Card
<!-- instance of recipes/tool-build-vs-buy-verdict.md · opened 2026-09-10T06:03:59-07:00 by claude on claude · goal: A working /canvas he can use for a week in place of Poppy, a parity test on his real workflow, a true monthly cost table, and a build-vs-buy verdict he can act on -->
---
job: tool-build-vs-buy-verdict
name: Tool build-vs-buy verdict
family: harness
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
Take "should I keep paying for tool X or build it here?" to a verdict he can act on: a working local version he can use for real (not a demo), a parity test on the exact workflow he values in the paid tool, a true monthly cost table for keep / build / hybrid, and a Do / Don't / Wrong-if memo. Stop the build the moment the parity test says the feel is not reachable.

## Sub-jobs / lanes
- L1 Reachable now — the local version serves on a port he can open today; the "can't reach the server" class of failure is closed with a receipt (curl 200) [parallel]
- L2 Parity spec — the exact job he runs in the paid tool (his tab, or his URLs + ask), written as a fixture: inputs, the ask, what a good answer contains [parallel]
- L3 Parity run — the fixture through the local version; time, tokens, cost, and the answer beside the paid tool's [after: L2]
- L4 Ingestion edges — every input type the paid tool takes (YouTube, TikTok, IG, PDF, article, voice note, profile page) tried once; pass / fail / needs-vendor per row [parallel]
- L5 Cost table — keep vs build vs hybrid, monthly, with the marginal cost of one heavy session; build hours so far and remaining polish named [after: L3, L4]
- L6 Verdict memo — Do / Don't / Wrong-if in his words' plain register; what would reverse it [after: L5]
- L7 Land it — merge the lane so the always-on server has it; Homebase tile live; needs the merge-over-dirty-main approval [after: L1]

## Ask me first
- Q: May I read the paid tool's open tab to copy the exact workflow? · look first: nothing on disk can answer this
- Q: What does "worth it" mean — replace the tool for the one job, match it feature-for-feature, or answer only? · look first: `FARRICE-MASTER-CONTEXT.md` offer/priority section, `MEMORY.md` cost-transparency rule
- Q: Which surface for the trial week — land on the always-on server (needs main hygiene) or run from the lane port? · look first: `project_main-hygiene-lane-backlog.md`

## Handles alone
Ingestion tests, timing, token counts, cost math, seat wiring, page fixes, the memo draft, receipts.

## Comes back when
- Parity run shows the feel is not reachable without a paid vendor — packet with the exact gap and the vendor cost
- A seat needs a global tool upgrade (codex CLI, claude CLI) — his call
- Anything that spends beyond cents (Gemini Pro at scale, vidIQ credits > 25) — packet first

## Needs approval
Reading his browser tab · upgrading global CLIs · merging a parked lane over main's drift · any vendor signup.

## Needs
Worktree lane · `.venv` · pulse_serve port · the paid tool's trial still active for the side-by-side.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| an ingestion path fails | mark the row FAIL with the log line, keep the others moving | it is the input type he uses most |
| a seat is blocked (login, old CLI) | run the parity on the seats that work, note the gap | the blocked seat is the one he wanted |
| lane parked on merge (dirty main) | keep serving from the lane port; packet for the absorb | never block the trial on it |
| paid tool's output unavailable for comparison | compare against the ask's own "good answer contains" list | he wants the side-by-side specifically |

## Done means
He has used the local version on one real job · cost table with receipts · memo delivered · lane merged or the trial port documented · his verdict recorded.

## Ratchet log
- none yet

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
