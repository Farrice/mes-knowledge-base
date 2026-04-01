---
description: Audit any hand-coded heuristic, prompt trick, or manual pattern for evolution replacement potential — the Bitter Lesson applied to Antigravity
---

# Bitter Lesson Check

> Load `skills/self-evolving-systems/genius.md` first (GP-8 specifically).

## When to Use
- Periodic audit of manually-tuned system components
- Before spending significant time hand-tuning a prompt or workflow
- When a component feels "over-engineered" with manual heuristics
- System-wide sweep for evolution candidates

## Input Required
- **Target(s)**: Specific component to audit, OR "all" for full system sweep
- **Scope**: Deep audit (single component) or sweep (all components, surface-level)

## Execution

### For Each Component — Score on the Bitter Lesson Scale

| Dimension | Score 1-10 | Question |
|-----------|-----------|----------|
| **Hand-coding density** | _/10 | How much of this component's behavior is manually specified vs. emergent? |
| **Heuristic fragility** | _/10 | How much would it break if inputs changed slightly? |
| **Evolution potential** | _/10 | Could an automated proposer discover a better version? |
| **Value at stake** | _/10 | How much does this component's quality affect final output? |
| **Iteration investment** | _/10 | How much time has been spent manually tuning this? |

**Bitter Lesson Score** = (Hand-coding + Fragility + Evolution potential + Value + Iteration investment) / 5

### Interpretation

| Score | Verdict | Action |
|-------|---------|--------|
| 8-10 | 🔴 **Prime evolution candidate** | Run `/self-evolve` or `/proposer-sprint` immediately |
| 5-7 | 🟡 **Monitor** | Schedule for evolution in next sprint |
| 1-4 | 🟢 **Low priority** | Component is simple enough that hand-coding is fine |

### System Sweep Mode
When target is "all":
1. List all workflows in `.agent/workflows/`
2. List all skills in `skills/`
3. List all directives in `directives/`
4. Score each on the 5 dimensions above (quick 1-line assessment per component)
5. Rank by Bitter Lesson Score
6. Present top 5 evolution candidates

## Output
1. **Scorecards** — per-component Bitter Lesson scores
2. **Evolution priority queue** — ranked list of what to evolve next
3. **Quick wins** — components where a 5-iteration sprint would likely produce gains
4. **Leave alone** — components where hand-coding is appropriate (simple, stable, low-value)

---

## The Bitter Lesson (Reference)

> "The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin." — Rich Sutton, 2019

Applied to harnesses: Hand-tuned prompts, manually designed workflows, and human-curated retrieval logic will be outperformed by evolved versions. The question is when — not if.
