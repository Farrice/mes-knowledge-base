---
title: P1 Fixes — Immediate Actions
date: 2026-07-15
priority: critical
---

# P1 Fixes — Critical Routing & Telemetry Repairs

## Overview

Two P1 issues block routing precision and operator visibility. Both are workspace-local, low-risk fixes with clear verification paths.

**Timeline**: Complete within 1 hour  
**Verification**: Both issues must pass re-test before considering "done"

---

## Fix #1: Routing Conflict (health-check misrouting)

### Issue
Query: `"health check harness status"` routes to `/system-audit` instead of `/health-check`

### Root Cause
Workflow router scoring logic doesn't distinguish between:
- Status reads → `/health-check` (lightweight, read-only)
- System repairs → `/system-audit` (heavyweight audit & fix)

### Fix Steps

#### Step 1a: Understand Current Routing

```bash
cd /Users/farricecain/Google\ Antigravity

# Test current routing
python3 execution/workflow_router.py search "health check harness status"
```

**Expected output before fix**:
```
/system-audit (scored X.XX)
/health-check (scored X.XX)
...
```

The problem: `/system-audit` is ranked first when it should be `/health-check`.

#### Step 1b: Audit Workflow Router Logic

```bash
# Read the router code to understand scoring
grep -A 20 "def score_workflow" execution/workflow_router.py | head -30
```

**Look for**: 
- Where "health" + "check" keywords are scored
- Whether the router distinguishes "status" from "repair"
- If there's a binding override for health-check queries

#### Step 1c: Check Golden Query Matrix

```bash
# Review what the golden matrix expects
python3 << 'EOF'
import json
matrix = json.loads(open("execution/control_plane_golden_queries.json").read())
for case in matrix["queries"]:
    if "health-check" in case.get("id", ""):
        print(f"ID: {case['id']}")
        print(f"Query: {case['query']}")
        print(f"Expected first: {case['expected_first']}")
        print(f"Expected lane: {case.get('expected_lane', 'N/A')}")
        print()
EOF
```

**Expected output**:
```
ID: health-check-harness-status
Query: health check harness status
Expected first: ['health-check']
Expected lane: health-check-status
```

#### Step 1d: Fix Routing Bindings or Scoring

**Option A** (Recommended — Bindings): Add explicit binding for health-check queries

Edit `execution/routing_enforcer.py` or `.agent/workflows/health-check.md` to add:

```python
# In routing_enforcer.py BINDINGS dict, add:
"health check status harness" : ["health-check"],
"health check" : ["health-check"],
```

**Option B** (Scoring adjustment): Modify workflow_router scoring for health-check keyword

Edit `execution/workflow_router.py` to boost `/health-check` score when:
- Query contains "health" + "check" OR "status"
- Query does NOT contain "audit" or "repair" or "broken"

#### Step 1e: Re-Test

```bash
python3 execution/workflow_router.py search "health check harness status"
```

**Expected output after fix**:
```
/health-check (scored X.XX)  ← Now ranked #1
/system-audit (scored X.XX)
...
```

#### Step 1f: Run Full Control-Plane Verification

```bash
python3 execution/verify_system_control_plane.py 2>&1 | head -100
```

**Must pass**: The golden query test for `health-check-harness-status` should now pass.

**Expected**:
```
golden query health-check-harness-status: menu=/health-check, router=/health-check, governor=/health-check
```

---

## Fix #2: Telemetry Broken (routing_intelligence.py KeyError)

### Issue
`python3 execution/routing_intelligence.py scoreboard` crashes with `KeyError: 'auto_miss'`

### Root Cause
Rating enum mismatch in routing_intelligence.py. The code expects a rating value 'auto_miss' that doesn't exist in the data or enum.

### Fix Steps

#### Step 2a: Reproduce the Error

```bash
cd /Users/farricecain/Google\ Antigravity
python3 execution/routing_intelligence.py scoreboard 2>&1
```

**Expected error**:
```
KeyError: 'auto_miss'
  File execution/routing_intelligence.py, line 438
    ensembles[pairing][rating] += 1
```

#### Step 2b: Audit Data Model

```bash
# Check what ratings exist in the telemetry data
python3 << 'EOF'
import json
from pathlib import Path

log_file = Path(".agent/routing_telemetry.jsonl")
if log_file.exists():
    ratings = set()
    for line in log_file.read_text().split("\n"):
        if line.strip():
            data = json.loads(line)
            if "rating" in data:
                ratings.add(data["rating"])
    print("Ratings found in telemetry data:")
    for r in sorted(ratings):
        print(f"  - {r}")
else:
    print("No routing_telemetry.jsonl file found")
EOF
```

