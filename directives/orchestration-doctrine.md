# Orchestration Doctrine — The Conductor's Law (Farrice-approved 2026-07-13)

> Banked frontier judgment from the sessions that built the Renaissance, the Prompt Wiring OS, and
> survived three concurrent-session collisions. Any model driving this system orchestrates the SAME
> way by reading this file — pattern choice is system property, not session luck.

## The Laws (non-negotiable)

1. **The Conductor conducts, Executors execute — roles, not models.** The main thread holds
   judgment, synthesis, gating, taste staging, commits. Fleets do the grind. Whoever is the
   strongest available model sits in the conductor seat and inherits this ENTIRE doctrine —
   that is the point of banking judgment in a file instead of a model. See the Conductor
   Ladder below. Raise effort before raising tier; never pin a specific model and stall
   (Farrice's standing opus-fallback policy: degrade a tier, don't stop).
2. **Done = passes-gate, never exists.** Every resumable pipeline pairs its queue with a quality
   gate. File-existence resume poisoned 890 files once; never again.
3. **Proof before scale.** A novel pattern about to run >50 units gets a 1-2 unit proof judged
   first (A/B when the claim is "this new way is better"). Farrice's standing gate: if the proof
   isn't a clear win — stop and jam.
4. **Deterministic-first.** Push work down the stack: script > hook > prompt > model judgment.
   A rule that lives in documentation gets violated by accident; a rule in a mechanism can't be.
5. **One driver per tree.** Check/claim `.agent/session.lock` before any long autonomous run
   (`python3 execution/session_lock.py claim "<mission>"`). Three collisions taught this.
6. **Expert embodiment is sacred.** Extractions replicate-then-surpass the EXPERT's flavor.
   Farrice's taste applies to Farrice-owned deliverables and via `/voice-over` overlays — never
   baked into an expert's Role/methodology/voice. (Taste ratchet carries the same guard.)
7. **Every mission logs.** One JSONL line to `.agent/missions.jsonl` at compile + at close
   (see /go Stage 2.5) — the pulse dashboard and COS read from it.
8. **Verify what you didn't watch being made.** Corpus claimed done by another process/session =
   fingerprint triage, then content-level verify fleet, then delete-and-regenerate (never patch).

## The Conductor Ladder (model-agnostic seating, Farrice 2026-07-13)

The seat is filled by the best model available IN THE MOMENT — plan limits, availability, and
platform decide, never a hard pin. Same laws at every rung; what changes is how much the rung
leans on deterministic scaffolding.

| Conductor seat | Behavioral adjustments |
|---|---|
| **Fable / Mythos-class** | Full doctrine as written. Novel-pattern authoring allowed freely (new workflow scripts, new gates) — but bank anything reusable into directives/solution cards before session end. |
| **Opus-class** | Full doctrine as written — this is the EXPECTED steady-state conductor, not a degraded mode. Prefer proven machinery (existing wave scripts, gates, queue builders) over authoring novel orchestration mid-mission; when a genuinely new pattern is needed, wargame it first (`/wargame-run`) or run a smaller proof. Fast mode is fine for conducting; it's still Opus. |
| **Sonnet-class (fallback)** | Conduct by the book: doctrine table + Mission Cards + existing scripts ONLY — no novel orchestration authoring. Halve wave sizes, double verify sampling, prefer T2 posture (show cards, wait) even where grants would allow T1. Escalate judgment-heavy verdicts (taste, kill decisions, strategy) to Farrice or park them for a stronger seat via handoff. |
| **Haiku-class** | NEVER conducts and never executes quality-bearing forge/content work (proven 2026-07-11: template slop at scale). Mechanical scouts, file inventories, and format shuttling only. |

**Executor floor**: quality-bearing fleet work (forging, refactoring, verification, content) runs on
Sonnet-class minimum, effort-high — raise effort, not tier. Judge/verify panels may seat the
conductor's tier for the hardest calls.

