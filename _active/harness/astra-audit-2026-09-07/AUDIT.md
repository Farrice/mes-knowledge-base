# Astra harness audit and working guide

September 7, 2026 · Historical diagnostic baseline, followed by approved repair. The two global configuration changes are now applied and observed in a fresh task. See `REPAIR-RESULT.md` for current status; proposal language below describes the original decision point.

## Verdict

There are real instruction conflicts that can restrict useful execution. The evidence does not show that Astra is running at a lower model capability, or that the wrong workspace caused all of Jen's writing problems. The clearest failures are loss of the approved creative target, premature generalization from one success, and conflicting automatic behavior instructions.

Your prompting was sufficient to state the desired result. Better operating instructions can reduce friction, but you should not have to repeatedly diagnose the assistant's writing or remember the internal workflow names.

OpenAI's current [Astra guidance](https://developers.openai.com/api/docs/guides/latest-model) specifically notes sensitivity to skill and AGENTS.md instructions, clarification pauses, verbose output, restrained delegation, and excessive testing on small changes. Those are reasons to audit instruction quality and test behavior, rather than simply increase reasoning effort.

## What actually happened with Jen

The central chain reviewed was **Research: Jen Instagram Content - Topic and Format Mechanics**, **Content: Jen Reels - Buyer-First Hooks and Captions**, and **Content: Jen Writing - Restore Approved Standard**. Native task retrieval was supplemented with the exact local conversation records where the app returned empty turn items. This is a focused causal audit of that chain, not a claim to have exhaustively read every Jen task.

1. Earlier work ran in Google Antigravity worktrees. There were already writing failures there: the group-chat story was rejected after the original kitchen/101 carousel received a 10/10 aesthetic verdict. A technically successful render did not establish successful storytelling.
2. The assistant requested a fresh Google project worktree. When the task was not available, it created a **projectless replacement** under Documents/Codex. The operator did not accidentally choose that location. The parent explicitly transferred the full project, eight research documents, approved visual assets, VidIQ evidence, and creative direction.
3. The approved “Sorry, one more question…” caption was produced in that projectless workspace with Astra. Both the success and subsequent failures occurred there. Earlier failures occurred inside Google worktrees. This contradicts a location-only explanation.
4. The successful run had the full conversational reference, preferred caption B, Jen's actual language, and one clear purpose. It also read the eight research documents. This was neither a research-free success nor evidence that tiny context alone caused it.
5. **The successful post came before the new playbook and Jen Studio package.** Those artifacts attempted to explain and reproduce the success; they did not cause it. The assistant then expanded to multiple formats before another specimen had earned approval.
6. Subsequent drafts copied surface friendliness, added an unwanted spoken component, or invented situations without a comparable inspected source. The user repeatedly corrected these changes.
7. The later recovery selected high-view B-roll references whose instructional captions did not match the conversational execution the user valued. It recovered source evidence while losing the approved creative target.

**Diagnosis:** the assistant treated each correction as a replacement objective instead of preserving the accumulated objective. “Use winners” displaced “match this conversational craft.” “Make it repeatable” became permission to package a broad system before proving transfer. These are judgment failures, not proof of inadequate prompting.

The latest source task is active and already contains a transfer request. This audit did not send it a message, relocate its files, or start competing Jen production.

## Severity-ranked findings

