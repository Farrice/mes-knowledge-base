---
date: 2026-07-13
session: maestro-layer
tier: operator-guide
status: enriched
---

# The Maestro Layer — What We Built 2026-07-13 and How to Use It

> One session, five pieces: `/go` v2 with Mission Cards, the orchestration doctrine (Conductor Ladder + pattern table + autonomy tiers), a physical session lock, the `/pulse-board` operator console, and `/voice-over`. Plus one binding guard on the taste ratchet. Sources: `directives/orchestration-doctrine.md` · `.agent/workflows/go.md` · handoff pin `.agent/handoffs/2026-07-13-maestro-os.md`. Standing rule: **extend, never rebuild** any of these.

---

## The mental model (read this once, everything else follows)

Before this session the system had world-class parts and door-picking as the operating experience: which of ~140 commands, which orchestration shape, how much autonomy — all decided per session, by whoever was driving, from memory. That made pattern choice session luck. The Maestro layer turns it into system property, with three ideas:

1. **One front door, one card.** Any raw thought goes into `/go`, which compiles it into a Mission Card — intent, which standing goal it serves, orchestration pattern, what loads, which gates fire, blast-radius tier. The card is the contract; the conductor executes it.
2. **The law lives in a file, not a model.** `orchestration-doctrine.md` banks the frontier judgment from the Renaissance and Wiring arcs so *any* model in the conductor seat orchestrates the same way. Roles, not models: the conductor holds judgment, gating, and commits; Sonnet-class executors do the grind.
3. **Rules become mechanisms.** "One driver per tree" was documentation until three concurrent-session collisions; now it's `session_lock.py` and the queue builders physically refuse to run without a token. Same move as the cost gate: a rule in a mechanism can't be violated by accident.

---

## 1. `/go` v2 — the podium and the Mission Card

### What it is

The Maestro front door. `/go "<messy thought>"` runs a silent compile: DICE-scores the thought (score >= 3 means zero questions; <= 2 gets ONE round on only the missing dimensions), reads `.agent/cos/goals.json` to name which standing goal the mission serves (no match = `ORPHAN ⚑` — one flag line, compass never cage, then full execution), picks the primary orchestration pattern from the doctrine table with a one-line reason, and classifies blast radius T1/T2/T3. Output is the card:

```
MISSION CARD
Intent: <sharpened one-liner>            Serves: <goal-id | ORPHAN ⚑>
Pattern: <doctrine row> — <one-line reason>
Loads: <experts/skills + the v2 prompts whose contracts govern output>
Gates: <audit / prose / verify / jam / voice — whichever will fire>
Tier: <T1 auto | T2 waiting | T3 waiting>   Cost: <$0 | flagged>
```

T1 missions show the card as they start; T2/T3 wait for your nod. Then Stage 1 hands the mission to exactly one conductor (`/create`, `/supercomputer`, `/jw-engine`, the workflow engine, `/convene`, `/wargame-run`, `/autopilot`, `/system-audit`, `research.py`/`/swarm`, or `/voice-over`), and Stage 2.5 appends one JSONL line to `.agent/missions.jsonl` at compile AND at close — the pulse board and COS read from that log.

### When to reach for it

- Default entry for any substantive ask. If you'd otherwise be picking a door, don't — `/go` picks it and shows its work.
- Especially when the thought is messy: `/go` never returns a bare clarifying question when it can propose an answer.

### When NOT to

- Pure system commands and trivial follow-ups inside an already-running mission — the conductor owns its own sequence; `/go` stages the engine, it doesn't re-implement Chain steps the conductor already runs.
- Don't split one ask into mini-missions to run two conductors. Two conductors require two genuinely separate deliverables.

### How to invoke

```
/go "turn the Cooz call notes into a case-study post and figure out where it should live"
```

→ Card compiles (likely Pattern: solo + voice layer, Serves: the $5K sprint goal, Tier: T1), conductor runs, mission logs, delivery closes with the three Next-Prompts (Deepen / Adjacent / Next milestone — the milestone names the specific active goal from goals.json, never a generic "next step").

### Honest edges

- An unlogged mission is invisible to the console — if something's missing from the pulse board, fix Stage 2.5 logging, not the board.
- The goal spine is only as current as `.agent/cos/goals.json`; a stale sprint there means stale `Serves:` lines everywhere.

---

## 2. `directives/orchestration-doctrine.md` — the Conductor's Law

### What it is

Eight non-negotiable laws + two tables. You don't invoke it; every conductor (and `/go` Stage 0) reads it. The laws in one breath: conductor conducts / executors execute; done = passes-gate, never file-exists (file-existence resume once poisoned 890 files); proof before scale (>50 units of a novel pattern = 1-2 unit proof judged first); deterministic-first (script > hook > prompt > model judgment); one driver per tree; expert embodiment is sacred; every mission logs; verify what you didn't watch being made.

