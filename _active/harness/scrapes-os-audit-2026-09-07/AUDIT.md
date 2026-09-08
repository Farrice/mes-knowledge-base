# Scrapes vs Antigravity: the operating system decision

Follow-up: [verified repair and remaining deployment/source limits](REPAIR-RESULT.md). The findings below preserve the original baseline.

September 7, 2026 · Prepared for Farrice · Astra reliability audit

## Verdict

**Keep your knowledge and production capabilities. Repair and simplify the operating layer around them. Do not replace Antigravity with Scrapes, or stack both complete operating systems, on the present evidence.**

Your current system is capable, but it is not fully reliable or fully verified in Codex. We reproduced failures in worktree memory retrieval, Codex event accounting, and pipeline readiness. Those defects explain some operating friction. They do not establish the cause of every rejected output, and repairing them would not by itself establish better creative work.

Scrapes has a more coherent documented design for client workspaces, memory ownership, and customization. Its purchased production skills already add useful machinery to your system. Its complete OS has not demonstrated better Astra execution here.

**Scope limit:** this is a completed audit of the accessible architecture, current Antigravity wiring, official Scrapes documentation, and the locally cached Scrapes installer v1.3.0. The private Agentic OS repository returned 404 through the connected GitHub account; the machine's Git login could not authenticate. The actual OS implementation and its live runtime remain **UNTESTED**. A complete vendor source/runtime audit requires that access. The recommendation is consequently provisional, not a fabricated head-to-head win.

## Which system is better, and at what?

The comparison separates what exists, what documentation promises, and what has actually been exercised. Feature counts are not a quality score.

| Dimension | Antigravity today | Scrapes Agentic OS | Judgment for your work |
|---|---|---|---|
| Your accumulated expertise | Local domain skills, source material, approved examples, voice and client decisions. Their presence and established use are verified; repeatability varies. | General methods plus user/client context. No access to the complete purchased library for comparison. | Preserve yours. Migration should never discard this asset. |
| Operating structure | Multiple instruction surfaces, routers, hooks and overlapping contracts; concrete contradictions observed. | Documented shared instruction owner, client scopes and base/local customization. Actual startup file size unknown. | Borrow the clearer ownership pattern; do not equate documented simplicity with tested reliability. |
| Astra compatibility | Native Codex work and tools function; some adapters still assume Claude-shaped events and model roles. | Shared AGENTS instructions support Codex. Several UI, permission and consolidation paths explicitly describe Claude. | Neither deserves blanket parity certification. Ours has more local Astra evidence. |
| Production mechanics | Includes 36 vendored Scrapes skills and four pipeline front doors. Some integration is usable; some brands remain incomplete. | Skill Systems is a separate product component from the full OS. | Continue using purchased pipelines selectively. The complete OS is not required merely to access those installed skills. |
| Creative quality | Approved specimens exist alongside documented regressions. Instruction checks have not predicted taste reliably. | No matched output test on your approved standard. | No overall winner established. Judge new work against the accepted specimen. |
| Memory and continuity | Multiple stores and a retrieval facade; episodic retrieval breaks in a fresh lane because project identity changes. | Documented scoped hybrid search, expansion and exact transcript lookup. | Repair the demonstrated defect first. Evaluate the vendor retrieval design before replacing stores. |
| Client separation | Named brand roots and resolution exist; readiness and ownership validation are incomplete. | Documented root methodology plus client-specific context, memory, projects and jobs. | Adopt the separation principle within your existing client structure. |
| Learning | Telemetry exists, but native Codex events can be missed and suggestion counts can masquerade as usage. | Documented staged captures, consolidation, review/discard and provenance; a Claude Haiku default appears in consolidation. | Fix observation before believing compounding claims. Vendor learning is also untested here. |
| Task interface | Native Codex tasks, files, handoffs and tools are available, alongside local boards. | Command Centre groups goals, chats, files and changes; documentation describes Claude execution. | Keep native Codex as your active interface. A second UI does not repair memory identity or editorial drift. |
| Scheduling and teams | Existing schedules, protections and receipts; this audit did not exhaustively replay every automation. | Documented shared cron runtime and optional hosted Team OS. Retry, cost and Astra parity not exercised. | No current evidence justifies another scheduler or hosted service. Revisit when a team/hosting requirement is real. |
| Verification | Six canonical checks pass, while independent negative controls expose false readiness and blind spots. | Installer limitations verified; OS verifiers unavailable. | Improve the truthfulness of your existing checks. There is no fair numeric reliability ranking yet. |
| Updates and migration | One shared repository with isolated writer lanes; generated changes complicate integration. | Explicit base/local ownership; inspected installer incorrectly recognizes any AGENTS root as its OS. | Evaluate vendor code in a separate inspection location. Never point the inspected updater at Antigravity. |

