# Artifact Design Language — Growth Blueprint OS

The visual/interaction canon for every HTML artifact this skill ships. Two sources, one hierarchy:

1. **Outward form (colors, type, spacing, brand): `_active/farrice-brand/premium-minimal/package/02-DESIGN-CONTRACT.md` GOVERNS.** Canvas/paper/ink/graphite/line/stone tokens, Helvetica Neue only, restrained-contemporary-decisive. **His dark-navy chat style is NOT our client style** — it reads as session output; ours reads as a commissioned decision object. Nothing below overrides the design contract.
2. **Interaction + semantic grammar: adopted from the Kallaway extraction** (delta #27–30, artifact ledger §6) — the patterns below are what made his artifacts teach. We keep the grammar, re-voiced in Premium Minimal.

Client renders go through `execution/render_brief.py <brief.json> --client` (Readout OS, `templates/research-brief/template-client.html`). This file is the spec the templates implement — and the hand-render spec for any artifact geometry the template doesn't yet carry (wheel, matrix, rings).

---

## 1. Shared palette SEMANTICS (adopted delta #27; values ours)

One meaning-system across ALL artifacts in an engagement — a color read in one artifact must be legible in every other. His semantic layer is right; his values (red→dark-blue heat on navy) are replaced with a restrained Premium Minimal expression:

| Semantic | Meaning (constant everywhere) | Expression (Premium Minimal) |
|---|---|---|
| **Ring altitude 1→5** | Center → broadest audience | A single-hue tonal ramp: ink-dense at Ring 1 → stone-light at Ring 5. Never five rainbow hues |
| **Open / white space** | Unclaimed lane, worth a bet | Paper field + fine dashed `line` border + a small "OPEN" label — emptiness rendered as quiet space, not neon green |
| **Contested** | Someone's there, beatable | Graphite label + the incumbent named inline |
| **Crowded / danger** | Saturated, or Ring-5 trap | Ink-solid band + uppercase functional label (+0.16em tracking). Danger reads through weight and words, not alarm colors |
| **Chosen / starred** | The recommended pick | Ink emphasis + ★; bench items at graphite, present but subordinate |
| **Test / provisional** | Amber-class meaning: unproven, watching | Graphite + "TEST" functional label |
| **Excluded** | ✗ rows, struck | Strikethrough + stone dimming, kept in rank position |

**Verification labels are typographic, always:** VERIFIED / LIKELY / UNCONFIRMED as small-caps functional labels beside the claim; `[NEED]` slots render as a hairline-boxed placeholder naming the missing number. Never color-only — labels must survive grayscale print (the PDF export is the deliverable of record).

## 2. Same geometry, different legend (adopted delta #28)

One mental model, many read-outs: the ring geometry is drawn ONCE and re-legended — audience bullseye, 3-2-1 batch plan, sourcing-rights map, top-50 placement view — instead of introducing a new diagram per idea. The reader learns the shape once and reads it four ways. Rule: any time a new view is proposed, first ask whether an existing geometry re-legended can carry it. New geometry is a cost; a new legend is nearly free.

## 3. Five-beat teaching panels (adopted delta #29)

Every interactive wedge/slice/cell detail panel walks the same five beats, in order, in plain language:

1. **What this even is** — one sentence, zero jargon, one concrete contrast.
2. **The full menu of options** — the option space before what's taken.
3. **What we're seeing in your niche** — a scoreboard, not a paragraph: one row per option, occupancy count ("N of 12 here"), the channels on the row, a one-word verdict (crowded / contested / open). **Our addition: every row cites its specimens** — the receipts live in the panel, not behind a paywall.
4. **The white space** — stated plainly.
5. **What it means for you** — the translation to THIS operator, citing the interview evidence it leans on; opportunity or trap, and which (unclaimed vs. graveyard, on the measured data).

The same five beats appear in the markdown artifact so the teaching survives outside the HTML. A reader who has never heard the word "positioning" can use the artifact; one who has can audit it.

## 4. Interaction contract (adopted delta #30, tap-a micro-instructions)

- **"Tap a wedge / Tap a cell / Tap a ring"** — every interactive artifact carries its micro-instruction inline, once, where the hand hovers. Functional-label styling.
- **A click that does nothing is a bug.** Every bubble/cell/row click opens something useful; missing data says "not enough data" rather than staying silent.
- **Element cards answer "what exactly is this?"** — a clicked channel bubble opens: which option it executes on this dimension, one specimen (link + views + outlier + date), a one-line plain-English read, and the compact all-dimensions fingerprint strip.
- **Dim-the-rest on focus:** hovering/selecting an element quiets everything outside its context.
- **Plain-English glossing:** every term of art (outlier, hook, bucket, avatar) defined inline in parentheses at first use. The artifact needs no external glossary. Four-part naming everywhere a format or structure appears: plain name · one-liner · 12-second example · linked specimen.

## 5. Trap callouts inside the chart (adopted P9/SM3)

Every ranked visual carries an adjacent callout naming the wrong conclusion it invites, in the reader's line of sight — not a footnote: "one channel winning, not a topic" beside the inflated bucket; the scale-distortion caveat inside the legend itself; "don't judge at 24 hours" on the tracker. Blind-spot sections close every dashboard: what the data cannot see (platform coverage, conversion invisibility) and the wrong conclusion each gap invites.

## 6. Evidence furniture (ours — the receipts layer his artifacts lacked)

- **Every score/claim row carries its receipt inline:** specimen link + views + outlier multiple + date, in stone-colored small type — present, never shouting.
- **Outlier defined where it appears:** "outlier = N× that channel's normal" in the key line, every table (adopted SM9 — the denominator is always stated).
- **Strikethrough pedagogy:** excluded rows struck + dimmed + reasoned, kept in rank position (adopted from the top-50 treatment).
- **Highlight-the-money-line:** in any rendered script/copy specimen, the one load-bearing line gets a quiet background emphasis — and if it's a `[NEED]`-flagged claim, the highlight IS the flag.
- **Phone-frame mockups** for anything that will appear on a screen (text hooks, titles): typeset as they would actually render, captioned. Recognition beats description.
- **Data-tier banner:** FRESH runs carry the provenance line (pack date + receipt path) in the footer; STALE runs carry the date-stamp + refresh command under the title; ABSENT runs carry the INTERVIEW-ONLY banner at the top. The banner placement escalates with the honesty debt.

## 7. Export row (adopted delta #30, extended)

Every artifact ends with an export row: **Download HTML · PDF** (+ Express where relevant) and the artifact's provenance line (produced date · source pack + `generated_at` · workflow that made it · data tier). His artifacts died with the session; the export row plus the `growth-lab/` state folder is why ours don't. The PDF is the deliverable of record — every semantic must survive grayscale print (see §1).

## 8. Register

Dense, decisive, quiet. Headlines sentence-case; functional labels uppercase tracked; no chartjunk, no decoration that serves none of restrained/contemporary/decisive; standfirsts one sentence that tells the reader how to read the artifact. Mobile-friendly; wide tables scroll in their own container. Ban-bank clean (`prose_classifier.py` before ship).
