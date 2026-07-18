# Source Ledger — fareed-zakaria-writing-mastery

Claim-by-claim provenance. Labels: **VERIFIED** (confirmed against a primary or reputable secondary source this session), **LIKELY** (well-attested public fact, not re-verified line-by-line), **UNCONFIRMED** (no source found in this repo or on the open web — treated as synthesized/illustrative, not extracted).

## 0. Repo-wide search for a primary extraction source

Before labeling anything, this repair searched for a real Zakaria extraction transcript (interview, book excerpt, podcast) anywhere in the repo, per the envelope's rule that an "absence" claim must be verified, not assumed:

- `extractions/` — content grep for "zakaria" across all files: **zero matches**.
- `_active/codex-harvest-2026-06-11/` — matches found (`agents/fareed-zakaria/AGENT.md`, `skills/fareed-zakaria-writing-mastery/SKILL.md`) are prior mirrors of the *same* SKILL.md/AGENT.md content already in `skills/`, not a distinct raw source. No transcript file present.
- `_archive/claude-export-2026-07-01.tar.gz` — `tar -tzf` file-name index searched for "zakaria": **zero matches**.
- `swarm_outputs/20260306_130322/agent_outputs/fareed-zakaria.md` — exists but is an unrelated LinkedIn-ghostwriting-demand research memo (Gemini 2.5 Flash output), not a Zakaria craft extraction.
- `evolution_store/v2_variants/genius_compressed/fareed-zakaria-writing-mastery_genius.md` — a compressed variant of this same genius.md, same unsourced content, not an independent source.

**Conclusion: VERIFIED absence.** No primary extraction transcript for Fareed Zakaria exists anywhere in this repository. This skill was built without a grounding source document.

## 1. Craft content (Hall of Fame Exemplars, Signature Moves, Genius Patterns placeholder)

| Claim | Label | Basis |
|---|---|---|
| "Exemplar 1" and "Exemplar 2" quoted passages in Hall of Fame Exemplars | **UNCONFIRMED** | No verbatim match found in any repo source or via web search of the exact quoted text. Reads as style-matched pastiche, not an extracted quote. Retained as illustrative model only — see provenance note added inline in genius.md. |
| "The Stakes Mirror," "The Global Interconnect Weave," "The Proof Before Claim Protocol," "The Nuance Navigator," "The Clarity-First Edit" as named techniques | **UNCONFIRMED** | These are this skill's own descriptive labels for a general pattern observed in his public commentary; no source ties the literal names to Zakaria's own words. |
| "One idea per piece, argued thoroughly" (core principle, SKILL.md) | **LIKELY** | Consistent with widely observed structure of his Washington Post columns and CNN segments; not tied to a specific dated quote. |

## 2. Biographical / bibliographic facts (used to ground the Genius Patterns section)

| Claim | Label | Basis |
|---|---|---|
| Hosts CNN's *Fareed Zakaria GPS*, weekly, since 2008 | **VERIFIED** | WebSearch 2026-07-17; corroborated by Wikipedia ("Fareed Zakaria") and cnn.com/specials/fareed-zakaria-gps-2021-archive. |
| Writes a syndicated Washington Post column | **VERIFIED** | WebSearch 2026-07-17; washingtonpost.com/people/fareed-zakaria/. |
| Author of "Ten Lessons for a Post-Pandemic World" (2020) | **VERIFIED** | WebFetch/WebSearch 2026-07-17; Simon & Schuster publisher page, NPR interview (2020-10-13), Washington Post essay (2020-10-06). |
| Author of "Age of Revolutions" (2024) | **VERIFIED** | WebSearch 2026-07-17; publisher listing, corroborated by author bio pages. |
| "Author of five New York Times–bestselling books" | **LIKELY** | Stated on author bio aggregation found via WebSearch 2026-07-17; not individually cross-checked against NYT bestseller archive for this repair. |

## 3. Anti-Patterns section (attribution & evidence-compression failures)

All five items below were verified this session via WebSearch + WebFetch (2026-07-17) against named, reputable secondary sources. These are real, dated, widely reported events in Zakaria's professional record, used here strictly as craft case studies for the "evidence compression" / "proof before claim" discipline this skill teaches — not as editorializing about the person.

| Claim | Label | Source |
|---|---|---|
| 2012-08-20 *Time* gun-control column contained uncredited material from Jill Lepore's "Battleground America" (*The New Yorker*, 2012-04-23); also posted to his CNN blog | **VERIFIED** | Harvard Magazine, "Fareed Zakaria, international affairs commentator, penalized for plagiarism" (2012-08) — https://www.harvardmagazine.com/2012/08/zakaria-penalized-for-plagiarism |
| Suspended by Time/CNN 2012-08-10, suspension lifted 2012-08-16; apology quote: "I made a terrible mistake. It is a serious lapse and one that is entirely my fault." | **VERIFIED** | Same Harvard Magazine article as above. |
| Time called the incident "an unintentional error and an isolated incident"; CNN said its review "found nothing that merited continuing the suspension" | **VERIFIED** | Same Harvard Magazine article as above. |
| August 2014: bloggers "CrushingBort" and "BlippoBlappo" (Our Bad Media) published 12 further examples of uncredited compression — 7 Newsweek columns, 1 Slate column, 4 Washington Post pieces — each later carrying editor's notes | **VERIFIED** | The Week, "Three major publications have acknowledged plagiarism by Fareed Zakaria. Does CNN have no shame?" — https://theweek.com/articles/442125/three-major-publications-have-acknowledged-plagiarism-by-fareed-zakaria-does-cnn-have-no-shame |
| Contemporaneous critique (2012-08-13) framed the deeper anti-pattern as presenting compressed synthesis of others' primary research as freestanding original analysis | **VERIFIED** | Reason, "The Real Problem With Fareed Zakaria Isn't His Plagiarism" (2012-08-13) — https://reason.com/2012/08/13/the-real-problem-with-fareed-zakaria-isn/ |

## 4. Out of scope for this repair

Workflow files (`workflows/*.md`), `references/prompts/`, `references/prompts-v2/`, `references/_legacy-prompts/`, and `SKILL.md`'s execution-prompt list were not re-verified — `workflow_contracts` already passed the heartbeat audit and the envelope scopes this repair to the four failing checks only. Their provenance status is unchanged from before this repair (i.e., also ungrounded in a primary transcript, per §0 above).
