# CODEX.md - Codex Antigravity Active Harness

This is the active Codex-native operating specification for `/Users/farricecain/Google Antigravity`.

`AGENTS.md` is the Codex entry-point constitution and delegates expanded harness detail to this file; CODEX.md is subordinate to AGENTS.md, not a competing authority. `GEMINI.md` and `CLAUDE.md` are peer constitutions for their own platforms (`docs/OPERATING-CODEX-AND-CLAUDE.md`), and `.claude/commands/` is a source compatibility reference — read them on demand, not as legacy files, unless a task explicitly asks to inspect or back-port model-specific behavior.

## Authority Order

1. System, developer, tool, and user instructions.
2. `AGENTS.md` plus this file for workspace behavior.
3. `.agent/workflows/` plus the hot `.agents/skills/source-command-*` control-plane wrappers for active Codex routing.
4. `execution/` scripts for deterministic work and verification.
5. `GEMINI.md` and `CLAUDE.md` as peer-platform constitutions (read on demand, not primary Codex routing authority); `.claude/commands/` as source compatibility reference.

Do not treat `GEMINI.md` or `CLAUDE.md` as primary routing authority in Codex. Use them only when a workflow needs historical detail that is not yet represented in Codex-native files.

## Codex Control Plane

- Front doors (2026-07-06): `/go "<messy thought>"` is the anti-bottleneck
  staging path: silent DICE compile, written assumptions, max one question
  round, run packet, then route to the right conductor. `/create` is the
  universal content conductor: outcome contract with at least two engineered
  outcomes, context richness, live zeitgeist with receipts, purpose routing,
  proven recipe, and gates. For multi-step or quality-critical orchestration,
  load `directives/peak-operation.md` before decomposing the work.
