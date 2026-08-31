---
date: 2026-08-28
session: follow-up-monitor
tier: operator-guide
status: enriched
---

# System: Browser Crash Automations + Second Brain Merge - Fixed and Landed — What We Built 2026-08-28 and How to Use It

> This session killed the daily "Chrome/Firefox/Playwright quit unexpectedly" pop-ups (root cause: ChatGPT desktop's local Codex automations launching browsers from a windowless background context) and landed the two-week-parked `codex/notion-second-brain-reliability` merge — your memory facade now searches 9 stores, including a network-free Notion mirror. Companions: [.agent/handoffs/2026-08-28-follow-up-monitor.md](../.agent/handoffs/2026-08-28-follow-up-monitor.md) (full session state) · `docs/solutions/2026-08-11-notion-second-brain-local-first-repair.md` (the branch's own repair card).

## ⚡ If you only read 10 lines

- Memory recall now hits Notion **without the network**: `python3 execution/memory_facade.py "<intent>" --top 10` — a `notion` source queries the local mirror in `sovereign.db`; `mirror_notion.py` owns freshness (nightly).
- Restrict stores when you want just one: `--sources notion` (or any comma list from: sovereign, notion, automem, wiki, agents, episodic, solutions, prompts, catalog).
- Second-brain health check: `python3 execution/verify_notion_second_brain_reliability.py` → expect `PASS 11/0`.
- Codex automations live in `~/.codex/automations/<id>/automation.toml` **plus** a row in `~/.codex/sqlite/codex-dev.db` — pausing means editing BOTH (`status = "PAUSED"`, `next_run_at NULL`), then restarting the ChatGPT app.
- See every automation at a glance: `python3 ~/.codex/tools/automation_control_status.py`.
- `execution_environment` accepts ONLY `local` | `worktree` — "cloud" does not exist; the cloud path is a ChatGPT scheduled task, created in the app.
- Browser crash forensics: `~/Library/Logs/DiagnosticReports/*.ips` — the `responsibleProc` field names the true launcher; `RegisterApplication → abort()` = GUI app launched with no window-server session.
- A lane merge that keeps parking "main tree dirty" is telling you to commit the telemetry backlog on main first — that exact backlog silently starved a retry loop for two weeks.
- Doctrine line: a stuck retry automation is an alarm clock, not the work — deleting it deletes nothing; landing the merge it was retrying is the fix.
- Still open: origin/main divergence (origin +9) — recover-files-first per `directives/merge-discipline.md`, never `merge -s ours`.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `python3 execution/memory_facade.py "<query>" --top 10` | Ranked recall across all 9 stores | Any "have we done/decided this before?" moment |
| `python3 execution/memory_facade.py "<query>" --sources notion --json` | Notion-mirror-only hits, machine-readable | You specifically want Notion pages, scripted |
| `python3 execution/verify_notion_second_brain_reliability.py` | 11-check PASS/FAIL receipt | After touching notion_api / session memory / mirror code |
| `python3 execution/verify_memory_stack.py` | Import + facade smoke receipt | After any memory-stack dependency change |
| `python3 ~/.codex/tools/automation_control_status.py` | Table: every Codex automation, schedule, last/next run | "What is ChatGPT running on my Mac and when?" |
| `python3 execution/session_lock.py claim "<mission>"` → `release <token>` | Legitimate main-tree writer token | Manual merge/long write while automations coexist |
| `python3 execution/worktree_lane.py merge --lane <branch>` | Guarded merge or a one-line PARK reason | Landing any lane; read the park reason, don't force |
| `ls -lt ~/Library/Logs/DiagnosticReports/ \| head` | Recent macOS crash reports | Any "app quit unexpectedly" pop-up investigation |

## The mental model