**Expected output**: A list of actual rating values (e.g., PASS, MISS, PARTIAL)

#### Step 2c: Check Enum Definition

```bash
# Find enum definition in routing_intelligence.py
grep -B 5 -A 10 "class.*Rating\|RATING.*=\|'auto_miss'" execution/routing_intelligence.py
```

#### Step 2d: Fix the Enum or Data Handler

**Option A** (Add missing value): If 'auto_miss' should exist but doesn't:
```python
# In routing_intelligence.py, add 'auto_miss' to the enum
class Rating(Enum):
    PASS = "pass"
    MISS = "miss"
    PARTIAL = "partial"
    AUTO_MISS = "auto_miss"  # ← Add this
```

**Option B** (Handle gracefully): If 'auto_miss' is a legacy value that should be ignored:
```python
# In routing_intelligence.py line 438, change:
if rating in ensembles[pairing]:
    ensembles[pairing][rating] += 1
# to handle missing ratings:
if rating in ensembles[pairing]:
    ensembles[pairing][rating] += 1
else:
    ensembles[pairing][rating] = 1
```

**Option C** (Filter telemetry): If 'auto_miss' is a data corruption issue, clean it out:
```bash
# Backup and clean
cp .agent/routing_telemetry.jsonl .agent/routing_telemetry.jsonl.bak
python3 << 'EOF'
import json
from pathlib import Path

cleaned = []
for line in Path(".agent/routing_telemetry.jsonl").read_text().split("\n"):
    if line.strip():
        data = json.loads(line)
        if data.get("rating") != "auto_miss":  # Skip auto_miss entries
            cleaned.append(line)

Path(".agent/routing_telemetry.jsonl").write_text("\n".join(cleaned))
print(f"Cleaned {len(cleaned)} entries (removed auto_miss)")
EOF
```

#### Step 2e: Re-Test

```bash
python3 execution/routing_intelligence.py scoreboard
```

**Expected output**: A scoreboard table with routing analytics (no KeyError)

```
Routing Intelligence Scoreboard
═════════════════════════════════
Route          PASS   MISS   PARTIAL   Total
autopilot      245    12     8         265
health-check   52     3      2         57
system-audit   28     5      1         34
...
```

---

## Verification Checklist

After both fixes, run this sequence to confirm:

```bash
#!/bin/bash
set -e

echo "=== Fix #1: Routing Conflict ==="
python3 execution/workflow_router.py search "health check harness status" | head -1
# Expected: health-check (first line)

echo ""
echo "=== Fix #2: Telemetry Scoreboard ==="
python3 execution/routing_intelligence.py scoreboard | head -5
# Expected: No error; table headers appear

echo ""
echo "=== Full Control-Plane Verification ==="
python3 execution/verify_system_control_plane.py 2>&1 | grep -E "PASS|FAIL|health-check-harness"
# Expected: "health-check-harness-status: menu=/health-check, router=/health-check"

echo ""
echo "✅ All P1 fixes verified"
```

---

## Rollback Plan

If a fix breaks something:

```bash
# Revert to last good state
git diff HEAD execution/workflow_router.py execution/routing_intelligence.py
git checkout HEAD -- execution/workflow_router.py execution/routing_intelligence.py

# Re-test
python3 execution/verify_system_control_plane.py
```

---

## Sign-Off

**Fix #1 Status**: [ ] In progress  [ ] Complete  [ ] Verified  
**Fix #2 Status**: [ ] In progress  [ ] Complete  [ ] Verified  

Once both pass verification, commit with:

```bash
git add execution/workflow_router.py execution/routing_intelligence.py execution/routing_enforcer.py
git commit -m "Fix P1 routing conflicts and telemetry KeyError

- Reconcile health-check routing against golden query matrix
- Fix routing_intelligence.py enum mismatch causing scoreboard failure
- Both issues verified with control-plane golden queries

Resolves system-health-check-framework audit findings (2026-07-15)"
```

---

## Timeline

- **Now - 30 min**: Run diagnostics, identify exact issue location
- **30-45 min**: Apply fixes per Option A/B above
- **45-60 min**: Verify + commit

**Total: ~1 hour**