- `/autopilot` is the intent-to-outcome front door for raw context, co-creative launchpad packets, intent lock, routing, visible trace, safe workspace-local execution, verification, run receipts, and risk-gated judgment.
- `/system-audit` is the control-plane audit route for "built but not firing," competing defaults, broken routing, bridge drift, activation telemetry, and Autopilot behavior repair.
- Operator Cockpit V2 is the pre-action cockpit for non-trivial work. Use `python3 execution/operator_cockpit.py --intent "<raw request>" --plain` to render the Intent Confidence Packet, current cockpit status, local friction capture, retrieval home, proof plan, and global mirror checkpoint before meaningful mutation.
- `/repeatability-spine` is the repeatability route for "cannot repeat the magic," failed revisions, wrong routes, and regressions that need a preservation lock plus regression guard.
- `/end-session` is the closeout intelligence route; it must capture performance evidence, routing decisions, route feedback or feedback inbox items, health snapshots, and a safe conversation-index status without requiring manual logging commands.
- `/orchestrate` is the menu backend when the user wants ranked options instead of a chosen route.
- `/mission` is the governance backend for persistent, multi-milestone, validation-heavy, reusable, or system-changing work.
- `/expert-composition-governor` is the composition backend for "expert soup," many plausible skills, full-arsenal deployment, or work where several experts must become one coherent output.
- `/extraction-governor-agent` owns source-to-capability decisions before a source becomes a skill, reference, workflow, agent, or system.
- `/convene` is the collective-genius/general-purpose council owner for creative, strategic, and judgment-heavy work that needs divergent expert takes, inner-council deliberation, synthesis, grounding, and a learning digest. It is deployable through `.agent/workflows/convene.md` and `execution/convene.py`, but it must not compete with `/virtuoso` as a super-router or `/deep-research-os` as the research owner.
- `/kimi-swarm` is a thin Kimi-style packet compiler for research and general-purpose swarm runs. Research mode routes through `/deep-research-os`; general mode routes through `/convene`; real Codex subagents remain approval-gated per run.
- `/self-evolve` and `/skill-anneal` improve existing workflows or skills from failure evidence instead of adding bloat.
- Self-improvement and maintenance runs use `semantic_libraries/antigravity/primitives/goal-loop-maintenance-contract.md`: target, criteria, permitted side effect, proof artifact, measurable stop, turn cap, evaluator, wake-up check, human checkpoint, and rollback/archive rule must be explicit before mutation.
- Agentic engineering runs use `semantic_libraries/antigravity/primitives/agentic-engineering-loop-contract.md`: human-owned objective, thin context, exact source truth, small reviewable chunks, review-until-stop proof, dependency safety, structure cleanup, and use-now artifacts must be explicit when the task changes agent harness behavior, package/tool adoption, review loops, or source-to-system practice.
- Intent-to-outcome runs use `semantic_libraries/antigravity/primitives/co-creative-launchpad-contract.md`, `execution/co_creative_launchpad.py`, `execution/autopilot_runtime_preflight.py`, `execution/outcome_recipes.py`, `execution/capability_graph.py`, `execution/friction_ledger.py`, and `execution/run_receipt.py`: predicted need, center, edges, execution-changing questions, one best route, support gates, execution decision, safe-local policy, verifier plan, friction capture, and run receipt must be visible for meaningful Autopilot work.
- Operating-alignment runs use `semantic_libraries/antigravity/primitives/operating-alignment-contract.md`: raw intent -> Launchpad -> meta-intent classification -> one owner -> bounded expert composition -> proof -> feedback capture -> one next action. System-level orchestration, global/workspace alignment, automations, subagent, full-arsenal, or output-consistency requests are `/system-audit` owned unless a narrower route has explicit evidence.
- V2 cockpit starts use an Intent Confidence Packet for non-trivial work: goal, audience, success criteria, non-trivial reason, confidence, unresolved questions, chosen route, support gates, arsenal policy, proof plan, retrieval home, and pause/run decision. If the packet has unanswered execution-changing questions, Codex may do read-only discovery but must pause before meaningful mutation or delivery.
- Magic-preservation checks use `semantic_libraries/antigravity/primitives/magic-preservation-regression-set.md` for Josh, Coach Cooz, and source extraction wins. Strong prior work is regression evidence, not nostalgia; preserve the success criteria before broadening the system.
- Read-only status runs use `execution/harness_status.py` for the compact trust surface, `execution/operator_core_fast_proof.py` for daily fast proof, and `execution/savant_control_room.py` for the higher-level cockpit: current intent, cohesion state, mission status, latest receipt, friction ledger, end-session health, routing probes, protocol counts, stale anchors, capability graph summary, packaging readiness, and the next move must be visible without writing files.
- Operator Cockpit V2 extends the status cockpit into a pre-action cockpit. It may capture local friction entries automatically for operator struggle, retrieval failure, stale proof, misroutes, or unanswered confidence-packet questions. This capture is local-only and does not authorize global writes, external writes, broad cleanup, publishing, Mission mutation, or real Codex subagents.
- Closeout steering uses `execution/contextual_next_prompts.py` and the `/steering-compass` contract to produce a visible recommended task title plus 3 Next Prompts: Use Now, Harden, and Expand. Each prompt must explain when to use it, why it is recommended, the copy-paste prompt, expected output, quality bar, skip condition, and suggested skills/workflows. Deep closeouts fail the visible-surface contract when the task title or any prompt's expected outcome is absent.
- Focused transfer handoffs use `/handoff`; whole-session closeouts use `/end-session`. `/handoff` may create a disposable OS-temp handoff for another session, branch, tool, or agent, while `/end-session` captures session intelligence and continuity evidence.

## Artifact Comprehension Pilot (SHADOW v0.2)

This branch evaluates one narrow workspace-only behavior. Its source is
`execution/fixtures/burnout_safe_output/artifact-comprehension-contract-v0.2.md`.

- Ordinary replies and closeouts defer entirely to the existing global Clear
  Depth and Three Contextual Next Prompts contracts. This pilot does not render,
  rank, expand, or replace them.
- Activate only for substantial written documents or artifacts whose
  information shape can be made materially easier to understand, remember, or
  act on.
- Select the smallest representation that earns its place: scan-friendly
  prose, a table, evidence rows, a timeline, a flow, a playbook, or an existing
  Briefing Room section. Plain prose is valid when a visual would flatten
  nuance or repeat the same information.
- Prefer a flow when dependencies, feedback loops, approval gates, or state
  changes are what keep the work on track. Do not add one to a simple list or
  ordinary reply.
- Choose one primary delivery surface before drafting a substantial artifact:
  normal conversation for answers, a native writing block for finished
  reusable prose, a native artifact for durable knowledge work, a spreadsheet
  for real quantitative data, slides for presentation-shaped delivery, the
  Briefing Room for live or interactive state, and image generation for
  genuinely visual concepts. Add a second surface only when it performs a
  different job; do not duplicate the same content across formats.
