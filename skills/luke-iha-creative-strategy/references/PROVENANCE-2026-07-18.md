# Provenance — luke-iha-creative-strategy repair

Anchor → source file+location, for every quote added this repair.

| Anchor (genius.md location) | Quote | Source file | Verified how |
|---|---|---|---|
| Model Calibration section | "what sensation do you feel, something in your chest, in your gut, in your neck" | `extractions/luke-iha-client-acquisition/transcript.txt` | `grep -o "what sensation[^.]*"` exact match |
| Anti-Patterns — Mechanism-First Hook | "a mistake that people do is they try to put that mechanism first... there needs to be relevance in the very very first line" | `extractions/luke-iha-hooks/transcript.txt` | `grep -o "a mistake that people do is[^.]*\.[^.]*\."` exact match |
| Anti-Patterns — The Give-Away Hook | "if they can make an educated guess and feel confident in their guess of what you're going to say, then they have no business to actually read the ad" | `extractions/luke-iha-hooks/transcript.txt` | `grep -o` exact match (transcript reads "make a a an educated guess" — stutter normalized to "an educated guess" in the anchor quote, meaning preserved, same clause) |
| Anti-Patterns — Dribbling Instead of the Kill | "You don't want there to be any pause, no hesitation. You need to go directly to the kill and don't let go until that person buys." | `extractions/luke-iha-hooks/transcript.txt` | `grep -o` exact match |
| Anti-Patterns — Skipping Profile/Portfolio Completion | "It blows my mind how many times I tell people to fill out their profile to 100% completion and they don't do it." | `extractions/luke-iha/video-2-creative-strategy/transcript.txt` | `grep -o` exact match |
| Anti-Patterns — Calcifying Into Cheap Long-Term Gigs | "you don't want to get stuck in these long-term arrangements... get quick jobs that you can get in and out to get the review" | `extractions/luke-iha/video-2-creative-strategy/transcript.txt` | `grep -o` exact match (ellipsis joins two adjacent sentences from the same passage) |
| Anti-Patterns — Never Questioning Sacred Cows | "there's types of myths and sacred cows, things that you're never supposed to question." | `extractions/luke-iha-hooks/transcript.txt` | `grep -o` exact match |
| Anti-Patterns — Adding Polish Instead of Subtracting the Block | "the insight that was given to my friend was no, you don't need to add anything, you actually need to subtract what's holding you back." | `extractions/luke-iha-insight-mastery/transcript.txt` | `grep -o` exact match |
| Anti-Patterns — Generic "Here's My Work" Portfolio | (no new quote — cross-references genius.md's own pre-existing Anti-Exemplar prose in the Hall of Fame Exemplars section) | `skills/luke-iha-creative-strategy/genius.md` (pre-existing content) | direct Read of the file; this is a self-reference, labeled LIKELY in the ledger, not VERIFIED against an external transcript |
| Decision Stack cluster (Diamond and the Bullseye, cited in genius.md's existing 2026-07-01 section, unchanged this repair) | "the diamond is all about Clarity... Clarity is King it will always be king you can never sacrifice Clarity" | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/c00a368c-3395-4a7f-8e07-05db430fdc40.md` | extracted single conversation file from the 332MB archive via `tar -xzf ... claude-export/normalized/conversations/c00a368c-....md`, then `grep -n` confirmed the passage — done to spot-check the pre-existing claim's provenance, not to add a new anchor |

## Gap named, not fabricated

The rest of the "Patterns from claude.ai export — Luke Iha conversations
(2026-07-01)" section in genius.md (Seven-Layer Decision Stack, Test
Economics, Reverse Beat Map + UMP Trigger, Character Casting, Micro-Lead
Multiplication, upstream review order, AI expectation ratchet) cites a
second source — "6 Advanced Marketing Lessons $100MM Copywriters (Genesis
certainty-call recording)" — that this repair pass could NOT locate. The
archive tarball exists (332,779,255 bytes, 3,864 files) and one conversation
from it was opened and verified (the Mega Prompt file above); the specific
"6 Advanced Marketing Lessons" conversation was not found via the indexed
triage/JSON files and a full-archive grep was outside this repair's scope.
This is recorded as UNCONFIRMED in `references/source-ledger.md` rather than
silently left with an unverifiable anchor — per the envelope's hard rule,
these existing claims were NOT touched, deleted, or re-anchored; the gap is
named for the conductor/next pass, not hidden.
