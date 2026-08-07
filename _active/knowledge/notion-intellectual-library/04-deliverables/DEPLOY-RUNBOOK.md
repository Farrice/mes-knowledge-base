# Notion Second Brain — Deploy Runbook (Phase 3 + Phase 4 wiring)

> **STATUS 2026-07-06**: historical deploy documentation. The live pipeline is `mirror_notion.py` → `.memory/sovereign.db` (`notion_mirror`), nightly launchd `com.antigravity.mirror-nightly`; write path = `chain_runner` finalize → Notion. This folder is not a live mirror.

**STATUS: DEPLOYED & LIVE (2026-06-23).** Hub `🏛️ Intellectual Library` + 5 DBs created in Notion. Local→Notion sync working. `NOTION_DB_SESSION_MEMORY=38849875a89781c0950ef6a48bb28a72` in `.env`. First row written. To log a session: `python3 execution/notion_api.py session-memory "<title>" --decisions "..." --pickup "..."`.

> **Gotcha we hit + the fix (don't repeat):** Notion AI created the Session Memory DB under the new **data-source** model, surfaced in the hub as a **linked view**. Sharing the hub page with the `Antigravity` integration exposed the *linked view* (`data_sources: []`) but NOT the underlying source data source — so every write 404'd or threw "is a database, not a database" under the pinned `2022-06-28` API. **Resolution:** the integration can read/write the hub page, so we had it **create its own classic Session Memory DB under the hub** (`POST /databases` parent=hub page_id) — integration-owned, single-source, fully writable by the 2022-06-28 code, no sharing dance, no data-source/version friction. That id is what's in `.env`. The two original AI-made Session Memory refs (`46dc60b8…`, `2a4b6108…`) are empty linked views — safe to delete in Notion to avoid confusion.

---

_Original deploy instructions (kept for reference / re-deploy):_

**Context:** the Notion AI prompt pack ([notion-ai-deployment-prompts.md](../notion-ai-deployment-prompts.md)) had existed since the Simon Intellectual Library build but was **never deployed** — which is exactly why the Notion logs felt like a write-only header-dump instead of a second brain. This runbook deploys it and wires it to the local memory stack (the L3 layer of the 3-layer memory system; see the memory-upgrade plan).

This is the **human gate**. Claude cannot run Notion AI prompts or create the databases for you. Do these steps yourself; they take ~20–30 min.

---

## Step 1 — Build the library (Notion AI, ~1 session)
Open Notion AI personal-agent chat with the strongest model. Paste **Prompt 1** from [notion-ai-deployment-prompts.md](../notion-ai-deployment-prompts.md) verbatim. Approve its build plan, then let it build the hub + 5 databases (Knowledge Entries, Experts, Sources, Skills & Playbooks, **💬 Session Memory**) + the two pages.

**Verify:** all 5 DBs exist with the exact properties; relations connect (create one dummy linked entry); the **Session Memory** DB has `Title`, `Date`, `Advisor/Mode`, `Key Decisions`, `Pickup Prompt`.

## Step 2 — Capture the Session Memory DB id → `.env`
In Notion, open the Session Memory DB → Share/Copy link. The 32-char hex in the URL (between the last `/` and the `?`) is the database id. Add to the project `.env`:

```
NOTION_DB_SESSION_MEMORY=<32-char-id>
```

(The other Simon DBs — Knowledge Entries / Experts / Sources — are human-curated via Notion AI per Prompts 2–4; only Session Memory is written programmatically from local.)

## Step 3 — Smoke-test the local→Notion sync (Phase 4)
The code is already shipped: `execution/notion_api.py session-memory`. With the id set, run one **dummy** row to confirm the `2022-06-28` pin works on the AI-created DB:

```bash
python3 execution/notion_api.py session-memory "Sync smoke test" \
  --decisions "Verifying the Session Memory write path" \
  --pickup "Delete this row if it round-trips"
```

**Verify:** prints `Session memory pushed: <url>`; the row appears in Notion with all five fields. If it returns a `400` (property/`data_sources` mismatch under the newer Notion data model), re-create the DB or access it via the data-source-aware path — see the version-pin caveat in `execution/notion_api.py`.

## Step 4 — Grounded advisors + ingestion (optional, Notion AI)
Run **Prompt 2** (per advisor) and **Prompt 3** (ingest a source) from the pack. Seed the library so it isn't born empty: ask Claude here to run `/library-extraction-bridge` on 2–3 existing extractions and paste the atomized entries via Prompt 3.

**Acceptance tests (from the pack):** glance test (state library size/strongest lanes in 30s), filter test (advisor cites entries by name), refusal test (advisor refuses when its lanes are empty instead of going generic).

---

## What flows to Notion (privacy boundary — Phase 4 allow-list)
**Only** five distilled fields per session: Title, Date, Advisor/Mode, Key Decisions, Pickup Prompt. **Never** raw transcripts or `assistant_message` blobs. Client + personal content stays in the local stores; the manually-curated "Personal Context" DB is the only home for personal material, and it is never auto-fed. Direction is strictly **local → Notion** (no read-back loop).

## How rows get written day-to-day
- **Manually:** the `session-memory` CLI above, at the end of a meaningful session.
- **Via `/handoff` (Phase 5):** handoff is demoted to a "pickup pointer" that also pushes a Session Memory row — so resuming work and the Notion second brain stay in sync. (Wiring lives in the handoff flow; this runbook only requires Steps 1–2 to unblock it.)
