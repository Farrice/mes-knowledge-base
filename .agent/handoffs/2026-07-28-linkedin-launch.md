---
thread: linkedin-launch
status: ready
resume_hint: Take Farrice's verdict on v3 profile blocks, merge on PASS, finish Drive export
unfinished: v3 verdict + go-live merge + Drive verification + mission close
branch: main
pin: true
---

# LinkedIn Cash Launch — Context OS + Profile Copy v3 (wargame follow-through, Drive export)

## Purpose
- **Next session should do:** take Farrice's verdict on the v3 profile copy blocks; on PASS merge them into the go-live doc verbatim and prose-check; on FAIL apply the spiral brake (collect a raw voice-dump per job from Farrice — his words are the ore — before ANY rendition 4). Then verify/complete the Google Drive export and close mission `context-os-package-0729` with a done line.
- **Not in scope:** rebuilding the Context OS (done, committed), touching the About Take A or headline (LOCKED), mission 2b execution (a sibling session holds that lock — coordinate, never collide), new research.

## Load First
- `_active/linkedin-launch/CAMPAIGN.md` — campaign state + mission queue
- `_active/linkedin-launch/03-launch/2026-07-29-profile-copy-v3-PENDING-VERDICT.md` — THE artifact awaiting verdict; its frontmatter carries the binding register + banned tells + spiral brake
- `_active/linkedin-launch/03-launch/2026-07-28-PROFILE-GO-LIVE-TONIGHT.md` — merge target (canonical)
- `_active/linkedin-launch/04-deliverables/context-os/` — the 7-doc Context OS (done; source for Drive)
- `_active/linkedin-launch/CANON.md` — which docs are live vs superseded

## Current State
- **Objective:** $500–$2,000 collected by ~08-10 (`revenue-5k-incumbency`); this thread finishes the profile/packaging layer so content and DMs run on top.
- **What is already done:** offer wargame (GO-WITH-FIXES: $750 Angle Map, one-gap DM engine, day-7/10/14 tripwires) · 14-day launch plan · ICP battle card · 3 Gemini Deep runs (146 sources) · profile go-live master doc (About Take A locked) · Context OS 7 docs (canonical, committed) · /missions front door + campaign beacon + canon layer (read guard live) · v3 copy blocks written and persisted.
- **What is uncertain or stale:** Google Drive export state — an exporter agent died repeatedly to 529s mid-upload; folder "Farrice — LinkedIn Launch OS" (subfolders: 01 Context OS ×7, 02 Working Assets ×7 — "Profile Go-Live Master" DELIBERATELY excluded until v3 verdict, 03 Research ×3) is partially uploaded, possibly with duplicates. Verify with Google Drive MCP `search_files`; upload missing via `create_file` + `contentMimeType: text/markdown` (banked solution: memory `project_drive-export-via-mcp-fallback`). No Drive delete tool exists — flag duplicates, don't fight them.
- **Latest proof/receipt:** all work committed to main through `wip(profile-copy): v3 blocks persisted pending Farrice verdict (outage handoff)`; mission `context-os-package-0729` logged `stopped` in `.agent/missions.jsonl`.

## Suggested Skills / Workflows
- `/missions` — campaign queue front door (NOT /campaign — that's the council preset)
- `prose_classifier.py check` on merged paste blocks (locked About flags are accepted — felt verdict outranks)
- `chain_runner.py finalize` + missions.jsonl done line + commit/push at close

## Exact Next Prompt
```text
Read _active/linkedin-launch/03-launch/2026-07-29-profile-copy-v3-PENDING-VERDICT.md and show me the 8 blocks for my verdict. Register bar and banned tells are in its frontmatter — hold them. On my PASS: merge into 2026-07-28-PROFILE-GO-LIVE-TONIGHT.md, prose-check, commit, then verify and complete the Drive export ("Farrice — LinkedIn Launch OS") including uploading the final go-live doc as "Profile Go-Live Master", and close mission context-os-package-0729. On my FAIL: spiral brake — no rendition 4; collect my raw voice-dump per job first.
```

## Acceptance Criteria
- Farrice verdict recorded (voice_ratchet + missions.jsonl)
- Go-live doc contains verdict-passed copy only; classifier run on paste blocks
- Drive folder verified complete: 7/8/3 docs (+ final go-live doc after PASS), duplicates flagged
- Mission closed with done line; work committed and pushed

## Risk Notes
- A sibling session holds the tree lock for mission 2b — claim/queue via session_lock before multi-file writes.
- Anthropic 529 weather may persist: prefer main-loop work over subagent dispatch until stable.
- Privacy law (VOICE-CARD §1) binds all copy: pattern, never family specifics. Celebrity clients stay understated, never named.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- Previous handoff on this thread: `.agent/handoffs/2026-07-21-linkedin-launch.md` — everything it lists as shipped is EXTEND-ONLY.
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
