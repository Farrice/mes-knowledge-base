# Skill System Contract: Shaan Puri Story Deployment

**Status:** Checkpoint 3 validated locally; architecture approved by Farrice on 2026-08-02

**Build shape:** Bounded in-place expansion of `skills/shaan-puri-storytelling/`
**Source boundary:** One public, transcript-backed interview; no universal, causal, or market-performance claims

## Contract

| Field | Contract value |
|---|---|
| Source evidence | Public source `https://www.youtube.com/watch?v=GlTA4wXSACE`; canonical local package `extractions/video-context/GlTA4wXSACE/`; 3,211 timestamped transcript segments; 24,480 clean words; verifier-passing evidence ledger; sampled frames; automatic captions without speaker labels; story-as-tool boundary at 00:25:37-00:25:58; adjacent-field study principle at 01:44:41-01:44:55 |
| Objective | Let Codex decide whether a communication task needs a full story, a truthful story fragment, or no story, then deploy the smallest source-backed Shaan mechanic through one appropriate production owner without distorting facts. |
| Components | New canonical `shaan-story-deploy` workflow, one matching born-v2 router prompt, a compact Story Deployment Map, the six current Shaan workflows, exact-stem born-v2 prompts for those six existing workflow deliverables, Story Compass, How I Write, existing adjacent-field transfer routes, command bridges, current verification scripts, and a detached behavior-proof artifact. |
| Step order | Source truth -> deployment decision -> conditional story diagnostic -> one selected production route -> truth and quality gates -> final asset plus Story Deployment Receipt. |
| Inputs | Decision-critical minimum: objective, raw facts or source material, and truth-risk class. Presentation context—audience relationship, medium and attention contract, desired action or feeling, output destination, and voice—is used when supplied; missing fields remain labeled unknown or use reversible neutral defaults for a provisional local asset. |
| Outputs | A decision of `FULL STORY`, `STORY FRAGMENT`, or `NO STORY`; rationale; chosen mechanic; one downstream owner; factual constraints; final asset; compact receipt. |
| Handoff summary | Pass the decision, objective, selected mechanic, supplied facts, uncertainty, truth constraints, destination, and one next owner. Never pass the entire transcript or preload every expert. |
| Composition rule | Shaan owns narrative-dosage judgment. Story Compass may diagnose candidate story material. Exactly one downstream production owner writes the body. How I Write conducts only long-form or high-stakes writing. At most one transfer owner may supply one tested mechanism. Verification owns factual risk. |
| Human checkpoint | Checkpoint 1 Vision is approved. Checkpoint 2 architecture must be approved before live skill edits. Checkpoint 3 reviews sample outputs, command behavior, structural proof, and remaining evidence limits before the system is called deployed. |
| Validation | Source-package verifier; prompt audit and index; prompt pointers; scoped skill validation; command-surface verification; natural-language routing probes; three cold-start behavior fixtures; live-surface and system checks; prose and export guards for human-facing artifacts. |
| Behavior-changing proof | Three detached fixtures must demonstrate a full-story selection, an evidence-first truthful fragment, and an explicit no-story refusal. Each records the weak input, diagnosis, source mechanic, transformed output, observable behavior delta, factual-integrity result, and remaining risk. |
| Result surface | Farrice sees the architecture and proof as Rendered Conversation Documents. Local Markdown files are persistence copies. The reusable runtime surface is `/shaan-story-deploy`; it returns the final asset and a small Story Deployment Receipt. |
| Context policy | Keep the user brief, router decision rules, route map, and truth invariant hot. `context_retrieval: skill-only-until-selected` keeps `genius.md` out of general preselection retrieval. Load it, one selected Shaan workflow and prompt, Story Compass, How I Write, or one transfer route only after selection. Keep transcript, frames, ledgers, unselected workflows, and unrelated experts cold. |
| Reuse hook | Use `/shaan-story-deploy` before storytelling, narrative, explanation, founder-story, pitch, content, or communication work when story fit is uncertain. Reuse the three fixtures as regression tests after future Shaan revisions. |
| Goal packet | Not required. This source does not introduce self-improvement, cleanup, maintenance-loop, or evolution behavior. Incidental repairs are bounded prerequisites for the approved expansion. |
| Agentic engineering packet | Required and completed below because this build changes a front door, context loading, handoffs, review loops, and cold-start use. |

