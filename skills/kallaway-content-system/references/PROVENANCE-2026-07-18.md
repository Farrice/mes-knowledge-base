# PROVENANCE — kallaway-content-system repair

Anchor → source file + location, for every quote/claim added or preserved this pass.
All quotes located via `grep -n` against `extractions/kallaway-content-system/transcript.txt`
(43,221 bytes, `wc -c` verified) and confirmed by reading surrounding context before citing.

| Anchor text (as it appears in genius.md) | Source | Location |
|---|---|---|
| "The topic should not be at the category level." | transcript.txt | L204 |
| "hooks or storytelling or Nike or Apple... that's way too broad" | transcript.txt | L372 |
| "I find AI is good at regurgitating what it's been trained on and what it's heard." | transcript.txt | L472 |
| "It's not great at coming up with novel things outside the box." | transcript.txt | L474 |
| "I don't recommend combining multiple creators here because oftentimes... speaking patterns are like fingerprints." | transcript.txt | L688 |
| "If you combine examples from all three, it'll confuse the writer and make it generic." | transcript.txt | L692 |
| "You cannot be editing." | transcript.txt | L804 |
| "It's too low leverage of a task for you as the creator to be doing it." | transcript.txt | L806 |
| "You're not going to run all 10 like that cuz it's going to get way too repetitive for you and the viewer." | transcript.txt | L952 |
| "my process is if I don't have an original idea I want to make, I'm always starting with this list" | transcript.txt | L222 |
| "one video flopping and one crushing in the exact same hook, but one has title text and one doesn't" | transcript.txt | L452 |
| "To make one video, I go through the same six stages every single time." | transcript.txt | L44 |
| S-tier rank format contrarian-take example | transcript.txt | L504-512 |
| "Constraints breed creativity is like a common frame." | transcript.txt | L516 |
| "It's not that AI is going to remove human creativity." / "It's that it frees up human creativity." | transcript.txt | L830, L832 |
| Duration 32:47 / 1967 seconds, acquired 2026-05-07 | references/source-map.md (pre-existing, unmodified) | L3-8 |

## Explicitly UNCONFIRMED (not anchored, not fabricated)

| Claim | Status | Reason |
|---|---|---|
| "Moving to scripting before format is locked" (Anti-Pattern bullet) | UNCONFIRMED | No direct transcript quote located after searching "before format", "scripting", "too early/soon" variants. Left as an unsourced bullet in genius.md rather than force a citation. |
| "Repeating the same message across visual, text, and spoken hook" (Anti-Pattern bullet) | UNCONFIRMED | Hook Triad Coordination pattern (L564) defines the three distinct layers but no explicit anti-repetition warning was found in the transcript. Left unanchored. |

## Files checked but NOT cited (verified present, not needed as sources)

| File | Size (wc -c) | Why not used |
|---|---|---|
| `extractions/kallaway-content-system/B9l9TRhu5Vw.en-orig.vtt` | 398,725 bytes | Raw captions; transcript.txt is the cleaned derivative and sufficient for every claim above |
| `extractions/kallaway-content-system/integrity-patch.md` | 5,108 bytes | Documents a different skill (`kallaway-trend-hook-engine`), not this one — excluded to avoid cross-skill provenance contamination |
| `extractions/kallaway/*` | n/a | Belongs to `kallaway-ai-content-engine` / `kallaway-word-mastery`, out of scope |

No "source is absent" claim was made anywhere in this repair without first opening the file and recording its size (see table above), per Envelope Rule 2.