- Preserve source detail, caveats, proof state, and authority. A compact surface
  may reveal depth progressively but may not delete it.
- Reuse native artifacts, Markdown, and the existing Briefing Room renderer.
  Do not create a new renderer, dashboard, task, hook, skill, or global rule.
- Treat this as `PILOT / SHADOW`. Promotion, merge, global activation, hook
  changes, and production-renderer changes require separate approval.
- Human behavior gate passed on 2026-09-01. The tested artifact rule remains
  SHADOW and workspace-local until a separate promotion decision.

## Deterministic Hook Layer (verified live-fire 2026-07-13, Codex CLI 0.144.3)

`.codex/hooks.json` → `.codex/tools/codex_hook_runner.py` fires PHYSICALLY in this workspace — these gates are real on Codex, not advisory:

| Event (verified firing) | Handlers | Behavior |
|---|---|---|
| SessionStart | plugin hooks (JCC orchestrator, watch setup) | context injection |
| UserPromptSubmit | skill-router, session-ledger prompt | routing warnings + skill suggestions injected |
| PreToolUse (shell → `Bash` matcher) | cost-gate, dangerous-git, active-tool-lock | HARD BLOCK on gated spend / dangerous git; concurrent-tool warn |
| PostToolUse (shell) | session-ledger posttool | debt tracking |
| Stop | session-ledger stop | finalize-debt check |

Facts that keep this table honest:
- Codex maps its shell tool onto the `Bash` matcher — every shell command passes the same gates as Claude Code. Work WITH a firing gate, never around it.
- **Native (non-shell) file reads fire NO tool hooks.** The Claude-side execution-prompt menu injection does not exist here — on skill load, read the SKILL.md "Execution Prompts" section and honor the matching v2 prompt contract yourself.
- Hook output contract is stricter than Claude Code: `hookSpecificOutput` REQUIRES `hookEventName` or Codex marks the hook Failed (root-caused 2026-07-13, JCC SessionStart).
- Editing `.codex/hooks.json` invalidates per-hook trust hashes in `~/.codex/config.toml` — after any edit, hooks silently stop until re-trusted in Codex Desktop. Prefer changing the TARGET scripts (hook_runner targets) over the hooks.json wiring.
- Keep the CLI current (`npm install -g @openai/codex@latest`): 0.133.0 hard-failed against gpt-5.6-sol; 0.144.3 verified working. Subagents + per-thread runtime routing available since 0.116.0/0.137.0 — real Codex subagents remain approval-gated per run.

## Skill Systems

Use skill systems for end-to-end work that should run as a connected process, not as one isolated skill call and not as a giant mega-skill.

Each skill system must define:

- component skills, workflows, scripts, agents, and references
- step order and dependency rules
- inputs each component requires
- outputs each component produces
- handoff summaries between steps
- expert composition rules when many components are active
- human checkpoints and approval gates
- validation checks at each boundary
- user-facing result surface
- context policy for what is loaded, summarized, or kept cold

The full contract lives at `semantic_libraries/antigravity/primitives/skill-system-contract.md`.

## Agent Arsenal Routing

Agents must route like one coordinated arsenal, not isolated fixed menus. Use
`semantic_libraries/antigravity/primitives/agent-arsenal-routing-contract.md`
for agent/operator routing, seed-workflow policy, expert stacking, visible route
traces, and subagent approval boundaries.

Fixed workflow lists inside agent files are seed candidates only. Operator agents
must route through the local command, workflow, expert, compound, context, and
tool routers before committing to a path. Expert/persona agents remain expertise
contexts; they should include routing interop and hand off to function-owner
operators when another part of the arsenal is a better fit.

Cross-patterning and stacking are first-class behavior. Preserve declared
pairings from `execution/expert_router.py`, skill stacking guides, routing
intelligence ensemble feedback, and cascade relationships. Use the generated
registry at `semantic_libraries/antigravity/stacking/agent-stacking-registry.json`
as the compact lookup surface.

When a task risks expert soup, use
`semantic_libraries/antigravity/primitives/expert-composition-contract.md`.
Expert count is not quality. Multi-expert work needs one owner, contribution
slots, skipped-expert reasons, and a Composition Ledger when stakes are high.

## Virtuoso Orchestration

