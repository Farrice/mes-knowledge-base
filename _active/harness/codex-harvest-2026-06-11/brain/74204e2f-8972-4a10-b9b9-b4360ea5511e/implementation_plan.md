# Phase 4 Unlock + Self-Improvement Loop Automation

## The Problem

The autoresearch loop has 4 phases. Phases 1-3 are now activated, but the loop **doesn't run on its own** — every phase requires you to manually ask me to do it. Phase 4 is locked because a critical dependency (the gap log) doesn't exist yet.

---

## Phase 4 Unlock — What's Missing

Phase 4 (Gap Intelligence) has **3 dependencies**, all currently at zero:

| Dependency | Current State | What Fills It |
|-----------|--------------|---------------|
| `.agent/gap-log.md` | ❌ File doesn't exist | Created when the Expertise Gap Protocol fires during routing |
| Gap log entries | 0 entries | Each time I can't find an expert for a task, a gap gets logged |
| 3+ recurring gaps in same domain | 0 recurring | Need the same missing domain to appear 3+ times |

**The blocker**: The Expertise Gap Protocol (`directives/expertise-gap-protocol.md`) has **0 activations** — meaning every task you've given me so far has matched an existing expert. Gaps only get logged when routing *fails* to find a skill.

### How to unlock Phase 4:

1. **Initialize the gap log** — I'll create `.agent/gap-log.md` so it's ready when gaps fire
2. **Start working in domains you don't have skills for** — any task that falls outside your 45+ extracted experts will trigger gap detection and log it
3. **Alternatively**: Run `/gap-report` periodically — `execution/gap_analysis.py` already works and will surface dead skills, low performers, and weak task types even without gap log data

> [!IMPORTANT]
> Phase 4 will likely unlock **naturally** as you use the system for more diverse work. The fact that it hasn't fired means your skill coverage is actually very strong.

---

## Making the Self-Improvement Loop Automatic

Currently, each phase requires manual triggering:

```
Phase 1 → Happens automatically (chain_runner finalize logs to Notion)
Phase 2 → You say "/skill-evolution" manually
Phase 3 → I propagate manually after Phase 2
Phase 4 → Gaps log automatically, but gap-report is manual
```

### What I Can Build

#### Option A: Session Triggers (Low-Effort, High-Impact)

Add automatic checks to existing workflows so the loop fires without you remembering:

| Trigger | What Fires | When |
|---------|-----------|------|
| Every `/session-kickoff` | Check if any skill has 5+ new entries since last evolution → suggest `/skill-evolution` | Start of every session |
| Every `chain_runner finalize` | Auto-log performance + auto-check for regression → flag if evolution needed | End of every deliverable |
| Every routing failure | Auto-create gap-log entry + surface gap report if 3+ recurring | During `/recommend` or any routed task |

#### Option B: `/system-pulse` Enhancement (Medium Effort)

Enhance the existing `/system-pulse` weekly dashboard to include:
- Skills due for evolution (5+ entries since last cycle, weakest dimension < 7)
- Cross-pollination candidates from recent evolutions
- Gap log summary + recurring gap alerts
- Dead skills for cleanup

#### Option C: Full Automation Script (Higher Effort)

Build `execution/autoresearch_loop.py` — a single script that:
1. Pulls latest performance data from Notion
2. Identifies the weakest skill + dimension
3. Generates an evolution hypothesis
4. Presents it for approval (or auto-runs with `--autonomous` flag)
5. Propagates improvements to related skills
6. Runs gap analysis and surfaces recommendations

### My Recommendation

**Start with Option A** — it's the highest-leverage move. The loop becomes semi-automatic because the system *reminds you* at natural checkpoints. You don't need to remember to run `/skill-evolution` — the session kickoff tells you when one is due.

Then **layer Option B** to get a weekly intelligence view.

Option C is the endgame but premature until you have 100+ Performance Log entries and consistent usage patterns.

---

## Proposed Changes

### Session Kickoff Enhancement

#### [MODIFY] [session-kickoff.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/session-kickoff.md)

Add an "Autoresearch Check" step that:
- Queries Notion Performance Log for entries since last evolution
- If 5+ new entries exist → present evolution candidate
- Checks gap log for recurring gaps → surface if found

---

### Gap Log Initialization

#### [NEW] [gap-log.md](file:///Users/farricecain/Google%20Antigravity/.agent/gap-log.md)

Create the empty gap log file so the Expertise Gap Protocol can write to it.

---

### Feedback Ratchet Update

#### [MODIFY] [feedback-ratchet.md](file:///Users/farricecain/Google%20Antigravity/directives/feedback-ratchet.md)

Update Phase 2 activation threshold (currently says "20 entries needed, currently at 13" — this is stale since we already activated Phase 2 with 45 entries).

---

## Verification Plan

### Automated Tests
```bash
# Verify gap_analysis.py runs clean with current data
python execution/gap_analysis.py recommendations

# Verify pattern_propagation.py can scan evolution logs
python execution/pattern_propagation.py scan
```

### Manual Verification
- Run `/session-kickoff` and confirm the autoresearch check appears
- Verify `.agent/gap-log.md` exists and is writable
