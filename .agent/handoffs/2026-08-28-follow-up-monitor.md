---
thread: follow-up-monitor
status: active
resume_hint: Check ~/Library/Logs/DiagnosticReports for 8-9 AM crashes; Farrice: restart ChatGPT + recreate briefs as ChatGPT tasks; then origin+9 divergence recovery
unfinished: Crash-free morning unverified; ChatGPT restart + cloud task recreation pending (human); origin/main divergence recovery not started
branch: main
pin: true
---

# System: Browser Crash Automations + Second Brain Merge - Fixed and Landed

## Purpose
Two jobs, both closed: (1) diagnosed and stopped the daily "Chrome/Firefox/Playwright quit unexpectedly" pop-ups on Farrice's Mac; (2) landed the two-week-stuck `codex/notion-second-brain-reliability` merge into main, verified.

## Current State

### Browser crash pop-ups — root-caused and stopped
- Cause: ChatGPT desktop's **local Codex automations** (`daily-brief` weekdays 8 AM, `follow-up-monitor` 9 AM) launched Playwright browsers from a background context with no window-server access; every browser aborted in `RegisterApplication`. Crash reports: `~/Library/Logs/DiagnosticReports/*.ips`, all with `responsibleProc: ChatGPT`.
- Both automations set to PAUSED in `~/.codex/automations/*/automation.toml` **and** `~/.codex/sqlite/codex-dev.db` (next_run_at NULL). Verified via `python3 ~/.codex/tools/automation_control_status.py`.
- "Cloud execution" is NOT a valid config value — app schema (app.asar) allows only `local`|`worktree`. Cloud equivalent = ChatGPT scheduled tasks (server-side, connectors).
- Deleted the runaway 10-minute heartbeat `finish-notion-second-brain-merge` (toml dir + DB row). Backup: session scratchpad `finish-notion-second-brain-merge.bak` (temp — gone after reboot).

### Second Brain merge — landed and verified
- Merge commit `d1d98190c` on main. Union-resolved `execution/memory_facade.py`: facade now searches 9 stores including the branch's new **notion local-mirror** source AND main's **catalog** source + read instrumentation. Three directive conflicts (activation counters) took main's newer side.
- Verified: `execution/verify_notion_second_brain_reliability.py` **11/11 PASS** · `verify_memory_stack.py` PASS · live facade smoke returned notion-mirror hits.
- Lane worktree + branch deleted (worktree had only a symlink); session lock claimed/released cleanly.
- Pre-merge: committed 122-file telemetry backlog (`fdb43f270`) — that dirty tree was why the heartbeat failed for two weeks.

### Uncertain / watch
- ChatGPT app may still hold the old automation schedule in memory until restarted — if crash pop-ups appear tomorrow 8–9 AM, that's why; re-check the control status table.
- `origin/main` divergence: origin holds 9 commits main lacks (standing alarm). No push attempted. Needs recover-files-first per `directives/merge-discipline.md` — never `merge -s ours`.

## Remaining Priority (next session)
1. Confirm no new `.ips` crash reports in `~/Library/Logs/DiagnosticReports/` from 8–9 AM.
2. Farrice (human steps): restart ChatGPT app once; recreate the two briefs as ChatGPT scheduled tasks (prompt text preserved in the paused tomls).
3. Then: origin/main divergence recovery (origin +9) before any push.

## Do NOT Rebuild
- The pause/delete work is DONE — do not touch `~/.codex` automations again unless crashes recur.
- The second-brain merge is DONE — never re-merge or re-solve the memory_facade conflict; `git log d1d98190c` is the proof.

## Core Paths
- `execution/memory_facade.py` — the union-merged 9-store recall facade (notion + catalog both live)
- `execution/verify_notion_second_brain_reliability.py` — the 11-check verifier (all passing at close)
- `directives/merge-discipline.md` — BINDING rules for the pending origin/main divergence recovery
- `.agent/handoffs/2026-08-27-follow-up-monitor.md` — prior handoff for this thread (diagnosis detail)

## Suggested skills (next agent)
- `resolving-merge-conflicts` — only if divergence recovery hits conflicts.
- `git-guardrails-claude-code` — before the origin/main recovery pass.
- No expert skill load needed for the crash-verification check (pure diagnostics).