**The Conductor Ladder** — the seat goes to the strongest model available *in the moment*, never a hard pin (opus-fallback policy: degrade a tier, don't stall):

| Seat | Adjustment |
|---|---|
| Fable/Mythos-class | Full doctrine; may author novel patterns freely, banks anything reusable before session end |
| Opus-class | Full doctrine — the EXPECTED steady-state conductor; prefers proven machinery, wargames genuinely new patterns first |
| Sonnet-class | Conducts by the book: doctrine + Mission Cards + existing scripts only; halved waves, doubled verify sampling, T2 posture; escalates taste/kill/strategy calls |
| Haiku-class | NEVER conducts, never executes quality-bearing work — mechanical scouts and format shuttling only |

Executor floor: quality-bearing fleet work runs Sonnet-class minimum, effort-high. Seat handoffs park judgment calls via `handoff_store.py save --thread <t>` with an "awaiting stronger seat" note.

**Blast-radius tiers**: T1 (reversible, in-repo, $0) auto-runs; T2 (publishes, sends, spends, or first-of-kind) shows the card and waits; T3 (destructive, overwrites human work, ships AS Farrice to real people) ALWAYS waits. Standing grants like "run to empty, push as you go" elevate T2→T1 for the granted scope only — never T3.

### When it matters to you

Mostly it runs itself. Where you'll feel it: a Sonnet session behaving more conservatively than a Fable one is the ladder working, not the system degrading. And when a session parks a verdict "for a stronger seat," that's Law-compliant, not lazy.

---

## 3. `execution/session_lock.py` — one driver per tree, physically

### What it is

Law 5 as a mechanism. A long autonomous run (wave loops, fleets, backfills) claims a heartbeated lock at `.agent/session.lock`; `forge_queue.py` and `renaissance_queue.py` refuse to build waves without a valid token. Stale locks (no heartbeat for 45 min) are claimable, so a crashed session never bricks the tree.

### How to invoke

```
python3 execution/session_lock.py claim "<mission>"     # claim or renew (prints token)
python3 execution/session_lock.py heartbeat <token>     # renew between waves
python3 execution/session_lock.py check [<token>]       # exit 0 = clear to run / own lock
python3 execution/session_lock.py release <token>
python3 execution/session_lock.py status
```

### When / when not

- Claim before ANY long autonomous run — three collisions in one arc taught this. A fresh foreign lock prints `BLOCKED` with the holding mission and heartbeat age: wait or coordinate, don't force.
- Ordinary interactive sessions don't need it. It complements, not replaces, the golden rule about never running Codex and Claude Code on this directory simultaneously — the lock only guards workflows wired to check it.

---

## 4. `/pulse-board` — the operator console

### What it is

A one-glance artifact dashboard: missions (including the ones WAITING on your verdict), taste-ledger verdicts, outcomes due from the revenue tracker, open handoff threads, sprint banner, lock status. All deterministic sources — `.agent/missions.jsonl`, `.agent/cos/goals.json`, `.agent/jam/taste-ledger.jsonl`, `revenue_tracker.py due`, `handoff_store.py list`, `.agent/session.lock`.

### How to invoke

```
/pulse-board
```

→ Runs `python3 execution/pulse_dashboard.py`, then republishes `.agent/pulse/pulse-board.html` via the Artifact tool. Same conversation keeps the URL automatically; a different conversation must pass the existing artifact URL so the board never forks into duplicates. Favicon stays 🎛️ — stable tab identity.

### When / when not

- Session open, before verdict-collection sessions, whenever you've lost the thread of what's waiting on you. As of the handoff, three missions sit WAITING (PMF Card-2, fidelity-flag review, Kandi shoot).
- Not a to-do app and not self-updating — it reads logs. Missing data means a logging gap upstream.

---

## 5. `/voice-over` — the overlay pass

### What it is

One-shot Farrice-voice (or brand-context) overlay on any expert-pure output, side-by-side, never destructive. It loads `VOICE-CARD.md` + dial mode (default BLEND — "better version of me," never blanket mimicry), separates what carries the EXPERT's signature (structure, methodology, signature moves) from surface voice (word choice, rhythm, register), rewrites only the surface, and writes a sibling file `<original-name>.voiced.md`. Prose gate runs before delivery: `python3 execution/prose_classifier.py check <overlay-file>`.

### How to invoke

```
/voice-over <file>
/voice-over <file> --dial MIRROR|BLEND|STRETCH
/voice-over <file> --context <brand>        # e.g. mybpm, jen — brand ground doc instead of personal voice
```

### When / when not

- Any expert-pure draft, v2-prompt output, or client piece that needs to ship in your (or a brand's) voice while keeping the expert's thinking measurable.
- Never as an excuse to dilute methodology: if voice and method conflict, the workflow flags the tension rather than averaging it. It composes `skills/voice-os/` — extend that skill, never fork rules into the workflow.
- Felt verdicts on the pair can bank to the taste ledger (domain: voice-overlay), which feeds the weekly ratchet — scoped by the guard below.

---

## 6. The Embodiment Purity Guard (binding, on the taste ratchet)

Wired into `/weekly-closeout` Step 5.5: taste dials promote ONLY into prompts for Farrice-owned deliverables — his brand, client work he directs, system output. NEVER into an extracted expert's embodiment: Role & Activation framing, methodology, voice texture, and signature moves stay THE EXPERT's. Every extraction exists to replicate-then-surpass the expert's own flavor; your taste applies as a separate `/voice-over` overlay. When in doubt, the dial stays in the ledger. This is the same rule as doctrine Law 6 — one law, two enforcement points.

---

## Honest edges (layer-wide)

- **The layer is new.** Card-2's binding-conflict surfacing is the reference behavior for `/go`, but the mission log is thin — the first weeks will surface pattern-table rows that need sharpening. Extend the doctrine table; don't route around it.
- **The lock only guards what checks it.** Wave/queue builders refuse without a token; an ad-hoc script that never calls `check` isn't protected. New long-running machinery should wire the check in.
- **Two overlapping laws, know which fires**: session_lock handles two *Claude* sessions; the CLAUDE.md golden rule handles Claude + Codex. Neither substitutes for the other.
- **Pulse board across conversations** needs the URL passed explicitly, or you mint a duplicate console.
- **Resume the arc by name**: `/resume maestro-os` reloads the pinned handoff, including the three waiting verdicts and the menu-hook live-fire check.

*Created 2026-07-13 (Maestro layer session). Extend this guide as the layer evolves — don't let it sediment.*
