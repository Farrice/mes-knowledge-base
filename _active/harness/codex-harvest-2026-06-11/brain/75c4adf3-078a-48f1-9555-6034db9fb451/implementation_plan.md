# Harness Architecture Audit & Evolution Plan

## Audit Summary (DPVI Framework)

Full scan of the Antigravity harness using Nate B. Jones's **Discover → Prioritize → Verify → Iterate** pattern.

### Always-On Cost (Every Message)

| File | Size | Purpose |
|------|------|---------|
| [AGENTS.md](file:///Users/farricecain/Google%20Antigravity/AGENTS.md) | 11.8KB | Claude Code harness |
| [GEMINI.md](file:///Users/farricecain/Google%20Antigravity/GEMINI.md) | 5.0KB | Gemini model harness |
| Workflow descriptions | ~2.8KB | 388 slash commands |
| **Total** | **~19.6KB** | **~4,900 tokens/message** |

> [!NOTE]
> AGENTS.md and GEMINI.md share 7 concepts (The Chain, Architecture, Context Engine, Finalize, etc.) but this is **intentional** — each file must be self-contained for its model runtime. No changes to either file proposed.

---

## Finding 1: 29 Orphaned Directives

> [!WARNING]
> Only **13 of 42 directives** are referenced in AGENTS.md's Supporting Protocols table. The other 29 exist but the agent can't discover them unless a workflow happens to load one.

**Live (13)**: agent-loading-protocol, collaboration-protocol, content_creation_gate, deep_self_annealing, expert_auto_routing, feedback-ratchet, intent-pipeline, notebooklm-usage-policy, operating-principles, perplexity-usage-policy, quality_assurance, quality_gate, session-state-protocol, sub_agent_protocol, token-efficiency-protocol

**Orphaned (29)**: ai-slop-detector, content-creation, cross-pollination, daily-council, decision-council, expertise-gap-protocol, extraction-to-skill, extraction-workflow, gemini-reference, ghostwriting-delivery, hybrid-knowledge-retrieval, mcp-research-setup, mcp-server-setup, mes-3.0-extract, mes-3.0-validate, multi-expert-synthesis, notion-databases, parallel_thought, parallelism-cheat-sheet, research-protocol, sales-conversation, session-end-commit, skill-evolution-protocol, skill-paths-reference, user-state-awareness, verification-agent-protocol, workflow-chains

**Impact**: Important directives like `notion-databases.md`, `extraction-workflow.md`, and `skill-evolution-protocol.md` are invisible to the orchestration loop.

---

## Finding 2: Missing Evolution Infrastructure

> [!IMPORTANT]
> No `evolution_store/` directory exists for trace logging, search sets, or proposer history. The self-evolving loop has no persistent local storage. (Note: user's open files show `evolution_store/` with `baseline/` and `variant_001/variant_003/` — these may be from a previous conversation and need verification.)

---

## Finding 3: AGENTS.md Internal Issues

1. **Title says `# CLAUDE.md`** — should say `# AGENTS.md` or `# CLAUDE.md / AGENTS.md`
2. **Stale sync comment** (line 5) — references `/sync-instructions` to update GEMINI.md, which is now independently maintained
3. **Static config in harness** — NotebookLM notebook names hardcoded in the knowledge sources section

---

## Proposed Changes

### Phase 1: Directive Index in AGENTS.md

> Make all 42 directives discoverable without bloating the always-on payload.

#### [MODIFY] [AGENTS.md](file:///Users/farricecain/Google%20Antigravity/AGENTS.md)

Replace the current "Supporting Protocols" table (13 directives, 19 lines) with a compact **full directive index** organized by category. Each entry: name + 1-line trigger condition. This adds ~15 lines but makes 29 previously invisible directives discoverable.

**Categories**:
- **Chain Protocols** (fire during the 6-step chain): quality_assurance, quality_gate, feedback-ratchet, content_creation_gate, etc.
- **Routing & Loading**: agent-loading-protocol, expert_auto_routing, intent-pipeline, multi-expert-synthesis
- **Research & Knowledge**: hybrid-knowledge-retrieval, research-protocol, perplexity-usage-policy, notebooklm-usage-policy
- **Extraction & Skills**: extraction-workflow, extraction-to-skill, mes-3.0-extract, mes-3.0-validate, skill-evolution-protocol
- **Session & System**: session-state-protocol, session-end-commit, token-efficiency-protocol, collaboration-protocol, operating-principles
- **Domain-Specific**: ghostwriting-delivery, sales-conversation, notion-databases, daily-council, decision-council

Also fix:
- Title: `# CLAUDE.md` → `# AGENTS.md — Antigravity System Harness`
- Remove stale sync comment (line 5)
- Move NotebookLM notebook names to a directive or `.agent/config.json`

---

### Phase 2: Evolution Store Verification & Setup

#### Verify existing `evolution_store/`
Check if the directory from the previous harness evolution conversation (conversation `54cb496f`) is still intact and functional.

#### [NEW or VERIFY] `evolution_store/` structure
- `traces/` — structured failure/success logs from chain_runner
- `search_sets/` — curated hard examples
- `proposals/` — improvement candidates
- `baselines/` — current performance snapshots with `score.json`

#### [MODIFY] [chain_runner.py](file:///Users/farricecain/Google%20Antigravity/execution/chain_runner.py)
- Add `--trace` flag to finalize that appends a structured JSON trace to `evolution_store/traces/`
- Each trace: timestamp, intent score, expert, tier, quality dimensions, notes

---

## Verification Plan

### Automated
```bash
# Confirm all 42 directives mentioned in AGENTS.md
for d in directives/*.md; do
  name=$(basename "$d")
  grep -q "$name" AGENTS.md || echo "MISSING: $name"
done

# Confirm evolution_store structure
test -d evolution_store/traces && echo "PASS"

# Test chain_runner with --trace
python3 execution/chain_runner.py finalize "test" --expert test --skill test \
  --workflow test --type System --intent 8 --expert-score 8 --adversarial 8 \
  --trace --notes "harness audit verification"
```

### Manual
- User runs one expert deployment to verify the updated AGENTS.md doesn't break routing
