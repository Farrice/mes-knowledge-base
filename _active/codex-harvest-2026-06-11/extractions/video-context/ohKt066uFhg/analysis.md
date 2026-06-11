# Video Context Analysis: Viktor AI Coworker

## Metadata

- Title: Viktor: AI Coworker That Lives in Slack - Fryderyk Wiatrowski
- Channel/Uploader: AI Engineer
- Duration: 19:29
- Publish date: 20260511
- URL: https://www.youtube.com/watch?v=ohKt066uFhg
- Video ID: ohKt066uFhg

## Evidence Status

- Spoken evidence rows: 900
- Visual frame samples: 20
- OCR rows: 0
- Uncertainty rows: 1
- Limitation: OCR is unavailable because tesseract/pytesseract is not installed or configured.

This source is safe to use as transcript-backed evidence. Visual claims should not be made unless a human or vision adapter reviews the sampled frames.

## Executive Summary

The source argues that a useful AI employee is not a separate chatbot or generic web app. It is an ambient coworker that lives in the team's existing work surface, carries enough company context to act across functions, inherits or scopes integrations deliberately, and earns broad activation through staged trust.

For Codex Antigravity, the strongest reusable upgrade is a command-grade AI Employee OS contract: every agent-like system should define its role, work surface, context boundaries, integration permissions, event semantics, proactivity threshold, personality/model regression guard, and rollout ladder before being treated as a real AI employee.

## Source-Backed Operating Principles

| Principle | Transcript Evidence | Antigravity Translation |
|---|---|---|
| Live where the work happens | 00:00:57-00:01:10 describes the employee living in Slack, participating in threads and channels, and avoiding a separate web app. | Agent systems should identify the natural work surface before designing the workflow. In Codex this usually means conversation, local files, command bridges, and recurring loops rather than a new UI. |
| Company agent differs from personal agent | 00:05:30-00:06:28 contrasts a personal agent with a company agent that lives where people work, has company context, and can reuse a connected integration for the team. | The command must separate personal-agent and team/company-agent designs, including shared context and inherited permissions. |
| Memory scales into leakage risk | 00:06:44-00:08:15 says memory concerns multiply across users and channels, with growth/executive context needing isolation from engineering/support/DMs. | Any Antigravity agent employee needs a context partition map, access rule, and leakage test before broad use. |
| Ambient interfaces change event semantics | 00:10:13-00:11:51 explains that DMs, public channels, threads, reactions, edits, deletes, and thread drift must fit into linear context. | The OS should force an event ledger: create/update/delete/reaction/thread-hop semantics, not just "last message". |
| Latency is judged by interface expectations | 00:08:55-00:10:06 says a ten-minute agent task feels bad in a web app but impressive in Slack. | The workflow must set expected latency and progress posture by surface. Long work should produce status, handoff, and completion signals. |
| Personality is product behavior | 00:11:55-00:13:00 describes a model swap that looked good for tool calling/codegen but failed because users disliked the personality. | Model changes need personality, trust, and interaction regression checks, not only task-quality checks. |
| Proactivity must earn trust | 00:13:02-00:14:24 praises proactive workflow suggestions but warns against day-one workspace-wide DMs/thread participation. | Proactivity gets a ladder: observe -> suggest -> ask -> act in sandbox -> act with approval -> broader activation. |
| Shared integrations need scope | 00:14:35-00:17:00 describes shared integrations saving effort, wrong integrations causing confusion, and personal email leakage driving scoped integrations. | Integrations need ownership, scope, allowed surfaces, private/team split, audit trail, and revocation rules. |
| Great AI coworkers have three pillars | 00:17:06-00:17:51 summarizes: get work done, know the company/use context well, and make it friendly. | Score every AI employee on execution, context/access, and trust/experience. |

## Build Shape Decision

- Selected shape: full command-grade skill system.
- Command: `/ai-employee-os`
- Skill package: `skills/fryderyk-wiatrowski-ai-employee-os/`
- Semantic contract: `semantic_libraries/antigravity/primitives/ai-employee-operating-contract.md`
- Command bridge: `.agent/workflows/ai-employee-os.md`, `.claude/commands/ai-employee-os.md`, `.agents/skills/source-command-ai-employee-os/SKILL.md`

This should not become a giant all-purpose agent skill. It should be an orchestrator and operating contract that reuses `/context-audit`, `/memory-architect`, `/conde-agent-experience-design`, `/24-assets-agent-system-design`, trust architecture, and production hardening routes.

## Reuse Hook

Use `/ai-employee-os` when a workflow, agent, automation, recurring job, content system, or client delivery system should behave less like a tool and more like a trusted employee with role ownership, context boundaries, controlled proactivity, and a staged trust path.
