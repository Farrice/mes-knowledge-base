---
date: 2026-07-25
session: jen-listings
tier: operator-guide
status: enriched
---

# Jen Listings — 1654 Moonseed Shoot Sheet + Voice Lock (@_jiing) — What We Built 2026-07-25 and How to Use It

> This session shipped a filmable hook set for Jen's own Simi Valley co-listing and, more durably, replaced the *guessed* version of her voice with a sourced one. The correction matters beyond Jen: our golden reference had calibrated format correctly and voice wrongly, because we wrote it instead of sourcing it from the client. Companion files: the deliverable at `_active/clients/jen-listings/1654-moonseed-simi-valley/1654-moonseed-SHOOT-SHEET.md`, the new voice source at `skills/jen-santulan-listing-content/references/jen-real-voice-profile.md`, the reusable method at `docs/solutions/2026-07-25-instagram-voice-scrape-without-downloads.md`.

## ⚡ If you only read 10 lines

1. **Jen's handle is `@_jiing`**, not @realestatewithjing — and `#realestatewithjing` appears nowhere in her content. Stop appending it.
2. **Her register is calm-warm and gently witty, NOT high-energy.** "real talk," "unicorn," "smart money," "let's go make it yours" are out (Farrice, this session).
3. `skills/jen-santulan-listing-content/references/jen-real-voice-profile.md` is now the **canonical voice source** and **wins over `genius.md`** on any register conflict.
4. Her caption register **equals** her spoken register — verified by cross-checking burned-in reel captions against posted captions. Write scripts and captions as one voice.
5. **Hooks must be separated from body scripts** in every shoot sheet (Farrice, this session): `HOOK (first 3 seconds) / Visual / Rest of script / Hashtags`.
6. **Hooks must be walkable** — she fronts the first 15–20s on camera moving through the property, then cuts to b-roll. A hook she can't say while walking or touching something doesn't fit her format.
7. The 6853-Willis shoot sheet remains the **structure** reference (objection ≤8 words, physical pattern-interrupt, marquee-as-bonus). It is no longer a **voice** reference.
8. IG scraping method that works with zero downloads and no Whisper key: Playwright → `og:description` meta for captions, canvas seek-capture for frames. `yt-dlp` is blocked; `--cookies-from-browser chrome` hangs — don't retry it.
9. Two team registers exist on her grid and must never blend: **Jen personal** (@_jiing, lowercase, sincere) vs **My House Sellers** (Title Case, "✨ JUST LISTED ✨").
10. First thing to run next session: the SKILL.md/genius.md propagation prompt in the command table below — the skill's own entry points still teach the retired voice.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `/listing-content [address]` | 6-hook shoot sheet for a property | New Jen listing — **load the voice profile first**, the workflow doesn't yet |
| `/voice-calibrate` | Jen-voice polish on foreign copy | Another expert's output needs her register |
| `/resume jen-listings` | This session's handoff, pinned | Picking the thread back up |
| `/watch <url>` | Frames + transcript | Video sources generally — but see "honest edges," IG needs the manual path |
| `python3 execution/prose_classifier.py check <file>` | Slop-pattern report | Before delivery — but compare against the golden ref before acting (see below) |

## The mental model

**Format and voice are separate calibrations with separate sources.** A golden reference we authored can lock format perfectly and still teach the wrong voice, because format is a structural choice we're qualified to make and voice is an empirical fact about a person we're not. The 6853-Willis sheet was 4/10 → calibrated on format in July; its slang was our invention, and it silently became "how Jen talks" in memory for three weeks. **Source voice from the client's own published words, always.**

**A deterministic gate flagging calibrated client work is a hypothesis, not a verdict.** `prose_classifier.py` flagged the v1 sheet hard. Running it against the Farrice-approved golden reference showed *identical* pattern hits (23 em-dashes vs. our 18, same structural-emoji flags) — the gate was measuring the shoot-sheet format, not quality. Test the gate against a known-good exemplar before rewriting to satisfy it.

