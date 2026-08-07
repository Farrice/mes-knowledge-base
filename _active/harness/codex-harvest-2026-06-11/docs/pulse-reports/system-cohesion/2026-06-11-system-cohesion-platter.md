# Weekly System Cohesion Platter, 2026-06-11

**Generated**: 2026-06-11 10:32

## Executive Read

The cohesion spine is healthy at the proof layer.

## Route Health

| Check | Status |
|---|---|
| Control Plane | PASS |
| Autopilot Routing | PASS |
| System Health | PASS |
| Protocol Audit | PASS |
| Routing Scoreboard | PASS |
| Unused Experts | PASS |
| Silver Platter Workspace Audit | PASS |
| Activation Governor Plan | PASS |

## Misroutes This Week

# Routing Intelligence Dashboard
**Generated**: 2026-06-11 17:37 UTC
**Period**: 2026-06 (current month)

## Overview

| Metric | Value |
|--------|-------|
| Total Routings | 20 |
| Total Feedback | 0 |
| Positive Rate | 0% (0/0) |
| Negative | 0 |
| Mixed | 0 |
| Ensemble Rate | 0% (0/20) |
| Avg Intent Score | 5.0 |

## Expert Utilization

| Expert | Deployments | Positive | Negative | Mixed |
|--------|-------------|----------|----------|-------|
| antigravity-orchestrator | 20 | 0 | 0 | 0 |
| evolution-agent | 20 | 0 | 0 | 0 |

## Domain Distribution

| Domain | Requests | % of Total |
|--------|----------|------------|
| system | 20 | 100% |

## Top-Performing Ensembles

No ensemble routings recorded yet.

## Underperforming Routes

No negative or mixed feedback recorded. Either everything's working well, or feedback isn't being captured yet.

## Unused Experts

**169 agents** with

[truncated]

## Dormant Protocols

============================================================
  PROTOCOL ACTIVATION AUDIT
============================================================
  Total Protocols:    44
  Activated Ever:     11
  Active Recent:      0
  Healthy Total:      4
  Dormant:            25
  Cold/Source-Only:   8
  Overdue:            7
  Deprecated:         0
  Never Activated:    33
  Total Activations:  792
  Activation Rate:    25%
------------------------------------------------------------

  OVERDUE (review required) (7):
    - apify-usage-policy.md: overdue since 2026-05-06 (count: 0)
    - user-state-awareness.md: overdue since 2026-05-01 (count: 0)
    - verification-agent-protocol.md: overdue since 2026-05-01 (count: 0)
    - intent-pipeline.md: overdue since 2026-06-08 (count: 1)
    - notion-databases.md: overdue since 2026-05-13 (count: 1)
    - operating-principles.md: overdue since 2026-04

[truncated]

## Activation Blockers

# Activation Governor Plan

**Generated**: 2026-06-11 10:37

## Autonomy Boundary

Supervised queue/report only. This worker does not activate protocols, mark agents as used, commit performance entries, or write routing evidence.

## Local Signals

| Signal | Value | Source |
|---|---:|---|
| Performance entries | 20/20 | local performance log |
| Registrar inbox drafts | 93 | session_log_registrar |
| Registrar skipped candidates | 394 | session_log_registrar |
| Pending/local-first sync | 16 | log_performance |
| Sync failed | 4 | log_performance |
| Protocol lifecycle attention | 7 overdue / 25 dormant / 8 cold-source | protocol_tracker |
| Routing decisions | 20 | routing_intelligence |
| Negative/mixed route feedback | 0 | routing_intelligence |
| Session state | STALE | system_health |
| Gap log | DORMANT | system_health |

## Supervised Activation Queue

| ID | Priority | Queue St

[truncated]

## Pantry: Evidence Sources

- **Control-plane verifiers**: Proof spine for routing, Autopilot, skill-system, and harness health.
- **Routing Intelligence**: Shows route usage, feedback, unused experts, and ensemble capture gaps.
- **Protocol Tracker**: Separates active, dormant, stale, and never-activated protocols.
- **System Health**: Summarizes blockers such as Skill Evolution thresholds and telemetry gaps.
- **Activation Governor**: Turns dormant assets into approval-gated next actions without fake activation.

