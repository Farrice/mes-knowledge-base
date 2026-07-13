---
description: Turn source material into a connected Codex skill system with components, handoffs, checkpoints, validation, cold-start proof, and agentic engineering loops for context engineering, review loops, dependency safety, package safety, and source truth
---

# /source-to-skill-system - Source To Skill System Pilot

Build an end-to-end Codex skill system from source material. Use this when a video, transcript, article, book, or raw method should improve the operating system itself or become a reusable orchestrated capability.

This is the pilot implementation of `semantic_libraries/antigravity/primitives/skill-system-contract.md`, grounded first in:

`extractions/video-context/FD53kEpLh9c/`

Agentic engineering source harvests are also grounded in:

`extractions/video-context/PzVV4X37ihg/`

Entrepreneurial operator excellence example corpus:

`extractions/dom-iacovone/multi-company-operator/`

Use this corpus as a concrete example of a source that became both a harness
primitive and a cold/on-demand skill surface because it contains reusable
mechanics across SGM planning, stage-gate innovation, delegation, channels,
financial leakage, launch readiness, and exit optionality.

## Operator Core Alignment

This workflow is the canonical source of truth for Source-to-skill-system behavior.
Global and local Source-to-skill-system wrappers must stay thin
compatibility wrappers that point back here, not competing behavior contracts.

Preserve these invariants:

- `/source-to-skill-system` turns source material into connected skill systems, not isolated mega-skills.
- Evidence and existing-route fit come before building.
- Every build needs the Skill System Contract fields before implementation.
- Agentic engineering changes require the Agentic Engineering Packet.
- Self-improvement, maintenance, cleanup, or evolution changes require a Goal Packet.
- Prefer companion OS layers over duplicate expert skills when source material improves existing control-plane behavior.
- Do not create hot skills, global mirrors, external writes, new dependencies, or broad workflow mutations without explicit approval and validation.
- Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`; use `/source-to-skill-system` for explicit source-to-system conversion.
- Real Codex subagents require explicit authorization.

## Pre-Flight Reads

1. `CODEX.md`
2. `semantic_libraries/antigravity/primitives/skill-system-contract.md`
3. `semantic_libraries/antigravity/primitives/source-to-skill-extraction.md`
4. `semantic_libraries/antigravity/primitives/agentic-engineering-loop-contract.md` when the source teaches agent harnesses, context engineering, review loops, dependency safety, source-code-as-truth, or launch/use-now behavior
5. `semantic_libraries/antigravity/primitives/goal-loop-maintenance-contract.md` when the source teaches self-improvement, maintenance, cleanup, forge, or evolution loops
6. `semantic_libraries/antigravity/primitives/behavior-changing-extraction-contract.md`
7. `semantic_libraries/antigravity/primitives/co-creative-launchpad-contract.md` when the source improves prompt intent, co-creation, question quality, front-door routing, or pre-execution alignment
8. `semantic_libraries/antigravity/primitives/how-i-write-harvest-spine.md` when the source is a `How I Write`-style expert writing, comedy, copy, storytelling, or communication interview
9. `.agent/workflows/extraction-governor-agent.md`
10. `extractions/video-context/FD53kEpLh9c/analysis.md` when running the pilot video
11. `extractions/video-context/FD53kEpLh9c/video-context-ledger.md` for timestamped evidence
12. `extractions/video-context/FD53kEpLh9c/uncertainty-report.md`
13. `extractions/video-context/PzVV4X37ihg/analysis.md` when running the agentic engineering harvest
14. `extractions/video-context/PzVV4X37ihg/video-context-ledger.md` for timestamped spoken evidence
15. `extractions/video-context/PzVV4X37ihg/uncertainty-report.md` for the transcript-only evidence limit
16. `extractions/video-context/ogTLWGBc3cE/analysis.md` when running the Nate B. Jones co-creative launchpad harvest
17. `extractions/video-context/ogTLWGBc3cE/video-context-ledger.md` for timestamped spoken evidence and source limits

## Routing Stack

Run targeted routing before proposing a build:

```bash
python3 execution/command_menu.py search "[source/system goal]"
python3 execution/workflow_router.py search "[source/system goal]"
python3 execution/routing_governor.py evaluate "[source/system goal]"
python3 execution/expert_router.py route "[source/system goal]"
python3 execution/context_retriever.py search "[source/system goal]" --top 8
```

## Skill System Contract

Every run must fill these fields before implementation:

| Field | Required Output |
|---|---|
| Source evidence | URL, local source package, transcript/file path, and uncertainty limits |
| Objective | One specific system outcome |
| Components | Existing/new skills, workflows, scripts, agents, and references |
| Step order | Ordered phases with dependency rules |
| Inputs | What each step needs |
| Outputs | What each step produces |
| Handoff summary | Boundary summary between each step |
| Human checkpoint | Approval/review point or explicit skip reason |
| Validation | Commands or checks to prove the system works |
| Behavior-changing proof | Before/after, cold-start run, applied scenario, or transformed artifact proving the source changes real behavior |
| Result surface | How Farrice consumes the output |
| Context policy | What stays hot, cold, or on-demand |
| Reuse hook | Where this becomes a reusable route, skill, or primitive |
| Goal packet | Required when the source changes self-improvement, maintenance, skill evolution, or cleanup behavior |
| Agentic engineering packet | Required when the source changes context policy, review loops, dependency safety, source truth, or launch/use-now behavior |

## Default Order Of Operations

1. **Acquire source evidence** with `/video-context-ledger`, file reads, OCR, or supplied text.
2. **Classify build shape**: component skill, reference, workflow, skill system, companion OS layer, or no build.
3. **Route existing arsenal** so the system extends rather than duplicates.
4. **Apply agentic engineering rules** when relevant: context sweet spot, source truth, plan-then-shrink, small chunks, review-until-stop, dependency safety, structure cleanup, and use-now artifact.
5. **Apply co-creative launchpad rules** when relevant: predicted need, flashlight center, edges, what good looks like, data/opinion/source separation, senior-partner pushback, execution-changing questions, route handoff, and proof gate.
6. **Draft the contract** using the table above.
7. **Build the minimum durable surface**: semantic primitive, workflow, command bridge, reference, or skill.
8. **Validate each boundary** with router checks, file checks, contract checks, and cold-start proof.
9. **Require behavior-changing proof** before calling any capability-enhancing extraction complete. For copy, content, sales, or persuasion sources, this means a before/after transformation with diagnosis, source mechanic, behavior delta, proof object or proof gap, and next gate. For workflow, operations, or agent-system sources, this means a cold-start run that shows input, selected route, produced output, validation, and handoff.
10. **For `How I Write`-style writing/comedy/storytelling harvests**, keep the reusable spine elastic: reuse gates and proof requirements, not a rigid expert template.
11. **Close with starter route**: exact first command, first artifact, quality bar, and reuse hook.

When the source is a self-improvement or maintenance method, prefer a companion
OS layer over a duplicate expert skill. Build the method into the relevant
control-plane workflows and verifiers, then keep expert packages hot/cold
according to `CODEX.md`.

When the source teaches agentic engineering, prefer a companion OS layer over a
new hot command. Encode the method into existing control-plane workflows and
verifiers so future runs inherit better context, source-truth, review, safety,
and launch behavior without expanding the live skill surface.

## Pilot Contract

| Field | Pilot Value |
|---|---|
| Source evidence | `extractions/video-context/FD53kEpLh9c/video-context-ledger.md`; transcript-only package with visual/OCR unavailable |
| Objective | Teach Codex Antigravity to build skill systems instead of isolated skills or mega-skills |
| Components | `/video-context-ledger`, `/extraction-governor-agent`, `/source-to-skill-system`, `/mission`, `/self-evolve`, `/skill-anneal`, `command_menu.py`, `workflow_router.py`, `validate_skill.py` |
| Step order | source capture -> build-shape decision -> contract -> system patch -> validation -> starter route |
| Inputs | source URL or package path; user goal; existing arsenal routing results; approval boundary |
| Outputs | contract, semantic primitive, workflow bridge, validation report, first-use sequence |
| Handoff summary | Use the Skill System Handoff shape from the primitive |
| Human checkpoint | Required before broad archive/delete/external action; skipped for local reversible Codex Antigravity edits once approved |
| Validation | `verify_codex_authority.py`, `verify_skill_system_contract.py`, router parity checks, `validate_skill.py source-command-source-to-skill-system` |
| Behavior-changing proof | Cold-start proof or applied transformation required when the source claims to enhance a capability |
| Result surface | concise plan or artifact in conversation, with local source files for persistence; human-facing Markdown sources open as readable documents with metadata in sidecar JSON |
| Context policy | keep front doors hot; keep migrated command library cold behind routers |
| Reuse hook | use this workflow for future source-to-OS upgrades |

## Agentic Engineering Harvest Contract

| Field | Harvest Value |
|---|---|
| Source evidence | `extractions/video-context/PzVV4X37ihg/video-context-ledger.md`; transcript-backed package with frame/OCR evidence unavailable |
| Objective | Teach Codex Antigravity to run agentic engineering loops instead of vague vibe-coding loops |
| Components | `/source-to-skill-system`, `/expert-composition-governor`, `/self-evolve`, `/system-audit`, `agentic-engineering-loop-contract.md`, `verify_agentic_engineering_loop_contract.py` |
| Step order | source capture -> principle harvest -> existing-route fit -> companion OS contract -> workflow patch -> verifier -> router/cold-start proof |
| Inputs | source URL or package path; user goal; router output; source evidence; approval boundary |
| Outputs | semantic primitive, workflow integration, dependency safety rule, verifier output, cold-start prompt |
| Handoff summary | Pass exact source paths and the Agentic Engineering Packet, not full transcript dumps |
| Human checkpoint | Required before installing risky dependencies, broad routing changes, global edits, or external actions |
| Validation | `verify_agentic_engineering_loop_contract.py`, router checks for agentic engineering/context engineering/small PR/package safety, and relevant control-plane verifiers |
| Behavior-changing proof | Cold-start run showing input, selected route, produced output, validation, and handoff |
| Result surface | concise conversation closeout plus local primitive/workflow/verifier files |
| Context policy | keep the contract hot through workflow references; load transcript/source package only on demand |
| Reuse hook | use this contract for future agent-harness, context-engineering, dependency-safety, and review-loop upgrades |

## Quality Gate

Reject the run if it:

- creates a giant all-purpose skill instead of component systems
- adds a new skill without checking existing routes
- skips source grounding
- lacks handoff, checkpoint, or validation fields
- lacks behavior-changing proof when the source claims to improve a capability
- depends on hidden chat context rather than local files
- changes mutation-capable evolution behavior without a Goal Packet, proof artifact, stop condition, and wake-up check
- turns agentic engineering into a broad new command instead of an additive companion OS layer
- installs or recommends new packages without a dependency safety gate when package risk is relevant
- starts a review/fix loop without a measurable finish line or turn cap

## Starter Invocation

```bash
/source-to-skill-system https://www.youtube.com/watch?v=FD53kEpLh9c&t=59s
/source-to-skill-system https://www.youtube.com/watch?v=PzVV4X37ihg&t=419s
```

## Verification

After changing this workflow, run:

```bash
python3 execution/sync_operator_core_source_to_skill_system.py --check
python3 execution/verify_operator_core_source_to_skill_system.py
python3 execution/validate_skill.py source-command-source-to-skill-system
python3 execution/verify_skill_system_contract.py
python3 execution/verify_behavior_changing_extraction_contract.py
python3 execution/operator_core_status.py --plain
python3 execution/verify_operator_core_status.py
python3 execution/verify_system_control_plane.py
python3 execution/codex_live_surface_audit.py --strict
python3 execution/codex_harness_check.py
```

---

## Prompt Forging Gate (MANDATORY since 2026-07-13 — spec: `directives/prompt-forging-spec.md`)

Any skill this workflow creates, converts, or enriches ships with its execution layer — no exceptions:
1. **Born-v2 prompts**: one structure-pure v2 prompt per distinct deliverable (typically 4-10) in `skills/<skill>/references/prompts-v2/` — Role & Activation (real credentials only), Input Required, Execution Protocol at full depth FROM THE EXTRACTED MATERIAL (never training memory), Output Contract, Output Skeleton (placeholders only), Quality Gate, Deploy When. Fidelity rule: thin source → fewer/deeper prompts, flag `fidelity: low`, never invent.
2. **Wire (all four)**: `python3 execution/renaissance_audit.py` (0 fail) → `python3 execution/prompt_library.py build` → `python3 execution/wire_prompt_pointers.py --write` → `Execution prompt:` cross-ref line under each workflow's output step.

A skill without prompts is half-finished work — do not register or close out without this gate passing. The load-time menu hook (`execution/hooks/prompt_menu_hook.py`) flags violations at every future load.
