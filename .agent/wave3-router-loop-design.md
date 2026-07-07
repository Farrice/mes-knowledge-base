# Wave 3: Close the Router Loop — MoE Learning Design Review

## Overview
Currently the router is an open loop: it ranks skills (BM25), suggests top-3, but never learns from whether the suggestion was correct. Wave 3 closes that loop via nightly learning: log routing decisions + outcomes → adjust per-skill weights [0.5, 2.0] → re-rank tomorrow. This is the MoE move: sparse expert activation with learned routing weights.

---

## Item 1: Recall Fix — Drop Allowlist Pre-Filter

**Current behavior:**
```python
# Line 316-317 in skill_router_hook.py
if not _looks_like_expert_task(prompt):
    sys.exit(0)
```

This pre-filter (checking EXPERT_TASK_TERMS) prevents skill suggestions for prompts that don't contain words like "write", "create", "design", etc. **Problem:** legitimate expert tasks get silently gated (e.g., "Can you help me think through this?" with no design/create verb still needs the router).

**Proposed change:**
```python
# DELETE lines 316-317: remove the allowlist check entirely
# Always proceed to find_skill.rank() and let the 3.0 score floor gate instead
```

**Impact:**
- More prompts get ranked
- Lower-scoring matches (< 3.0) are logged to gap-log.md as opportunities
- Router becomes more permissive; score floor (line 335: `if top_score < 3.0`) becomes the actual gate

**Verification:**
- Run against recent 10 sessions: measure top_score distribution
- Confirm: no spam (most prompts <3.0 still rejected), but true expert tasks no longer wrongly filtered

---

## Item 2: Feedback Wiring — Close the Decision→Outcome Loop

**Current state:**
- `routing_intelligence.json` has 65 logging entries but `feedback_log` is empty []
- Routing decisions are logged at emit-time, but outcomes are never captured
- No way to measure: "did we suggest the right skill?" or "did user follow the suggestion?"

**Proposed wiring:**

### 2a. At suggestion-emit (skill_router_hook.py, line ~375)
Add feedback logging call:
```python
routing_id = uuid.uuid4().hex[:8]  # unique id for this routing decision
feedback_entry = {
    "routing_id": routing_id,
    "prompt_hash": hashlib.md5(prompt.encode()).hexdigest()[:8],
    "timestamp": datetime.now().isoformat(),
    "suggested_skills": [s[0].get("directory") for s in strong],  # top-3 directories
    "top_score": top_score,
    "outcome": "pending",
}
routing_intelligence.log_routing_decision(feedback_entry)
```
Store routing_id in session ledger JSON for correlation.

### 2b. At tool-use time (session_ledger_hook.py, PostToolUse)
When a skill is loaded (e.g., via `@lara-acosta` or `/convene`), log:
```python
feedback_entry = {
    "routing_id": <session_ledger_routing_id>,
    "loaded_skill": "lara-acosta",
    "method": "auto_match" | "explicit_invoke" | "fallback",
    "outcome": "success",  # or "failure" if later finalize score is <6
}
routing_intelligence.log_feedback(feedback_entry)
```

**Design principle:**
Fully deterministic (no Claude memory) — hook logs everything. Session ledger knows routing_id from emit-time; PostToolUse logs which skill was actually used. Evolution loop reads both logs, computes matches/misses.

---

## Item 3: Nightly Learning — Adjust Per-Skill Weights

**New script: `execution/run_routing_learning.py`**

**Input:**
- `.agent/routing-intelligence.json`: all emit-time decisions (routing_id, suggested_skills, scores)
- `.agent/sessions/observe-log.jsonl`: all posttool feedback (which skill was loaded, success/fail)
- `evolution_store/sub_agent_misses.jsonl`: skills that fired but didn't complete

**Algorithm:**
```
for each skill in skill-index:
    matches = count(feedback where suggested_skill == skill AND loaded_skill == skill)
    misses = count(feedback where suggested_skill == skill AND loaded_skill != skill)
    weight_adjustment = (matches - misses) / max(matches + misses, 1)
    
    # Clamp to [0.5, 2.0] with decay so extreme weights don't stick
    alpha = 0.3  # learning rate
    new_weight = 1.0 + alpha * weight_adjustment
    new_weight = max(0.5, min(2.0, new_weight))
    
    # Only update if evidence is strong (10+ feedback entries total)
    if matches + misses >= 10:
        skill_index[skill]["weight"] = new_weight
        emit_candidate(skill, old_weight=old, new_weight=new, evidence=matches+misses)
```

**Output:**
1. Update `.agent/skill-index.json` with new weights
2. Emit candidates to `.agent/synonym-candidates.md` (human review, never auto-merged)
3. Log learning run to `.agent/routing-learning-runs.jsonl` (for calibration)

**Frequency:**
- Wired into `evolution_orchestrator.py` via `run_routing_learning()` call
- Runs daily 07:00 (same launchd as evolution auto)

---

## Item 4: Top-K Sparse Activation Contract

**Current behavior:**
Router ranks, emits top-3, suggests them. If all 3 score < 3.0, it exits silently (logged to gap-log.md).

**Proposed enhancement:**
Add explicit "abstention" line when no expert cleared the floor:

