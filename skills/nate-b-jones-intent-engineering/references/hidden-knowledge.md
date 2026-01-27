# Nate B Jones - Hidden Knowledge

## Tacit 1: Answer-Shaped Text Problem
LLMs produce outputs that LOOK correct because they match the statistical pattern of correct answers. In chat, forgiving. In agent actions, catastrophic.

**Deploy**: Treat every agent output as potentially "answer-shaped but wrong" until validated against intent criteria.

---

## Tacit 2: Human Second-Pass Simulation
Humans automatically simulate consequences and social context before inferring priorities. Models skip this unless forced.

**Deploy**: Build explicit "consequence simulation" steps: What could go wrong? What would the user regret?

---

## Tacit 3: Social Cohesion Trap
Human language optimizes for relationship maintenance, not declarative specification. We're deliberately vague. Models take vagueness literally.

**Deploy**: Transform polite requests into explicit specifications before agent processing.

---

## Tacit 4: Reversibility Gradient
Actions exist on spectrum from fully reversible to completely irreversible. Different points require different confidence levels.

**Deploy**: Map every tool to reversibility score. Require higher intent confidence for lower reversibility.
