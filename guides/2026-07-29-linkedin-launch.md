---
date: 2026-07-29
session: linkedin-launch
tier: operator-guide
status: enriched
---

# LinkedIn Cash Launch — What We Built 2026-07-28/29 and How to Use It

> Two sessions of one campaign: an adversarially-wargamed offer path to $500–$2K in 14 days, a paste-ready profile package, a 7-doc Context OS that makes any external AI context-complete on the offer, and three permanent system layers born along the way — the campaign/missions continuity layer, the canon layer (stale docs redirect at read time), and the replication lesson. Companions: `_active/linkedin-launch/CAMPAIGN.md` (state) · `knowledge/lessons/2026-07-28-replication-lesson.md` (method) · `.agent/handoffs/2026-07-28-linkedin-launch.md` (next session's packet).

## ⚡ If you only read 10 lines

1. `/missions` → the campaign queue; `/missions next` → runs the top open mission through /go. The beacon announces state at every session start.
2. Cash comes from DMs, not the feed: ~160 sends by day 10; first organic inbound lands week 4–6. Judge week 1 by fit-conversations.
3. The middle rung is **the Angle Map: $750, prepaid, 48h, make-right clause** — it lives in teardown follow-up message 2, Featured Card 2, then the About.
4. Close deadline is **day 10**, not 14 — new payment accounts clear in 2–7 days. Prepaid only.
5. Tripwires: day 7 = 5 fit-conversations or lead with the $750 ask · day 10 = 60 sends/0 replies means red-team the DM · day 14 = $750 cleared or drop to a $250 same-day read.
6. Feed any AI the Context OS: `_active/linkedin-launch/04-deliverables/context-os/` — load 01 first, 04 for any writing (it carries the privacy law).
7. Reading a superseded doc now triggers a one-line redirect (canon layer). Per-project map: `CANON.md`. Audit: `python3 execution/canon_audit.py <project-folder>`.
8. Voice register, Farrice verbatim: "silent confidence and swag with wit and humor." Banned: grand-noun labels, "room", em-dashes, exclamation marks.
9. About = Take A, LOCKED. Headline = Treatment A, LOCKED. v3 copy for everything else awaits verdict in `03-launch/2026-07-29-profile-copy-v3-PENDING-VERDICT.md`.
10. The five-move recipe is the quality floor: inventory → fresh receipts → isolated skeptic → felt standard → decisions-not-homework.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/missions` | Queue + next open mission, one screen | Any session touching a campaign |
| `/missions new <name> — <goal>` | CAMPAIGN.md + pointer; beacon activates | Starting any multi-mission objective |
| `/missions done <n> "note"` | Queue row closed + log line | A mission ships |
| `python3 execution/canon_audit.py <project>` | CANON.md map; drift flags | After adding/retiring load-bearing docs |
| `python3 execution/voice_ratchet.py add --verdict fail --line "..." --why "..."` | Banked felt verdict | Farrice kills a line or a move |
| `python3 execution/research.py "<q>" --depth deep` | Gemini Deep run, receipts, $0 under Ultra | Any judgment needing fresh receipts |
| `python3 execution/research.py gemini-collect --id <iid>` | Re-fetch a completed run's full text | Deep-run stdout only showed the receipt |

## The mental model

**Continuity is files plus hooks, never memory.** CAMPAIGN.md holds the queue; the SessionStart beacon reads it aloud; the canon layer corrects stale reaches at read time. A cold session starts warm because the disk is the brain.

**The offer's cash path and its category are different things.** The $2,500 sprint is the category anchor; the $750 Angle Map is what a stranger can buy this week. Never pitch the ladder — pitch the rung that matches the temperature.

**Copy quality is a process property.** The About takes hit because raw verbatim ore + one pen + a loaded method stack + Farrice's felt verdict. Two rejections on one artifact = stop producing, change the input (voice-dump), never a third variant from the same context.

## Capability: the campaign/missions layer

**What it is:** `_active/<project>/CAMPAIGN.md` (mission queue + standing facts + close ritual), `.agent/active-campaign.json` (pointer), `execution/hooks/campaign_beacon.py` (SessionStart announcer), `.agent/workflows/missions.md` (the /missions front door — /campaign was taken by the council preset).
**When to reach for it:** any objective spanning 2+ sessions.
**When NOT to:** single-mission work — `/go` alone is cheaper; and never two campaigns active at once (the pointer is singular by design).
**Worked example:** this campaign — beacon currently announces mission 2b (Farrice's Day-1 sends) as next.
**Honest edges:** `/missions next` on a FARRICE-tagged row correctly stops rather than simulating him; queue rows with sub-letters (2b) need the beacon's `\d+[a-z]?` regex — fixed 07-28, watch for other row-id shapes. The end-session spine does not yet auto-update the queue (flagged, not built — PoC gate).

## Capability: the canon layer

**What it is:** frontmatter vocabulary (`status: canonical|draft|superseded|archived` + `superseded_by`), `canon_audit.py` (writes CANON.md per project, flags prose-banner drift), `superseded_read_guard.py` (PostToolUse-on-Read one-line redirect).
**When to reach for it:** stamp any doc that supersedes another the moment it ships; run the audit at mission close.
**When NOT to:** working files and scratch — stamping everything is noise; only load-bearing docs.
**Worked example:** `CANONICAL-OFFER-BRIEF.md` (name says canonical, banner said superseded) now redirects readers to `PROOF-TO-MARKET-OS.md`; 12 linkedin-launch docs stamped 07-28.
**Honest edges:** guard only fires on `.md` with proper frontmatter; repo-wide stamping beyond linkedin-launch is queued inside the org-sweep follow-up, not done.

## Capability: the Context OS package

**What it is:** 7 docs in `04-deliverables/context-os/` (README/load-order, master context, offer canon, ICP truth map, voice register with the absolute privacy law, content strategy, proof library with VERIFIED/LIKELY labels). Mirrored to Google Drive "Farrice — LinkedIn Launch OS" for use in any AI.
**When to reach for it:** any external-AI content generation on this offer; any new session needing offer context without archaeology.
**When NOT to:** in-repo sessions — read the canonical sources CANON.md names; the package is a compression, not the source of truth.
**Honest edges:** Drive upload state is partial/unverified after the 07-29 Anthropic 529 outage (verify: `search_files` for the folder; expect 7/7/3 with "Profile Go-Live Master" deliberately absent). The package snapshots 07-29 truth — offer or ICP changes require regenerating the affected doc, and nothing detects that drift yet.

## Capability: the launch package (mission artifacts)

Offer wargame (`02-offer/OFFER-WARGAME-2026-07-28.md`, GO-WITH-FIXES + tripwires) · 14-day plan (`03-launch/2026-07-28-LAUNCH-PLAN-14-DAY.md`, day-by-day, wargame-integrated) · ICP battle card (`01-research/ICP-BATTLE-CARD.md`) · fresh research (3 runs, 146 sources, `01-research/2026-07-28-FRESH-RESEARCH/`) · profile go-live master (`03-launch/2026-07-28-PROFILE-GO-LIVE-TONIGHT.md`, About/headline locked) · v3 copy pending verdict.
**Honest edges:** reply/close rates in the wargame's math are modeled, not receipted — the day-10 "60 sends/0 replies" trip exists precisely because the DM copy is unproven. Nothing in the package has produced a dollar yet; the tripwires are the honesty mechanism.

## Composition (options, never pipeline)

| Stack | When it earns its cost |
|---|---|
| /missions + /go | Always — the queue feeds the compiler |
| Context OS + Farrice's own LinkedIn prompts in external AIs | Content generation outside this repo |
| canon_audit + org-sweep's PROJECTS.md | Repo-wide retrieval hygiene |
| research.py deep + adversarial-reviewer | Any offer/strategy decision (receipts before skeptic, skeptic before ship) |
