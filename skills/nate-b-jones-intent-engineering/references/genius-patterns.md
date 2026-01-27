# Nate B Jones - Genius Patterns

## Pattern 1: Inflection Point Recognition
**Execute**: Identify the precise moment where stakes fundamentally change. "Once you give the model tools, the fluent completion becomes a real-world commitment."

**Success Metric**: Zero surprise consequences from agent actions.

---

## Pattern 2: Latent vs Explicit Distinction
**Execute**: Separate what's IN the text (context) from what's BEHIND the text (intent). Articulate priorities, tradeoffs, what done looks like.

**Success Metric**: Agent can articulate understood priorities before acting.

---

## Pattern 3: Invisible Guardrails Insight
**Execute**: Enumerate constraints humans assume but never state. "We hear 'clean up the docs' and infer 'don't destroy anything important.'"

**Success Metric**: Agent respects constraints that were never explicitly stated.

---

## Pattern 4: Clarification Loop Architecture
**Execute**: Build disambiguation as a design feature. Trigger: (1) high uncertainty, (2) serious consequences, (3) multiple plausible interpretations.

**Success Metric**: Agent asks questions at appropriate moments—not too many, not too few.

---

## Pattern 5: Intent Commit Pattern
**Execute**: Create standalone Intent Documents with goals, failure conditions, tradeoffs. Version separately from prompts.

**Success Metric**: Intent can be updated without touching execution code.

---

## Pattern 6: Production Pragmatism
**Execute**: Build harnesses that compensate for weak intent inference—eval suites, constrained permissions, traced execution.

**Success Metric**: Agents ship and perform reliably despite imperfect understanding.

---

## Pattern 7: Interpretation-Execution Separation
**Execute**: Two-phase systems: (1) Interpretation outputs explicit understanding, (2) Execution only after validation.

**Success Metric**: Every tool call has inspectable interpretation that preceded it.

---

## Pattern 8: Assumption Surfacing
**Execute**: Include in agent instructions: "Before executing, state your assumptions. Where is confidence low? What would you ask?"

**Success Metric**: Model reveals assumptions that would otherwise cause failures.
