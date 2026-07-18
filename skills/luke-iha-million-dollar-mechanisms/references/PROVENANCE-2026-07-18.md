# Provenance — luke-iha-million-dollar-mechanisms repair (2026-07-18)

Anchor → source file + location. Full per-claim ledger with VERIFIED/LIKELY/UNCONFIRMED labels: `references/source-ledger.md`.

| Anchor (genius.md location) | Source file | Location in source | Label |
|---|---|---|---|
| "How to Use This Skill" — jargon quote | `extractions/luke-iha/video-1-proof-mechanisms/transcript.txt` | mid-transcript, jargon-flurry example passage | VERIFIED |
| "How to Use This Skill" — Stefan Georgi mentor quote | `extractions/luke-iha-insight-mastery/transcript.txt` | opening third, mentor-origin passage | VERIFIED |
| "Core Belief" — "one of the most powerful concepts..." / "Genesis" | `extractions/luke-iha-insight-mastery/transcript.txt` | opening lines of transcript | VERIFIED |
| "How Luke Thinks About Mechanisms" — mentor quote (2nd use) | `extractions/luke-iha-insight-mastery/transcript.txt` | same mentor-origin passage as above | VERIFIED |
| "Operating Principle 1 (Simple > Accurate)" — curcumoids quote | `extractions/luke-iha/video-1-proof-mechanisms/transcript.txt` | jargon-flurry example passage | VERIFIED |
| "Operating Principle 3 (UMP)" — "deeper problem mechanism" / "why behind the problem" | `extractions/luke-iha/video-3-levels-of-awareness/transcript.txt` | hook→payoff→mechanism structural walkthrough | VERIFIED |
| "Operating Principle 5 (One Mechanism)" — metabolism reversal quote | `extractions/luke-iha-insight-mastery/transcript.txt` | causation-reversal example, mid-transcript | VERIFIED |
| "Operating Principle 6 (Validation Triangle)" — "60-second story" | `extractions/luke-iha/video-7-million-dollar-mechanisms/extraction-report.md` | section 1.8, Mechanism Validation Triangle | LIKELY |
| AP1 — Complexity Flex | `extractions/luke-iha/video-1-proof-mechanisms/transcript.txt` | jargon-flurry example passage | VERIFIED |
| AP2 — Bare Claim | `extractions/luke-iha/video-1-proof-mechanisms/transcript.txt` | "explanatory reasoning" passage (proof weapon #3) | VERIFIED |
| AP3 — Unbridged Borrow | `extractions/luke-iha/video-1-proof-mechanisms/transcript.txt` | sauna/borrowed-authority passage | VERIFIED |
| AP4 — First-Order Causation | `extractions/luke-iha-insight-mastery/transcript.txt` | causation-reversal example, mid-transcript | VERIFIED |
| AP5 — Missing Reveal | `extractions/luke-iha/video-3-levels-of-awareness/transcript.txt` | Flexner report / grounding worked example | VERIFIED |
| AP6 — Unnamed Mechanism | `extractions/luke-iha/video-7-million-dollar-mechanisms/extraction-report.md` | section 3, HK1 | LIKELY |

## Absence check (per envelope Rule 2: verify before claiming absence)

Ran `find extractions/luke-iha/video-7-million-dollar-mechanisms -type f` → returned only `extraction-report.md`. Ran `wc -c` on it → 13,953 bytes (non-trivial, readable, not corrupted). No `transcript.txt` exists for this specific video anywhere under `extractions/`. This absence is file-system-verified, not inferred.

## Verbatim spot-check method

Every quote listed above was located with `grep -o "<exact string>" <path>` against the live source file before being written into genius.md, confirming byte-for-byte match (including source typos like "liposomaal" and transcript filler like "uh"). No quote was reconstructed from memory or approximated.
