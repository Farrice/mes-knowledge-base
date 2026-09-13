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
