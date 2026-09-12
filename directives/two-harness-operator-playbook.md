# Two-Harness Operator Playbook (living doc — Farrice, 2026-09-11)

*"Best intelligence available as the starting base, never a nuclear weapon for a gunfight."*

This is how you run Claude Code and Codex as one shop after the `agent-loops-real` build. Every command
here exists and was live-fired on 2026-09-11. Update this file in place; never write a second one.

## Three ideas to embody

1. **The board is the brain.** A job lives on disk at `.agent/missions/<slug>/` (card · plan · lane briefs
   with result contracts · packets · trace · receipts). Your judgment gets written there ONCE, by the best
   model you have. Every other model then executes the board instead of asking you to steer it.
2. **Seats are pens.** Fable manages (plan · brief · verdict · integration). Opus 5, Sonnet, Astra and the
   5.6 models execute lane briefs. A seat never re-plans, never re-interviews, never widens scope. A question
   it cannot answer becomes a `PACKET:` line in its result file, and you answer it in one sentence.
3. **A loop exists only when a script performs the transition and writes a receipt.** No receipt file, it did
   not run. Design gauntlet, copy floor gate, worker seats, headless runs: each leaves one.

## The decision ladder (run it in your head before you type)

| Question | Answer |
|---|---|
| **Which door?** | One owner, one deliverable, fits a session → `/autopilot <ask>`. Several deliverables, days, dependent lanes, "handle it" → `/job <ask>`. Tradeoffs across experts → `/convene`. Mission OS work → `/mission`. Never two doors in one message. |
| **Which harness?** | You are already in one; stay there. Claude Code when the work is taste, synthesis, canonical-file surgery, or Fable is available. Codex when the work needs Astra's computer use, or your Fable usage is out, or the work is bounded repository grind on your ChatGPT plan. |
| **Which pen?** | Claude: Fable conducts; write lanes seat opus, read lanes seat sonnet. Codex: Astra (gpt-6-astra, medium) for everything; `gpt-5.6-sol` only for cheap mechanical grind. |
| **Which mode?** | In-session (you watch, visible beats) for taste work. Headless seats (`worker`) for parallel or mechanical lanes. Headless runner (`run`) when you want to walk away. Handoff (`handoff --to codex`) when Fable is out mid-job. |

## The six plays

### Play 1 — A task: `/autopilot`
```
/autopilot write the caption for Jen's Woodland Hills listing reel using LISTING-REEL-WINNERS
```
Mirror → shape check (it will push you to `/job` if the ask is a job) → compile → route → code gates → run →
receipt. `--preflight` prints the old `/go` card and waits for your yes. No board, no seats: one owner.

### Play 2 — A job: `/job`, once
```
/job build Jen's week-3 listing content: 5 posts, 2 reels, captions, all through the copy gate
```
Turn one is the JOB PLAN (interview only for what disk cannot answer). Say **go**. Then the manager runs every
unblocked lane, seats readers, closes lanes with LANE RECEIPT lines, batches questions into DECISION PACKETS,
and ends the turn only when the board prints MAY END. Fire `/job` once per job; after that, plain messages.
Resume any time on either harness: `/job resume <slug>` (Codex: `$job resume <slug>`).

### Play 3 — Delegate down inside the job (both harnesses)
```
python3 execution/job_board.py dispatch <slug>                 # writes lanes/<id>.brief.md per runnable lane
python3 execution/job_board.py worker <slug> --lanes L2,L3     # headless Claude seats: opus write / sonnet read
python3 execution/job_board.py worker <slug> --lanes L2,L3 --harness codex   # headless Astra seats on your ChatGPT plan
```
One `claude -p` or `codex exec` per brief, in parallel, no window. Each writes `lanes/<id>.result.md` and a
WORKER RECEIPT under `runs/`. Add `--auto-close`: a clean result closes the lane; a result carrying a `PACKET:`
line blocks the lane and files the packet for you. Inside a Claude session the manager can also seat a Sonnet
reader through the Agent tool; the brief is the same file.

### Play 4 — Walk away: the headless runner
```
python3 execution/job_board.py run <slug> --max-turns 6 --max-minutes 90            # Claude, opus pen
python3 execution/job_board.py run <slug> --harness codex                             # Astra pen
```
Loops `/job resume` from a lane worktree until MAY END, two stalls, or the minute cap. Refuses a pending plan
and refuses main. Receipts: `runs/<ts>-turn<N>.md`. Watch without a screen:
```
python3 execution/job_board.py status <slug> --trace
```

