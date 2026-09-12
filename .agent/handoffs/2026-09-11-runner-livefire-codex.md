---
thread: runner-livefire-codex
status: mid-build
resume_hint: python3 execution/job_board.py resume runner-livefire-codex
unfinished: L1
branch: worktree-job-visibility-fix
pin: false
---

# JOB PACKET — runner-livefire-codex · for codex · generated 2026-09-11T21:10:54-07:00 on codex (branch worktree-job-visibility-fix)

## Resume
- `python3 execution/job_board.py resume runner-livefire-codex` then follow `skills/nate-b-jones-manager-loop/workflows/manager-loop-run.md`
- end the turn only when `python3 execution/job_board.py next runner-livefire-codex` prints MAY END

## Rules that travel
- Keep every unblocked lane moving; batch questions into DECISION PACKETS; deliver packets + receipts, not status.
- Never publish, send, spend, delete outside the repo, or ship AS Farrice without approval (the card's `Needs approval`).
- Dispatch briefs carry verbatim: "no Chain, no finalize, no Notion, no Next Moves, return only the artifact".

## Lanes now
| id | status | owner | after | expected | evidence | blocker |
|---|---|---|---|---|---|---|
| L1 | blocked | claude | — | Packet | /Users/farricecain/Google Antigravity/.claude/work | Awaiting answer to default-runner decision packet  |
runnable: none · waiting on deps: none · blocked on Farrice: L1 · done: none

## Decision packets open
## Packet 1 — L1 · open · 2026-09-11T21:10:53-07:00
Choice: Use Codex provisionally or retain Claude as the default unattended runner?
Irreversible? No; changing the default is reversible. No setting changed in this run.
Options: Codex: explicit workspace-write sandbox plus shared .agent access and approval_policy=never. Claude: current default, acceptEdits plus tool allowlist, no equivalent filesystem sandbox configured by runner. Comparative turn cost and live hook parity remain UNCONFIRMED: neither live-fire directory had a completed receipt at inspection; runner records no token/dollar usage. Evidence: .scratch/runner-livefire-codex/L1.result.md in job-visibility-fix worktree.
Recommend: Codex provisionally for bounded unattended repository jobs, based on explicit filesystem boundaries, not a proven cost or quality advantage. Confirm with matched completed receipts and usage/hook evidence before broad rollout.
If no answer: Keep the existing Claude default unchanged; this lane remains blocked on the packet answer.

## Decisions answered
none

## Trace (last 6 of 6)
- 2026-09-11T21:08:10-07:00 · - · opened · recipe decision-packet · 1 lanes · CONFIDENT match (score 17 is at or above 15) · [claude]
- 2026-09-11T21:08:10-07:00 · - · go · opened with --go (his 'just do it') · [claude]
- 2026-09-11T21:09:01-07:00 · L1 · dispatched · kind write · seat astra · brief .agent/missions/runner-livefire-codex/lanes/L1.brief.md · [codex]
- 2026-09-11T21:10:53-07:00 · L1 · asked · packet #1: Use Codex provisionally or retain Claude as the default unattended runner? · [codex]
- 2026-09-11T21:10:53-07:00 · L1 · blocked · planned → blocked · did: Researched both runner paths, receipt directories, usage trackers, hook wiring and official policies; wrote decision evidence and packet. Recommend Codex provisionally for filesystem boundaries; cost and live parity unconfirmed; no default changed. · blocker: Awaiting answer to default-runner decision packet 1 · result: /Users/farricecain/Google Antigravity/.claude/worktrees/job-visibility-fix/.scratch/runner-livefire-codex/L1.result.md · [astra]
- 2026-09-11T21:10:53-07:00 · L1 · found · Recommendation (INFERENCE): prefer Codex for bounded unattended repository jobs because this runner explicitly configures workspace-write and approval_policy=ne · [astra]

## Card
<!-- instance of recipes/decision-packet.md · opened 2026-09-11T21:08:10-07:00 by claude on claude · goal: Should job_board.py run default to claude or codex when both subscriptions are available — compare turn cost, sandbox limits, and hook parity from the receipts on disk and recommend one -->
---
job: decision-packet
name: Decision packet (a choice that is his, on the board)
family: harness
tier_default: T1
runs: 0
last_ratchet: never
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
- none yet

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
