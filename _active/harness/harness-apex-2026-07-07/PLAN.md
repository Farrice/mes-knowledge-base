# Harness Apex Plan — Fable-Level Orchestration on Any Model

**Date:** 2026-07-07 · **Owner route:** /system-audit · **Status:** APPROVED ("go", 2026-07-07) — **Waves 0, 1, 2 SHIPPED** (Wave 2 receipts: `2026-07-10T004341Z…`, `2026-07-10T004625Z…`, `2026-07-10T005523Z…` in `.agent/run-receipts/`) · Merged with Swarm Apex (`_active/harness/swarm-apex-2026-07-07/PLAN.md`) as driving use-case of Waves 3+5 · Waves 3-5 queued
**Wave 2 notes:** the "7.25 flattening" was intended behavior — taste_signature Rule 2 caps every unanchored ≥8 at 7.25 (below the 7.5 PASS floor); now unreachable silently, since finalize refuses unanchored ≥8s at input (`--anchor-named` required). Outcome classes: autopilot actually has 12+fallback, not 7 (plan text was stale). skill_auditor heartbeat gate live: 8 skills tier-capped A→B on first full audit.
**Evidence:** 4 parallel audits (supercomputer/autopilot/jw-engine/mission · JCC plugin · extraction stack · routing spine), including a live-reproduced routing miss.

---

## The One Truth

**The harness puts determinism on the cheap parts and trusts the model on the quality-defining parts.** Cost gates, state files, and routing scores are real Python. But the mechanic that actually makes each workflow remarkable — anchor propagation in supercomputer, the claim/fabrication audit in jw-engine, gate conditions in autopilot, validation-contract-first in mission, stage handoffs in JCC, the blind-pass in extraction — is prose the model is trusted to execute. Fable executes it. Sonnet skips it, collapses it, or fakes it.

**Therefore:** Fable-level output on Opus/Sonnet is not achieved by writing smarter prompts. It is achieved by moving every load-bearing judgment into one of three forms a mid-tier model cannot silently skip:

