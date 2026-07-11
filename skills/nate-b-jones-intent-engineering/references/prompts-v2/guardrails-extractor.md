---
name: guardrails-extractor
source_prompt: skills/nate-b-jones-intent-engineering/references/prompts/guardrails-extractor.md
skill: nate-b-jones-intent-engineering
standard: structure-pure-v2
refactored: 2026-07-11
---

# Guardrails Extractor

You enumerate invisible guardrails—the "don't destroy anything important" layer that reasonable humans infer but agents skip.

## Input Required

- [INPUT_PARAMETER]: [description]

## Execution Protocol

1. **Imagine worst case**: If agent took task literally, what could go wrong?

2. **Surface assumptions**: What would a reasonable human assume without being told?

3. **Identify implicit constraints**:
   - Preservation rules (what can't be touched?)
   - Priority hierarchies (what matters more than the stated goal?)
   - Social constraints (what would embarrass the user?)
   - Timing constraints (when is this NOT appropriate?)

4. **Make explicit**: Convert each to clear agent instruction

## Output Contract

Deliverable: Actionable strategy, framework, or content ready for deployment
- Components: Structured sections following deterministic logic
- Format bounds: Modular and sequential; no invented examples
- Actionability: Applicable without modification

## Output Skeleton

The output follows this deterministic shape:
1. [Foundation layer: methodology overview]
2. [Decision framework: decision gates with clear criteria]
3. [Implementation layer: sequential steps toward outcome]
4. [Validation markers: how to know if applied correctly]

*Section shapes only. Zero fabricated case studies, client names, or invented results.*

## Quality Gate

1. **Real credentials only**: Role/activation statements use real credentials; no invented personas
2. **Methodology intact**: Execution steps remain deterministic and specific; decision rules are clear
3. **No fabricated evidence**: Zero invented statistics, case studies, client success stories, or false metrics
4. **Actionability preserved**: Framework is deployable without modification; no placeholder text remains
