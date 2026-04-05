---
description: Periodic maintenance audit for context window health
---

# /system-hygiene — System Maintenance & Context Window Health

Run this workflow monthly or after heavy extraction sessions (5+ new workflows created) to prevent context window exhaustion.

---

## Phase 1: Workflow Description Audit

```bash
python3 execution/trim_workflow_descriptions.py --audit
```

**Check:**
- Total workflow count (flag if >500 — approaching critical overhead)
- Average words per description (target: ≤6)
- Any descriptions over 8 words → run `--trim` to preview, `--trim --apply` to fix
- Estimated token overhead from descriptions alone

**Context math:** Each workflow listing costs ~24 tokens (path + dash + description). At 460 workflows, that's ~11,000 tokens of static system prompt overhead before any conversation begins.

---

## Phase 2: Duplicate & Redundant Workflow Detection

Scan for overlapping workflows that could be consolidated:

```bash
# Find workflows with very similar descriptions
cd .agent/workflows && grep -h '^description:' *.md | sort | uniq -c | sort -rn | head -20
```

**Known consolidation candidates:**
| Cluster | Count | Example Workflows | Consolidation Path |
|---------|-------|-------------------|--------------------|
| `drk-*` | 18 | drk-belief-dissolve, drk-creative-unblock, drk-emotional | Consider a master `/drk` dispatcher that routes to sub-workflows |
| `connelly-*` | 12 | connelly-anchor, connelly-calibrate, connelly-character | Consider a master `/connelly` dispatcher |
| `wright-*` | 12 | wright-detail, wright-erosion, wright-gap | Consider a master `/wright` dispatcher |
| `junyuh-*` | 13 | junyuh-audit, junyuh-brandbook, junyuh-coach | Consider a master `/junyuh` dispatcher |
| `enrico-*` | 11 | enrico-audit, enrico-curb-appeal, enrico-expand | Consider a master `/enrico` dispatcher |
| `roth-*` | 9 | roth-content, roth-copy, roth-email | Consider a master `/roth` dispatcher |
| `word-*` | 14 | word-audit, word-charisma, word-copy | Consider a master `/word` dispatcher |
| `grace-*` | 10 | grace-attention-swarm, grace-city-blueprint | Consider a master `/grace` dispatcher |
| `proof-*` | 11 | proof-audit-360, proof-braid-engine | Consider a master `/proof` dispatcher |
| `newsletter-*` | 9 | newsletter-flywheel, newsletter-growth-audit | Consider a master `/newsletter` dispatcher |
| `insight-*` | 8 | insight-audit, insight-bridge, insight-brief | Consider a master `/insight` dispatcher |

**Consolidation pattern (dispatcher model):**
Instead of 12 individual `connelly-*` listings in the system prompt, a single `/connelly` dispatcher reads a sub-menu and routes internally. This would replace 12 listings with 1 — saving ~264 tokens per cluster.

**Estimated savings if top 6 clusters consolidated:** ~60 workflow listings removed → ~1,440 tokens saved from system prompt.

> **DO NOT consolidate now.** This is a reporting step. Present findings to the user and let them decide which clusters to consolidate and when.

---

## Phase 3: Orphan & Broken Workflow Check

```bash
# Check for workflow files referenced but missing
cd .agent/workflows
for f in *.md; do
  name="${f%.md}"
  if ! grep -q "^description:" "$f" 2>/dev/null; then
    echo "MISSING DESCRIPTION: $f"
  fi
done

# Check for empty or near-empty workflow files
find .agent/workflows -name "*.md" -size -50c
```

---

## Phase 4: Genius File Size Audit

```bash
# Report genius.md sizes across all skills (large files = high context cost when loaded)
find skills -name "genius.md" -exec wc -c {} \; | sort -rn | head -20
```

**Thresholds:**
- <5KB: ✅ Lean
- 5-15KB: ⚠️ Standard — only load at Tier 2
- >15KB: 🔴 Heavy — consider splitting or compressing

---

## Phase 5: Stale File Cleanup

```bash
# Clean .tmp/ directory
rm -rf .tmp/*

# Check session state staleness (>7 days = stale)
if [ -f .agent/session-state.md ]; then
  age=$(( ($(date +%s) - $(stat -f %m .agent/session-state.md)) / 86400 ))
  if [ $age -gt 7 ]; then
    echo "SESSION STATE IS STALE ($age days old) — safe to delete"
    rm .agent/session-state.md
  else
    echo "Session state is $age days old — still fresh"
  fi
fi
```

---

## Phase 6: System Prompt Size Estimate

```bash
# Estimate total AGENTS.md size
wc -c AGENTS.md GEMINI.md

# Check character limits (AGENTS < 11K, GEMINI < 2K)
agents_size=$(wc -c < AGENTS.md)
gemini_size=$(wc -c < GEMINI.md)

if [ $agents_size -gt 11000 ]; then
  echo "⚠️  AGENTS.md is $agents_size chars (limit: 11,000)"
else
  echo "✅ AGENTS.md is $agents_size chars (under 11,000)"
fi

if [ $gemini_size -gt 2000 ]; then
  echo "⚠️  GEMINI.md is $gemini_size chars (limit: 2,000)"
else
  echo "✅ GEMINI.md is $gemini_size chars (under 2,000)"
fi
```

---

## Output: Hygiene Report

Produce a summary with:
1. **Workflow count** + trend (up/down from last run)
2. **Description audit** — any violations, tokens saved
3. **Consolidation candidates** — top 3 clusters worth merging
4. **Genius file sizes** — any over 15KB
5. **Stale files cleaned** — what was removed
6. **Harness file sizes** — AGENTS.md and GEMINI.md vs limits
7. **Recommendation** — single most impactful next action

---

## When to Run

- **Monthly minimum** during active development
- **After any extraction session** that creates 5+ new workflows
- **Before heavy sessions** (multi-expert deploys, campaigns) to ensure headroom
- **If you hit "agent executor truncation" errors** — run immediately