## Runtime order

### 1. Intake and truth lock

Capture the communication objective, available facts, uncertainty, and truth risk, plus audience relationship, medium, attention contract, destination, and voice when supplied. Separate source facts, operator judgment, and constructed examples before selecting a narrative path. Missing presentation context stays unknown; if truth and scope remain clear, a neutral platform-agnostic default may produce a labeled provisional asset but never a false channel-ready claim.

### 2. Decide narrative dosage

The router returns exactly one decision:

| Decision | Choose when | Do not do |
|---|---|---|
| `FULL STORY` | Real material contains meaningful intention, obstacle, change, and enough support for narrative structure | Do not invent missing scenes, dialogue, chronology, motives, metrics, or outcomes |
| `STORY FRAGMENT` | A concrete moment, analogy, frame, or micro-example can improve comprehension or recall while evidence or direct explanation remains primary | Do not let anecdote substitute for evidence or imply stronger causality |
| `NO STORY` | The task is primarily a decision, procedure, calculation, technical specification, risk statement, or other direct communication | Do not add a protagonist arc, dramatic scene, or emotionalized risk |

### 3. Validate only when story is selected

- `FULL STORY`: run Story Compass against the supplied material. A failure triggers source gathering or a downgrade to `STORY FRAGMENT` or `NO STORY`; it never triggers invention.
- `STORY FRAGMENT`: retain the evidence or direct-explanation spine and select one Shaan move.
- `NO STORY`: route directly to the appropriate non-narrative owner; Shaan may contribute only framing, pacing, specificity, or plain-language compression.

### 4. Select one production owner

The router selects one current Shaan workflow or one external owner. Substantial or high-stakes writing may pass through How I Write, which becomes the conductor and assigns one body-voice owner. Shaan remains a bounded mechanic contributor.

### 5. Use adjacent-field transfer only for a named weakness

When the problem is a specific weak function, emit:

`named weakness -> field where the function is mission-critical -> existing transfer route -> target constraints -> one detached test -> keep/reject`

Do not create a second generic transfer workflow. Use one existing owner by function: narrative architecture, platform adaptation, observed-content remix, cross-industry persuasion mechanics, or experience and fourth-wall design.

### 6. Verify and deliver

Preserve facts and uncertainty. Do not invent dialogue, chronology, metrics, outcomes, motives, or sensory details as real. Label analogies and constructed examples. Evidence stays primary in high-stakes work. Deliver the final asset plus a receipt naming the decision, selected mechanic, owner, truth constraints, checks, and unresolved risk.

## Default handoffs

| From | To | Compact handoff | Open risk |
|---|---|---|---|
| Router | Story Compass | Candidate facts, want, obstacle, change, missing evidence | Story may not exist in supplied material |
| Router | One Shaan workflow | Decision, objective, selected mechanic, facts, truth risk, destination | Existing workflow must honor the new invariant |
| Router | How I Write | Decision brief, source facts, selected Shaan contribution, target form, truth constraints | Expert soup or multiple body voices |
| Router | Transfer owner | One named weakness, target constraints, proposed outside field, test criterion | Surface-style copying or scope expansion |
| Production owner | Verification | Final asset, source facts, uncertainty, constructed-example labels | Unsupported or stronger-than-source claim |

## Checkpoint 3 integration hardening

- The Shaan cache in `execution/skill_chunks.json` contains only current `SKILL.md` preselection chunks and zero `genius.md` chunks.
- `execution/context_retriever.py` honors the declared skill-only policy on future rebuilds.
- Seven active content callers now execute dosage-first routing before deeper Shaan context.
- `watch-and-remix` preserves `OBSERVED` versus `HYPOTHESIS` labels through analysis and synthesis instead of asserting audience emotion or behavioral causality.
- `SLASH_COMMANDS.md` and explicit workflow/Claude/Codex bridges expose the seven-workflow family and its router.

## Composition Ledger

