---
description: Source-backed Kallaway content OS route from strategy to production, retention, craft, batch feedback, and monetization
---

# Kallaway Content OS Orchestrator

## Pre-Flight

Read only the files needed for the current lane:

1. `skills/kallaway-content-operating-system/SKILL.md`
2. `skills/kallaway-content-operating-system/references/source-evidence-map.md`
3. `skills/kallaway-content-operating-system/references/skill-system-contract.md`
4. The relevant source package `analysis.md`, `video-context-ledger.md`, and `uncertainty-report.md`
5. The selected downstream Kallaway component skill/workflow files

## Intent Lock

State:

- Goal:
- Audience:
- Platform or format:
- Offer or monetization path:
- First artifact:
- Evidence packages loaded:
- Components selected:
- Components skipped:

Ask only if the missing information changes the execution path. Otherwise state assumptions and proceed.

## Lane Selection

| User Need | Primary Source Evidence | Component Chain |
|---|---|---|
| Build an audience of buyers | `oRYfJ_yxz6M`, `7pCEsr-0KIw` | `kallaway-content-psychology -> /kcs-topic-format -> /kcs-substance -> /obsession-level-architect -> kallaway-social-commerce` |
| Run the content production system | `B9l9TRhu5Vw`, `1q__Vs2JqbI` | `/ai-topic-mining -> /kcs-topic-format -> /kcs-substance -> /kcs-hook-triad -> /kcs-script-profile -> /kcs-edit-path -> /kcs-performance-loop` |
| Adapt to social media in 2026 | `ImzoNTrgvFg`, `bqzd0h0gmU0` | `kallaway-content-psychology -> kallaway-social-commerce -> /kcs-10x-batch` |
| Create obsession or belief shift | `cuVyTmbOZjk` | `/obsession-level-architect -> /five-input-content-gate -> /bankshot-suggestion-engine -> /word-expert` |
| Build hooks that cannot be skipped | `onQoYdxWXdA` | `/kcs-hook-triad -> /word-opener -> /word-grip -> /addiction-loop-architect` |
| Upgrade storytelling and retention | `SDHKQbKC7gA` | `/addiction-loop-architect -> /loop-chain-scripting -> /word-rhythm -> /word-grip` |
| Create content faster with AI | `1q__Vs2JqbI`, `B9l9TRhu5Vw` | `/ai-topic-mining -> /ai-hook-extractor -> /ai-creative-sprint -> /kcs-one-rep` |

## Execution Protocol

1. Select the lane and evidence packages.
2. Load no more than three source analyses unless the user asks for a full evidence synthesis.
3. Produce a compact source evidence summary.
4. Run the component chain in order.
5. After each component, write a handoff:

```markdown
## Skill System Handoff: [Component] -> [Next Component]
- **Source evidence**: [path or timestamp rows]
- **Component used**: [skill/workflow/script/agent]
- **Output produced**: [file/path/object]
- **Next input**: [what the next step receives]
- **Validation**: [pass/fail/check]
- **Open risk**: [none or exact limitation]
```

6. Produce the first artifact:
   - content strategy blueprint
   - one-rep production brief
   - hook and story package
   - 10-video batch plan
   - content system audit
   - content-to-revenue map
7. Close with validation, next command, and reuse hook.

## Quality Gate

Before final output, confirm:

- Evidence claims are grounded in source packages or explicitly marked as assumptions.
- OCR is not treated as available unless the source package has OCR rows.
- The output is not a generic content plan.
- The artifact can be used immediately without asking the user to choose another workflow.
- Buyer quality, batch learning, and monetization are considered when relevant.

## Failure Modes

| Failure | Recovery |
|---|---|
| Source package missing | Run `python3 execution/video_context_ledger.py '<url>' --mode full` or mark source unavailable. |
| Too many components selected | Pick one function owner and reduce to the smallest complete chain. |
| Output becomes a summary | Re-route to a first artifact: blueprint, script package, hook suite, batch plan, audit, or monetization map. |
| Kallaway component overlap | Use this OS layer as the orchestrator and keep the existing component skill as the method owner. |
| Visual claim lacks proof | Remove the claim or mark it as inferred/uncertain. |
