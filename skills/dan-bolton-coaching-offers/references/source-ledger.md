# Source Ledger — Dan Bolton Coaching Offers

Claim-by-claim provenance for every factual/quote claim used or referenced in `genius.md`
and `SKILL.md`. Labels: **VERIFIED** (confirmed against a primary/external source as of
this pass), **LIKELY** (concept/paraphrase confirmed but not verbatim, or inferred with
reasonable confidence from a confirmed adjacent fact), **UNCONFIRMED** (no source found
for this specific claim as of this repair pass — carried forward, not invented).

## Absence check (run before writing anything else, 2026-07-17)

```
ls extractions/ | grep -i bolton                                  → no results (193 total entries in extractions/, none match)
grep -ril "bolton" extractions/ 2>/dev/null                        → no results
ls _active/codex-harvest-2026-06-11/extractions/ 2>/dev/null | grep -i bolton   → no results
find . -iname "*bolton*" -not -path "*/node_modules/*"             → skills/dan-bolton-coaching-offers, agents/dan-bolton,
                                                                       .claude/commands/dan-bolton*.md, and their worktree mirrors —
                                                                       all consumers/mirrors of THIS skill, not a source for it
wc -c _archive/claude-export-2026-07-01.tar.gz                     → 332,779,255 bytes (real, non-empty archive)
tar tzf _archive/claude-export-2026-07-01.tar.gz | grep -i bolton  → no results (filename-level search across the full archive listing)
```

