# Source Ledger — russell-brunson-funnels

Ground truth for this skill is a set of 10 claude.ai conversations (Farrice's own transcript-analysis sessions with Claude, each pasting a Merlin-AI transcript of a Russell Brunson YouTube video and asking for extraction/analysis). Located in `_archive/claude-export-2026-07-01.tar.gz` at path `claude-export/normalized/conversations/<id>.md`. Identified via `_active/claude-export/harvest/census-full.json` (entry `"expert": "Russell Brunson"`, 10 conversation ids, `max_richness: 8`) and confirmed by extracting and reading all 10 files directly (`python3 tarfile` scan, sizes recorded below).

**Provenance caveat**: each conversation file contains two layers — (1) the Merlin-AI transcript of Brunson's actual spoken video content, timestamped `m:ss`, which is the layer cited below and treated as his words; and (2) Claude's own follow-on "extraction framework" prose (e.g. "TRANSCENDENCE SYSTEM", numbered "artifact" prompts) generated in that chat session, which is AI-authored analysis *about* Brunson, not his words, and is never cited as a quote in this skill.

## Source Files (extracted, sizes confirmed)

| Conversation ID | Title | Created | Size (bytes) |
|---|---|---|---|
| 156c576f-536b-4a6d-a33b-3b5efd30b38e | "I paid $500,000 for these books teaching the lost secrets of marketing..." | 2025-05-29 | 74,852 |
| 0a89743f-81f6-47cc-b539-86345323a94f | "I paid $12,500 for this book about mind control (Edward Bernays)" | 2025-05-31 | 53,065 |
| e111041c-a359-43db-9a42-6d7c481470c1 | "I paid $100K to learn how to access the universal mind...it worked" | 2025-07-23 | 49,829 |
| c6416fe8-9783-478c-ad64-42d7577d26d4 | "I paid $30,000 for a secret set of ELITE laws...I'm EXPOSING Everything" | 2025-07-12 | 44,049 |
| 3c7d1c70-5330-4220-b964-ab74769883da | "I paid $3500 for a lost course on ELITE marketing...I'm exposing it all" | 2025-08-18 | 45,485 |
| b7261d84-0983-405d-9940-8244bff594d4 | "I paid $75 for this LOST book on controlling your subconscious mind" | 2025-06-19 | 37,545 |
| 5ec3d942-387d-4dfb-be1c-44ea74d509df | "The hidden manuscript that TERRIFIES the ultra-wealthy \| Gospel of Wealth" | 2025-07-12 | 36,875 |
| dc53e5d3-e5a3-4b78-8021-7ee2655e6f1f | "I paid $150,000 for a book given to a man by an angel...it changed everything" | 2025-07-17 | 36,401 |
| d103b3ad-41c1-4647-b186-239251e58581 | "I paid $500 for a book that secretly influenced generations" | 2025-08-07 | 34,049 |
| cdda44d6-fed6-4a60-b678-9968c656878f | "The Dark Playbook Behind Success (Mind Control & Propaganda) pt.2" | 2026-01-01 | 26,871 |

Also consulted: `skills/russell-brunson-funnels/references/prompts-v2/principle-vs-tactic-teardown.md` (in-repo, structure-pure v2 prompt; VERIFIED as a repo artifact, not a Brunson quote source).

## VERIFIED (checked verbatim or near-verbatim against the extracted transcript text this session)

| Claim / quote in genius.md | Source file | Timestamp |
|---|---|---|
| "you got to grab their attention first... then you got to persuade them" (Hook-Story-Offer traced to Napoleon Hill's advertising course) | 156c576f...md | 7:14-7:22, 9:33-9:41 |
| Robert Allen "vivid vision" sequences; Hormozi's Hawaii/flight travel-agent analogy | 156c576f...md | 8:35-9:04 (transcript spells the name "Alex Heroszi" — a Merlin-AI mis-transcription of Alex Hormozi; concept and framing confirmed, name spelling not corrected in source) |
| Bernays "torches of freedom" cigarette campaign, women didn't smoke before it | 0a89743f...md | 3:46-4:32 (transcript renders it "torch of for[freedom] women" — transcription artifact; the historical claim and mechanism are confirmed) |
| "lady boss" shirts, Caitlin Poland, "superhero cape" identity framing | 0a89743f...md | 6:05-6:20 (verbatim) |
| Desire-over-need / Bernays selling WWI war bonds emotionally, not on "features and benefits" logically | 0a89743f...md | 1:41-1:58 (verbatim) |
| Propaganda → Public Relations rename when the word turned toxic | 0a89743f...md | 8:31-8:43 (verbatim) |
| $12,500 paid for a first-edition *Propaganda* | 0a89743f...md | 0:05 (verbatim: "spent $12,500 for this copy") |
| "the core strategies... don't shift... don't move when the algorithm changes" (25-year bulletproofing) | 156c576f...md | 11:29-11:44 (near-verbatim, light smoothing of spoken cadence) |
| Nautilus magazine, Elizabeth Towne, 200,000 copies of the Master Key System sold pre-internet | e111041c...md | 9:07-9:34 (verbatim) |
| Irving R. Allen, "10 Basic Laws" (1918, pre-dates Hill's Laws of Success), "healthy egotism" as prerequisite | c6416fe8...md | 0:20-2:34, 4:07 (verbatim) |
| Shower / concentrated-thought answer arriving unbidden | b7261d84...md and e111041c...md (corroborated in both) | 6:30-6:37 / 6:23-6:28 |
| "there's a grain of truth, but... when you hear the whole story, it's not the same outcome" (critics pattern) | 156c576f...md | 4:43-4:46 (verbatim); surrounding context (2:16-4:40) covers Napoleon Hill controversy, Tony Robbins FTC, Trump University as the worked examples |

## LIKELY (concept confirmed in source, exact phrasing not verbatim-matched this pass)

- Hill's course "develops the person before the hooks and headlines" and belief "comes through on the camera" — concept present in 156c576f...md (9:33-9:43 region) but the precise sentence in genius.md is a compressed paraphrase, not a verbatim string match.
- Bernays' *Propaganda* chapter-one opening ("we are governed, our minds are molded...") — this is the actual published opening line of the book; not independently re-verified against the transcript text in this repair pass (Brunson does discuss and hold up the book on camera across 0a89743f...md).

## UNCONFIRMED

- None. Every quote in genius.md's Genius Patterns and Hidden Knowledge sections that was checked this pass resolved to VERIFIED or LIKELY against the extracted source transcripts; nothing required an UNCONFIRMED demotion.

## Anti-Patterns Added This Repair (all VERIFIED against transcript timestamps)

1. Selling the process instead of the visualized outcome — 156c576f...md, 2025-05-29, 8:41-8:48
2. "Believing your own bio" (unchecked ego) preceding business collapse (Brunson's own 100-employee crash) — c6416fe8...md, 2025-07-12, 6:44-7:19
3. Selling features/benefits logically instead of emotionally (Bernays' WWI war-bonds case) — 0a89743f...md, 2025-05-31, 1:41-1:58
4. Leaving a negative connotation unaddressed instead of reframing it — 0a89743f...md, 2025-05-31, 8:31-8:43
5. Marketing on hope/ideas instead of real-money-tested prediction — 156c576f...md, 2025-05-29, 11:29-11:36
6. Scattering across every channel instead of concentrating one (Nautilus vs. "20 copies... Facebook, Instagram") — e111041c...md, 2025-07-23, 9:07-9:20
