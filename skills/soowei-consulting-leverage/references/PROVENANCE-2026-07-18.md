# PROVENANCE — soowei-consulting-leverage repair

Anchor → source file + location. All sources are inside
`_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes; verified `wc -c`, not
`wc -l`). `extractions/` has zero files matching `soowei`/`soo wei`/`soo-wei` — confirmed
by directory listing AND a per-member `tarfile` content scan of all 7,728 archive members
(script logic: `tarfile.open(...).getmembers()`, regex search on decoded bytes for
`soowei|soo\s*wei|soo-wei`, case-insensitive). 6 members matched; 5 are primary/duplicate
transcripts, 1 is a meta-conversation (excluded).

## Anchor table (genius.md Anti-Patterns section, in file order)

| Anchor (genius.md bullet) | Source member | Approx. char offset in extracted .md | Verbatim? |
|---|---|---|---|
| "you're building yourself a hamster wheel that you can't get off" | `09e3e3a2-87b5-4c81-9416-807bd8dcad2c.md` | ~3,507 | Yes, exact |
| "That's exactly why you guys are not making the money you want to make." | `09e3e3a2-87b5-4c81-9416-807bd8dcad2c.md` | ~10,845 | Yes, exact |
| "you are posting your content in the epher and hoping it sticks" | `09e3e3a2-87b5-4c81-9416-807bd8dcad2c.md` | ~26,121 | Yes, exact (source transcription artifact "epher" kept as-is) |
| "people could literally take my reel, put in the transcript, read the script word for word and have the same brand as me" | `09e3e3a2-87b5-4c81-9416-807bd8dcad2c.md` | ~34,193 | Yes, exact |
| "It's that awkward period. Get rid of it." | `09e3e3a2-87b5-4c81-9416-807bd8dcad2c.md` | ~15,320 | Yes, exact |
| "your appointment center doesn't even talk to the content person. Why? Like, why?" | `09e3e3a2-87b5-4c81-9416-807bd8dcad2c.md` | ~42,309 | Yes, exact |
| "I don't make any claims. I'm like, these are the results I get. You decide the claim that you want for yourself." | `09e3e3a2-87b5-4c81-9416-807bd8dcad2c.md` | ~45,378-45,650 | Contiguous, one word trimmed (source stutters "I I don't" — kept second "I", rest verbatim) |

## How the anchors were pulled

1. `ls extractions/ | grep -i soowei` / `soo wei` / `soo-wei` → 0 hits (confirmed empty,
   not a scan failure — `extractions/` directory exists and lists normally for other
   experts).
2. Per envelope Rule 2, ran a Python `tarfile` per-member content scan (not filename scan)
   over `_archive/claude-export-2026-07-01.tar.gz` — 7,728 members, regex
   `soowei|soo\s*wei|soo-wei` case-insensitive against raw decoded bytes of every file
   member (size-bounded to skip >20MB members, none of which were relevant here).
   6 hits, all `.md` conversation exports.
3. Extracted all 6 hit members to scratchpad, read each in full via the Read tool.
   `09e3e3a2-87b5-4c81-9416-807bd8dcad2c.md` is the primary masterclass transcript
   directly matching this skill's domain ("consulting-leverage" ↔ "$2m/yr profit
   consulting business"); it is the source for every quoted anti-pattern anchor.
4. Cross-checked all 15 originally-existing genius.md patterns (1-15) against this same
   transcript — all 15 have a direct verbatim or near-verbatim basis (see
   `references/source-ledger.md` claim table). Pattern 16 does NOT have a verbatim basis
   in any of the 5 primary/duplicate transcripts — flagged LIKELY in both genius.md
   (inline provenance note) and the ledger, not silently upgraded to VERIFIED.
5. Every quote above was located via Python substring search (`text.find(needle)`) against
   the actual extracted file content before being written into genius.md — none were
   typed from memory or reconstructed from the assistant's own extraction summary in the
   conversation (which would risk quoting the *extractor's paraphrase* rather than
   SooWei's actual words).

## What was NOT re-verified in this pass (named as gap, not silently skipped)

- The 42 files under `references/prompts/`, `references/prompts-v2/`, and
  `references/_legacy-prompts/` (14 workflows × 3 variants) were not individually
  re-audited against transcript quotes — out of scope for a 3-check repair pass (the
  failing checks were anti_patterns_sourced, recognition_test, source_ledger; workflow
  contracts and named-entity floor were already passing per the audit). Logged as LIKELY
  in the ledger rather than claimed VERIFIED.
- Hall of Fame Exemplars and Signature Moves in genius.md predate this repair and read as
  synthesized illustrations, not verbatim transcript scenes — labeled LIKELY, not altered
  (additive-only boundary; not a failing check).