No `extractions/dan-bolton*` directory or transcript exists in this repo, and no filename
inside the 332MB claude-export archive matches "bolton." This is a confirmed absence
(verified by real directory listings, a recursive grep, and a full archive filename
listing on 2026-07-17), not an unread gap. SKILL.md's frontmatter cites `source: claude.ai
export 2026-07-01` — this appears to describe a Claude.ai conversation the skill was
authored from directly, with no separate extraction/transcript file retained anywhere in
the repo. That conversation content is not independently recoverable in this repair pass.

Pre-existing skill files were checked for size so "no source" isn't confused with
"empty/corrupt file":

```
wc -c skills/dan-bolton-coaching-offers/SKILL.md                                    → 3,111 bytes
wc -c skills/dan-bolton-coaching-offers/genius.md (pre-repair)                      → 6,948 bytes
wc -c skills/dan-bolton-coaching-offers/workflows/01-redesign-coaching-offer.md     → non-empty (workflow_contracts check already PASS)
wc -c skills/dan-bolton-coaching-offers/workflows/02-build-client-infrastructure.md → non-empty (workflow_contracts check already PASS)
wc -c skills/dan-bolton-coaching-offers/workflows/03-script-mini-vsl.md             → non-empty (workflow_contracts check already PASS)
```

All non-empty. None cite an external source for any claim in the pre-repair file — the
skill was built without a source ledger, same failure pattern as other batch-4 skills
built from an unsaved claude.ai export.

## External verification attempted (live search/fetch, 2026-07-17)

Since no local transcript exists, this pass searched the open web for Dan Bolton (coach,
New Zealand, "Scale School" podcast) to confirm he is a real person with the described
business, and to attempt verification of specific quotes/numbers already in the skill.

| # | Source | Type | Date | URL |
|---|--------|------|------|-----|
| S1 | Zander Fryer, "032: Dan Bolton — Rising from Rock-Bottom" | Podcast show notes (fetched) | 2021-09 | https://zanderfryer.com/podcast/032-dan-bolton-rising-from-rock-bottom/ |
| S2 | "Shutting Down a $100k a Month (Profit) Coaching Business w/ Dan Bolton" | YouTube video (title/metadata only — transcript not accessible via fetch) | undated | https://www.youtube.com/watch?v=RgPeMjbEJtM |
| S3 | danbolton.co | Personal/offer website (fetched) | current as of 2026-07-17 | https://www.danbolton.co/ |
| S4 | "Scale School with Dan Bolton" | Podcast series (existence confirmed via search, episodes not fetched) | ongoing | https://podcasts.apple.com/podcast/scale-school-with-dan-bolton/id1671250753 |
| S5 | Taki Moore, "Black Belt Sensei Session: The Facebook & Funnel Fix with Dan Bolton" | Article (existence confirmed via search, not fetched) | undated | https://medium.com/@takimoore/black-belt-sensei-session-the-facebook-funnel-fix-with-dan-bolton-5b1d0d80238e |

Note: WebFetch on the YouTube URL (S2) returned only page-chrome/footer content, not the
video description or transcript — the shutdown claim is VERIFIED only as "a real video
with this title exists," not as a verified account of Bolton's own reasoning or timeline.
WebSearch queries specifically for "Three I Framework," "information infrastructure
implementation," and "co-creation" + Bolton returned no matches — these terms could not be
externally corroborated as Bolton's own naming in this pass.

## Claim ledger

| Claim (as it appears in genius.md / SKILL.md) | Label | Source | Note |
|---|---|---|---|
| Dan Bolton is a real NZ-based coach who built a multi-million-dollar online coaching business | VERIFIED | S1, S4, S5 | Corroborated across an independent podcast (S1), his own ongoing podcast (S4), and a third-party coaching-community writeup (S5). |
| Bolton previously ran a $100k/month coaching business and shut it down | LIKELY | S2 | Video title confirms the shutdown as a real, published event; the underlying reasoning/quotes are not transcript-verified. |
| "Everything works... burned it down on instinct in 2023" / 8 hrs/week, drinking through calls | UNCONFIRMED | — | Directionally consistent with S2's existence but the specific year, hours, and drinking detail were not found in any source opened this pass. Pre-existing skill content; flagged, not deleted (additive-only repair boundary). |
| "Why you'll never succeed if you think you can do it alone" | LIKELY | S1 | This is the podcast's own paraphrase of the episode's teaching point, not a verbatim Bolton quote. |
| danbolton.co offer: "you. me. 8 weeks. magic." — $8,000, 8-week engagement | VERIFIED | S3 | Fetched directly from the live site. |
| The Three I Framework (Information / Infrastructure / Implementation) as Bolton's own named system | UNCONFIRMED | — | Not found in S1–S5 or any search pass. Pre-existing skill content; flagged, not deleted. |
| "here's the secret formula, ping me if you get stuck" (old-model quote) | UNCONFIRMED | — | Not found in any source opened this pass; reads as this skill's own paraphrase of a generic coaching-model failure, not a verbatim Bolton quote. |
| Client Jason: $103K cash month on $10/day ad spend; turned off marketing within 30 days | UNCONFIRMED | — | Not found in S1–S5. Specific enough (named client, exact dollar figures) that it should be treated as a real case study Bolton has referenced somewhere, but no primary source was located in this pass. |
| One GPT with 700+ active client chats; ~100 hours spent building GPTs; GPTs named "Messaging Architect," "Game Plan GPT," "the Wizard" | UNCONFIRMED | — | Not found in S1–S5. Named tools this specific are unlikely to be fabricated wholesale, but were not independently confirmed. |
| "bored out of my brains" (re: repeated offer/VSL reviews) | UNCONFIRMED | — | Not found in S1–S5. |
| Mini-VSL: ~10,000 YouTube views in 18 months, hundreds of clients, millions in revenue, 4 hours to shoot | UNCONFIRMED | — | Not found in S1–S5; S2's existence (a YouTube channel with business-teardown content) is consistent with Bolton being an active video creator but does not confirm these specific figures. |
| Neon-sign concept "adapted from Iman Gadzhi" | UNCONFIRMED | — | Not independently checked against Iman Gadzhi source material in this pass. |
| "I have no idea what other people should do" / "...but what do you think? What is your gut saying?" | UNCONFIRMED | — | Not found in S1–S5. The Scale School podcast (S4) is the most likely place this would surface; episodes were not individually opened in this pass. |
| Client into $1,400/mo offer at $150-200 acquisition cost | UNCONFIRMED | — | Not found in S1–S5. |
| All "Success Metric" and "Deploy" lines in genius.md (interpretive/prescriptive, not attributed to Bolton verbatim) | N/A (not a sourcing claim) | — | These are the skill's own execution guidance, not claimed as Bolton quotes; excluded from VERIFIED/LIKELY/UNCONFIRMED scoring. |

## Skill-level verdict

The pre-existing skill (`SKILL.md`, `genius.md` before this repair) was written with zero
external sourcing — every pattern read as plausible Bolton-adjacent content with no
citation trail, and the frontmatter's `source: claude.ai export 2026-07-01` points at a
conversation that was not itself retained anywhere in the repo. This repair confirmed Dan
Bolton is a real coach matching the general profile (New Zealand, ex-youth-pastor
background per S1, an active "Scale School" podcast per S4, a live compressed coaching
offer per S3, and a documented business-shutdown decision per S2) but could NOT
independently verify the specific named framework ("Three I Framework"), the specific
dollar figures (Jason's $103K month, the $1,400/mo offer, 700+ GPT chats), or any of the
direct quotes attributed to Bolton in the pre-existing pattern text. This repair did not
delete or rewrite that content (additive-only boundary); it added the Anti-Patterns
section with honest per-item labels and this ledger so the gap is visible rather than
buried. Every numeric and quoted claim in the Genius Patterns / Hidden Knowledge sections
above should be treated as UNCONFIRMED until a primary Scale School episode, Skool post,
or direct Bolton interview is opened and checked.
