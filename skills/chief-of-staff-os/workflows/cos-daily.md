---
description: "/cos daily — the Standing Board's daily sitting: 3 advisors cast by situation fit, dispatch in parallel, compose Operator Primer, gate quality, retry on fail (≤2), then capture + close. First run routes to Onboarding."
---

# /cos daily — Standing Board Daily Sitting

## Pre-Flight

1. Read `skills/chief-of-staff-os/genius.md` (voice rules + capture discipline).
2. `python3 execution/cos_prep.py status`
   - `first_run: true` → jump to **Onboarding path** (unchanged from prior).
   - `daily_done: true` → "Already checked in today (streak N). Want `/cos status` instead?" STOP.
   - `brief_exists: false` → self-heal: `python3 execution/cos_prep.py prep`, then continue.

3. **Board confirmation gate** (one-time, day 1 only): if `board.md` has `status: unconfirmed`, surface the seat staffing for sign-off and flip to `confirmed: YYYY-MM-DD` (no re-prompt on day 2+).

🔒 **Gate:** genius.md loaded; status JSON read; board.md confirmed. All writes this session stay under `.agent/cos/` (sole exception: `cos_prep.py capture --route inbox` for creative sparks).

## Workflow — Three Steps

**Step 1 — Cast the Board (deterministic, $0).**
```bash
python3 execution/cos_board_cast.py --brief .agent/cos/briefs/YYYY-MM-DD.md
```
Returns JSON with 3 selected advisors (`{advisors: [{seat, name, genius_path, mandate, ledger_lines}], situation, mode}`). Daily mode = 2 most-relevant staffed seats + 1 rotating specialist.

**Step 2 — Dispatch Advisors (parallel, ≤3 Sonnet sub-agents).**

For each advisor, dispatch a sub-agent with:
- **Persona**: Load `[genius_path]/AGENT.md` + top 3 skill files from the expert's directory
- **Bundle** (privacy-gated): `.agent/cos/goals.json` · top threads via `handoff_store.py` · `## Open loops` from journal · outer-loop numbers + due items · gated world pulse · advisor's own `board-ledger.md` lines (own seat only)
- **Task contract** (≤120 words): *What I see* (≤2 sentences, ≥1 concrete item) / *The move* (ONE, with a startable next step) / *Risk* (1 line) / *Callback* (last advice → followed/ignored/partial, or "first sitting")
- **Input**: the situation string from Step 1

Dispatch all three advisors in parallel. Wait for completion.

**Step 3 — Compose Operator Primer (main thread).**

Owner (Chief of Staff voice) reads the three advisories and composes the Operator Primer:
- **Today's 3 moves** — synthesize from the situation + outer-loop + advisories; must be already-finished work (never "build X"); each move has `→ next:` startable command
- **Delta since yesterday** — how the situation changed 24 hours; brief, 2-3 sentences
- **Board advisories** — attribute each `[Seat: Name]` exactly as written; do NOT edit, only attribute and order
- **Your questions** — from the brief (unchanged); each has `↳ context` line
- **World pulse** — from the brief; if zero items cleared the bar, render "nothing cleared the bar today"
- **Outer loop** — from the brief; list due items with per-item close command
- **Composition footer** — one line: who sat, who skipped and why

Read the prompt contract at `skills/chief-of-staff-os/references/prompts-v2/operator-primer-output.md` (see Phase 5 wiring note below).

**Step 4 — Quality Gate (deterministic, $0).**
```bash
python3 execution/cos_primer_gate.py check --text "[primer text]"
```
Exit 0 = PASS. Exit 2 = FAIL (JSON with failure codes).

**On PASS:** proceed to Step 5.

**On FAIL:** recompose the primer with the failure JSON injected (at most **2 retries**, main-thread only; no new sub-agents). Track retry count. After 2 failures, ship the primer with a `[DEGRADED]` banner naming the failures and why.

**Step 5 — Capture & Close.**

Capture per genius.md Capture Discipline:
- Operator's live-session thoughts (if offered) → journal `## Raw`
- Durable facts → sovereign memory (valid categories)
- Touched life sections → update + restamp
- Creative sparks → `cos_prep.py capture --route inbox`
- Open loops → journal `## Open loops`

Then: `python3 execution/cos_prep.py mark daily`. Close with only what's relevant:
- If a creative spark surfaced: name its ONE container (e.g., "`/parallax`") and stop.
- "Working today? `/daily-focus` for the block plan."
- If status shows `weekly_due: true`: "Board's full form is due — `/cos weekly` when you've got 15."

**Step 6 — Ledger (deterministic).**

Append a one-line Daily Advisory entry to `.agent/cos/board-ledger.md` under today's date:
```
### YYYY-MM-DD
- [Seat: Name]: <the move> | callback: <followed/ignored/partial/first sitting>
```
(Callback line is for next sitting's advisor—it tracks whether Farrice acted on today's advice.)

## Onboarding path (first run only)

Frame it: *"First session — I'm going to interview you for ten minutes so I never have to ask generic questions again."* Then:
1. Walk the five life-context sections (JJ → Jen & Family → Health → Mindset → Creative), 1-2 open questions each. Write each section + stamp as you go.
2. Confirm the five seat staffing in `board.md` (read the charter aloud) — edit per his preference. Set `status: confirmed: YYYY-MM-DD` in the charter.
3. Confirm the three seeded goals in `goals.json` (read them aloud, plain language) — edit/add per his answers. Set `last_reviewed` = today.
4. Ask how he wants the counsel to speak to him when he's drifting (capture as `--category preference`).
5. Durable facts → sovereign memory per Capture Discipline. Everything verbatim → journal.
6. `python3 execution/cos_prep.py mark daily` and `mark weekly` (onboarding counts as both), then `prep --force` so tomorrow's questions use the fresh stamps.

## Quality Gate

✓ Primer gate passed (or shipped with DEGRADED banner if retry budget exhausted)
✓ All three advisories attributed `[Seat: Name]` 
✓ Each advisory follows the ≤120-word contract (What I see / The move / Risk / Callback)
✓ Every move in Today's 3 has a `→ next:` startable command
✓ World pulse shows "nothing cleared the bar" (not omitted) if no items qualified
✓ Outer-loop items listed with per-item close commands
✓ Ledger entry appended with the day's moves + callback marker
✓ `mark daily` ran
✓ All writes under `.agent/cos/` (except inbox mirror)
✓ Session feel ≤5 min (dispatch → gate → compose takes most time; capture fast)
