---
description: Universal Oren front door for taste, luxury, repositioning, identity, social archetypes, content teams, operations, AI marketing, funnel flywheels, ad psychology, brand worlds, and slop-era creative strategy
---

# /oren — Universal Oren Conductor

Use this front door when the user asks for Oren, asks to use all relevant Oren expertise, or describes an Oren-shaped marketing, brand, creative, content, or funnel problem without naming the exact package.

## Dispatch Contract

1. Read `agents/oren-taste-development/references/universal-route-map.json`.
2. Classify the **purchased job**, not merely the vocabulary in the request.
3. Check `external_handoffs` before selecting an Oren package. If a specialist owns the requested work, hand off; do not keep it inside Oren for name continuity.
4. Select exactly **one primary Oren skill**. A second Oren skill is allowed only as bounded support when it changes a named decision or quality gate.
5. Load the selected skill's `SKILL.md` and `genius.md`, then the single best-fit workflow or execution prompt. **Never bulk-load all Oren skills.**
6. Show a compact Oren Route Card, then execute immediately unless a genuine user decision changes the route.

## Oren Route Card

```markdown
Oren Route Card
- Purchased job: [what progress the user is buying]
- Primary owner: [one Oren skill]
- Workflow: [exact command or path]
- Bounded support: [none, or one skill plus the decision it changes]
- Evidence state: [verified / source-grounded practitioner claim / assumption / untested]
- Outside-owner handoff: [none, or exact owner and boundary]
```

## Tie-Breakers

- **Taste vs slop-era:** critique a specific object with `oren-taste-development`; diagnose systemic sameness or train marketer judgment with `oren-slop-era-creative-strategy`.
- **Identity vs archetype:** establish who the buyer/founder becomes with `oren-identity-brand-os`; decide what the brand repeatedly does on social with `oren-brand-archetypes`.
- **Luxury vs repositioning vs world-building:** buyer codes and premium progression belong to `oren-luxury-psychology`; market-meaning change belongs to `oren-repositioning`; lore, roles, props, and institutions belong to `oren-norton-world-building`.
- **Operations vs content-team:** trackers, repositories, updates, calendars, and SOPs belong to `oren-operational-systems`; staffing, pods, cadence, and media-company structure belong to `oren-content-team-architecture`.
- **AI marketer vs funnel specialist:** both live in `oren-one-person-ai-marketer`; `/oren-one` selects the workflow. Complete acquisition-to-retention design must route to `/oren-funnel-flywheel`.
- **Ad psychology vs paid economics:** creative psychology belongs to `oren-dara-ad-psychology`; ROAS, CAC, attribution, and media-buying diagnosis belong to Benoit Vatere.

## Truth And Permission Gates

- Label Oren's earnings, list-size, price, and performance statements as practitioner claims unless independently verified.
- Do not infer profitability when CAC, conversion, fulfillment cost, repeat purchase, or LTV is missing; return the missing measurement requirements.
- Draft DM and email sequences only. Do not send, publish, edit profiles, launch ads, create pages, collect payments, or mutate CRM records without explicit approval.
- Treat Framer as an optional sponsored example, never a dependency.
- Preserve specialist ownership: Oren may architect the system, but full VSL copy, detailed lead-magnet construction, paid-media economics, and post-purchase referral implementation stay with their established owners.

## Completion Gate

Before delivery, verify that the response names one primary owner, no more than one bounded Oren support package, an exact workflow, the evidence/economics state, and any outside-owner handoff. If the user asked for "all Oren expertise," return a routed composition—not an expert dump.
