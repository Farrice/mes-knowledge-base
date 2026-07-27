# Skill Craft Standard — How We Build Skills/Agents/Workflows That Actually Work

> **Origin**: Farrice, 2026-07-06 — "I've never really understood how to build them out properly... best practices that actually result in amazing results and remarkable output consistently." This file is the answer, grounded in this repo's own evidence (not generic advice). Synthesizes `directives/embodiment-standard.md` (the blind-pass gate), `directives/mes-3.0-extract.md` (density mandate), and Anthropic's skill-authoring conventions (`~/.claude/plugins/.../writing-skills/`), adapted where they fit.
> **Consumers**: `.agent/workflows/extract.md`, `.agent/workflows/extract-forge.md`, `directives/mes-3.0-extract.md`, `execution/skill_auditor.py`. This is the pre-ship checklist — point here, don't duplicate.

## 1. The Heartbeat Test

A skill is not documentation. **It is a thinking transplant** — it exists so a fresh context window can make the same judgment calls the source expert would, on inputs the expert never saw. The acceptance question, every time: *would the expert recognize this as theirs, or as someone wearing their vocabulary?*

Evidence this is the real failure mode, not a hypothetical: E1's factory audit found the extraction pipeline verified **structure** (files exist, sections present) but never **embodiment** — and E3's blind bake-off proved the gap: Farrice detected real experts only 5/15 of the time, and *preferred* skill-generated work 8-6-1 once skills were built to the embodiment standard (`_active/elevation-track/e3/E3-results.md`). "Loading files ≠ embodying thinking. Structure without heartbeat = 5/10 max" is the standing lesson.

Heartbeat in practice, verbatim from `skills/claim-safe-health-marketing/genius.md`: GP-08, "The Two-Experts Test" — *"would a supplement regulatory attorney AND a direct-response copywriter both sign off unchanged?"* That is a judgment call compressed into a one-line recognition test, not a topic summary. Compare the anti-example: `skills/kallaway-content-operating-system/references/genius-patterns.md` (43 lines) reads as a components list — no recognition test, no named judgment call, nothing to run in your head before writing.

## 2. Anatomy — One Customer Per File

Each file in a skill has exactly one reader. Writing to the wrong reader is the single most common cause of a thin skill.

**`SKILL.md` → written FOR THE ROUTER.** Its job is triggering, not teaching. Per Anthropic's own skill-authoring guidance (superpowers `writing-skills`): description = when-to-fire, never a workflow summary — a description that explains the process becomes a shortcut the router takes *instead of* reading the skill. This repo extends that with two more router-facing fields the base convention doesn't have: `domain` (BM25/embedding-matched keywords) and `when_to_use` (concrete trigger scenarios), plus a expected **when-NOT-to-use** line. `skills/claim-safe-health-marketing/SKILL.md` does all three (lines 3-5, and the full "When NOT to Use This Skill" table routing to `alan-aragon-nutrition`, `jw-engine`, and naming an explicit capability gap rather than pretending coverage). Contrast `skills/nate-herk-client-acquisition/SKILL.md`: 21 lines, no `domain` field, no `when_to_use` field, no when-NOT-to-use — it is architecturally invisible to keyword/embedding routing no matter how good its genius.md is. This is the exact bug fixed 2026-07-06 across the roster; the lesson is durable, not a one-time cleanup.

**`genius.md` → the brain.** Patterns WITH the why, not topic headers. Anti-patterns FROM REAL FAILURES with dates. Exemplars quoted verbatim (+ ≥1 anti-exemplar). A decision rubric anchored at named levels. Evidence of density mattering: `skills/satori-graphics/genius.md` (516 lines, 17 patterns) and `skills/claim-safe-health-marketing/genius.md` (208 lines, 9 patterns, 11 hits on anti-pattern/exemplar/rubric/VERIFIED-LIKELY-UNCONFIRMED language) both read as operating systems you can run a judgment through. `skills/liam-ottley-linkedin-lead-magnet/genius.md` is 124 lines — comparable length to claim-safe's 208 at a glance — but only 1 hit on that same grep: it has prose, not a rubric, not named exemplars. Length does not predict quality; pattern *density* (anti-patterns, exemplars, rubric anchors, named entities per the source-ledger discipline) does.