Complex work should show the blend, not merely name the winning command. Use
`execution/virtuoso_orchestration.py` when the request asks for full-system
orchestration, subagents, cross-pollination, expert composition, agent
elevation, plugin/tool blending, or unusually high creative/operator quality.

The Virtuoso layer is a composer over the existing routers. It must not become a
competing super-router. It reads Autopilot preflight, recommended stack,
subagent readiness, routing intelligence, and plugin readiness, then returns a
single **Virtuoso Trace** with:

- primary route and function owner
- support gates and tool/plugin surface
- recommended stack or skip reason
- bounded composition slots
- subagent packet candidates with main-thread integration
- dynamic workflow manifest trace when `--workflow` is used
- optional ensemble routing log
- verifier plan and first action

Run it from the project root:

```bash
python3 execution/virtuoso_orchestration.py "[goal]"
python3 execution/virtuoso_orchestration.py "[goal]" --json
python3 execution/virtuoso_orchestration.py "[goal]" --delegate --log
python3 execution/virtuoso_orchestration.py "[goal]" --trace-only
python3 execution/virtuoso_orchestration.py "[goal]" --workflow
python3 execution/virtuoso_orchestration.py "[goal]" --mode revenue
```

Command surface: `/virtuoso [goal]` is the single hot deploy-at-will front door.
It renders the trace, labels considered versus executed surfaces, prepares
delegation packets when useful, and runs the first safe workspace-local action
by default.

Real Codex subagents still require explicit authorization. `--delegate-intent`
only prepares subagent-first packets and delegation receipts; it does not spawn
workers. `--log-routing` writes a real routing-intelligence entry and should be
used only when the route was actually chosen for the current work.

## Codex Dynamic Workflows

Large, multi-phase, cross-checked, or resumable work can use the manifest-held
runtime at `execution/codex_dynamic_workflow.py`. This is a companion runtime
behind `/virtuoso --workflow`, not a competing hot command.

The runtime stores objective, recipe, phases, worker packets, inputs, outputs,
approval gates, resume state, verification rules, and receipts under
`.agent/dynamic-workflows/`. It may prepare worker packets, but it never spawns
real Codex subagents. Real subagents still require explicit user authorization,
the Codex subagent tool surface, and a Delegation Receipt.

Use it for codebase audits, migration planning, cross-checked research,
adversarial plan review, and source-to-system extraction when ordinary
single-thread execution would lose intermediate state or proof.

The runtime is portable beyond this workspace. A global install may place the
script at `~/.codex/tools/codex_dynamic_workflow.py` and a generic skill at
`~/.codex/skills/codex-dynamic-workflow/SKILL.md`; outside Antigravity, run the
script directly from the target workspace so state stays local to that
workspace.

## Kimi Swarm And Convene

Kimi-style swarms are implemented as Codex-native packet plans and receipts, not
as a hidden always-on agent runtime.

Use:

```bash
python3 execution/kimi_swarm.py plan "[objective]" --mode research --depth standard --allow-subagents --json
python3 execution/kimi_swarm.py plan "[objective]" --mode general --convene-mode wide --json
python3 execution/convene.py plan "[task]" --mode tight --json
```

The contract is:

- `/virtuoso` composes the route and support gates.
- `/deep-research-os` owns sourced research swarms.
- `/convene` owns general-purpose council deliberation.
- `/kimi-swarm` only compiles the context pack, worker packets, source rules, phase sequence, and verification plan.
- real Codex subagents are never spawned by these scripts; approval and a Delegation Receipt are required per run.
- source-grounded findings must pass through `execution/research.py` / `execution/research_contract.py`, and factual strategic output should be checked with `execution/grounding_guard.py`.

## Hot And Cold Skill Surface

Keep front doors and high-use control routes hot:

- `/autopilot`
- Operator Cockpit V2 command-backed surface: `python3 execution/operator_cockpit.py --intent "<raw request>" --plain`
- `/ai-employee-os`
- `/system-audit`
- `/end-session`
- `/repeatability-spine`
- `/mission`
- `/orchestrate`
- `/extraction-governor-agent`
- `/expert-composition-governor`
- `/source-to-skill-system`
- `/knowledge-librarian`
- `/virtuoso`
- `/self-evolve`
- `/skill-anneal`
- `/routing-intelligence`
- `/health-check`
- `/artifact-router`
- `/buyer-trigger-os`
- Extraction core: `/extract`, `/extract-forge`, `/extract-vision`, `/extract-amplify`, `/video-source-extract`, `/video-transcript-ledger`
- `/sam-parr-copywriting-mechanics`
- `/session-calibrate`
- `/project-coordinate`
- `/project-onboard`
- `/align`
- `/devil`
- `/burst`
- `/tweak`

