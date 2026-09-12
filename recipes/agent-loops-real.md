---
job: agent-loops-real
name: Make the agent loops real (audit, runner, recipes)
family: harness
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
Every loop this harness advertises either runs with a receipt on disk or is named as prose and repaired or retired: the manager loop gets a headless walk-away runner, the recipe library gets seeded from his repeated jobs, and the critic loops (design gauntlet, copy floor gate, adversarial review, QA review loop, control-beating review) are audited for evidence of ever running and made receipt-bearing or retired. Forged 2026-09-11 from his verdict: "I'm tired of our harness being half-functioning."

## Sub-jobs / lanes
- L1 Loop inventory — every workflow, skill, or agent that claims to iterate, critique, or gate (design gauntlet, adversarial review, qa review loop, publishable copy gate, copy doctor, writers room, control beating review, prose classifier gate, design iteration loop): for each — exists? deterministic runner? receipt path? any receipt of ever running? verifier? One table, paths only [parallel]
- L2 Disease memo — from L1: which loops are prose only, which have a runner but no receipt, which have receipts; the one design rule that separates them; repair vs retire per loop with the reason [after: L1]
- L3 Headless runner — `job_board.py run <slug> --harness claude|codex --max-turns N --spend-cap USD` loops resume until MAY END inside a lane, one run receipt per turn under `.agent/missions/<slug>/runs/`, stops on no-progress; live-fired on a real job [parallel]
- L4 Recipe seeding — ten cards from his repeated jobs, each Ask-me-first tied to disk paths, lint clean, match floor proven on the real ask that produced each [parallel]
- L5 Critic loop repair — the loops L2 marks repairable get a deterministic runner + receipt file + both-direction verifier (design gauntlet and the copy floor gate first); retired ones get superseded pointers [after: L2]
- L6 Verifier and live fire — verify_job_handoff extended for the runner; one real /job run end to end (dispatch → sonnet seat → result close → MAY END); one design artifact and one copy artifact through their repaired loops with receipts [after: L3, L4, L5]
- L8 Front door collapse — task-shaped asks get ONE door with the bridge's shape (mirror · route · run, no preflight sign-off beat): /go's Stage 0.5 preflight becomes opt-in, /raw-intent-bridge and /go share one compiler; job-shaped → /job; deliberation → /convene; autopilot, orchestrate, swarm, strike, parallel-swarm, mission get superseded pointers or a one-line role; CLAUDE.md and AGENTS.md routing anchors updated; nothing deleted [after: L2]
- L7 Closeout — four questions with receipts, memory and docs updated, recipe ratcheted [after: L6, L8]

## Ask me first
- Q: Which ten repeated jobs get cards first? · look first: `.agent/missions.jsonl`, `recipes/`, MEMORY.md active projects, `deliverables/` folder names (the manager proposes ten; he strikes or adds)
- Q: Headless runner spend cap per run and default harness · look first: `directives/*-usage-policy.md`, cost gate config (no per-run cap exists today; the number is his)
- Q: Retire or repair when a critic loop is prose-only with zero runs? · look first: the L2 memo (default: repair the two he named, retire the rest with pointers)
- Q: Any front door you want kept by name after the collapse (/go, /autopilot, /orchestrate, /swarm, /strike, /mission)? · look first: `.agent/workflows/*.md` usage receipts, `docs/solutions/` (default: /job, /convene, and one task door survive; the rest become pointers)

## Handles alone
Inventory, receipts, memo, runner build, card drafting, verifier, live fire on repo-internal artifacts, docs.

## Comes back when
- A critic loop's repair changes what an existing skill does for a client (Jen, Cooz) — his verdict
- The headless runner needs a permission mode wider than the lane grants
- Any spend beyond the cost-gate floor

## Needs approval
Retiring any workflow he named as loved · any paid API call in live fire · pushing main.

## Needs
`.agent/workflows/` · `skills/` · `.claude/agents/` · `execution/verify_*.py` · `.agent/sessions/steering-observe.jsonl` · `job_board.py` · `worktree_lane.py` · `claude -p` and `codex exec`.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| a loop's runner exists but throws | record the traceback as the receipt, mark repairable | never |
| headless run loops without progress | stop at max-turns, receipt names the stuck lane | on the second stuck run |
| recipe lint fails | fix the card, re-lint | a lane name has no workflow behind it |
| live fire needs a paid call | use a free artifact | always — that is the packet |

## Done means
Every advertised loop carries one of three labels with a receipt path: RUNS (receipt of a real run) · REPAIRED (runner + receipt + verifier) · RETIRED (superseded pointer). `job_board.py run` finished one real job to MAY END unattended. Ten new cards lint clean. Verifier green.

## Ratchet log
- none yet
