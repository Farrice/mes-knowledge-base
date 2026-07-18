# PROVENANCE — lara-acosta-content-system repair pass (2026-07-17)

Anchor → source file+location table for every new claim added this pass. Full
claim-by-claim ledger is `references/source-ledger.md`; this file is the
quick-reference index an adversarial verifier can spot-check against.

| # | Anchor (as written in genius.md) | Source file | Verbatim quote check |
|---|---|---|---|
| 1 | "People get this wrong all the time where they feel like they can only educate but never storytell." | `extractions/lara-acosta-content-system/transcript.txt` | Confirmed via `grep -o` against the live file this session. |
| 2 | "This defeats the typical viral LinkedIn slop which is like here's how to build a productivity app." | `extractions/lara-acosta-content-system/transcript.txt` | Confirmed via `grep -o`. |
| 3 | "most people don't poison them because they don't know how" | `extractions/lara-acosta-content-system/transcript.txt` | Confirmed via `grep -o`; flagged in-line as a likely transcription artifact for "post them" — quoted exactly as it appears, not silently corrected. |
| 4 | "Where people fail in the execution is that they'll try and copy a viral post but they won't copy it correctly. They won't emulate it..." | `extractions/lara-acosta-content-system/transcript.txt` | Confirmed via `grep -o`. |
| 5 | "That's how you kind of like beat that from being just generic AI fluff that Chat GPT writes." | `extractions/lara-acosta-content-system/transcript.txt` | Confirmed via `grep -o`. |
| 6 | "I was playing LinkedIn on hard mode because I was trying to be really cool and not really use any photos because I was like, I'm too good for that." | `extractions/lara-acosta-content-system/transcript.txt` | Confirmed via `grep -o`. |
| 7 | "There's too many LinkedIn personal branding experts right now talking about personal branding with 10,000 followers or thousand followers." | `extractions/lara-acosta-content-system/transcript.txt` | Confirmed via `grep -o`. |

## File sizes verified this pass (rule 2 — false "unrecoverable" claims are a
provenance failure in themselves)

```
$ wc -c extractions/lara-acosta-content-system/*.md extractions/lara-acosta-content-system/*.txt
    6720 extractions/lara-acosta-content-system/extraction-report.md
   25149 extractions/lara-acosta-content-system/transcript.txt
```

Neither file is 0 bytes or unrecoverable. Both were opened and read in full.

## Cross-source note (Hall of Fame Exemplar 1)

genius.md's Exemplar 1 ("I just handed my dad the keys...") is a constructed
illustration, not a transcript quote. Its opening beat echoes a real line from
a *different* extraction bucket — `extractions/lara-acosta/transcript.txt`
("today's the proudest day of my life, I retired my dad") — already VERIFIED
in `skills/lara-acosta-linkedin-growth/references/source-ledger.md`. Not
re-verified here as a new claim; flagged in-line in genius.md and in
`references/source-ledger.md` so it is never mistaken for a Cameron-transcript
quote.

## Auditor self-check (run this pass, not fabricated)

```
anti_patterns_sourced: 7 / 7 PASS
recognition_test: True — matched "recognize this as"
named_entity_floor: sections=13 zero_ratio=0.154 PASS (max 0.2)
source_ledger: references/source-ledger.md present, name-matches "ledger" — PASS
```
