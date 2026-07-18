# Provenance — kunal-shah-consumer-psychology repair

| Anchor (genius.md, Anti-Patterns section) | Source file | Location |
|---|---|---|
| "just by adding tech it doesn't become delta four..." | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/366b1ef4-cb21-4983-93d1-9492d0f0b835.md` | transcript body, ~char 49,000 (shirt-buying passage) |
| "i see 90 of them fail all the time..." | same tarball member | ~char 49,780 |
| "netflix made the mistake of coming to india..." | same tarball member | ~char 15,860 (value-per-hour/Netflix passage) |
| "i've not seen people come out of that trap... envy is hyper local..." | same tarball member | ~char 83,440 |
| "when you reduce the concentration of people with very high slope..." | same tarball member | ~char 126,800–127,100 |
| "i can't even risk one percent of my reputation..." | same tarball member | ~char 9,600 |

Local extracted copy used for verification: `.tmp/wave3-lane4-b9/kunal-shah-consumer-psychology/_src/src-366b.md` (190,012 bytes, byte-identical to the tarball member). Full ledger with claim-by-claim VERIFIED/LIKELY status: `references/source-ledger.md`.

Discovery method (per envelope discipline): filename search (`find`, `grep -l -i kunal`) returned zero hits — the source lives inside a conversation body, not a filename. Recovered via `python3` + `tarfile`, iterating all 7,728 members and content-decoding each `.md`/`.txt`/`.json` file, matching on `kunal`, `shah`+(`cred`|`freecharge`), and `delta-4`/`delta 4`.
