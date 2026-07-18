---
description: "/cos weekly — the Standing Board's weekly session: all 5 seats + tight-mode wildcards through /convene structure (Diverge → Deliberate → Synthesize), outputs focal question consensus, dissent, trust update, 3 commitments with review dates."
---

# /cos weekly — Standing Board Session

## Pre-Flight

1. Read `skills/chief-of-staff-os/genius.md` (voice + capture discipline).
2. `python3 execution/cos_prep.py status` — if `weekly_due: false`, confirm he wants an early board ("Board sat N days ago — run it anyway?").
3. **Weekly pack:** assemble or dispatch a subagent to digest into a ≤1-page pack: last 7 days of `.agent/cos/journal/*.md`, threads via `handoff_store.py`, `.tmp/weekly-pulse/` (if <7d old), `.agent/cos/goals.json`, open items in `decisions.md`, `revenue_tracker.py due` + `pipeline` outputs. If subagent fails, proceed on raw files — never block.

4. **Focal question (user input).** Ask: *"What's the one question the board should deliberate this week?"* Capture his one-liner; this sets the frame.

🔒 **Gate:** genius.md loaded; board.md confirmed (reconfirm seats if `status: unconfirmed`). Writes stay under `.agent/cos/`.

## Workflow — /Convene Structure (Three Phases)

The weekly board runs via the **collective-genius-council** structure (Diverge → Deliberate → Synthesize), dispatching one Agent run per phase to orchestrate all 5 seats + wildcards in parallel where possible.

**Phase 1 — Diverge (Unpack the focal question).**

Dispatch five seat sub-agents (parallel):
- **CEO (Spine)**: What is the ONE move that matters this week toward the focal question? Cost of delay?
- **CFO (Risk Gate)**: Money truth this week — actual vs targets, Incumbency Rule, collected-cash enforcement.
- **COO (Mechanism)**: What's broken or drifting? Threads sorted into advancing/maintenance/drift; recommendations for each drifting one.
- **Chairman (Craft)**: Life truth this week — life sections in staleness order; heavy stuff acknowledged + parked or deepened, never tasked.
- **Mentor (Differentiator)**: What capability expansion or strategic principle applies to this week's focal question? One real frame applied to the operator's situation.

Each seat delivers its position (≤150 words). Rotate in 2–3 tight-mode wildcards pulled via council_cast.py if specialists are high-fit (e.g., Ali Abdaal for action-bias diagnosis, Daniel Priestley for demand/pipeline). Wildcards sit as observers/sharers, not separate seats.

**Phase 2 — Deliberate (Synthesize across seats).**

Single run (main thread or one orchestrating Agent):
- **Consensus** — Where do all five seats agree on the week's priority?
- **Dissent** — Where do they disagree? Preserve the strongest disagreement without averaging it out.
- **Solution Cards** — List cards under `docs/solutions/` dated within the last 7 days (spaced repetition): `[card name] — [problem_signature]`, one per line.
- **Trust Update** — Which seat's prior calls proved right/wrong/partial this week? Update confidence in their mandate for next week.

Output: a ≤2-page deliberation block appended to `.agent/cos/board-ledger.md` under `## Weekly Sessions / YYYY-MM-DD — [focal question]`.

**Phase 3 — Synthesize (Commitments).**

CEO close + owner voice:
1. Review **LAST week's 3 commitments** from `decisions.md`: each is done / carried (say why) / dead.
2. Propose **3 NEW commitments for the coming week**, synthesized from Diverge + Deliberate (CEO prioritizes, CFO enforces urgency, COO threads them, Chairman checks life). Each commitment has a review date.
3. Append finalized set to `decisions.md` under `## Weekly Commitments / ### YYYY-MM-DD — Week of [date]`.
4. Update `goals.json` `last_reviewed` for every goal discussed.

## Ledger Entry (Deterministic)

Append to `.agent/cos/board-ledger.md` under `## Weekly Sessions`:

```
### YYYY-MM-DD — [focal question]
**Members:** CEO (Justin Welsh) · CFO (Alex Hormozi) · COO (Dan Martell) · Chairman (Dr.K) · Mentor (Robert Greene) [+ Specialist/Wildcards if sat]
**Positions:** [one line per seat, from Diverge]
**Consensus:** [main alignment on the focal question]
**Dissent:** [strongest disagreement, if any — never blended away]
**Outcome:** [from Commitments: 3 items with review dates]
**Trust Update:** [which seat's calls proved right/wrong; reweight if needed]
```

## Capture & Close

Capture per genius.md discipline:
- Life sections touched → update + restamp in `life-context.md`
- Durable facts → sovereign memory (valid categories)
- Heavy stuff logged → journal `## Raw` (verbatim)
- Open loops resolved → remove from journal `## Open loops`; unresolved ones age another week
- New-offer drift → journal `## Parked` (CFO line, one sentence)

Then: `python3 execution/cos_prep.py mark weekly` (and `mark daily` if not yet done today).

**Final check:** Are the 3 commitments with review dates actually in `decisions.md`? Did `last_reviewed` flip for all goals touched?

## Output Schema

Two artifacts, both required — a weekly session that produces one without the other is
incomplete:

1. **The board-ledger deliberation block** — appended verbatim under `## Weekly
   Sessions / YYYY-MM-DD — [focal question]`, carrying exactly the Ledger Entry
   template above (Members / Positions / Consensus / Dissent / Outcome / Trust
   Update) — no field skipped; a seat that didn't sit gets a named reason, not a
   blank.
2. **The decisions.md commitment set** — under `## Weekly Commitments / ###
   YYYY-MM-DD — Week of [date]`, exactly 3 new commitments, each with a review date,
   preceded by last week's 3 commitments each marked done/carried/dead with a reason.

Dissent is a required field, not optional flavor: if Phase 2 genuinely produced no
disagreement, the block says "no dissent this week" explicitly — it is never silently
omitted, since an omitted Dissent field is indistinguishable from a forgotten one.

## Quality Gate

✓ Focal question captured and deliberated (not skipped)
✓ All 5 seats delivered a position (or explicit reason why seat didn't sit)
✓ Last week's 3 commitments reviewed with done/carried/dead verdict on each
✓ 3 NEW commitments appended to `decisions.md` with review dates
✓ Consensus + Dissent logged in board-ledger.md (not averaged away)
✓ Trust Update recorded (seat performance vs mandate)
✓ Solution Cards resurfaced (≤7 days old, spaced repetition)
✓ Life-context sections refreshed + stamped for everything touched
✓ `goals.json` `last_reviewed` updated for discussed goals
✓ `mark weekly` ran
✓ All writes under `.agent/cos/`
✓ Session feel ≤20 min (Diverge dispatch + synthesis rounds count as the bulk)
