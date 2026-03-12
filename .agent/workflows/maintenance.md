# Maintenance — Weekly Intelligence Check

> **Invocation**: `/maintenance` | `@maintenance` | "run maintenance"
> **Purpose**: System self-assessment, skill evolution checks, agent health, research pulse. The system stays sharp without Farrice carrying the cognitive load.
> **When**: Once a week, or whenever you want the system to check itself and report back.

---

## How It Works

This is the "parallel agency" workflow. Fire it, and the system runs its own diagnostics — checking if skills need evolving, agents need updating, patterns need propagating, and gaps need filling.

---

## Phase 1: Performance Data Check (2 min)

```bash
cd execution && python log_performance.py baseline
```

Report:
- Total entries in Performance Log
- Average quality score (rolling 10)
- Average sub-scores (Intent, Expert, Adversarial)
- Keep rate
- Any regressions detected
- **Phase 2 activation status**: Need 20+ entries for Skill Evolution Engine

---

## Phase 2: Skill Evolution Check (if 20+ entries exist)

Run `execution/skill_benchmark.py` against the top 5 most-used skills:
1. `lara-acosta-linkedin-content`
2. `kallaway-content-psychology`
3. `nicolas-cole-digital-writing`
4. `cardinal-mason-ai-copywriting`
5. `shaan-puri-storytelling`

For each skill:
- Pull rolling quality baseline
- Check for regression (>1.0 below rolling average)
- Check for improvement (>1.0 above rolling average)
- If regression detected: flag for review, suggest workflow variant
- If improvement detected: check if pattern is transferable (Phase 3)

---

## Phase 3: Cross-Pollination Scan

Run `execution/pattern_propagation.py` to check for transferable improvements:

9 pattern families to scan:
1. Persuasion patterns
2. Hook patterns
3. Structure patterns
4. Voice patterns
5. Research patterns
6. Conversion patterns
7. Storytelling patterns
8. Positioning patterns
9. Systems patterns

Report any improvements in one skill that could benefit related skills.

---

## Phase 4: Gap Analysis

Run `execution/gap_analysis.py` to identify coverage gaps:

- Check Performance Log for task types with low scores
- Check for domains with no recent entries
- Check expertise gap logs for systematic weaknesses
- Report top 3 gaps with recommended actions

---

## Phase 5: Agent Health Check

For the top 5 actively-used agents, verify:
1. AGENT.md exists and is current
2. SKILL.md + genius.md + workflows are complete
3. No broken references in SKILL_INDEX or AGENT_INDEX
4. Memory directory has recent context

Flag any agents that need attention.

---

## Phase 6: Research Pulse (Optional — Budget-Gated)

If Perplexity budget allows (check `.agent/perplexity-usage.json`):
- Quick scan for major developments in: AI agents, ghostwriting, LinkedIn content, solopreneur tools
- Report anything relevant to Farrice's positioning or skill set
- Suggest extractions or skill updates if warranted

If NotebookLM budget allows (check `.agent/notebooklm-usage.json`):
- Query relevant notebooks for cross-reference with recent work

---

## Phase 7: Summary Report

Deliver a concise report:

```
## Maintenance Report — [Date]

### Performance Data
- Total entries: X (need 20+ for Phase 2 activation)
- Rolling quality: X.X/10
- Sub-scores: Intent X.X | Expert X.X | Adversarial X.X
- Keep rate: X%

### Skill Evolution
- [Status: Active/Waiting for data]
- Regressions: [none | list]
- Improvements: [none | list]

### Cross-Pollination
- [Transferable patterns found | none]

### Gap Analysis
- Top gaps: [list or "no significant gaps"]

### Agent Health
- [All healthy | issues found]

### Research
- [Key findings | skipped due to budget]

### Recommended Actions
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

---

## Auto-Log

Log the maintenance session itself:

```bash
python execution/log_performance.py log "Weekly maintenance check" \
    --skill system \
    --type System \
    --quality [1-10] \
    --intent 10 \
    --expert [1-10 based on thoroughness] \
    --adversarial 10 \
    --status Keep \
    --notes "[Summary of findings and actions taken]"
```
