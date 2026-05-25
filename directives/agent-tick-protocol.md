# Agent Tick Protocol (Phase D / 2026-05-25)

> **Owner**: `execution/agent_tick.py` + `execution/task_queue.py`
> **Plan**: `/Users/farricecain/.claude/plans/i-think-the-biggest-virtual-emerson.md` Phase D
> **Status**: v1 shipped 2026-05-25 (skeleton + dry-run). v1.1 (full execution mode) deferred.

This directive defines the safety contract for autonomous multi-day agent work. The infrastructure is real and the cost of a runaway tick loop is also real — these rules exist to make autonomous mode safe by default.

---

## The Five Rules (Non-Negotiable)

### Rule 1 — ONE PHASE PER TICK

Each wake advances the project by AT MOST one phase. Never compound. Never auto-execute "phase N then phase N+1 since I have time" — that's how runaway agents burn through cost ceilings and produce uncalibrated work.

Enforced in: `agent_tick.run_tick()` — returns after writing the wake-report, regardless of how many additional pending phases exist.

### Rule 2 — BLOCK ON AMBIGUITY

If the next phase requires a taste call, branching choice, or any decision the user hasn't pre-approved → halt. Move the phase from `pending.jsonl` to `blocked.jsonl` with a clear reason. Do NOT improvise past a taste boundary.

Examples of ambiguity that MUST block:
- "Pick the best of these 3 angles" (taste)
- "Should we extend the scope to also cover X?" (decision)
- "The factual grounding came back unclear" (verification gate)
- "The first sub-result was below the bimodal PASS bar" (calibration)

Enforced in: human-in-loop. agent_tick reads the wake-report-instructions and surfaces blocking decisions; v1.1 execution mode will call `task_queue.mark_blocked()` when the chain returns a `STATUS=blocked` outcome.

### Rule 3 — EXPLICIT OPT-IN

A project does NOT get a launchd tick installed automatically. Two-step opt-in:

```bash
# Step 1: register in the agent_tick registry
python3 execution/agent_tick.py enable --project <slug>

# Step 2: install the launchd job (manual — see Appendix A)
# This is intentionally not auto-installed. launchd jobs persist across
# reboots, run as your user, and have full disk access. Installing one is
# a meaningful security boundary; the user MUST do this consciously.
cp ~/Library/LaunchAgents/com.antigravity.agent-tick.<slug>.plist  ...
launchctl load ~/Library/LaunchAgents/com.antigravity.agent-tick.<slug>.plist
```

Removing opt-in: `agent_tick.py disable --project <slug>` removes from the registry; user separately runs `launchctl unload` + deletes the plist.

### Rule 4 — STATE.YAML IS SOURCE OF TRUTH

If `projects/<slug>/state.yaml` is missing or corrupt → tick exits with an error. It does NOT attempt to reconstruct, guess, or recover. The user's in-progress work is too valuable to overwrite from a half-loaded state.

Initialize state via `anchor_memory.py init <slug>` BEFORE enabling agent_tick.

### Rule 5 — PER-PROJECT DAILY COST CEILING

(v1.1 enforcement; v1 reports only.) Paid-API costs compound silently across days. Each tick must check:

```python
# Pseudocode for v1.1
if cost_gate.project_daily_spend(slug) + estimated_cost > daily_cap:
    mark_blocked(phase_id, "would exceed daily cost cap")
    exit
```

In v1, agent_tick writes wake-reports that estimate cost; the user reads them and decides. v1.1 will enforce automatically via `cost_gate.py` extension.

---

## How a tick proceeds

```
launchd fires →  agent_tick run --project <slug>
                  ↓
              Load projects/<slug>/state.yaml (FAIL → exit)
                  ↓
              Check enabled registry (NOT REGISTERED → exit)
                  ↓
              Read task_queue.next_pending(slug)
                  ↓
              Identify the next phase (deps satisfied? else exit)
                  ↓
              Load sovereign memory + anchors for this phase
                  ↓
              [v1] Write wake-report → exit (user reviews + fires manually)
              [v1.1] Invoke autopilot with phase instructions
                     ↓
                 Phase succeeds → task_queue.mark_done()
                 Phase blocks   → task_queue.mark_blocked()
                 Phase errors   → log + exit (do NOT retry on same tick)
                  ↓
              Emit ledger
                  ↓
              Exit (max one phase advanced per wake)
```

