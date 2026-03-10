---
description: Generate a monthly intelligence gap report — identify weak skills, missing coverage, and knowledge investment priorities
---

# /gap-report — Intelligence Gap Analysis Workflow

Analyze accumulated performance data to identify systematic gaps in knowledge coverage and generate a prioritized investment plan.

## Usage

```
/gap-report
/gap-report --skill <skill-name>
/gap-report --domain <domain-name>
```

## Steps

### 1. Pull System State

Run the gap analysis engine:

```bash
python execution/gap_analysis.py analyze
```

This produces:
- System health metrics (total skills, active vs unused, performance entries)
- Low-performing skills (avg < 6/10)
- Weak task types
- Recurring knowledge gaps (from gap log)
- Task type coverage map
- Prioritized recommendations

### 2. Cross-Reference with Gap Log

Read `.agent/gap-log.md` for recurring patterns:
- Domains that appear 3+ times → proactive extraction needed
- Severity escalation patterns → important domains getting worse
- Unresolved gaps → still using training data for these domains

### 3. Cross-Reference with Domain Registry

Read `DOMAIN_REGISTRY.md` and compare against active skill usage:
- Domains with agents but low Performance Log activity → underutilized expertise
- Domains with high activity but low quality → skills need evolution
- Missing domains (not in registry, but appearing in gap log) → new domain needed

### 4. Generate the Report

Present a structured gap report:

```markdown
## Intelligence Gap Report — [Date]

### System Health
[Table from gap_analysis.py]

### Critical Gaps (Action Required)
[Prioritized list of gaps that need immediate attention]

### Evolution Candidates
[Skills with declining trends or plateau that should go through /skill-evolution]

### Extraction Opportunities
[Domains that repeatedly appear in gap log — extraction would permanently close the gap]

### Cross-Pollination Opportunities
[High-performing skills whose patterns could transfer to related weak skills]

### Dead Weight Audit
[Skills with 0 usage — candidates for archiving or testing]

### Recommended Actions (Prioritized)
1. [Highest impact action]
2. [Second highest]
3. [Third]
...
```

### 5. CHECKPOINT: User Review

Present the report. Ask:
- Which gaps should we prioritize closing?
- Any skills to archive?
- Should we trigger `/skill-evolution` on any candidates?
- Any domains to proactively extract for?

### 6. Execute Approved Actions

Based on user decisions:

| Action | How |
|--------|-----|
| Close a knowledge gap | `/extract <source>` for the missing domain |
| Evolve a weak skill | `/skill-evolution <skill-name>` |
| Cross-pollinate | Run `python execution/pattern_propagation.py report` |
| Archive dead skills | Move to `skills/_archived/` |
| Add missing domain | Update `DOMAIN_REGISTRY.md` after extraction |

### 7. Log the Report

```python
from execution.log_performance import log_output

log_output(
    output=f"Gap Report — {date} ({num_recommendations} recommendations)",
    workflow="gap-report",
    task_type="System",
    quality_score=None,  # Gap reports aren't scored
    status="Keep",
    notes=f"Gaps: {critical_count} critical, {evolution_count} evolution candidates, {dead_count} dead skills",
)
```

## Protocol Reference

Full protocol: `directives/expertise-gap-protocol.md` (handles real-time gap detection)
Gap analysis engine: `execution/gap_analysis.py` (handles periodic analysis)
Performance data: `execution/log_performance.py`
Cross-pollination: `execution/pattern_propagation.py`

## Scheduling

Run this workflow:
- **Monthly** (first of each month) — comprehensive review
- **After 50 new Performance Log entries** — enough new data for meaningful analysis
- **On demand** — whenever you want to assess system health
