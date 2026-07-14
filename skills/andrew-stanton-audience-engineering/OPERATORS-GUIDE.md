# Andrew Stanton — Operator's Guide

The system-level view: what fires automatically, how the conductor composes, how quality compounds, and how to maintain or extend the deployment without breaking it. Companion: `USER-GUIDE.md` (how to use it). Built from the 2026-06-24 extraction session + the 2026-07-13 enrichment session.

## 1. The deployment map (three layers)

**Layer A — Embedded (fires without invocation).** Stanton is wired INSIDE these engines at these exact points:

| Engine | Where | What fires |
|---|---|---|
| `parallax` | Phase 3 plan-mode + Quality Standards | Architecture pass (premise/spine/change) before drafting; clamp-audit before ship |
| `linkedin-daily` | Step 7 "Single truth" + Step 8 Voice Gate | Premise-sentence litmus; line-to-line clamp-audit next to "polished but flat = FAIL" |
| `copy-engine` | Phase 6 (Polish) | Clamp-audit before finalize; surgical, never rewrites verified blocks |
| `autopilot` | Phase 3 (G3 Taste Pass) | Internal clamp-audit alongside prose classifier; **adds no gate** (gate-suppression contract) |
| `writers-room` | Layer 1 (10th source) + Phase 2 diagnostic 5c | Premise & Clamp Architect — runs first (premise) and last (clamp) |
| depth layer (`/deepen`, `/depth-stack`) | routing-map Deficit 1 + Stage 1 | Co-owner of architecture with Hawley; "a spine that doesn't clamp is a spine no one follows" |

**Layer B — The conductor.** `/stanton-produce`: story gate → architecture → route to owning engine → clamp-audit QA loop → Stanton-Grade Gate → voice/prose/fact gates → anchor-named finalize. Contract: **composition, never rebuild** — if it starts writing what copy-engine/parallax already write, it has failed by its own quality gate.

**Layer C — À la carte.** 20 workflows, three tiers (5 foundation engines, 11 practitioner techniques, 4 cross-domain deployments). Full chain per command: `.claude/commands/stanton-*` → `.agent/workflows/stanton-*` wrapper → `skills/andrew-stanton-audience-engineering/workflows/stanton-*` → `genius.md` gates.

## 2. The quality system (how "Pixar-level" is enforced, not hoped for)

- **The Stanton-Grade Gate** (`references/exemplars.md`) — eight hard vetoes run before any delivery. Treat them as VETOES: per `docs/solutions/2026-07-07-blind-pass-taste-failure-hard-vetoes.md`, taste rules written as prose get read, flagged, and shipped anyway; a numbered fail-list gets enforced. Proven 2026-07-13: the gate caught two loop lines in the Receipt Arc that stated the next post's conclusion (Gate 2, "handed them 4") — clean, on-voice lines that would have shipped under the old pipeline.
- **The exemplar bank** (`references/exemplars.md`) — ground truth for what Stanton-grade looks like in Farrice's domains: 4 session-proven exemplars + 1 anti-exemplar (polished-but-flat), each annotated with rubric anchors + the transferable move. **The compounding rule: every felt PASS from Farrice gets appended.** Rules without exemplars = structure without heartbeat (the 5/10 ceiling).
- **The rubric** (`genius.md § Expert-Specific Quality Rubric`) — 7 criteria anchored at 4/7/10. Finalize enforces anchor-naming: any dimension ≥8 must name its matching anchor or lower the score (learned live: first finalize attempt was rejected for exactly this; re-scored honestly, expert 9→8).
- **The standing gates** — voice rules per surface, `prose_classifier.py check` (AI-slop bank), `fact-verifier` on real-world claims. Stanton never replaces these; it runs before them.

## 3. The stack order (never invert)

**Runia (`story-compass`, is there a story?) → Hawley (season/theme architecture) → Stanton (uncover the premise + audit the clamp) → Roth (scene/line).** On brand: Miller frames customer-as-hero → Stanton gives the spine + negation list. On copy: Stanton sets the arc → copy-engine/Georgi/Fladlien execute blocks. Sovereign pins hold this order (4 pins, semantic tier, 2026-06-24).

## 4. Source ground truth (what the skill knows and from where)

