---
date: 2026-07-13
session: guide-library-backfill
tier: operator-guide
status: enriched
---

# Chief of Staff OS — What We Built 2026-07-02 and How to Use It

> A standing CEO/CFO/COO/Chairman counsel that does the homework before you sit down: a ~2-minute daily briefing that asks YOU tailored questions, a ~15-minute weekly board session, an on-demand state of the union, and `/dump` — the anytime pressure valve for tangled thoughts. Skill: `skills/chief-of-staff-os/` · deterministic prep: `execution/cos_prep.py` · private state: `.agent/cos/` (gitignored).

## ⚡ If you only read 10 lines

- Bare `/cos` auto-routes: it runs `python3 execution/cos_prep.py status` and picks onboarding / daily / weekly / status for you. You never have to remember which is due.
- Explicit overrides: `/cos daily` · `/cos weekly` · `/cos status`.
- Daily = 2-min pulse: brief + 3 tailored questions (JJ, Jen/family, health, mindset, creative — driven by staleness stamps) + capture + one CEO line.
- Weekly = 15-min board: 4 seats, revenue vs targets, Incumbency Rule, thread drift, **exactly 3 commitments with review dates**.
- `/dump` = throw any tangled blob at it, any hour. It captures verbatim, visibly detangles, routes each piece, and OFFERS the next step — never performs it.
- Close every daily/weekly with `python3 execution/cos_prep.py mark daily|weekly` — that's what silences the nudge and keeps staleness honest.
- All state lives in `.agent/cos/` — gitignored; the family/health journal never commits.
- Creative sparks are the only thing that leaves: `python3 execution/cos_prep.py capture --route inbox --text "..."` mirrors to the thought-bank inbox.
- Memory writes use valid categories only: `--category insight|preference|pattern` — custom categories silently fail.
- Morning prep is launchd (`com.antigravity.cos-prep`, daily 06:45), no LLM — the brief is waiting before the session opens.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/cos` | The right session, auto-routed | Any time — the default |
| `/cos daily` | 2-min pulse: brief + 3 questions + capture + one CEO line | Every day |
| `/cos weekly` | 15-min board session: 4 seats, 3 commitments w/ review dates | Weekly (Monday default) |
| `/cos status` | ≤1-page state of the union, read-only | "Where am I?" moments |
| `/dump` | Anytime capture: visible detangle + routing, 30-sec feel | Tangled thought, any hour — never pre-sort it yourself |
| `python3 execution/cos_prep.py status` | Routing JSON (first_run / daily_done / weekly_due / nudge) | Debugging routing or checking cadence state |
| `python3 execution/cos_prep.py mark daily\|weekly` | Silenced nudge, honest staleness stamps | Closing every daily/weekly |

## The mental model

1. **The counsel holds context so you don't have to.** The whole system exists because cognitive overload makes threads blend and bounce. Staleness stamps drive which questions get asked, so context rot self-surfaces instead of silently accumulating.
2. **It asks, never reports.** The daily is the system interviewing YOU — 3 questions picked by what's gone stale — not a dashboard you read. The Chairman seat asks about JJ, Jen, health, mindset; it never lectures.
3. **Compass, never cage.** The counsel flags with one line and a named tradeoff, then executes fully. "Parked" means a retrievable shelf, never a gate (binding, 3rd correction 2026-07-11).
4. **One Container.** A capture or briefing session names the next engine (`/linkedin-daily`, `/parallax`, `/writers-room`) — it never does the work inside itself.

## The Four Seats (who speaks when)

| Seat | Owns | Speaks up when |
|---|---|---|
| **CEO** | Focus, priorities, the one thing today | Every daily close — one sentence, never a lecture |
| **CFO** | Revenue vs targets, Incumbency Rule | Weekly; instantly on any new-offer/repositioning drift |
| **COO** | Threads, projects, open loops | Weekly; names drift, recommends kill/park |
| **Chairman** | JJ, Jen/family, health, mindset | Daily questions; weekly life review |

## Capability 1: `/cos` — the routed briefing surface

**What it is.** A deterministic router over four workflows (`cos-daily.md`, `cos-weekly.md`, `cos-status.md`, plus the onboarding path). Routing order from the status JSON: `first_run: true` → onboarding interview · `daily_done: false` → daily (self-heal: if `brief_exists: false`, run `cos_prep.py prep` first) · `weekly_due: true` → offer weekly · otherwise → status.

**When to reach for it.** Start of day, start of week, or any "where am I?" moment. The auto-route means bare `/cos` is always correct.

**When NOT to.** Work-block planning (`/daily-focus` owns that), the weekly metrics ritual (`/weekly-pulse` output gets read, not rerun), or `/weekly-closeout` (surfaced, not executed). The counsel composes with these; it never absorbs them.

**How to invoke.** `/cos`, or explicit `/cos daily` / `/cos weekly` / `/cos status`. Load `genius.md` before any workflow — the voice rules there are not optional.

**Honest edges.** The weekly's value depends on you closing with `mark weekly` — skip it and the nudge logic and staleness stamps drift. The first `/cos` run is an extended onboarding interview (populates life-context, confirms seeded goals); until that's done the tailored questions run on seed data.

## Capability 2: `/dump` — the anytime pressure valve

**What it is.** Raw-thought capture with the **Detangle Rule**: the counsel visibly decomposes your blob into numbered pieces with destinations (thought-bank, memory, open loops, parked, goals) before routing anything — because blended threads are the core failure mode it exists to counter. Then it offers, never performs, the next step.

**When to reach for it.** Any tangled thought at any hour. Don't pre-sort — throwing the mess at it as-is IS the correct usage.

**When NOT to.** A single clean content spark that needs no detangling can go straight to the sink: `python3 execution/thought_bank.py capture "<text>" --theme <t> --source dump` (skips the journal mirror entirely).

**How it lands (deterministic spine, 2026-07-06).** The capture call delegates to `execution/thought_bank.py capture` under the hood — one writer, one entry format, plus a mirror into the sovereign episodic tier so fragments flow into the weekly distill pipeline. **Nightly backstop:** `execution/harvest_memory_daily.py` scans the last 24h of episodic exchanges for user turns opening with `/dump`, `thought:`, `note to self`, or `capture this` and appends anything missed (deduped by normalized first-60-chars). Even a dump where the capture call got skipped mid-conversation still lands.

## Hard rules (memorize these four)

1. All file writes stay under `.agent/cos/`. Only creative sparks mirror out, via `cos_prep.py capture --route inbox`. Personal/family raw NEVER leaves the journal.
2. Memory writes: `python3 execution/memory_store.py store --tier semantic --category insight|preference|pattern --content "..." --meta '{"domain":"founder-context","source":"cos"}'` — invalid categories fail silently.
3. Close sessions with `cos_prep.py mark daily|weekly`.
4. Extend this system, never rebuild a founder-briefing or goal-tracking engine beside it.

## Composition options (never forced wiring)

| Stacks with | When it earns its cost |
|---|---|
| `/daily-focus` | After the daily, when the day needs work blocks |
| Thought-bank + memory facade | Automatic — dump routing feeds both |
| `/weekly-closeout` | The weekly board can surface it as due; you run it |
| Solution Cards digest | COS weekly digest resurfaces `docs/solutions/` cards |
