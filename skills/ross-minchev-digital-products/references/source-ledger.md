# Source Ledger — Ross Minchev (Digital Products)

Ground truth = the Claude.ai conversation exports inside `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes; confirmed via `ls -la`) at path prefix `claude-export/normalized/conversations/`. No `extractions/` entry exists for this expert (`ls extractions/ | grep -i minchev` returns nothing) — the skill's own `source: claude.ai export 2026-07-01` frontmatter points at this archive, not a separate extraction folder. Located by `python3 tarfile` member scan for `Minchev`/`minchev` across all 7,728 members (15 matching `.md` conversation files), cross-checked with `zgrep -a -c "Ross Minchev"` on the raw tar.gz (140 hits) to confirm the archive itself carries the text before trusting any per-member read. Each source file below was extracted to a local scratch copy and quote-matched against the skill content with `python3 -c "... re.finditer(...)"` (exact substrings, not paraphrase-matching).

## Primary Source Files (extracted, quote-verified)

| File (in `claude-export/normalized/conversations/`) | Conversation title | Created | Size (bytes) | Status |
|---|---|---|---|---|
| `3ee10b8d-e576-45f9-b884-fadd0eecba43.md` | Ross Minchev \| I Made $4,938 in One Week Using AI Digital Products | 2025-12-24 | 51,625 | VERIFIED — source, quote-matched |
| `56732bd0-1ab9-42c1-85d8-498cfba39c92.md` | Ross Minchev \| How This AI Tool Solves the NICHE Selection Problem | 2025-12-23 | 48,245 | VERIFIED — near-duplicate transcript of the same underlying video as above (same Merlin AI transcript header, identical body text), quote-matched |
| `02416885-1509-4d7e-abd3-0796b6f3a753.md` | Important Ross Minchev: How I Built a $10K/m AI Digital Product | 2025-10-23 | 26,967 | VERIFIED — source of the "Mistake number one/two/three" sequence, quote-matched |
| `53cb090c-b879-426a-a6b1-0193fb29978e.md` | 12-8-25 Ross Minchev: How To Actually Make Money Online in 2026 | 2025-12-04 | 38,789 | VERIFIED — source of the "five critical mistakes" sequence, quote-matched |
| `ec7a6102-2e70-47a4-a4b5-0b6832587aab.md` | AI Monetization Strategist — Ross Minchev: How I Use AI to Make Money | 2025-10-15 | 81,167 | VERIFIED — source of "due diligence"/"research takes forever" and "ChatGPT is a tool, not a miracle" material (not quoted verbatim in current genius.md; logged here for the next revision) |
| `728f9266-a8a2-43a3-ae4b-4dac48f34a89.md` | Important Ross Minchev: How I Built a $10K/m AI Digital Product pt.2 | 2025-10-24 | 19,484 | LIKELY — companion part-2 of `02416885`, same underlying video series; not directly quoted, listed for completeness |
| `4842bbba-11fc-41b2-a315-217e03c2817d.md` | 11-11-25 Ross Minchev: The Secret AI Trick 99% Miss | 2025-11-12 | 41,233 | LIKELY — confirmed to mention Minchev by name (tarfile scan), not read in full; not quoted |
| `e458b035-c8b6-4cfa-bbce-f54af570901d.md` | 12-8-25 Ross Minchev: The Secret AI Trick 99% Miss | 2025-12-04 | 76,471 | LIKELY — confirmed to mention Minchev by name, not read in full; not quoted |
| `9b153669-0a02-47cb-815e-dea3065ad230.md` | 12-8-25 [Digital Products]-Ross Minchev: I Made $4,938 in One Week | 2025-12-04 | 49,135 | LIKELY — appears to be another ingest of the same $4,938 video; not read in full |
| `43c61e1d-558d-4c91-83a0-44fd0bedf3c5.md` | 10-29-25 Ross Minchev: How To Make Your First $1,000 With AI Digital Product | 2025-10-29 | 38,286 | LIKELY — confirmed ClickBank-validation content by spot search, not fully read |
| `db8411fc-2018-4f91-bac5-c5908a3e0686.md` | Ross Minchev: This is How To Make REAL Money With Affiliate Marketing | 2025-10-17 | 30,511 | LIKELY — confirmed ClickBank Platinum Award bio claims by spot search, not fully read; bio superlatives NOT used in genius.md (deliberately, to avoid unverifiable claims) |
| `5886bdfe-32a1-4622-bb69-661b6ce27eb5.md` | AI Monetization Strategist pt.2 | 2025-10-17 | 11,475 | LIKELY — confirmed by tarfile name scan, not read |
| `f488627d-b565-4547-9481-be85697640d8.md` | 11-22-25 How to Quit Your Job With a 1-Person AI Business pt.2 | 2025-11-23 | 19,591 | LIKELY — confirmed Minchev mention by name scan, not read |
| `63be4032-83ac-4c72-818d-3374f2091fc6.md` | Seth Godin \| Why Strategy Always Beats Talent | 2025-12-23 | 122,686 | UNCONFIRMED as Minchev source — matched on "Minchev" substring but title/content is a different expert (Seth Godin); likely a stray cross-reference or comparison inside the conversation, not used for any claim |
| `3ccf4709-1c47-4045-8f3a-48c9f15b2b46.md` | Pat Flynn \| The No. 1 Skill For Anyone to Learn | 2025-12-23 | 98,929 | UNCONFIRMED as Minchev source — same as above, different expert (Pat Flynn), not used for any claim |

## Claim-by-Claim Labels

### SKILL.md — Quick Reference
- "Drill three levels, always... mushroom coffee immunity" — **VERIFIED** (`3ee10b8d…md` / `56732bd0…md`)
- "Title-as-targeting... one element does five jobs" — **VERIFIED**, "The title is the actual targeting" is a direct quote (`3ee10b8d…md` / `56732bd0…md`)
- "Validate before you build: trend → competition → offers → ads" — **VERIFIED**, sequence matches Ross's on-screen walk-through of the niche-discovery tool (`3ee10b8d…md` / `56732bd0…md`)
- "Active ads = market proof" — **VERIFIED**, "real ads from real people... you don't have to do any due diligence" (`3ee10b8d…md` / `56732bd0…md`)
- "Dual-path... ~50-60% commissions on digital" — **VERIFIED**, "60% out of 50 bucks... almost $30 commissions" (`3ee10b8d…md` / `56732bd0…md`)
- "Commission consciousness: 60% of $50 = ~$30/sale" — **VERIFIED**, same passage as above
- "Never ship raw AI: text-on-white-pages ebooks fail... 45 recipes, 85 pages, 12,000 words" — **VERIFIED**, both the "lazy job" quote and the countable-value list are direct quotes (`3ee10b8d…md` / `56732bd0…md`)
- "Speed-to-demonstration... execute, don't estimate" — **LIKELY**: consistent with Ross's repeated 24-hour/7-day framing across multiple videos (`02416885…md`, `53cb090c…md` "first door within 7 days"); no single verbatim sentence anchors the phrase "execute, don't estimate," so labeled LIKELY rather than VERIFIED.

### genius.md — Genius Patterns (all VERIFIED unless noted)
- Three-Level Micro-Niche Drilling, "nobody's fighting for these niches" — **VERIFIED** (`3ee10b8d…md` / `56732bd0…md`)
- Title-As-Targeting — **VERIFIED** (`3ee10b8d…md` / `56732bd0…md`)
- Data-Before-Intuition Validation (four gates) — **VERIFIED**, gate sequence matches the on-screen tool walkthrough; the specific phrase "extremely high competition... unique accessories, recipe books" is a direct on-screen text quote Ross reads aloud (`3ee10b8d…md` / `56732bd0…md`)
- Active Ads as Market Proof — **VERIFIED** direct quote (`3ee10b8d…md` / `56732bd0…md`)
- Dual-Path Monetization, "equal partner" — **VERIFIED** direct quote (`3ee10b8d…md` / `56732bd0…md`)
- AI Tool Stacking (Claude → Nano Banana) — **VERIFIED**, "Nano Banana Pro to create images" and the tool-pipeline description (`3ee10b8d…md` / `56732bd0…md`)
- Smart Packaging Over Raw AI, "lazy job" quote — **VERIFIED** (`3ee10b8d…md` / `56732bd0…md`)
- One Problem, One Solution — **LIKELY**: the discipline is real and named explicitly in the AI-generated meta-summary inside `728f9266…md` ("One Problem, One Solution Discipline"), but the summary line itself is Claude's synthesis of the source video, not Ross's own sentence; the *practice* (dorm cooking, allergy-safe treats) is drawn from his actual niche examples in `3ee10b8d…md`, which are VERIFIED.
- Speed-to-Demonstration — **LIKELY**, same basis as the SKILL.md line above.

### genius.md — Hidden Knowledge
- Saturated Niches Are Entered Sideways — **VERIFIED** direct quote (`3ee10b8d…md` / `56732bd0…md`)
- Audience Willingness-to-Pay Is Selected, Not Persuaded, "vet visit is expensive" — **VERIFIED** direct quote (`3ee10b8d…md` / `56732bd0…md`)
- Creatives Are the New Targeting, "Facebook does the targeting for me" — **VERIFIED** direct quote (`3ee10b8d…md` / `56732bd0…md`)
- The Affiliate Network Is a Free Back Office — **LIKELY**: "they give us everything, we just promote it" paraphrases the affiliate-network walkthrough rather than quoting one sentence verbatim; the underlying mechanics (ClickBank/DigiStore24 supply product + landing page + checkout) are VERIFIED in the same passage.
- Countable Value Closes the Sale — **VERIFIED** direct quote, "12,000 words, 85 pages, 45 complete recipes, meal prep guide, safety charts, troubleshooting" (`3ee10b8d…md` / `56732bd0…md`)

### genius.md — Anti-Patterns (Sourced, new)
All seven bullets are **VERIFIED** direct quotes, each individually quote-matched against its cited source file (see table above): three "Mistake number N" quotes from `02416885…md` (2025-10-23), two mistakes from the "five critical mistakes" list in `53cb090c…md` (2025-12-04), and two quotes ("lazy job," "extremely high competition... unique accessories") from `3ee10b8d…md` (2025-12-24).

## Explicitly NOT Used (checked, rejected as unverifiable or off-topic)
- Bio superlatives from `db8411fc…md` ("7-figure earner," "$300K+ months," "ClickBank Platinum Award," "$1M+ in affiliate commissions," "Forbes Featured") — spot-confirmed present in the transcript's self-introduction, but not used anywhere in SKILL.md or genius.md because they are unverifiable third-party claims about Ross's business, not teachable patterns. **UNCONFIRMED as a fact about Ross** (no independent corroboration attempted) and out of scope for this repair regardless.
- `63be4032…md` (Seth Godin) and `3ccf4709…md` (Pat Flynn) — matched the "Minchev" name-scan but are transcripts of different experts entirely; **UNCONFIRMED / not relevant**, excluded from all claims.
