---
name: forge-os
description: The Forge — cornerstone generation suite. Raw intent → production-grade prompt / workflow / skill / agent / plugin through one front door (/forge), five lanes, and a shared spine (translate → ground → compose → forge → gate → prove → wire → evolve). Model-dialect adaptive and platform-portable. Extends the existing generators; never rebuilds them.
---

# Forge OS — Raw Intent → Production-Grade Artifact

> The system already forges world-class artifacts FROM artifacts (source → skill, prompt → skill,
> extraction → skill). The Forge closes the one true gap: **bare concept in, production-grade
> artifact out** — with the same deterministic rigor, plus two properties no single existing door
> owns: (1) artifacts are **born instrumented** for self-evolution, and (2) artifacts are
> **model- and platform-agnostic by contract**, adapted through a thin dialect layer instead of
> per-artifact rewrites.

## The Five Lanes

| Lane | Input | Output | Engine | Status |
|------|-------|--------|--------|--------|
| **Prompt Forge** | raw concept | one born-v2 structure-pure prompt + fixture | `references/prompts-v2/prompt-forge.md` | **LIVE (Wave 1)** |
| **Workflow Forge** | raw concept / repeated manual loop | `.agent/workflows/<name>.md` command with gates + verification | `references/prompts-v2/workflow-forge.md` | **LIVE (Wave 2)** |
| **Skill Forge** | raw concept (no source required) | full skill (SKILL.md + genius + workflows + v2 prompts) | Stage 1: `references/prompts-v2/grounding-sprint.md` (receipts-backed corpus) → existing `/extract-forge` pipeline | **Stage 1 LIVE (Wave 2)** |
| **Agent Forge** | raw concept or existing skill | `agents/<name>/` AGENT.md + memory + card | `references/prompts-v2/agent-forge.md` (promotion mechanics per `/create-agent`; no-corpus → SKILL-FIRST stop) | **LIVE (Wave 2)** |
| **Plugin Forge** | skill / prompt-set / workflow family | installable plugin (plugin-dev toolchain) | `references/prompts-v2/plugin-forge.md` — **HARD-GATED**: builds nothing without a verbatim operator lift token + 4/4 lift-plan fixtures in one run | **ENGINE READY · packaging gated (Wave 3)** |

**Routing honesty (never rebuild):** if the intent arrives WITH an artifact, the Forge front door
routes to the existing crown jewels — source material → `/extract-forge` or `/source-to-skill-system`;
existing prompt → `/convert-prompt`; finished extraction → `/convert-extraction`; perfected exemplar
→ `/design-skill-enshrine`. The Forge's own lanes fire only for bare-intent input or for the
instrument/portability passes no other door owns.

## The Shared Spine (every lane, in order)

- **F0 TRANSLATE** — Translation Card per `/raw-intent-bridge` Stage 0: anchor, deliverable,
  audience, felt standard VERBATIM, sharpened intent line. Felt-standard words travel to the
  forging model untouched; the sharpened line does the routing.
- **F1 GROUND** — the Grounding Gate. Search prompt_library + skills registry + Recall + episodic
  memory for owning expertise. Found → forge from that corpus (provenance guard). Not found →
  grounding sprint (deep-research with receipts) manufactures an honest corpus FIRST, or the lane
  flags `fidelity: low` and forges less. **Forging from training memory is prohibited**
  (docs/solutions/2026-07-07-transcript-only-extraction-generic-output.md).
- **F2 COMPOSE** — expert composition per the 5-slot standard (Spine / Differentiator / Mechanism /
  Craft / Risk Gate; docs/solutions/expert-composition-standard.md). One owner, bounded experts.
- **F3 FORGE** — draft per the owning spec: prompts → `directives/prompt-forging-spec.md`
  (HIGH FLOOR, UNLIMITED CEILING); workflows → command conventions + gates; skills → skill-system
  contract; agents → AGENT.md template; plugins → plugin-dev structure.
- **F4 GATE** — the deterministic layer: `renaissance_audit.py` (prompts), verifier scripts,
  prose/slop checks where prose ships. Existence ≠ done; audit-pass = done.
- **F5 PROVE** — live cold-start proof before registration: run the artifact on a real fixture in
  a fresh context. Skills use the baseline-vs-with-skill differential; blind-pass against the best
  in-library artifact of the same deliverable class backs any "top-1%" claim with a comparison it
  could lose.
