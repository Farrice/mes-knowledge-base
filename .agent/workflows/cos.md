---
name: cos
description: "/cos — Chief of Staff OS v3 (The Standing Board). Daily: 3 advisors (cast by situation fit) dispatch in parallel, synthesized into Operator Primer (gate-checked, ≤2 retries). Weekly: all 5 seats + wildcards through /convene (Diverge → Deliberate → Synthesize) on focal question → 3 commitments. Auto-routes daily/weekly/status. Ledger compounds memory + accountability."
expert: Chief of Staff OS
domains: system, personal, goals, memory, briefing, standing-board
---

# /cos — The Standing Board

> **Skill**: `chief-of-staff-os`
> **Routing**: run `python3 execution/cos_prep.py status`, then route per SKILL.md routing table
> (first_run → onboarding · daily_done:false → cos-daily · weekly_due:true → offer cos-weekly · else → cos-status).
> Explicit: `/cos daily` · `/cos weekly` · `/cos status` · `/dump` (anytime capture).

**Read `skills/chief-of-staff-os/SKILL.md` first** — it describes the Standing Board charter, seats, workflows, and the Operator Primer format. Load `genius.md` before any session. All state under `.agent/cos/` (private, deterministic, leveraging live data).