1. **Two stores, one truth.** Codex automations are dual-written (toml dir + sqlite). The toml is what the app re-reads; the DB drives the scheduler's next-run. Change one and not the other and you get ghost behavior. Same shape as every mirror in this repo: fix both or fix nothing.
2. **`responsibleProc` beats the crash name.** macOS attributes every crash to the process tree that spawned it. Four different "apps" crashing = one launcher failing four times. Start attribution at the responsible process, not the dialog.
3. **Guards park for exactly one reason at a time.** The lane merge surfaced its blockers serially: dirty tree → fresh writer lock → content conflict. Each park message is the entire diagnosis. A retry loop can't clear any of them — only a driver reading the message can.
4. **Additive conflicts resolve by union.** Both sides added a memory source to the same lines. Neither was wrong; the merge keeps both. Check whether a conflict is *competing edits* or *parallel additions* before picking a side.

## Capability: Notion local-mirror recall (`notion` source in memory_facade)

**What it is.** A ninth recall store: LIKE-token search over the `notion_mirror` table inside `sovereign.db`, read-only (`PRAGMA query_only=ON`), returning `[db_name] title — excerpt` snippets with direct notion.so links. Zero network round-trips; `mirror_notion.py` owns freshness via the nightly sync. Shipped alongside `execution/notion_session_memory.py` (session-memory writes queued for your review — the review gate stays yours).

**When to reach for it.** Any recall where the answer might live in the 5 Notion DBs — past session memories, Simon Library cards — and you want it in the same ranked list as sovereign/episodic/solutions instead of a separate Notion query.

**When NOT to.** Live Notion writes or fresh-page reads — that's `execution/notion_api.py` (pinned `2022-06-28`), which pays the network cost for current data. The mirror is at most a day stale by design.

**How to invoke.** It's automatic — `recall()` and the CLI include it by default. Explicit: `--sources notion`.

**Worked example (live).** This very session's closeout ran `notion-session-memory: OK — Session Memory queued for review` and the smoke query `"notion second brain reliability"` returned 5 notion-mirror hits ranked among 9 stores — the merged code exercised itself within the hour it landed.

**Honest edges.** Token-LIKE scoring, not semantic — phrase your query with content words. Mirror freshness untested against a missed nightly run (degrades to `notion mirror unavailable`, never crashes recall). The union resolution passed 11/11 verifier checks + live smoke, but no load test on large mirrors.

## Capability: Codex automation control (outside the repo, on the Mac)

**What it is.** Ground-truth map of what ChatGPT desktop schedules on this machine: `~/.codex/automations/<id>/automation.toml` (definitions: rrule, model, `execution_environment`, status) + `~/.codex/sqlite/codex-dev.db` (`automations`, `automation_runs` tables driving the scheduler).

**When to reach for it.** Unexplained periodic behavior — crash pop-ups on a clock, surprise CPU, jobs running "on their own." The control-status table answers it in one command.

**When NOT to.** Don't hand-edit these files to *create* automations — that's the ChatGPT app's job. Manual edits are for pause/inspect/delete, followed by an app restart to flush the in-memory schedule.

**How to invoke.** Status table: command above. Pause: set `status = "PAUSED"` in the toml AND `UPDATE automations SET status='PAUSED', next_run_at=NULL WHERE id='<id>'` in the DB. Delete: remove the toml dir and the DB row (back up first).

**Worked example (live).** `daily-brief` (weekdays 8 AM) and `follow-up-monitor` (9 AM) paused both-store; `finish-notion-second-brain-merge` (a 10-minute heartbeat that had been failing for two weeks) deleted. Crash dialogs stopped with them.

**Honest edges.** Crash-free morning not yet observed (paused late on the 27th; check `DiagnosticReports` after 8–9 AM). ChatGPT app restart still pending — until then the old schedule may live in memory. The two briefs are OFF, not migrated: recreating them as ChatGPT scheduled tasks is a human step in the app.

## Composition (options, not wiring)

| Stacks with | When it earns its cost |
|---|---|
| `/resume follow-up-monitor` | Re-entering this thread — handoff carries the divergence-recovery next step |
| `directives/merge-discipline.md` + `git-guardrails-claude-code` skill | Before the origin +9 recovery pass — the one remaining git task |
| `execution/memory_pulse.py --full` | Periodic check that notion-mirror rows keep flowing into recall |