- **F6 WIRE** — registration: prompt_library build + wire_prompt_pointers + SLASH_COMMANDS.md +
  invocation cards. An unwired artifact does not exist.
- **F7 EVOLVE (born instrumented)** — the artifact ships with 2–3 golden fixtures (input →
  expected output shape) and a failure-logging pointer, wiring it into the EXISTING evolution
  loop from birth: `/skill-anneal` (≥3 documented failures), `/self-evolve` (plateaued),
  `evolution_orchestrator.py` daily cycle. The Forge builds no new evolution engine.

## Self-Evolution Spine — the model-relearn tax, deleted

Artifacts stay **model-agnostic by contract**: the v2 Output Contract + Skeleton + Quality Gate
enforce shape regardless of model. Model-specific behavior lives in ONE place:

- **Model Dialect Cards** — `directives/model-dialects/<model>.md`, grown from
  `directives/model-notes.md`. Quirks, structured-output behavior, param rules, verbosity tells,
  instruction-following idioms.
- **`/forge dialect <model>`** (LIVE, Wave 2) — the standard P1–P8 probe battery
  (`references/prompts-v2/dialect-probe.md`) fingerprints a new model in one run and writes its
  card. New model ships → one card updates → the entire forged library adapts.
- **Compliance replay** — grown from `/test-model-compliance`: on model change, replay each
  artifact's golden fixtures, diff against expected shape, queue drift into the anneal loop.
  Deterministic backstop, never AI-memory-dependent observability (standing rule).

## Portability Spine — never trapped in one harness

The Platform Portability OS already owns cross-platform truth (per-platform constitutions +
`execution/platform_compiler.py` drift gate). The Forge compiles TO it: every forged artifact
keeps its methodology/contract core harness-neutral (plain markdown, bracket inputs, output
contracts) and isolates harness-specific wiring (hooks, frontmatter, tool names) in the thin
outer layer the platform compiler already manages. Result: prompts run anywhere; skills port by
constitution, not by hand-copying.

## Boundaries

- No global writes (`~/.codex`, `~/.claude`) without explicit ask. No plugin marketplace edits.
- Plugin lane stays deferred until Farrice lifts it explicitly and cold-start proof passes.
- Extractions are never gated (standing decision 2026-06-09) — the Forge inherits that: forge
  telemetry is telemetry, never a block.
- The Forge serves the whole system, unbounded by any single revenue goal (compass, never cage).

## Source Spine (provenance for this skill's own prompts)

`directives/prompt-forging-spec.md` · `.agent/workflows/raw-intent-bridge.md` ·
`.agent/workflows/source-to-skill-system.md` · `docs/solutions/expert-composition-standard.md` ·
`.agent/workflows/self-evolve.md` · `.agent/workflows/test-model-compliance.md` ·
`directives/model-notes.md`. Nothing in this skill is forged from training memory.

## Verification

After changing this skill or its prompts: `python3 execution/renaissance_audit.py` (0 fail) →
`python3 execution/prompt_library.py build` → `python3 execution/wire_prompt_pointers.py --write`.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

7 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Agent Forge — Concept or Skill → `agents/<name>/` Deployable Agent** — `skills/forge-os/references/prompts-v2/agent-forge.md`
- **Dialect Probe — New Model → One Dialect Card** — `skills/forge-os/references/prompts-v2/dialect-probe.md`
- **Grounding Sprint — Skill Forge Stage 1** — `skills/forge-os/references/prompts-v2/grounding-sprint.md`
- **Forge Front Door — Translation Card + Lane Decision** — `skills/forge-os/references/prompts-v2/intent-translation-card.md`
- **Plugin Forge — Proven Asset Family → Installable Plugin** — `skills/forge-os/references/prompts-v2/plugin-forge.md`
- **Prompt Forge — Bare Concept → Structure-Pure v2 Prompt** — `skills/forge-os/references/prompts-v2/prompt-forge.md`
- **Workflow Forge — Bare Concept / Manual Loop → `.agent/workflows/<name>.md`** — `skills/forge-os/references/prompts-v2/workflow-forge.md`

<!-- END:execution-prompts -->
