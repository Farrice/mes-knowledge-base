---
thread: claude-seat-post-promo
status: mid-build
resume_hint: python3 execution/job_board.py resume claude-seat-post-promo
unfinished: L1
branch: worktree-claude-seat-post-promo
pin: false
---

# JOB PACKET — claude-seat-post-promo · for claude · generated 2026-09-13T23:54:36-07:00 on claude (branch worktree-claude-seat-post-promo)

## Resume
- `python3 execution/job_board.py resume claude-seat-post-promo` then follow `skills/nate-b-jones-manager-loop/workflows/manager-loop-run.md`
- end the turn only when `python3 execution/job_board.py next claude-seat-post-promo` prints MAY END

## Rules that travel
- Keep every unblocked lane moving; batch questions into DECISION PACKETS; deliver packets + receipts, not status.
- Never publish, send, spend, delete outside the repo, or ship AS Farrice without approval (the card's `Needs approval`).
- Dispatch briefs carry verbatim: "no Chain, no finalize, no Notion, no Next Moves, return only the artifact".

## Lanes now
| id | status | owner | after | expected | evidence | blocker |
|---|---|---|---|---|---|---|
| L1 | blocked | claude | — | Packet | .agent/missions/claude-seat-post-promo/decisions.m | his answer to packet #1 (A/B/C) |
runnable: none · waiting on deps: none · blocked on Farrice: L1 · done: none

## Decision packets open
## Packet 1 — L1 · open · 2026-09-13T23:54:31-07:00
Choice: From 09-14, when the week's Fable share is spent, who takes the live Claude Code chair for messy, shaping-heavy knowledge work?
Irreversible? no — a per-session model-picker choice; re-seat any time
Options: A) Sonnet 5 in the live chair, Fable for plan/brief/verdict/taste only, Opus 5 never live — it executes written boards headless (job_board.py run/worker), Codex keeps repo grind. Evidence: 08-20 containment test (Sonnet 0 tool calls/25s on a 2-sentence ask vs Opus 9 calls/86s), Sonnet blind take rated GREAT, Opus board-executed studio_preview.py landed with 15 tests on 09-03. | B) Opus 5 in the live chair with the dialect card and BOARD-FIRST injection. Tried 07-27 and 08-20; both sessions opened with 'horrible experience'. GDPval-AA v2 says Opus 5 beats Sonnet 5 on judgment work (1861 vs 1618 Elo, LIKELY), but the failure you feel is scope expansion and over-structure in live turns, which benchmarks do not measure. | C) Drop to Max 5x () and buy Fable usage credits. The Fable ceiling is 50% of whatever pool you have, so a smaller plan shrinks the Fable allowance too; credit burn rate UNCONFIRMED (Anthropic publishes no per-token quota). Only wins if you truly abandon every non-Fable model.
Recommend: A. The verified rule is that half your $200 can only be spent through non-Fable models, so the real question is how to make that half productive, not whether Opus is redeemable. /job is the answer for job-shaped work (Fable writes the board, Opus executes it headless). For the messy shaping conversations, Sonnet 5 is the steerable seat. No Opus 5 point release or behavior update was found in the web check (UNCONFIRMED that any exists).
If no answer: the harness already defaults to A (two-harness playbook, Play 5); you keep closing Claude Code when Fable runs out and the non-Fable half of the plan stays unused

## Decisions answered
none

