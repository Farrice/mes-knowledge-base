# Session Closeout Intelligence

**Generated**: 2026-07-16 15:39
**Mode**: write

## Performance Registrar

```text
PASS
| State | Confidence | Lane | Type | Workflow | Title | Reason |
|---|---:|---|---|---|---|---|
| inbox | 0.62 | System | System | autopilot | Session Closeout Intelligence | recurring report needs review before becoming performance evidence |
| inbox | 0.62 | System | System | autopilot | Session Closeout Intelligence | recurring report needs review before becoming performance evidence |
| inbox | 0.62 | System | System | autopilot | Session Closeout Intelligence | recurring report needs review before becoming performance evidence |
| inbox | 0.62 | System | System | autopilot | Session Closeout Intelligence | recurring report needs review before becoming performance evidence |
| inbox | 0.62 | System | System | autopilot | Session Closeout Intelligence | recurring report needs review before becoming performance evidence |
| inbox | 0.62 | System | System | autopilot | Session Closeout Intelligence | recurring report needs review before becoming performance evidence |
| inbox | 0.62 | System | System | autopilot | Session Closeout Intelligence | recurring report needs review before becoming performance evidence |
| inbox | 0.62 | System | System | autopilot | Session Closeout Intelligence | recurring report needs review before becoming performance evidence |
| inbox | 0.62 | System | System | autopilot | Session Closeout Intelligence | recurring report needs review before becoming performance evidence |
| skipped | 0.62 | System | System | autopilot | Session Closeout Intelligence | already in inbox as draft_ca529e7015f79f90 |

Summary: committed=0 inbox=9 skipped=1
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
**Generated**: 2026-07-16 15:39

## Activation Status

| System | Status | Last Active | Entries | Health |
|--------|--------|-------------|---------|--------|
| Performance Log (Phase 1) | ACTIVE | Today | 100 | Healthy |
| Skill Evolution (Phase 2) | READY | — | — | Ready |
| Cross-Pollination (Phase 3) | BLOCKED | — | — | Needs Phase 2 |
| Gap Detection (Phase 4) | READY | — | — | Ready |
| Session State | ACTIVE | Today (2026-07-16 12:01) | — | Healthy |
| Routing Intelligence | ACTIVE | — | 373 | Healthy |
| Gap Log | ACTIVE | — | 2 | Healthy |
| Sovereign Memory | ACTIVE | — | 5196 | Healthy |

## Sovereign Memory

- **Total memories**: 5196 (91 pinned, 5165 embedded — 99.4% coverage)
- **By tier**: episodic=4965, procedural=107, semantic=124
- **By workspace**: (global)=1585, claude-export=3611
- **Notion mirror**: 822 pages, last mirrored 13.66h ago (OK)
- **Latest backup**: 12.66h ago (OK)

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

## Finalize Gate

- **Mode**: observe (Farrice 2026-07-02: observe; flip via LEDGER_ENFORCE=1)
- **Would-blocks last 7d**: 156
- ⚠ 156 unenforced finalize debts this week — revisit the observe-mode decision if this stays high

## Cascade Dependencies

```
Performance Log (100 entries)
  └─> Skill Evolution (needs 20+) READY
        └─> Cross-Pollination (needs evolution data) [waiting]
              └─> Gap Detection (monthly) READY
```

## Recommended Actions

1. **READY**: Run `/skill-evolution` to start the first Skill Evolution cycle.
```

### Skill Evolution Candidates

```text
PASS
# Skill Evolution Candidate Status

ready=0 watchlist=325 blocked=57 top=maria-wendt-digital-products (watchlist)
```

### Protocol Audit

```text
PASS
============================================================
  PROTOCOL ACTIVATION AUDIT
============================================================
  Total Protocols:    47
  Active:             15
  Never Activated:    32
  Zombies (overdue):  39
  Total Activations:  1951
  Activation Rate:    32%
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
    • sales-conversation.md: never activated (count: 0)
    • session-end-commit.md: never activated (count: 0)
    • skill-evolution-protocol.md: overdue since 2026-04-09 (count: 42)
    • skill-paths-reference.md: never activated (count: 0)
    • slash-command-playbook.md: never activated (count: 0)
    • user-state-awareness.md: overdue since 2026-05-01 (count: 0)
    • verification-agent-protocol.md: overdue since 2026-05-01 (count: 0)
    • when-to-use-deep-think.md: never activated (count: 0)
    • workflow-chains.md: never activated (count: 0)
    • workflow-gate-convention.md: overdue since 2026-06-12 (count: 0)

  ✅ ACTIVE (8):
    • feedback-ratchet.md: 2026-07-16 (chain_runner finalize for tommy-clark-linkedin-growth) (count: 642)
    • quality_gate.md: 2026-07-16 (chain_runner finalize for tommy-clark-linkedin-growth) (count: 630)
    • session-state-protocol.md: 2026-07-16 (chain_runner session checkpoint) (count: 630)
    • token-efficiency-protocol.md: 2026-04-03 (count: 2)
    • embodiment-standard.md: 2026-07-02 (E4 ship — standard created and wired into both extraction routes + validator) (count: 1)
    • intent-pipeline.md: 2026-07-06 (codex parity verifier run) (count: 1)
    • skill-craft-standard.md: 2026-07-06 (authored) (count: 1)
    • sub_agent_protocol.md: 2026-05-12 (deterministic backstop shipped — `chain_runner.py` auto-logs misses) (count: 0)
============================================================
```

### Routing Scoreboard

```text
FAIL (1)
Traceback (most recent call last):
  File "/Users/farricecain/Google Antigravity/execution/routing_intelligence.py", line 722, in <module>
    main()
  File "/Users/farricecain/Google Antigravity/execution/routing_intelligence.py", line 688, in main
    print(generate_scoreboard())
          ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/farricecain/Google Antigravity/execution/routing_intelligence.py", line 530, in generate_scoreboard
    top_combinations(data),
    ^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/farricecain/Google Antigravity/execution/routing_intelligence.py", line 438, in top_combinations
    ensembles[pairing][rating] += 1
    ~~~~~~~~~~~~~~~~~~^^^^^^^^
KeyError: 'auto_miss'
```

### Registrar Status

```text
PASS
# Session Log Registrar Status

- Committed local performance entries: 14
- Auto/promoted registrar entries: 0
- Inbox drafts: 9
- Skipped duplicate/low-confidence candidates: 1
- Next review: `python3 execution/session_log_registrar.py inbox`
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