Hot and cold are routing and context-loading states, not filesystem placement. Keep the broad migrated command library logically cold behind `execution/command_menu.py`, `execution/workflow_router.py`, and targeted skill loads. The extraction core is intentionally hot because source work is a daily operator surface and must be deployable without remembering wrapper paths. A command wrapper existing in the single canonical live wrapper tree does not mean Codex should preload or advertise it as the first route.

`/buyer-trigger-os` is intentionally hot as a thin launcher for `skills/meg-heckman-buyer-trigger-os/`. It must enforce source-trace default and research-trace default, and must not become a duplicate, cheaper implementation of the Meg OS. Current buyer insights, trend-backed concepts, purchase intent research, and social-listening claims must route through `execution/buyer_trigger_research.py` or an equivalent source-led research package before recommendation. The default lane is public/free; paid/quota tools remain approval-gated.

The daily operator command kit (`/session-calibrate`, `/project-coordinate`, `/project-onboard`, `/align`, `/devil`, `/burst`, `/tweak`) is intentionally hot because these commands are small steering utilities used to make ordinary sessions more aligned, coordinated, critique-ready, variant-rich, and easier to improve. Keep their shared policy in `semantic_libraries/antigravity/primitives/daily-operator-command-kit.md`.

`/convene`, `/kimi-swarm`, `/council`, `/roundtable`, `/strike`,
`/deploy-council`, `/jcc-deploy`, and `/campaign` are deployable, on-demand workflow
surfaces by default. Their wrappers remain in the canonical single tree, but the routes stay logically cold. Do not hot-promote them
unless later proof shows frequent direct use, clean routing behavior, and no
expert-soup or super-router drift.

`/ai-employee-os` is intentionally hot because it is the command-grade route
for AI employee/company-agent design, memory isolation, shared integration
scope, proactivity gates, rollout safety, and model/personality regression
checks.

`/sam-parr-copywriting-mechanics` is intentionally hot only as an
operator-approved direct-response mechanics front door. It is bounded to
headline gravity, proof-first rescue, curiosity gaps, rhythm, story desire,
objections, humor fit, and copywork. It does not replace `/copywriting-agent`,
`/high-taste-writing-os`, or `/publishable-copy-gate`, and it must preserve a
behavior-changing before/after proof standard. Its wrapper remains physically
live for recoverable deployability while the route is intentionally hot for
direct-response work.

The advertised and preloaded Codex skill surface is intentionally small. The
workspace keeps one single canonical live wrapper tree under `.agents/skills/`
so every source command remains explicitly discoverable. Only hot control-plane
front doors should be advertised or loaded by default; other wrappers are
logically cold and load only after router, menu, or direct invocation. Do not
reintroduce a second quarantine tree. The executable arsenal remains
`.agent/workflows/`.

Run the live-surface audit after bridge or skill-surface changes:

```bash
python3 execution/codex_live_surface_audit.py --strict
```

## Bridge Rules

Claude slash commands are represented for compatibility as `.claude/commands/<command>.md`.

Codex-active command execution uses:

- `.agent/workflows/<command>.md`
- `.agents/skills/source-command-<command>/SKILL.md` wrappers, with hotness controlled by routing policy

When a workflow should be command-invokable, `.agent/workflows/` remains the
executable source of truth. A non-hot `source-command-*` wrapper remains in the
single live tree for explicit discovery but must not be preloaded or promoted as
a default route. Load it through `execution/command_menu.py`,
`execution/workflow_router.py`, direct invocation, or the workflow file.

## Subagent Boundary

Legacy Claude subagent files are role/process specifications in Codex. Do not spawn real Codex subagents unless the user explicitly asks for subagents, parallel agents, or delegated agent work.

Before claiming real parallel delegation, run `python3 execution/subagent_readiness.py --dry-run --json` and keep the main Codex thread as the integration owner. The delegation receipt must name the worker, reason used, exact slice, context read, accepted/rejected output, risk notes, and integration owner.