## Prep: Summaries Maintained

- **Route Health Summary**: Keeps front-door routing visible and test-backed.
- **Misroute Ledger**: Shows routes that need correction or proof.
- **Activation Summary**: Turns dormant protocols, unused experts, and blocked evolution into a supervised queue.
- **Validation Summary**: Keeps the weekly report tied to proof rather than vibes.

## Plate: What Farrice Should See

- **Operator Readout**: One scan-first readout for what is firing, what is dormant, and what to fix next.
- **Repair Queue**: Makes the system recommend the next move instead of asking Farrice to remember tools.

## Repair Queue

1. **Keep /autopilot as the tool-choice front door**: Run the routing verifiers and protect the two real-world prompts.
2. **Turn activation debt into a supervised queue**: Review activation_governor.py plan output during daily health and weekly pulse.
3. **Read one weekly system-cohesion platter**: Use the weekly pulse report as the operating readout.

## Validation Results

### Control Plane

**Status**: PASS

```text
running: golden queries
ok: golden queries (85 checks, 38.9s)
running: bridge coverage
ok: bridge coverage (14 checks, 0.0s)
running: required text
ok: required text (3 checks, 0.0s)
running: autopilot runtime preflight
ok: autopilot runtime preflight (8 checks, 12.3s)
running: local helpers
  helper running: execution/capability_graph.py --json
  helper ok: execution/capability_graph.py --json (0.5s)
  helper running: execution/outcome_recipes.py --list
  helper ok: execution/outcome_recipes.py --list (0.1s)
  helper running: execution/friction_ledger.py verify
  helper ok: execution/friction_ledger.py verify (0.1s)
  helper running: execution/run_receipt.py --verify
  helper ok: execution/run_receipt.py --verify (0.1s)
  helper running: execution/verify_operator_core_ai_employee_os.py
  helper ok: execution/verify_operator_core_ai_employee_os.py (1.8s)
  helper running: execution/verify_operator_core_fast_proof.py
  helper ok: execution/verify_operator_core_fast_proof.py (18.3s)
  helper running: execution/verify_session_state_freshness_loop.py
  helper ok: execution/verify_session_state_freshness_loop.py (0.1s)
  helper running: execution/verify_savant_control_room.py
  helper ok: execution/verify_savant_control_room.py (31.8s)
  helper running: execution/sync_global_operator_core.py --check
  helper ok: execution/sync_global_operator_core.py --check (0.1s)
  helper running: execution/verify_operator_lesson.py
  helper ok: execution/verify_operator_lesson.py (2.2s)
  helper running: execution/verify_global_autopilot_source_truth.py
  helper ok: execution/verify_global_autopilot_source_truth.py (0.0s)
  helper running: execution/sync_operator_core_orchestrate.py --check
  helper ok: execution/sync_operator_core_orchestrate.py --check (0.1s)
  helper running: execution/verify_operator_core_orchestrate.py
  helper ok: execution/verify_operator_core_orchestrate.py (9.7s)
  helper running: execution/sync_operator_core_end_session.py --check
  helper ok: execution/sync_operator_core_end_session.py --check (0.1s)
  helper running: execution/verify_operator_core_end_session.py
  helper ok: execution/verify_operator_core_end_session.py (12.0s)
  helper running: execut

[truncated]
```

### Autopilot Routing

**Status**: PASS

```text
ok: routing order
ok: research stack routing
ok: routing governor evaluation
ok: misroute feedback capture
ok: Autopilot intent-to-outcome contract
ok: Autopilot runtime preflight
ok: intent-to-outcome helpers
ok: Claude/Codex bridge policy
Autopilot routing regression checks passed.
```

### System Health

**Status**: PASS

