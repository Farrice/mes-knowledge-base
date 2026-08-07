# Source Ledger — fryderyk-wiatrowski-ai-employee-os

Every claim used in `SKILL.md`, `genius.md`, and `references/*.md` traced to its source, claim-by-claim. Labels: **VERIFIED** (directly present in the source package, checked verbatim), **LIKELY** (reasonable inference from directly observed evidence, not itself stated verbatim), **UNCONFIRMED** (could not be checked against a primary source in this package).

Ground truth package: `extractions/video-context/ohKt066uFhg/` — `transcript.txt` (900 spoken rows, fully read), `evidence-map.md`, `analysis.md`, `metadata.json`, `uncertainty-report.md`. No other extraction package exists for this expert (checked `extractions/`, `_active/harness/codex-harvest-2026-06-11/`, and the claude-export tarball by content — see Absence Note below).

## Video / Speaker Facts

| Claim | Label | Source |
|---|---|---|
| Video: "Viktor: AI Coworker That Lives in Slack — Fryderyk Wiatrowski," channel "AI Engineer," published 2026-05-11, duration 19:29 (1169s) | VERIFIED | `extractions/video-context/ohKt066uFhg/metadata.json` |
| Fryderyk Wiatrowski is co-founder of Victor; "It's absolutely blowing up," launched February 2026, "zero expectations of growing at all," calls it "immediate product market fit" | VERIFIED | transcript.txt [00:00:14-00:00:39] |
| Speaker links: x.com/fawiatrowski, getviktor.com | VERIFIED | metadata.json description field |

## Product / Architecture Claims

| Claim | Label | Source |
|---|---|---|
| Victor lives in Slack, has no separate web app, participates in threads and channels like a teammate | VERIFIED | transcript.txt [00:00:44-00:01:10] |
| Victor has access to 3,000 integrations and can build its own connection if one is missing | VERIFIED | transcript.txt [00:01:12-00:01:25] |
| Earlier prototype ("JCAI") was a browser-DOM agent, state-of-the-art on the WebArena benchmark, reliable for ~3-5 steps at ~60% reliability, degrading compoundingly per step | VERIFIED | transcript.txt [00:03:16-00:03:56] |
| JCAI evolved into an email agent ("Jace") that triggers on incoming email, can draft replies or call tools, and can gate a consequential action (e.g. a refund) behind approval | VERIFIED | transcript.txt [00:04:53-00:11:17] |
| Victor (company agent) launched February 2026; one connected integration is inherited by the whole team rather than reconnected per person | VERIFIED | transcript.txt [00:05:17-00:06:20] |
| Memory built for one user degrades ~100x faster when reused unmodified for 100 users on the same architecture | VERIFIED | transcript.txt [00:06:44-00:07:21] |
| Growth-channel context must not leak into engineering/support channels; a DM to Victor should not pull growth-channel context unless the requester is on the growth team | VERIFIED | transcript.txt [00:07:26-00:08:15] |
| Slack chosen as interface for two reasons: (1) employees interact with teammates in Slack, not a web app, (2) a 10-minute task feels acceptable from a Slack teammate but frustrating from a web-app agent | VERIFIED | transcript.txt [00:08:23-00:10:06] |
| Slack ambient events (DMs, public channels, threads, reactions, edits, deletes, cross-thread drift) must be linearized into a single agent context; a deleted message signals "stop," an edit should be re-responded to, a new DM after an abandoned thread must be checked for continuation vs. new task | VERIFIED | transcript.txt [00:10:13-00:11:51] |
| GPT-5.4 ("GPD 5.4" as transcribed) tested as a cheaper Opus-4.6 replacement; strong on tool-calling/codegen but rejected after an A/B test because users reacted to the personality change; Opus is described as "a bit sassy... in Victor" | VERIFIED (as spoken; model-version names not independently verified against a vendor source in this package) | transcript.txt [00:11:55-00:12:56] |
| Proactive example: Victor checked PostHog during a live growth-team discussion and flagged a cited A/B result as not statistically significant, with the calculation shown | VERIFIED | transcript.txt [00:13:02-00:13:49] |
| Day-one, workspace-wide proactivity (Victor DMing everyone, joining threads unprompted) triggered a security-team reaction at a customer | VERIFIED | transcript.txt [00:14:01-00:14:18] |
| Recommended rollout: earn broader activation "with a few users first," then expand | VERIFIED | transcript.txt [00:14:21-00:14:25] |
| E-commerce customer connected personal Gmail as the team's first shared integration; the team then discussed that employee's private emails until he confronted Fryderyk directly ("Victor is leaking all of my data. Why are you doing this?") | VERIFIED | transcript.txt [00:15:56-00:16:28] |
| In response, Victor gained the ability to scope integrations as personal (non-shared) rather than always team-wide | VERIFIED | transcript.txt [00:16:44-00:16:53] |
| "Victor is not a tool. It's a hire." | VERIFIED | transcript.txt [00:15:47-00:15:53] |
| Closing three-pillar summary: helps get work done, knows the company/context, is friendly ("make sure that Victor likes your team, your team likes Victor") | VERIFIED | transcript.txt [00:17:06-00:17:53] |
| Closing quote: "It is unworthy of excellent men to lose hours like slaves in the labor of calculation. Let us leave that to machines," spoken as attributed to the 17th-century inventor of calculus | VERIFIED (as spoken) | transcript.txt [00:18:04-00:18:46] |
| Attribution of the closing quote to "Godfrey Litz" | UNCONFIRMED | transcript.txt renders the name "Godfrey Litz" at [00:18:04-00:18:10]; this reads as an ASR mis-transcription of Gottfried Leibniz (inventor of calculus, 17th century), which matches the spoken description, but no primary Leibniz source is present in this extraction package to confirm the quote's exact wording or attribution — flagged, not corrected, per the "never invent provenance" rule |

## Absence Note (searched, not assumed)

- `extractions/` contains no other file or directory matching `wiatrowski` or `fryderyk` beyond the `ohKt066uFhg` video-context package — confirmed via `ls extractions/ | grep -i` on both surname and first name (no hits).
- `_active/harness/codex-harvest-2026-06-11/skills/fryderyk-wiatrowski-ai-employee-os/` exists and contains the same reference files as the live skill (verified by `wc -c`: SKILL.md 4074B, workflows/ai-employee-os.md 5321B, references/*.md 875B-1715B each) — a prior harvest of this same skill, not an independent additional source.
- `_active/harness/codex-harvest-2026-06-11/agents/fryderyk-wiatrowski/AGENT.md` (3255B) and `memory/context.md` (837B) exist as a persona wrapper around the same skill; read for cross-check, no new sourced claims beyond the video package.
- `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes) — checked via `tar -tzf ... | grep -i "wiatrowski\|fryderyk"` (filename-level content listing, not a full extraction): zero matches. No file inside the archive is named for this expert. A full byte-content grep of every archived file was not run (would require extracting 332MB); the filename-level check is recorded honestly as what was actually done, not upgraded to a stronger claim.
