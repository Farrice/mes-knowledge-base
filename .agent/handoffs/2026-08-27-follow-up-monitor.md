---
thread: follow-up-monitor
status: active
resume_hint: Browser crash pop-ups fixed: Codex local automations paused + heartbeat deleted; verify no crashes tomorrow 8-9 AM, notion-reliability branch still unmerged
branch: main
pin: false
---

# Handoff — Browser crash pop-ups / Codex automations

## Purpose
Diagnose why Chrome, Firefox, and Playwright kept crashing with "reopen" pop-ups every weekday ~8 AM, then act on Farrice's decision: move the two daily Codex briefs off local execution and delete the 10-minute merge heartbeat.

## Current State
- Root cause CONFIRMED: ChatGPT desktop's local Codex automations (`daily-brief` 8 AM, `follow-up-monitor` 9 AM) launch Playwright browsers from a background context with no window-server access; every browser aborts in `RegisterApplication` (crash reports in `~/Library/Logs/DiagnosticReports/`, responsibleProc = ChatGPT).
- "Cloud execution" does NOT exist for local automations — app schema (app.asar) allows only `local` | `worktree`. Verified, not guessed.
- DONE: `daily-brief` + `follow-up-monitor` set to PAUSED in `~/.codex/automations/*/automation.toml` AND `~/.codex/sqlite/codex-dev.db` (next_run_at NULL, verified via `~/.codex/tools/automation_control_status.py`).
- DONE: deleted `finish-notion-second-brain-merge` heartbeat (10-min retry loop, 2 weeks of failed merges). Backup: scratchpad `finish-notion-second-brain-merge.bak`.
- OPEN: branch `codex/notion-second-brain-reliability` remains unmerged into main (commits 10eb863b9 / 3c56e9d56 absent) — the heartbeat's job never completed; needs a manual `worktree_lane.py merge` decision.
- Farrice still needs to: restart ChatGPT app once (flush in-memory scheduler) and recreate the two briefs as ChatGPT scheduled tasks (server-side, connector-based).

## Remaining Priority
Confirm no new browser crash reports appear tomorrow ~8-9 AM; if any do, the ChatGPT app restart hadn't happened — re-verify the paused state in the control center.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