| Priority | Finding and evidence | Practical effect | Recommended treatment |
|---|---|---|---|
| P1 | **Learning output style is enabled and injected in this session.** It directs the assistant to ask the user to implement 5–10 lines and add educational callouts. | Can turn execution into teaching homework and inflate responses. | Disable this plugin for normal work; enable deliberately for coding lessons. Global approval required. |
| P1 | **JARVIS SessionStart injects a complete competing orchestrator.** It requires scale scoring, a deployment proposal and a permission prompt; its script reads the entire orchestrator and failure registry on startup/resume/clear/compact. | Competes with one-owner execution and introduces unnecessary ceremony. | Disable the automatic startup hook, retaining the plugin's callable capabilities. Global approval required. |
| P1 | **Live follow-up routing ignored task continuity.** Explaining which Jen task failed triggered a recommendation to load the real-estate writing skill during this system audit. | Can switch from diagnosing a system to producing the domain artifact mentioned in the example. | Treat recommendations as advisory; repair session-aware routing only with a regression case that preserves the active audit. |
| P1 | **Production continuity drift is proven in the Jen chain.** Approved register and medium gave way to different purposes and premature packaging. | User spends repeated turns restoring already-stated requirements. | Keep approved examples and current decisions authoritative; prove one new complete post before widening formats. No new universal checklist required. |
| P1 | **Some behavioral evidence is structural evidence mislabeled.** Weekly eval E5 says verbosity passes because model instructions specify length constraints; E1 cites a routing binding and E2 cites the mirror block. | A green score can coexist with failures the user sees. | Measure actual outputs and user turns. Retain real code probes but label what they establish. |
| P2 | **Platform-specific seating is not mapped to Astra.** The shared doctrine uses Fable/Opus/Sonnet rules, including a closed list for direct conductor writing; searched canonical model notes contain no Astra mapping. | If copied literally into Codex, it can restrict direct writing or imply unavailable model dispatch. | Scope those rules to the platform they describe. Astra can execute directly here; native tools determine available models. No automatic remapping of Claude work. |
| P2 | **Instruction volume and duplication are measurable; harm is not quantified.** Global AGENTS.md, project AGENTS.md and CODEX.md total 90,700 bytes / 11,285 whitespace words, before skills, memory, tools or plugin injections. The advertised skill surface is broad despite a documented small hot surface. | Conflicting requirements demand interpretation and may distract from the active job. | Reduce competing authority and redundant startup text first. Preserve the library for selective retrieval. Do not invent a percent of capacity lost. |
| P2 | **Health report converts unavailable evidence into zero.** A failed Notion query returns count=0, then the report recommends starting the log and shows downstream systems blocked. This run's query failed DNS resolution. | Encourages repairs for an unverified absence of data. | Report UNKNOWN and preserve the actual error. Do not infer an empty database or failed learning loop from this run. |
| P2 | **Audit workflow contradicts itself.** It declares the older control-plane/cohesion verifiers deferred, then requires them in later steps. | Can produce needless red checks and repair work against deliberately unwired architecture. | Reconcile the existing workflow around canonical baseline vs optional historical checks. |
| P2 | **Context sharing is partial.** Parent task initially confused the live side conversation with a separate sidebar task. The continuation still said 30 VidIQ credits were pending after the transcript showed approval. | Files and handoff summaries can lag live decisions. | Read the actual latest decision where available; transfer paths, approvals and open work explicitly. Do not ask for an already-granted approval. |

A stored mismatch is a defect even when an instruction-aware assistant works around it. Conversely, the audit does not establish that every conflict caused a particular rejected caption.

## What passed, and what those passes mean

| Check run in the canonical workspace | Result | Scope |
|---|---|---|
| verify_google_operator_core.py | PASS | Hot surfaces, routing fixtures, hook trust/configuration, synthetic hook probes, local preflight and receipt checks. |
| verify_codex_authority.py | PASS | Peer constitution authority checks. |
| verify_autopilot_runtime_preflight.py | PASS | Intent and boundary fixtures, including negative controls. |
| verify_skill_system_contract.py | PASS | Skill-system contract checks. |
| verify_subagent_approval_language.py | PASS | Delegation policy checks. |
| platform_compiler.py lint --json | PASS | No reported lint failures. |
| codex_operator_preflight.py on this audit | PASS, limited | Correctly selects system-audit and permits local work; its predicted-need prose prematurely assumes a wiring failure. |
| Global bridge preflight invoked from /private/tmp | PASS | Can resolve and route into Google Antigravity outside the project; does not prove identical plugin/skill injection everywhere. |
| Isolated audit lane bootstrap | PASS | Reports FULL POWER, 18 links and one context snapshot. |

Live observations also establish that startup plugin content and the prompt router fired here. They do not prove every hook works in every app event. The main checkout had unrelated changes; the report was saved in an isolated lane. A sandbox denial of the initial Git write was resolved through the normal approval tool, without a user workaround.

Telemetry reported 228 routing records and four feedback records. That is sparse and inconsistent quality evidence, not a reliable accuracy percentage. Protocol activation counts likewise do not establish useful outcomes. No matched Astra-vs-prior-model test or full-vs-lean harness generation experiment was run. No percentage improvement or recovery of “full capacity” is claimed.

## How to work with Astra in this harness

### Give the target and the evidence that defines good

Use natural language. State what should exist, who it serves, the approved example if there is one, what must survive, and the boundary on action. I should choose the method, retrieve the right material, close research gaps, and deliver the work. You should not need to name a dozen experts or specify each step.

For Jen, the useful brief is:

