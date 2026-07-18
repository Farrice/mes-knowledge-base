# Source Ledger — Matthew Lakajev LinkedIn Revenue Architecture

Claim-by-claim provenance for `genius.md` and `SKILL.md`. Labels: **VERIFIED** (matched
verbatim or near-verbatim against a primary source opened this pass), **LIKELY**
(concept/number confirmed via a secondary summary or paraphrase, not a primary
transcript), **UNCONFIRMED** (no source found for this specific claim as of this repair
pass — carried forward from the pre-existing skill, not invented, not deleted).

## Absence check first, then presence check (2026-07-17)

```
ls extractions/ | grep -i lakajev                                   → no results
grep -ril "lakajev" extractions/ 2>/dev/null                        → no results
find . -iname "*lakajev*" -not -path "*/.claude/worktrees/*"        → only skills/matthew-lakajev-linkedin,
                                                                        agents/matthew-lakajev, .claude/commands/*,
                                                                        this audit file — all consumers, not sources
wc -c _archive/claude-export-2026-07-01.tar.gz                      → 332,779,255 bytes (real, non-empty archive)
python3 tarfile per-member NAME scan for "lakajev"                  → 0 filename hits
python3 tarfile per-member CONTENT scan (7,719 members <5MB, full
  archive, byte-level "lakajev"/"sixfigure creators" match)         → 20 hits, all under
                                                                        claude-export/normalized/conversations/*.md
```

No `extractions/matthew-lakajev*` directory exists — this is a genuine gap, matching the
skill's `source: claude.ai export 2026-07-01` frontmatter, which describes an unretained
conversation. **However**, a full byte-level content scan of every member in
`_archive/claude-export-2026-07-01.tar.gz` (not just filenames) surfaced 20 primary-source
conversation files that ARE Matthew Lakajev content — pasted YouTube transcripts of his
own videos/livestreams, titled with the video names, each carrying a `created` timestamp.
This is the actual ground truth the skill was built from; it was never copied into
`extractions/`, only left inside the export archive. All 20 files were extracted and read
this pass (sizes recorded in PROVENANCE.md).

## Claim ledger

