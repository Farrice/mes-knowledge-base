---
name: Forge OS — Genius Layer
skill: forge-os
type: system-infrastructure
---

# Forge OS — Genius Layer

> The system already forges world-class artifacts FROM artifacts (source → skill, prompt → skill,
> extraction → skill). The Forge closes the one true gap: bare concept in, production-grade
> artifact out — with the same deterministic rigor, plus two properties no single existing door
> owns: (1) artifacts are born instrumented for self-evolution, and (2) artifacts are model- and
> platform-agnostic by contract, adapted through a thin dialect layer instead of per-artifact
> rewrites.
(`skills/forge-os/SKILL.md`, 8,877 bytes, lines 8-13 — the skill's own epigraph, quoted verbatim)

This is a SYSTEM skill, not a person extraction: the Forge is the `/forge` front door across five
lanes (Prompt / Workflow / Skill / Agent / Plugin), and its "voice" is the shared F0–F7 spine
(translate → ground → compose → forge → gate → prove → wire → evolve), not a practitioner's
personality. Everything below is grounded in the skill's own build history — session solution
cards, the Wave 3 decision doc, and the engine prompts themselves — never in generic prompt-
engineering advice.

## How to Use This Skill (Model Calibration)

These are intuition primitives for running a forging spine, not a checklist to march through.
Absorb the Grounding Gate, the fidelity-honesty rule, and the five lane contracts below, then
forge from judgment — if the output mechanically stamps "F0 done, F1 done, F2 done" in order with
no real corpus underneath any of it, you have failed. The test: would the Forge's own standard
(the discipline behind the 3,400+ audited v2 prompts this system already ships) recognize this as
a genuinely forged artifact, or as something using Forge vocabulary as a skin over an improvised
guess?

Specifically:
- Do NOT announce the machinery. Never output "Running F1 GROUND now" or "entering F4 GATE" to the
  operator — run the Grounding Gate, then hand back the artifact and its receipt; naming the stage
  numbers to the operator turns a spine into a script.
- Do NOT let a thin corpus pass as a full one. A [GROUNDING MATERIAL] set with 3 loosely-related
  hits is not a corpus — either run the Grounding Sprint properly or ship the artifact marked
  `fidelity: low`, out loud, in the forge receipt. Silent padding is the single fastest way back to
  the 2026-07-07 generic-output failure this skill exists to prevent.
- This skill's specific texture is contract-first, not craft-first: every lane's Output Contract
  and Quality Gate are fixed BEFORE the creative pass, and Creative Latitude is a named zone inside
  that fixed shape, never an excuse to drift the shape itself.
- Polish-is-the-tell inverts here: a forged artifact that reads fluent, confident, and structurally
  perfect is not evidence it is good — it is exactly the shape a training-memory forgery takes.
  The tell is grounding, not prose quality: can every claim in Role & Activation and Execution
  Protocol be traced to a real corpus entry? If not, the fluency is the failure, not the fix.

## Anti-Patterns (Corrected, Dated)

- Forging a skill from transcripts/training memory instead of a receipted corpus — corrected 2026-07-07 (`docs/solutions/2026-07-07-transcript-only-extraction-generic-output.md`, 3,417 bytes): the Alex Suzuki DWA rebuild extracted from transcript alone and shipped output the operator called "very straightforward and to the point… didn't capture the style and essence… I wouldn't be able to use any of this to see results" — the fix is now forge-os's own F1 GROUND hard rule, stated verbatim in `SKILL.md`: "Forging from training memory is prohibited."
- A freshly forged engine prompt passing the structure audit while hiding fatal ambiguity for its real (cold) user — corrected 2026-07-14 (`docs/solutions/2026-07-14-cold-start-probe-anneals-new-engine-prompts.md`, 2,805 bytes): the first cold-start run of Prompt Forge's own engine, `references/prompts-v2/prompt-forge.md`, surfaced 7 real defects (undefined "wiring trio" jargon, a dangling F1 reference, frontmatter semantics living only in the upstream spec) before any of them shipped — F5 PROVE now runs a mandatory cold-start friction probe on every new engine prompt.
- Plugin packaging tempted toward a full lift before proof existed — resolved in the Wave 3 decision doc `references/plugin-forge-lift-plan.md` (5,065 bytes): "Lift now (full)" was explicitly rejected because "exposure risk is the one irreversible item," so Plugin Forge stays HARD-GATED on a verbatim operator lift token plus all four F-REV/F-CRE/F-SYS/F-REG fixtures passing in a single run — see the file's own line 51 recommendation: "lift partially — local-only, no marketplace, effective only when all four fixtures pass in a single run."
- Multi-expert composition collapsing into "expert soup" instead of one owned artifact — standing prevention rule in `docs/solutions/expert-composition-standard.md` (2,233 bytes): loading every plausible expert "delivers an output that is patched together, overconfident, or still generic," so F2 COMPOSE enforces the 5-slot standard (Spine / Differentiator / Mechanism / Craft / Risk Gate) with one owner and a Composition Ledger naming which experts were skipped and why.
- $0-tier Skill Forge runs quietly escalating into a paid research tier mid-sprint — closed in the 2026-07-15 refactor of `references/prompts-v2/grounding-sprint.md` (7,279 bytes): the file now states plainly that "running it without `--depth quick` at $0 tier is a tier violation," so a Grounding Sprint can no longer drift past its approved budget one `research.py` call at a time.
- The heartbeat auditor's own regex missing an equivalent contract heading and flagging honest work as failing — caught 2026-07-17 (`docs/solutions/2026-07-17-repair-fleet-poc-three-failure-shapes.md`, 5,899 bytes): "14 of luke-iha-vicious-hooks' 'missing' workflow contracts existed under `## Output Contract`; the auditor regex only matches `Output Schema/Format/Requirements`" — the exact shape that left forge-os's own `references/prompts-v2/*.md` files (which use "Output Contract" throughout) invisible to `workflow_contracts` until this 2026-07-17 repair pass added matching files under `skills/forge-os/workflows/`.

## Recognition Test

The bar, every forge run: would the Forge's own standard (`directives/prompt-forging-spec.md`, the
discipline behind the 3,400+ audited v2 prompts already in production) recognize this as a
genuinely forged artifact — corpus-traceable, contract-bound, fidelity honestly labeled — or would
it recognize this as an artifact using Forge vocabulary (Role & Activation, Output Contract,
Quality Gate) as decoration over an ungrounded improvisation? If the Grounding Gate was skipped, if
[GROUNDING MATERIAL] traces to nothing real, or if `fidelity: low` was never declared on a thin
corpus, rebuild it — that is precisely the failure F4 GATE and `execution/renaissance_audit.py`
exist to catch: a prompt that reads perfectly and grounds nowhere.
