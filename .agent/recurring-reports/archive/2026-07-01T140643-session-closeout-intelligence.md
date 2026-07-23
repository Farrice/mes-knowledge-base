# Session Closeout Intelligence

**Generated**: 2026-07-01 14:06
**Mode**: write

## Performance Registrar

```text
FAIL (1)
Traceback (most recent call last):
  File "/Users/farricecain/Google Antigravity/execution/session_log_registrar.py", line 30, in <module>
    from log_performance import get_local_performance_entries, log_output
ImportError: cannot import name 'get_local_performance_entries' from 'log_performance' (/Users/farricecain/Google Antigravity/execution/log_performance.py)
```

## Routing Decisions

No routing candidates found.

## Explicit Route Feedback

No explicit route feedback candidates found.

## Ambiguous Feedback Inbox

No ambiguous feedback signals found.

## Snapshots

### Health Check

```text
PASS
Running Antigravity System Health Check...

# Antigravity System Health Report
**Generated**: 2026-07-01 14:06

## Activation Status

| System | Status | Last Active | Entries | Health |
|--------|--------|-------------|---------|--------|
| Performance Log (Phase 1) | ERROR | Error | 0 | Unknown |
| Skill Evolution (Phase 2) | BLOCKED (0/20 entries) | — | — | Waiting |
| Cross-Pollination (Phase 3) | BLOCKED | — | — | Needs Phase 2 |
| Gap Detection (Phase 4) | BLOCKED | — | — | Needs data |
| Session State | ACTIVE | Today (2026-07-01 12:41) | — | Healthy |
| Routing Intelligence | DORMANT | — | 0 | Warning |
| Gap Log | DORMANT | — | 0 | OK |
| Sovereign Memory | ACTIVE | — | 4623 | Degraded |

## Sovereign Memory

- **Total memories**: 4623 (88 pinned, 1149 embedded — 24.9% coverage)
- **By tier**: episodic=4417, procedural=113, semantic=93
- **By workspace**: (global)=999, claude-export=3624
- **Notion mirror**: 559 pages, last mirrored 12.11h ago (OK)
- **Latest backup**: 11.11h ago (OK)
- **⚠ Flagged for review**: 1 pending — run `python3 execution/memory_review.py list`

## Hookify Guards

| Hook | Enabled | Event | Action |
|------|---------|-------|--------|
| anchor-named-discipline | Yes | stop | warn |
| autopilot-ledger-reminder | Yes | stop | warn |
| fal-budget-check | Yes | bash | warn |
| freshness-tax-enforcement | Yes | stop | warn |
| intent-pipeline-check | Yes | stop | warn |
| notion-api-guard | Yes | bash | block |
| performance-log-reminder | Yes | stop | warn |
| perplexity-budget-check | Yes | bash | warn |
| quality-gate-enforcement | Yes | stop | warn |
| routing-coverage-check | Yes | stop | warn |
| session-state-reminder | Yes | stop | warn |

## Cascade Dependencies

```
Performance Log (0 entries)
  └─> Skill Evolution (needs 20+) [0/20]
        └─> Cross-Pollination (needs evolution data) [waiting]
              └─> Gap Detection (monthly) [waiting]
```

## Recommended Actions

1. **CRITICAL**: Start logging performance entries. Run the Quality Gate after your next expert-driven output, then log with `python execution/log_performance.py log "description" --skill X --type Y --quality N --status Keep`
2. **WARNING**: No routing decisions logged. The routing intelligence system needs data to improve over time.
3. **INFO**: Embedding coverage at 24.9% — run `python3 execution/memory_embed.py backfill` to fill gaps.
4. **REVIEW**: 1 distilled memories awaiting human approval. Run `python3 execution/memory_review.py list`.
```

### Skill Evolution Candidates

```text
PASS
# Skill Evolution Candidate Status

ready=0 watchlist=268 blocked=50 top=maria-wendt-digital-products (watchlist)
```

### Protocol Audit

