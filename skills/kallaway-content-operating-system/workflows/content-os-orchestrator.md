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
| Build qualified category authority or diagnose audience dilution | `1ilMGCxJBQY`, plus the relevant buyer/psychology package | `micro-fame-authority-density -> kallaway-content-psychology -> /kcs-topic-format -> /kcs-performance-loop -> kallaway-social-commerce` |
| Build an audience of buyers | `oRYfJ_yxz6M`, `7pCEsr-0KIw` | `kallaway-content-psychology -> /kcs-topic-format -> /kcs-substance -> /obsession-level-architect -> kallaway-social-commerce` |
| Run the content production system | `B9l9TRhu5Vw`, `1q__Vs2JqbI` | `/ai-topic-mining -> /kcs-topic-format -> /kcs-substance -> /kcs-hook-triad -> /kcs-script-profile -> /kcs-edit-path -> /kcs-performance-loop` |
| Adapt to social media in 2026 | `ImzoNTrgvFg`, `bqzd0h0gmU0` | `kallaway-content-psychology -> kallaway-social-commerce -> /kcs-10x-batch` |
| Create obsession or belief shift | `cuVyTmbOZjk` | `/obsession-level-architect -> /five-input-content-gate -> /bankshot-suggestion-engine -> /word-expert` |
| Build hooks that cannot be skipped | `onQoYdxWXdA` | `/kcs-hook-triad -> /word-opener -> /word-grip -> /addiction-loop-architect` |
| Upgrade storytelling and retention | `SDHKQbKC7gA` | `/addiction-loop-architect -> /loop-chain-scripting -> /word-rhythm -> /word-grip` |
| Create content faster with AI | `1q__Vs2JqbI`, `B9l9TRhu5Vw` | `/ai-topic-mining -> /ai-hook-extractor -> /ai-creative-sprint -> /kcs-one-rep` |
| Build data-enabled creativity without proxy drift | `GmIn1W9V8Rs` | `/ai-topic-mining -> /ai-creative-sprint -> /kcs-one-rep -> /kcs-performance-loop` |
| Deliver a sellable client content strategy | `GmIn1W9V8Rs` + `extractions/kallaway/` | `outlier-radar signal pack -> kallaway-ai-content-engine research controls -> /gb-orchestrate -> selected production components` |

## Execution Protocol

1. Select the lane and evidence packages.
2. Load no more than three source analyses unless the user asks for a full evidence synthesis.
3. Produce a compact source evidence summary.
4. When the authority lane is selected, load `workflows/micro-fame-authority-density.md`. Treat the seven positioning axes as search lenses, surface only the decisive contrast, and treat four reps as the minimum evidence floor.
5. For research or AI-production lanes, declare the data-maturity state (`COLD_START`, `HYBRID`, or `OWNED_LEARNING`), highest available metric class, and topic-vs-format cohort boundary.
6. Run the component chain in order.
7. After each component, write a handoff:

```markdown
## Skill System Handoff: [Component] -> [Next Component]
- **Source evidence**: [path or timestamp rows]
- **Component used**: [skill/workflow/script/agent]
- **Output produced**: [file/path/object]
- **Next input**: [what the next step receives]
- **Validation**: [pass/fail/check]
- **Open risk**: [none or exact limitation]
```

8. Produce the first artifact:
   - authority-density diagnostic
   - positioning contrast brief
   - 3-2-1 authority batch plan
   - four-rep authority review
   - content strategy blueprint
   - one-rep production brief
   - hook and story package
   - 10-video batch plan
   - content system audit
   - content-to-revenue map
9. Close with validation, next command, and reuse hook.

## Output Schema

```yaml
deliverable: "Kallaway Content OS Run"
components:
  intent_lock:
    description: "Goal, audience, platform/format, offer/monetization path, first artifact, evidence packages loaded, components selected, components skipped"
  lane_selection:
    description: "Chosen row from the Lane Selection table plus the resulting component chain string"
  source_evidence_summary:
    description: "Compact citation of the source package(s) actually read (path + evidence-row counts), or an explicit 'package not present' note per the Failure Modes table when the claimed extractions/video-context/<id>/ path does not resolve"
  component_handoffs:
    description: "One Skill System Handoff block per component run, in order: source evidence, component used, output produced, next input, validation, open risk"
  first_artifact:
    description: "Exactly one of: authority-density diagnostic, positioning contrast brief, 3-2-1 authority batch plan, four-rep authority review, content strategy blueprint, one-rep production brief, hook and story package, 10-video batch plan, content system audit, content-to-revenue map — matching the matched prompts-v2 file's own Output Contract when one exists"
  next_use_route:
    description: "The next command or chain to run, plus the reuse hook for a repeat request"
```

## Quality Gate

Before final output, confirm:

- Evidence claims are grounded in source packages or explicitly marked as assumptions.
- OCR is not treated as available unless the source package has OCR rows.
- The output is not a generic content plan.
- The artifact can be used immediately without asking the user to choose another workflow.
- Buyer quality, batch learning, and monetization are considered when relevant.
- Authority-lane outputs keep reach, fit, trust, and commercial action separate.
- Positioning outputs surface the smallest decisive contrast rather than a completed axis checklist.
- Four-rep reviews treat four fair executions as a floor and preserve `INCONCLUSIVE` when evidence conflicts.
- Public views are never reported as proof of demand, conversion, or revenue.
- Competitor research is intentionally reduced once 10-20 owned pieces provide usable first-party evidence.
- AI collection and drafting never substitute for the creator's thesis, substance, or final creative judgment.

## Failure Modes

| Failure | Recovery |
|---|---|
| Source package missing | Run `python3 execution/video_context_ledger.py '<url>' --mode full` or mark source unavailable. |
| Too many components selected | Pick one function owner and reduce to the smallest complete chain. |
| Output becomes a summary | Re-route to a first artifact: blueprint, script package, hook suite, batch plan, audit, or monetization map. |
| Kallaway component overlap | Use this OS layer as the orchestrator and keep the existing component skill as the method owner. |
| Visual claim lacks proof | Remove the claim or mark it as inferred/uncertain. |
