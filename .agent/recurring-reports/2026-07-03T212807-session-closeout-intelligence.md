# Session Closeout Intelligence

**Generated**: 2026-07-03 21:28
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
**Generated**: 2026-07-03 21:28

## Activation Status

| System | Status | Last Active | Entries | Health |
|--------|--------|-------------|---------|--------|
| Performance Log (Phase 1) | ERROR | Error | 0 | Unknown |
| Skill Evolution (Phase 2) | BLOCKED (0/20 entries) | — | — | Waiting |
| Cross-Pollination (Phase 3) | BLOCKED | — | — | Needs Phase 2 |
| Gap Detection (Phase 4) | BLOCKED | — | — | Needs data |
| Session State | ACTIVE | Today (2026-07-03 21:27) | — | Healthy |
| Routing Intelligence | ACTIVE | — | 54 | Healthy |
| Gap Log | ACTIVE | — | 1 | Healthy |
| Sovereign Memory | ACTIVE | — | 4809 | Healthy |

## Sovereign Memory

- **Total memories**: 4809 (88 pinned, 4772 embedded — 99.2% coverage)
- **By tier**: episodic=4608, procedural=107, semantic=94
- **By workspace**: (global)=1197, claude-export=3612
- **Notion mirror**: 633 pages, last mirrored 19.47h ago (OK)
- **Latest backup**: 18.47h ago (OK)
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
- **Would-blocks last 7d**: 104
- ⚠ 104 unenforced finalize debts this week — revisit the observe-mode decision if this stays high

## Cascade Dependencies

```
Performance Log (0 entries)
  └─> Skill Evolution (needs 20+) [0/20]
        └─> Cross-Pollination (needs evolution data) [waiting]
              └─> Gap Detection (monthly) [waiting]
```

## Recommended Actions

1. **CRITICAL**: Start logging performance entries. Run the Quality Gate after your next expert-driven output, then log with `python execution/log_performance.py log "description" --skill X --type Y --quality N --status Keep`
2. **REVIEW**: 6 distilled memories awaiting human approval. Run `python3 execution/memory_review.py list`.
```

### Skill Evolution Candidates

```text
PASS
# Skill Evolution Candidate Status

ready=0 watchlist=318 blocked=58 top=maria-wendt-digital-products (watchlist)
```

### Protocol Audit

```text
PASS
============================================================
  PROTOCOL ACTIVATION AUDIT
============================================================
  Total Protocols:    46
  Active:             14
  Never Activated:    32
  Zombies (overdue):  40
  Total Activations:  1610
  Activation Rate:    30%
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

  ✅ ACTIVE (6):
    • feedback-ratchet.md: 2026-07-03 (chain_runner finalize for creative-direction) (count: 529)
    • quality_gate.md: 2026-07-03 (chain_runner finalize for creative-direction) (count: 517)
    • session-state-protocol.md: 2026-07-03 (chain_runner session checkpoint) (count: 517)
    • token-efficiency-protocol.md: 2026-04-03 (count: 2)
    • embodiment-standard.md: 2026-07-02 (E4 ship — standard created and wired into both extraction routes + validator) (count: 1)
    • sub_agent_protocol.md: 2026-05-12 (deterministic backstop shipped — `chain_runner.py` auto-logs misses) (count: 0)
============================================================
```

### Routing Scoreboard

```text
PASS
# Routing Intelligence Dashboard
**Generated**: 2026-07-04 04:28 UTC
**Period**: 2026-07 (current month)

## Overview

| Metric | Value |
|--------|-------|
| Total Routings | 54 |
| Total Feedback | 0 |
| Positive Rate | 0% (0/0) |
| Negative | 0 |
| Mixed | 0 |
| Ensemble Rate | 26% (14/54) |
| Avg Intent Score | 5.5 |

## Expert Utilization

| Expert | Deployments | Positive | Negative | Mixed |
|--------|-------------|----------|----------|-------|
| system-audit | 15 | 0 | 0 | 0 |
| jen-santulan-listing-content | 14 | 0 | 0 | 0 |
| creative-direction | 6 | 0 | 0 | 0 |
| jen-santulan | 3 | 0 | 0 | 0 |
| strength-conditioning-os | 2 | 0 | 0 | 0 |
| chief-of-staff-os | 2 | 0 | 0 | 0 |
| david-placek | 2 | 0 | 0 | 0 |
| health-performance-geo-client-acquisition-engine | 2 | 0 | 0 | 0 |
| deep-research | 2 | 0 | 0 | 0 |
| nicolas-cole | 1 | 0 | 0 | 0 |
| source-to-skill-system | 1 | 0 | 0 | 0 |
| founder-voice | 1 | 0 | 0 | 0 |
| David Placek | 1 | 0 | 0 | 0 |
| nate-b-jones-orchestration-intelligence | 1 | 0 | 0 | 0 |
| source-command-mission | 1 | 0 | 0 | 0 |

## Domain Distribution

| Domain | Requests | % of Total |
|--------|----------|------------|
| Content | 19 | 35% |
| System | 14 | 26% |
| Creative | 7 | 13% |
| Strategy | 5 | 9% |
| Client Work | 4 | 7% |
| Analysis | 4 | 7% |
| Legal Consult Prep | 1 | 2% |

## Top-Performing Ensembles

| Pairing | Uses | Positive | Negative | Mixed |
|---------|------|----------|----------|-------|
| system-audit | 5 | 0 | 0 | 0 |
| strength-conditioning-os | 2 | 0 | 0 | 0 |
| chief-of-staff-os | 2 | 0 | 0 | 0 |
| jen-santulan | 3 | 0 | 0 | 0 |
| nate-b-jones-orchestration-intelligence | 1 | 0 | 0 | 0 |
| source-command-mission | 1 | 0 | 0 | 0 |

## Underperforming Routes

No negative feedback recorded. Either everything's working well, or feedback isn't being captured yet.

## Unused Experts

**214 agents** with zero deployments (all-time):

- `adam-enfroy` (Adam Enfroy)
- `ai-chris-lee` (Ai Chris Lee)
- `alan-aragon` (Alan Aragon)
- `alen-sultanic` (Alen Sultanic)
- `alex-content-science` (Alex Content Science)
- `alex-copper` (Alex Copper)
- `alex-hormozi` (Alex Hormozi)
- `alex-m-smith` (Alex M Smith)
- `alex-myatt` (Alex Myatt)
- `alex-suzuki` (Alex Suzuki)
- `alex-suzuki-revenue-architect` (Alex Suzuki Revenue Architect)
- `ali-abdaal` (Ali Abdaal)
- `andrew-dun` (Andrew Dun)
- `andrew-lane` (Andrew Lane)
- `andrew-stanton` (Andrew Stanton)
- `andrew-wilkinson` (Andrew Wilkinson)
- `andy-galpin` (Andy Galpin)
- `andy-lo` (Andy Lo)
- `anne-lamott` (Anne Lamott)
- `anne-lamott-neal-allen` (Anne Lamott Neal Allen)
- `april-dunford` (April Dunford)
- `ash-maurya` (Ash Maurya)
- `authority-hacker` (Authority Hacker)
- `benjamin-hardy` (Benjamin Hardy)
- `bill-browder` (Bill Browder)
- `bitbranding` (Bitbranding)
- `bond-halbert` (Bond Halbert)
- `boris` (Boris)
- `brad-bonanno` (Brad Bonanno)
- `brendan-kane` (Brendan Kane)
- ... and 184 more

## Suggestions

- **Low feedback rate**: Only 0/54 routings have feedback (0%). Use `/rate` more often to improve insights.
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
