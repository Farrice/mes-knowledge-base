# PROVENANCE — robert-mack-comedy-writing repair

Anchor → source file + location. All quotes below are verbatim substrings of
`extractions/comedy-writing/transcript.txt` (60,090-char single-line file), confirmed via
direct Python string search (`str.find`), not assumed.

| Anchor text (as used in genius.md) | Location in transcript.txt (char offset) |
|---|---|
| "If I say Romeo, you think Juliet. If I say peanut butter, jelly." | ~11184 |
| "That guy's seven feet tall... the audience knows it before he's even taken the mic" | ~16400–16750 |
| "If I did an Ella Fitzgerald reference that wouldn't work, but if I did Beyoncé it would" | ~38385–38460 |
| "I can make Polish jokes because I'm Polish... I can't make a Mexican joke" | ~39267–39330 |
| "The only way to get rid of that stench is to perform another show" | ~53644–53660 |
| "a bad storyteller shares the wrong details and gets caught up on the wrong details" | ~47804–47892 |
| "You don't need to know what he was wearing, where he was driving to, what day of the week it was" | ~47411–47510 |
| "Uniform. Too serious. There's none of the roleplaying" | ~23813–23860 |
| "people shouldn't slip on banana peels... didn't get up and a pool of blood started" | ~39778–39900 |
| "this little story from Louis CK" (taxi-driver bit framing) | ~45750 |
| "close talker... this is from Seinfeld which he obviously worked on" | ~30455–31150 |
| "winning isn't funny... Charles Schultz" | ~14520–14544 |

Source files:
- `extractions/comedy-writing/transcript.txt` (60,090 bytes)
- `extractions/comedy-writing/extraction-report.md` (18,814 bytes, 218 lines)

Full ledger with VERIFIED/LIKELY/UNCONFIRMED labels per claim: `references/source-ledger.md`
in this same output directory. One attribution — "(Rodney Dangerfield)" on the nurse-outfit
exemplar quote — is flagged UNCONFIRMED there: the joke itself is verbatim in the transcript
but the transcript gives no attribution, and "Rodney Dangerfield" does not appear in the file.
That pre-existing line was left untouched (additive-only boundary; it was not part of a
failing check) but is now honestly labeled instead of silently carried forward.
