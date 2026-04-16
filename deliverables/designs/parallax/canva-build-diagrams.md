# Parallax Canva Build Diagrams

All measurements in pixels. Colors: Dark = #1C1C1E, White = #F5F0EB, Violet = #7B61FF

---

## 1. WORDMARK (1344 x 256 px)

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│                                                              │
│         P A R A L L A X                                      │
│                   ▲                                          │
│                   │                                          │
│            This L is #7B61FF (violet)                         │
│            All other letters are #F5F0EB (warm white)         │
│                                                              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
  Background: transparent (export as PNG)
  Font: Space Grotesk Bold, 140px
  Letter spacing: +20
```

---

## 2. FAVICON (512 x 512 px)

```
┌────────────────┐
│                │
│                │
│       P        │  ← #7B61FF (violet)
│                │
│                │
└────────────────┘
  Background: #1C1C1E (dark)
  Font: Space Grotesk Bold
  Center the P both horizontally and vertically
```

---

## 3. COVER PHOTO (1200 x 1200 px)

```
┌──────────────────────────────────────┐
│                                      │
│            (empty space)             │  ← ~240px of breathing room
│                                      │
│                                      │
│         P A R A L L A X              │  ← 40% from top (~480px)
│                   ▲                  │     Space Grotesk Bold, ~72px
│              violet L                │     #F5F0EB, violet L
│                                      │
│   For people who see everything      │  ← Source Serif 4 Italic, 24px
│     from more than one angle.        │     #F5F0EB at 50% opacity
│                                      │
│          ─────────────               │  ← 1px line, #7B61FF
│                                      │     ~60% width of wordmark
│                                      │     centered
│                                      │
│                                      │
│                                      │  ← Bottom half is EMPTY
│            (empty space)             │     Negative space = confidence
│                                      │
│                                      │
│                                      │
└──────────────────────────────────────┘
  Background: #1C1C1E (solid dark)
```

**Canva steps:**
1. Create custom size 1200x1200
2. Set background color to #1C1C1E
3. Add text "PARALLAX" → Space Grotesk Bold, 72px, #F5F0EB
4. Position: center horizontally, about 40% down from top
5. Select just the second L → change color to #7B61FF
6. Add second text block for tagline → Source Serif 4 Italic, 24px
7. Set tagline color to #F5F0EB, then reduce transparency to 50%
8. Position tagline centered, just below the wordmark (~30px gap)
9. Add a line element → 1px height, #7B61FF, ~430px wide
10. Center the line, position ~30px below tagline
11. Leave entire bottom half empty

---

## 4. EMAIL BANNER (1100 x 300 px)

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│                                                              │
│  ↑48px                                                       │
│  ←──→  P A R A L L A X                                       │
│  48px        ▲                                               │
│         violet L                                             │
│                                          (empty right side)  │
│                                                              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
  Background: #1C1C1E
  Wordmark: Space Grotesk Bold, ~32px cap height
  Position: left-aligned, 48px from left edge, vertically centered
  Right side: NOTHING. Let it breathe.
```

**Canva steps:**
1. Create custom size 1100x300
2. Background: #1C1C1E
3. Add "PARALLAX" text → Space Grotesk Bold, ~40px
4. Color: #F5F0EB, second L → #7B61FF
5. Position: left side, 48px from left edge, vertically centered
6. Done. No other elements.

---

## 5. SOCIAL PREVIEW (1200 x 630 px)

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│                     (breathing room)                         │
│                                                              │
│                  P A R A L L A X                              │  ← 40% from top
│                            ▲                                 │     ~72px, centered
│                       violet L                               │
│                                                              │
│            For people who see everything                      │  ← Source Serif 4 Italic
│              from more than one angle.                        │     20px, #F5F0EB @ 60%
│                                                              │
│                     ────────                                 │  ← 1px violet line
│                                                              │     200px wide, centered
│                                                              │
│                     (empty space)                            │
│                                                              │
└──────────────────────────────────────────────────────────────┘
  Background: #1C1C1E
