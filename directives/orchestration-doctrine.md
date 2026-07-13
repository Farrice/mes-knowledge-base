# Orchestration Doctrine — The Conductor's Law (Farrice-approved 2026-07-13)

> Banked frontier judgment from the sessions that built the Renaissance, the Prompt Wiring OS, and
> survived three concurrent-session collisions. Any model driving this system orchestrates the SAME
> way by reading this file — pattern choice is system property, not session luck.

## The Laws (non-negotiable)

1. **Fable conducts, Sonnet executes.** The main thread holds judgment, synthesis, gating, taste
   staging, commits. Fleets do the grind. Raise effort before raising tier; never pin Opus.
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
