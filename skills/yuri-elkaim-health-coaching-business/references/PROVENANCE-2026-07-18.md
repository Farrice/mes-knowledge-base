# Provenance — yuri-elkaim-health-coaching-business repair

Anchor → source file + location. All sources are timestamped YouTube-transcript
conversation exports inside `_archive/claude-export-2026-07-01.tar.gz` (path:
`claude-export/normalized/conversations/<uuid>.md`), located via a python
`tarfile` per-member content scan for "elkaim"/"healthpreneur" (no match under
`extractions/` — confirmed absent by directory listing before falling back to
the archive, per envelope source-search discipline).

| Anchor (genius.md) | Source file | Timestamp | Verbatim substring located at |
|---|---|---|---|
| "a lot of people are making the mistake and doing too much too soon" | `06ecf597-fa67-49ce-9da9-36bda86e2770.md` | 20:29 | lines 638–639 |
| "one of the worst things you can spend your timeline" | `3c7fe82a-5236-4429-bae9-51d8756a6ede.md` | 16:14 | lines 502–503 |
| "this is one of the worst things you can do when building" | `b2443ff5-76db-482b-93f0-f811b110873e.md` | 11:16 | lines 330–332 |
| "if you've never worked with a paying client and you start running ads, um, you're going to lose your shirt very quickly" | `d91d258e-903f-4679-8a6c-0c4473832990.md` | 4:58–5:03 | lines 155–159 |
| "chasing external validation whether it's in numbers or people praising your work — you will fail because you will give up very quickly" | `dcbc85af-a5d5-4390-8eb0-d39451094c44.md` | 9:45–9:52 | lines 310–313 |
| "it's not copy paste out of Chatty G onto whatever platform it's to avoid the blank screen" | `dcbc85af-a5d5-4390-8eb0-d39451094c44.md` | 16:30–16:35 | lines 504–506 |
| "the only thing more dangerous than free advice is the wrong advice" | `d91d258e-903f-4679-8a6c-0c4473832990.md` | 17:45–17:50 | lines 531–532 |
| "published more than 3,000 videos on YouTube alone" | `dcbc85af-a5d5-4390-8eb0-d39451094c44.md` | 19:13 | line 572 |
| "took me 7 years to make my first million dollars" | `06ecf597-fa67-49ce-9da9-36bda86e2770.md` | 18:53–18:56 | lines 590–591 |
| "helped half a million people" | `b2443ff5-76db-482b-93f0-f811b110873e.md` | 12:09 | line 354 |
| 625 opted in / ~20 finished (The Trade beta) | `dcbc85af-a5d5-4390-8eb0-d39451094c44.md` | 29:52 / 30:08–30:15 | lines 871, 875–889 |

Full extraction procedure (repeatable):
```python
import tarfile
with tarfile.open("_archive/claude-export-2026-07-01.tar.gz", "r:gz") as tf:
    for member in tf:
        if member.isfile() and 0 < member.size <= 5_000_000:
            text = tf.extractfile(member).read().decode("utf-8", errors="ignore").lower()
            if "elkaim" in text or "healthpreneur" in text:
                print(member.name, member.size)
```
Returned exactly 6 members, all listed in `references/source-ledger.md` S1–S6.
File sizes there are `wc -c` byte counts (not `wc -c` line counts) per envelope
instruction — none are 0-byte or truncated.
