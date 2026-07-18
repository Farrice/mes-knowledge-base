# Provenance — michael-margolis-user-research repair

Anchor → source file + location. All anchors point into conversation files extracted from
`_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, confirmed via `wc -c`) —
the archive was opened directly with Python `tarfile`, member-scanned by UUID (no
filename search possible; conversations are named by UUID not title), and the 3 relevant
members extracted to a scratchpad for reading. Both primary conversations are raw YouTube
transcripts of *Lenny's Podcast* — "Identify your bullseye customer in one day | Michael
Margolis (UX Research Partner at GV)" (`youtube.com/watch?v=B6Dt1sgGmLI`) — pasted by the
user, not Claude-generated commentary.

| Anchor (genius.md, Anti-Patterns section) | Source file (extracted) | Location |
|---|---|---|
| "we did not select specifically... weren't picky enough about Bullseye customers... it just feels mushy" | `81526288-a470-4353-b247-20ebab6da854.md` (126,943 bytes) | Lines 2269–2286, timestamp 79:42–80:19 |
| "we have people manually taking notes and not using AI to take notes... lean out a little bit or maybe you checked your slack" | `81526288-a470-4353-b247-20ebab6da854.md` | Lines 1985–1999, timestamp 69:50–70:22 |
| "I will pay $125 to anybody who... listens to Lenny's podcast... a bazillion people who [say] I will take that $125" | `81526288-a470-4353-b247-20ebab6da854.md` | Lines 1257–1284, timestamp 43:52–44:56 |
| "you get overcommitted to one idea you're polishing... pushes teams to think of new different possibilities" | `81526288-a470-4353-b247-20ebab6da854.md` | Lines 543–551, timestamp 17:59–18:31 |
| "it should feel comically narrow" / "oh for God's sakes Margolis... this is too much" | `81526288-a470-4353-b247-20ebab6da854.md` | Lines 774–784, timestamp 26:09–27:10 |
| "put more weight on past experiences than on people's predictions of what they would do" | `81526288-a470-4353-b247-20ebab6da854.md` | Lines 2344–2354, timestamp 82:27–82:49 |

Cross-confirmation: `8f994738-1c58-451a-8435-6f475c739237.md` (142,497 bytes, captured
2025-09-05 — five weeks earlier, independent paste of the same transcript) contains the
identical passages at the equivalent offsets (`diff` on body content shows only
front-matter/prompt-preamble deltas, not transcript deltas). This corroborates the
transcript text rather than resting on a single capture.

Not used as a quote source: `779c66a8-5c0b-4fa4-9c57-f84fe91841f0.md` (20,156 bytes) —
Claude-generated "Crown Jewel" prompt-extension conversation, explicitly a derivative
work built to replace Margolis's interview method with AI research. See
`references/source-ledger.md` for the full claim-by-claim table, including the one
pre-existing unresolved claim in the untouched "Genius Patterns" section (Gong/Linear)
flagged UNCONFIRMED rather than silently re-certified.