```text
PASS
============================================================
  PROTOCOL ACTIVATION AUDIT
============================================================
  Total Protocols:    45
  Active:             13
  Never Activated:    32
  Zombies (overdue):  42
  Total Activations:  1413
  Activation Rate:    29%
------------------------------------------------------------

  🔴 ZOMBIES (need attention):
    • agent-loading-protocol.md: never activated (count: 0)
    • ai-slop-detector.md: never activated (count: 0)
    • apify-usage-policy.md: overdue since 2026-05-06 (count: 0)
    • collaboration-protocol.md: never activated (count: 0)
    • content-creation.md: never activated (count: 0)
    • content_creation_gate.md: never activated (count: 0)
    • cross-pollination.md: never activated (count: 0)
    • daily-council.md: never activated (count: 0)
    • decision-council.md: never activated (count: 0)
    • deep_self_annealing.md: never activated (count: 0)
    • expert_auto_routing.md: never activated (count: 0)
    • expertise-gap-protocol.md: never activated (count: 0)
    • extraction-to-skill.md: never activated (count: 0)
    • extraction-workflow.md: never activated (count: 0)
    • ghostwriting-delivery.md: never activated (count: 0)
    • google-api-usage-policy.md: never activated (count: 0)
    • hybrid-knowledge-retrieval.md: never activated (count: 0)
    • intent-pipeline.md: overdue since 2026-04-11 (count: 0)
    • mcp-server-setup.md: never activated (count: 0)
    • mes-3.0-extract.md: never activated (count: 0)
    • mes-3.0-validate.md: never activated (count: 0)
    • multi-expert-synthesis.md: never activated (count: 0)
    • notebooklm-usage-policy.md: never activated (count: 0)
    • notion-autofill-guide.md: never activated (count: 0)
    • notion-databases.md: overdue since 2026-05-13 (count: 1)
    • operating-principles.md: overdue since 2026-04-11 (count: 1)
    • parallel_thought.md: never activated (count: 0)
    • parallelism-cheat-sheet.md: never activated (count: 0)
    • perplexity-usage-policy.md: never activated (count: 0)
    • quality_assurance.md: never activated (count: 0)
    • quality_gate.md: overdue since 2026-04-11 (count: 452)
    • sales-conversation.md: never activated (count: 0)
    • session-end-commit.md: never activated (count: 0)
    • session-state-protocol.md: overdue since 2026-04-11 (count: 451)
    • skill-evolution-protocol.md: overdue since 2026-04-09 (count: 42)
    • skill-paths-reference.md: never activated (count: 0)
    • slash-command-playbook.md: never activated (count: 0)
    • user-state-awareness.md: overdue since 2026-05-01 (count: 0)
    • verification-agent-protocol.md: overdue since 2026-05-01 (count: 0)
    • when-to-use-deep-think.md: never activated (count: 0)
    • workflow-chains.md: never activated (count: 0)
    • workflow-gate-convention.md: overdue since 2026-06-12 (count: 0)

  ✅ ACTIVE (3):
    • feedback-ratchet.md: 2026-07-01 (chain_runner finalize for content-os-exemplars) (count: 464)
    • token-efficiency-protocol.md: 2026-04-03 (count: 2)
    • sub_agent_protocol.md: 2026-05-12 (deterministic backstop shipped — `chain_runner.py` auto-logs misses) (count: 0)
============================================================
```

### Routing Scoreboard

```text
PASS
# Routing Intelligence Dashboard

**Period**: 2026-07

No routing data yet. Data will accumulate as you use the system.

The intelligence layer logs every expert routing decision and your feedback.
Use `/rate` after expert outputs to start building your scoreboard.
```

### Registrar Status

```text
FAIL (1)
Traceback (most recent call last):
  File "/Users/farricecain/Google Antigravity/execution/session_log_registrar.py", line 30, in <module>
    from log_performance import get_local_performance_entries, log_output
ImportError: cannot import name 'get_local_performance_entries' from 'log_performance' (/Users/farricecain/Google Antigravity/execution/log_performance.py)
```

### Conversation Index Stats

```text
PASS
============================================================
📊 CONVERSATION INDEX STATS
============================================================
  Total conversations:    106
  ✅ Completed:           54
  🔄 In progress:         37
  📄 With artifacts:      94
  ⬜ Empty:               12

📂 TOP DOMAINS:
  Extraction            82  ██████████████████████████████
  System                80  ██████████████████████████████
  Content               78  ██████████████████████████████
  Strategy              63  ██████████████████████████████
  LinkedIn              61  ██████████████████████████████
  Research              21  █████████████████████
  Ghostwriting          21  █████████████████████
  Copywriting           16  ████████████████
  Video                 11  ███████████
  SEO                    5  █████

👤 TOP EXPERTS:
  Lara Acosta           27  ███████████████████████████
  Kallaway              22  ██████████████████████
  Luke Iha              18  ██████████████████
  Nicolas Cole          17  █████████████████
  Oren                  11  ███████████
  Dan Koe                9  █████████
  Nick Saraev            8  ████████
  Dai Media              7  ███████
  Cardinal Mason         7  ███████
  Samuel Thompson        6  ██████

📁 Index location: /Users/farricecain/.gemini/antigravity/brain/_index
============================================================
```
