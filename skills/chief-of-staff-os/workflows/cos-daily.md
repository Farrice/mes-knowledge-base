---
description: "/cos daily — the 2-minute micro briefing: present the morning brief, ask the 3 tailored questions, capture whatever comes back, one CEO-seat close. First run ever routes to the Onboarding path below."
---

# /cos daily — Micro Briefing

## Pre-Flight

1. Read `skills/chief-of-staff-os/genius.md` (voice rules + capture discipline).
2. `python3 execution/cos_prep.py status`
   - `first_run: true` → jump to **Onboarding path**.
   - `daily_done: true` → "Already checked in today (streak N). Want `/cos status` instead?" STOP.
   - `brief_exists: false` → self-heal: `python3 execution/cos_prep.py prep`, then continue.

🔒 **Gate:** genius.md loaded; status JSON read. All writes this session stay under `.agent/cos/` (sole exception: `cos_prep.py capture --route inbox` for creative sparks).

## Workflow

**Step 1 — Present the brief.** Read `.agent/cos/briefs/YYYY-MM-DD.md` (today). Render it verbatim — it's pre-formatted and ≤20 lines. Then the three questions, all in one message, closing with: *"Answer any, all, or just brain-dump — raw is fine."*

**Step 2 — Capture what comes back** (per genius.md Capture Discipline). If the answer
is a mixed dump, apply the **Detangle Rule first**: name the separate things back to him,
numbered with destinations, before routing. Then:
- Verbatim → `journal/YYYY-MM-DD.md` under `## Raw` (Write tool; create file with `# Journal — date` header if missing).
- Durable facts → `python3 execution/memory_store.py store --tier semantic --category insight --content "..." --meta '{"domain":"founder-context","source":"cos"}'` (category `preference`/`pattern` where apt).
- Life sections touched → update the section in `life-context.md` + restamp `<!-- updated: YYYY-MM-DD -->`.
- Creative sparks only → `python3 execution/cos_prep.py capture --route inbox --text "..."`.
- Goal-relevant statements → `goals.json`. New-offer ideas → journal `## Parked` (CFO: cite Incumbency Rule, one sentence, no debate).
- Unresolved threads → journal `## Open loops` (feeds tomorrow's questions).

If he skips or gives one line: capture the line, no interrogation, proceed.

**Step 3 — The Counsel Close** (upgraded 2026-07-08 — Farrice: "I thought I would be getting more mentorship or guidance... real support or next steps"). Three parts, ≤6 lines total, all grounded in what he just said:
1. **CEO line** — one sentence connecting today to the active goal.
2. **One mentor insight** — teach him something real that expands capability: a frame, a mechanism, a principle drawn from the expert stack and applied to HIS situation today. Not a platitude; something he could not have said himself this morning.
3. **One load-lift** — name the thing he can stop holding in his head because the system now carries it ("Josh follow-up date is in the loop file — off your mind until Friday").

Logging without guidance = failed session. No lecture, no task list he didn't ask for — but never capture-and-run silent either.

**Step 4 — Close.** `python3 execution/cos_prep.py mark daily`. Then, only what's relevant:
- Content spark with legs captured? Name its ONE container and stop (genius.md One Container rule): "`/linkedin-daily`" / "`/parallax`" / "`/writers-room`". Never write the content inside the briefing.
- "Working today? `/daily-focus` for the block plan."
- If status showed `weekly_due: true`: "Board's also due — `/cos weekly` when you've got 15."

## Onboarding path (first run only)

Frame it: *"First session — I'm going to interview you for ten minutes so I never have to ask generic questions again."* Then:
1. Walk the five life-context sections (JJ → Jen & Family → Health → Mindset → Creative), 1-2 open questions each. Write each section + stamp as you go.
2. Confirm the three seeded goals in `goals.json` (read them aloud, plain language) — edit/add per his answers (health goal is a known candidate). Set `last_reviewed` = today on confirmed ones.
3. Ask how he wants the counsel to speak to him when he's drifting (capture as `--category preference`).
4. Durable facts → sovereign memory per Capture Discipline. Everything verbatim → journal.
5. `python3 execution/cos_prep.py mark daily` and `mark weekly` (onboarding counts as both), then `prep --force` so tomorrow's questions use the fresh stamps.

## Quality Gate

Journal written · durable facts in sovereign memory (valid categories) · touched sections restamped · `mark daily` ran · zero writes outside `.agent/cos/` (except sanctioned inbox mirror) · total feel ≤2 min (onboarding ≤10).