> Create one complete B-roll post for Jen's first-time buyers in the San Fernando Valley. Read the exact approved “Sorry, one more question…” post, its full source packet, and our latest creative direction. Find a relevant real-estate execution whose writing earns comparison with that standard. Preserve the conversational quality and screen-to-caption relationship; use original language. Deliver the overlay, simple footage suggestion and full caption first. Include a natural invitation only if it belongs. Keep the wider studio goal in view, but do not expand formats or build infrastructure before this example works. Use existing authorized research, and carry forward every prior decision unless I change it.

That brief is a convenience, not a new required incantation. “Continue Jen's approved brief and show me one finished post” should work once the current task has the named sources and current decisions.

### Separate durable intent from the next reviewable unit

“The goal is a repeatable content studio; today's unit is one complete B-roll post.” This lets the assistant preserve the ambition without attempting to prove all formats at once. Small output scope can still involve deep research and editorial work.

### Steer during work

Correct a premise, add a source, or reject a direction while the task is active. The assistant should incorporate that into the current objective, not restart the job or drop earlier requirements. A useful correction is: “Keep the purpose and audience; change the delivery. This critique does not replace our prior decisions.”

### Use fresh tasks when the evidence packet is ready

A fresh task can reduce anchoring on rejected work. It does not automatically inherit another task's unsaved decisions or worktree files. Keep the broader research reachable, and put the accepted specimen, latest direction, source paths and next unit at the front. Ask the assistant to create the task in the Google project and verify it is ready; do not make the operator manage the transfer.

### Delegate deliberately when it helps

Subagents are available, but this session's policy requires explicit authorization. For independent research or diagnostic comparisons, authorize a bounded number and role. For a single voice-sensitive post, the primary writer can work directly. More agents are not evidence of stronger craft. No subagents were used in this audit.

### Use proof suited to the work

For writing: compare the complete new piece with the approved example and actual source. For coding: test changed behavior and the relevant failure path. For research: inspect underlying evidence and mark uncertainties. For commercial claims: observe buyer behavior. Passing a format check never substitutes for the result being good.

## Keep, change, and test

**Keep:** source material and extracted craft, approved examples, user taste decisions, evidence honesty, cost controls, isolated worktrees, and approval for external/destructive/global actions. These preserve trust and usable work.

**Change first:** teaching-by-default and automatic competing orchestration. A small exact configuration proposal is in CHANGE-PROPOSAL.md. It requires global approval and a fresh task to validate activation.

**Test next:** one original Jen adaptation with the same authoritative sources and a comparable full reference. Evaluate craft, unnecessary questions, time to usable draft, and preservation of the brief. Improvement remains unproven until that output exists and is judged.

Do not add another universal behavior layer to fix accumulated behavior layers. Repair the existing sources of conflict, preserve what earned approval, and measure the result.

## Evidence locations

- Global settings: `/Users/farricecain/.codex/config.toml`, model lines 2–3; learning plugin lines 139–140; JARVIS hook state around line 602.
- JARVIS startup injection: `/Users/farricecain/.codex/plugins/cache/jcc-local/jarvis-command-center/1.0.3/hooks/session-start.sh` and `skills/orchestrator/SKILL.md`.
- Workspace seating: `directives/orchestration-doctrine.md`, especially lines 80–139.
- False-zero report: `execution/system_health.py`, lines 112–118, plus the recorded DNS failure.
- Weekly eval: `.agent/mission-queue/done/card-harness-evals-2026-W36-transcript.md`, lines 7–14.
- Existing corrected Jen history: `/Users/farricecain/Documents/Codex/2026-09-07/jen-content-studio/outputs/jen-approved-post-recovery.md`, `CONTINUE-JEN.md`, and `jen-approved-execution-brief.md`.
- Exact workspace-switch record: `/Users/farricecain/.codex/sessions/2026/09/05/rollout-2026-09-05T10-39-05-01a072a7-0b48-77b1-8bac-941cb8f17511.jsonl`, records at lines 3987 and 4227. The first requests the project worktree; the latter creates the projectless replacement.
- Exact approved run and later regression: `/Users/farricecain/.codex/sessions/2026/09/07/rollout-2026-09-07T08-18-16-01a07c72-da57-7f73-a995-745e6ad1c96d.jsonl`.

Scope boundary: no global settings, plugin files, client files, scheduled jobs or harness implementation files were edited. Audit artifacts and required local bookkeeping only. This is a diagnosis and operating guide, not a claim of completed behavioral repair.
