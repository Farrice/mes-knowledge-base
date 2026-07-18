# Provenance — steven-young-consciousness repair

Archive: `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, confirmed via `wc -c`).
Primary transcript file: `claude-export/normalized/conversations/58c6c715-a4fb-43be-bcf2-88c234668b68.md` (174,728 bytes, confirmed via `wc -c` — never `wc -l`).
Corroborating duplicate: `claude-export/normalized/conversations/1798e41b-541c-4672-8a58-c92786a54223.md` (176,259 bytes).

Extracted to local scratch for read access: `/private/tmp/claude-501/-Users-farricecain-Google-Antigravity/28d76098-a0d8-475f-bc8a-9609aae4b6f1/scratchpad/steven-young-src/` (not part of the deliverable; read-only working copy).

## Anchor → Source Table (new Anti-Patterns section, genius.md)

| Anchor (genius.md bullet) | Quote | Source file | Lines |
|---|---|---|---|
| Chasing the goal directly | "That way of doing it traps you in the forever loop. It keeps you on the hamster wheel. It keeps you on the pendulum. We were never taught how to go at things obliquely" | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 993-1000 |
| Managing/processing emotion instead of removing judgment first | "We were basically told either what's wrong or stop crying. And so we've been conditioned to essentially repress and suppress our emotions" | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 861-864 |
| Intellect substituting for felt experience | "I was deeply intellectual simply as a way so that I don't feel all the pain and hurt and fear and anger and grief that was in me" | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 884-887 |
| Leaving judgment vocabulary intact | "There's so much language around good, bad, right, wrong, positive, negative... let go of those six words. Literally, just don't use them anymore" | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 1403-1409 |
| Praising "potential" | "In their mind, they're like, 'You have so much potential.' But what they also just said was, 'You're not there yet'" | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 929-933 |
| Fixating on the control-mechanism narrative | "I fall into that trap sometimes, man. I'm a human" | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 1512-1513 |

## Anchor → Source Table (pre-existing Genius Patterns / Hidden Knowledge, re-verified during this repair)

| Claim | Source file | Lines |
|---|---|---|
| "how was your massage?" origin story | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 309-321 |
| NASA-engineer Kabbalist / light-at-an-angle metaphor | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 973-989 |
| "programmed to exist in a context of judgment" / six words | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 1403-1409 |
| "hard worker" → "problem solver" identity | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 218-232 |
| 9,000+ patients | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 202, 1208 |
| 70% light / junk DNA | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 61-67, 747-768 |
| "casting different spells" / trauma-vulnerability reframing | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 583, 919-943 |
| "remembering of what was" / "remembrance, not a learning" | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 1496, 335 |
| Dream Day / 2028 journal entry | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 2558-2566 |
| Ho'oponopono / "I love you, God" / "resourced" | `58c6c715-a4fb-43be-bcf2-88c234668b68.md` | 1450-1477, 2969 |

Full claim-by-claim VERIFIED/LIKELY/UNCONFIRMED breakdown: `references/source-ledger.md`.

## Absence Check (per envelope Rule 2)

`extractions/` was searched via `ls extractions/ | grep -i "steven\|young"` — zero matches (only `extractions/steven-pressfield` exists, a different expert). This is recorded as a checked fact: the directory was listed and grepped, not assumed empty. The archive scan (below) is what surfaced the real source.

Full-archive scan method: Python `tarfile`, iterating all 7,720 members, reading each file's bytes and regex-matching `steven\s+young` case-insensitive on content (not filename). 6 hits total; 5 are `.md` conversation files, 1 is the raw `conversations.json` (867,859,945 bytes, not opened directly — the normalized `.md` exports were used instead). Of the 5 `.md` hits, 2 contain actual timestamped transcript dialogue (the primary + duplicate above); the other 3 were confirmed by grep to contain zero timestamp-pattern lines and are downstream prompt-request conversations, not source material.