```text
Running Antigravity System Health Check...

# Antigravity System Health Report
**Generated**: 2026-06-11 10:37

## Activation Status

| System | Status | Last Active | Entries | Health |
|--------|--------|-------------|---------|--------|
| Performance Log (Phase 1) | ACTIVE | 30 days ago | 20 | Growing |
| Skill Evolution (Phase 2) | READY - collecting evidence | — | 0 ready / 220 watch | Collecting |
| Cross-Pollination (Phase 3) | BLOCKED | — | — | Needs Phase 2 |
| Gap Detection (Phase 4) | READY | — | — | Ready |
| Session State | STALE | 18 days ago (2026-05-23 20:29) | — | Stale |
| Routing Intelligence | ACTIVE | — | 20 | Healthy |
| Gap Log | DORMANT | — | 0 | OK |

## Skill Evolution Candidates

- ready=0 watchlist=220 blocked=65 top=nicolas-cole-client-acquisition (watchlist)
- Top recommendation: `nicolas-cole-client-acquisition` (watchlist) - needs 2 more scored local entries

## Notion Sync

| Check | Status | Detail |
|-------|--------|--------|
| DNS/API preflight | network_unavailable | Use local-first evidence or run the Notion check in a network-enabled context. |
| Local performance entries | 20 | Source of truth for self-improvement when Notion is unavailable |
| Remote synced | 0 | Entries with confirmed Notion URL |
| Pending/local-first | 16 | Run `python3 execution/log_performance.py sync-pending --dry-run` before syncing |
| Sync failed | 4 | Usually sandbox DNS/network unless API error says otherwise |

## Hookify Guards

| Hook | Enabled | Event | Action |
|------|---------|-------|--------|
| fal-budget-check | Yes | bash | warn |
| freshness-tax-enforcement | Yes | stop | warn |
| intent-pipeline-check | Yes | stop | warn |
| notion-api-guard | Yes | bash | block |
| performance-log-reminder | Yes | stop | warn |
| perplexity-budget-check | Yes | bash | warn |
| quality-gate-enforcement | Yes | stop | warn |
| session-state-reminder | Yes | stop | warn |

## Cascade Dependencies

```
Performance Log (20 entries)
  └─> Skill Evolution (needs 20+) READY - collecting evidence
        └─> Cross-Pollination (needs evolution data) [waiting]
              └─> Gap Detection (monthly) READY
```

## Recommended Actions

1. **READY**: Skill E

[truncated]
```

### Protocol Audit

**Status**: PASS

```text
============================================================
  PROTOCOL ACTIVATION AUDIT
============================================================
  Total Protocols:    44
  Activated Ever:     11
  Active Recent:      0
  Healthy Total:      4
  Dormant:            25
  Cold/Source-Only:   8
  Overdue:            7
  Deprecated:         0
  Never Activated:    33
  Total Activations:  792
  Activation Rate:    25%
------------------------------------------------------------

  OVERDUE (review required) (7):
    - apify-usage-policy.md: overdue since 2026-05-06 (count: 0)
    - user-state-awareness.md: overdue since 2026-05-01 (count: 0)
    - verification-agent-protocol.md: overdue since 2026-05-01 (count: 0)
    - intent-pipeline.md: overdue since 2026-06-08 (count: 1)
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
    - quality_assurance

[truncated]
```

### Routing Scoreboard

**Status**: PASS

