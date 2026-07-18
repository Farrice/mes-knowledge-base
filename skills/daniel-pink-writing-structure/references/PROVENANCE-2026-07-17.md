# PROVENANCE — daniel-pink-writing-structure repair

Anchor → source file + location, for the new content added this repair (the 7
Anti-Patterns + the Model Calibration section). Full claim-by-claim confidence labels
for both new and pre-existing content: `references/source-ledger.md`.

Primary source (recovered this session, not previously extracted into `extractions/`):
`_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/2bf2299f-cbfd-4936-8b08-2bee19fc22e2.md`
("Daniel Pink | How to Write Something Truly Useful," claude.ai capture, 2026-01-14;
95,102 bytes). Reproduce with:
`tar -xzf _archive/claude-export-2026-07-01.tar.gz claude-export/normalized/conversations/2bf2299f-cbfd-4936-8b08-2bee19fc22e2.md`

| Anchor (in new content) | Source file | Location |
|---|---|---|
| "a mistake that some authors [make]... the world starts kind of pushing them in this direction... it might not be a good idea for them" (Anti-Pattern #1) | `2bf2299f-cbfd-4936-8b08-2bee19fc22e2.md` | body, paragraph beginning "Yeah. Okay. I'm glad you said that. All right. So, because it is a big it's a big commitment..." |
| "I would stare at it and stare at it and stare at it and say I have nothing to say" (Anti-Pattern #2) | `2bf2299f-cbfd-4936-8b08-2bee19fc22e2.md` | body, "When" structure-hunt paragraph beginning "Okay. So let's take let's take a book like uh when the book about the science of timing..." |
| "The biggest lie that writers will tell themselves is ah I'll remember that later" (Anti-Pattern #3) | `2bf2299f-cbfd-4936-8b08-2bee19fc22e2.md` | body, paragraph immediately after the "green socks" / treadmill research discussion, before the Podcast Magic sponsor read |
| "You had me till the present thing... that's a little too clever" (Anti-Pattern #4) | `2bf2299f-cbfd-4936-8b08-2bee19fc22e2.md` | body, "The Invisible Present" anecdote, paragraph beginning "But I wasn't getting any traction on it..." |
| "If I see one paper from an obscure journal... wearing green socks makes you more creative... a little bit more skeptical" (Anti-Pattern #5) | `2bf2299f-cbfd-4936-8b08-2bee19fc22e2.md` | body, paragraph beginning "You can get distracted and lost in it. There's no question about that..." |
| "if you listen to a transcript of people actually talking, that's totally boring" (Anti-Pattern #6) | `2bf2299f-cbfd-4936-8b08-2bee19fc22e2.md` | body, playwriting section, paragraph beginning "And what I like about plays also is the... compression..." |
| "many writers delude themselves into thinking their audience is everybody, and it's never everybody" (Anti-Pattern #7) | `2bf2299f-cbfd-4936-8b08-2bee19fc22e2.md` | body, book-proposal-structure paragraph beginning "It depends. It It depends. The most important thing..." |
| "writing is still really, really hard for me" / "sort of the tortured process that I go through" (Model Calibration texture) | `2bf2299f-cbfd-4936-8b08-2bee19fc22e2.md` | body, opening writing-routine paragraph and the *When*-structure-hunt paragraph, respectively |
| "gears don't mesh perfectly, it's not going to tell time" (Model Calibration engineering metaphor) | `2bf2299f-cbfd-4936-8b08-2bee19fc22e2.md` | body, playwriting section, "A play a play is I discovered it. Writing a play is like building a watch..." |
| Cross-reference: same transcript re-captured 2026-02-12 under "How to Write Structurally Well" | `claude-export/normalized/conversations/2d9a5291-20b3-4cbb-9b36-d6cf57a8d180.md` | frontmatter (`title:`) + body (identical transcript text, confirmed by diff-by-eye of the two files' raw transcript blocks) |

Every anchor above was verified by direct file read this session (both conversation
files were extracted from the tarball to scratchpad and read in full) before being
cited — no quote in this repair was taken from memory or inferred from the existing
`genius.md` prose alone.
