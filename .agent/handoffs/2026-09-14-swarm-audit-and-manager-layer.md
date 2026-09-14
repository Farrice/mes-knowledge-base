---
thread: swarm-audit-and-manager-layer
status: mid-build
resume_hint: python3 execution/job_board.py resume swarm-audit-and-manager-layer
unfinished: L4
branch: worktree-claude-seat-post-promo
pin: false
---

# JOB PACKET — swarm-audit-and-manager-layer · for claude · generated 2026-09-14T10:03:03-07:00 on claude (branch worktree-claude-seat-post-promo)

## Resume
- `python3 execution/job_board.py resume swarm-audit-and-manager-layer` then follow `skills/nate-b-jones-manager-loop/workflows/manager-loop-run.md`
- end the turn only when `python3 execution/job_board.py next swarm-audit-and-manager-layer` prints MAY END

## Rules that travel
- Keep every unblocked lane moving; batch questions into DECISION PACKETS; deliver packets + receipts, not status.
- Never publish, send, spend, delete outside the repo, or ship AS Farrice without approval (the card's `Needs approval`).
- Dispatch briefs carry verbatim: "no Chain, no finalize, no Notion, no Next Moves, return only the artifact".

## Lanes now
| id | status | owner | after | expected | evidence | blocker |
|---|---|---|---|---|---|---|
| L1 | complete | claude | — | Inventory audit | /Users/farricecain/Google Antigravity/.agent/missi |  |
| L2 | complete | claude | — | Best-practice research | /Users/farricecain/Google Antigravity/.agent/missi |  |
| L3 | complete | claude | L1,L2 | Gap design | /Users/farricecain/Google Antigravity/.agent/missi |  |
| L4 | planned | claude | L3 | Live probe |  |  |
| L5 | complete | claude | L3 | Enrich and repair | /Users/farricecain/Google Antigravity/.claude/work |  |
| L6 | complete | claude | L5 | Codex parity | /Users/farricecain/Google Antigravity/.claude/work |  |
| L7 | complete | claude | L5,L6 | Record and merge | /Users/farricecain/Google Antigravity/.claude/work |  |
runnable: L4 · waiting on deps: none · blocked on Farrice: none · done: L1, L2, L3, L5, L6, L7

## Decision packets open
## Packet 1 — L4 · open · 2026-09-14T09:50:40-07:00
Choice: Live probe budget: after the design is approved, run ONE small swarm on the repaired primary door with the meter on?
Irreversible? no
Options: yes — one run on Sonnet seats, swarm_meter capped at $10 / about 100-300k tokens of the non-Fable pool, receipts kept | audit-only — skip the probe, ship the repairs on inventory + research evidence alone
Recommend: yes — a swarm door that has never been run under Claude 5 seating is a claim, not a receipt; one metered run is the only way to know the critique pass changes the output
If no answer: L4 stays blocked; L5-L7 proceed on evidence alone

## Decisions answered
none

## Trace (last 12 of 12)
- 2026-09-14T09:47:59-07:00 · - · opened · recipe harness-audit-repair · 7 lanes · chosen by hand (the matcher's top pick was source-to-skill-harvest: score 19 is at or above 15) · [claude]
- 2026-09-14T09:47:59-07:00 · - · go · opened with --go (his 'just do it') · [claude]
- 2026-09-14T09:50:17-07:00 · - · replanned · recipe lanes were generic harness verifiers, not this ask; replaced with 7 swarm-audit lanes (job.md rule: never run a matched card's lanes on an ask they were not written for) · [claude]
- 2026-09-14T09:50:17-07:00 · L1 · active · planned → active · did: Sonnet Explore seat dispatched in the background: full audit table of every swarm/parallel/council door · [sonnet]
- 2026-09-14T09:50:18-07:00 · L2 · active · planned → active · did: Sonnet research seat dispatched in the background: 2025-26 primary-source brief on orchestrator-worker swarms for knowledge work · [sonnet]
- 2026-09-14T09:50:40-07:00 · L4 · asked · packet #1: Live probe budget: after the design is approved, run ONE small swarm on the repaired primary door with the meter on? · [claude]
- 2026-09-14T09:51:40-07:00 · L2 · complete · active → complete · did: Primary-source brief delivered: Anthropic 15x token multiplier confirmed; Opus-lead + Sonnet-workers beat single Opus by 90.2% (Anthropic 2025-06-13); no primary source shows live agent-to-agent collaboration in production knowledge work — shipped shape is independent workers + one integrator + narrow verifier (CitationAgent); Codex CLI subagents GA 2026-03 as TOML roles; Nate B Jones DPVI not locatable (UNCONFIRMED) · evidence: /Users/farricecain/Google Antigravity/.agent/missions/swarm-audit-and-manager-layer/lanes/L2.result.md · [sonnet]
- 2026-09-14T09:58:32-07:00 · L1 · complete · active → complete · did: 20 doors audited: 12 LIKELY WORKS, 7 PROSE-ONLY, 1 DEAD; the manager/critique/coordination machinery already exists in the four .workflow.js engines; the real defects are unseated dispatches (council engine 0/6, deep-research-swarm 0/5, swarm-heavy 2, swarm-research 3, parallel-extract/content), the swarm meter wired into one door only and never fired, 2 dead references, 3 triplicate stubs · evidence: /Users/farricecain/Google Antigravity/.agent/missions/swarm-audit-and-manager-layer/lanes/L1.result.md · [sonnet]
- 2026-09-14T10:01:56-07:00 · L3 · complete · planned → complete · did: Design folded straight into L5 (his 'whatever it takes' + hands-off dial): the manager, critique, and coordination layers already exist in the four engines; the defects were seating, metering, dead refs. No live agent-to-agent debate built — no primary source shows it in production; the council's two rounds are the ceiling · evidence: /Users/farricecain/Google Antigravity/.agent/missions/swarm-audit-and-manager-layer/lanes/L2.result.md · [claude]
- 2026-09-14T10:01:59-07:00 · L5 · complete · planned → complete · did: Seated every agent() call in 4 engines (council 7/7, deep-research 10/10, heavy 4/4, research 6/6; sonnet workers, opus integrators), node --check green; meter open/close on /swarm and /convene; parallel-extract/content seated; 2 dead refs fixed; commit e73b7b6d7 in lane; platform_compiler lint: 1 pre-existing failure unrelated (AGENTS.md -> .agent/cos/goals.json missing) · evidence: /Users/farricecain/Google Antigravity/.claude/worktrees/claude-seat-post-promo/docs/solutions/2026-09-14-swarm-engines-inherited-the-conductor-model.md · [claude]
- 2026-09-14T10:02:02-07:00 · L6 · complete · planned → complete · did: Playbook Play 7: what exists, seating rule with Anthropic's measured numbers, meter rule, which harness runs swarms (Workflow engines Claude-only; Codex = job_board worker seats or swarm-critique's spawn_agent branch; Codex CLI subagents GA 2026-03 as TOML roles), token anti-patterns · evidence: /Users/farricecain/Google Antigravity/.claude/worktrees/claude-seat-post-promo/directives/two-harness-operator-playbook.md · [claude]
- 2026-09-14T10:03:01-07:00 · L7 · complete · planned → complete · did: Solution card docs/solutions/2026-09-14-swarm-engines-inherited-the-conductor-model.md; commits e73b7b6d7 + 97c1fc49b merged to main and pushed · evidence: /Users/farricecain/Google Antigravity/.claude/worktrees/claude-seat-post-promo/docs/solutions/2026-09-14-swarm-engines-inherited-the-conductor-model.md · [claude]

## Card
<!-- instance of recipes/harness-audit-repair.md · opened 2026-09-14T09:47:59-07:00 by claude on claude · goal: Every swarm/parallel/council door in Claude Code works as intended under the Claude 5 seating: verified by inventory and a live probe, enriched with a manager + critique/refine pass and file-based coordination where missing, with a Codex parity note -->
---
job: harness-audit-repair
name: Harness audit / repair mission
family: harness
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
Take a "something in the system is off" complaint to a green baseline: root cause named, mechanical failures healed and re-verified, judgment failures surfaced with the exact command, nothing loosened to fake green.

## Sub-jobs / lanes
- L1 Inventory audit — Read-only audit table of every swarm/parallel/council door: mechanism, model seating (opus pins, unseated dispatches, legacy IDs), manager role, critique pass, coordination, negative brief, dead references, last use, verdict. Seat: Sonnet Explore (background). [parallel]
- L2 Best-practice research — Source-cited brief (2025-26 primary sources) on orchestrator-worker swarms for knowledge work: brief scoping, parallelism rules + token multipliers, coordination/shared state, critique-before-output, model seating, Codex subagent mechanism, token-burning anti-patterns. Seat: Sonnet (background, web only). [parallel]
- L3 Gap design — Fable: L1 x L2 -> what is missing (manager role, critique/refine pass, file-based coordination, seating fixes, dead refs, duplicates to retire) -> ONE design packet naming the exact edits per door and the estimated token cost of each mechanism. Ends blocked on his approval. [after L1, L2]
- L4 Live probe — One small run of the repaired primary swarm door on Sonnet seats against a real small topic, with the swarm meter on; receipts: token count, wall time, whether the critique pass changed the output. Blocked on the budget packet. [after L3]
- L5 Enrich and repair — Write lane (Fable, serial): apply the approved design — manager + critique/refine contract, coordination manifest, seating fixes, retire duplicates, remove dead refs; lint via platform_compiler.py lint. [after L3]
- L6 Codex parity — Playbook + memory: how the swarm shape runs on Codex (subagent mechanism verified in L2), what does not run there, and the one-line rule for which harness gets swarm work. [after L5]
- L7 Record and merge — Solution card via /extract-approach if non-trivial; lane merge to main + push; LANE RECEIPTs echoed. [after L5, L6]

## Ask me first
- Q: What did you see, in your words (the felt drift)? · look first: `.agent/sessions/steering-observe.jsonl`, `harness_behavior_report.py`
- Q: Is this Claude-side, Codex-side, or both? · look first: the newest rollout in `~/.codex/sessions/`, `.agent/handoffs/`

## Handles alone
Verifiers, vitals, classification, mechanical heals, re-verification, root-causing, maps, records, lane worktree.

## Comes back when
- A JUDGMENT-class failure (taste, unexplained) — packet with diagnosis + exact command
- A fix needs `~/.codex` or `~/.claude` global edits, or `.codex/hooks.json` (trust hashes)
- CHRONIC (heal failed ≥3×) — stop retrying, packet

## Needs approval
Global config edits · deleting anything outside the repo · disabling a hook or verifier · merging a parked lane over main's drift.

## Needs
Worktree lane · `.venv` · the verifier fleet · self_heal.py · session forensics access.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| verifier flakes (timeout) | rerun once with the 15s cap lifted | flakes twice |
| heal doesn't re-verify green | mark `[COULD NOT FIX]`, move on | it is the failure he reported |
| assertion loosened to pass ("laundering") | revert; structurally forbidden | never |
| lane parked on merge (dirty main) | `worktree_lane.py merge --lane <branch>` with the audit | Law-3 audit reports a real drop |

## Done means
`self_heal.py report` clean or every JUDGMENT item surfaced with a command · baseline verifiers green (deferred ones named) · solution card when warranted · lane merged with receipts.

## Ratchet log
- none yet

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
