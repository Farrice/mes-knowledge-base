# Forge Log — Cody Schneider Extraction

**Run**: 2026-08-06, overnight autonomy granted by Farrice. `/extract-forge` phase structure followed; the three human checkpoints were **self-approved with reasoning logged here** rather than paused on, per the mission grant.

**Phases skipped by instruction** (conductor owns them): Phase 0 session lock, Phase 6 registry generators (`sync_registries.py`, `generate_slash_commands.py`, slash wrappers), Phase 5.5 wiring commands (`renaissance_audit.py`, `prompt_library.py build`, `wire_prompt_pointers.py --write`), Phase 7.4a/c `blind_pass.py` invocations, Phase 8 finalize + `forge_gate.py`. Nothing under `.agent/`, `execution/`, `_active/`, or any registry file was written. The `<!-- BEGIN:execution-prompts -->` block was deliberately **omitted** from SKILL.md so `wire_prompt_pointers.py --write` inserts a clean generated section.

---

## Phase 1 — Source Acquisition ✅

Transcript (8,932 words) and 100 frames were already on disk; not re-fetched per instruction. Read the transcript in full. Read **16 frames selectively** at the demo timestamps rather than all 100:

| Frame | Timestamp ≈ | What it grounded |
|---|---|---|
| 0038 | 04:26 | LinkedIn "wordpress development" search — the *rejected* example, on camera |
| 0060 | 09:09 | apimaestro actor suite; reliability badges → the vendor-maintenance criterion (HK8) |
| 0069 | ~10:40 | **His own LinkedIn profile card** — "Graphed.com – Deploy AI Agents for Marketing", 2,894 profile viewers, **36,190 post impressions** → identity verification + P18 evidence |
| 0071 | ~11:30 | **The terminal**: `61 unique engagers extracted`, `Counter({'reactor': 52, 'commenter': 9})`, `obfuscated/no-slug: 52`, Exa-resolution next step, `Sauntered for 34s` → HK1, the blind-pass reference |
| 0074, 0128, 0140, 0145, 0151 | various | Talking-head — no new information; sampled to confirm frame timing |
| 0077 | ~16:00 | Origami landing page — aggregator positioning |
| 0080 | 15:45 | GetLeads.io — "402 million B2B contacts", tier-1 slot |
| 0086 | ~17:30 | Google Sheet with LinkedIn URLs + Gemini panel — the manual spreadsheet stage |
| 0091 | ~19:00 | Browser transition (no content) |
| 0095, 0112, 0120 | 25:38+ | Instantly — product nav and **pricing tiers $47 / $97 / $358 / custom** |
| 0100 | ~26:30 | Hypertide — "Automated Cold Email Infrastructure Across Google, Microsoft, and Entra" |
| 0134 | ~31:00 | **Architecture slide**: PIPELINE → WAREHOUSE → AGENT → BACK, THE BAN MYTH, "Reads come from the warehouse. Writes go through the API." → HK7 |

**Expert identity — VERIFIED.** Self-identified at 00:52; frame 0069 corroborates company and role. Transcript ASR garbles the company ("graft", "graph.com"); the frame is authoritative → **Graphed**. Host is Greg Isenberg. No transcription-tool misattribution risk.

**Dedup check — CLEAN.** `grep -ri "cody"` across `AGENT_INDEX.md`, `SKILL_INDEX.md`, `DOMAIN_REGISTRY.md` returned nothing; no `agents/cody-*` directory existed. This is a **new** expert, not an expansion. Note: `execution/signal_scout.py` already exists and cites "Cody Schneider doctrine (extraction 2026-08-06)" in its docstring — the tool was built ahead of the skill. Workflows wire to it rather than inventing parallel plumbing.

---

## CHECKPOINT 1 — Vision (after Phase 2) · **SELF-APPROVED**

`vision.md` written. Decision and reasoning:

**APPROVED, with one scope narrowing.** The uniqueness audit holds: no existing roster expert answers *how you know who to talk to before writing a word*. Business leverage concentrates in the top-right quadrant (signal doctrine + resonance→angle), which is directly deployable against Proof-to-Market and already half-implemented in `signal_scout.py`.

**Narrowing applied**: the sending half (infrastructure, DM tooling, autonomous reply agents) is demoted from "deployable capability" to "client-facing design knowledge," per Farrice's standing 2026-08-06 decision that sends stay human. This is not a loss — it removes exactly the material with the shortest shelf life, and keeps the half that compounds.

