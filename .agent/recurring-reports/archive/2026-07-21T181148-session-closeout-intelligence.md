# Session Closeout Intelligence

**Generated**: 2026-07-21 18:11
**Mode**: write

## Performance Registrar

```text
FAIL (1)
Traceback (most recent call last):
  File "/Users/farricecain/Google Antigravity/execution/session_log_registrar.py", line 636, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "/Users/farricecain/Google Antigravity/execution/session_log_registrar.py", line 623, in main
    return cmd_register(args)
           ^^^^^^^^^^^^^^^^^^
  File "/Users/farricecain/Google Antigravity/execution/session_log_registrar.py", line 485, in cmd_register
    state, reason = route_candidate(candidate, args.dry_run)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/farricecain/Google Antigravity/execution/session_log_registrar.py", line 445, in route_candidate
    commit_candidate(candidate, dry_run)
  File "/Users/farricecain/Google Antigravity/execution/session_log_registrar.py", line 416, in commit_candidate
    return log_output(
           ^^^^^^^^^^^
TypeError: log_output() got an unexpected keyword argument 'lane'
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
**Generated**: 2026-07-21 18:11

## Activation Status

| System | Status | Last Active | Entries | Health |
|--------|--------|-------------|---------|--------|
| Performance Log (Phase 1) | ACTIVE | Today | 100 | Healthy |
| Skill Evolution (Phase 2) | READY | — | — | Ready |
| Cross-Pollination (Phase 3) | BLOCKED | — | — | Needs Phase 2 |
| Gap Detection (Phase 4) | READY | — | — | Ready |
| Session State | ACTIVE | Today (2026-07-21 16:43) | — | Healthy |
| Routing Intelligence | ACTIVE | — | 576 | Healthy |
| Gap Log | ACTIVE | — | 3 | Healthy |
| Sovereign Memory | ACTIVE | — | 5423 | Healthy |

## Sovereign Memory

- **Total memories**: 5423 (91 pinned, 5385 embedded — 99.3% coverage)
- **By tier**: episodic=5182, procedural=107, semantic=134
- **By workspace**: (global)=1812, claude-export=3611
- **Notion mirror**: 941 pages, last mirrored 16.19h ago (OK)
- **Latest backup**: 15.19h ago (OK)
- **⚠ Flagged for review**: 6 pending — run `python3 execution/memory_review.py list`

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
- **Would-blocks last 7d**: 337
- ⚠ 337 unenforced finalize debts this week — revisit the observe-mode decision if this stays high

## Cascade Dependencies

```
Performance Log (100 entries)
  └─> Skill Evolution (needs 20+) READY
        └─> Cross-Pollination (needs evolution data) [waiting]
              └─> Gap Detection (monthly) READY
```

## Recommended Actions

1. **READY**: Run `/skill-evolution` to start the first Skill Evolution cycle.
2. **REVIEW**: 6 distilled memories awaiting human approval. Run `python3 execution/memory_review.py list`.
```

### Skill Evolution Candidates

```text
PASS
# Skill Evolution Candidate Status

ready=0 watchlist=350 blocked=48 top=maria-wendt-digital-products (watchlist)
```

### Protocol Audit

```text
PASS
============================================================
  PROTOCOL ACTIVATION AUDIT
============================================================
  Total Protocols:    48
  Activated Ever:     15
  Active Recent:      3
  Healthy Total:      8
  Dormant:            25
  Cold/Source-Only:   8
  Overdue:            7
  Deprecated:         0
  Never Activated:    33
  Total Activations:  2188
  Activation Rate:    31%
------------------------------------------------------------

  OVERDUE (review required) (7):
    - apify-usage-policy.md: overdue since 2026-05-06 (count: 0)
    - user-state-awareness.md: overdue since 2026-05-01 (count: 0)
    - verification-agent-protocol.md: overdue since 2026-05-01 (count: 0)
    - workflow-gate-convention.md: overdue since 2026-06-12 (count: 0)
    - notion-databases.md: overdue since 2026-05-13 (count: 1)
    - operating-principles.md: overdue since 2026-04-11 (count: 1)
    - skill-evolution-protocol.md: overdue since 2026-04-09 (count: 42)

  DORMANT (never activated) (25):
    - agent-loading-protocol.md: *Not yet activated* (count: 0)
    - ai-slop-detector.md: *Not yet activated* (count: 0)
    - collaboration-protocol.md: *Not yet activated* (count: 0)
    - content-creation.md: *Not yet activated* (count: 0)
    - content_creation_gate.md: *Not yet activated* (count: 0)
    - cross-pollination.md: *Not yet activated* (count: 0)
    - daily-council.md: *Not yet activated* (count: 0)
    - decision-council.md: *Not yet activated* (count: 0)
    - deep_self_annealing.md: *Not yet activated* (count: 0)
    - expert_auto_routing.md: *Not yet activated* (count: 0)
    - expertise-gap-protocol.md: *Not yet activated* (count: 0)
    - extraction-to-skill.md: *Not yet activated* (count: 0)
    - extraction-workflow.md: *Not yet activated* (count: 0)
    - ghostwriting-delivery.md: *Not yet activated* (count: 0)
    - hybrid-knowledge-retrieval.md: *Not yet activated* (count: 0)
    - mes-3.0-extract.md: *Not yet activated* (count: 0)
    - mes-3.0-validate.md: *Not yet activated* (count: 0)
    - multi-expert-synthesis.md: *Not yet activated* (count: 0)
    - parallel_thought.md: *Not yet activated* (count: 0)
    - quality_assurance.md: *Not yet activated* (count: 0)
    - sales-conversation.md: *Not yet activated* (count: 0)
    - session-end-commit.md: *Not yet activated* (count: 0)
    - task-lifecycle-content.md: *Not yet activated* (count: 0)
    - when-to-use-deep-think.md: unknown (count: 0)
    - workflow-chains.md: *Not yet activated* (count: 0)

  COLD/SOURCE-ONLY (8):
    - google-api-usage-policy.md: *Not yet activated — pending Phase 0 browser setup* (count: 0)
    - mcp-server-setup.md: *Not yet activated* (count: 0)
    - notebooklm-usage-policy.md: *Not yet activated* (count: 0)
    - notion-autofill-guide.md: unknown (count: 0)
    - parallelism-cheat-sheet.md: *Not yet activated* (count: 0)
    - perplexity-usage-policy.md: *Not yet activated* (count: 0)
    - skill-paths-reference.md: *Not yet activated* (count: 0)
    - slash-command-playbook.md: unknown (count: 0)

  ACTIVE RECENT (3):
    - feedback-ratchet.md: 2026-07-21 (chain_runner finalize for expert-assembly-os) (count: 721)
    - session-state-protocol.md: 2026-07-21 (chain_runner session checkpoint) (count: 709)
    - quality_gate.md: 2026-07-21 (chain_runner finalize for expert-assembly-os) (count: 709)

  HEALTHY (5):
    - token-efficiency-protocol.md: 2026-04-03 (count: 2)
    - skill-craft-standard.md: 2026-07-06 (authored) (count: 1)
    - intent-pipeline.md: 2026-07-06 (codex parity verifier run) (count: 1)
    - embodiment-standard.md: 2026-07-02 (E4 ship — standard created and wired into both extraction routes + validator) (count: 1)
    - sub_agent_protocol.md: 2026-05-12 (deterministic backstop shipped — `chain_runner.py` auto-logs misses) (count: 0)
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

- Committed local performance entries: 89
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
