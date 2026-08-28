---
name: "gb-refresh"
description: "Staleness + drift sweep: reads manifest.json, checks pack freshness and artifact TTLs, detects content drift (upstream changed after downstream produced), and emits a drift report with the exact refresh order and commands. Flags, never blocks."
expert: "Growth Blueprint OS"
produces: "drift report (chat) + refreshed manifest.json statuses"
---

# Growth Blueprint OS — Refresh (Staleness + Drift Sweep)

Closes his gap #4: his write-once folders could not answer "what's now stale?" when positioning changed — downstream docs silently rotted. This workflow answers it by name, with a fix order. It is a compass, never a cage: every finding is a flag plus a quoted command; nothing here stops work.

## Pre-Flight Gate

- `growth-lab/<niche-slug>/manifest.json` exists? Missing → nothing to sweep; route to `gb-orchestrate` (or `gb-interview` for a brand-new engagement).
- Multiple engagements? Run per slug, or sweep all `growth-lab/*/manifest.json` when asked for the portfolio view.

## Skill Acquisition

Load `genius.md` §2.7 (schema'd state) and the SKILL.md `data_contract` (freshness test + TTL table). No other loads — this is a deterministic sweep, not an expert deliverable.

## Execution

### Step 1 — Pack freshness

Read `.agent/outlier-radar/packs/<niche-slug>/latest.json` → classify FRESH / STALE / ABSENT (SKILL.md test: `generated_at` vs `freshness_ttl_hours`, `status` field). Also run `python3 execution/outlier_radar.py status` for the per-niche freshness receipt. STALE/ABSENT → quote the refresh command and offer to run it now (cost: $0, keyless, minutes). If run: confirm the new pack validates (the radar's own `validate_pack()` runs at write time) and record the new `generated_at`.

### Step 2 — Artifact TTL sweep

Per `manifest.json` artifact entry: `now − produced_at` vs `ttl_days` → mark `fresh` or `stale`. Also compare each artifact's `pack_ref.generated_at` against the current pack: an artifact built on a superseded pack is flagged "data behind current" even inside its TTL.

### Step 3 — Drift detection (the part TTLs can't see)

Walk `depends_on` edges: any artifact whose upstream has a **newer `produced_at`** than its own is **`drifted`** — its inputs changed after it was built. Positioning re-run yesterday → whitespace, bullseye, scan, playbook, blueprint are all drifted regardless of their TTLs. Mark statuses in `manifest.json`.

**Content-drift check (beyond timestamps, cheap and honest):** for each drifted edge, read the upstream's history diff (latest `history/` snapshot vs living file) and say in one line WHAT changed and whether it plausibly invalidates the downstream ("authority statement unchanged; only pain ranks moved → whitespace likely survives; bullseye overlay needs the new pain→offer rows"). This is judgment, labeled as judgment — the mechanical flag stands either way.

### Step 4 — The drift report (chat, dense)

One block:

```
DRIFT REPORT — <niche-slug> · <date>
Pack: <FRESH|STALE(nd)|ABSENT>  <refresh command if not fresh>
Artifacts: <N> fresh · <N> stale · <N> drifted
  <artifact>: <status> — <one-line why> — fix: /<gb-workflow>
Refresh order: <only what needs refreshing, in dependency order>
One line: <plain-English state — what's safe to use today, what isn't>
```

Refresh order comes from `manifest.json.refresh_order` filtered to flagged artifacts — never "re-run everything" when two files need it. Write updated statuses back to `manifest.json`. Do not invoke the fix workflows yourself unless asked — the report is the deliverable; the operator (or `gb-orchestrate`) routes.

## Output Contract

1. **Drift report** in chat (shape above) — this workflow's deliverable is the report plus updated `manifest.json` statuses; it produces no new strategy artifact and therefore no client HTML of its own.
2. When run as part of a client cadence: append one dated line to `growth-lab/<niche-slug>/history/refresh-log.md` (date · pack age · counts · order given) so the maintenance story is receipted for the client.

## Content-Type Adaptations

| Mode | Adaptation |
|---|---|
| **Self-run (Farrice)** | Monthly sweep folded into /weekly-closeout rhythm where engagements are live; portfolio view across all growth-lab slugs |
| **Client engagement** | The refresh-log is client-visible proof of maintenance — retainers are sold on exactly this receipt trail |
| **Lead-magnet step-down** | N/A — refresh is an operating workflow, not a shipped artifact; its existence is a selling point named in the blueprint's refresh-cadence section |

## Quality Gate

- Every flag carries a one-line why and an exact fix (command or workflow) — a flag without a fix is noise.
- Drift computed from `depends_on` edges, not vibes; content-drift judgment labeled as judgment.
- Nothing blocked, nothing auto-rerun without an ask; statuses written back to `manifest.json`.
- Report fits in one block; refresh order is minimal, dependency-sorted.
