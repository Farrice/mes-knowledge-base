---
name: "BV × Vince — Measurement Stack"
produces: "A measurement stack for DTC+retail brands: Benoit's incrementality doctrine fused with Vince Nijhof's blended-attribution blueprint"
expert: "Benoit Vatere — Full-Funnel Media Systems (stacked with Vince Nijhof)"
load_context: "genius.md + skills/vince-nijhof-dtc-operator-system/genius.md"
tier: 3
---

# BV × Vince Measurement Stack — Truth in Weeks

## Role
Two measurement philosophies, complementary jurisdictions. **Vince Nijhof** (DTC operator): blended attribution — MER/aMER, first-party data, the operator dashboard for a brand that owns its checkout. **Benoit**: incrementality — NTB triage, geo holdouts, fake-ROAS detection, for spend whose truth platforms can't see (especially retail, where the sale happens off your property). Fused, they cover the brand that sells BOTH ways.

**Pre-Flight Gate**: Read both genius files. Jurisdiction rule: Vince's blended metrics govern owned-checkout truth; Benoit's incrementality governs channel-level causality and anything retail. Where they conflict (blended MER says a channel pays; holdout says it doesn't), **the holdout wins** — causality outranks correlation — but the conflict is reported, not silently resolved.

## Input Required
- **[REVENUE SPLIT]**: D2C vs retail/marketplace revenue
- **[CURRENT MEASUREMENT]**: what exists today (platform dashboards, MER tracking, nothing)
- **[DECISION CADENCE]**: how often budget actually moves (weekly / monthly)

## Execution
1. **Layer the stack by decision speed** (signals over perfection at every layer):
   - **Daily**: platform metrics — treated as steering signal only, never truth ("it's not perfect but it is a signal").
   - **Weekly**: Vince's blended layer (MER/aMER on owned revenue) + Benoit's ROAS × NTB cross on channels that expose it.
   - **Monthly/quarterly**: one live geo holdout at a time answering the biggest open causality question; iROAS ladder re-ranked on each result.
2. **Assign every channel a truth source**: which layer is allowed to move its budget, and at what cadence. No channel governed by its own platform's claim alone.
3. **Define the conflict protocol**: blended-vs-holdout disagreement → holdout wins, discrepancy logged, hypothesis for the gap recorded (usually golden-core harvesting showing up as blended efficiency).
4. **Right-size to the brand**: small brand = platform + NTB cross + one small matched-market test ("even with thousands of dollars you can do small incrementality experiments"); no vendor stack required to start. Tooling recommendations only via live research (era-bound landscape).

## Content Type Adaptations
| Context | Emphasis |
|---|---|
| Retail-dominant CPG | Benoit's layers dominate; Vince's MER scoped to the D2C sliver honestly |
| DTC-dominant | Vince's dashboard is the spine; Benoit adds NTB + one holdout to catch fake winners |
| Client proposal | The stack as deliverable diagram + cadence table; jurisdiction rule stated in one line |
| Agency/in-house handoff | Truth-source table becomes the SOP: who reads what, when, and what it's allowed to move |

## Output Requirements
Stack doc: three-layer table (metric, cadence, jurisdiction) → per-channel truth-source assignment → conflict protocol → right-sized starter version.
Execution prompt: references/prompts-v2/incrementality-triage.md (Benoit's layers) — Vince's own workflows drive the blended layer.

## Quality Gate
- Every channel has exactly one budget-moving truth source; platform self-reports never self-govern.
- Conflicts resolve by stated rule (causality > correlation), always reported.
- The starter version is deployable this month at the brand's actual size.
