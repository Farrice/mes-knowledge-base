# Source Ledger — mark-forsyth-rhetoric

Every source consulted for this repair pass, claim-by-claim, labeled VERIFIED / LIKELY / UNCONFIRMED. This skill is a BOOK-framework skill (*The Elements of Eloquence* and siblings) — the raw book text and the raw interview transcript are both deliberately absent from this repo. Ground truth for this repair = (1) the skill's own pre-existing material in `genius.md`/`SKILL.md`, which the repo's own provenance note says was built from a transcript read in an earlier session, and (2) checkable publication facts verified fresh via web search on 2026-07-18.

## Primary source claimed by the skill (not re-read this session)

- **David Perell "How I Write" — Mark Forsyth interview.** Title "You're Using the English Language Wrong — Mark Forsyth," youtube.com/watch?v=ulhrXgpjveA. **VERIFIED** that this video exists, its title, and its channel (David Perell) via WebSearch on 2026-07-18. **UNCONFIRMED** (this session) that every genius-pattern quote inside `genius.md` is a verbatim transcript match — I did not fetch or read the transcript itself this session. `agents/mark-forsyth/memory/context.md` (repo file, 1,050 bytes per `wc -c`) records that the skill's original patterns were "extracted twice in the export (2025-05-04 and 2025-10-12 sessions)" from this interview; that provenance claim is itself **LIKELY** (consistent, internally cited, not independently re-verified against a transcript file because none exists in the repo — confirmed absent by `grep -rl "ulhrXgpjveA"` and `find -iname "*forsyth*"` across the repo, 2026-07-18, both returning only the skill/agent/command files themselves, no transcript).
- Public-domain quotations already embedded in `genius.md` prior to this repair (Bond "James Bond," JFK inaugural chiasmus, "I came, I saw, I conquered," "Please please me," McCartney's "Here, There and Everywhere" manuscript anecdote, etc.) are **LIKELY** accurate as commonly-cited public quotations/anecdotes; not independently re-verified against primary recordings this session.

## Publication facts (verified fresh, 2026-07-18, via WebSearch)

- ***The Elements of Eloquence: How to Turn the Perfect English Phrase*** — Mark Forsyth, Icon Books, UK, 2013 (US edition: Berkley/Penguin Random House, ISBN 9780425276181). **VERIFIED** via Icon Books, PenguinRandomHouse.com, and Amazon catalog listings.
- ***The Etymologicon: A Circular Stroll Through the Hidden Connections of the English Language*** — Mark Forsyth, Icon Books, late 2011. **VERIFIED** via Icon Books catalog and secondary coverage of the book's reception (Channel 4 / BBC 2 / Christmas bestseller coverage).
- ***The Horologicon: A Day's Jaunt Through the Lost Words of the English Language*** — Mark Forsyth, Icon Books, 2012. **VERIFIED** via Icon Books catalog.
- Perell "How I Write" episode title and channel — **VERIFIED** via WebSearch, 2026-07-18 (YouTube listing "You're Using the English Language Wrong — Mark Forsyth," youtube.com/watch?v=ulhrXgpjveA).
- Exact upload date of the Perell episode (2024-07-24) — **LIKELY**, sourced from a WebSearch summary result, not opened and confirmed directly against the YouTube page's metadata this session.

## Repo file sizes checked this session (`wc -c`, 2026-07-18)

- `skills/mark-forsyth-rhetoric/SKILL.md` — 4,913 bytes
- `skills/mark-forsyth-rhetoric/genius.md` (pre-repair) — 13,091 bytes
- `skills/mark-forsyth-rhetoric/workflows/01-forge-memorable-line.md` — 3,931 bytes
- `skills/mark-forsyth-rhetoric/workflows/02-establish-voice.md` — 4,071 bytes
- `skills/mark-forsyth-rhetoric/workflows/03-train-writing-scales.md` — 5,051 bytes
- `agents/mark-forsyth/memory/context.md` — 1,050 bytes
- `agents/mark-forsyth/AGENT.md` — 4,710 bytes
- `extractions/` directory — 193 entries; none match `forsyth` (checked via `grep -ril forsyth`) — **no raw source material exists for this expert in `extractions/`**, confirming the "raw book/interview text deliberately absent" framing rather than a missed-file error.

## Explicit UNCONFIRMED items

- Any claim that a line in `genius.md` is a word-for-word transcript quote from the Perell interview — UNCONFIRMED (transcript not present to check against).
- The exact minute-marker or in-episode location of any Forsyth statement — UNCONFIRMED (no timestamped transcript available).
- No line in this repair or in the pre-existing skill is presented as verbatim book prose from *The Elements of Eloquence*, *The Etymologicon*, or *The Horologicon* — all book-attributed material here is publication metadata (title/publisher/year/ISBN), not quoted book text.
