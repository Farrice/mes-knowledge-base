# Root-Core Operator Guide — What We Built 2026-07-10 and How to Use It

> The Matt Pocock v1.1 merge session produced three harness-native workflows, one standing doctrine, and a refreshed set of imported skills. This is the operator's manual: what each does, how to invoke it, worked examples from the live pilots, and the honest edges. Companion: `docs/HARNESS-LAYERS-EXPLAINED.md` · registry: `directives/external-skills-registry.md` · solution card: `docs/solutions/2026-07-10-external-system-merge-adapt-pattern.md`.

---

## The mental model (read this once, everything else follows)

Three ideas run through everything built:

1. **Decisions before deliverables.** When an effort is foggy — you can't see the way from here to done — the mistake is charging at the destination and producing half-right deliverables. Chart the *decisions* first; deliverables come out clean once the way is clear. That's `/wayfinder-work`.
2. **HITL vs AFK.** Every piece of work is either human-in-the-loop (your taste, your verdicts, your relationships, your logins — never simulated) or agent-alone (research, drafts, transforms — runs in parallel while you do something else). Naming which is which, per ticket, is what lets the swarm work without the system pretending to be you. That's `directives/orchestration-primitive.md`.
3. **Verify everything, axes separate.** A deliverable can nail your voice and miss the brief, or nail the brief in someone else's voice — and a merged review lets one failure hide behind the other's pass. That's `/two-axis-verify`.

---

## 1. `/wayfinder-work` — decision maps for foggy, multi-session efforts

### What it is

A persistent map of the *open decisions* standing between you and a named destination, stored as plain markdown in the project folder. Each decision is a ticket. Tickets declare what blocks them. The **frontier** — tickets that are unblocked and unclaimed — is always visible, so any session (today, next week, a different machine) opens the map and knows exactly what's next. No more re-explaining a project to a fresh context window.

### When to reach for it

- Offer launches, campaign builds, client engagements, pivots, big learning missions — anything that will take **more than one session** and where real questions are still open.
- The tell: you catch yourself thinking "there's a lot here and I'm not sure where to start." That feeling *is* fog. Chart it.

### When NOT to

- Single-session deliverables → just run the Chain.
- A plan that's already clear and only needs execution → `/supercomputer` or a fleet.
- Repo/code work → imported `/wayfinder` directly (it uses `.scratch/`).

### How to invoke — copy-paste examples