**Dispatch seating law (Farrice 2026-07-21, binding — the token-economy rule):** a dispatch with
no explicit model inherits the CONDUCTOR'S model — when Fable conducts, every unseated Agent or
workflow agent() call silently burns Fable tokens on executor work. Therefore **no unseated
dispatches**. Every dispatch names its seat:
- **`sonnet`** — default for ALL execution: research sweeps, evidence hunts, extractions, drafts,
  gauntlets, advisories, file generation. Effort high for quality-bearing work, low for mechanical.
- **`opus`** — reasoning-heavy execution where Sonnet visibly degrades the deliverable: hardest
  adversarial verification, dense multi-source synthesis, judge-panel finals. Never pinned
  (opus-fallback policy stands: degrade a tier, don't stall).
- **Conductor tier (Fable)** — the main loop only: routing, Mission Cards, synthesis of executor
  output, taste/kill verdicts, user-facing polish. A subagent inherits the conductor tier only by
  deliberate exception, named in one line at dispatch time.
Workflow scripts obey the same law via `agent(opts.model/effort)`; pre-launch review of any
workflow includes checking its seats.

**Seat handoffs**: when a stronger seat will resume later, park judgment calls explicitly —
`handoff_store.py save --thread <t>` with an "awaiting stronger seat" note — rather than forcing
them at the current rung. When a weaker seat inherits mid-mission, it re-reads this doctrine +
the mission's cards before touching anything (the Mission Card is the wargame order).

## Orchestration Pattern Table (Stage 1 law for /go and any conductor)

| Signal in the mission | Pattern | Machinery |
|---|---|---|
| Single deliverable, one domain, known shape | **Solo expert** — Tier 1/2 load + honor the matching v2 prompt's contract | Chain steps 3-6 |
| Taste-bearing creative where felt verdict matters | **Solo + jam stage** — produce take(s), stage side-by-side, bank verdicts | `/jam`, taste-ledger |
| Deliverable ships under Farrice's name | Solo + **VOICE-CARD layer** (dial default BLEND); overlay-on-expert via `/voice-over` | voice-os |
| 3+ independent workstreams OR 10+ similar units | **Fleet** — scout → one Sonnet agent per unit → deterministic gate → commit per wave | Workflow engine |
| 50+ units or novel fleet pattern | **Proof first** (Law 3), then fleet | A/B + JUDGMENT.md |
| Real tradeoffs, multi-domain, dissent valuable | **Council** | `/convene` (+presets) |
| Plan now, cheaper model/session executes later; wrong turns expensive | **Wargame** — bank failure-maps | `/wargame-*` |
| Open-ended discovery, multi-modal search | **Swarm / research** | `/swarm`, `research.py` |
| Corpus of unknown provenance claimed "done" | **Verify fleet** — read-only batches vs source, err toward regenerate | Law 8 |
| Decision map before deliverables, foggy multi-session | **Wayfinder** | `/wayfinder-work` |

Two rows matching = name the fork in one line, pick the stronger. Composing rows (fleet inside a
wargame, jam after a fleet) is normal; the table names the PRIMARY shape.

## Blast-Radius Autonomy Tiers (Stage 2 law)

| Tier | Definition | Posture |
|---|---|---|
| **T1 — reversible, in-repo** | files/commits in this repo, $0 APIs, established patterns | AUTO-RUN; Mission Card shown as it starts |
| **T2 — outward/paid/novel** | publishes, sends, spends (cost-gated APIs), or first-of-kind pattern | Show Mission Card, WAIT for nod (or standing grant) |
| **T3 — destructive/identity** | deletes outside repo, overwrites human work, ships AS Farrice to real people | ALWAYS wait; never auto |

Standing grants (e.g. "run to empty, push as you go") elevate T2→T1 for the granted scope only,
and never touch T3.

## Mission Card (the /go Stage 0 output, evolved)

```
MISSION CARD
Intent: <sharpened one-liner>            Serves: <goal-id from .agent/cos/goals.json | ORPHAN ⚑>
Pattern: <table row> — <one-line reason>
Loads: <experts/skills + v2 prompts that will govern output>
Gates: <which will fire: audit / prose / verify / jam / voice>
Tier: <T1 auto | T2 waiting | T3 waiting>   Cost: <$0 | flagged>
```

Orphan flag is a compass, never a cage (COS law): one line, then execute fully.
