# Source Coverage — Oren Archetype Social Strategy

## Source Packages

| Video | Role In Build | Local Package | Evidence Notes |
|---|---|---|---|
| Once You Master Brand Archetypes, You Master Social Media | Primary spine: five social archetypes and resource-fit workshop | `extractions/video-context/tcqf6sgw_Ho/` | Full ledger with spoken, visual frame, and uncertainty rows; OCR unavailable |
| What ACTUALLY Makes People Buy Things | Pricing, product mix, personas, persona-to-copy layer | `extractions/video-context/l3inbx2jeZU/` | Transcript ledger; frames/OCR skipped by design |
| How to build a marketing team in 2026 | Content-first org, pod structure, media flywheel, anchors | `extractions/video-context/IdmtqdoZTBA/` | Transcript ledger; overlaps with existing content-team package |
| How to Make a Marketing Plan | Funnel audit, initiative map, calendar matrix, campaigns | `extractions/video-context/1YVi3iFk3V0/` | Transcript ledger; new planning workflow layer |
| How to Be a 1-Person Marketing Machine in 2026 | Solo AI marketing operator cadence, referral gate, monthly message loop, AI copy machine, 40-hour execution calendar | `extractions/video-context/DWDFRi5ONMI/` | Full ledger with spoken rows, 10 sampled frames, and OCR unavailable |
| I've made 1067 short form videos | Short-form monetization, personality, niche, offers, traps | `extractions/video-context/8gvCc5jvcH0/` | Transcript ledger; source claims kept as creator claims |
| 11 ways to get your life together | Creative systems, trackers, updates, process docs, pillar measurement | `extractions/video-context/QHPmOgnc96E/` | Transcript ledger; overlaps with existing operational-systems package |

## Duplicate And Overlap Decisions

- Existing `oren-content-team-architecture` already owns pods, media-company flywheels, anchors, creator networks, and team cadence. This build links to it rather than recreating those workflows, while repairing its missing references and stale workflow entries.
- The one-person AI marketing source is an enrichment to the existing planning and content-team layers. It adds a solo operator bridge, not a contradiction of Oren's pod architecture.
- Existing `oren-operational-systems` already owns reference repositories, idea calendars, weekly updates, team trackers, process docs, and content pillar measurement. This build uses the systems layer as a stack after archetype selection, not as a duplicate systems skill.
- Existing `oren-luxury-psychology` already owns premium triggers and connoisseurship ladders. This build uses pricing/product-mix mechanics for social and offer alignment, then points premium cases back to that skill.
- Existing `/archetype-build` remains a generic Luke Iha audience typing factory. The Oren archetype workflows are specifically for brand social roles and content behavior.

## Evidence Limits

- Full visual claims are only available for the archetype video via sampled frames. OCR did not run because the OCR stack was unavailable.
- The five support videos were intentionally acquired as transcript-first packages. Their visual examples should not be treated as observed visual evidence unless a future run upgrades them to full ledgers.
- Metrics and brand performance examples are source claims unless independently verified in a separate research workflow.