## Written Deliverable Surface Contract

For substantial written knowledge work, the user-facing surface is a Rendered Conversation Document: the readable document shown directly in chat with clean headings, sections, spacing, and tables when useful.

Use exact surface terms:

- Rendered Conversation Document: full readable content shown in conversation.
- Local Markdown Source: saved `.md` persistence copy. It is not the primary review surface.
- External Export: `.docx`, HTML, Canva, Google Docs, Notion, PDF, or similar formats. Create only when explicitly requested.

Local saved files are persistence copies. They can support reuse, guard checks, and later rendering, but they are not the main review surface. Sidecar metadata for written deliverables must include `userFacingSurface: "rendered-conversation-document"`, `sourceRole: "persistence-copy"`, and `externalExportRequested: false` unless an export was explicitly requested.

Readable Markdown rule: human-facing `.md` files must open as documents, not
metadata records. The first meaningful line should normally be `# Title`.
Do not put visible YAML frontmatter, JSON metadata, `IsArtifact`,
`artifact_type`, `title:`, `status:`, `tags:`, or similar metadata headers at
the top of written deliverables. Use sidecar metadata instead. YAML
frontmatter remains allowed only for system surfaces that require it, such as
workflow files, command bridges, skills, agents, parseable design specs, and
explicitly machine-readable templates.

## Global Artifact Organization

Use `/artifact-router` and `execution/artifact_router.py` as the Codex-wide placement layer for files, documents, artifacts, deliverables, and project folders across this workspace plus `/Users/farricecain/Documents/Codex`.

The physical hierarchy is project-first under `_active/<project-slug>/`, using `INDEX.md`, `00-start-here/`, `01-source/`, `02-research/`, `03-working-drafts/`, `04-deliverables/`, `05-assets/`, `06-system/`, `90-exports/`, and `99-archive/`. Retrieval metadata stays domain-first: `System`, `Creative`, `Extraction`, `Revenue`, `Client`, `Research`, `Content`, `Ops`, and `Personal`.

Before finalizing substantial artifact-producing work, classify or enforce the output path:

```bash
python3 execution/artifact_router.py classify [artifact path]
python3 execution/artifact_router.py enforce [artifact path]
python3 execution/artifact_frontmatter_guard.py [artifact path]
```

For backlog cleanup, generate a staged plan and apply only the safe bucket:

```bash
python3 execution/artifact_router.py plan
python3 execution/artifact_router.py apply --plan [plan path]
```

Do not modify `/Users/farricecain/Google Antigravity` from this organization layer.

## Verification Standard

After system, router, workflow, skill, or bridge changes, run the smallest relevant proof set:

```bash
python3 execution/verify_artifact_router.py
python3 execution/verify_codex_authority.py
python3 execution/verify_agentic_engineering_loop_contract.py
python3 execution/verify_skill_system_contract.py
python3 execution/verify_goal_loop_maintenance_contract.py
python3 execution/verify_mission_activation_contract.py
python3 execution/verify_expert_composition_standard.py
python3 execution/verify_repeatability_spine.py
python3 execution/verify_autopilot_runtime_preflight.py
python3 execution/verify_codex_dynamic_workflow.py
python3 execution/verify_system_control_plane.py
python3 execution/verify_end_session_intelligence.py
python3 execution/verify_autopilot_routing.py
python3 execution/verify_skill_evolution_candidate_freshness.py
python3 execution/codex_live_surface_audit.py --strict
python3 execution/capability_graph.py --json
python3 execution/friction_ledger.py verify
python3 execution/run_receipt.py --verify
python3 execution/harness_status.py --json
python3 execution/verify_operator_core_ai_employee_os.py
python3 execution/verify_operator_core_fast_proof.py
python3 execution/verify_savant_control_room.py
python3 execution/subagent_readiness.py --dry-run --json
python3 execution/verify_subagent_readiness.py
python3 execution/verify_plugin_readiness_stdout.py
python3 execution/artifact_frontmatter_guard.py [artifact path]
python3 execution/artifact_surface_guard.py [artifact path]
python3 execution/codex_harness_check.py
```

If source-to-capability artifacts changed, also run:

```bash
python3 execution/sync_registries.py
python3 execution/validate_skill.py source-command-source-to-skill-system
```

## Verify Tag

CODEX-HARNESS-ACTIVE-2026-05-09