1. **A runnable verifier** with an exit code (the model can't "forget" a gate that blocks finalize)
2. **A structured contract** with schema validation between stages (the model can't drop fields free-prose lets it drop)
3. **A calibration block** written for mid-tier cognition (where judgment genuinely can't be mechanized, tell the weaker model exactly how it will fail and what apex looks like)

Everything below is an application of that principle. Nothing is a rebuild — every wave extends what exists (per standing rules: don't rebuild the router, hubs compose freely, extend never rebuild).

---

## Evidence Base (what the audits found)

| Surface | Deterministic today | Left as prose (the failure point) |
|---|---|---|
| **supercomputer** | cost_gate, anchor_memory state | Anchor *propagation check* (P3 "grep for key terms") — genius.md:84 admits it's an open question. `workflows/` dir is empty. Task spawning implied, never specified. |
| **autopilot** | preflight, recipes, verifiers (good) | G1/G2/G3 gate conditions = multi-clause prose; closeout ritual heavy; 7 outcome classes never enumerated in-file |
| **jw-engine** | Best-designed: worker envelope, hard cap 12, gate-on-file-not-summary | Gate-0 anti-fabrication scan = model-executed prose under 12-worker load |
| **mission/orchestrate** | mission_control.py state, 7 Python routers | Validation-contract-first discipline (the whole point) unenforced; 30-row routing tables restated in markdown |
| **JCC plugin** | Nothing (one bash context-loader) | ~100% prose: free-text stage handoffs, model-computed DAG math, dead evolution stubs, contradictory scale tables (5–8 vs 2–3 experts), `model: inherit` everywhere |
| **extraction** | skill_auditor (advisory only), census flags | Blind-pass = honor system; anti-pattern/exemplar floors unchecked; eval_set has **32 entries for ~370 skills**; chain_runner accepts any scores |
| **routing spine** | BM25 find_skill (good), enforcer BINDINGS (correct) | BINDINGS only checked **post-finalize, non-blocking**; workflow_router has no stopwords/IDF; quality scores never feed weight learning |

**Live specimen:** this session's own request routed to `/bw-but-therefore` because the connective **"but"** substring-matched a workflow literally named `bw-but-therefore` (+3 name, +2 desc — workflow_router strips no stopwords). Meanwhile "supercomputer" and "autopilot" are *literal mandatory signal phrases* in `routing_enforcer.BINDINGS` — the enforcer would have caught it, but the suggestion path never consults BINDINGS. The system already knows the right answer and doesn't ask itself.

---

## Wave 0 — COS Intelligence Brief (user-requested 2026-07-07 — independent, can ship immediately)

Farrice's direct feedback: the goal-pulse brief is "good, not bad" — underwhelming. He avoids social media by design, so the morning brief must be his tap-in channel to the world.

1. **World Pulse loop.** `.agent/cos/interests.json` registry (marketing, copywriting, creative strategy, content strategy, AI, anime — extendable). A nightly research loop (scheduled routine or launchd + `execution/research.py` within existing Perplexity/Gemini budget gates) writes `.agent/cos/world/YYYY-MM-DD.md`: 5-8 items, each = what happened + why it matters *to his goals/threads* + optional one action. `cos_prep.py` renders the top items as a "🌍 World pulse" brief section. Honest-receipt discipline: every item carries a source; no training-memory news.
2. **Question engine v2** in `cos_prep.py`: questions must (a) connect two of his live threads, (b) reference a stamp/loop/goal/world-item, (c) rotate archetypes (decision-forcing · connection-surfacing · life) so no two days feel the same. "Any updates?"-shaped questions are a lint failure.
3. This is also the harness's **first production loop** (see loops discussion) — outcome + cadence + verifier (`world brief exists, ≥5 sourced items, <90 lines`), no human prompting.

**Effort:** 1 session. **Verify:** 3 consecutive mornings of briefs Farrice rates "made my mind flow" ≥1.

## Wave 1 — Routing Spine Correctness (smallest, highest leverage — do first)

> A perfect skill roster is worthless if the router hands the mission to a storyteller.

1. **Consult BINDINGS upstream.** `skill_router_hook.py` and `workflow_router.py` call `routing_enforcer`'s signal matcher *before* fuzzy ranking; a binding hit short-circuits the scorer. Pure deterministic Python — identical on every model.
2. **Unify workflow_router scoring with find_skill.** Route workflows through the same BM25 engine (stopwords, IDF, length norm) or minimally add the stopword filter. Kills the entire connective-noise misroute class.
3. **Close the quality→routing loop.** Feed chain_runner finalize composite into `run_routing_learning` (weight down routes producing <7). Today the loop learns "was the suggestion followed," not "did it work." Wave-3 design doc already proposed this (Q4) — it was never wired.
4. **Hard abstention escalation.** When BM25 < floor AND no binding fires → force explicit route selection (surface top candidates + `/convene` option) instead of silent generalist mode. A mid-tier model must not quietly ship an unrouted turn.

**Verify:** re-run this session's query → owner must rank /system-audit or /virtuoso; regression file of 20 past-misroute queries; `verify_google_operator_core.py` clean.
**Effort:** 1 session.

## Wave 2 — The Verifier Layer (turn every load-bearing prose check into an exit code)

New/promoted verifiers, each callable standalone AND wired into the owning workflow + chain_runner:

| Verifier | Replaces | Wire point |
|---|---|---|
| `anchor_verify.py` — greps dependent deliverables for anchor key-terms, returns propagation score 1–10 | supercomputer P3 manual grep prose | supercomputer P3 gate; finalize warns <7 |
| `claim_audit.py` — regex numbers/dates/names/results → each must carry `[VERIFIED]`/`[ASSUMED]`/`[MODELED]`/source tag | jw-engine Gate-0; Chain Step 5.5 assist | jw P4; any workflow with factual grounding |
| `gates.py check` — evaluates autopilot G1/G2/G3 in code, returns which gate fires | autopilot's three nested prose conditionals | autopilot step 2 |
| `blind_pass.py` — requires N provenance-verified real pieces in `extractions/<expert>/reference-corpus/`, records side-by-side PASS/FAIL, auto-appends eval_set entry | honor-system blind-pass | chain_runner finalize refuses extraction finalize without a recorded verdict — **with explicit `--skip-blind-pass` override flag that logs** (compass-not-cage; extractions stay cost-ungated per standing decision — this is a quality latch, not a spend gate, and the override keeps it advisory-at-will) |
| `skill_auditor.py` promotion — 6 heartbeat checks (anti-patterns ≥5 sourced, exemplars ≥3 verbatim, recognition test, source-ledger, named-entity floor, Output Schema+Quality Gate per workflow) become tier-gating, not advisory | "REQUIRED before ship" prose pointers | extract/extract-forge QC phase |
| chain_runner: reject ≥8 scores lacking `--anchor-named` | convention | finalize validation |

**Verify:** each verifier gets a fixture test (one known-PASS, one known-FAIL artifact); run against ben-watkins (must PASS) and one thin extraction (must FAIL).
**Effort:** 2–3 sessions.

## Wave 3 — Structured Mission Contracts (JCC + supercomputer + swarm)

1. **JSON schemas between every JCC stage:** decomposition graph (workstreams, DAG edges, acceptance criteria), expert injection payload, workstream output (deliverable paths + self-report vs criteria). A validator script between stages; critical-path depth and wave grouping become *code-computed*, not model-guessed.
2. **One source of truth for scale:** reconcile JCC's contradictory tables (scaling-thresholds vs orchestrator vs deploy.md; 3-dim vs 4-dim scoring) into a single config consumed everywhere.
3. **Standard worker envelope** (adopt jw-engine's four-field OBJECTIVE/OUTPUT-FORMAT/TOOLS/BOUNDARIES+ANCHORS + hard cap + `.tmp/<session>/` + ≤500-tok summaries + gate-on-file-not-summary) as `directives/worker-envelope-standard.md`; supercomputer P2 and JCC execute-stage reference it instead of improvising.
4. **Pilot one mission archetype on the native Workflow tool.** Claude Code's Workflow tool now provides exactly what JCC hand-rolls in prose: deterministic fan-out, schema-enforced agent outputs (`schema:` option forces validated JSON — retries on mismatch), pipelines, phases, resume. Author `strike` as a saved workflow script and run it head-to-head against prose-JCC on the same brief. If it wins, migrate campaign/deploy; JCC's *taste* (mission briefing, expert assembly logic, AAR) stays — only the *plumbing* moves to code.
5. **Acceptance-criteria enforcement:** synthesis stage hard-fails and re-dispatches on missing/contradictory workstream outputs instead of trusting self-report.

**Verify:** run the same mission brief through old and new paths; compare synthesis completeness + fabrication count.
**Effort:** 3–4 sessions (pilot first, migrate on evidence).

## Wave 4 — Model Portability (Fable-in-the-files)

1. **Mandatory model-calibration block in every genius.md** — ben-watkins already has the exemplar ("these are intuition primitives, do NOT enumerate the pillars, machinery invisible, **polish is the tell**"). Bake the section into the mes-3.0 report schema + build checklist + skill_auditor heartbeat checks. This is the single biggest thinking-vs-vocabulary lever: mid-tier models pattern-lock and overpolish; the block tells them exactly how.
2. **Per-stage model tiering (never pinned).** Add an advisory `model_tier` field to worker envelopes and JCC/Workflow stages: `judgment` (synthesis, decomposition, taste gates → highest available), `execution` (bulk drafting → inherit), `mechanical` (classification, formatting → cheapest). Respects the Opus-fallback policy: tiers express *relative* intent, degrade gracefully, platform_compiler lint stays.
3. **Compress orchestration surfaces.** Externalize the 30-row routing/agent tables in orchestrate.md/mission.md into calls to the Python routers that already exist (~40% token cut, ends table drift). Dedupe supercomputer's SKILL.md/workflow near-duplicates. Enumerate autopilot's 7 outcome classes in-file; convert its closeout ritual to a fill-in template.
4. **Instruction style rule for all orchestration surfaces** (added to skill-craft-standard): checklists with runnable commands, never multi-clause conditionals; every gate names its command; every stage names its output artifact path.

**Effort:** 2 sessions.

## Wave 5 — The Universal Maker (the AI-arbitrage front door)

The extraction stack (hardened by Wave 2) covers *experts*. What's missing is a single front door for *deliverable modalities*: "make me a dashboard / deck / model / brand system / video at world-class level."

1. **`directives/modality-registry.md`** — deliverable-type → toolchain + expert + verifier map. Rows exist already, scattered: dashboards/graphs → Artifact + dataviz skill · decks → Gamma/pptx + presentation-build · design → fantastic-studio + satori (never a bare prompt to a generator) · UI → DESIGN.md + /product-build · spreadsheets/models → xlsx · video → create-video/remotion + cost gate · docs → docx/pdf. The registry makes composition deterministic instead of remembered.
2. **`/make` front door** (thin — composes, never absorbs): intent → DICE score → modality-registry row → expert load (Chain Step 4) → produce → the modality's *verifier* (dataviz validator, prose_classifier, claim_audit, design taste gate) → finalize. It's The Chain with a modality-aware Step 3/4 — not a new engine.
3. **Extraction beyond people:** extend mes-3.0 with a *craft-extraction* variant (extract a discipline's apex standard — e.g. "world-class financial model," "McKinsey-grade slide" — from exemplar corpora rather than a single speaker). Same blind-pass discipline: generated artifact side-by-side with a real apex artifact.

**Effort:** 2 sessions (registry + front door), craft-extraction variant on demand.

---

## Sequencing & Dependencies

```
Wave 1 (spine)  ──►  Wave 2 (verifiers)  ──►  Wave 3 (contracts/JCC pilot)
                              │
                              └──►  Wave 4 (portability)  ──►  Wave 5 (maker)
```

Waves 1–2 are the foundation everything else trusts. Wave 3's pilot decides JCC's future on evidence, not taste. Waves 4–5 are where "use Opus/Sonnet, keep Fable-level output" is actually cashed in.

**Total: ~10–12 working sessions.** Each wave ends with: verifier run + run receipt + finalize + re-bless where constitutions are touched.

## What We Deliberately Do NOT Do

- **No router rebuild** — Wave 1 is three surgical patches to a router that just learned to learn (Harness Frontier Loops, 2026-07-06).
- **No JCC rewrite-from-scratch** — retrofit contracts; pilot the Workflow tool on one archetype; migrate only on head-to-head evidence.
- **No new orchestration hub** — /make composes existing hubs (no-forced-wiring rule); autopilot/supercomputer/jw-engine keep their identities.
- **No hard blocks on Farrice** — every new gate ships with a logged override flag (compass, never cage).
- **No claude-mem, no Opus pinning, no re-imports** — standing decisions hold.

## Open Decisions for Farrice — RESOLVED 2026-07-07 (all three approved)

1. **Wave order approved as-is?** → **YES** (Farrice, 2026-07-07).
2. **JCC pilot on the native Workflow tool** → **YES** — head-to-head decides, JCC prose as incumbent.
3. **blind_pass as default-on finalize latch with logged override** → **YES** — quality latch, not spend gate; override keeps Farrice sovereign.

## Merge: Swarm Apex mission (2026-07-07)

Farrice's platform-parity mission ("replace SuperGrok Heavy / Manus / Kimi OK Computer / Perplexity Labs+Comet natively") is merged into this plan as the **driving use-case of Waves 3+5**. Full mission plan, alignment answers, platform research briefs (Manus/Grok/Kimi/Perplexity mechanics, VERIFIED-labeled), and internal stack audit: `_active/harness/swarm-apex-2026-07-07/PLAN.md`. Headline design: upgrade the existing `/swarm` front door into a thin conductor (plan gate → unattended) whose patterns (`heavy`, `research`, `mission`, `browser`, `council`) run as native Workflow scripts — the one surface the audit confirmed does real schema-validated parallel fan-out (`collective-genius-council.workflow.js`). Wave 3's worker-envelope standard and JCC pilot, and Wave 5's modality registry + packaging automation, ship inside the Swarm Apex sessions.
