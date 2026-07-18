# PROVENANCE — sam-parr-taste-acquisition repair (wave3-lane4-b15)

Anchor → source file + location, for every new quote/claim added to `genius.md` in
this repair (the "How to Use This Skill" and "Anti-Patterns (Sourced)" sections).

| Anchor (as it appears in genius.md) | Source file | Location |
|---|---|---|
| "It would be impossible, right? Like, you can't like write a song that way." | `extractions/sam-parr/transcript.txt` | Instrument-teaching passage (piano handed cold, no framework). |
| "for months" (Boron Letters / Great Gatsby / SNL scripts copywork) | `extractions/sam-parr/transcript.txt` | Same passage, immediately following the instrument metaphor: "you copy it word for word... I did this for months... Boron letters... The Great Gatsby... SNL scripts." |
| "you have to feel the texture actually. There's science that shows you remember things more by being physical... than typing." | `extractions/sam-parr/transcript.txt` | Immediately after the "write it down" exchange, same interview segment as the Blind Copy Protocol. |
| "you see the rules of how other and the texture of how other people do it" | `extractions/sam-parr/transcript.txt` | Instrument-teaching passage, describing moving through Foo Fighters / Green Day / Lady Gaga before the pattern surfaces. |
| "you learn jingle bells by copying it and then you learn maybe happy birthday and then a little bit more complicated" | `extractions/sam-parr/transcript.txt` | Same instrument-teaching passage, teaching-sequence portion. |
| "That's a pretty bad ad for this one." / "Nightly Rest is within arm's reach... the nightly drink for restorative sleep." | `extractions/sam-parr/transcript.txt` | Live AG1/AGZ sleep-supplement ad-rewrite segment ("bad ads" section). |
| "so basic" / guy who knows "a handful of songs on his guitar" is "still the coolest guy there" | `extractions/sam-parr/transcript.txt` | Same "bad ads" segment, immediately preceding the AG1 rewrite. |
| 2026-04-09 — genius.md and transcript.txt both first added same commit | git history | `git log --diff-filter=A --format="%ad %h" --date=short -- skills/sam-parr-taste-acquisition/genius.md` and same command against `extractions/sam-parr/transcript.txt` → both `2026-04-09 e615c3013`. |
| 2026-05-30 — copywriting-extraction.md added (postdates genius.md) | git history | `git log --diff-filter=A --format="%ad %h" --date=short -- extractions/sam-parr/copywriting-extraction.md` → `2026-05-30 205d3dc14`. |

All quotes above were located via direct Python substring/`.find()` search against the
live text of `extractions/sam-parr/transcript.txt` and read in surrounding context
before use — none were taken from a prior draft or from genius.md's own pre-existing
(unverified) claims. Full absence-check methodology (including the `_archive/claude-
export-2026-07-01.tar.gz` per-member content scan for the skill's UNCONFIRMED
Bauhaus/Dr.-Dre/fashion-journey content) is documented in `references/source-ledger.md`.
