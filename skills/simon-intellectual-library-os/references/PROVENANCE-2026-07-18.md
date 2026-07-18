# PROVENANCE — simon-intellectual-library-os repair (Wave 3 Lane 4 Batch 16)

Ground truth used: `extractions/systems-made-better/` (extraction-report.md, transcript-claude-kb.txt,
transcript-notion-advisors.txt) + `skills/simon-intellectual-library-os/references/source-quotes.md`
(pre-existing verbatim quote bank, already VERIFIED/LIKELY/UNCONFIRMED-labeled). No new external
sources were consulted — all anchors below trace to files already inside the skill's own extraction
folder. `wc -c` sizes recorded to confirm these are real, non-empty files (not "unrecoverable/0-byte"
claims):

| File | Size (wc -c) |
|---|---|
| extractions/systems-made-better/extraction-report.md | 21,261 bytes |
| extractions/systems-made-better/transcript-claude-kb.txt | 36,717 bytes |
| extractions/systems-made-better/transcript-notion-advisors.txt | 38,170 bytes |
| skills/simon-intellectual-library-os/references/source-quotes.md | (pre-existing, unmodified) |

## Anchor → source table (anti_patterns_sourced, 8/8 anchored)

| genius.md anti-pattern | Quote used | Source |
|---|---|---|
| The bookmark graveyard | "We find something brilliant, we save it, and then we lose it." | `references/source-quotes.md` line 9 (V2, "Build A Claude Knowledge Base That Self-Improves!", 2026) |
| Human-as-librarian | "The problem with something like Notion or Obsidian to manage a second brain... is that they kind of ask you to be the librarian. You organize things yourself" | `references/source-quotes.md` line 8 (V2, 2026) |
| Generic-with-a-process | "Without the knowledge base, I found that the AI tends to just be still a bit generic but with a very clear process that it is following." | `references/source-quotes.md` line 15 (V1, "Turn Books Into AI Business Advisors (Full Notion Demo)", 2026) |
| Un-gated advisors | "make sure that the knowledge base we've created is directly referenced as a linked view early on ensuring that that is a mandatory step before it answers anything" | `extractions/systems-made-better/transcript-notion-advisors.txt` (verified via `grep -no` search, verbatim match; V1, 2026) — not previously in source-quotes.md, pulled fresh from the primary transcript |
| Multi-idea entries | "it goes through it extract atomize normalize into knowledge base entries... on each section extract all the information from within it atomize, so go what are the key concepts to take out" | `extractions/systems-made-better/transcript-notion-advisors.txt` (verified via `grep -no` search, verbatim match; V1, 2026) — pulled fresh from the primary transcript |
| Token bloat | "Before we now begin the ingest, please update your instructions thoughtfully and without creating too much token bloat" | `references/source-quotes.md` line 34 (V1, 2026) |
| Trust-by-default automation | "A lot of us won't want to be spending credits like this... go and make yourself a skill that does exactly that and then you can just trigger it with personal agent once a month... it's a hell of a lot cheaper." | `references/source-quotes.md` line 48 (V1, 2026) |
| Static libraries | "The AI will sometimes write something slightly wrong. You'll save it back and the next answer quietly builds on a mistake." | `references/source-quotes.md` line 42 (V2, 2026) |

The two anchors not already in `source-quotes.md` (un-gated advisors, multi-idea entries) were verified
directly against `extractions/systems-made-better/transcript-notion-advisors.txt` via targeted `grep -no`
before use — quoted verbatim, no paraphrase, no invented provenance. Both transcripts are continuous
single-line text files (`wc -l` = 0, no embedded newlines), so citation is by file, not line number —
consistent with how the pre-existing `source-quotes.md` cites the same two videos.

## "How to Use This Skill (Model Calibration)" section
Modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 (structure only — intuition primitives,
never announce the machinery, expert-specific texture, polish-is-the-tell). Content is net-new, written
against Simon's own demonstrated behaviors already documented in this skill's genius.md (mandatory
KB-read gate, empty-KB refusal test, the Obsidian-vault floor anchor, demo-first plain-spoken texture) —
no quotes invented, no new claims beyond what genius.md's existing Identity/Anti-Patterns/Calibration-
Anchors sections already assert.
