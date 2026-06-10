# Operating Manual — How Farrice Runs Antigravity

> One page. The ~10 commands that constitute daily operation. Everything else is long-tail — invoke by explicit `/name` or ask `/recommend`.
> The system now has physical gates (hooks): cost, finalize-debt, routing warnings, extraction freeze. When a gate fires, it's working — don't fight it.

## Daily (10 min)

| When | Command | What it does |
|---|---|---|
| Monday morning | `/weekly-pulse` | 5-day revenue-weighted plan |
| Other mornings | `/daily-focus` | Today's 1-3 tasks |

## Client / Brand Production — THE MONEY PATH

| Task | Command | Notes |
|---|---|---|
| Cold-start converting copy (VSL/ad/email/landing) | `/copy-engine "<brief>"` | Grounds once (~$0-2.50), every refinement after is $0 |
| LinkedIn post from scratch | `/ghostwrite` | Lara/Diandra load automatically |
| Parallax edition | `/parallax` | Phase 2.5 GROUND mandatory (Edition 02 lesson) |
| Refine an EXISTING draft | `/writers-room` | Never use for production-from-scratch |
| Jen Santulan work | `cd _active/jen-listings/` then work | Client CLAUDE.md auto-loads |
| Andrea / Resonance work | `cd projects/andrea-dj/` then work | Client CLAUDE.md auto-loads |
| Brand system build | `/build-bos` | 7-phase, full BOS |
| Posters / visuals | "make a poster..." | fantastic-posters; cost gate fires automatically — approve or decline |

## Thinking & Research

| Task | Command |
|---|---|
| Decision / strategy / multiple perspectives | `/convene "<question>"` |
| Research anything | `/deep-research` or `python3 execution/research.py "<q>" --depth standard\|deep` |
| Multi-deliverable mission | `/supercomputer` (or `/autopilot` for gate-suppressed) |

## After EVERY Client Delivery (30 seconds — this is how the system learns what pays)

```bash
python3 execution/revenue_tracker.py log "<deliverable>" --revenue N --outcome "<what happened>"
```

No revenue yet? Log it when you know. The weekly closeout will keep asking about the 5 oldest until the queue drains.

## Weekly: `/weekly-closeout` (~20 min, Friday or pre-pulse Monday)

The outer loop. The session hook reminds you when it's stale — you don't have to remember. It runs:
1. `evolution_orchestrator.py auto` (also auto-runs daily 07:00 via launchd)
2. The 5 oldest pending revenue items → you answer: revenue / dead / still pending
3. Calibration drift check (shown only if inflation is firing)
4. Top evolution-queue item → accept/reject
5. Monthly: skill audit + CORE DRIFT review (demote trace-less core, promote earning long-tail)

## The Gates (what to expect)

| Gate | What you'll see | What to do |
|---|---|---|
| Cost | Claude asks "Approve $X for Y?" | Yes → Claude runs `cost_gate.py approve` and retries. No → it stops. Denied = hard cap hit, no override |
| Finalize debt | Claude gets bounced once at turn-end into running finalize | Nothing — it self-corrects. (Observe-mode first; flip to enforce after ~5 clean sessions: add `LEDGER_ENFORCE=1` to the Stop hook command in `.claude/settings.json`) |
| Routing warning | Injected note: "workflow X is forbidden for this domain" | Let Claude pivot to the mandatory workflow |

Extractions are **never gated** — `/extract` and `/extract-forge` run on demand. The monthly closeout reports each extraction's production-use count as information, nothing more.

## North Star

Core list: `PRODUCTION_CORE.md`. If a week's work never touched `/copy-engine`, `/ghostwrite`, `/parallax`, or a client folder — the system was busy, not productive. Skills don't pay; deliverables do.

## Rollback (if the rebuild misbehaves)

```bash
git checkout pre-rebuild-2026-06-09          # full state rollback
# or just disable gates: revert .claude/settings.json to the router-only version
launchctl bootout gui/$(id -u)/com.antigravity.evolution-auto   # stop the scheduler
# state backup: ~/antigravity-state-backup-2026-06-09.tar.gz
```