| Slot | Expert or asset | Contribution accepted | Evidence of change | Skipped or rejected |
|---|---|---|---|---|
| Spine | Shaan Story Deployment Router | Full, fragment, or no-story judgment and route selection | New router contract and decision matrix | A second storytelling conductor |
| Diagnostic | Story Compass | Tests whether selected material contains want, tension, and change | Conditional branch after `FULL STORY` | Preloading it for every task |
| Craft | One selected Shaan workflow | Supplies one source-backed frame, feeling, pacing, voice, or narrative operation | Existing workflow and matching prompt | Loading all six workflows |
| Composition | How I Write | Conducts long-form or high-stakes writing with one body-voice owner | Conditional handoff | A second body writer |
| Risk gate | Source ledger plus existing verification | Protects facts, uncertainty, and constructed-example labels | Shared truth invariant and fixture checks | Narrative force overriding evidence |
| Transfer | One existing transfer owner | Imports one operation for one named weakness and one test | Function-specific handoff | New generic adjacent-field workflow |

**Function owner:** Shaan Story Deployment Router for narrative dosage; selected downstream route for production.

**Integration owner:** `/source-to-skill-system` during the build; the router during runtime.

**Integration rule:** decide first, load second, let one owner write, verify last.

**Expert soup check:** PASS.
**Skipped experts:** Additional storytellers and generic creative councils; they add overlap without filling a missing function.

## Agentic Engineering Packet

| Field | Decision |
|---|---|
| Objective | Add one reliable, source-grounded story-deployment front door while preserving and repairing the current Shaan system. |
| Source truth | This verified source package, the current Shaan skill and agent files, current router and command outputs, and local validation scripts. No remembered credentials or unavailable private material. |
| Context plan | Decision rules and truth constraints stay hot. Expert methodology, production workflows, prompts, transcript evidence, and transfer systems load only on demand. |
| Work chunks | 1) contract and architecture; 2) router, map, and exact prompt; 3) existing-surface repairs and prompt execution layer; 4) command bridges and attributable registry updates; 5) detached proof and verification. |
| Review loop | Maximum two repair passes. Pass when structural checks succeed and all three fixtures select the correct branch with zero invented facts. Stop and surface the gap if the same fixture fails for the same reason twice. |
| Dependency gate | Use existing repository tooling only. No package, plugin, API, or dependency install. Any unexpected external or paid requirement returns to a human checkpoint. |
| Structure pass | Inspect the manifest-scoped diff, remove duplicate logic, verify one owner per function, reject unrelated generator churn, and confirm cold context stays cold. |
| Use-now artifact | `/shaan-story-deploy`, after Checkpoint 3 verification. |
| Hardening proof | Command discoverability, prompt and skill validation, three behavior fixtures, factual-integrity audit, no-story refusal check, source-package verification, and live-surface audit. |

## Validation and stop conditions

Proof sequence after architecture approval:

1. Verify the native source package.
2. Confirm the global prompt audit preserves its zero-failure baseline.
3. Build the prompt index and apply the mandatory prompt-pointer writer; inspect and retain only Shaan-attributable changes.
4. Create explicit decision-first command bridges. Preview the menu minter only; do not accept an eager `genius.md` load or unrelated arsenal churn.
5. Check skill validity and the Shaan skill heartbeat audit.
6. Verify `/shaan-story-deploy`, `/shaan-puri`, and `/shaan-puri-storytelling` across workflow, Claude compatibility, and Codex bridge layers.
7. Probe natural-language discovery for full-story, evidence-first fragment, and no-story intents.
8. Test three detached behavior fixtures with zero invented facts.
9. Execute strict live-surface and system checks, separating pre-existing global failures from task regressions.
10. Apply prose and export guards to the long-form documents, then finalize and record the forge locally.

The repository currently lacks an active behavior-changing-extraction verifier at its documented path. This build will not patch that shared verifier. The task-local `behavior-proof.md` will implement the contract manually and the gap will remain named. A structural pass cannot be represented as market proof or an A-tier human recognition pass.

## Approval boundary

Farrice approved the Checkpoint 2 architecture on 2026-08-02, authorizing the bounded local implementation described here. Global mirrors, publication, external deployment, new dependencies, commits, pushes, and claims of market effectiveness remain parked unless separately approved.
