---
name: "Jennifer Santulan — Listing Send Package (One Forwardable Text)"
source_prompt: born-v2
skill: jen-santulan-listing-content
standard: structure-pure-v2
forged: born-v2
refactored: 2026-08-05
---

## Role & Activation

You are compressing a completed listing content run (approved hooks + scripts, verified facts, register decision) into **the single text message Farrice forwards to Jen** — the artifact she shoots from on her phone. Provenance: 2026-08-05, 5200 Armida — the robust shoot sheet was the better *thinking*, the forwardable text was the better *deliverable*; Farrice rebuilt it externally and sent his version. This prompt makes the system produce that shape natively. The governing law: **robustness in the sheet, simplicity in the send.** The repo shoot-sheet (research, ledger, diagnostics) is the substrate; NONE of its machinery may leak into the send text — no repo paths, no tool names, no workflow jargon (`execution/client_package_lint.py` is the floor).

## Input Required

```
[HOOKS + SCRIPTS] — from the same run (or Farrice-approved iterations), required
[LISTING.JSON + CLAIMS-LEDGER.JSON] — fact source of record, required
[REGISTER] — fthb | luxury (from the run's Step 0), required
[CAPTION DIRECTION] — Farrice's iteration notes, if any (post-delivery feedback)
```

## Execution Protocol

### Step 1 — Numbers block
Three lines max, top of text: price · bed/bath · sqft · lot; main-vs-ADU split if any; 3-5 headline features; open-house dates. Every number from the ledger as VERIFIED.

### Step 2 — Options assembly (pick-one architecture)
5-6 reels as OPTIONS, exactly ONE marked "my top pick" (chosen by: strongest photo support + lowest verification load + register fit). Each option = **COVER TEXT → HOOK → SHOT → THEN SAY** (four blocks, filmable as discrete takes). Include the buyer line ("For: …") — internal targeting stays fair-housing-safe and NEVER appears in caption/spoken text. Add the "if you only film 3" line naming which (open-house carrier always included).

### Step 3 — Cover text pairs
Every option's on-screen text paired `→` to the specific photo/shot that proves it. Two lines, real numbers. FTHB lowercase / luxury Title Case.

### Step 4 — Caption (one, works under all options)
Register-matched:
- Opening line = universal multi-fact curiosity stack (each fact a different buyer's door) OR the top pick's thesis line — must survive the ~125-char fold.
- Narrative walk (curb → inside → out back), facts riding inside scenes.
- Compact fine-print block ("the fine print, so you don't have to hunt ↓") — buyer never leaves the post for a fact: price, beds/baths, sqft split, lot, story count, garage, systems, year/remodel, schools as data (ratings + distance only), MLS#.
- CTA: keyword DM ("comment TOUR / DM me '<KEYWORD>'") + open-house times.
- Attribution: agents | brokerage, DRE # line.
- Hashtags: her set + adjacent-city reach tags (Calabasas/Tarzana/Encino).

### Step 5 — Filming notes + don't-say list
Filming notes: operational only, ≤6 bullets (length, hook lands ≤2s no walk-up, opening shot, close filmed separately at hero spot golden hour, IG-native captions, post same day). Don't-say list = the ledger distilled: fair-housing set ALWAYS (safe/family/great-for-kids → say guest house/extended living/office; schools off camera; no prior-sale-price talk; no Zestimate) + this listing's specific landmines (contradiction items from claims-diff, each with its fallback line).

### Step 6 — Lint pass
Run `client_package_lint.py` + `fair_housing_lint.py check --context package` on the rendered text. Fix, never ship on FAIL.

## Output Contract

1. The send text — one continuous copy-paste block, phone-formatted (short lines, visual separators, minimal markdown that survives SMS/iMessage), starting "hey babe, here's everything for <address>" and containing: numbers block · options (one top pick) · cover-text pairs · caption · filming notes · don't-say list.
2. A 3-line footer FOR FARRICE ONLY (not part of the send): where the sheet lives, which claims are UNCONFIRMED pending Marty, natural split points if the text is too long for one message.

Hard constraints: zero repo paths/tool names in the send text; every number ledger-VERIFIED or absent; don't-say list present in every package; exactly one top pick.

## Output Skeleton

```
[ADDRESS] — REEL SCRIPTS 🎬
$X · open [days/times]

If you only get 3 filmed: [n, n, n].

━━━━━━━━━━━━━━━
OPTION 1 — [NAME] ← my top pick
For: [buyer]

COVER TEXT: `line1` / `line2`
🎣 HOOK (first 3 seconds): "..."
SHOT: ...
THEN SAY: "..."
━━━━━━━━━━━━━━━
[Options 2–6 same shape]
━━━━━━━━━━━━━━━
📝 THE CAPTION (works under any option)
[caption]
━━━━━━━━━━━━━━━
FILMING NOTES
• ...
DON'T SAY ON CAMERA
• ...
```

## Quality Gate

- [ ] One forwardable block; survives paste into iMessage without formatting collapse
- [ ] Exactly one "my top pick"; "if you only film 3" line present; open-house carrier included
- [ ] Every cover-text pair maps to a real photo/shot; every number traces to the ledger
- [ ] Caption: fold-surviving opener · facts inside scenes · complete fine-print block · keyword CTA · DRE line · adjacent-city hashtags
- [ ] Don't-say list = fair-housing set + this listing's contradiction items with fallback lines
- [ ] `client_package_lint.py` and `fair_housing_lint.py` both clean on the rendered text

## Creative Latitude

The skeleton fixes blocks, never sentences. The top-pick call is a real judgment — make it and say why in the Farrice footer. Caption storytelling should carry the register's personality (warm walk vs private market brief); the fine-print block is the only part allowed to read like data. If Farrice's feedback notes named a direction, that direction outranks the defaults.

## Deploy When

The generation phase of `/listing-package` has produced hooks + scripts (same run — no stop between); or Farrice asks to "make this textable to Jen" for any existing hook/script set.
