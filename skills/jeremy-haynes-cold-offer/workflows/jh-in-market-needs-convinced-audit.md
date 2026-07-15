---
description: Classify audience state (in-market vs. needs-convinced) and design migration path as audiences scale
routing: core
tier: practitioner
aliases:
  - jh-audience-state-classification
  - jh-classify-buyer-readiness
requires_prior:
  - jh-umbrella-narrative
prerequisite_for:
  - jh-offer-stack
  - jh-audience-state-messaging
---

# /jh-in-market-needs-convinced-audit — Audience State Classification

Step 3 of the 8-step spine: **CLASSIFY**. "In-market (actively, literally pursuing it and open to the idea of buying it) or needs-convinced (open to the idea of being sold... but they needed a lot more convincing)?" Haynes: "Completely different offer stacks" — same product, framed differently per state.

## Pre-Flight Gate

- **Do you know your ICP's current readiness?** If you haven't validated where they are in the buyer's journey, mark PROSPECTIVE and run field research first.
- **One audience or multiple?** If you're targeting both in-market AND needs-convinced with the same offer → STOP. Design state-specific stacks. Haynes: this is non-negotiable.
- **Funnel type needed?** Audience state "is also going to dictate the type of funnel." Hidden Knowledge: offer upstream of funnel. Classify before selecting funnel family.

## Skill Acquisition

- `genius.md` — Decision Framework (which audience state?), Hidden Knowledge (offer dictates funnel type), Lineage Crosswalk (Schwartz to Haynes mapping)
- `references/lineage-schwartz-crosswalk.md` — In-market ↔ Most Aware, Needs-convinced ↔ Problem-Aware, Mass-Market ↔ Unaware

## Execution

1. **Define in-market vs. needs-convinced** (from genius.md):
   - **In-market**: Actively, literally pursuing the solution. Already shopping. Open to buying. Example: "I'm looking for a copywriter to rewrite my sales page."
   - **Needs-convinced**: Open to the idea of being sold. Don't yet know they have a problem or that a solution exists. Must be persuaded first. Example: "I have good customers but my sales funnel is 'fine' " (doesn't know it's leaking).

2. **Evidence gathering** (from field research/umbrella narrative):
   - **In-market signals**: Actively searching, comparing competitors, asking pricing/timeline questions, using industry terminology, looking for shortcut.
   - **Needs-convinced signals**: Don't know they're shopping, don't use solution-layer language, view solution as "nice-to-have," believe they can DIY or don't need it.

3. **Map to Schwartz awareness ladder** (lineage-crosswalk.md):
   - **In-market** = Most Aware + Product-Aware (Schwartz stages 4–5)
   - **Needs-convinced** = Solution-Aware + Problem-Aware (Schwartz stages 2–3)
   - **Mass-market** = Unaware (Schwartz stage 1) — future scaling tier

4. **Classify your primary audience**:
   - Primary in-market or needs-convinced? (You will have 80/20 split; pick the revenue driver.)
   - Secondary segments? (Can be addressed with editions or separate campaigns.)

5. **Design the stack implications** (from lineage-crosswalk and genius.md):

   | Audience State | In-Market | Needs-Convinced |
   |---|---|---|
   | **Stack priority** | Differentiation + de-risking (proof, guarantees) | Education + belief installation (training, mechanism articulation) |
   | **Component profile** | 2–7 opt-ins, high conversion, immediate profitability | Education components + backend selling (sales call is where persuasion happens) |
   | **Objection profile** | "How is this different?" "Can you prove ROI?" | "How do I know this works?" "Why should I believe this is important?" |
   | **Messaging tone** | Specific, comparative, ROI-focused | Educational, foundational, belief-building |
   | **Funnel family** | Webinar, challenge, direct-response ads | Content, nurture, authority + sales call |
   | **Show rate expectation** | Higher (60%+, they're already interested) | Lower (40%–50%, must be convinced) |
   | **Expected ROAS** | 3:1 to 10:1+ at scale | 1:1 to 3:1, scaling through education layer |

6. **Migration trigger** (Step 8 preview):
   - At scale, in-market pools exhaust. What's your trigger to recompose for needs-convinced?
   - Haynes: salespeople report "more curious, less sold" → temperature has drifted.
   - Prepare the migration path now (→ `/jh-plateau-diagnostic`).

7. **Verdict document**:
   - Declared primary state (in-market or needs-convinced)
   - Evidence (3–5 data points from field research)
   - Mapped Schwartz stage
   - Stack-design implications (component types, funnel family, expected metrics)
   - Secondary segments (if any) and their state
   - Migration trigger conditions

Execution prompt: references/prompts-v2/audience-state-classification.md — honor its Output Contract.

## Content-Type Adaptations

| Scenario | Classification Lens |
|---|---|
| **B2B SaaS** | Operator in-market (shopping for tools) vs. stakeholder needs-convinced (didn't know they needed this) |
| **High-ticket services** | Founder in-market (knows they need help) vs. team needs-convinced (doesn't see the gap) |
| **Local / real estate** | Seller in-market (listing property) vs. buyer needs-convinced (didn't know this strategy existed) |
| **Pivot: scaling from in-market to needs-convinced** | Re-document as "Phase 2: Needs-Convinced Recomposition" not "new offer" |

## Output Requirements

**Audience State Classification Document**:
- Primary audience state declaration (in-market or needs-convinced)
- Evidence inventory (data from field research supporting the classification)
- Mapped Schwartz awareness stage(s)
- Stack-design implications table (from execution step 5)
- Metrics expectations (show rate, ROAS floor, segment size)
- Secondary audiences (if any) and their state
- Migration trigger conditions (when to recompose for colder audiences)

## Quality Gate

- [ ] State is declared, not ambiguous ("mixed" = re-classify; pick primary revenue driver)
- [ ] Evidence ties back to umbrella narrative / field research
- [ ] Schwartz mapping complete (helps downstream with messaging)
- [ ] Stack implications understood (team knows this dictates funnel choice)
- [ ] Migration trigger is specific, not vague ("when leads are colder" is vague; "when show rate drops below X%" is specific)

