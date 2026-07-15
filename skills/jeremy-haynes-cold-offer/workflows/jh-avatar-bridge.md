---
description: Ingest existing avatar/ICP research into the umbrella narrative format — stacking workflow
---

# /jh-avatar-bridge — Avatar→Narrative Bridge

The harness already produces deep ICP work (`/avatar-machine` Phase 0 GROUND, `icp-deep-canvasser`, McRaney identity profiles, client research docs). This bridge converts any of those into the problems/circumstances/desired-outcomes grammar so offer composition can start without re-researching.

## Pre-Flight Gate

- An actual research artifact must exist (avatar doc, ICP profile, canvass output, interview notes). Nothing to bridge → `/jh-umbrella-narrative` (which gathers) instead.
- Bridge ≠ launder: if the source artifact was itself ungrounded (assumed personas), the output inherits DRAFT-UNGROUNDED status — conversion doesn't add credibility.

## Skill Acquisition

- `genius.md` — Method steps 2–3; the source avatar/ICP artifact in full

## Execution

1. **Read the source artifact completely.** Note its grounding (field-researched vs. inferred) and date.
2. **Extract to the grammar**: problems (named frustrations) / circumstances (what the problems create — often the layer avatar docs UNDER-specify; flag gaps) / desired outcomes (specific, in their language).
3. **Mine failure history**: avatar docs often bury this in "past solutions tried" — surface it as the radioactive-components register.
4. **Classify temperature**: does the source describe an in-market buyer (pursuing solutions) or needs-convinced (identity-level resistance, unaware of category)? McRaney-grade profiles usually reveal deeper resistance → often needs-convinced.
5. **Gap list**: name what the source artifact could NOT supply (usually: circumstances layer, verbatim language, purchase-blocker data) and which workflow fills each (`/jh-umbrella-narrative` gather step, `/jh-objection-mine`).
6. **Emit** the standard Umbrella Narrative Map so `/jh-offer-stack` can consume it directly.

Execution prompt: references/prompts-v2/umbrella-narrative-map.md — honor its Output Contract (provenance note added per this workflow).

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| /avatar-machine output | Phase 0 GROUND data maps nearly 1:1; mostly re-formatting + gap list |
| McRaney/identity profiles | Identity resistance enriches circumstances; keep the identity layer attached as an annex — offer framing must not collide with identity |
| Client-supplied personas | Usually ungrounded — label honestly, recommend a grounding pass |
| Deep-ICP invisible-expert profile | Direct input for Farrice's own offers; check PATH decision before strategy-shaped output |

## Output Requirements

Umbrella Narrative Map (standard format) + provenance note (source artifact, grounding status) + gap list with fill-route per gap.

## Quality Gate

- Grounding status inherited honestly
- Circumstances layer present or explicitly flagged as gap
- Failure history surfaced
- Output consumable by /jh-offer-stack without rework
