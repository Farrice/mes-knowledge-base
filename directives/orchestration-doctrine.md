# Orchestration Doctrine — The Conductor's Law (Farrice-approved 2026-07-13)

> Banked frontier judgment from the sessions that built the Renaissance, the Prompt Wiring OS, and
> survived three concurrent-session collisions. Any model driving this system orchestrates the SAME
> way by reading this file — pattern choice is system property, not session luck.

## The Laws (expected)

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
4. **Deterministic-first — for protective mechanisms only** (amnesty scope, 2026-07-29).
   Push PROTECTIVE work down the stack (interlocks, minting, logging, receipts): script > hook >
   prompt. A tree-guard in a mechanism can't be skipped by accident. Quality and judgment are
   NOT pushed down — the Compass Doctrine and Partner Posture outrank this law there: a quality
   rule in a mechanism becomes a cage the moment it misreads the request (scar: 2026-07-27
   anaphora false positive).
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
- **`sonnet`** — default for ALL grunt/grind execution: research sweeps, evidence hunts,
  extractions, drafts, gauntlets, advisories, file generation. Effort high for quality-bearing
  work, low for mechanical.
- **`opus`** — the HEAVY EXECUTOR tier (Farrice 2026-07-24, standing — leverage Opus 5, don't
  hoard it): dense multi-source synthesis, hardest adversarial verification and judge-panel
  finals, taste-adjacent first drafts headed for Farrice's verdict, complex multi-file builds,
  and any executor task where Sonnet output would need a conductor rewrite. Opus 5 is a
  step-change over 4.8 at the SAME price — under-seating it is the new waste, not over-seating.
  Never pinned (opus-fallback policy stands: degrade a tier, don't stall).
- **Conductor tier (Fable)** — the main loop only: routing, Mission Cards, synthesis of executor
  output, taste/kill verdicts, user-facing polish. A subagent inherits the conductor tier only by
  deliberate exception, named in one line at dispatch time.
Workflow scripts obey the same law via `agent(opts.model/effort)`; pre-launch review of any
workflow includes checking its seats.

**Bar clause (Farrice 2026-08-05 — gauntlet-loop extraction, `directives/blind-bar-protocol.md`):**
every dispatch/production brief for a taste-bearing deliverable carries one line naming its bar as
an ARTIFACT — `Bar: <golden ref / rubric-anchor example / register exemplar path>. Nothing else
counts as done.` — or explicitly `Bar: none`. Adjectives ("high quality", "on-brand") are not a
bar; an unanchored quality loop polishes the wrong target (KetoneIQ edge). The Blind Bar pass
itself runs in-context in the producing loop, never as a spawned critic (Seating Charter stands:
verification never gets its own seat).

### Executor Model Registry (hard-coded 2026-07-24 — Farrice standing instruction; update on model launches)

Current seat → model resolution (Agent/Workflow `model:` values map to these):

| Seat | Model (ID) | Price /MTok | Prompt like this (per claude-api skill, 2026-07 canon) |
|---|---|---|---|
| Conductor | Fable 5 (`claude-fable-5`) | $10/$50 | Main loop only. Thinking always on; state goal + constraints, not steps. |
| `opus` | **Opus 5 (`claude-opus-5`)** | $5/$25 | Thinking ON by default; effort `xhigh` for hardest coding/agentic, `high` default, `low`/`medium` punch above weight — sweep down. Full task spec in ONE turn. DELETE verification scaffolding ("double-check", verify-subagents) — it self-verifies; over-verification is the failure mode. Add scope-discipline + conciseness lines. Delegates readily — cap its subagent spawns. |
| `sonnet` | Sonnet 5 (`claude-sonnet-5`) | $3/$15 | Adaptive thinking on by default; literal instruction-follower — state scope explicitly; effort `high` default, `xhigh` for hardest; coverage-first prompts for review work (severity filters depress recall); ~30% more tokens/text than 4.6 — give max_tokens headroom. |
| `haiku` | Haiku 4.5 (`claude-haiku-4-5`) | $1/$5 | Mechanical shuttling only (Ladder law: never quality-bearing). |

Standing rules: (1) fleets = Sonnet 5 bodies, Opus 5 heads (judge/verify/synthesis nodes inside
the same fleet); (2) any LLM-calling script in execution/ names exact IDs from this table —
never date-suffixed variants (one exception: Haiku 4.5's real API ID IS date-suffixed,
`claude-haiku-4-5-20251001` — amnesty 2026-07-29, contradiction C12); (3) per-model prompting deltas live in `directives/model-notes.md`
— load it before writing dispatch prompts for a seat you haven't used this session; (4) on a new
model launch, update THIS table + model-notes.md in one commit (the claude-api skill is the
verification source, never memory).

### Latency-Class Seating (adopted 2026-08-06 — God Agent delta move #5; goal: right cost per urgency, scar: none — preventive)

Seat by **latency class**, not just capability: **interactive work** (Farrice waiting on the answer) seats for speed at the capability floor the task needs; **async work** (overnight missions, mission-queue cards, launchd jobs — nobody waiting) seats for accuracy per dollar — prefer a cheaper/slower seat at higher effort over a premium seat at default effort, and batch-shaped async work (many independent units) is the first candidate for the cheapest quality-bearing seat. One-line test when dispatching: *is a human waiting?* No → optimize $/quality, never wall-clock.

## Seating Charter — the Grounding Chain (council-ratified 2026-07-28, Farrice Fork-1B)

Full deliberation: `knowledge/council-sessions/2026-07-28-seating-charter-harness-diet-ratification-contex.md`.

**The law**: every expenditure — a Fable turn, a hook injection, a log line, a canonical rule —
carries one of two tags: **forward** (`consumer:` — code or a human ritual provably acts on it)
or **backward** (`scar:` — a dated wound it guards). Its chain must ground out in a human within
two hops. Neither tag = decoration → archived wholesale (`execution/archive/`, delist-not-delete;
/arsenal restocks; a real break is the ticket back). **Receipts are MINED from observe logs,
never manufactured on a calendar — no new trackers, ledgers, or probation channels, ever.** The
receipt check lives inside `/weekly-closeout` (existing consumer), nowhere else.

**The hop ladder seats the models**:

| Hop | Definition | Seat |
|---|---|---|
| **0** | A human outside the repo directly receives it | **Fable may write directly — CLOSED LIST ONLY** (Farrice Fork-1B, 2026-07-28): Parallax editions · cold offer emails · letters-to-JJ-grade personal writing. Nothing enters this list without Farrice's explicit say — "voice-bearing" as an adjective is how creep starts. Everything else at hop 0: Opus 5 writes, taste arbitrates after. |
| **1** | Consumed by a process whose output a human receives | Opus 5 steady-state production (client deliverables, briefs, drafts, refinement) · Fable for dispatch/compilation when the turn ends in a decision consumed by 3+ downstream cheaper turns · Sonnet 5 when a script/agent consumes it |
| **2+** | Read only by another subsystem | **No seat. Archive without ceremony** — observer-of-observer chains are the 60%-maintenance disease. *Mailroom exception (Farrice, 2026-08-27 — goal: reply-to-reply deliberation; scar: frozen-snapshot councils): live council agent-to-agent DMs, the Commons, and persona session memory are sanctioned; each chain still grounds in Farrice within 2 hops (DM → synthesis → him; memory → next council → him). Canon: `directives/agent-mailroom.md`.* |

**Fable budget rule** (≈50% of monthly budget — spend deliberately): before a Fable turn, name
the consumer — either the closed-list hop-0 artifact, or the 3+ downstream turns that consume the
dispatch. A Fable-written artifact outside the closed list = a **misseat**, logged and read in
`/weekly-closeout` as a trend, never a quota. Verification never gets its own seat: the main
loop verifies (dialect law), a spawned reviewer only on Farrice's ask or a compromised context.

**Fable-absent degradation (Farrice 2026-07-28 — the ORIGINAL intent of this charter: Opus 5 is
the default seat and must deliver Fable-grade conducting when no Fable seat exists):** the
charter NEVER stalls work waiting for Fable (opus-fallback policy: degrade a tier, don't stall).
When Fable is unavailable: hop-0 closed-list artifacts route to **Opus 5 + Farrice's felt
verdict as the taste gate** (his arbitration replaces Fable's composition — the human is the
apex seat, Fable was only ever its proxy); everything else runs exactly as written, because the
Opus-5 seat inherits the same machinery that makes conducting work — the dieted constitutions,
the dialect injector's per-prompt corrections, Mission Cards, solution cards, and this doctrine.
What closes the Opus→Fable gap is **pre-banked judgment, not prompting**: park genuinely
Fable-grade calls (kill decisions, closed-list amendments, hype-vs-real verdicts) via
`handoff_store.py save` with an "awaiting stronger seat" note, and bank reusable judgment as
wargame failure-maps (`/wargame-run`) so cheaper seats run them blind. A parked call is charter
behavior; a stalled mission is a violation.

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
