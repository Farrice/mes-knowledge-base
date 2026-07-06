---
name: "Fryderyk Wiatrowski AI Employee OS"
description: "Design, audit, and upgrade AI employee systems with ambient work surfaces, context isolation, scoped integrations, event semantics, trust ladders, rollout gates, and model/personality regression checks."
version: "1.0"
format: "skill-system"
workflows: 1
source_url: "https://www.youtube.com/watch?v=ohKt066uFhg&t=195s"
source_package: "extractions/video-context/ohKt066uFhg"
contract: "semantic_libraries/antigravity/primitives/ai-employee-operating-contract.md"
---

# Fryderyk Wiatrowski AI Employee OS

Use this skill when the user wants an AI employee, AI coworker, company agent, operating partner, internal operator, or agent system that should behave like a trusted teammate instead of a generic tool.

This skill is source-backed by the Viktor AI coworker talk. It is vendor-neutral for Antigravity use: it does not require Slack, Viktor, Pipedream, or any specific model. It extracts the operating method into a local Codex command system.

## Source Grounding

- Evidence package: `extractions/video-context/ohKt066uFhg/`
- Evidence map: `extractions/video-context/ohKt066uFhg/evidence-map.md`
- Extraction brief: `extractions/video-context/ohKt066uFhg/extraction-brief.md`
- Operating contract: `semantic_libraries/antigravity/primitives/ai-employee-operating-contract.md`

## Command Surface

Run through the workflow:

```bash
/ai-employee-os [target system or agent]
/ai-employee-os --audit [target]
/ai-employee-os --design [role/context/tools]
/ai-employee-os --upgrade [route/skill/workflow]
```

## Operating Rule

An AI employee earns scope. Start with role clarity, context isolation, scoped integrations, and trust gates before broad proactivity or autonomy.

## Component Order

1. **Intent lock**: decide audit, design, or upgrade.
2. **Source and target read**: load the compact contract, evidence map, and target files only as needed.
3. **Surface map**: identify where the employee lives and which events it receives.
4. **Context/access map**: partition memory and integrations before granting autonomy.
5. **Employee contract**: define job, non-job, inputs, outputs, approvals, and handoffs.
6. **Proactivity ladder**: stage observe, suggest, ask, draft, sandbox act, approved act, and broader activation.
7. **Regression guard**: protect tone, trust, leakage, event semantics, and model swaps.
8. **Implementation sequence**: produce the first safe build or upgrade path.

## Supporting Routes

Use these as components, not replacements:

- `/context-audit` for context bloat and compression.
- `/memory-architect` for persistent memory tiers, decay, and retrieval.
- `/conde-agent-experience-design` for trust, progress, handoffs, and command UX.
- `/24-assets-agent-system-design` for roster, ownership, and data flow.
- `/source-to-skill-system` for future source-to-OS expansions.
- Trust architecture and production hardening lenses for permission, security, and regression checks.

## Required Output

Every serious run must produce:

1. AI Employee OS scorecard
2. AI employee system contract
3. Context/access map
4. Event semantics map
5. Proactivity and trust ladder
6. Model/personality regression guard
7. Validation checklist
8. First implementation sequence

## Boundaries

- Do not connect Slack, Gmail, Drive, calendar, CRM, or other external systems without explicit approval.
- Do not publish, message, DM, invite, email, or automate accounts unless the user explicitly asks.
- Do not mix client, team, project, or private context without a named access rule.
- Do not treat model replacement as safe because task outputs look correct; check personality and trust.

## Quality Bar

- The output names the employee's job and non-job.
- Every context source has a scope and leakage risk.
- Every integration has owner, allowed actions, approvals, and revocation path.
- Ambient events are linearized into a usable event ledger.
- Proactivity is staged, not turned on globally.
- The final path is useful in Codex today and extensible to external team surfaces later.
