# System Cohesion Silver-Platter Audit: Unified Operating Tree

Created: 2026-05-11
Mission: system-cohesion-silver-platter-audit
User-facing surface: Rendered Conversation Document
Source role: Local Markdown Source for persistence

## Executive Read
The Codex Antigravity system is not failing because it lacks tools. It has the opposite shape: a strong substrate with many workflows, skills, agents, bridges, verifiers, and routing scripts. The live proof set passes. The user's friction is that route choice and activation still leak back to the operator.

The first operating verdict:

- The structural control plane is mostly healthy.
- The Silver Platter audit correctly detects this as an existing AI operating workspace, not greenfield.
- The system still under-protects the user from broad "what should I use?" and "too many tools" prompts.
- The expert library is underactivated rather than inherently bloated.
- The next repair should improve root-route detection and activation loops, not create another command.

## Root Node
`/autopilot` should remain the root node.

It owns raw context, intent lock, clarity scoring, route choice, visible trace, first action, and steering closeout. Every other major surface is a backend or support layer:

| Layer | Route | Job | When it should appear |
|---|---|---|---|
| Root front door | `/autopilot` | Choose the route and reduce decision burden | Raw thoughts, uncertainty, "what should I use?", messy context, underuse, intent verification. |
| Option backend | `/orchestrate` | Show ranked paths without executing | User explicitly wants a menu, alternatives, or path comparison. |
| Governance backend | `/mission` | Durable state, validation, handoffs, artifact contract | Multi-step, reusable, system-changing, client-facing, or validation-heavy work. |
| Proof and repair | `/system-audit` | Check routing, bridges, activation, telemetry, firing behavior | Built-but-not-firing, cluttered, broken, opaque, or not steering. |
| Data-map lens | `/silver-platter` | Map Pantry -> Prep -> Plate and find OS setup gaps | Tool-stack, business-OS, AI-workspace, data-prep, weekly-summary, or audit-existing needs. |
| Composition layer | `/expert-composition-governor` | Prevent expert soup with one owner and bounded slots | Too many experts, not interwoven, full arsenal, many plausible workflows. |
| Library reuse | `/knowledge-librarian` | Find existing solution docs and avoid duplicate builds | Missions, reusable knowledge, unclear existing capability, source-to-system work. |
| Feedback layer | `/routing-intelligence` | Record routing outcomes and misroutes | Wrong route, generic answer, route dissatisfaction, ensemble evidence. |
| Evolution layer | `/self-evolve` | Propose supervised improvements from failure evidence | Recurring failure, underperforming route, stale skill, measured improvement needed. |

## Operating Tree
```text
Codex Antigravity
`- Root: /autopilot
   |- Understand: Intent Lock, Clarity Score, Ambiguity Map
   |- Route: command_menu + workflow_router + routing_governor + expert_router + recommend_stack
   |- Choose:
   |  |- Direct Execute for tiny clear tasks
   |  |- /orchestrate when the user asks for options
   |  |- /mission when the work needs state, validation, or reuse
   |  |- /system-audit when the system feels built but not firing
   |  |- /silver-platter when the data/tool stack needs mapping
   |  `- /expert-composition-governor when many experts/workflows must become one output
   |- Prove:
   |  |- verifiers
   |  |- artifact guards
   |  |- routing intelligence
   |  `- performance log
   `- Improve:
      |- misroute feedback
      |- self-evolve proposals
      |- mission solution capture
      `- supervised router/workflow patches
