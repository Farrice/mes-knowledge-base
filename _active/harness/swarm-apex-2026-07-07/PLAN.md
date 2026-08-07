# Swarm Apex — Native Platform-Class Orchestration

**Date:** 2026-07-07 · **Owner route:** /system-audit (build) → /swarm (product) · **Status:** ALIGNED (Farrice 2026-07-07) — merged into Harness Apex plan as the driving use-case of Waves 3+5
**Goal:** Replace SuperGrok Heavy, Manus, Kimi OK Computer, and Perplexity Labs/Comet subscriptions with native capability that exceeds them — because we hold two structural advantages none of them have: a 221-persona expert layer with genius-depth files, and a deterministic verification chain (Step 5.5, cost gates, honest receipts).

**Farrice's alignment answers (2026-07-07):**
1. Jobs to replace: ALL FOUR — autonomous missions (Manus), parallel swarm (Grok Heavy), deep research (Perplexity), live browser tasks (Comet).
2. Front door: **one `/swarm` conductor** — thin, composes existing hubs, never absorbs them.
3. Autonomy: **plan gate, then unattended** — 30-second plan approval, then hands-off with receipts.
4. Harness Apex: **merge + all 3 open decisions approved** (wave order as-is · JCC-vs-Workflow head-to-head pilot · blind_pass latch with logged override).

---

## What the research established (briefs in `research/`)

| Platform | Actual mechanic (verified) | What we steal | What we already beat them on |
|---|---|---|---|
| **Manus** | NOT a specialist swarm — planner + one general executor + knowledge module; CodeAct; append-only cache-friendly context; `todo.md` recitation against goal drift; file system as memory; failures kept in context; Wide Research = homogeneous agents + schema-constrained submit | todo recitation · schema submit contracts · file-path (not content) handoffs · keep-failures-in-context | Expert depth; their credit burn is opaque — our cost gates are physical |
| **Grok 4 Heavy** | Fan-out 4 or 16 keyed to one effort knob → single leader-agent synthesis. No verification layer — leader bias/hallucination passes through | Deterministic effort→fan-out function · per-subagent spend receipt lines · role-typed rosters | Step 5.5 verification; council synthesis that preserves dissent instead of one leader blending |
| **Kimi K2.6** | Heavy mode = 8 full trajectories + reflective aggregation; swarm = map-reduce ("one reader per file, merge"); best at bounded artifacts (decks); degrades on multi-hour adaptive work; default ask-before-acting on state changes | Reflect-and-aggregate pattern · named swarm roles · approval-gating on state-changing browser/file actions | Adaptive judgment at the orchestrator (Fable main loop) |
| **Perplexity** | Deep Research = 20–50 query fan-out, iterative retrieve→reason→refine; Labs = research→code→**packaged artifact bundle** (report + deployed mini-app + assets) with visible task trace; Comet = AX-tree perception (never raw DOM), subagent-per-tab, deterministic URL blocking — but fails multi-step transactions; independent citation misattribution ~37% (CJR/Tow) | Query fan-out shape · **packaging as product** · visible tool-trace artifact · AX-tree default for Playwright · code-level domain gating | Verification chain (their 37% misattribution IS our wedge); expert-lens research |

**The one truth:** every platform is fan-out + synthesis + trace. They win on packaging polish, unattended reliability mechanics, visible progress, and one-button UX. They cannot match expert depth or deterministic verification. Build the four missing pieces; keep our spine.

## What the internal audit established (full matrix in `research/internal-audit.md`)

