# Session Closeout Intelligence

**Generated**: 2026-07-02 22:51
**Mode**: write

## Performance Registrar

```text
FAIL (1)
Traceback (most recent call last):
  File "/Users/farricecain/Google Antigravity/execution/session_log_registrar.py", line 30, in <module>
    from log_performance import get_local_performance_entries, log_output
  File "/Users/farricecain/Google Antigravity/execution/log_performance.py", line 45, in <module>
    from dotenv import load_dotenv
ModuleNotFoundError: No module named 'dotenv'
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
FAIL (1)
Traceback (most recent call last):
  File "/Users/farricecain/Google Antigravity/execution/system_health.py", line 31, in <module>
    from dotenv import load_dotenv
ModuleNotFoundError: No module named 'dotenv'
```

### Skill Evolution Candidates

```text
PASS
# Skill Evolution Candidate Status

ready=0 watchlist=318 blocked=61 top=maria-wendt-digital-products (watchlist)
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
  Total Activations:  1565
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
    • feedback-ratchet.md: 2026-07-02 (chain_runner finalize for jen-santulan-listing-content) (count: 514)
    • quality_gate.md: 2026-07-02 (chain_runner finalize for jen-santulan-listing-content) (count: 502)
    • session-state-protocol.md: 2026-07-02 (chain_runner session checkpoint) (count: 502)
    • token-efficiency-protocol.md: 2026-04-03 (count: 2)
    • embodiment-standard.md: 2026-07-02 (E4 ship — standard created and wired into both extraction routes + validator) (count: 1)
    • sub_agent_protocol.md: 2026-05-12 (deterministic backstop shipped — `chain_runner.py` auto-logs misses) (count: 0)
============================================================
```

### Routing Scoreboard

```text
PASS
# Routing Intelligence Dashboard
**Generated**: 2026-07-03 05:51 UTC
**Period**: 2026-07 (current month)

## Overview

| Metric | Value |
|--------|-------|
| Total Routings | 39 |
| Total Feedback | 0 |
| Positive Rate | 0% (0/0) |
| Negative | 0 |
| Mixed | 0 |
| Ensemble Rate | 28% (11/39) |
| Avg Intent Score | 6.1 |

## Expert Utilization

| Expert | Deployments | Positive | Negative | Mixed |
|--------|-------------|----------|----------|-------|
| jen-santulan-listing-content | 14 | 0 | 0 | 0 |
| system-audit | 13 | 0 | 0 | 0 |
| strength-conditioning-os | 2 | 0 | 0 | 0 |
| chief-of-staff-os | 2 | 0 | 0 | 0 |
| david-placek | 2 | 0 | 0 | 0 |
| jen-santulan | 2 | 0 | 0 | 0 |
| nicolas-cole | 1 | 0 | 0 | 0 |
| source-to-skill-system | 1 | 0 | 0 | 0 |
| founder-voice | 1 | 0 | 0 | 0 |
| David Placek | 1 | 0 | 0 | 0 |

## Domain Distribution

| Domain | Requests | % of Total |
|--------|----------|------------|
| Content | 16 | 41% |
| System | 12 | 31% |
| Client Work | 4 | 10% |
| Analysis | 4 | 10% |
| Strategy | 1 | 3% |
| Creative | 1 | 3% |
| Legal Consult Prep | 1 | 3% |

## Top-Performing Ensembles

| Pairing | Uses | Positive | Negative | Mixed |
|---------|------|----------|----------|-------|
| system-audit | 5 | 0 | 0 | 0 |
| strength-conditioning-os | 2 | 0 | 0 | 0 |
| chief-of-staff-os | 2 | 0 | 0 | 0 |
| jen-santulan | 2 | 0 | 0 | 0 |

## Underperforming Routes

No negative feedback recorded. Either everything's working well, or feedback isn't being captured yet.

## Unused Experts

**215 agents** with zero deployments (all-time):

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
- ... and 185 more

## Suggestions

- **Low feedback rate**: Only 0/39 routings have feedback (0%). Use `/rate` more often to improve insights.
```

### Registrar Status

```text
FAIL (1)
Traceback (most recent call last):
  File "/Users/farricecain/Google Antigravity/execution/session_log_registrar.py", line 30, in <module>
    from log_performance import get_local_performance_entries, log_output
  File "/Users/farricecain/Google Antigravity/execution/log_performance.py", line 45, in <module>
    from dotenv import load_dotenv
ModuleNotFoundError: No module named 'dotenv'
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
