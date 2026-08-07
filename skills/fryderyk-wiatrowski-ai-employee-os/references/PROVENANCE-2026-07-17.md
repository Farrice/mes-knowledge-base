# Provenance — fryderyk-wiatrowski-ai-employee-os repair

Anchor → source file + location. Full claim table lives in `references/source-ledger.md`; this is the compact anchor map for everything added in `genius.md`.

| Anchor in genius.md | Source file | Location |
|---|---|---|
| "Victor is an AI employee... lives in Slack, it doesn't have a web app" | `extractions/video-context/ohKt066uFhg/transcript.txt` | [00:00:46]-[00:01:02] |
| "3,000 integrations" | transcript.txt | [00:01:15]-[00:01:18] |
| JCAI / WebArena / 60% reliability / 3-5 steps | transcript.txt | [00:03:16]-[00:03:56] |
| Jace email agent, refund gated by approval | transcript.txt | [00:04:53]-[00:11:17] |
| One integration inherited team-wide | transcript.txt | [00:05:17]-[00:06:20] |
| Memory 100x faster exhaustion at 100 users | transcript.txt | [00:06:44]-[00:07:21] |
| Growth/engineering/DM context-leak boundary | transcript.txt | [00:07:26]-[00:08:15] |
| Slack chosen: teammate framing + 10-minute latency tolerance | transcript.txt | [00:08:23]-[00:10:06] |
| Ambient event linearization (DM/thread/edit/delete/reaction) | transcript.txt | [00:10:13]-[00:11:51] |
| GPT-5.4 vs Opus-4.6 personality regression | transcript.txt | [00:11:55]-[00:12:56] |
| PostHog proactive statistical-significance flag | transcript.txt | [00:13:02]-[00:13:49] |
| Day-one proactivity → security team reaction | transcript.txt | [00:14:01]-[00:14:18] |
| "earn it with a few users first... roll it out broadly" | transcript.txt | [00:14:21]-[00:14:25] |
| Personal Gmail leak incident (full story) | transcript.txt | [00:15:56]-[00:16:28] |
| Scoped (non-shared) integration capability added | transcript.txt | [00:16:44]-[00:16:53] |
| "Victor is not a tool. It's a hire." | transcript.txt | [00:15:47]-[00:15:53] |
| Three-pillar close ("make it friendly") | transcript.txt | [00:17:06]-[00:17:53] |
| Leibniz-attributed closing quote | transcript.txt | [00:18:04]-[00:18:46] (attribution UNCONFIRMED — see source-ledger.md) |
| Video/speaker metadata | `extractions/video-context/ohKt066uFhg/metadata.json` | full file |
| Absence check — extractions/ | `extractions/` directory listing | `ls extractions/ \| grep -i "wiatrowski\|fryderyk"` → only `video-context/ohKt066uFhg/` |
| Absence check — codex-harvest | `_active/harness/codex-harvest-2026-06-11/skills/fryderyk-wiatrowski-ai-employee-os/` + `agents/fryderyk-wiatrowski/` | `wc -c` on all files (recorded in source-ledger.md); same skill, no new source |
| Absence check — claude-export tarball | `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes) | `tar -tzf ... \| grep -i "wiatrowski\|fryderyk"` → zero matches |
