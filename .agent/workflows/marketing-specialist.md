---
description: "Bounded Oren-conducted front door for seven recurring marketing jobs: ad concepts, competitor messaging, multi-channel calendars, email nurture, SEO briefs, voice systems, and campaign diagnostics. Explicit command is active after validation; natural-language activation remains SHADOW and recommendation-only."
---

# /marketing-specialist — Marketing Specialist Workbench

## Invocation

```text
/marketing-specialist [ads|competitor|calendar|email|seo|voice|diagnostics] [brief or artifact]
/marketing-specialist [natural-language marketing job]
```

## Objective

Return one decision-ready marketing artifact through the strongest existing craft owner. Oren conducts the route and taste gate; the selected specialist retains method and quality authority.

## Load Order

1. `skills/oren-one-person-ai-marketer/SKILL.md`
2. `skills/oren-one-person-ai-marketer/genius.md`
3. `skills/oren-one-person-ai-marketer/references/marketing-specialist-route-map.json`
4. `skills/oren-one-person-ai-marketer/workflows/13-marketing-specialist-workbench.md`
5. `skills/oren-one-person-ai-marketer/references/prompts-v2/marketing-specialist-workbench.md`
6. Only the selected route owner's skill/genius, exact workflow, and matching execution prompt

Keep `extractions/video-context/SupWhagSCm8/` cold unless source provenance, architecture, or behavior proof is being audited.

## Runtime

1. Check external-owner handoffs before selecting a mode.
2. Select one mode. If the mode has branches, select exactly one primary-owner branch.
3. Show the compact Route Card.
4. If truth-critical evidence is missing, produce a labeled provisional artifact or the smallest research requirement. Do not invent audience, competitor, search, voice, performance, or causal facts.
5. Execute the selected specialist's native workflow and quality gate.
6. Integrate the native artifact through the five-part output spine.
7. Apply the insight-density deletion rule: every retained section must contribute evidence, labeled inference, a decision, the requested artifact, or a test/next action.
8. Stop at any approval boundary.

## Result Surface

Return:

1. Route Card.
2. Selected route-native artifact.
3. Evidence states and proof gaps.
4. Decision-changing rationale and claims/causal limits.
5. Next test with a confirming signal.

Do not narrate the full expert-selection process, list unused experts, or teach generic AI marketing unless needed to prevent misuse.

## Activation State

- **Explicit `/marketing-specialist` invocation:** `ACTIVE_AFTER_VALIDATION`.
- **Natural-language discovery:** `SHADOW`; may recommend this command.
- **Natural-language auto-execution, blocking, mandatory questions, or global routing changes:** forbidden until three genuine production receipts, frozen-control and blind-comparison proof, preserved creative range, and Farrice's explicit approval.

## Approval Boundaries

Stop before publishing, outreach, connector writes, media spend, paid research, campaign/list/CRM mutation, global `~/.codex` changes, destructive action, or hot natural-language promotion.

## Validation

```bash
python3 execution/verify_marketing_specialist_workbench.py
python3 execution/verify_video_context_source_package.py extractions/video-context/SupWhagSCm8
python3 execution/verify_skill_system_contract.py
python3 execution/verify_behavior_changing_extraction_contract.py
python3 execution/codex_live_surface_audit.py --strict
```
