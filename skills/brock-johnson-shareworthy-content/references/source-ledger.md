# Source Ledger — brock-johnson-shareworthy-content

Claim-by-claim provenance audit, run 2026-07-17 during the Wave 3 Lane 4
repair pass. Every file size below was confirmed with `wc -c` (bytes, not
lines) on 2026-07-17, from the repo root.

## 0. The absence check (done first, per the envelope's hard rule)

`ls extractions/ | grep -i "brock\|johnson"` → **no matches**. `extractions/`
exists as a directory (not missing) and contains files for other experts;
it simply holds nothing for Brock Johnson. This is recorded as a verified
absence, not an assumption.

`find . -iname "*brock*johnson*"` (excluding `skills/` and `.tmp/`) surfaces
only: `agents/brock-johnson/` (persona files) and evolution-store trace/variant
artifacts generated *from* this skill (not sources *for* it). No transcript,
interview file, course export, or dated primary source exists anywhere in
this repo for Brock Johnson.

## 1. Biographical / authority claims — UNCONFIRMED

| Claim | Where it appears | Label | Why |
|---|---|---|---|
| "Direct intelligence from Instagram's Head (Adam Mosseri)" | `SKILL.md` line 14 | UNCONFIRMED | No interview transcript, URL, or dated source file exists in this repo substantiating an Adam Mosseri interview. |
| "100K+ following," creator of "Build Your Tribe" | `agents/brock-johnson/AGENT.md` line 10 | UNCONFIRMED | No follower-count source, screenshot, or dated reference in-repo. |
| "18+ months of proven strategy implementation" | `agents/brock-johnson/AGENT.md` line 10 | UNCONFIRMED | No case-study, results doc, or dated log in-repo. |
| "1 share = 150-400 views (10-26x more than likes)" | `SKILL.md` line 13, echoed in `genius.md` § Metrics That Actually Matter | UNCONFIRMED as an Instagram platform statistic | No Instagram engineering source, blog post, or dated citation in-repo backs this ratio. Treated as this skill's own internal reference math (LIKELY reflects the skill author's working assumption), not independently verified. |

These claims are NOT deleted (additive-first boundary) — they're flagged
here so downstream users know the persona's authority claims are unverified
inside this repo, and would need external verification (a real Brock
Johnson interview/course transcript) before being asserted as fact in
client-facing output.

## 2. The skill's own constitutive material — VERIFIED to exist, LIKELY as methodology, UNCONFIRMED as verbatim Brock Johnson quotes

None of the files below are primary-source transcripts. They are
practitioner-style instructional prompts authored for this skill. They are
internally consistent with each other (same taxonomy, same vocabulary
across all six "Crown Jewel" prompts), which is why they're labeled LIKELY
for methodology — but no file traces back to Brock Johnson's actual words,
so nothing here is labeled VERIFIED as a quote.

