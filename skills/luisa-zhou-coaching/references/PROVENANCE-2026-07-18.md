# PROVENANCE — luisa-zhou-coaching repair

All anchors below resolve into `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes), a claude.ai conversation export. Location verified via a Python `tarfile` per-member scan (name-fragment match on `luisa`/`zhou`, no punctuation, across all 7,728 members; then a full-text scan of the 7,712 `.json`/`.md`/`.txt`/`.jsonl` members for `luisa`/` zhou`) — not `grep`, since the file is a `.tar.gz`. 21 members matched; 7 were genuine Luisa Zhou source transcripts, the rest were false positives (a `luisazhou.com` URL inside an unrelated conversation, or coincidental substring hits) confirmed by opening and reading each one.

| Anchor (genius.md location) | Source file (inside tarball) | Location | Size (bytes) |
|---|---|---|---|
| Coach-Sulting pattern | `claude-export/normalized/conversations/967f235a-8451-4f78-8829-8f397caff137.md` | 7:33–8:43 | 31,946 |
| Welcome Questionnaire pattern | same file | 0:26–4:24 | 31,946 |
| Three S's pattern | same file | 4:34–7:13 | 31,946 |
| Teach Clients to Be Coachable pattern | same file | 9:04–10:02 | 31,946 |
| Boundaries pattern | same file | 11:05–12:43 | 31,946 |
| Systematize Knowledge in Plain Docs pattern | same file | 10:04–10:46 | 31,946 |
| "Preparation Is the Charisma" insight | same file | 0:38–0:48 | 31,946 |
| "Client Docs Are a Compounding Asset Class" insight | same file | 10:37–10:46 | 31,946 |
| Anti-pattern: 24/7 availability | same file | 11:21–11:31 | 31,946 |
| Anti-pattern: over-functioning ("teach you how to fish") | same file | 9:27–9:30 | 31,946 |
| Experience Is the Qualification pattern | `claude-export/normalized/conversations/03a11a83-418f-46ed-84f3-4e50e1c14d49.md` | 0:14–3:40 | 26,022 |
| Pick a Start, Not a Forever pattern | same file | 3:53–6:38 | 26,022 |
| 3-Month/$1,500 pricing detail (rejection story) | same file | 6:48–9:19 | 26,022 |
| Free Taster Session pattern | same file | 12:40–14:56 | 26,022 |
| "Rejection Volume Is Tuition" insight | same file | 9:21–11:57 | 26,022 |
| "Productive Procrastination" insight | same file | 10:48–11:22 | 26,022 |
| "Abstract-Offer Tangibility Test" insight | same file | 4:46–5:03 | 26,022 |
| SKILL.md "3,500+ coaches" claim | same file | 3:07–3:12 | 26,022 |
| Anti-pattern: pure-Socratic reads as a scam | same file | 1:39–1:41 | 26,022 |
| Anti-pattern: certification-hunting | same file | 0:35–0:40 | 26,022 |
| Anti-pattern: gray-sofa idea-chasing | same file | 4:08–4:15 | 26,022 |
| Anti-pattern: complicated pricing formula | same file | 9:52–9:58 | 26,022 |
| 3-Month container structure (90-day framing, weekly calls) | `claude-export/normalized/conversations/90061dbb-d598-4c64-9974-c8d9bbdeef75.md` | 0:36–4:37 | 31,050 |
| Rapid Content Engine pattern (all 7 sub-moves) | `claude-export/normalized/conversations/1da08d35-b3b8-4168-8f82-7ef7dd0ff90c.md` | 0:00–10:25 | 27,563 |
| Anti-pattern: waiting for inspiration | same file | 1:00–1:03 | 27,563 |
| Anti-pattern: cold-professional/robot voice | same file | 10:00–10:05 | 27,563 |
| SKILL.md "10+ years coaching" claim | `967f235a-8451-4f78-8829-8f397caff137.md` | 3:38–3:41 | 31,946 |
| SKILL.md "five-figure...fully booked" claim | same file | 8:19–8:21 | 31,946 |

## Model Calibration section (new)

Not source-anchored (it is instructional framing, not a factual claim) — written fresh, modeled structurally on `skills/ben-watkins-storytelling/genius.md` lines 7–16 per the batch envelope, but content (big-sister real-talk, specific-numbers-not-hedges, naming the failure before the fix) is drawn from the texture of the verified transcripts above, not copied from Watkins.

## False leads investigated and ruled out

- `claude-export/normalized/conversations/a4bf3c97-b52e-4de3-9d4e-ee1e39441a2e.md` (201,164 bytes) — "Continuing Coaching Business Strategy," actually a Coach Cooz LinkedIn-strategy conversation. Matched the scan only because it contains a `luisazhou.com` favicon URL. Opened and read; contains no Zhou methodology content. Not used.
- `claude-export/normalized/conversations/f12761ef-f991-4feb-9fb1-550a972b87e4.md` (752,424 bytes) — titled "Comprehensive Principles for Injury Rehabilitation." Matched on "Zhou" as a coincidental substring. Opened; unrelated domain. Not used.
- `claude-export/normalized/conversations/4e1a9d26-8e0d-4ffd-b858-9275bbb72029.md` and `c91c74d9-40a2-4a93-95fd-9156e5f3d0c2.md` — Coach Cooz ad-strategy conversations, unrelated to Luisa Zhou. Not used.
- `claude-export/raw/batch-0001/conversations.json` (867,859,945 bytes) — the pre-normalization master export containing all conversations above in raw JSON form. Not separately re-parsed since the normalized `.md` files are the human-readable, line-numbered form of the identical transcript text and were sufficient for quote-level verification.

No claim in the repaired `genius.md` required an UNCONFIRMED label — every existing pattern/insight and every new anti-pattern item resolved to a verbatim or near-verbatim quote in a primary transcript, confirmed by direct file read (not filename or grep-count alone).