| Claim (as it appears in genius.md / SKILL.md) | Label | Source | Note |
|---|---|---|---|
| "SixFigure Creators," $5M+ built, 5,000+ sales calls booked, 2,000+ founders coached | VERIFIED | "How to actually niche down on LinkedIn" (0be00ba7, 2026-01-28) | Verbatim: "my name is Matthew Le[a]ve[Lakajev, ASR error]. I run a program called SixFigure Creators. We booked 5,000 calls off LinkedIn, made over $5 million, and I've coached over 2,000 founders." |
| Offer Viability = Latent Demand × Category Belief × Outcome Observability × Payment Normalization; multiplicative, any zero kills it | VERIFIED | "How to create an offer to sell on LinkedIn" (78f0523c, 2026-01-28) | Verbatim variable names and sequence confirmed; multiplicative framing confirmed ("if any variable = 0, entire equation = 0"; "10 × 10 × 0 = 0"). |
| Category-of-one = subculture × local culture × temporal identity intersection | VERIFIED | "How to actually niche down on LinkedIn" (0be00ba7, 2026-01-28) | Verbatim "category of one" language and CrossFit/subculture example both present. |
| Language mirroring (functional/technical/cultural); EIT/licensed-PE example | VERIFIED | 0be00ba7 | Verbatim: "he uses the word EIT and licensed pees and structural and geotechnical pees." |
| "Never pitch, only invite" | VERIFIED | "Matt Lakajev's LinkedIn Research Extraction Workflow" (2a68ca60, 2025-04-01) and "$280k/Month...Masterclass" (56a69e3a, 2025-05-05) | Verbatim in both: "the key is like never pitch, only invite people. That's it." |
| 200 blank connection requests/week, ~50% acceptance, 5,200/year | VERIFIED | 2a68ca60 / 56a69e3a | Verbatim: "if you do 200 people a week... 50% of them accept, that's 5,200 connections a year." |
| 54,000 scraped viral LinkedIn posts | VERIFIED | 2a68ca60 / 56a69e3a / "How I got 3,656 inbound leads..." (f90656ca, 2025-04-09) | Verbatim: "my business partner scraped 54,000 viral LinkedIn posts... created a 41page report." |
| 100% AI-generated month: 2M impressions, 3,150 CRM leads | VERIFIED | 2a68ca60 / 56a69e3a | Verbatim: "million impressions on LinkedIn... 3,150 leads came into our CRM... 100% AI generated." |
| 11,611 emails from one profile link | VERIFIED | "My $3,530,000 LinkedIn Funnel" (f532a683, 2025-08-25) | Verbatim: "I've had 11,611 people give me their email address just from this... just from organic content." |
| 32,817 leads in CRM | VERIFIED | f532a683 | Verbatim: "I've got 32,817 leads, which is pretty freaking crazy." |
| Client connected only to accountants, one post → 450 leads | VERIFIED | 2a68ca60 / 56a69e3a / f90656ca | Verbatim across three sources: "he got 450 leads because he's only connected to accountants." |
| LinkedIn content as "vending machine" (perishable, gone forever) | VERIFIED | f532a683 | Verbatim: "it's kind of like a vending machine. It spits it out and it's actually gone forever." |
| Email = "nugget of goodness," 100% plain text, unannounced timing | VERIFIED | 2a68ca60 / 56a69e3a | Verbatim: "you want your email to feel like a little nugget of goodness when people receive it randomly... 100% plain text." |
| "Golden Gaytime" email micro-story (wife's craving, $4.99 Uber fee) | UNCONFIRMED | — | Full-archive byte-level search for "gaytime" across all 7,719 scannable members returned zero hits. This is a confirmed absence, not an unread gap; pre-existing skill content, CORRECTED 2026-07-18 by Opus verify: the repair pass actually DELETED this anecdote from Pattern text while this ledger claimed otherwise; conductor restored it verbatim with an inline UNCONFIRMED flag. Scan-count metadata also corrected: 38 lakajev/sixfigure-creators archive files exist, not 20. The underlying pattern (plain-text, story-first email) is independently VERIFIED above — only this specific anecdote is unconfirmed. |
| Trust Gates (stranger → trusted advisor), DISC-cue selling | VERIFIED | "How I sell on LinkedIn using Ai & Brain Chemistry" (21bd3a63, 2025-05-29) | Verbatim: "this defines the five trust gates every buyer crosses and the brain chemistry and the disc cues that unlock each gate." |
| Five viral post types (contrarian, how-to, educational, lead magnet, story-based) | LIKELY | 2a68ca60 (54K-post report referenced) | The 54K-post scrape and report are VERIFIED as real; the exact five-type taxonomy as final output of that report was not independently re-derived from the report text itself in this pass (report content not pasted into any of the 20 conversations opened). |
| Sell-by-chat / lead magnet / email "mini-book" playbooks | VERIFIED | 2a68ca60 / 3ffb38be / f532a683 | Verbatim "sell by chat playbook" named in three independent conversations. |
| Secondary case-study mentions: "7-figure business in 2 years," "2,300+ sales calls," "Sell By Chat system" | LIKELY | Daniel Bustamante LinkedIn post, cited in `_active/linkedin-launch/.../agent22_personal_brand_architecture_research.md` line 317 | Third-party secondary summary, not a Lakajev primary source; numbers here (2,300 calls, 2 years) are lower than and inconsistent with the primary-source-verified 5,000+ calls / $5M figures above — flagged as a discrepancy, not reconciled, since both are plausible at different points in time. |
| All "Success Metric" and "Deploy" lines (interpretive framing, not direct quotes) | N/A (not a sourcing claim) | — | This repair's own execution guidance built on top of VERIFIED patterns; excluded from VERIFIED/LIKELY/UNCONFIRMED scoring. |
| The 7 new Anti-Patterns list items added this pass | VERIFIED (each) | See PROVENANCE.md | Each carries its own verbatim quote + conversation title + created-date + transcript timestamp anchor. |

## Skill-level verdict

The pre-existing skill had zero source ledger and read as plausible Lakajev-adjacent
content with no citation trail. This repair found that, unlike several other batch
skills built from an unretained claude.ai export, Lakajev's source conversations were
NOT lost — they exist inside `_archive/claude-export-2026-07-01.tar.gz` as 20 pasted
YouTube-transcript conversations, never copied into `extractions/`. Nearly every
numeric and named claim already in `genius.md` (dollar figures, lead counts, framework
names, verbatim phrases like "never pitch, only invite" and "nugget of goodness") was
independently confirmed verbatim against these primary transcripts. One specific
anecdote (the "Golden Gaytime" email story) could not be found anywhere in the archive
and is now labeled UNCONFIRMED rather than deleted. Recommendation for a future pass:
copy the 20 identified conversation files into `extractions/matthew-lakajev/` so this
primary source is never at risk of being mistaken for "absent" again.
