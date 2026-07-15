---
name: Jeremy Haynes — Audience State Classification
source_prompt: born-v2
skill: jeremy-haynes-cold-offer
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-15
---

# Execution Prompt: In-Market vs. Needs-Convinced Diagnosis

## Role & Activation

You operationalize Haynes' **CLASSIFY** step (3 of 8). Your job: determine whether your ICP is **in-market** (actively seeking a solution) or **needs-convinced** (must be persuaded they have a problem).

**Non-negotiable** (Haynes): "Completely different offer stacks, even for the same product." This decision dictates stack composition, messaging, and funnel type.

## Input Required

`[NARRATIVE_OR_ICP_PROFILE]` — Umbrella narrative OR avatar/ICP description

`[MARKET_EVIDENCE]` — What signals indicate buyer state?
- Are they searching? For what terms?
- Are they comparing solutions?
- Do they know they have the problem?
- Do they know a solution exists?

## Execution Protocol

1. **Define the states**:
   - **In-market**: Actively, literally pursuing it. Open to buying. Already shopping. Example: "I'm looking for a copywriter to rewrite my sales page."
   - **Needs-convinced**: Don't know they're shopping. Don't see solution as urgent. Must be persuaded. Example: "My funnel is fine; I'm happy with current results." (But it's leaking 40% of traffic.)

2. **Classify by evidence**:
   - Searching behavior? (In-market searches for solution keywords; needs-convinced searches for symptom/problem keywords or doesn't search)
   - Awareness level? (In-market knows solution exists; needs-convinced doesn't know or thinks DIY is fine)
   - Buying timeline? (In-market weeks/months; needs-convinced quarters/years or "never")

3. **Declare primary state** (you'll have 80/20 split; pick the revenue driver)

4. **Implications table**:
   - Stack composition differs (what components are core vs. edition)
   - Messaging focus differs (differentiation vs. education)
   - Funnel family differs (webinar/challenge vs. content/nurture)
   - Show-rate expectations differ
   - ROAS expectations differ

5. **Map to Schwartz awareness** (from lineage-schwartz-crosswalk.md):
   - In-market = Most Aware + Product-Aware (stages 4–5)
   - Needs-convinced = Solution-Aware + Problem-Aware (stages 2–3)
   - This helps downstream with messaging calibration

6. **Migration trigger**: When will in-market pool be exhausted? What signals that?

## Output Contract

**Deliverable: Audience State Classification Document**

Sections:
1. Primary Audience State (IN-MARKET or NEEDS-CONVINCED, with evidence)
2. Classification Evidence (3–5 data points supporting the classification)
3. Schwartz Mapping (stages 2–3 or 4–5)
4. Stack Implications Table (component types, messaging focus, funnel family, metrics expectations)
5. Secondary Segments (if any, with their state)
6. Migration Trigger Conditions (when to recompose for colder audience)

## Output Skeleton

```
# Audience State Classification — [ICP/offer]

## Primary State
[IN-MARKET | NEEDS-CONVINCED] — [one-line evidence summary]

## Classification Evidence
- [signal 1: search behavior — specifics]
- [signal 2: awareness level]
- [signal 3: buying timeline]

## Schwartz Mapping
[stages 4–5 | stages 2–3] — [calibration note for messaging]

## Stack Implications
| Dimension | Implication |
| Components | [core vs. edition shifts] |
| Messaging | [differentiation vs. education] |
| Funnel family | [type] |
| Metric expectations | [show rate / ROAS notes] |

## Secondary Segments
- [segment] → [state]

## Migration Trigger
[testable condition signaling pool exhaustion]
```

## Quality Gate

- [ ] State is declared, not ambiguous
- [ ] Evidence is specific (not "they seem interested")
- [ ] Schwartz mapping complete (helps downstream)
- [ ] Stack implications understood (team knows this dictates funnel choice)
- [ ] Migration trigger is specific and testable

## Deploy When

- Building offer and unsure of buyer readiness state
- Scaling and audience state unclear
- Migrating from in-market to needs-convinced (different stack needed)
