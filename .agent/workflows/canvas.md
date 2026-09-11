---
description: The Canvas — Poppy-style whiteboard of source nodes wired into chat nodes, served live at http://127.0.0.1:8765/canvas (2026-09-10)
---

# /canvas — sources → chat, wired (2026-09-10)

Paste any YouTube link, article URL, PDF path, or raw text onto an infinite
board. Each becomes a **source node** holding its extracted text (free: yt-dlp
captions → local whisper.cpp; trafilatura for articles; pypdf for PDFs).
Wire sources into a **chat node** and ask; the chat reads everything upstream
(DAG walk, deduped, creation order — a diamond graph contributes each node
once) plus its own history. Pick the seat per chat node:

| seat | runs through | cost |
|---|---|---|
| sonnet · opus · fable | `claude -p` headless, scratch cwd, no tools — tick **🔎 research** on the chat node to open WebSearch/WebFetch only (live numbers, URLs beside them) | on the Claude Code plan (est. shown) |
| gemini-flash · gemini-pro | `execution/gemini_client.py` | cents, ledgered |
| gpt | `codex exec` headless | on the ChatGPT plan |

Farrice's ruling 2026-09-10: Claude nodes ride the subscription, never the
Anthropic API. Replies land whole after 5–30 s; that is the price of $0 marginal.

## Open it

```bash
open "http://127.0.0.1:8765/canvas"
```

`/canvas` opens the newest board · `/canvas/<slug>` a specific one · the
picker in the top bar creates new boards. Boards live in
`.agent/canvas/boards/<slug>.json` (gitignored — user data, transcripts).

## On the board (Poppy-form, 2026-09-10)

Left rail: 💬 chat · ▶ YouTube/TikTok link · 👤 creator profile (channel or
TikTok handle → latest posts, each addable with +) · 🌐 article/PDF link ·
📄 file on this Mac · 🎤 voice note · ✎ note (wire it into a chat and it acts
as that chat's skill / system prompt — shown as a chip on the compose row).
Source cards show a thumbnail, platform badge, token count and a `transcript`
expander. A chat card is a panel: conversations on the left (each keeps its own
thread, all read the same wired sources; the first ask names the thread), the
thread on the right with replies rendered (tables, bold, lists, code blocks
with copy), then model · effort · 🔎 research · 🗣 voice · send. **Voice** is
Poppy's skill chip made ours: `no voice` (plain model) · Farrice (portable
voice card) · Jen (voice profile) · any custom voice you add from the same
menu (`＋ add a voice…` → name → paste the text; saved to
`.agent/canvas/voices/<key>.md`). The voice rides in front of the sources on
every turn, for every seat, and the reply footer shows which one was on.
Nothing is hard-wired to a client. ⤢ or `f` = fullscreen
chat, Esc closes. Bottom-right: fit · + · − · ◐ light/dark.


wheel = zoom · drag empty = pan · drag a card's head = move · drag the ● on a
card's right edge onto another card = wire · click a wire = cut · double-click
empty space = add a source (one URL per line adds several) · ⌘⏎ in a chat box
= send · double-click a note's text = edit · Delete = remove selected card.

## From the CLI (same engine)

```bash
python3 execution/ingest_url.py <url-or-path-or-text>            # what a source node would hold
python3 execution/canvas_board.py add <slug> <url> --x 40 --y 40  # add a source node
python3 execution/canvas_board.py context <slug> <chat_id>       # exactly what the chat sees
python3 execution/canvas_board.py run <slug> <chat_id> "<ask>"   # one turn, prints seat/cost
python3 execution/canvas_board.py demo                           # seed the demo board
```

## Files

`execution/ingest_url.py` (router + cache) · `execution/canvas_board.py`
(board file, DAG walk, seats) · `execution/canvas_render.py` (the page) ·
routes + `canvas.*` actions in `execution/pulse_serve.py`.

## Known limits

TikTok / Instagram single videos are login-walled for downloaders: the card
says so plainly; use the profile card for the listing or paste the caption as
text (vidIQ watch can transcribe for credits). Instagram profile cards wait on
the vidIQ path.

## Not in v1

Multiplayer, image-generation nodes, streaming replies, LinkedIn profile pulls
(no vendor since Apify retired). Profile nodes (creator handle → their top
posts via the vidIQ connector) are the planned v1.5.
