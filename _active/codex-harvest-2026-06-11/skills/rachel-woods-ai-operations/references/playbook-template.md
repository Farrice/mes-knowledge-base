# Rachel Woods - AI Playbook Template

Use this schema for any personal, client-facing, team, or automation playbook.

## 1. Playbook Header

| Field | Specification |
|-------|---------------|
| Playbook Name | Clear process name. |
| Playbook Promise | What becomes faster, clearer, or more reliable. |
| Owner | Who maintains the playbook. |
| Users | Who runs it. |
| Run Environment | ChatGPT, Claude, Copilot, automation tool, agent, SOP, or other. |
| Review Cadence | When it gets improved. |

## 2. Trigger And Scope

- **Use When**: Conditions that trigger the playbook.
- **Do Not Use When**: Cases outside scope.
- **Start Point**: What must exist before running.
- **End Point**: What finished means.
- **Minimum Useful Slice**: The narrowest version that still creates value.

## 3. Inputs

| Input | Required? | Source | Quality Requirement | Fallback |
|-------|-----------|--------|---------------------|----------|
| Input name | Yes/No | System/person/doc | What good input looks like | What to do if missing |

## 4. Step Runner

For each step:

| Step | Purpose | Instructions | Output | Quality Bar | Review Gate |
|------|---------|--------------|--------|-------------|-------------|
| 1 | Why this step exists | Exactly what AI does | Artifact/decision produced | What good means | Human/AI/none |

Rules:
- Announce the step before running it.
- Do not skip intake.
- Do not produce the final deliverable until the brief is confirmed.
- Flag assumptions.
- Stop at review gates.
- Offer delegated next actions after the main output.

## 5. Decision Rules

Document the hidden logic:
- If X, do Y.
- If confidence is below threshold, ask.
- If client risk is present, escalate.
- If data is stale, flag it.
- If examples conflict, prioritize the newest approved example.

## 6. Quality Standards

| Criterion | Pass | Strong | Unacceptable |
|-----------|------|--------|--------------|
| Specificity | Uses real context | Names concrete causes/actions | Generic or reusable anywhere |
| Accuracy | Source-backed | Flags uncertainty | Invents unsupported claims |
| Usefulness | User can act | Reduces next-step friction | Requires major rework |

## 7. Examples

- **Strong Example**: A finished output or step output that meets the standard.
- **Why It Works**: The exact qualities to repeat.
- **Weak Example**: A mediocre output.
- **Why It Fails**: The rule it violates.

## 8. Delegation Map

| Task | Objective / Good Enough / Expert | AI Role | Human Role | Escalation |
|------|----------------------------------|---------|------------|------------|
| Task | Category | Execute/draft/research/review | Approve/refine/decide | When to stop |

## 9. Tool Placement

| Tool Layer | Use When | Notes |
|------------|----------|-------|
| Prompt-only | Early test or manual process | Lowest setup, highest manual handoff. |
| Custom GPT / Claude project | Repeated process with stable instructions | Store playbook and examples. |
| Automation | Stable trigger and repeatable inputs | Connect prompts step by step. |
| Agent / code workflow | Multi-step execution with tool use | Delegate one clear step per agent where possible. |

## 10. Output Contract

Define:
- Final deliverable format.
- Required sections.
- File or destination.
- Handoff recipient.
- What the recipient should be able to do next.

## 11. Feedback Log

| Date | Run Context | Issue | Clear? | Actionable? | Necessary? | Patch | Status |
|------|-------------|-------|--------|-------------|------------|-------|--------|
| YYYY-MM-DD | What was run | What failed | Yes/No | Yes/No | Yes/No | Instruction/example/scope change | Open/Fixed |

## 12. Maintenance Rules

- Patch the playbook, not only the current output.
- Keep known limitations visible.
- Remove stale examples.
- Re-test after major tool/model changes.
- Revisit failed use cases every six months.