**Blocked pipelines usually have a side door.** yt-dlp blocked + no Whisper key looked terminal. But captions live in page metadata, video pixels are readable in-page via canvas, and short-form creators burn their own transcript into every frame for silent autoplay. Three independent sources, none requiring the blocked capability.

## The voice profile (`references/jen-real-voice-profile.md`)

**What it is** — a sourced register document: her bio, 20 verbatim captions, and delivery notes from 3 reels watched frame-by-frame (39 frames). It carries an IN/OUT lexicon, her five signature moves, the two-register split, and her on-camera listing formula.

**When to reach for it** — any Jen deliverable, before the workflow runs. Any client where our voice reference was authored rather than sourced.

**When NOT to** — it doesn't govern structure; the shoot-sheet shape still comes from the 6853-Willis reference and `prompts-v2/listing-hook-set.md`. For a non-Jen realtor, don't reuse it — run the scrape method instead.

**How to invoke** — `Read skills/jen-santulan-listing-content/references/jen-real-voice-profile.md` alongside `genius.md`. On conflict, the profile wins (stated in the file's header).

**Worked example** — her signature misconception-correct, verbatim: *"i've had buyers wait years because they thought they needed perfect credit, 20% down, or that rates would suddenly crash. meanwhile… people buy homes every day with less money down than they expected. the hardest part is usually not the numbers. it's figuring out what's actually true."* Hook 2 of the Moonseed set is that move applied to a $700K listing.

**Honest edges** — no audio transcription was possible (no Whisper key), so "spoken == caption" is an inference from burned-in caption text matching posted captions on one reel, not a waveform-verified fact. Strong evidence, not proof. A Groq key in `~/.config/watch/.env` would settle it. Her humor register is documented from meme reels only; we have no sample of her being funny *in a listing reel*, so the checklist hook's wryness is calibrated-but-unproven.

## The Moonseed shoot sheet

**What it is** — 6 hooks with the hook isolated from the body, a lead IG caption in her lowercase style, 3 My-House-Sellers team variations, and a pre-filming verification footer.

**When NOT to reuse the numbers** — the engagement stats (3 days / 807 views / 33 saves / "faster than 93% nearby") drift daily. Hook 5 speaks them aloud; re-pull Zillow the morning of the shoot or cut the hook.

**Honest edges** — three facts still need eyes-on confirmation before filming: whether the walls are genuinely shared-free (MLS says "No Common Walls" + SFR subtype, but the wall-tap is the whole spine of Hook 1), whether the HOA truly covers sewer, and indoor laundry (the description says yes, the MLS facts field says "Laundry: None"). All three are in the sheet's footer.

## Composition table (options, not a pipeline)

| Stacks with | When it earns its cost |
|---|---|
| `/watch` + Groq key | Settling the spoken-vs-caption question with real audio; ~$0.01/reel |
| `/scrape-creator`-style build | If voice-locking a third creator this way — two manual runs is the tell, one build is ~an hour |
| `/jam` | If Jen gives a felt verdict on which hook lands; her taste, banked |

## Session snapshot

- **Completed:** v1 shoot sheet (finalized 8.3) → Farrice flagged the hype register → scraped @_jiing (bio + 20 posts) → wrote the voice profile → v2 rewrite with hooks separated → watched 3 reels frame-by-frame → added on-camera delivery notes → lead caption → text-message-ready package → solution card for the scrape method → memory `feedback-jen-reel-hook-style.md` corrected.
- **Remaining:** `SKILL.md` and `genius.md` still name @realestatewithjing and carry hype-adjacent pattern examples; the three MLS facts need confirming before Jen films.
- **Operator assets shipped this session:** `skills/jen-santulan-listing-content/references/jen-real-voice-profile.md`, `docs/solutions/2026-07-25-instagram-voice-scrape-without-downloads.md`. *(The spine's auto-stub listed 20 bc-*/riley-* workflows — those are from the previous commit, not this session.)*