**Risk accepted**: one 44-minute source. Cody explicitly says "we don't have time today to go into all the finite details." Where he gestures rather than teaches (compliance checklists, hosting specifics, DM tooling depth), the extraction marks the gap and does not extrapolate. Recorded in `extraction-report.md` Part IX.

**Would Farrice have said no?** Unlikely on scope. The one thing he might have pushed on: whether an eleventh workflow is warranted for a single-source expert. Addressed at Checkpoint 2.

---

## CHECKPOINT 2 — Architecture (after Phase 4) · **SELF-APPROVED WITH MODIFICATIONS**

Extraction produced **18 genius patterns, 10 hidden-knowledge items, 5 exemplars, 8 signature moves, an 8-criterion rubric** — comfortably past the Deep-tier floor and past the virtuoso bar (12+ patterns, 5+ moves). The source is denser than its runtime suggests because he demos live and states numbers unprompted.

Architecture approved at **11 workflows / 3 tiers**, with these modifications to the suggested spine:

1. **Split "creator-list design" out of the front door.** The suggested spine put signal doctrine as one T1 block; aperture sizing earns its own workflow because it is the single artifact everything downstream inherits, and it has a machine-readable output (`signal_scout.py`'s creators file). Front door became `signal-system-blueprint` instead.
2. **Reply handling shipped as draft-only**, renamed accordingly, with "never sends" written into the frontmatter description, the pre-flight gate, and the quality gate. Three enforcement points, because one is how constraints get lost.
3. **Added `marketing-as-code-audit` (T3)** — the suggested spine had it; retained and sharpened, because the "invisible copy-paste work" step is where its value actually is, and that's a genuinely different deliverable from the agent-vs-automation verdict.
4. **Vendor quarantine enforced structurally.** Workflow bodies name *roles* (sourcing API, first-tier enricher, verifier, sending platform); vendors appear only in `references/era-bound-2026-08-stack.md`. This is checked in every workflow's quality gate. Rationale: the binding recency rule, and the fact that half this material has a ~12-month half-life.
5. **Declined**: a separate "compliance posture" workflow. He gestures at it and explicitly disclaims expertise twice. A workflow built on gestures would be the invented-pattern failure. It lives as a step inside `outbound-infra-blueprint` with his disclaimers carried forward verbatim.

**Would Farrice have said no?** The plausible objection is workflow count on a single source. Defense: every workflow maps to a *distinct deliverable* Cody actually demonstrates or specifies, and three (5, 6, 7) are explicitly marked client-facing rather than house-deployable. Nothing was padded to reach a number — the count fell out of the deliverables.

---

## Phase 5 / 5.5 — Build ✅

Written: `genius.md` (durable craft only), `references/era-bound-2026-08-stack.md` (the dated shell), 11 workflows, 11 born-v2 execution prompts, `SKILL.md`, `agents/cody-schneider/AGENT.md` + `memory/context.md`.

Fidelity note on the prompts: all 11 marked `fidelity: high`. Each Execution Protocol was written **from the extracted material**, not from training memory about outbound — every step traces to something he says or demonstrates. Where the source is thin (compliance detail, hosting), the prompts route or disclaim rather than fill.

---

## CHECKPOINT 3 — Verification (after Phase 7) · **SELF-APPROVED, SHIPPED A-MINUS**

Structural check: all 26 files present. Spot-read `engager-signal-audit.md`, `waterfall-design.md`, and `agent-or-automation.md` for practitioner grade — each carries a pre-flight gate, concrete numbered execution, adaptations table, output requirements, prompt pointer, and an anti-pattern-derived quality gate.

Blind pass run manually against the video's own live demo output (`blind-pass-log.md`) — **verdict PASS**, with two named gaps.

**Tier: A-minus.** Held back from a clean A because (a) reference corpus is a single source rather than ≥2 published artifacts, and (b) the sourcing math and enrichment hit-rates are unverified against Farrice's own niche — they're his numbers, not measured ones. Both are honestly named in the artifacts rather than papered over. A Farrice-judged pass on a real roster would promote it.

**Handoff to conductor**: run `renaissance_audit.py` → `prompt_library.py build` → `wire_prompt_pointers.py --write` → `sync_registries.py` → `generate_slash_commands.py` → `skill_auditor.py check --skill cody-schneider-signal-outbound` → `blind_pass.py record` → finalize.