## Trace (last 6 of 6)
- 2026-09-13T23:52:20-07:00 · - · opened · recipe decision-packet · 1 lanes · chosen by hand (the matcher's top pick was mybpm-store-relaunch: top score 7 is under the floor 10) · [claude]
- 2026-09-13T23:52:20-07:00 · - · go · opened with --go (his 'just do it') · [claude]
- 2026-09-13T23:53:47-07:00 · L1 · found · VERIFIED (support.claude.com/15424964): Fable 5 and 5.1 on Max = up to 50% of the weekly limit, inside the same pool, then usage credits or switch model. VERIFIED (support.claude.com/15910845): +50% Claude Code weekly promo runs through 2026-09-13; page says limits 'return to standard' after. LIKELY (@ClaudeDevs via BleepingComputer): permanent +25% over old baseline from 09-14 = 17% below today. · [claude]
- 2026-09-13T23:53:47-07:00 · L1 · found · Session record: 2026-07-27 and 2026-08-20 sessions both opened with 'horrible experience with Opus 5'; 08-20 blind A/B: Opus artifact GREAT, Fable TERRIBLE (n=1) — his Opus pain is live-session ergonomics, not output quality. 2026-09-03 he handed Opus 5 a written board (studio preview wrapper) as a test; execution/studio_preview.py was built and committed (e53c8496b). · [claude]
- 2026-09-13T23:54:31-07:00 · L1 · asked · packet #1: From 09-14, when the week's Fable share is spent, who takes the live Claude Code chair for messy, shaping-heavy knowledge work? · [claude]
- 2026-09-13T23:54:34-07:00 · L1 · blocked · planned → blocked · did: Verified plan rules on Anthropic's own pages (Fable 50% share inside the pool; promo ends 09-13), pulled the 07-27/08-20/09-03 session record on Opus 5, wrote one packet with three priced options and a recommendation; skipped: Fable credit burn rate (unpublished) · evidence: .agent/missions/claude-seat-post-promo/decisions.md · blocker: his answer to packet #1 (A/B/C) · [claude]

## Card
<!-- instance of recipes/decision-packet.md · opened 2026-09-13T23:52:20-07:00 by claude on claude · goal: Decide how Farrice gets quality knowledge work out of his $200 Claude Max subscription after the +50% promo ends 2026-09-13, given Fable 5.1 is metered at a share of the pool and Opus 5 has been a poor live-session partner -->
---
job: decision-packet
name: Decision packet (a choice that is his, on the board)
family: harness
tier_default: T1
runs: 5
last_ratchet: 2026-09-11
---

## The job
Take a DECISION-shaped ask ("should I…", "which…", "allocate…") to one packet he can answer in a sentence: the options researched with receipts, one recommendation with the why, what happens if he does not answer. It lives on the board as a one-lane job so the packet shows on Homebase and in the session brief instead of vanishing in a chat reply. No build, no lanes beyond the one.

## Sub-jobs / lanes
- L1 Packet — research every option named (prices, limits, what he already pays for on disk: `.agent/*.json` trackers, `directives/<service>-usage-policy.md`, `MEMORY.md` cost rules); write ONE decision packet (`job_board.py packet add`); mark this lane blocked on his answer [parallel]

## Ask me first
- Q: none before the packet — the packet IS the question · look first: the ask itself names the options; budgets live in `.agent/*.json` and the usage policies

## Handles alone
Reading trackers and policies, web-checking prices and plan limits, the math, the recommendation.

## Comes back when
- The packet is written (that is the only come-back)
- A named option cannot be priced from any source — say so inside the packet, never guess

## Needs approval
Nothing — a decision packet spends nothing and sends nothing. Acting on his answer is a NEW job if it is job-shaped.

## Needs
The ask verbatim · `.agent/*.json` spend trackers · usage-policy directives · web access for current prices.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| a price or limit is unverifiable | label it UNCONFIRMED in the packet | never — the packet carries the label |
| the ask is really a job (several deliverables, sequence) | close this and `/job` it with a real recipe | in one line |
| his answer needs work done | open the follow-on job; this one closes as answered | never |

## Done means
One packet on the board (Choice · Irreversible? · Options + recommendation · If no answer) · every figure labelled VERIFIED / LIKELY / UNCONFIRMED · lane L1 blocked on his answer · after his answer: lane complete with the answer as evidence, job closed.

## Ratchet log
- 2026-09-11 — decision-packet: the worker seat writes the PACKET line, the manager files it, he answers in a sentence
- 2026-09-11 — decision-packet: the worker seat writes the PACKET line, the manager files it, he answers in a sentence
- 2026-09-11 — decision-packet: the worker seat writes the PACKET line, the manager files it, he answers in a sentence
- 2026-09-11 — decision-packet: the worker seat writes the PACKET line, the manager files it, he answers in a sentence
- 2026-09-11 — decision-packet: the worker seat writes the PACKET line, the manager files it, he answers in a sentence

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