| File | Bytes (wc -c) | Label |
|---|---|---|
| `references/_legacy-prompts/algorithm-transcendence-playbook.md` | 5,739 | VERIFIED (exists, populated) / LIKELY (methodology) / UNCONFIRMED (as Brock's verbatim words) |
| `references/_legacy-prompts/content-format-architect.md` | 5,147 | same |
| `references/_legacy-prompts/engagement-psychology-system.md` | 4,388 | same |
| `references/_legacy-prompts/hook-science-engineer.md` | 4,633 | same |
| `references/_legacy-prompts/shareworthy-content-generator.md` | 5,071 | same |
| `references/_legacy-prompts/viral-share-optimizer.md` | 4,535 | same |
| `references/prompts/*.md` (6 files) | identical byte-for-byte to `_legacy-prompts/` | same — verified duplicate copies |
| `references/prompts-v2/*.md` (6 files) | 5,261–6,955 each | same — restructured "structure-pure" variants (Output Contract/Skeleton/Quality Gate added), same underlying claims |
| `references/quality-rubric.md` | 83,382 | VERIFIED (exists, populated, not a stub) / LIKELY (skill's own quality calibration) / UNCONFIRMED (as verified Brock Johnson quotes) |
| `references/genius-patterns.md` | 5,013 | VERIFIED (exists) — duplicate of `genius.md`'s Unconscious Mastery Behaviors + Hidden Knowledge sections, same caveats apply |
| `agents/brock-johnson/AGENT.md` | 2,022 | VERIFIED (exists) — persona routing file, not a source |
| `agents/brock-johnson/memory/context.md` | 164 | VERIFIED (exists) — empty template, no content to source from |

## 3. What the anti-patterns and named-entity anchors in genius.md actually cite

Every "Source anchor" line added to `genius.md` in this repair points at one
of the files above and quotes it verbatim (see `PROVENANCE.md` in this
output folder for the exact file+line table). None of those anchors claim
Brock Johnson said the quoted line in an interview — they cite the skill's
own prompt files as the origin of the pattern, which is the honest
provenance available.

## 4. Primary source added 2026-08-30 — VERIFIED transcript package

Source: [What Getting 2 Billion Views On Instagram Taught Me About Human Psychology](https://www.youtube.com/watch?v=MX-Emk6vkE4), published 2026-08-27 on the Build Your Tribe channel.

Local evidence package: `extractions/video-context/MX-Emk6vkE4/`.

- `transcript.vtt`: native English auto-caption track.
- `transcript.txt`: 5,070-word cleaned reading surface.
- `transcript_segments.json`: 737 timestamped spoken segments.
- `video-context-ledger.*`: spoken-evidence rows plus explicit uncertainty rows.
- Frames and OCR: unavailable because the local YouTube PO-token provider could retrieve captions and metadata but not playable formats.

| Mechanic | Timestamp | Evidence status | Translation |
|---|---:|---|---|
| Sharing as identity expression | `00:01:10–00:03:44` | VERIFIED as spoken | Design the post around what forwarding it lets the sharer say about themselves. |
| Private conversation as taboo-language research | `00:03:46–00:04:35` | VERIFIED as spoken | Mine DMs, comments, calls, and coaching for beliefs people admit privately but will not post publicly. |
| Repetition and 90-day “upycling” | `00:05:14–00:06:46` | VERIFIED as spoken | Repeat durable ideas and re-post proven assets after 90 days; treat the interval as Brock's heuristic, not a platform rule. |
| Experiment permission and 20% flop target | `00:07:53–00:09:22` | VERIFIED as spoken | Reserve a visible experiment lane; 20% is a speaker heuristic, not a guaranteed optimal rate. |
| Plain-language simplification | `00:09:25–00:10:34` | VERIFIED as spoken | Reduce cognitive load so the audience can understand and retain the lesson. |
| Authenticity / anti-pandering | `00:10:38–00:12:44` | VERIFIED as spoken, mechanism UNCONFIRMED | Treat intention-content mismatch as a creative risk; do not assert that audiences can literally detect AI or motive with certainty. |
| Negativity bias with saturation warning | `00:12:46–00:14:57` | VERIFIED as spoken, scientific causality UNCONFIRMED | Test accurate negative framing, but avoid a feed dominated by threat language. |
| Say–Do–Need gap / chocolate-covered carrot | `00:16:57–00:19:05` | VERIFIED as spoken | Attract with stated desire and observed choice while delivering the system or behavior needed for durable progress. |
| Systems over motivation and discipline | `00:19:07–00:20:37` | VERIFIED as spoken | Make consistency an inventory, batching, scheduling, and reuse problem. |
| Delusional optimism | `00:20:38–00:22:58` | VERIFIED as spoken, outcome effect UNTESTED | Preserve as creator posture, not as a guaranteed growth mechanism or mental-health prescription. |

## Net assessment

The skill now has one primary transcript source that directly grounds identity-signaling, audience-language research, repetition, experimentation, simplicity, the Say–Do–Need gap, the chocolate-covered-carrot metaphor, and systems-led consistency. Earlier framework details and authority claims remain mixed: the source verifies that Brock stated several performance figures and methods, but it does not independently verify those figures or prove the claimed psychological causality. Use the source-grounded mechanics as testable practitioner heuristics; do not treat the skill as a scientific-claim or verbatim-quote engine beyond the preserved transcript.