```

## Pantry: What Exists
| Pantry item | Evidence | Read |
|---|---|---|
| Active authority | `CODEX.md`, workspace `AGENTS.md`, global `~/.codex/AGENTS.md` read-only | Current authority is Codex-native; legacy Claude/Gemini files are compatibility references. |
| Command/workflow substrate | harness check: 805 Claude commands, 820 Codex command skills, 1,038 workflows, 137 execution scripts | The library is large but command skill coverage passes. |
| Root skills | harness check: 250 root skills | The library is broad and should stay cold behind routers. |
| Expert agents | harness check: 169 expert agents; Silver Platter audit saw 170 Codex agents | Inventory is large; count discrepancy is minor and should be reconciled later. |
| Knowledge base | knowledge compiler stats: 726 files, 2,975,081 words, estimated 3,956,857 tokens | Retrieval and reuse matter more than loading everything. |
| Mission artifacts | `docs/mission-artifacts/` | Mission OS already supports durable continuity. |
| Solution docs | `docs/solutions/` | Reusable patterns exist and surfaced correctly for this mission. |
| Telemetry | routing intelligence, performance log, protocol tracker, system health | Activation evidence exists, but some loops are blocked or dormant. |

## Prep: Summaries The System Should Maintain
| Prep summary | Current source | Status | Needed behavior |
|---|---|---|---|
| Control-plane health | `/system-audit`, `verify_system_control_plane.py` | Active and passing | Keep as proof spine after control-plane changes. |
| Route confidence | command menu, workflow router, routing governor | Partially active | Must better classify route-choice-burden prompts. |
| Mission continuity | Mission OS artifact contract | Active | Use for system-changing work instead of chat-only plans. |
| Library reuse | Knowledge Librarian solution search | Active | Keep required before new system builds. |
| Expert composition | Expert Composition Standard | Structurally valid | Needs more live activation evidence and ensemble logging. |
| Evolution readiness | performance log, skill evolution, cross-pollination | Blocked | Need 3 more performance entries to unlock Skill Evolution. |
| Protocol activation | protocol tracker | Weak | 33 protocols never activated; 38 overdue/zombie signals. |
| Routing outcomes | routing intelligence scoreboard | Active | Now includes two newly logged cohesion audit misroutes. |

## Plate: What The User Should See
| User moment | Plate output | Quality bar |
|---|---|---|
| "I do not know what to use" | Autopilot Trace with chosen route, skipped routes, verification, and first action | One chosen path, not a generic command list. |
| "Show me my options" | `/orchestrate` Execution Menu | Three paths, clear recommendation, no execution. |
| "This is big/system-changing" | Mission Charter plus validation contract | State path, Library Decision, workstreams, validators. |
| "The system feels broken or isolated" | `/system-audit` issue ledger | Trigger, route, activation path, telemetry/proof, verifier. |
| "Map the whole operating setup" | Silver Platter Pantry -> Prep -> Plate map | Existing setup acknowledged, gaps prioritized. |
| "Too many agents/workflows" | Composition Plan and Composition Ledger | One owner, bounded slots, skipped-expert reasons. |
| "That routed wrong" | Routing Intelligence misroute record | Wrong route, correct route, reason, future verifier. |
| "Make it better next time" | Self-evolve proposal | Evidence-backed patch plan, supervised approval. |

## Activation Status
| Surface | Status | Evidence |
|---|---|---|
| Control-plane verifier | Active | `verify_system_control_plane.py` passed. |
| Autopilot routing verifier | Active | `verify_autopilot_routing.py` passed. |
| Skill-system contract | Active | `verify_skill_system_contract.py` passed. |
| Expert composition standard | Active structurally | `verify_expert_composition_standard.py` passed. |
| Harness health | Active | `codex_harness_check.py` passed. |
| Silver Platter skill | Active structurally | example validation and both skill validations passed. |
| Performance Log | Active | 17 entries, growing. |
| Skill Evolution | Blocked | 17/20 entries; needs 3 more. |
| Cross-Pollination | Blocked | Waiting on Skill Evolution data. |
| Gap Detection | Ready | System health reports ready. |
| Protocol activation | Weak | 25 percent activation rate; 33 never activated, 38 overdue/zombie. |
| Routing Intelligence | Active but sparse | 23 total routings, 12 feedback, 0 percent ensemble rate. |
| Expert utilization | Underactivated | 167 agents with zero deployments. |
| Notion sync | Network unavailable | Local-first evidence is available; remote sync not confirmed. |

## Routing Scenario Results
| Scenario | Expected | Actual | Status |
|---|---|---|---|
| "silver platter audit my system" | `/silver-platter` first | `/silver-platter` first | PASS |
| "not interwoven too many agents" | `/expert-composition-governor` first | `/expert-composition-governor` first | PASS |
| "I have too many tools and don't know what to use" | `/autopilot` plus `/system-audit` logic | `/compile-knowledge` first | FAIL, logged as misroute |
| "what should I use next?" | `/autopilot` chosen route | `/ash-risk-map` first | FAIL, logged as misroute |

## Issue Ledger
| Severity | Symptom | Cause | Affected surface | Fix | Verifier | Boundary |
|---|---|---|---|---|---|---|
| P1 | Broad route-choice-burden prompts do not reliably hit the front door | Router and governor do not recognize some natural phrases as operator-steering intent | command menu, workflow router, routing governor | Add detectors and metadata boosts for "too many tools", "don't know what to use", and "what should I use next" so `/autopilot` wins and `/system-audit` supports when the symptom is system-level | Add golden queries, rerun `verify_system_control_plane.py` and `verify_autopilot_routing.py` | workspace-only |
| P1 | The system still risks making the user choose the route | Some surfaces return a menu-like ranked list even when the user wants the system to choose | `/autopilot`, command menu, workflow router | Keep `/orchestrate` as explicit menu-only backend; make general steering prompts go through `/autopilot` | Scenario tests for "what should I use next?" and "I have too many tools..." | workspace-only |
| P2 | Expert library is broad but underactivated | 167 agents have zero deployments and ensemble rate is 0 percent | expert router, recommend stack, routing intelligence | Trigger `/expert-composition-governor` when many experts/workflows are plausible and log accepted/rejected slots | `verify_expert_composition_standard.py`, routing intelligence ensemble rate | workspace-only |
| P2 | Protocols are mostly inactive or overdue | Protocol activation is not wired strongly into everyday closeouts and audits | protocol tracker, session closeout, self-evolve | Create a hot/cold protocol activation policy and let `/system-audit` flag dormant essentials before cleanup | `protocol_tracker.py audit`, `verify_system_control_plane.py` | workspace-only |
| P2 | Skill Evolution and Cross-Pollination are blocked | Performance Log has 17 entries and needs 20 for the next phase | performance log, skill evolution, cross-pollination | Log 3 more meaningful performance entries, then run the next evolution phase | `system_health.py --quick`, skill-evolution verifier when available | workspace-only |
| P2 | Notion sync is unavailable from this sandbox | DNS/network unavailable | Notion sync and remote performance logging | Keep local-first evidence as the source of truth and sync later in a network-enabled context | `system_health.py --quick`, dry-run sync | external approval/network |
| P3 | Inventory counts differ slightly across tools | Silver Platter audit reports 828 command skills while harness check reports 820 Codex command skills | inventory scripts | Reconcile count definitions before using counts as hard proof | `codex_harness_check.py`, audit script | workspace-only |
| P3 | No harness-specific Silver Platter cadence exists yet | The skill can audit, but no recurring cohesion platter exists for the workspace | mission artifacts, future silver_platters | After router fixes, consider a recurring weekly system-cohesion platter | artifact guard and health check | workspace-only |

## Owner Layer
| Slot | Owner / Asset | Contribution accepted | Evidence of change | Skipped / rejected |
|---|---|---|---|---|
| Spine | Mission OS plus `/system-audit` | Use Mission artifact contract and issue-ledger proof spine | Mission state and artifact chain created | New standalone OS rejected |
| Differentiator | `/silver-platter` | Reframe system as Pantry -> Prep -> Plate so gaps are operational, not abstract | `audit-existing` detection and map sections | Greenfield business-OS setup rejected |
| Mechanism | Routing Governor and Routing Intelligence | Failed natural prompts become misroute feedback | Two new misroutes logged | Generic dissatisfaction rejected as sufficient evidence |
| Craft | `/autopilot` and `/orchestrate` boundary | Root chooses; menu compares only when asked | Root node and Plate outputs specify this | Long command catalog as user surface rejected |
| Risk Gate | Expert Composition Standard | One owner, bounded slots, skipped-route logic | Composition table and issue ledger | Expert count as quality rejected |

Owner: Mission/System Audit.
Integration rule: system-changing work is governed by `/mission`, proven by `/system-audit`, mapped by `/silver-platter`, and routed through `/autopilot`.
Expert soup check: PASS for this first pass.

## 30-Day Build Order
| Window | Move | Output | Quality bar |
|---|---|---|---|
| Days 1-3 | Patch route-choice-burden phrases | Router/governor update plus regression queries | `/autopilot` wins for "too many tools", "don't know what to use", and "what should I use next". |
| Days 4-7 | Add a visible route-choice smoke test to `/system-audit` | Expanded control-plane verifier | The audit fails if user-steering prompts route to generic commands. |
| Days 8-12 | Activate composition by default when many routes compete | Composition trigger and ledger requirement in relevant workflows | "Too many agents/not interwoven" produces one owner and bounded slots. |
| Days 13-16 | Finish the Skill Evolution unlock | 3 more performance entries and evolution readiness check | System health moves Skill Evolution from blocked to actionable. |
| Days 17-21 | Create a weekly system-cohesion platter | Local summary artifact for routes, misroutes, dormant protocols, and next fixes | The operator sees one weekly control-plane read instead of scattered dashboards. |
| Days 22-26 | Harden activation telemetry | Protocol hot/cold policy and dormant-essential warnings | Important protocols are active, intentionally cold, or explicitly retired. |
| Days 27-30 | Fresh-session and global-alignment review | Workspace proof pack plus optional global mirror recommendation | No global edits without approval; fresh session can find the root behavior. |

## Verifier Matrix
| Check | Result |
|---|---|
| `python3 execution/verify_system_control_plane.py` | PASS |
| `python3 execution/verify_autopilot_routing.py` | PASS |
| `python3 execution/verify_skill_system_contract.py` | PASS |
| `python3 execution/verify_expert_composition_standard.py` | PASS |
| `python3 execution/codex_harness_check.py` | PASS |
| `python3 skills/mark-kashef-silver-platter-agentic-os/scripts/validate_examples.py` | PASS |
| `python3 execution/validate_skill.py mark-kashef-silver-platter-agentic-os` | PASS |
| `python3 execution/validate_skill.py source-command-silver-platter` | PASS |

## Next Implementation Target
The highest-leverage next implementation is the P1 routing repair for route-choice-burden prompts. It is small, workspace-only, testable, and directly addresses the user's core friction.