```text
# Routing Intelligence Dashboard
**Generated**: 2026-06-11 17:37 UTC
**Period**: 2026-06 (current month)

## Overview

| Metric | Value |
|--------|-------|
| Total Routings | 20 |
| Total Feedback | 0 |
| Positive Rate | 0% (0/0) |
| Negative | 0 |
| Mixed | 0 |
| Ensemble Rate | 0% (0/20) |
| Avg Intent Score | 5.0 |

## Expert Utilization

| Expert | Deployments | Positive | Negative | Mixed |
|--------|-------------|----------|----------|-------|
| antigravity-orchestrator | 20 | 0 | 0 | 0 |
| evolution-agent | 20 | 0 | 0 | 0 |

## Domain Distribution

| Domain | Requests | % of Total |
|--------|----------|------------|
| system | 20 | 100% |

## Top-Performing Ensembles

No ensemble routings recorded yet.

## Underperforming Routes

No negative or mixed feedback recorded. Either everything's working well, or feedback isn't being captured yet.

## Unused Experts

**169 agents** with zero deployments (all-time):

- `adam-enfroy` (Adam Enfroy)
- `ai-carousel-content-engine` (Ai Carousel Content Engine)
- `ai-chris-lee` (Ai Chris Lee)
- `alen-sultanic` (Alen Sultanic)
- `alex-content-science` (Alex Content Science)
- `alex-copper` (Alex Copper)
- `ali-abdaal` (Ali Abdaal)
- `andrew-dun` (Andrew Dun)
- `andrew-wilkinson` (Andrew Wilkinson)
- `andy-lo` (Andy Lo)
- `anne-lamott` (Anne Lamott)
- `april-dunford` (April Dunford)
- `ash-maurya` (Ash Maurya)
- `attention-hijack-hooks` (Attention Hijack Hooks)
- `authority-hacker` (Authority Hacker)
- `bond-halbert` (Bond Halbert)
- `brandon-jacoby` (Brandon Jacoby)
- `brock-johnson` (Brock Johnson)
- `caleb-ralston` (Caleb Ralston)
- `cardinal-mason` (Cardinal Mason)
- `cheri-tree` (Cheri Tree)
- `chris-cimorelli` (Chris Cimorelli)
- `client-delivery-agent` (Client Delivery Agent)
- `content-media-agent` (Content Media Agent)
- `copywriting-agent` (Copywriting Agent)
- `creative-design-agent` (Creative Design Agent)
- `creative-director` (Creative Director)
- `dai-media` (Dai Media)
- `dan-koe` (Dan Koe)
- `dan-martell` (Dan Martell)
- ... and 139 more

## Suggestions

- **Low feedback rate**: Only 0/20 routings have feedback (0%). Use `/rate` more often to improve insights.
```

### Unused Experts

**Status**: PASS

```text
**169 agents** with zero deployments (all-time):

- `adam-enfroy` (Adam Enfroy)
- `ai-carousel-content-engine` (Ai Carousel Content Engine)
- `ai-chris-lee` (Ai Chris Lee)
- `alen-sultanic` (Alen Sultanic)
- `alex-content-science` (Alex Content Science)
- `alex-copper` (Alex Copper)
- `ali-abdaal` (Ali Abdaal)
- `andrew-dun` (Andrew Dun)
- `andrew-wilkinson` (Andrew Wilkinson)
- `andy-lo` (Andy Lo)
- `anne-lamott` (Anne Lamott)
- `april-dunford` (April Dunford)
- `ash-maurya` (Ash Maurya)
- `attention-hijack-hooks` (Attention Hijack Hooks)
- `authority-hacker` (Authority Hacker)
- `bond-halbert` (Bond Halbert)
- `brandon-jacoby` (Brandon Jacoby)
- `brock-johnson` (Brock Johnson)
- `caleb-ralston` (Caleb Ralston)
- `cardinal-mason` (Cardinal Mason)
- `cheri-tree` (Cheri Tree)
- `chris-cimorelli` (Chris Cimorelli)
- `client-delivery-agent` (Client Delivery Agent)
- `content-media-agent` (Content Media Agent)
- `copywriting-agent` (Copywriting Agent)
- `creative-design-agent` (Creative Design Agent)
- `creative-director` (Creative Director)
- `dai-media` (Dai Media)
- `dan-koe` (Dan Koe)
- `dan-martell` (Dan Martell)
- ... and 139 more
```

### Silver Platter Workspace Audit

**Status**: PASS

