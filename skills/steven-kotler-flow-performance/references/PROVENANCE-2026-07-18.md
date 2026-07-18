# PROVENANCE — steven-kotler-flow-performance repair (2026-07-18)

Anchor → source file + location, for every new claim added by this repair
(the 6 Anti-Patterns items in `genius.md`). Pre-existing skill content is
unchanged and not re-listed here (see `references/source-ledger.md` for its
labels).

| Anti-pattern anchor (genius.md) | Source file (archive member) | Location |
|---|---|---|
| "psychology... they're metaphor... but there's still metaphor" / "what works for me will work for you" | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/8338117f-f0a5-4760-bc80-b3b6fee81822.md` | transcript timestamps 0:32-1:43 |
| Ski body-position self-consciousness story ("How did I look?" → speed metric) | same archive → `8338117f-f0a5-4760-bc80-b3b6fee81822.md` | transcript timestamps 35:48-37:04 |
| "15 minutes to get back into flow, if they can get back in at all" | same archive → `8338117f-f0a5-4760-bc80-b3b6fee81822.md` | transcript timestamps 33:53-33:58 |
| "Type A types... 10%, 20%, 30% greater... simply for the thrill of it" | same archive → `7c705b11-9e4c-43a3-9ef7-2e361e6ade05.md` | transcript timestamps 20:23-20:51 |
| "earn enough money to pay your bills and have a little leftover for fun" | same archive → `7c705b11-9e4c-43a3-9ef7-2e361e6ade05.md` | transcript timestamps 23:45-23:52 |
| "transient hypofrontality... temporary deactivation of the prefrontal cortex" | same archive → `8338117f-f0a5-4760-bc80-b3b6fee81822.md` | transcript timestamps 34:40-34:48 |

## How these were found (method, not claimed from memory)

1. `ls extractions/ | grep -i kotler` → no match. No `extractions/` folder for this expert.
2. Per the envelope's SOURCE-SEARCH DISCIPLINE, scanned `_archive/claude-export-2026-07-01.tar.gz`
   (confirmed 332,779,255 bytes via `wc -c`, not `wc -l`) with a Python `tarfile` per-member
   CONTENT scan (case-insensitive `kotler` regex over all 7,728 members) rather than trusting
   filenames (members are UUID-named).
3. 7 members matched. 6 are genuine Kotler-interview transcripts (2 pairs are duplicate
   extraction passes of the same two source videos); 1 (`73de793e-...md`, "Advanced code
   extraction protocol") is an unrelated conversation with a single incidental "Kotler" mention
   and was excluded as a source.
4. Extracted the 6 relevant members to `.tmp/wave3-lane4-b16/scratch/kotler_sources/` (worker
   scratch — not part of the delivered skill) and grep-verified each quote's exact wording and
   timestamp before using it as an anti-pattern anchor.
5. Every quote above was read directly from the extracted transcript text in this session —
   none were reconstructed from memory or paraphrased into a "quote."