---

## What agent_tick is NOT

- NOT a background daemon. Each tick is a one-shot launchd-fired invocation that exits.
- NOT a fully autonomous coder. It coordinates the chain; the chain still does the work; the user still owns taste.
- NOT a way to skip Phase 2.5 gates from other workflows (e.g., /verticalize). Tick advances a phase that's been pre-approved by being in pending.jsonl; gates inside that phase still fire.
- NOT a substitute for cost_gate. Paid API spend still flows through the standard gate; agent_tick just enforces a daily cap on top.

---

## Recovery & debugging

- **Stuck blocked queue**: `task_queue.py list <slug>` shows all blocked phases with reasons. Unblock via `task_queue.py unblock <slug> <phase_id>`.
- **Bad wake-report**: wake-reports archive to `_active/_ledgers/agent-tick-<slug>-<datetime>.md`. Diff between consecutive ticks shows what state changed.
- **Runaway suspicion**: `agent_tick.py status --project <slug>` shows tick count + last outcome. If ticks_executed grows fast unexpectedly, run `disable --project <slug>` immediately.
- **Disable everything**: `cat .agent/agent-tick-enabled.json | jq 'keys'` → loop disable each one.

---

## Appendix A — launchd plist template

Save as `~/Library/LaunchAgents/com.antigravity.agent-tick.<slug>.plist` (replace `<slug>` and `<absolute-project-path>`):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.antigravity.agent-tick.<slug></string>

    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/farricecain/Google Antigravity/execution/agent_tick.py</string>
        <string>run</string>
        <string>--project</string>
        <string><slug></string>
    </array>

    <key>WorkingDirectory</key>
    <string>/Users/farricecain/Google Antigravity</string>

    <!-- Run daily at 6am local. Adjust as needed. -->
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>6</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>

    <key>StandardOutPath</key>
    <string>/Users/farricecain/Google Antigravity/.agent/agent-tick-<slug>.log</string>

    <key>StandardErrorPath</key>
    <string>/Users/farricecain/Google Antigravity/.agent/agent-tick-<slug>.err</string>

    <!-- KEY: do NOT set RunAtLoad=true. Agent_tick should only fire on
         the schedule, not on every system boot. -->
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
```

After saving, install with:
```bash
launchctl load ~/Library/LaunchAgents/com.antigravity.agent-tick.<slug>.plist
launchctl list | grep agent-tick   # verify
```

To run once on-demand (bypass schedule):
```bash
launchctl start com.antigravity.agent-tick.<slug>
```

To remove:
```bash
launchctl unload ~/Library/LaunchAgents/com.antigravity.agent-tick.<slug>.plist
rm ~/Library/LaunchAgents/com.antigravity.agent-tick.<slug>.plist
```

---

## Appendix B — Migration from manual sessions

If you've been running a multi-day project as a series of manual sessions, you can convert to agent_tick:

1. Make sure `projects/<slug>/state.yaml` exists (via `anchor_memory.py init <slug>` if needed).
2. List remaining phases as `task_queue.py enqueue` calls — one per phase, with `--depends-on` to chain them.
3. `agent_tick.py enable --project <slug>` to register.
4. (Optional) Install the launchd plist per Appendix A.
5. Run `agent_tick.py run --project <slug>` manually first to confirm the dry-run output looks right.

---

## v1 → v1.1 roadmap (deferred work)

- **Full execution mode**: `agent_tick.py run --execute` fires the phase via autopilot, captures the outcome, calls `task_queue.mark_done` or `mark_blocked` based on chain_runner result.
- **Cost gate per-project ceiling**: `cost_gate.py` extension that tracks per-project daily spend and blocks ticks that would exceed it.
- **Notification on block**: when a tick blocks, send a macOS notification (`osascript -e 'display notification ...'`) so the user knows to unblock.
- **Multi-user support**: per-user opt-in + isolated registries (currently single-user only).
- **Tick frequency throttle**: prevent more than 1 tick/hour per project regardless of launchd schedule (defense-in-depth against rogue plists).
