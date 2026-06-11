# Farrice Content OS

Local state home for `/farrice-content-os`.

## Purpose

Turn raw Farrice concepts, source material, research, and timely market signals into nearly publish-ready content packages with Diandra's system spine, Farrice's voice, writers' room treatment, top-tier hooks, taste gates, and engagement packaging.

## Modes

| Mode | Output |
|---|---|
| `setup` | Context registry, state home check, first route |
| `ingest` | Raw source summary and content argument candidates |
| `research` | Research ledger and opportunity board |
| `sprint` | 20-post sprint with card records |
| `week` | Weekly batch and calendar |
| `hook-room` | Hook candidates, top 3, rejects, and selected hook |
| `service-package` | Client-facing AI Content OS offer assets |
| `context-audit` | Voice/context/source inventory and missing-context ledger |

## Current Status

| Area | Status | Notes |
|---|---|---|
| Command bridge | Scaffolded | `.agent/workflows/farrice-content-os.md` owns execution |
| Context base | Scaffolded | See `context-index.md` |
| Research | Scaffolded | See `research-ledger.md` |
| Brandjacking | Scaffolded | See `brandjack-board.md` |
| Hook Lab | Scaffolded | See `hook-lab.md` |
| Calendar | Scaffolded | See `content-calendar.md` |
| Engagement | Scaffolded | See `engagement-list.md` |
| Packages | Scaffolded | See `content-packs/` and `service-package/` |
| Vibe Tax deployment | Active | `/vibe-tax-deploy` uses this OS for Farrice voice, hooks, taste, and LinkedIn packaging while `/vibe-tax-brief` owns the diagnostic frame |
| Creator-to-Brand Format OS | Active | `_active/farrice-content-os/04-deliverables/creator-to-brand-format-os.md` and `/creator-format-os` turn sources, raw thoughts, founder interviews, and brand problems into reusable creator-format cards and briefs |

## First Recommended Run

```text
/farrice-content-os context-audit
/farrice-content-os research "AI operating partner for visible experts" --brandjack
/farrice-content-os sprint --count 20 --include-brandjacks
/creator-format-os use "[raw thought, source, draft, product, or problem]"
```
