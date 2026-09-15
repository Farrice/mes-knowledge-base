# Mastery Transfer Proof Spine — Implementation Contract

**Mode:** `SHADOW`
**Owner:** `/source-to-skill-system`
**Optional learning surface:** `/operator-school` through explicit `/embody`
**Approval:** Farrice approved this workspace-local build and the Oren funnel-flywheel pilot on 2026-08-26.

## Skill System Contract

| Field | Contract |
|---|---|
| Source evidence | Existing source-to-skill contracts, `execution/skill_benchmark.py`, `execution/blind_pass.py`, the repeatability spine, the Jason Fladlien mastery benchmark, and `extractions/oren-1person-ai-marketing/funnel-flywheel-2026/`. |
| Objective | Add one evidence ladder between runnable capability and surpassing claims, plus an operator-invoked loop for embodying one judgment unit from an extraction or session. |
| Components | New SHADOW semantic primitive and deterministic verifier; existing behavior-changing, skill-system, source-to-skill, blind-pass, benchmark, repeatability, and outcome tools; `/operator-school`; thin `/embody` bridge; Oren pilot manifest and report. |
| Step order | Existing source proof -> runnable behavior proof -> transfer proof -> generalization proof -> blind preference -> field evidence -> dimension-bounded surpassing; optional `/embody` runs beside this chain and never changes proof state by itself. |
| Inputs | Capability home, source paths, current proof artifacts, comparison baseline, named performance dimension, held-out/negative cases when available, and optional session or extraction pointer for `/embody`. |
| Outputs | Honest proof-state manifest, verifier receipt, next missing proof, Oren SHADOW pilot report, and an in-session embodiment loop or explicitly requested persistent learning record. |
| Handoff summary | Pass source paths, current highest earned state, failed or untested rung, preservation locks, evaluator independence, field-event state, and next evidence action. |
| Composition rule | `/source-to-skill-system` owns proof progression. Existing tools keep their native jobs. `/operator-school` owns learning; `/embody` is only a thin explicit bridge. No new extraction owner or mega-skill. |
| Human checkpoint | Required before promotion beyond SHADOW, any global mirror, automatic invocation, external use, or a claim of field validity or surpassing. |
| Validation | Deterministic valid/invalid manifest tests, Oren package validators, positive `/embody` discovery, negative deliberation-route control, explicit-only skill policy, source-to-skill verifiers, and control-plane checks. |
| Behavior-changing proof | Oren is evaluated against existing commercial, neutral, and negative-control evidence. The pilot must reject `GENERALIZED`, `BLIND_PREFERRED`, `FIELD_VALIDATED`, and `SURPASSING` unless their evidence is actually present. |
| Result surface | Conversation receipt plus local primitive, verifier, command bridge, pilot manifest, and pilot report. |
| Context policy | Keep the proof ladder and `/embody` entry contracts hot only when invoked; load detailed source packages, benchmark cases, and learning records on demand. |
| Reuse hook | Apply the proof ladder to capability-enhancing extractions; invoke `/embody` manually on a source path or the current session when Farrice wants personal practice. |

## Agentic Engineering Packet

| Field | Contract |
|---|---|
| Objective | Make proof progression and discretionary embodiment reproducible without another broad runtime. |
| Source truth | Exact canonical files and Oren artifacts named above; no external source fetch or remembered evidence. |
| Context plan | Load contracts and the current proof rung; keep raw media, unrelated experts, and full session history cold. |
| Work chunks | Primitive/schema -> verifier/tests -> Oren manifest/report -> operator-school mode -> `/embody` bridges -> route/control verification. |
| Review loop | One implementation pass and one focused repair pass; stop when valid manifests pass, known overclaims fail, Oren reports its highest earned state, and `/embody` remains explicit-only. |
| Dependency gate | Standard library only; no package install or paid tool. |
| Structure pass | Confirm no duplicate proof tool, extraction owner, teaching OS, or hot global surface was introduced. |
| Use-now artifact | `/embody <extraction-path>` or `/embody this session` and the Oren proof-state report. |
| Hardening proof | Unit tests, verifier receipts, Oren validators, route probes, wrapper validation, and Operator Core checks. |

## Goal Packet

| Field | Contract |
|---|---|
| `target` | Mastery-transfer proof state and opt-in embodiment behavior in the current isolated lane. |
| `scope` | Canonical semantic/workflow surfaces, deterministic local scripts/tests, command bridges, and Oren pilot artifacts. Excludes global `~/.codex`, automatic invocation, external action, and unrelated skills. |
| `per_item_criteria` | Each file must have one owner, an observable purpose, source or contract grounding, and a direct verifier or route probe. |
| `permitted_side_effect` | Workspace-local files and branch commits only. Main-tree merge remains guarded by lane machinery. |
| `proof_artifact` | `mastery-transfer-shadow-pilot.json`, `mastery-transfer-shadow-report.md`, verifier output, and `/embody` command verification. |
| `measurable_stop` | All focused tests pass; Oren is not promoted above supported evidence; `/embody` is explicitly invokable and not implicitly selected; relevant control-plane checks pass. |
| `turn_cap` | One build pass plus one repair pass after the first full verifier run. |
| `evaluator` | Standard-library validators and existing Oren/control-plane validators. Human or isolated blind judgment remains required for `BLIND_PREFERRED`. |
| `wake_up_check` | `python3 execution/verify_mastery_transfer_proof_spine.py --pilot extractions/oren-1person-ai-marketing/funnel-flywheel-2026/mastery-transfer-shadow-pilot.json` and `python3 execution/verify_embody_command.py`. |
| `human_checkpoint` | Farrice must approve promotion, automatic invocation, external use, or global mirroring. |
| `rollback_or_archive_rule` | Keep the branch parked or revert its bounded commits; never delete source packages or prior proof artifacts. |

## Evolution Council Verdict

- **Target:** proof progression and discretionary operator embodiment
- **Goal packet complete:** yes
- **Recommended path:** smallest companion primitive plus thin explicit bridge
- **Permitted side effect:** workspace-local branch changes
- **Proof artifact:** Oren SHADOW pilot and deterministic verifier receipts
- **Stop condition:** focused and control-plane checks pass without proof inflation or implicit invocation
- **No-regression check:** existing source-to-skill and Oren routes still pass; deliberate council requests remain owned by `/convene`
- **Human checkpoint:** promotion or global/automatic behavior
- **Open risk:** current Oren evidence was built during development and has no independent blind preference, delayed replay, or market event
