# Source-To-Skill Extraction

## Purpose And Operating Definition

This primitive governs converting source material into a deployed Antigravity capability. The work is not "summarize the source." The work is deciding what the source should become, extracting the useful operating method, building the right artifact, registering it, and proving future agents can use it.

## When To Use

- A user asks to extract, forge, fully leverage, or operationalize a source.
- A transcript, YouTube video, PDF, article, course, book, or pasted content contains a repeatable method.
- A source should become a skill, companion skill, workflow, reference, agent, semantic document, or productized business asset.

## When Not To Use

- The user only wants a short summary.
- The source is too thin to justify durable system changes.
- The source belongs as an example inside an existing skill rather than a new capability.
- The source requires private or paid access that has not been provided or approved.

## Inputs

| Input | Required | Source Of Truth | Notes |
|---|---|---|---|
| Source material | Yes | Transcript, file, URL, pasted content, OCR output | Preserve the raw or cleaned source when feasible |
| User intent | Yes | Current conversation | Capture business, client, personal, or productized use |
| Existing arsenal | Yes | `AGENT_INDEX.md`, `SKILL_INDEX.md`, routers, relevant skills | Prevent duplicates |
| Build boundary | Yes | AGENTS.md and user instructions | Do not modify original Google Antigravity workspace |
| Verification path | Yes | validation scripts and router output | Must be run before final if files change |
| Behavior-changing proof | Yes when enhancing a capability | Before/after, cold-start run, applied scenario, or transformed artifact | Prevents summaries and wiring from being mistaken for deployment |

## Outputs

| Output | Format | Destination | Owner |
|---|---|---|---|
| Extraction brief | Markdown | `extractions/[slug]/` | Implementing agent |
| Skill or companion files | Markdown | `skills/[slug]/` | Codex Antigravity |
| Workflow command bridge | Markdown | `.agent/workflows/`, `.claude/commands/`, `.agents/skills/` | Codex Antigravity |
| Semantic primitive | Markdown | `semantic_libraries/[library]/primitives/` when needed | Semantic library owner |
| Productization artifact | Markdown | extraction folder or deliverables | Operator |
| Validation evidence | Command output, trace, log | final response/local trace | Implementing agent |
| Behavior proof | Markdown or command output | capability home, extraction folder, or final response | Implementing agent |

## Objects And Meaning

| Object | What It Means | Why It Matters |
|---|---|---|
| Source | Raw expert or methodology input | Must be grounded before synthesis |
| Extraction | Operating method distilled from the source | Prevents shallow collection |
| Skill | Reusable methodology package | Loads expertise for future work |
| Workflow | Executable protocol | Turns expertise into action |
| Skill system | Orchestrated chain of small components | Turns isolated skills into end-to-end capability |
| Command bridge | Invocation surface | Makes the workflow discoverable |
| Semantic document | Agent-readable work primitive | Prevents hidden meaning gaps |
| Finalize trace | Local quality memory | Creates retrieval evidence |

## Authority And Permissions

| Action | Agent May Do | Requires Approval | Never Do |
|---|---|---|---|
| Read local source and existing skills | Yes | No | Do not bulk-load irrelevant files |
| Fetch public transcript | Yes if needed | Network approval if sandbox requires it | Do not bypass network restrictions |
| Create files in Codex Antigravity | Yes | No | Do not edit Google Antigravity |
| Use paid/quota-heavy tools | No by default | Explicit approval | Do not silently incur cost |
| Publish or contact anyone | No | Explicit approval | Never treat internal extraction as external action |

## Execution Protocol

1. Capture the user intent and desired deployment surface.
2. Acquire or read the source; preserve transcript, OCR, or source path.
   - For YouTube source packages, preserve raw `transcript.vtt`, clean `transcript.txt`, timestamped `transcript_segments.json`, metadata, ledger, and uncertainty report.
   - Use the clean transcript for reading; use segments and ledger rows for evidence.
3. Route the existing arsenal with command, workflow, expert, and context routers.
4. Decide build shape: summary, reference, semantic document, workflow, skill system, companion skill, companion OS layer, new skill, agent, or productized asset.
5. Extract operating principles, hidden knowledge, examples, failure modes, and quality criteria.
6. Build only the artifacts needed for durable execution.
7. Add command bridges when a workflow should be invoked by slash command.
8. Sync registries if skills or agents changed.
9. Validate skill, router discoverability, command bridge, and at least one cold-start use case.
10. Add behavior-changing proof when the build claims to enhance a capability.
11. Finalize locally and report any remote logging failure plainly.

## Decision Rules

| Condition | Rule | Reason |
|---|---|---|
| Existing skill already owns the domain | Prefer companion, expansion, reference, or workflow | Prevents duplicate expertise |
| Source contains an operating method | Build workflow or skill, not just notes | Captures deployable leverage |
| Source contains orchestration mechanics | Build a skill system or companion OS layer | Avoids isolated skills and mega-skills |
| Source changes how agents should act | Add semantic primitive or validation doc | Prevents hidden execution assumptions |
| Source has commercial use | Add productization artifact | Turns knowledge into revenue path |
| Workflow should be command-invokable | Add all three bridge layers | Prevents command misfires |
| Validation cannot run | State exactly what failed and why | Avoids false confidence |

## Examples

### Good Example

A Nate B. Jones video about semantic work primitives becomes a companion OS skill, five command workflows, a semantic library layer, validated primitives, and a productized service blueprint.

### Counterexample

Creating a long summary of the video without command surfaces, validation, or a way to apply it to client work.

## Quality Tests

| Test | Pass Criteria | Failure Response |
|---|---|---|
| Source grounding | Raw or cleaned source is saved or cited | Re-acquire source or mark limitation |
| Arsenal routing | Existing relevant skills/workflows are checked | Run routers before building |
| Build-shape fit | Artifact type matches source leverage | Reclassify as reference/companion/workflow |
| Bridge completeness | All invocation layers exist when needed | Add missing layer |
| Registry truth | Indexes include new skill/agent | Run registry sync |
| Skill validation | No critical validation errors | Fix missing required files |
| Router discoverability | Command/workflow search finds new surface | Improve metadata or bridge |
| Cold-start use | Agent can use the artifact without hidden explanation | Add semantic document or examples |
| Behavior-changing proof | A realistic input is transformed or a cold-start run proves the capability changes behavior | Add a proof lab, applied scenario, or verifier fixture |
| Productization | Commercial source includes offer/use cases when relevant | Add productization artifact |

## Failure Modes

| Failure Mode | Early Signal | Prevention | Recovery |
|---|---|---|---|
| Shallow summary | Output has ideas but no execution surface | Use build-shape decision gate | Convert into workflow/skill/reference |
| Duplicate skill | New slug overlaps existing expert | Search indexes and routers | Reframe as companion/expansion |
| Missing bridge | Command exists in one layer only | Use bridge checklist | Add missing shims |
| Source drift | Claims exceed source evidence | Preserve transcript and extraction brief | Remove unsupported claims |
| Remote logging failure | Notion DNS/API error | Use `--skip-notion` or local trace | Report local finalize evidence |
| Hidden authority gap | Workflow can act but not decide when to stop | Add semantic primitive | Run validator |
| Structural pass, usefulness fail | Routes, registries, and docs pass but the user cannot see changed output quality | Require behavior-changing proof | Build a before/after proof lab or cold-start fixture |

## Maintenance Protocol

- Owner: Extraction Governor Agent and Codex Antigravity operator.
- Review cadence: after every new forge or major extraction build.
- Update triggers: bridge convention changes, new validation scripts, repeated extraction failure, new productized source pattern.
- Last updated: 2026-05-06.
