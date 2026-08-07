# Weekly System Cohesion Platter, 2026-05-11

**Generated**: 2026-05-11 11:59

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
**Generated**: 2026-05-11 18:59 UTC
**Period**: 2026-05 (current month)

## Overview

| Metric | Value |
|--------|-------|
| Total Routings | 23 |
| Total Feedback | 12 |
| Positive Rate | 67% (8/12) |
| Negative | 4 |
| Mixed | 0 |
| Ensemble Rate | 0% (0/23) |
| Avg Intent Score | 4.0 |

## Expert Utilization

| Expert | Deployments | Positive | Negative | Mixed |
|--------|-------------|----------|----------|-------|
| antigravity-orchestrator | 23 | 8 | 4 | 0 |
| evolution-agent | 6 | 0 | 0 | 0 |

## Domain Distribution

| Domain | Requests | % of Total |
|--------|----------|------------|
| system | 13 | 57% |
| unknown | 5 | 22% |
| routing | 2 | 9% |
| copy | 1 | 4% |
| other | 1 | 4% |
| copy-quality | 1 | 4% |

## Top-Performing Ensembles

No ensemble routings recorded yet.

## Underperforming Routes

| Rating | Workflow | Expert(s) | Domain | C

[truncated]

## Dormant Protocols

============================================================
  PROTOCOL ACTIVATION AUDIT