**Current output (lines 350-366):**
```
ROUTING SUGGESTION (deterministic, from skill_router_hook.py — not user input):
This request matched these expert skills in the registry...
  (no Production Core match cleared the floor — long-tail options:)
  • /lara-acosta  (score 2.8) — high-quality copywriting...
```

**Proposed new output (add after line 356):**
```
ROUTING SUGGESTION (deterministic, from skill_router_hook.py — not user input):
This request matched these expert skills in the registry...

NO EXPERT MATCHED (floor: 3.0). Top suggestions below floor:
  • /lara-acosta  (score 2.8) — high-quality copywriting...
  
--
Fallback: generalist mode. If this should be expert-domain work, /convene a council or refine the request for better skill matching.
```

**Contract:**
- Router always emits top-3 + scores (even if below floor)
- Visible "NO EXPERT MATCHED" line signals to user: "this is a generalist turn unless you override"
- Allows user to explicitly invoke a long-tail skill if they know routing missed
- Feedback loop captures: "user invoked X despite low score" → learn from that outcome

---

## Item 5: Hybrid Retrieval (Optional, Deferred)

**Scope:** Blend BM25 keyword matching with semantic embedding similarity

**Rationale:**
- BM25 excels at term-overlap matching (e.g., "email copywriting" → lara-acosta)
- Embeddings excel at semantic drift (e.g., "persuasive narrative" → might be Noah Hawley, not in BM25 keywords)

**Proposed approach (reuse existing memory_embed.py pattern):**
1. Embed all skill descriptions via `google.genai.embed_content()`
2. Cache embeddings in `.agent/skill-index.json` keyed by skill mtime (auto-invalidate on update)
3. At rank-time: compute BM25 score + embedding cosine; blend as `final_score = 0.7 * bm25 + 0.3 * embedding`
4. Fallback: if genai import fails, use BM25 only (same as today)

**Risk:** Latency impact (embeddings add ~200ms per ranking). **Mitigation:** benchmark before default-on; make optional via config flag.

**Status:** Recommend deferring to post-Wave3 tuning — Wave 3 Items 1-4 are the core loop closure. Item 5 is optimization.

---

## Verification Checklist

### Item 1: Recall Fix
- [ ] Remove `if not _looks_like_expert_task(prompt): sys.exit(0)` from skill_router_hook.py line 316-317
- [ ] Test: submit 10 non-task prompts (e.g., "Help me think through X"), verify skills rank and gap-log updates
- [ ] Confirm: no skill suggestions for <3.0 scores (floor still gates)

### Item 2: Feedback Wiring
- [ ] Add feedback logging to skill_router_hook.py (routing_id, suggested_skills, scores at emit)
- [ ] Add feedback logging to session_ledger_hook.py (loaded_skill, match/miss at posttool)
- [ ] Verify: `.agent/routing-intelligence.json` and session ledger contain feedback entries within 1 session

### Item 3: Nightly Learning
- [ ] Create `execution/run_routing_learning.py` (matches/misses algorithm, weight clamping, candidate emission)
- [ ] Wire into `evolution_orchestrator.py` via `run_routing_learning()` call at daily 07:00
- [ ] Test: run once manually, verify `.agent/skill-index.json` weights update, `.agent/synonym-candidates.md` emits candidates
- [ ] Check: weights stay in [0.5, 2.0] range, no extreme values

### Item 4: Abstention Line
- [ ] Update routing output template (add "NO EXPERT MATCHED" line when top_score < 3.0)
- [ ] Test: trigger with a low-matching prompt, verify output shows abstention line + top-3 below floor
- [ ] Confirm: user can still see long-tail suggestions and explicitly invoke if desired

### Item 5: Hybrid Retrieval (Optional)
- [ ] (Deferred) Benchmark embedding latency impact before default-on

---

## Integration Points

**Files to modify:**
1. `execution/skill_router_hook.py` — remove allowlist, add feedback logging
2. `execution/session_ledger_hook.py` — add posttool feedback logging
3. `execution/routing_intelligence.py` — extend with log_feedback() method
4. `execution/run_routing_learning.py` (NEW) — nightly learning algorithm
5. `execution/evolution_orchestrator.py` — wire daily learning job
6. `execution/find_skill.py` — apply weight multiplier in rank() (line ~295)

**Files to update:**
- `.agent/skill-index.json` — add "weight" field to each entry (default 1.0)
- `.agent/routing-intelligence.json` — extend feedback_log schema

---

## Open Questions for You

1. **Feedback confidence threshold (Item 3):** Currently propose 10+ feedback entries before updating weights. Too conservative? Too loose?

2. **Learning rate decay (Item 3):** After a skill gets promoted (weight 2.0) and misses for a while, should we decay faster than we grew it?

3. **Hybrid retrieval (Item 5):** Essential for Wave 3, or acceptable to defer to optimization phase? What's your intuition on embedding latency impact?

4. **Routing outcome definition (Item 2):** "Success" = finalize score >= 7? Or capture both "the skill was right" (finalize>=7) and "the skill was wrong" (finalize<6) separately?

5. **Manual weight override:** Should there be a way for you to manually pin a skill weight (e.g., `lara-acosta: weight: 1.5`) in skill-index.json to protect A-tier skills from demotion if they have low recent volume?