- **Primary**: `extractions/andrew-stanton/transcript.txt` — Perell *How I Write* interview, 11,074 words, 2026. Wins on emphasis.
- **Secondary (labeled)**: `extractions/andrew-stanton-ted/transcript.txt` — 2012 TED talk → `references/ted-talk-layer.md` (punchline-first, Make Me Care, the Promise, 2+2, negation + conditional likability). Six patterns cross-validated across both sources.
- **Deliberate non-action** (logged in the Evolution Log): no frame extraction on the interview — two people at a table; Stanton's on-screen artifacts are his films, so the WATCH prescription is served by film-moment exemplars + the TED layer.
- **Filmography claims**: VERIFIED via web 2026-06-24 (director + co-writer of Toy Story 5, premiered 2026-06-09; co-writer on the first four; Pixar's second animator, 1990). Do not extend credits from memory.

## 5. Registration map (every file that knows about Stanton — touch these when maintaining)

`SKILL_INDEX.md` · `AGENT_INDEX.md` · `.agent/skill-index.json` · `.agent/skill-commands.json` · `DOMAIN_REGISTRY.md` Domain 7 (swim lane + routing branches) · `COUNCIL.md` (Quick Reference, Content Council seat, Tier-3 registry entry) · `agents/_framework/invocation-cards.md` (Writing section card) · `agents/andrew-stanton/` (persona + memory) · auto-memory `project_andrew-stanton-extraction.md` + MEMORY.md pointer · 4 sovereign pins (`memory_store.py`, semantic/rule + insight) · the six engine files in §1.

## 6. Extend-never-rebuild rules

- **Add a workflow (#22+)**: write `skills/.../workflows/stanton-<name>.md` to the Hawley bar (Pre-Flight, gate, steps, adaptations, output format, quality gate, pitfalls) → wrapper in `.agent/workflows/` → mirror in `.claude/commands/` → row in SKILL.md's tier table + bump `workflows:` count → `python3 execution/sync_registries.py` → `python3 execution/find_skill.py --rebuild-index "<probe>"`.
- **Add an exemplar**: append to `references/exemplars.md` (source, load-bearing excerpt, rubric anchors, the transferable move). Trigger: any felt PASS.
- **Add a source**: fetch to `extractions/andrew-stanton-<source>/`, write a LABELED layer file in `references/`, log it in the genius.md Evolution Log, state which source wins on conflict. Never merge unlabeled material into the primary grounding.
- **Never**: gate extractions (standing decision), add a `routing_enforcer` hard binding for Stanton (additive intelligence, not mandatory substitution), duplicate production engines inside Stanton workflows, or install a `.claude/agents/` subagent (this system uses personas + skills).

## 7. Failure modes → fixes

| Symptom | Cause | Fix |
|---|---|---|
| Output uses Stanton vocabulary ("clamp," "premise") on the page | Machinery named — Gate 3 | Execute the move, delete the label; the audience only feels transported |
| A "finished" piece is clean but nobody finishes it | Flat-but-clean — the prose gate can't see it | Run `/stanton-clamp-audit`; check the anti-exemplar in the bank |
| A loop/hook line spoils its own payoff | Handed them 4 — Gate 2 (caught twice live) | Open the debt, withhold the payment; the next unit pays it |
| Premise forced to hit a deadline | The trap Stanton names — a forced premise is false | Let it be lost a while; keep writing bad candidate sentences (P1, P15) |
| Finalize rejected at ≥8 | Anchor not named | Score against `rubric_v1.md` anchors; can't name it → lower it (this is calibration working) |
| Engine wiring stops firing after an engine-file edit | Wiring lines removed in a refactor | §1 table is the checklist — grep each engine file for `stanton` after edits |

## 8. Session receipts (evidence, not claims)

- **2026-06-24**: extraction session — skill + agent + 20 workflows + deep integration; live demos: P1-1 clamp-audit (found the after-the-best-line slip), 14-post escalation find (folder → series), 3 cross-domain demos (sales open, Resonance manifesto, MyBPM 30-sec). Commits `ec87d6e4`, `0be3ca98`, `5b676c89`.
- **2026-07-13**: enrichment + first `/stanton-produce` run — TED layer + exemplar bank + gate (`709cf6521`); Receipt Arc launch sequence finalized 8.33/10 with named anchors, gate 8/8 with two catches (`301b25dc2`).