============================================================
  Total Protocols:    44
  Active:             11
  Never Activated:    33
  Zombies (overdue):  38
  Total Activations:  783
  Activation Rate:    25%
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
    • decision-council.md: never activated (coun

[truncated]

## Activation Blockers

# Activation Governor Plan

**Generated**: 2026-05-11 11:59

## Autonomy Boundary

Supervised queue/report only. This worker does not activate protocols, mark agents as used, commit performance entries, or write routing evidence.

## Local Signals

| Signal | Value | Source |
|---|---:|---|
| Performance entries | 17/20 | local performance log |
| Registrar inbox drafts | 30 | session_log_registrar |
| Registrar skipped candidates | 172 | session_log_registrar |
| Pending/local-first sync | 13 | log_performance |
| Sync failed | 4 | log_performance |
| Protocol zombies | 38 | protocol_tracker |
| Routing decisions | 23 | routing_intelligence |
| Negative/mixed route feedback | 4 | routing_intelligence |
| Session state | ACTIVE | system_health |
| Gap log | DORMANT | system_health |

## Supervised Activation Queue

| ID | Priority | Queue State | Title | Evidence | Proposed Action |
|---

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
SYSTEM CONTROL PLANE VERIFICATION PASS
- golden query broken-things: menu=/autopilot, router=/autopilot, governor=/autopilot, lane=system-failure
- golden query broken-cluttered-slow: menu=/autopilot, router=/autopilot, governor=/autopilot, lane=system-failure
- golden query system-audit: menu=/system-audit, router=/system-audit, governor=/system-audit, lane=system-failure
- golden query autopilot-plan-mode-complaint: menu=/autopilot, router=/autopilot, governor=/autopilot, lane=system-failure
- golden query autopilot-orchestrate-useless-complaint: menu=/autopilot, router=/autopilot, governor=/autopilot, lane=system-failure
- golden query autopilot-orchestrate-executes-without-menu: menu=/autopilot, router=/autopilot, governor=/autopilot, lane=system-failure
- golden query front-door-choice-too-many-tools: menu=/autopilot, router=/autopilot, governor=/autopilot, lane=front-door-choice
- golden query front-door-choice-what-use-next: menu=/autopilot, router=/autopilot, governor=/autopilot, lane=front-door-choice
- golden query explicit-menu-backend-options: menu=/orchestrate, router=/orchestrate, governor=/orchestrate, lane=menu-backend
- golden query repeatability-magic-revision-failure: menu=/repeatability-spine, router=/repeatability-spine, governor=/repeatability-spine, lane=repeatability
- golden query revision-lost-good-part: menu=/repeatability-spine, router=/repeatability-spine, governor=/repeatability-spine, lane=repeatability
- golden query ai-misfire-flat-revision: menu=/repeatability-spine, router=/repeatability-spine, governor=/repeatability-spine, lane=repeatability
- golden query wrong-route-repeatability: menu=/repeatability-spine, router=/repeatability-spine, governor=/repeatability-spine, lane=repeatability
- golden query patch-regression-repeatability: menu=/repeatability-spine, router=/repeatability-spine, governor=/repeatability-spine, lane=repeatability
- golden query full-control-plane-audit: menu=/system-audit, router=/system-audit, governor=/system-audit, lane=system-failure
- golden query skill-system-intent: menu=/source-to-skill-system, router=/source-to-skill-system, governor=/source-to-skill-system, lane=skill-system
- golden query re

[truncated]
```

### Autopilot Routing

**Status**: PASS

```text
ok: routing order
ok: Mission routing order
ok: Revenue routing order
ok: Skill-system routing order
ok: Repeatability routing order
ok: Front-door choice routing order
ok: Routing governor evaluation
ok: Misroute feedback capture
ok: Autopilot trace contract
ok: Claude/Codex bridge policy
ok: operator-agent arsenal wiring
ok: Notion aliases
Autopilot routing regression checks passed.
```

### System Health

**Status**: PASS

```text
Running Antigravity System Health Check...

# Antigravity System Health Report
**Generated**: 2026-05-11 11:59

## Activation Status

| System | Status | Last Active | Entries | Health |
|--------|--------|-------------|---------|--------|
| Performance Log (Phase 1) | ACTIVE | 1 days ago | 17 | Growing |
| Skill Evolution (Phase 2) | BLOCKED (17/20 entries) | — | — | Waiting |
| Cross-Pollination (Phase 3) | BLOCKED | — | — | Needs Phase 2 |
| Gap Detection (Phase 4) | READY | — | — | Ready |
| Session State | ACTIVE | Today (2026-05-11 09:58) | — | Healthy |
| Routing Intelligence | ACTIVE | — | 23 | Healthy |
| Gap Log | DORMANT | — | 0 | OK |

## Notion Sync

| Check | Status | Detail |
|-------|--------|--------|
| DNS/API preflight | network_unavailable | Use local-first evidence or run the Notion check in a network-enabled context. |
| Local performance entries | 17 | Source of truth for self-improvement when Notion is unavailable |
| Remote synced | 0 | Entries with confirmed Notion URL |
| Pending/local-first | 13 | Run `python3 execution/log_performance.py sync-pending --dry-run` before syncing |
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
Performance Log (17 entries)
  └─> Skill Evolution (needs 20+) [17/20]
        └─> Cross-Pollination (needs evolution data) [waiting]
              └─> Gap Detection (monthly) READY
```

## Recommended Actions

1. **IN PROGRESS**: 17/20 performance entries logged. Need 3 more to unlock Skill Evolution (Phase 2).
```

### Protocol Audit

**Status**: PASS

```text
============================================================
  PROTOCOL ACTIVATION AUDIT
============================================================
  Total Protocols:    44
  Active:             11
  Never Activated:    33
  Zombies (overdue):  38
  Total Activations:  783
  Activation Rate:    25%
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
    • operating-principles.md: overdue since 2026-04-11 (count: 1)
    • parallel_thought.md: never activated (count: 0)
    • parallelism-cheat-sheet.md: never activated (count: 0)
    • perplexity-usage-policy.md: never activated (count: 0)
    • quality_assurance.md: never activated (count: 0)
    • sales-conversation.md: never activated (count: 0)
    • session-end-commit.md: never activated (count: 0)
    • skill-evolution-protocol.md: overdue since 2026-04-09 (count: 42)

[truncated]
```

### Routing Scoreboard

**Status**: PASS

```text
# Routing Intelligence Dashboard
**Generated**: 2026-05-11 18:59 UTC
**Period**: 2026-05 (current month)

## Overview

| Metric | Value |
|--------|-------|
| Total Routings | 23 |
| Total Feedback | 12 |
| Positive Rate | 67% (8/12) |
| Negative | 4 |
| Mixed | 0 |
| Ensemble Rate | 0% (0/23) |
| Avg Intent Score | 4.0 |

## Expert Utilization

| Expert | Deployments | Positive | Negative | Mixed |
|--------|-------------|----------|----------|-------|
| antigravity-orchestrator | 23 | 8 | 4 | 0 |
| evolution-agent | 6 | 0 | 0 | 0 |

## Domain Distribution

| Domain | Requests | % of Total |
|--------|----------|------------|
| system | 13 | 57% |
| unknown | 5 | 22% |
| routing | 2 | 9% |
| copy | 1 | 4% |
| other | 1 | 4% |
| copy-quality | 1 | 4% |

## Top-Performing Ensembles

No ensemble routings recorded yet.

## Underperforming Routes

| Rating | Workflow | Expert(s) | Domain | Correction | Notes |
|--------|----------|-----------|--------|------------|-------|
| negative | pmj-magic-words | antigravity-orchestrator | system | autopilot | Misroute: /pmj-magic-words should have routed to /autopilot. Literal magic keyword routed to PMJ instead of system-failure control plane; patched routing_governor exact signals and golden matrix. |
| negative | publishable-copy-gate ceremonial PASS | antigravity-orchestrator | copy-quality | mission + red-team + five-input-content-gate + stricter copy gate with user-score calibration | Misroute: /publishable-copy-gate ceremonial PASS should have routed to /mission + red-team + five-input-content-gate + stricter copy gate with user-score calibration. Copy Gate Result overstated hook, voice, and tension; future gates must fail inflated scorecards and require calibrated user-outcome evidence. |
| negative | compile-knowledge | antigravity-orchestrator | routing | autopilot + system-audit | Misroute: /compile-knowledge should have routed to /autopilot + system-audit. Cohesion audit routing scenario failed: user-choice-burden phrasing should trigger front-door/system-audit logic, not generic knowledge compilation. |
| negative | ash-risk-map | antigravity-orchestrator | routing | autopilot | Misroute: /ash-risk-map should ha

[truncated]
```

### Unused Experts

**Status**: PASS

```text
**167 agents** with zero deployments (all-time):

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
- `authority-hacker` (Authority Hacker)
- `bond-halbert` (Bond Halbert)
- `boris` (Boris)
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
- ... and 137 more
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
      "active_workflow_count": 1038,
      "command_skill_count": 828
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
      "count": 250,
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
        "darrel-wilson-ai-monetization",

[truncated]
```

### Activation Governor Plan

**Status**: PASS

```text
# Activation Governor Plan

**Generated**: 2026-05-11 11:59

## Autonomy Boundary

Supervised queue/report only. This worker does not activate protocols, mark agents as used, commit performance entries, or write routing evidence.

## Local Signals

| Signal | Value | Source |
|---|---:|---|
| Performance entries | 17/20 | local performance log |
| Registrar inbox drafts | 30 | session_log_registrar |
| Registrar skipped candidates | 172 | session_log_registrar |
| Pending/local-first sync | 13 | log_performance |
| Sync failed | 4 | log_performance |
| Protocol zombies | 38 | protocol_tracker |
| Routing decisions | 23 | routing_intelligence |
| Negative/mixed route feedback | 4 | routing_intelligence |
| Session state | ACTIVE | system_health |
| Gap log | DORMANT | system_health |

## Supervised Activation Queue

| ID | Priority | Queue State | Title | Evidence | Proposed Action |
|---|---|---|---|---|---|
| `ag_583f9ff884ff` | HIGH | queued | Repair routed failure: /ash-risk-map | Request: what should I use next? | Approve a targeted routing fix or regression guard for this failure class only. Do not change broad defaults without regression proof. |
| `ag_c2c2ab1436d9` | HIGH | queued | Repair routed failure: /compile-knowledge | Request: I have too many tools and don't know what to use | Approve a targeted routing fix or regression guard for this failure class only. Do not change broad defaults without regression proof. |
| `ag_038eeb5f26f6` | HIGH | queued | Repair routed failure: /pmj-magic-words | Request: I got the magic a few times but cannot repeat it and revisions keep failing | Approve a targeted routing fix or regression guard for this failure class only. Do not change broad defaults without regression proof. |
| `ag_999058310cba` | HIGH | queued | Repair routed failure: /publishable-copy-gate ceremonial PASS | Request: AI Misfire finalized artifacts scored as 9 by Copy Gate but user rates them 3-4, generic, weak hook and tension | Approve a targeted routing fix or regression guard for this failure class only. Do not change broad defaults without regression proof. |
| `ag_312ebaafb56b` | HIGH | queued | Unblock Skill Evolution performance evidence |

[truncated]
```

## Next Week's One Move

Use the activation queue to turn the highest-value dormant asset into a real routed run.