### Play 5 — Fable is out: keep the Claude sub working
Opus 5 is unsteerable raw and fine on a board. Either resume in the same Claude session on Opus
(`/job resume <slug>`: the Opus dialect card now injects BOARD-FIRST), or hand the job across:
```
python3 execution/job_board.py handoff <slug> --to codex     # then in Codex: $job resume <slug>
python3 execution/job_board.py handoff <slug> --to chat      # paste-anywhere packet for ChatGPT / claude.ai
```

### Play 6 — Loops that leave receipts
```
python3 execution/design_gauntlet.py open <slug> …  → shoot → attach → verdict → repair (cap 2) → close --risks
python3 execution/content_finish_gate.py check --file <draft.md> --label <name>
```
Gauntlet receipt: `gauntlet/<slug>/GAUNTLET-RECEIPT.md`. Copy gate log: `.agent/content-finish-log.jsonl`.
A copy artifact written with no gate line gets relayed at your next prompt as `NO content-finish-gate`.

## Codex specifics (it reads literally)

- The pen is **Astra**. The words sonnet/opus mean nothing there. Cheaper pen = `-m gpt-5.6-sol`.
- No native subagents (codex-cli 0.154.0). Astra delegates by shelling out: Play 3 with `--harness codex`.
- Doors are `$job`, `$autopilot`, `$convene`; global skills in `~/.codex/skills/` are thin pointers to the repo.
- Write in a Codex lane: `git worktree add .tmp/codex-worktrees/<slug> -b codex/<slug>` then
  `python3 execution/worktree_lane.py bootstrap`. Interactive Codex writes to the shared board need this
  line in `~/.codex/config.toml` (yours to add): `[sandbox_workspace_write]` /
  `writable_roots = ["/Users/farricecain/Google Antigravity/.agent"]`. Headless runs pass it themselves.
- Billing: `~/.codex/auth.json` holds ChatGPT tokens and no API key, so `codex exec` seats spend plan usage,
  not dollars. VERIFIED 2026-09-11.

## What burns what

| Seat | Spends | Use for |
|---|---|---|
| Fable 5.1 | the scarce Claude budget | plan, brief, verdict, integration, taste calls, canonical-file surgery |
| Opus 5 | Claude Max usage (heavier) | executing a Fable board: write lanes, headless manager turns |
| Sonnet 5 | Claude Max usage (lighter) | read lanes, verifier extensions, fixtures, captures, inventories |
| Astra | ChatGPT plan usage (not your constraint) | Codex jobs, computer-use work, parallel repo grind |
| gpt-5.6-sol | ChatGPT plan, cheapest | bulk mechanical grind you name explicitly |

Fable token discipline: read narrow (`grep -n`, `sed` ranges, verifier tails), never re-read after an edit,
never cat a file to find one line, never verify by subagent. If a turn is mostly tool output, it should have
been a seat.

## Daily rhythm

1. **Open:** `/eli5` — where every piece is, what waits on you, in 20 lines.
2. **Answer packets first:** `python3 execution/job_board.py packet <slug> answer <n> "<your words>"`. Nothing
   else moves a blocked lane.
3. **One job per session.** Different jobs in parallel sessions are fine; the same job in two sessions is not.
4. **Lanes, then merge:** every writer works in a lane; when done, `python3 execution/worktree_lane.py merge
   --lane <branch> --push`. When it says PARKED, run the absorb command it prints and stop.
5. **Close jobs.** A job whose lanes are all done but never closed does not ratchet its recipe card.
6. **Verify by receipt, not by memory:** `status <slug> --trace`, `runs/`, `GAUNTLET-RECEIPT.md`, the gate log.

## Anti-patterns (each one cost a session)

- Stacking doors (`/job` + `/raw-intent-bridge` in one message): the model picks the lighter one and skips the board.
- Firing `/job` on a task; running a task through a board leaves no trace and no learning.
- A seat that returns a PACKET line marked "complete." Blocked is the correct state.
- Delegating as a reflex. Best pen first; downgrade for parallel or mechanical lanes only.
- Steering Opus by hand. Write the board with Fable; let Opus execute it.
- A loop that lives in chat. If no script wrote a receipt, it did not run.

## Where things live

`.agent/workflows/job.md` · `.agent/workflows/autopilot.md` · `execution/job_board.py` (open · go · dispatch ·
worker · run · packet · handoff · resume · status · close) · `recipes/*.md` (cards; `recipe_cards.py match`) ·
`directives/orchestration-doctrine.md` (Conductor Ladder) · `directives/model-dialects/*.md` (hook-injected
per prompt) · verifiers `execution/verify_job_handoff.py` (126), `verify_design_gauntlet.py`,
`verify_content_finish_gate.py`.
