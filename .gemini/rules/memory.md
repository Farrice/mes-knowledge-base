# Memory — See GEMINI.md for compaction recovery
# This file is intentionally minimal to reduce context budget.
# Write .agent/session-state.md after: intent validation, expert deployment, user decisions, 7+ file reads.
# After compaction: READ .agent/session-state.md IMMEDIATELY.
# Frustration detection: Tier 1 (explicit) → execute immediately. Tier 2 (implicit) → reduce 50%. Tier 3 (escalation) → zero overhead.
