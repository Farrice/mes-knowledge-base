# Rachel Woods - AI Playbook Methodology

## Core Thesis

A playbook is not a prompt. It is a reusable operating document that captures how work should be done, what decisions must be made, what good looks like, where AI can help, and how misses get turned into better instructions. The asset is the documented process; the tool is rented.

## Research Basis

- Rachel's CRAFT Cycle frames process automation as Clear Picture, Realistic Design, AI-ify, Feedback, and Team Rollout.
- The public AMP playbooking material frames playbooking as the bridge between casual AI use and reliable, repeatable value.
- The AI Exchange playbooking mistakes identify three failure modes: starting with tech instead of work, treating work as a black box, and under-specifying what good means.

## The Playbook OS Sequence

### 1. Spot the Right Opportunity

Start with work, not tools. Index processes before asking what AI can do.

Strong candidates have:
- Clear ROI: time saved, revenue enabled, quality improved, or a capability unlocked.
- Repeatability: the process happens often enough to repay documentation effort.
- Mastery: the user or team already knows what good looks like.
- Safe scope: the first version can be narrow, low risk, and useful.
- Downstream leverage: a better output reduces handoff friction or unlocks delegation.

Weak candidates:
- Rare, one-off work.
- Ambiguous work the human team has not stabilized.
- High-risk client-facing work with no review layer.
- Work where nobody can explain the current method.
- Tool-led ideas with no operational pain.

### 2. Decompose the Black Box

Most valuable work looks intuitive because the expert has compressed steps into instinct. Playbooking expands that instinct back into teachable units.

Break the process into:
- Research: what is gathered, where it comes from, what signals matter.
- Analysis: how inputs are interpreted.
- Judgment: where taste, context, or business risk enters.
- Execution: what artifact gets produced.
- Review: how quality is checked.
- Handoff: who uses the output next and what they need.

For each unit, ask:
- What is the first action?
- How is that action done?
- What tips, shortcuts, or filters are used?
- What decision or artifact must exist before moving on?
- What gets rejected?

### 3. Define Good At Every Step

AI does not fail only because it lacks capability. It often fails because the work is underspecified.

For every step, define:
- Success criteria.
- Assumptions that must be stated.
- Taste/context rules.
- Examples and anti-examples.
- Minimum acceptable quality.
- Review owner and escalation rule.

Client-facing playbooks need stricter standards:
- Brand voice and relationship context.
- Risk, privacy, and promise boundaries.
- Human approval before sending.
- Clear source traceability for claims.
- Failure handling that protects trust.

### 4. Run The CRAFT Scope

Use CRAFT to turn the process into a playable system.

| Stage | Output |
|-------|--------|
| Clear Picture | Current process map, roles, inputs, outputs, pain, success criteria. |
| Realistic Design | Minimum useful slice, risk level, review design, delegation boundary. |
| AI-ify | Playbook instructions, prompts, tools, knowledge sources, tool placement. |
| Feedback | Test cases, issue log, repair instructions, known limitations. |
| Team Rollout | Owner, users, training, metrics, maintenance cadence. |

The first version should be tiny but useful. Build one clear slice that works, then expand.

### 5. Build The Playbook

A complete AI-ready playbook includes:
- Name and promise.
- Trigger and use cases.
- Inputs and sources.
- Step-by-step runner.
- Decision rules.
- Quality standards.
- Examples and anti-examples.
- Delegation map.
- Tool placement.
- Output contract.
- Feedback and maintenance log.

### 6. Test, Break, Repair

Testing is not optional. A playbook is not done when written; it is done when it survives use.

Run tests for:
- Normal case.
- Missing-input case.
- Ambiguous-context case.
- Edge case.
- Client-risk case if relevant.

For every miss, decide:
- Was the issue clear?
- Is the fix actionable?
- Is the fix necessary?
- Should the instruction, example, quality standard, or scope change?

### 7. Deploy And Maintain

Choose the lightest useful run environment:
- Document + copy/paste prompts for early testing.
- Custom GPT or Claude project for repeated personal use.
- Automation tool when triggers and handoffs are stable.
- Agent or code workflow only after steps are well-defined.

Assign an owner, usage metric, quality metric, and review cadence. Revisit failed or limited playbooks as models and tools improve.