- The **native Workflow engine is our only real parallel surface** — `collective-genius-council.workflow.js` already does concurrent schema-validated fan-out. swarm-commander is explicitly sequential persona simulation ("80-95% of parallelism benefits" — it isn't); JCC is ~100% prose with contradictory scale tables; autopilot forbids fan-out by default.
- Constraints that BIND this design: no `.claude/agents/` named subagents (generic Agent-tool dispatch with Tier-3 expert file injection only) · no new orchestration hub (conductor composes) · 12-worker cap + 4-field envelope · word-ceilinged worker reports (density > completeness) · never pin Opus · plan-gate = compass not cage.
- 8 gaps vs platforms, the big four: no unattended mission mode with live progress · no automated deliverable packaging (`package-deliverable.md` is a manual playbook) · browser automation is an ad-hoc tool grant, not a worker type · swarm synthesis is prose-only cross-checking (Wave 2 verifiers queued, not shipped).

---

## The Build — four sessions, each shippable alone

### Session 1 — `/swarm` conductor v2 + first two patterns (heavy, research)
Upgrade the EXISTING `/swarm` workflow (not a new hub) from sequential simulation to the real thing:
1. **Conductor flow:** intent → DICE score → **Mission Plan file** (`.tmp/swarm/<slug>/mission.md`: pattern, expert roster via `council_cast.py`, fan-out size, cost estimate, deliverable spec, verifier list) → **ONE plan gate** → unattended execution via a native Workflow script → receipts + packaged output. Plan file doubles as the Manus-style `todo.md` — workers and synthesizer re-read it (recitation).
2. **Pattern: `heavy`** (Grok/Kimi killer): N independent expert trajectories on the same problem (N = deterministic function of declared effort: 4/8/12, capped 12), each with a distinct lens, schema-constrained submit → reflective aggregation that PRESERVES dissent (reuse convene's converge discipline) → Step 5.5 verify pass on the merged answer.
3. **Pattern: `research`** (Perplexity killer): query decomposition → parallel search workers (one per subtopic, word-ceilinged, source-locked) → iterative deepen on promising clusters → claim inventory with VERIFIED/LIKELY/UNCONFIRMED labels → honest receipt + visible task-trace section in the deliverable.
4. Per-subagent token/spend lines in the run receipt (Grok's one honest move, done better).

### Session 2 — Wave 2 verifiers wired into swarm synthesis
`claim_audit.py` (regex claims → each carries a label/source tag; hard-fails unlabeled) and `gates.py check` land here exactly as the apex plan specifies — now with platform justification: this is the layer Grok visibly lacks and Perplexity measurably fails (37%). Wire both as post-synthesis steps in every pattern script.

### Session 3 — Pattern: `mission` (Manus killer) + JCC head-to-head
1. **`mission` pattern:** planner agent writes the step graph into the Mission Plan → general executor workers per step (4-field envelope, file-path handoffs, failures kept in context, schema submit) → checkpoint recitation between phases → verifier gate before packaging. Multi-day resume via Workflow `resumeFromRunId` + mission file.
2. **`directives/worker-envelope-standard.md`** ships here (apex Wave 3 item), codifying: OBJECTIVE/OUTPUT-FORMAT/TOOLS/BOUNDARIES + anchors + ≤500-token summaries + gate-on-file-not-summary + schema submit.
3. **JCC pilot (approved decision 2):** author `strike` as a Workflow script, run head-to-head vs prose-JCC on the same brief. JCC's taste (mission briefing, expert assembly, AAR) survives either way; only plumbing is on trial.

### Session 4 — Packaging + `browser` pattern
1. **`package_deliverable.py`** — the script `package-deliverable.md` always promised: mission outputs → polished bundle. Routes by modality registry (apex Wave 5): dashboards → Artifact/dataviz · decks → Gamma MCP/pptx · docs → docx/pdf · sheets → xlsx. Every bundle includes the visible task-trace + receipt (Labs' best move). This IS apex Wave 5's `/make` machinery — `/swarm` calls it; `/make` remains the standalone door for single-artifact requests.
2. **Pattern: `browser`** (Comet killer): Playwright worker type with AX-tree snapshots as default perception, deterministic domain allow/block in code (extend `browser-automation-safety.md` tiers), subagent-per-tab for parallel sources, and Kimi-style ask-before-acting on any state-changing action (submit/post/purchase) — that one gate stays even in unattended mode.

### Continuous
- Roster truth: live-computed expert census feeding `council_cast.py` (audit found 4 conflicting counts: 89/96/109/221).
- Wave 4 portability (model_tier advisory fields, calibration blocks) applies to every pattern script as written.
- Acceptance test per platform: same brief run natively vs the subscription product, Farrice judges blind. **Done = he cancels the subscription.**

## What we deliberately do NOT do
- No new hub, no `.claude/agents/` roster revival, no JCC rewrite before the pilot verdict, no Opus pinning, no packaging that hides the receipt. Hubs stay peers; `/swarm` composes.

## Deliverable-shape acceptance (the bar per pattern)
- `heavy`: answer + preserved-dissent forks + verification labels — beats Grok Heavy because dissent and verification survive synthesis.
- `research`: cited narrative + task trace + honest receipt — beats Perplexity on citation integrity (labeled, audited claims).
- `mission`: packaged artifact bundle + mission file + resume handle — beats Manus on cost transparency and expert depth.
- `browser`: completed web task + action log + zero un-gated state changes — beats Comet on reliability by refusing the transaction classes it fabricates.