```

**Canva steps:**
1. Create custom size 1200x630
2. Background: #1C1C1E
3. Add "PARALLAX" → Space Grotesk Bold, 72px, #F5F0EB, violet L
4. Center horizontally, position ~250px from top (40%)
5. Add tagline → Source Serif 4 Italic, 20px, #F5F0EB at 60% opacity
6. Center below wordmark, ~24px gap
7. Add line → 1px, #7B61FF, 200px wide, centered, ~20px below tagline
8. Leave bottom third empty

---

## 6. PROFILE BANNER (1200 x 400 px) — The Most Complex One

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  psychology                                                  │
│  AI systems                                    PARALLAX      │
│  fatherhood                                       ▲          │
│  anime                                       violet L        │
│  spirituality                                                │
│  strategy                                                    │
│     ▲                                                        │
│     │                                                        │
│  JetBrains Mono, 14px                                        │
│  #7B61FF at 40% opacity                                      │
│  (barely visible, like a watermark)                          │
└──────────────────────────────────────────────────────────────┘
  Background: #1C1C1E

  LEFT SIDE (word list):              RIGHT SIDE (wordmark):
  ┌─────────────────┐                 ┌─────────────────────┐
  │ 60px from left   │                 │ 60px from right      │
  │ 80px from top    │                 │ vertically centered  │
  │                  │                 │                      │
  │ psychology       │                 │ PARALLAX             │
  │ AI systems       │                 │ Space Grotesk Bold   │
  │ fatherhood       │                 │ ~28px                │
  │ anime            │                 │ #F5F0EB + violet L   │
  │ spirituality     │                 │                      │
  │ strategy         │                 └─────────────────────┘
  │                  │
  │ Line height: ~24px│
  │ VERY faint (40%) │
  └─────────────────┘
```

**Canva steps:**
1. Create custom size 1200x400
2. Background: #1C1C1E
3. **Right side first**: Add "PARALLAX" → Space Grotesk Bold, 28px, #F5F0EB with violet L
4. Position: right-aligned, about 60px from right edge, vertically centered
5. **Left side**: Add a text block with these words on separate lines:
   ```
   psychology
   AI systems
   fatherhood
   anime
   spirituality
   strategy
   ```
6. Font: JetBrains Mono, 14px
7. Color: #7B61FF
8. **Key step**: Reduce the transparency/opacity of this text to 40%
   (In Canva: select the text → click the transparency icon in top toolbar → set to 40)
9. Position: left-aligned, 60px from left edge, ~80px from top
10. The word list should look like a faint watermark — visible if you look, but not screaming

**Why this layout works:**
The faint words on the left = who Farrice IS (his many interests)
The crisp wordmark on the right = the publication that holds all of it
The contrast in opacity between the two sides = literal parallax (two planes at different depths)

---

## Quick Reference: Hex Colors

Copy-paste these into Canva's color picker:

| What | Hex Code | Where to Use |
|------|----------|-------------|
| Dark background | `1C1C1E` | Every background |
| Warm white text | `F5F0EB` | All text except the violet L |
| Violet accent | `7B61FF` | The second L + lines + word list |

---

## Font Checklist

Before building, make sure these fonts are available in Canva:
- **Space Grotesk** → Search "Space Grotesk" in Canva fonts (it's free/available)
- **Source Serif 4** → Search "Source Serif" (might appear as "Source Serif Pro")
- **JetBrains Mono** → Search "JetBrains Mono" (if not available, use "IBM Plex Mono" or "Fira Code" as alternatives)

---

## Export Settings

For ALL assets:
- File type: **PNG**
- Quality: **Maximum / highest**
- Transparent background: **YES** for the wordmark only. All others use the #1C1C1E background.
- Download each with a clear filename: `parallax-logo.png`, `parallax-cover.png`, etc.