```
/wayfinder-work chart a map for the MyBPM Week-1 launch — destination: first 10 sales collected
```
→ Charts a new map: grills you to pin the destination, fans out breadth-first to surface every open decision, writes MAP.md + tickets, stops. (Charting is one session's work — it deliberately does not also start resolving.)

```
/wayfinder-work work the alignment-architect frontier
```
→ Opens the existing map, lists the frontier by name, takes the first unblocked ticket (or the one you name), claims it, resolves it with you, records the answer, closes it, and graduates any fog the answer sharpened into new tickets.

```
/wayfinder-work resolve ticket 0004 on the DWA map
```
→ Ticket 0004 is typed `research` (AFK) — so this dispatches a background research agent and you keep working. You'll get the findings as a saved asset plus a closed ticket.

```
dispatch agents for every AFK ticket on the DWA frontier
```
→ The parallel move: all unblocked research/task tickets run concurrently in the background; HITL tickets wait for you.

### What a map looks like (live example)

`_active/offer-strategy/alignment-architect-2026-07-07/wayfinder/MAP.md` — destination: *the 30-day test reaches an honest verdict on real execution*. Five tickets:

| # | Ticket | Type | Blocked by |
|---|---|---|---|
| 0001 | Lock the offer name | grilling (HITL) | — |
| 0002 | Josh & Katie + Cooz consent nods | task (HITL) | 0001 |
| 0003 | Create payment links | task (HITL) | 0001 |
| 0004 | Benchmark the [GUESS] conversion rates | research (AFK) | — |
| 0005 | Month-2 pipeline mechanism | grilling (HITL) | — |

Read: the frontier right now is 0001, 0004, 0005. Resolving 0001 (one grilling conversation: pick the name) unblocks 0002 and 0003. 0004 can run AFK *today* with zero input from you. The map also holds **Not yet specified** (fog you can see coming but can't phrase sharply yet — e.g. "does the $400 audit price hold after the first 3?") and **Out of scope** (ruled out consciously — e.g. rebuilding the shipped assets).

### Can / can't

- **Can**: hold weeks of thinking coherent across sessions · run AFK research in parallel while you sleep · stop you from re-deciding things (Decisions-so-far is the record) · be shared with a collaborator (it's just markdown).
- **Can't**: do the work — it produces *decisions, not deliverables* by design. When the map is done, you hand off to the execution OS. · answer HITL tickets for you — a grilling ticket resolves only through a live conversation with you; that's a feature, not a limit. · update itself — sessions must close tickets properly (the workflow enforces this, but if you edit files by hand, keep the gist-line in MAP.md in sync).
- **One HITL ticket per session.** Deliberate: it keeps each conversation sharp instead of grinding through five decisions with degraded attention.

---

## 2. `/two-axis-verify` — Voice ∥ Brief review, never merged

### What it is

Two subagents review the same deliverable in parallel and report side by side. The **Voice axis** checks the piece against documented standards (VOICE-CARD, slop ban bank, client voice card) plus a content-smell baseline. The **Brief axis** checks it against what was actually asked — missing asks, scope creep, delivered-but-wrong. A deterministic `prose_classifier.py` pass runs first so the model layer starts where the machine layer stopped.

### When to reach for it

- Any client-facing deliverable (implementation-grade binding applies anyway).
- Taste-bearing brand pieces before publish (Parallax editions, LinkedIn posts, DM scripts, offer pages).
- Anything that already scored <7 at Chain Step 6 once.

### When NOT to

- Internal scratch, system artifacts, exploration drafts — the two-subagent cost isn't earned there.
- As a substitute for your felt verdict — it feeds your judgment, never replaces it.

### How to invoke — copy-paste examples

```
/two-axis-verify _active/farrice-brand/drafts/post-07-11.md — brief: the thought-bank entry it came from
```

```
run two-axis-verify on the Jen listing sheet against her CLAUDE.md and the listing brief
```
(For client work the Voice axis loads *their* voice card, not yours.)

### Worked example — its first live run

Run on `WARM-DM-SCRIPTS.md`, a file the deterministic classifier scored **CLEAN, 0/10 AI signals**. The axes still found:

- **Voice, hard**: one exclamation mark (VOICE-CARD §2 bans them); em-dash as the connective in **12 of 12 messages** against your zero-em-dash law — the exact mechanical fingerprint the ban bank names.
- **Voice, judgment**: the "no pressure" release-valve cloned across 5 of 6 follow-ups; the same value-prop sentence pasted into 3 "personalized" scripts.
- **Brief, real**: the $1,500 founding-rate scarcity lever — WEEK-1.md's sharpest urgency mechanic — appears in **zero** DMs.
- **Brief, clean**: consent gates implemented verbatim; no scope creep.

That's the whole argument for the tool in one run: three different gates (deterministic, voice, brief) each catch what the others structurally cannot.

### Can / can't

- **Can**: catch mechanical fingerprints and brief drift on pieces that "read fine" · give you per-axis worst-issue triage · feed Step 6 scores with evidence instead of vibes.
- **Can't**: work without sources — the Voice axis is only as strong as the documented voice card it reads (a client with no voice card = a thin axis; build the card first). The Brief axis refuses to invent a brief: no brief on file → it reports "no brief available" rather than guessing.
- **Hard Voice violations block delivery** — same force as the Factual Grounding veto. Judgment-call smells are triage, not blocks.

---

## 3. `/operator-school` — beginner → operator in any domain

### What it is

A stateful learning OS that gets you from "I know nothing about this vertical" to "I can operate here with taste." It runs on the imported `/teach` mechanics (mission file, HTML lessons, learning records, spaced retrieval) with five operator deltas: a **deploy target** instead of a syllabus, a **pattern bridge** that maps every new domain onto domains you already master, a **taste ladder** of exemplar-pair verdicts, **expert wiring** into the extraction roster, and a **deploy gate** — you graduate by shipping, not by finishing lessons.

### When to reach for it

- A new client vertical you need to speak fluently in two weeks.
- A capability you're bootstrapping (prediction-market microstructure, paid ads, a platform you've never run).
- Any "I need to get up to speed on X" feeling — that phrase is the trigger.

### How to invoke — copy-paste examples

```
/operator-school start: prediction-market microstructure — deploy target: my first paper-bet portfolio built on my own edge model, by July 24
```
→ First session: grills the mission until the deploy target is concrete, builds `PATTERN-BRIDGE.md` (e.g. *market-making spread ≈ managing volume/intensity tradeoffs in programming; order-book depth ≈ audience-demand signal in content*), seeds RESOURCES.md from real sources, teaches lesson 0001.

```
/operator-school next lesson — prediction markets
```
→ Reads your learning records, picks the next lesson inside your zone of proximal development, teaches tight, drills with a feedback loop, runs one taste-ladder rung, records what stuck.

```
/operator-school taste rung — show me a sharp market vs a mug's market, I'll call it
```
→ One great exemplar beside one mediocre one, both real and sourced. You call the verdict + why in one line *before* seeing the tell. Verdicts log to `TASTE-LADDER.md` — your calibration curve for the domain, visible over time.

### The core move, explained

Your edge is transferable pattern recognition and systems thinking — the school's job is to *attach the new domain to patterns you already own* instead of teaching it from zero. Every lesson opens on the bridge ("this is like X in coaching, except…"), and **where the bridge breaks is flagged explicitly** — the breaks are the real learning content, because that's where imported intuition would mislead you.

### Can / can't

- **Can**: compress time-to-operator hard · make your judgment measurable (the taste ladder is a written calibration record) · teach from extracted experts + primary sources instead of parametric guessing.
- **Can't**: create wisdom without reps — the deploy gate exists because real-world contact is the only teacher of the last mile. · make you a *master* — operator means you can run the loop with taste; mastery is volume after graduation. · work well crammed — storage strength needs spacing; two or three sessions a week beats one marathon.
- Not yet run live end-to-end (built and structurally verified this session; its first real domain run is the remaining proof).

---

## 4. `directives/orchestration-primitive.md` — the doctrine (mostly automatic)

You don't invoke this; it invokes itself. It's the standing rule that was previously a per-session request: **Fable holds the map, the judgment, and everything HITL; Sonnet-tier executors do the grunt work in parallel on the frontier; nothing ships without the verify ladder** (deterministic checks → two-axis → adversarial verify → PoC gate → faithful reporting).

Where you'll feel it:

- Sharpening questions now split **facts vs decisions** — the system digs up facts itself (files, memory, receipts) and only brings you *decisions*, each with a recommended answer. If a session ever answers its own questions, that's a broken primitive — call it out.
- Saying `dispatch agents for X` fans work out while your thread stays for judgment.
- New assets always arrive with an in-session proof, and failures get reported with output, not hedged.

---

## 5. The refreshed imports — worth knowing directly

All global (`~/.claude/skills/`), upstream-managed (`npx skills@latest update`), Chain-exempt utilities. The high-value ones for you:

| Skill | Say | What you get |
|---|---|---|
| `/grilling` | "grill me on this plan" | Relentless one-question-at-a-time interview; facts looked up, decisions yours; won't act until you confirm shared understanding |
| `/research` | "research X in the background" | Background agent, primary sources only, cited markdown file saved to the repo |
| `/to-spec` → `/to-tickets` → `/implement` → `/code-review` | (dev loop, in order) | Conversation → spec → tracer-bullet tickets with blocking edges → build per ticket in fresh context → two-axis code review |
| `/teach` | "teach me X" | The raw learning engine (use `/operator-school` instead when the goal is operating a domain, not just understanding a concept) |
| `/ask-matt` | "/ask-matt" | His own router — explains which of his skills fits a situation |
| `/writing-great-skills` | (when authoring skills) | The predictability theory + glossary; our adoption of it lives in `directives/skill-craft-standard.md` §9 |

Renames to unlearn: `to-prd`→`to-spec`, `to-issues`→`to-tickets`, `diagnose`→`diagnosing-bugs`, `review`→`code-review`, `write-a-skill`→`writing-great-skills`. Old versions are archived at `~/.agents/skills-archive-2026-07-10/`, restorable by moving back.

---

## 6. How it all chains — the cold-start-to-shipped flow

```
loose idea
   │
   ├─ small enough for one session? ──yes──► Chain as usual ──► /two-axis-verify ──► ship
   │
   no (fog)
   │
   ▼
/wayfinder-work chart ──► work the frontier over sessions
   │        (HITL tickets with you · AFK tickets in parallel)
   ▼
map done — way is clear ──► destination artifact (brief/spec/offer doc)
   ▼
execution OS (/supercomputer, /copy-engine, /farrice-engine, fleet…)
   ▼
/two-axis-verify on every taste-bearing/client-facing piece ──► Chain Step 6 ──► ship
```

And when the domain itself is new to you, `/operator-school` runs *beside* that flow — its deploy target is usually the first real artifact the flow above will ship.

## 7. The living-guide loop — `/operator-guide-sync` (added 2026-07-10)

This guide maintains itself through a deterministic loop, so it never depends on anyone remembering it:

- **Detector**: `python3 execution/operator_guide_sync.py check` — flags operator assets (workflows, skills, directives, imports) changed since the last sync stamp. Wired into the closeout spine, so `/end-session` (and the SessionEnd backstop) nudges "OPERATOR GUIDE UPDATE DUE" automatically whenever a session shipped operator surface.
- **Writer**: `/operator-guide-sync` — reads the delta, updates *sections* surgically (never regenerates the guide), prunes superseded entries in the same pass, then stamps via `record`.
- **Your part**: nothing, usually. If you see the nudge at closeout, say "run operator-guide-sync" — or run it mid-session after a big build. When current, check exits clean and costs nothing.
- **Can't**: judge relevance deterministically — the detector over-reports (a telemetry edit flags the same as a new tool) and the writer filters. It also documents how to RUN things only; it is not a changelog, project tracker, or skill index.

### Recently added expert systems (extractions get one line here on arrival; depth lives in their own SKILL.md)

| System | Front door | One-liner |
|---|---|---|
| Ben Watkins storytelling (2026-07-09) | `/bw-story-selling-system` (14 `/bw-*` wf) | Pitch-room emotion engineering + the subtraction cut; B-tier pending your pass |

## 8. Honest edges (system-wide)

- **New global skills appear next session**, not mid-session — if a fresh install isn't visible, restart the session before debugging.
- **Maps are files, not magic** — a hand-edited ticket needs its MAP.md gist-line kept in sync; the workflow does this when it does the closing.
- **Two-axis costs two subagent runs** — reach for it at the moments listed, not on every paragraph.
- **The Voice axis inherits your documentation debt** — no voice card for a client means a weak axis; writing the card is the fix, not blaming the tool.
- **Wayfinder concurrency** — you *can* run parallel sessions on different tickets (claiming exists for exactly this), but remember the golden rule: never Codex and Claude Code on this directory at the same time.
- **Operator-school's live proof is pending** — first real domain run will surface rough edges; expect to `/extract-approach` whatever we learn.

*Created 2026-07-10 (extract-forge session, Matt Pocock v1.1 merge). Extend this guide as the tools evolve — don't let it sediment.*
