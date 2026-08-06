# Latest Handoff

**Thread:** readout-os  
**Full path:** .agent/handoffs/2026-08-06-readout-os.md  
**Date:** 2026-08-06 (today)  
**Status:** ready  
**Title:** Readout OS — Visual Delivery System Build (Briefing Room + Live Pulse + Premium Minimal)

> Not auto-loaded. Run `/resume` to choose any thread, or `/resume readout-os` for this one.

---

---
thread: readout-os
status: ready
resume_hint: Deploy phase: /briefing-room + /pulse-board daily; scratch off 3 waiting missions; verify Mon 07:30 angle brief lands
unfinished: Parked opt-ins: COS-to-brief bridge, chart kinds, arsenal reskin, sidebar search
branch: main
pin: true
---

# Readout OS — Visual Delivery System Build (Briefing Room + Live Pulse + Premium Minimal)

## Purpose
- **Next session should do:** Deploy phase — use /briefing-room and /pulse-board as daily surfaces; scratch off the 3 waiting compiled missions from the live Pulse; verify Monday 07:30 first automated pre-filed angle brief lands in the room; port worthy md deliverables to the Drive content vault (md_to_gdoc.py).
- **Not in scope:** New engines or boards; COS-to-brief bridge, chart section kinds, arsenal-board reskin, sidebar search (all parked opt-ins); productizing the system for others (parked behind P2M revenue).

## Load First
- .agent/workflows/briefs.md — the Visual Delivery Doctrine: 5 family recipes, librarian, --share rule, Drive vault road
- docs/solutions/2026-08-06-live-local-board-pattern.md — the live-board pattern (writers-first, dual-mode)
- _active/farrice-brand/premium-minimal/REPORT-DIALECT.md — design-system exceptions for report surfaces
- deliverables/research-briefs/design-system-showcase/ — every section kind, once (living format reference)
- deliverables/research-briefs/icp-invisible-expert/ — ICP family exemplar

## State
- All shipped + pushed on main, $0 spend: Premium Minimal across briefs/room/board/pulse; Briefing Room v2 (sidebar, pagination, quick-copy, context packs, --share); live Pulse (pulse_serve.py localhost, click-to-complete via pulse_actions.py — first-ever mission-close writers, reopen included); universal nav triad; pipeline integrity (render auto-refreshes index; Monday runner path bug fixed); Visual Delivery Doctrine both harnesses (AGENTS.md); librarian lifecycle (30d periodicals auto-archive, archived never gone, audit + housekeeping strip); side-window live reload (marker-verified).
- Verdicts: "great" (re-skin + room), "great" (session), "good" (visual delivery close). Doctor pass clean: 0 new hooks, binding suggestion-only, shelves clean, no new broken citations.

## Commands (no memory needed)
- /briefing-room · /pulse-board · python3 execution/pulse_serve.py --open (live boards)
- python3 execution/render_brief.py <json> [--share|--gdoc] · python3 execution/brief_library.py [archive|unarchive|audit]
- python3 execution/md_to_gdoc.py <file.md> (Drive vault port)

## Suggested skills/workflows
/briefs (authoring doctrine) · /go (mission close-outs offer brief-format receipts) · /nate-b-harness-design-audit (run after a week of living with the system)

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.

