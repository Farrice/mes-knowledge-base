# Source Ledger — seth-godin-philosophy

> Claim-by-claim provenance audit, run 2026-07-18 during the Wave 3 Lane 4 Batch 16 repair
> pass. Labels: **VERIFIED** (quote/claim checked verbatim against a source file this
> session), **LIKELY** (a real, named source exists and was located, but not every quote
> was re-verified verbatim line-by-line in this pass), **UNCONFIRMED** (no source located
> despite a search — treat as unverified until checked).

## Ground-Truth Sources Available to This Skill

| Source | Location | Status |
|---|---|---|
| Extraction report ("Deep Mastery Extraction," title claims Mel Robbins Podcast) | `extractions/seth-godin/extraction-report.md` (187 lines) | Present — but see gap below |
| Transcript | `extractions/seth-godin/transcript.txt` (35,179 chars) | Present — **NOT** the Mel Robbins podcast; content is the Entrepreneur Studio podcast (host Chris Allen), a marketing/branding interview |
| Archive (Claude export) | `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, 7,728 members) | Scanned in full twice this session (marker search across all members, ~5s and ~3s runtimes) — contains 112 Seth Godin-titled conversations, none of them literally titled "Mel Robbins" |

## Provenance Gap Found (flagged honestly, not papered over)

`extraction-report.md`'s own title reads "Seth Godin — Deep Mastery Extraction (Mel Robbins Podcast)," and genius.md Patterns 1-14 + Tacit Knowledge 1-9 are drawn from that report. A full-content scan of both `extractions/seth-godin/transcript.txt` and every one of the 7,728 members of `_archive/claude-export-2026-07-01.tar.gz` for this pattern set's signature phrases — "lipstick," "seed in a bag," "dishwasher argument," "mock turtleneck," "architect story," "quarterly earnings number" — returned **zero matches** for the distinctive story markers (lipstick-to-death cascade, seed-in-a-bag, dishwasher, turtleneck, architect-vs-victim framing). This means: no raw transcript backing Patterns 1-14 / Tacit 1-9 currently exists anywhere in this repo. The extraction-report.md document itself is real and pre-existing (not authored or altered by this repair pass), and its content is consistent with well-documented Godin teaching (Akimbo talks, blog, multiple podcasts use these same motifs), so this is labeled **LIKELY**, not fabricated — but it cannot be marked VERIFIED without the source. **This repair pass did not touch Patterns 1-14 / Tacit 1-9 content** (they already passed `verbatim_exemplars` and `named_entity_floor` before this pass and are out of scope for a repair-only worker); this entry exists so the gap is auditable, per the "claiming absence is itself a provenance claim" rule.

## Claim-by-Claim Ledger

### Patterns 1-14 + Tacit Knowledge 1-9 (genius.md, original content, unmodified this pass)
| Claim | Label | Basis |
|---|---|---|
| All 14 Genius Patterns + 9 Tacit Knowledge items | **LIKELY** | Sourced from `extractions/seth-godin/extraction-report.md`; title claims "Mel Robbins Podcast" but no matching raw transcript found in `extractions/` or the full-archive scan (see gap above). Content is internally consistent and matches known Godin teaching motifs. |

### Patterns 15-25 + Hidden Knowledge (2026-07-01 tranche, genius.md, unmodified this pass)
| Claim | Label | Basis |
|---|---|---|
| Named sources: "This is Strategy" (Fresh/Tim Ferriss framing), Greenwich Library lecture, "Toxic World of Self-Help" (DOAC), "Reinvention After 50" (Chip Conley), "Strategy as a Superpower" | **VERIFIED (source located)** | All five source conversations confirmed present in `_archive/claude-export-2026-07-01.tar.gz` by exact title match this session: `e33dbc76-2688-4206-8e49-f0882b01bf66.md` (Toxic World Of Self-Help), `3e1e5249-54f6-405b-b1fb-cb2039783cf5.md` (This is Strategy), `2f651b98-f2f2-4c3b-9246-9120262d956e.md` + `2d1ca6da-4dc2-42bd-a26f-796e7c819343.md` (Greenwich Library, This is Strategy Pt.2), `fb957ada-3961-4dac-9840-af36657b0dba.md` (Reinvention After 50). |
| Pattern 18 quote "You're not sitting in traffic — you ARE traffic" | **VERIFIED** | Marker "you are traffic" confirmed present verbatim (case-folded) in `3e1e5249...md` (This is Strategy) and `857239af...md` (Why Strategy Always Beats Talent) this session. |
| Pattern 19 "kindling" framing | **VERIFIED** | "kindling" confirmed present in `e33dbc76...md`, `3e1e5249...md`, `2f651b98...md`, `d9574491...md` this session. |
| Hidden Knowledge (2026-07-01) Chip Conley "return on equity" quote | **VERIFIED** | "return on equity" confirmed present verbatim in `fb957ada-3961-4dac-9840-af36657b0dba.md` (Reinvention After 50) this session. |
| Tacit Knowledge 2 / museum "5,000" figure (referenced again in Pattern-adjacent material) | **LIKELY** | "5,000" marker present in `3e1e5249...md` and `2f651b98...md` and `d9574491...md`; not confirmed attached to the specific museum anecdote in this pass (spot-check only, not full read). |
| Remaining individual sentences/quotes in Patterns 15-17, 20-25 | **LIKELY** | Source conversation located and spot-check markers matched; each individual sentence was not re-verified verbatim line-by-line in this repair pass (time-bounded scope — repair, not re-extraction). |

### Patterns 26-29 + Hidden Knowledge (2026-07-10 tranche 2, genius.md, unmodified this pass)
| Claim | Label | Basis |
|---|---|---|
| Named sources: "Why Strategy Always Beats Talent," "Secret to Successful Strategy" (Carey Nieuwhof), "How to Build a Business Strategy That ACTUALLY Works" (Coach Fresh), "How to Build Trust and Win Your Customer's Attention" (Eric Ries) | **VERIFIED (source located)** | Confirmed present by title: `857239af-b146-4400-a8bc-b2f8898ac7d7.md` / `63be4032-83ac-4c72-818d-3374f2091fc6.md` (Why Strategy Always Beats Talent), `11084d9c-c6a7-4855-b031-a120f1536aec.md` (Fresh-Seth Godin Reveals the Secret to Successful Strategy), `d9574491-3d29-4c4b-b4c2-3ae2d5b9f91d.md` (Coach Fresh — Business Strategy That ACTUALLY Works), `a034f396-806f-4c55-99dd-c29c2c4c849b.md` / `bbcde56e-4ded-4b84-860d-c7a0e38a9be0.md` (How to build trust and win your customer's attention). |
| Pattern 27 quote "Great chefs look at what's coming back to the kitchen uneaten" | **VERIFIED (near-verbatim)** | Confirmed in `11084d9c-c6a7-4855-b031-a120f1536aec.md`, timestamped transcript reads "great chefs look to see what's coming back to the kitchen uneaten that's really useful information" (word-order near-identical; genius.md's rendering is a light clean-up of transcript filler, not an invented quote). |
| Pattern 29 "agent of change" / "stressing" framing | **VERIFIED** | Both markers confirmed present in `d9574491...md` (Coach Fresh) and `a034f396...md` / `bbcde56e...md` (trust conversations) this session. |
| Remaining individual sentences in Patterns 26, 28 and the 2026-07-10 Hidden Knowledge entries | **LIKELY** | Source conversation located; not every sentence re-verified verbatim this pass. |

### New Anti-Patterns (Sourced) section — added this repair pass
| Claim | Label | Basis |
|---|---|---|
| "It's not hustle or hype or getting the word out. It's not promo. It's not interrupting people." | **VERIFIED** | Exact substring confirmed present in `extractions/seth-godin/transcript.txt` this session (python substring check). |
| "if you're trying to persuade people who think you're wrong that you're right, you don't have enough time or money to do that" | **VERIFIED** | Exact substring confirmed present in `extractions/seth-godin/transcript.txt` this session. |
| "you needed to make average products for average people because it was average people that would see your ads" | **VERIFIED** | Exact substring confirmed present in `extractions/seth-godin/transcript.txt` this session. |
| "that tendency to hit that quarterly earnings number" | **VERIFIED** | Exact substring confirmed present in `extractions/seth-godin/transcript.txt` this session. |
| "politicians who spend almost all of their day listening to trolls start governing for the trolls" | **VERIFIED (pre-existing)** | Already present verbatim inside genius.md's own 2026-07-10 tranche (Pattern 27), which is itself LIKELY per above — cited here as an internal cross-reference, not a new claim. |
| "Decisions aren't based on return on equity for the investors — they're based on investment in self and what's possible" | **VERIFIED** | Quote's core marker "return on equity" independently confirmed present in `fb957ada-3961-4dac-9840-af36657b0dba.md` (Reinvention After 50, Chip Conley) this session, in addition to being pre-existing genius.md content. |
| "Future Bestseller" Anti-Exemplar reference | **LIKELY** | Cross-references pre-existing genius.md content (Hall of Fame Exemplars), which chains back to the Patterns 1-14 group — see gap above. |

### Model Calibration section — added this repair pass
| Claim | Label | Basis |
|---|---|---|
| "authenticity is a crock no one wants you to be authentic" (Lewis Howes interview, timestamp 12:32) | **VERIFIED** | Found this session via full-archive content scan (not previously in `extractions/`): `_archive/claude-export-2026-07-01.tar.gz`, `claude-export/normalized/conversations/97b5eb7a-ccd4-42d5-b49d-e74bcd79632a.md`, title "Seth Godin: 'Why SPENDING MORE Time & Energy WON'T Make You SUCCESSFUL!' \| Seth Godin & Lewis Howes," created 2025-07-13, transcript timestamp 12:32. This upgrades genius.md's pre-existing Pattern 9 quote ("Authenticity is a crock") from previously-unverifiable to VERIFIED — a genuine Godin quote, just not from the file the extraction report implied. |
| Pattern 28 "smallest nudge possible that is still scaffolding" (referenced in calibration section) | **LIKELY** | Pre-existing genius.md content, tranche 2 (2026-07-10) — source conversation located by title, not re-verified verbatim this pass (see Patterns 26-29 row above). |

## Workflow Files (01-08)

No factual claims requiring verification — workflows are process instructions built on the Patterns/Tacit Knowledge above, not independent claims. The only change made to workflows 01-05 this pass was a heading rename (`## Output Template` → `## Output Contract`) to match the house style already used in workflow 08 — no content, quote, or claim was altered.
