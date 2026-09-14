---
thread: inbetweener-pitch-bible
status: mid-build
resume_hint: python3 execution/job_board.py resume inbetweener-pitch-bible
unfinished: none
branch: worktree-inbetweener-pitch-bible
pin: false
---

# JOB PACKET — inbetweener-pitch-bible · for claude · generated 2026-09-12T17:12:02-07:00 on claude (branch worktree-inbetweener-pitch-bible)

## Resume
- `python3 execution/job_board.py resume inbetweener-pitch-bible` then follow `skills/nate-b-jones-manager-loop/workflows/manager-loop-run.md`
- end the turn only when `python3 execution/job_board.py next inbetweener-pitch-bible` prints MAY END

## Rules that travel
- Keep every unblocked lane moving; batch questions into DECISION PACKETS; deliver packets + receipts, not status.
- Never publish, send, spend, delete outside the repo, or ship AS Farrice without approval (the card's `Needs approval`).
- Dispatch briefs carry verbatim: "no Chain, no finalize, no Notion, no Next Moves, return only the artifact".

## Lanes now
| id | status | owner | after | expected | evidence | blocker |
|---|---|---|---|---|---|---|
| L1 | complete | claude | — | Title verdict | .agent/missions/inbetweener-pitch-bible/lanes/L1.r |  |
| L2 | complete | claude | — | Visual inventory | .tmp/inbetweener-assets/manifest.json |  |
| L3 | complete | claude | L2 | World stills | deliverables/josh-banday-pitch-bible/lookbook/fram |  |
| L4 | complete | claude | L1,L2,L3 | Deck rebuild | deliverables/josh-banday-pitch-bible/lookbook/buil |  |
| L5 | complete | claude | L4 | Fact + rights pass | .agent/missions/inbetweener-pitch-bible/lanes/L5.r |  |
| L6 | complete | claude | L5 | Gauntlet + package | deliverables/josh-banday-pitch-bible/lookbook/RECU |  |
runnable: none · waiting on deps: none · blocked on Farrice: none · done: L1, L2, L3, L4, L5, L6

## Decision packets open
## Packet 1 — L1 · open · 2026-09-12T16:55:56-07:00
Choice: Retitle the deck?
Irreversible? no
Options: (a) Recurring: clean, already the finale episode title, the show's thesis in one industry word (recommended) | (b) Trailer Six: clean, more original, needs new hero copy | (c) keep In-Betweener: not recommended, direct collision with The Inbetweeners (UK sitcom, 2 films, MTV remake; a revival is LIKELY but unconfirmed)
Recommend: a
If no answer: deck rebuilds titled Recurring with In-Betweener kept as a one-line formerly note for Josh; one build flag reverses it

## Decisions answered
none

## Trace (last 12 of 18)
- 2026-09-12T16:55:56-07:00 · L1 · asked · packet #1: Retitle the deck? · [claude]
- 2026-09-12T17:00:36-07:00 · L2 · complete · planned → complete · did: 10 cast comps (2 per role, all Wikimedia Commons CC-licensed, attribution captured), 3 real Sunset Gower photos (PD/CC0/FAL), manifest.json written. Josh headshot: only a 300px Prime Video still exists on licensed/press tiers; used as labeled placeholder, deeper press-photo search seated as follow-up. Generic lot photos not found licensed, so world frames are generated (L3). · evidence: .tmp/inbetweener-assets/manifest.json · result: .agent/missions/inbetweener-pitch-bible/lanes/L2.result.md · [sonnet]
- 2026-09-12T17:00:36-07:00 · L2 · found · Assets saved under `/Users/farricecain/Google Antigravity/.claude/worktrees/inbetweener-pitch-bible/.tmp/inbetweener-assets/{cast,creator,locations}/` with `man · [sonnet]
- 2026-09-12T17:00:36-07:00 · L2 · found · Josh Banday headshot: no CC/press-licensed photo found (Wikimedia, Openverse, 3 query variants). Prime Video cast-page still (300px) used as placeholder labeled swap-me; follow-up seat searching ABC/Amazon press sites and IMDb media for a larger file. · [claude]
- 2026-09-12T17:01:04-07:00 · L3 · complete · planned → complete · did: Look card + 7-shot list written first (Dave Clark w03). 14 frames generated (2 takes x 7) on nano-banana-2 via generate_image.py, gemini-image quota lane, ~$0.09 total; 1 edit pass fixed a stage-door number (4 -> 7). Takes picked in frames/picks.json with reasons. No legible text, no faces, palette held to the deck's black/gold. · evidence: deliverables/josh-banday-pitch-bible/lookbook/frames/manifest.json · result: deliverables/josh-banday-pitch-bible/lookbook/SHOT-LIST.md · [claude]
- 2026-09-12T17:01:04-07:00 · L3 · found · Living doc. Frames generated from this list, never improvised at the prompt bar (Dave Clark w03: script → outline → shot list → prompts). · [claude]
- 2026-09-12T17:09:53-07:00 · L4 · complete · planned → complete · did: build_deck.py rebuilds the deck from source + frames + cast_map: 19 images embedded as JPEG data URIs (1.93 MB single file), hero key art, ABC press portrait in creator + lead slots, 6 location frames, 10 comp thumbnails with credits, confidentiality note, CREDITS.md. Retitled Recurring per packet if-silent default (one flag reverses). Source deck untouched. · evidence: deliverables/josh-banday-pitch-bible/lookbook/build_deck.py · result: deliverables/josh-banday-pitch-bible/lookbook/RECURRING_pitch_lookbook.html · [claude]
- 2026-09-12T17:09:53-07:00 · L4 · found · <!DOCTYPE html> · [claude]
- 2026-09-12T17:10:19-07:00 · L5 · complete · planned → complete · did: 28 claims checked: all people, credits, ages, studio, comps VERIFIED. 3 network misattributions fixed in the build layer (Hacks -> Max, Abbott Elementary removed from Hulu, The Bear cut from Hulu). Ethnicity line verified at source (Josh's own intake). RED: Netflix announced The Inbetweeners 3 in production on 2026-09-07, so the old title is unsendable. Recurring verified clear. Factual 8/10 pre-fix. · evidence: .agent/missions/inbetweener-pitch-bible/lanes/L5.result.md · result: .agent/missions/inbetweener-pitch-bible/lanes/L5.result.md · [sonnet]
- 2026-09-12T17:10:19-07:00 · L5 · found · | # | Claim | Verdict | Source | Fix | · [sonnet]
- 2026-09-12T17:12:02-07:00 · L6 · complete · planned → complete · did: Design gauntlet recurring-lookbook: round 1 VISUAL VERIFIED (desktop/tablet headless Chrome, mobile via Playwright true emulation), verdict INCOMPARABLE bar=self, closed PASS with 4 surviving risks. One in-lane repair (SCROLL indicator collision at 375). PDF exported beside the HTML (8.8 MB after killing image CSS filters in print; was 29.5). SEND-NOTE.md drafted for Farrice to forward; nothing sent. · evidence: deliverables/josh-banday-pitch-bible/lookbook/RECURRING_pitch_lookbook.pdf · result: deliverables/josh-banday-pitch-bible/lookbook/gauntlet/recurring-lookbook/GAUNTLET-RECEIPT.md · [claude]
- 2026-09-12T17:12:02-07:00 · L6 · found · - artifact: deliverables/josh-banday-pitch-bible/lookbook/RECURRING_pitch_lookbook.html · [claude]

## Card
<!-- instance of recipes/tv-pitch-lookbook.md · opened 2026-09-12T15:36:44-07:00 by claude on claude · goal: The In-Betweener pitch deck becomes a send-ready lookbook Josh would actually pitch: real faces for the cast, real places for the world, his own headshot, a title that survives Hollywood, so the asset stops sitting dead. -->
---
job: tv-pitch-lookbook
name: TV pitch lookbook (text deck → send-ready visual pitch)
family: client-content
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
A finished text pitch deck (HTML) becomes a send-ready lookbook a creator would actually pitch: faces for the cast, places for the world, the creator's own headshot, a title that survives collision checks, every real name verified, nothing sent by us.

## Sub-jobs / lanes
- L1 Title verdict — collision check on the current title plus five candidates via `.agent/workflows/name-audit.md` + `skills/david-placek-naming/SKILL.md`; collisions and trademarks checked with `execution/research.py`; lands as a DECISION PACKET with one recommendation [parallel]
- L2 Visual inventory — per character two dream-cast comps with photo source URLs and rights notes via `.claude/skills/tool-image-search/SKILL.md`; creator headshot source; real location references for the named lot; one table, sources only [parallel]
- L3 World stills — shot list first (look card per `skills/dave-clark/SKILL.md`: one light source, black point, atmosphere), then one frame per named location plus one hero key-art frame via `.agent/workflows/generate.md` with the craft-map master loaded; palette locked to the deck's existing one [after: L2]
- L4 Deck rebuild — images embedded as data URIs so the file travels alone; cast comp cards, headshot slot filled, hero key art, retitle only if the L1 packet landed; the gauntlet-passed layout preserved [after: L1, L2, L3]
- L5 Fact + rights pass — every real person, credit, network, and comp title labeled VERIFIED/LIKELY/UNCONFIRMED (fact-verifier agent); comp photo credit lines; confidentiality footer; `python3 execution/prose_classifier.py check` clean [after: L4]
- L6 Gauntlet + package — `.agent/workflows/design-gauntlet.md` against a named reference lookbook; PDF export beside the HTML; a two-line send note drafted for Farrice to forward (send stays human) [after: L5]

## Ask me first
- Q: Cast comps — real dream-cast actor photos (lookbook convention, confidential deck) or AI-rendered casting frames? · look first: the deck's existing character cards, `deliverables/josh-banday-pitch-bible/character_bibles.md`
- Q: The creator's headshot — a file he sent, or pull his public press photo as a flagged swap-me placeholder? · look first: `find . -iname "*<surname>*"`, Drive client folder
- Q: A named reference lookbook to gauntlet against, or bar=self? · look first: `directives/blind-bar-protocol.md`, prior `deliverables/gauntlet/*/GAUNTLET-RECEIPT.md`

## Handles alone
Title research, comp research, shot lists, image generation inside the approved spend, HTML rebuild, fact labeling, gauntlet rounds, PDF export, send-note draft.

## Comes back when
- The title packet (his call, then the creator's)
- Any comp photo whose rights are unclear for a confidential development deck
- Two rejected renditions of one frame → stop, back to the shot list
- A real-name claim lands UNCONFIRMED and the deck depends on it

## Needs approval
Image-generation spend (cost gate holds each paid call) · sending anything to the creator · publishing the deck anywhere public.

## Needs
The source HTML deck · the creator's bible folder · `skills/generate/references/craft-map.md` · `execution/openai_budget_guard.py` ($15/mo cap) · `.agent/workflows/design-gauntlet.md` · fact-verifier agent · `.claude/skills/tool-image-search/SKILL.md`.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| source missing | search the three locations, mark UNCONFIRMED | never invent |
| sources disagree | carry both, label LIKELY/UNCONFIRMED | the disagreement changes the deliverable |
| tool/site blocks | alternate route (Playwright, cached copy) | two routes fail |
| bar not met | one rewrite from the brief | second miss = packet, not a third take |
| generation blocked by the cost gate | surface the cost, hold for his approve | never retry silently |
| fullPage screenshot duplicates 100vh sections (scar: in-betweener gauntlet 2026-09-11) | capture real scroll positions instead | never trust the stitched PNG |
| comp photo rights unclear | swap to a different comp with a clear source | the character has no clear-source comp |

## Done means
Rebuilt HTML with every image embedded and zero broken `src` · PDF beside it · title packet answered or explicitly parked · fact pass file with labels · gauntlet receipt PASS or VISUAL UNVERIFIED stated · send note drafted, not sent.

## Ratchet log
- none yet

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
