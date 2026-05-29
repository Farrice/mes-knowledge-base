#!/bin/bash
# Phase 6: Continuous Quality Loop Setup
# Establishes automated weekly/monthly calibration checks
# Deploy these as cron jobs after perception product ships

set -e

ROOT="/Users/farricecain/Google Antigravity"
cd "$ROOT"

echo "=== Phase 6: Continuous Quality Loop Setup ==="
echo "Timestamp: $(date)"
echo ""

# Phase 6.1: Weekly Evolution Auto-Run
echo "[6.1] Weekly Evolution Auto-Run"
echo "Schedule: Every Monday 6am"
echo "Command: python3 execution/evolution_orchestrator.py auto"
echo "Purpose: Automatically advance grounded skills Phase 2->3, surface gaps"
echo "Logs: .agent/evolution-orchestrator-weekly-*.log"
echo ""

# Phase 6.2: Monthly Calibration Drift Detection
echo "[6.2] Monthly Calibration Drift Detection"
echo "Schedule: First of every month, 8am"
echo "Command: python3 execution/eval_harness.py calibrate --days 30"
echo "Purpose: Detect if recent finalize scores have inflated (>90% at 8+)"
echo "Threshold: If drift detected, trigger rubric re-anchoring"
echo "Logs: .agent/calibration-drift-monthly-*.log"
echo ""

# Phase 6.3: Perception Product Path Monthly Spot-Check
echo "[6.3] Perception Product Path Monthly Spot-Check"
echo "Schedule: 15th of every month, 10am"
echo "Commands:"
echo "  - python3 execution/dependency_validator.py (22 perception workflows)"
echo "  - python3 execution/notion_api.py query <perf-log-db-id> --filter 'skill in [perception-*, georgi-*]' --limit 100"
echo "Purpose: Verify no new broken refs, spot-check Quality Gate compliance"
echo "Action on failure: Run Phase 2 evolution on affected workflows"
echo "Logs: .agent/perception-spot-check-monthly-*.log"
echo ""

# Phase 6.4: Prose Classifier Weekly Scan (Tier 1 workflows only)
echo "[6.4] Prose Classifier Weekly Scan"
echo "Schedule: Every Wednesday, 2pm"
echo "Command: python3 execution/prose_classifier.py scan skills/rory-sutherland-marketing/ skills/stefan-georgi-dopamine-copy/ --severity flagged"
echo "Purpose: Detect AI-writing tells in finalized content before shipping"
echo "Threshold: Any FLAGGED = pause finalize, human review required"
echo "Logs: .agent/prose-scan-weekly-*.log"
echo ""

# Phase 6.5: Revenue & Outcome Tracking
echo "[6.5] Revenue & Outcome Tracking"
echo "Trigger: After every client delivery using perception product path"
echo "Command: python3 execution/revenue_tracker.py log '<deliverable>' --revenue <amount> --outcome '<result>'"
echo "Monthly roll-up: python3 execution/revenue_tracker.py report"
echo "Purpose: Connect quality scores to business outcomes; inform next cycle evolution"
echo "Logs: .agent/revenue-outcomes.json (append-only)"
echo ""

# Generate cron config template
cat > .agent/cron-setup-phase6.txt << 'CRON'
# Add these to `crontab -e` after perception product ships
# All times in user's local timezone (set in crontab environment)

# Weekly Evolution Auto-Run (Mondays, 6am)
0 6 * * 1 cd /Users/farricecain/Google\ Antigravity && python3 execution/evolution_orchestrator.py auto >> .agent/evolution-orchestrator-weekly-$(date +\%Y\%m\%d).log 2>&1

# Monthly Calibration Drift (1st, 8am)
0 8 1 * * cd /Users/farricecain/Google\ Antigravity && python3 execution/eval_harness.py calibrate --days 30 >> .agent/calibration-drift-monthly-$(date +\%Y\%m\%d).log 2>&1

# Perception Spot-Check (15th, 10am)
0 10 15 * * cd /Users/farricecain/Google\ Antigravity && python3 execution/dependency_validator.py >> .agent/perception-spot-check-monthly-$(date +\%Y\%m\%d).log 2>&1

# Prose Classifier Scan (Wednesdays, 2pm)
0 14 * * 3 cd /Users/farricecain/Google\ Antigravity && python3 execution/prose_classifier.py scan skills/rory-sutherland-marketing/ skills/stefan-georgi-dopamine-copy/ --severity flagged >> .agent/prose-scan-weekly-$(date +\%Y\%m\%d).log 2>&1
CRON

echo ""
echo "=== Phase 6 Setup Complete ==="
echo "Cron template written to: .agent/cron-setup-phase6.txt"
echo ""
echo "NEXT STEPS:"
echo "1. Review cron template: cat .agent/cron-setup-phase6.txt"
echo "2. After perception product ships, add to crontab: crontab -e"
echo "3. Verify: crontab -l (should show 4 new entries)"
echo "4. Monitor logs in .agent/ daily during first 30 days"
echo ""
echo "ANTI-PATTERN DETECTION:"
echo "- If prose_classifier reports FLAGGED: pause deliveries, run writers-room"
echo "- If calibration_drift shows >90% at score 8+: re-anchor rubric via eval_harness.py anchor"
echo "- If perception spot-check fails: don't ship, trigger Phase 2 evolution"
echo "- If revenue_tracker shows ROI <1.0: audit finalize scores for grade inflation"
echo ""