**`workflows/` → executable.** Every step names its tool/command, not a vague instruction. Every workflow has an Output Schema and a Quality Gate. `skills/claim-safe-health-marketing/workflows/04-pre-launch-compliance-gate.md` produces a named artifact (Go/No-Go verdict: SHIP/HOLD/BLOCKED) — that is executable. A workflow that says "review the copy for compliance issues" is not; it is a paragraph wearing a filename. `skills/kallaway-content-operating-system` has exactly 1 workflow file for an "operating system" — structurally thin regardless of how good the prose inside it is.

**`references/` → the source ledger.** Timestamp → signal → translation, with VERIFIED/LIKELY/UNCONFIRMED labels per claim (`skills/claim-safe-health-marketing/references/source-ledger.md`; genius.md's own "Source Caveats" section labels practitioner track-record claims LIKELY while regulatory mechanics are VERIFIED against primary sources). A skill with no source ledger is a skill nobody can audit for hallucinated authority.

## 3. Extraction Discipline (`/extract`, `/extract-forge`, MES 3.0)

- **Source-fit gate BEFORE deep work.** `.agent/workflows/extract-forge.md` Phase 1-2 exists precisely so a session doesn't sink hours into a source that can't support a real extraction — validate fit first, always.
- **Density over length, never pattern-lock.** `directives/mes-3.0-extract.md`'s Virtuoso Density Mandate: "Do not use 1,000 words if 200 words of lethal, paradigm-shifting insight will achieve the goal" — and its Anti-Pattern Lock: extract the *mechanics* of an example, discard the skin, never recycle the example's specific scenario as if it were the principle.
- **Voice verbatim, not paraphrased.** Exemplars are quoted from real published work with provenance, never invented "in the style of."
- **QC = diff against the expert's real published work**, never self-referential (`directives/embodiment-standard.md`'s Blind-Pass Protocol: generate 1-2 outputs, place beside real verbatim pieces, judge against the recognition test — PASS = indistinguishable or preferred). For non-person extractions with no single voice to blind-pass (claim-safe-health-marketing is the precedent), the adapted QC is diffing against real compliant ad copy + real enforcement language instead of one expert's prose — name the adaptation explicitly, don't skip the check.
- **Anti-Overpolish Rule**: E3's only consistent detection signal was that AI reads "teed-up, polished, overexplaining" while real experts read "conversational, rhythm, imperfection" — Farrice misjudged a real Hormozi post as AI *because it was too polished*. Preserve texture; don't tidy fragments into essay prose.
- **Scores are earned, never pre-written.** The old workflow text hardcoded `--intent 8 --expert-score 9` — every extraction scored identically regardless of quality (E1 finding). Scores now derive from the blind-pass verdict + checklist coverage; any dimension ≥8 requires naming the matching anchor in `evolution_store/ground_truth/rubric_v1.md`.

## 4. The Consistency Loop

A skill that ships once and is never checked again decays invisibly. Every new skill must:

1. Ship with **≥1 eval_set entry** appended to `evolution_store/ground_truth/eval_set_v1.jsonl` (the blind-pass result, not a vibe).
2. Register in frontmatter correctly the first time — run `sync_registries.py` if you touch frontmatter, so `SKILL_INDEX.md` reflects reality.
3. Enter `skill_benchmark`/evolution tracking so drift is visible, not assumed.
4. **A-tier promotion is Farrice-judged only** — self-judgment ships B-tier with the gap named; it never self-promotes to A. `execution/skill_auditor.py`'s tier classifier (A/B/C/REVIEW/UTILITY) backs this with structural + trace + cross-reference signal, but the A-tier bar in the standard is human, not just structural.

## 5. Agents (Personas) — Identity, Not Method

`AGENT.md` carries **WHO** (identity, judgment priors, memory/) — the skill carries **HOW** (method, workflows, rubric). Conflating the two is why "more experts stacked" degrades output: Diandra's engine tested 4/10 the moment her hooks-only voice got wired into body copy alongside other authors' methods (`feedback_diandra-hooks-only-separation.md`) — one author writes the body; a persona's voice is not a drop-in module for someone else's structure. Every agent needs an **invocation card** in `agents/_framework/invocation-cards.md` for Tier-0 discoverability — an agent nobody can find is an agent that doesn't exist for routing purposes, same bug as a skill missing `domain`/`when_to_use`.

## 6. Workflows — Conductor vs. Procedure

