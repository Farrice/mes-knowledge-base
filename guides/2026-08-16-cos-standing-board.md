---
date: 2026-08-16
session: cos-standing-board
tier: operator-guide
status: enriched
---

# COS Standing Board — What We Preserved 2026-08-16 and How to Resume It

> This guide preserves the intended COS v3 advisory experience and the current truth of the prototype. The board charter, July primer, deterministic quality gate, and regression tests remain. The board-casting adapter previously reported as built is missing, and daily/weekly workflow wiring plus fresh human acceptance remain unfinished. Canonical continuation: `.agent/handoffs/2026-08-16-cos-standing-board.md`.

## ⚡ If you only read 10 lines

- The job is not “make the brief prettier”; it is “give Farrice a standing expert board that did the homework.”
- Keep the existing COS gather/state/journal/goals engine. Replace only the counsel experience.
- Daily design: two relevant fixed seats plus one rotating specialist, each bounded to 120 words.
- Weekly design: all five seats in a deeper deliberate-and-synthesize sitting.
- Fixed seats are Justin Welsh, Alex Hormozi, Dan Martell, Dr. K, and Robert Greene.
- The owner must reconcile the advice into one useful primer; Farrice should never receive expert soup.
- `execution/cos_primer_gate.py` checks the primer for echo, missing actions, weak context, stale links, and prose failures.
- `python3 execution/verify_cos_primer_gate.py` is the regression check; it currently preserves eight named failure cases.
- `execution/cos_board_cast.py` is missing. Do not claim automated expert casting works until it is restored or replaced and verified.
- Resume with `/resume cos-standing-board`; the next proof is one fresh August `/cos` briefing and Farrice's keep/change/scrap verdict.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `/resume cos-standing-board` | Exact mid-build handoff and current next action | Restarting this work in a fresh task |
| `python3 execution/verify_cos_primer_gate.py` | Golden regression result for the primer gate | Before and after changing the quality bar |
| `python3 execution/cos_primer_gate.py check --file <primer.md>` | PASS/FAIL receipt with specific failure codes | Checking a composed Operator Primer |
| `python3 execution/cos_primer_gate.py check --file <primer.md> --offline` | Same structural checks without live URL requests | Network is unavailable or links are intentionally deferred |
| `/cos` | Current Chief of Staff entry point | Only after the next session verifies whether Standing Board wiring is actually live |

## The mental model

### 1. Gathering and counsel are different systems

The existing COS engine is useful at collecting goals, threads, journal context, staleness, and revenue-loop signals. Its failure was at the reader surface: it replayed stored information instead of turning that information into expert judgment. Rewriting storage would discard the part that worked. The repair boundary is the counsel layer.

### 2. A board is not several expert paragraphs

The board earns its cost only when each seat changes the recommendation. Each advisor gets one bounded contribution: what they see, one move, one risk, and a callback to prior advice. The Chief of Staff remains the sole composer. It reconciles agreement and dissent, ranks the move, and produces one readable primer.

### 3. Machine quality and human usefulness are separate

The primer gate can catch known structural failures cheaply. It cannot prove that the mentoring feels useful to Farrice. The promotion sequence is therefore: deterministic PASS, then one cold human reading, then keep/change/scrap. A gate result must never be reported as acceptance.

## Capability 1: Standing Board charter

### What it is

`.agent/cos/board.md` defines five functional seats staffed by named experts: CEO/Justin Welsh, CFO/Alex Hormozi, COO/Dan Martell, Chairman/Dr. K, and Mentor/Robert Greene. It also defines the rotating-specialist role, privacy allowlist, daily and weekly limits, and the required advisory shape.

### When to reach for it

Use it when deciding who is allowed to advise, what each seat owns, what context may enter advisor prompts, and how much daily depth is affordable.

### When not to

Do not use the charter as proof that the board runs. It is a design authority, not runtime evidence.

### Worked example

The July primer seated Hormozi, Greene, and a specialist. All three independently identified the same operating pattern: completed assets were accumulating while outbound decisions remained unmade. The owner synthesized that into a send-first recommendation instead of presenting three unrelated essays.

### Honest edges

The charter still references `execution/cos_board_cast.py`, but that file is absent at this closeout. Staffing was confirmed in July, yet the current runtime path must be re-proven against today's repository rather than assumed from the charter.

## Capability 2: Operator Primer proof

### What it is

`.agent/cos/primers/2026-07-14.md` is the preserved proof of the target reading experience: a ranked scoreboard, three startable moves, attributed expert advisories, context-carrying questions, an honestly suppressed world pulse, and an actionable outer loop.

### When to reach for it

Use it as the preservation example when repairing the workflow. New work may improve it, but should not regress to a journal recap, dead links, generic questions, or unattributed expert output.

### When not to

Do not treat its dated sprint numbers or recommendations as current. It is a format and behavior reference from July 14, not an August briefing.

### Honest edges

It passed the local gate after one bounded retry. It did not receive a final human acceptance verdict before the work stopped. Its usefulness is therefore `UNCONFIRMED`, not proven.

## Capability 3: Deterministic primer gate

### What it is

`execution/cos_primer_gate.py` evaluates a primer without asking another model to grade itself. It checks for known failure modes including journal echo, missing executable moves, missing expert attribution, questions without inline context, stale or invalid world-pulse material, and prose problems. `execution/verify_cos_primer_gate.py` pins the known cases as regression fixtures.

### How to use it

Run the golden set first:

```text
python3 execution/verify_cos_primer_gate.py
```

Then check a real primer:

```text
python3 execution/cos_primer_gate.py check --file .agent/cos/primers/YYYY-MM-DD.md
```

If it fails, inject the exact failure notes into one recompose attempt. Stop after two retries. A third miss should ship only with an honest degraded label, not an infinite token loop.

### Honest edges

The gate protects known scars. It cannot judge whether an expert genuinely embodied their source material, whether the ranked move is strategically right, or whether Farrice feels mentored. Those remain composition and human-acceptance checks.

## Resume sequence

1. Load `.agent/handoffs/2026-08-16-cos-standing-board.md` and the seven core paths named there.
2. Find why `execution/cos_board_cast.py` disappeared: history, supersession, or incomplete merge. Preserve evidence before rebuilding.
3. Restore or replace the smallest casting adapter and add a verifier that proves daily and weekly seat selection.
4. Wire the canonical `skills/chief-of-staff-os/workflows/cos-daily.md` and weekly workflow to compose, gate, and bound retries.
5. Generate one current August primer from live state.
6. Ask Farrice for one direct verdict: keep, change, or scrap. Do not expand the system before that verdict.

## What stays parked

- More seats, more advisor depth, or autonomous morning model spend.
- Promoting the Standing Board into a broader reusable skill system.
- Treating World Pulse, outcome check-ins, or the board ledger as solved merely because they appear in the primer.
- Git synchronization from the current dirty `main` tree.

