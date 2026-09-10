---
job: tool-build-vs-buy-verdict
name: Tool build-vs-buy verdict
family: harness
tier_default: T1
runs: 1
last_ratchet: 2026-09-10
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