**Conductors** compose existing skills/agents; they point, they never duplicate the pointed-to content, and they stay ≤250 lines (e.g., `how-i-write-os`, `/jw-engine`). **Procedures** execute a method directly, with named tools/commands at every step and an explicit Output Schema (e.g., `skills/claim-safe-health-marketing/workflows/01-claim-audit.md`). Frontmatter hygiene matters for both: `routing: long-tail` demotes a workflow from default routing on purpose (see `kallaway-content-operating-system`'s frontmatter) — use it deliberately, not as a way to avoid writing a real `when_to_use`.

## 7. The 8 Deadly Anti-Patterns

1. **Structure without heartbeat.** Full file tree, zero judgment calls inside it. (E1/E3 root cause, Section 1.)
2. **Router-blind frontmatter.** No `domain`, no `when_to_use`, or a description that summarizes workflow instead of triggers — the skill exists but is invisible to routing (`nate-herk-client-acquisition`, pre-fix roster-wide 2026-07-06).
3. **Templated scores.** Finalize numbers written into workflow text before the work exists (`--intent 8/9` hardcoding, E1).
4. **Self-referential QC.** Judging output against the skill's own prior output instead of the expert's real published work (the embodiment-standard's entire reason for existing).
5. **Topic summary masquerading as genius.md.** Headers and prose with no anti-patterns, no exemplars, no rubric, no named entities (`kallaway-content-operating-system` genius-patterns.md).
6. **One-workflow "operating system."** Naming implies breadth the file count doesn't deliver — a real OS has ≥3-5 executable workflows with distinct outputs, not one file wearing a grand title.
7. **Voice stacking.** Multiple experts' methods wired into one body of output instead of one author's voice carrying the piece (Diandra 4/10 lesson, Section 5).
8. **Overpolish as a proxy for quality.** Smoothing out the source's rhythm/fragments/imperfection in the name of "cleaning it up" — this is the #1 thing that reads as AI, per E3's blind notes.

## 8. Build Checklist — Run Before Finalize

- [ ] `SKILL.md` frontmatter has `domain` (keyword-rich, BM25/embedding-matched) and `when_to_use` (concrete trigger scenarios) — not description-only
- [ ] `SKILL.md` has an explicit "When NOT to Use" section naming the nearest alternate skill(s)
- [ ] `genius.md` exists and contains: ≥1 named recognition test, ≥5 anti-patterns each traceable to a source, a decision rubric anchored at named levels (not just numbers)
- [ ] ≥3 verbatim exemplars + ≥1 anti-exemplar, provenance-labeled
- [ ] Every genius pattern carries ≥1 proper noun / number / verbatim quote (zero-entity patterns fail `skill_census.py`)
- [ ] `references/source-ledger.md` (or equivalent) with VERIFIED/LIKELY/UNCONFIRMED per claim
- [ ] ≥1 real workflow in `workflows/`, each naming its tool/command, with an Output Schema and a Quality Gate
- [ ] No workflow file contains a pre-written finalize score (`--intent 8` etc.) — scores come from the blind-pass verdict, always
- [ ] Blind-pass run per `directives/embodiment-standard.md`: PASS/FAIL recorded, verdict appended to `evolution_store/ground_truth/eval_set_v1.jsonl`
- [ ] Frontmatter registered via `sync_registries.py` if touched — confirm `SKILL_INDEX.md` reflects the new skill accurately
- [ ] If this extends an existing persona/skill, confirm it does NOT get wired into another author's body copy (voice-stacking check, Anti-Pattern 7)
- [ ] A-tier claimed only with a Farrice-judged pass named explicitly in the finalize notes — otherwise ship B-tier with the gap stated
- [ ] **Menu parity (heartbeat check 7, physical since 2026-07-25)**: every `workflows/*.md` is fireable from the slash menu — a same-stem `.claude/commands/` shim OR an `.agent/workflows/` wrapper referencing `skills/<skill>/workflows/<file>` — or carries a NAMED exemption in its frontmatter (`menu_exempt: <reason>`, `status: superseded`, or `superseded_by: <file>`). Variant/backup artifacts (`.variant.`, `.pre-evolution.`, `backup`) are auto-excluded. Enforced by `skill_auditor.py check` (tier-affecting; root cause: 2026-07-25 riley-brown forge shipped 12 fireable-but-not-in-menu workflows because wrapper minting was a manual step)

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-07-06 (authored) |
| **Activation Count** | 1 |
| **30-Day Review Date** | 2026-08-05 |

*Created: 2026-07-06.*
