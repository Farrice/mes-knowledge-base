---
description: Check which Antigravity systems are active vs dormant
---

# /health-check — System Activation Health

Run a health check on all Antigravity systems to see what's active, what's dormant, and what needs attention.

## Usage
```
health-check
```

## Steps

### 1. Run the Health Check Script
```bash
python execution/system_health.py
```

### 2. Present the Report
Display the health report to the user with clear status indicators:
- **ACTIVE**: System is firing and producing data
- **DORMANT**: System has never activated or hasn't fired recently
- **BLOCKED**: System is waiting for upstream dependencies
- **READY**: System has met its activation conditions and can be run

### 3. Recommend Actions
For any CRITICAL or DORMANT systems, explain:
- What the system does
- Why it's not firing
- What specific step activates it

### 4. Offer Immediate Activation
If the Performance Log has 0 entries, offer to run a Quality Gate check on the most recent expert-driven output right now and log the first entry.

If Performance Log has 20+ entries and Skill Evolution hasn't run, offer to run `/skill-evolution`.
