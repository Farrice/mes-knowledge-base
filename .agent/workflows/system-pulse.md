---
description: Weekly operational intelligence dashboard — protocol health, quality trends, and expert performance
---

# System Pulse — Operational Intelligence

> Run weekly (or any time) to get a clear picture of system health.
> Invoke via: `/system-pulse`, `@system-pulse`, or "run system-pulse"

---

## Step 1: Protocol Health Audit

Run the protocol tracker to show which protocols are alive vs. zombie:

```bash
python3 execution/protocol_tracker.py audit
```

**Review the output.** Flag any critical protocols showing as zombies:
- `quality_gate.md` — Must be active if expert output is being produced
- `feedback-ratchet.md` — Must be active for learning to compound
- `session-state-protocol.md` — Must be active for context persistence
- `intent-pipeline.md` — Must be active for every deliverable request

If critical protocols are zombies, note them for the report.

---

## Step 2: Performance Baseline

Pull the rolling quality baseline from the Performance Log:

```bash
python3 execution/log_performance.py baseline
```

**Note the overall averages.** Also pull skill-specific baselines for the most-used skills:

```bash
python3 execution/log_performance.py baseline --skill lara-acosta-linkedin-ghostwriting
python3 execution/log_performance.py baseline --skill cardinal-mason-ai-copywriting
```

---

## Step 3: System Health Check

Run the system health script:

```bash
python3 execution/system_health.py
```

---

## Step 3.5: Autoresearch Loop Intelligence

Run the evolution readiness and gap analysis to feed into the pulse report:

```bash
# Skill evolution candidates (skills with enough data + declining or weak dimensions)
python3 execution/gap_analysis.py recommendations 2>/dev/null || echo "No gap data yet"

# Check for cross-pollination candidates from recent evolutions
python3 execution/pattern_propagation.py scan 2>/dev/null || echo "No evolution logs found"

# Gap log summary
echo "=== Gap Log Status ==="
wc -l .agent/gap-log.md 2>/dev/null || echo "Gap log: not initialized"
grep -c "^## " .agent/gap-log.md 2>/dev/null || echo "0 gap entries"
```

**Compile the autoresearch findings:**

| Metric | Value |
|--------|-------|
| Skills due for evolution (5+ entries since last cycle) | [count] |
| Cross-pollination candidates pending | [count] |
| Gap log entries (total / recurring) | [N] / [N] |
| Phase 4 status | [Locked / Ready / Active] |

---

## Step 4: Compile Report

Using the data from Steps 1-3, produce a concise System Pulse Report with these sections:

### Report Template

```markdown
# System Pulse — [Date]

## Protocol Health
- Total tracked: [N]
- Active: [N] ([%])
- Zombies: [N]
- Critical protocols status: [list]

## Quality Trend
- Overall baseline: [score]/10
- Keep rate: [%]
- Total entries: [N]
- Recent trend: [improving/stable/declining]

## Top Performers
- Highest quality skill: [skill] ([score])
- Most active skill: [skill] ([count] entries)

## Action Items
1. [Priority action based on data]
2. [Priority action based on data]
3. [Priority action based on data]

## Autoresearch Loop
- Phase status: [1 ✅ / 2 ✅ / 3 ✅ / 4 🔒]
- Skills due for evolution: [list or "None"]
- Cross-pollination candidates: [list or "None"]
- Gap log entries: [N total, N recurring]
- Next evolution target: [skill — dimension — score]
```

---

## Step 5: Activate Protocols

After producing the report, activate the relevant protocol tracking:

```bash
python3 execution/protocol_tracker.py activate directives/operating-principles.md --note "system-pulse audit"
```