```text
{
  "mode": "audit-existing",
  "detections": {
    "claude_md": {
      "exists": true,
      "lines": 397,
      "path": "CLAUDE.md"
    },
    "codex_authority": {
      "codex_md": true,
      "agents_md": true,
      "active_workflow_count": 1068,
      "command_skill_count": 41
    },
    "settings_json": {
      "exists": false,
      "has_hooks": false
    },
    "claude_skills": {
      "count": 5,
      "names": [
        "higgsfield-generate",
        "higgsfield-marketplace-cards",
        "higgsfield-product-photoshoot",
        "higgsfield-soul-id",
        "impeccable"
      ]
    },
    "codex_root_skills": {
      "count": 256,
      "names": [
        "adam-enfroy-affiliate-marketing",
        "ai-carousel-content-engine",
        "ai-chris-lee-zero-testimonial-sales",
        "alen-sultanic-copywriting",
        "alex-content-science",
        "alex-copper-creative-strategy",
        "algorithmic-art",
        "ali-abdaal-action-bias",
        "andreessen-horowitz-new-media",
        "andrew-dun-vibe-consulting",
        "andrew-wilkinson-ai-entrepreneurship",
        "andy-lo-premium-websites",
        "april-dunford-positioning",
        "ash-maurya-founder-systems",
        "asset_generator",
        "attention-hijack-hooks",
        "authority-hacker-ai-social-media",
        "bond-halbert-copywriting",
        "boris-claude-code",
        "brand-guidelines",
        "brandon-jacoby-taste-mastery",
        "brock-johnson-shareworthy-content",
        "business-intelligence-audit",
        "caleb-ralston-personal-brand",
        "canvas-design",
        "cardinal-mason-ai-copywriting",
        "cheri-tree-bank-buyology",
        "chris-cimorelli-copywriting",
        "cinematic-documentary",
        "consumer-posture-research",
        "creative-assembly",
        "creative-campaign-strategy",
        "creative-direction",
        "dai-media-consumer-posture",
        "dan-koe-ai-leverage",
        "dan-koe-multipassionate-mastery",
        "dan-martell-business-scaling",
        "dan-wang-literary-analysis",
        "daniel-priestley-24-assets-os",
        "daniel-priestley-oversubscribed",
        "darrel-wilson-ai-affiliate",
        "da

[truncated]
```

### Activation Governor Plan

**Status**: PASS

```text
# Activation Governor Plan

**Generated**: 2026-06-11 10:37

## Autonomy Boundary

Supervised queue/report only. This worker does not activate protocols, mark agents as used, commit performance entries, or write routing evidence.

## Local Signals

| Signal | Value | Source |
|---|---:|---|
| Performance entries | 20/20 | local performance log |
| Registrar inbox drafts | 93 | session_log_registrar |
| Registrar skipped candidates | 394 | session_log_registrar |
| Pending/local-first sync | 16 | log_performance |
| Sync failed | 4 | log_performance |
| Protocol lifecycle attention | 7 overdue / 25 dormant / 8 cold-source | protocol_tracker |
| Routing decisions | 20 | routing_intelligence |
| Negative/mixed route feedback | 0 | routing_intelligence |
| Session state | STALE | system_health |
| Gap log | DORMANT | system_health |

## Supervised Activation Queue

| ID | Priority | Queue State | Title | Evidence | Proposed Action |
|---|---|---|---|---|---|
| `ag_80d991b53ea1` | MEDIUM | already-queued | Clarify local-first performance sync status | Local JSONL remains the source of truth while remote sync is unavailable or unapproved. | Run a sync dry-run and record whether blockers are network, API, or approval-related. Do not auto-sync external systems. |
| `ag_098e70e9e1b2` | MEDIUM | already-queued | Refresh session state capture | Last updated: 18 days ago (2026-05-23 20:29) | Use the next real closeout to refresh session state and verify the registrar sees it. |
| `ag_8795f7da9b97` | MEDIUM | already-queued | Review registrar inbox before new automation | Uncertain performance candidates are waiting in .agent/performance-log-inbox.jsonl. | Approve, revise, or discard inbox drafts one by one. Keep ambiguous candidates out of committed performance evidence. |
| `ag_0d77e021d9f1` | MEDIUM | already-queued | Triage dormant protocols into a top-five activation plan | Leverage-ranked candidates: agent-loading-protocol.md (selecting or loading expert/skill context), expert_auto_routin... | Use `.agent/protocol-activation-plan.md` as the supervised trigger list. Do not activate every dormant protocol. |
| `ag_48b1085848a8` | LOW | already-queued | Queue gap detectio

[truncated]
```

## Next Week's One Move

Use the activation queue to turn the highest-value dormant asset into a real routed run.