Sources for the vendor architecture: [overview](https://docs.scrapes.ai/docs/agentic-os/what-is-agentic-os), [core concepts](https://docs.scrapes.ai/docs/agentic-os/core-concepts), [customization](https://docs.scrapes.ai/docs/agentic-os/custom-edits), [client workspaces](https://docs.scrapes.ai/docs/agentic-os/multi-client-workspaces), [layered recall](https://docs.scrapes.ai/docs/memory/layered-recall), [memory schema](https://docs.scrapes.ai/docs/memory/schema), [capture](https://docs.scrapes.ai/docs/memory/session-capture), [consolidation](https://docs.scrapes.ai/docs/memory/capture-consolidation), [Command Centre](https://docs.scrapes.ai/docs/command-centre/feed), [permissions](https://docs.scrapes.ai/docs/command-centre/task-permission-modes), and [hosted memory](https://docs.scrapes.ai/docs/team-os/memory-and-sync). These establish documented design, not a successful installation on your machine.

## What we proved is wrong

### 1. A workspace can report FULL POWER while missing historical memory

The main workspace's episodic project filter covers 25,061 conversation rows. The query “Scrapes” returned five matches.

The same module and query in a freshly bootstrapped Codex lane returned zero, with no degraded-state warning. Changing only the lane's project filter in memory restored the identical five matches.

The module derives repository identity from its checkout path. A worktree therefore looks like a different project to the historical index. Bootstrap checks a different memory database and misses this defect.

This is a **reproduced P1 defect**, not a guess about context overload. It affects the episodic store; it does not mean every memory source is unavailable. Nor does the controlled query establish that this caused a particular rejected caption.

Repair owner: [memory_facade.py](</Users/farricecain/Google Antigravity/execution/memory_facade.py>), project-key selection around line 73; [worktree_lane.py](</Users/farricecain/Google Antigravity/execution/worktree_lane.py>), memory parity around line 439.

### 2. Codex work is not consistently represented in the learning records

Controlled event fixtures produced different records for equivalent actions:

| Event fixture | Observed result |
|---|---|
| Full skill file read with a shell command | Recorded as a grep-level encounter; route feedback remained pending. |
| Equivalent native Read event | Recorded as a full skill load; feedback reconciled. |
| Native apply_patch event | No produced-artifact record. |
| Equivalent Write event | Produced-artifact record created. |
| Shell response with exit_code 7 and empty output | Failure streak stayed zero. |

The post-tool hook matcher also omits apply_patch. These are **handler and configuration defects reproduced with fixtures**. They do not establish that every desktop event takes this path, or that every shell read should count as a complete expert activation.

Practical consequence: the system may not know what was used, produced or failed. Usage analytics and learning built on those observations can be misleading.

Repair owner: [session_ledger_hook.py](</Users/farricecain/Google Antigravity/execution/hooks/session_ledger_hook.py>), full-load and shell handling around lines 468 and 536; [.codex/hooks.json](</Users/farricecain/Google Antigravity/.codex/hooks.json>), post-tool matchers around line 27.

### 3. “Ready” can describe a pipeline that cannot render

In temporary test fixtures, the brand readiness check returned true for:

- an empty voice profile, empty tokens object and nonexistent fallback renderer;
- an approved manifest entry with no actual template assets;
- an output location outside the declared brand root, when that location did not overlap another registered brand.

The last case proves an ownership-check gap, **not an observed cross-brand leak**.

Live registry checks were mixed: Farrice LinkedIn reported 11 of 12 templates ready; Jen's two pools reported not ready because tokens were missing in the registered location; Andrea lacked voice, tokens and a pool. The optimistic flag cannot certify the actual files until validation is strengthened.

Repair owner: [scrapes_brand.py](</Users/farricecain/Google Antigravity/execution/scrapes_brand.py>), readiness and ownership checks around lines 140–190. This is our adapter around Scrapes, not proof of a defect in their unavailable OS.

### 4. Follow-up routing can forget the job it is helping

In this audit, your answer “All of the above” generated an unrelated April Dunford positioning recommendation. The structured reply contains the original question as well as the answer; the router inspects the whole prompt without incorporating the active task owner.

This is **observed irrelevant routing advice**. The primary assistant retained the audit, so it is not evidence that the task actually switched. It is still unnecessary noise and a plausible contributor to accidental changes of direction.

Repair owner: [skill_router_hook.py](</Users/farricecain/Google Antigravity/execution/skill_router_hook.py>), context detection around line 211 and prompt classification around line 661. Preserve the current objective for answers and corrections; keep explicit new-task requests routable.

### 5. The green scoreboard overclaims

All six canonical baseline checks passed in this audit. They verify useful things: routing fixtures, contracts, authority text, selected hook configuration and preflight behavior.

They do not prove that a fresh task preserves your creative target, remembers the right history, completes the work or needs fewer corrections.

Specific proof defects:

- The weekly “behavioral” evaluation passed several cases because instructions or bindings existed. Its verbosity pass did not inspect an output.
- The router labels suggestions as experts deployed before deployment.
- A telemetry snapshot showed 232 route records and four automatic feedback records, with no human outcome ratings in that stream. It is not a useful quality percentage.
- The canonical verifier tolerates an absent or disabled dangerous-git hook and checks for the presence of trusted-hash text rather than verifying a matching hash. **That protective hook is currently enabled**; this is a weakness in the verifier, not a finding that the protection is off.
- Health reporting converts failed Notion queries to zero and derives downstream failure from that number.
- The audit workflow first defers historical verifiers, then mandates them later.

Repair owners: [weekly evaluation record](</Users/farricecain/Google Antigravity/.agent/mission-queue/done/card-harness-evals-2026-W36-transcript.md>), [verify_google_operator_core.py](</Users/farricecain/Google Antigravity/execution/verify_google_operator_core.py>), [system_health.py](</Users/farricecain/Google Antigravity/execution/system_health.py>), and [system-audit workflow](</Users/farricecain/Google Antigravity/.agent/workflows/system-audit.md>).

### 6. Old operating assumptions still compete with present capabilities

The global AGENTS file, project AGENTS file and manually loaded CODEX specification total approximately 90,700 bytes and 11,284 whitespace words on disk. That is **not an actual token count or a measured percentage of capacity lost**. The relevant problem is overlap and competing requirements.

The shared orchestration doctrine still specifies Claude model IDs and restrictions on direct conductor writing, without an Astra interpretation. Hot/cold policy says the advertised surface should be small, while the live wrapper directory contains 2,721 entries. Directory counts do not prove that all entries are loaded into a prompt.

OpenAI specifically recommends auditing instructions when using Astra because it follows skill and AGENTS guidance more sensitively. Its guidance also highlights clarification pauses, verbose output and disproportionate testing. [Official Astra guidance](https://developers.openai.com/api/docs/guides/latest-model)

**Current-state correction:** live configuration now selects gpt-6-astra with ultra reasoning effort. Learning-output style and automatic JARVIS startup injection are already disabled. The earlier adjacent audit correctly identified those conflicts, but its unapplied-change proposal is now stale. This task did not change those settings. Their absence from configuration is verified; improved creative performance still needs a production test.

## What Scrapes actually improves

Scrapes' useful design contribution is coherence:

- One clearly owned shared instruction source.
- An explicit separation between vendor files and user customization.
- Client-scoped context instead of repeatedly reconstructing a brand.
- Search that expands to exact evidence when needed.
- Raw session capture separated from promotion into durable memory.

These are good principles for your operating structure. Several already have partial equivalents in Antigravity. Borrowing them should remove ambiguity in existing components, not create another parallel framework.

The documented OS is not exclusively Codex-native. Command Centre execution and permission modes refer to Claude; consolidation names a Claude Haiku default. New Command Centre goals default to Full access in its documentation. Your existing action boundaries would need to be carried over and tested. AGENTS compatibility alone cannot establish runtime parity.

The inspected installer has two further limitations:

1. Its detector accepts any AGENTS.md as proof of an Agentic OS installation. A read-only probe incorrectly identified Antigravity as an installed OS. The install path can then become an update path that fetches the vendor updater. No update was executed.
2. The version status hardcodes available to null and outdated to false. “Not outdated” is therefore not a remote version comparison.

Both findings apply to cached installer **v1.3.0**. They are not claims about every later installer release or the unavailable OS implementation. Source: the cached [adapter](</Users/farricecain/.npm/_npx/8938a9bcd02ed5f7/node_modules/@scrapes/installer/src/adapters/agentic-os.js:111>) and [installer flow](</Users/farricecain/.npm/_npx/8938a9bcd02ed5f7/node_modules/@scrapes/installer/src/flow.js:269>).

## The structure I recommend for Astra

**One active runtime: native Codex. One small shared operating contract. Your library and vendor production modules loaded for the job.**

| Layer | Responsibility | Existing surface to use |
|---|---|---|
| Native runtime | Model execution, tools, tasks, delegation, steering and app approvals | Codex itself |
| Shared operating contract | User intent, initiative, truth, preservation and real action boundaries | Consolidated existing global/project instructions; platform-specific details scoped correctly |
| Current work context | Approved specimen, latest decisions, source locations, brand and next deliverable | Existing client/project folders and verified handoffs |
| Retrieved capability | Domain craft and exact production methods needed now | Antigravity skills plus installed Scrapes pipelines |
| Deterministic support | Memory identity, asset validation, event accounting, budget and repository protection | Repaired existing execution helpers |
| Evidence | Changed behavior, inspectable artifacts, explicit uncertainty and user taste | Existing receipts/evaluations with honest labels |

This keeps broad capability available while limiting how many controllers compete over a single task. It does not mean weakening research or replacing extracted expertise with generic output.

## Best course of action

**First: repair the measured reliability defects.** Start with memory identity and Codex event observation; then readiness validation and follow-up routing. Preserve baseline evidence and use the exact failing cases as regression tests. The companion repair brief specifies outcomes and acceptance criteria without introducing a new framework.

**Second: simplify only the instructions shown to conflict.** Scope legacy model rules, reconcile the audit workflow, and remove repeated global requirements through an explicit review. Global changes remain a separate approval boundary. Do not rewrite every skill, delete the library, or add another universal gate.

**Third: run a small matched output comparison.** Hold the model, sources, tools, action permissions and approved target constant. Compare existing and repaired behavior on one creative task, one research task and one interrupted/revised task. Obtain Scrapes source and add its isolated runtime only after its actual Codex path is understood.

Measure accepted output, unnecessary user interventions, preservation of corrections, unsupported claims, successful completion and elapsed time. Expand only if the first comparison changes the decision.

**We should reconsider this verdict if** Scrapes consistently completes the same tasks with fewer interventions, preserves your craft and context, respects the same boundaries, and costs less to maintain after migration. A polished dashboard or more installed skills would not be enough.

## What this audit changed

The audit produced the comparison, a prioritized repair brief, independent negative-control evidence, a current configuration snapshot, and six passing canonical baseline results. Two authorized read-only auditors challenged the design and the proof independently.

No harness implementation, global configuration, client files, scheduled jobs or vendor installation was changed by this task. No paid generation, external send or publication occurred. Report files are isolated in the audit lane. The saved negative-control replay ran successfully and reproduced the findings; its output is in REPLAY-OUTPUT.txt. The administrative finalize self-score was marginal and is recorded separately; it is not an independent quality verdict or a claim of system repair.

**Decision:** keep the capability library and native Codex runtime; repair the existing adapter and proof surfaces; defer any full OS replacement until source access and matched behavioral evidence exist.
