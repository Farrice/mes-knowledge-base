# Jen Santulan — Project Context

> **Inherits from**: `/Users/farricecain/Google Antigravity/CLAUDE.md` (The Chain, Architecture, Skill tiers, Quality Gate)
> **Active since**: 2026-03 · **Reset**: 2026-09-02 (one spine, one order)
> **Operating model (source of truth)**: `_active/clients/jen-listings/06-system/ENGINE-V2.md`
> **The only front door**: `/jen` (`.agent/workflows/jen.md`) — nine steps in a fixed order with a receipt after each. Do not enter through `/jen-engine`, `/jen-full-pipeline`, `/listing-content`, `/buyer-education-story`, or `/neighborhood-deep-dive-carousel`; those skills are archived or demoted.
> **Voice source of truth**: `skills/jen-santulan-listing-content/references/jen-real-voice-profile.md` + `jen-calibration-log.md`
> **Mix**: `06-system/CONTENT-MIX.md` (extraction-derived shares + the hook rule)
> **Domain**: LA real estate, San Fernando Valley, Instagram-first (**@_jiing**; never `@realestatewithjing`, never `#realestatewithjing`)

---

## Identity (ENGINE-V2 §1)

**Jennifer Santulan** is Farrice's wife and a Valley agent. On the grid the niche is the place, not the person: **"Your Valley agent. $800K and up, buying or selling."** The content is for buyers in the $800K–$2M band, including first-time buyers with the money to do it; sellers read the same post as theirs. Never "your first home" or "first-time buyer" on a frame; the price band does the sorting. "Buying or selling" is a detail inside the ask, never a pillar.

## The deal (ENGINE-V2 §2)

She does a thumbs-up on the week's posts and same-evening DM replies from the saved replies. We do everything else. **Never** a recurring ask, a template she fills, a talking-head reel, an intake questionnaire, a word she hasn't approved, or a topic that fails the realism gate. Never name the machine to her (no "carousel," "flywheel," "local signal," "stamp"; say post, caption, reel).

## Voice (the July scrape + the September memos win over anything older)

Calm-warm, lowercase, sincere, gently funny. Ellipses over em-dashes; soft landings, not punchlines; one emoji max at the emotional landing (🏡 🤝 ✨); periods over exclamation points. Invitation asks, never pressure. The gentle misconception-correct is her signature persuasion move. Luxury listings ($2M+) play a register UP: "Quiet Flex Elite Advisor," Title Case, authority at 10, hype at 4–5, thesis first, property as evidence.

**Voice test:** would she say this to a client, in these words? Her lexicon IN/OUT, on-camera notes, and verbatim lines live in `jen-real-voice-profile.md`. Her cringe list: "top producer," "in business for 30 years," any credential.

**The bank, never a stamp (2026-09-02).** Her verbatim lines ("i'm here for you. that's my job. i do this to protect you and your best interest." · "everything works out exactly the way it's supposed to." · "just breathe…" · "lipstick remodel") are drawn at most once per week each. `execution/jen_stamp_lint.py` fails a week where a sentence repeats across posts.

## What to load (all of it, in this order, before writing a word)

`/jen` step 0 reads: `ENGINE-V2.md` · `CONTENT-MIX.md` · `VAULT.md` · `jen-real-voice-profile.md` · `jen-calibration-log.md` · this file · `06-system/pulse/latest.md`. Facts ledger: `04-deliverables/2026-09-06-engine-v2-weeks-1-2/FACTS.md` (extend it). Funnel and read loop: `06-system/FUNNEL-MATH.md`, `execution/jen_pulse.py`, `/alyssa-stalker-outlier-audit`.

Amplify step, Phase 1: ONE pen (Alyssa hook-reframe + Luke Iha hooks, nothing else) and ONE check (Jen-as-herself from the voice profile, the memos, and her ChatGPT extractions). No expert room. Phases and the audit of what survives: `06-system/PHASES.md`.

One-off listing send package (Convert district only): `skills/jen-santulan-listing-content/workflows/listing-package.md`.

## Override List (where this project diverges from root CLAUDE.md)

- **Register ladder (Jen's own verdict, 5200 Armida 2026-08-05).** Everyday/education → calm-warm lowercase. Luxury ($2M+) → Quiet Flex Elite Advisor. Never blend. Still never: attack hooks, manufactured urgency, fair-housing steering language.
- **Emojis are voice, not slop,** but her actual rate is one per post, not "emoji-rich." Root minimize-emoji guidance does not apply; neither does stacking them.
- **Factual grounding is NOT skipped.** Every number on a frame or in a caption sits in `FACTS.md` with a date, a source, and a label (VERIFIED / LIKELY / UNCONFIRMED / HERS / Jen-seat). UNCONFIRMED never reaches copy. (The old "skip Step 5.5" override is retired: the September posts carry comps, rates, and insurance dates.)
- **Plain words with punch.** Jargon gets a six-word gloss in place (buydown, FAIR Plan, ADU). Plain is the floor, never the register: the hook names the fear or the wish, the middle holds attention, the close is hers.
- **California / SFV-specific.** Generic real estate advice that ignores Prop 13, supply constraints, $800K+ starter homes, HOA and disclosure timing (they arrive in escrow) is wrong by default.
- **Fair-housing floor is hard:** `python3 execution/fair_housing_lint.py check <file>` before every render. No safe/family/schools/great-for-kids, no protected-class language, no demographic steering.
- **Other agents' listings:** neighborhood, price, specs only; never the address on a frame or in a caption. The address goes out in her DM, one to one.
- **Photos:** hers (listing shoots, portraits), the cleared Valley pool, labeled AI plates behind the cost gate. Nothing stock-looking, nothing orange or terracotta (she hates orange). Type never on a face.

## Anti-Patterns

- ❌ The property as the hook (every bottom-quartile post on her grid opens on the house)
- ❌ A verbatim voice line on every post (the 9-of-9 scar)
- ❌ Agency copywriter jargon, forced authority ("as a top 1% agent"), urgency ("THIS WON'T LAST")
- ❌ Ignoring the reader's private fear (am I being financially irresponsible; am I ready)
- ❌ Generic amenities prose; show one specific moment or detail
- ❌ Delivering as a markdown wall; the deliverable is the Valley OS page (`execution/jen_os_page.py`)
- ❌ A second generator, a second facts ledger, a second voice file, a parallel Jen lane

## Records, not truth

`_active/clients/jen-santulan/` (May–July repositioning brief, YouTube engine) and `_active/clients/jen-team-pilot/` (brand card, POC carousels) are records of earlier passes. Read them for history; never build on them. Dated files in `06-system/` are session receipts.
