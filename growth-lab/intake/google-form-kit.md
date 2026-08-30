# Google Form Kit — intake form, copy-paste, 15 minutes from a phone

Build once at `forms.google.com` → blank form → paste the blocks below in order.
Question titles must be pasted EXACTLY (they become the Sheet column headers that
`execution/intake_bridge.py` parses — the contract is the header row at the bottom
of this file). Supersedes the retired 2026-07-29 Angle-Audit form template: the
mechanics carry over, the offer copy there is dead.

## Settings (do these first)

1. Settings → Responses → **Collect email addresses: Verified** (or "Responder input" — either produces the `Email Address` column).
2. Settings → Responses → **Limit to 1 response: OFF** (no Google sign-in wall for cold prospects if "Responder input" chosen).
3. Settings → Presentation → progress bar ON · shuffle OFF.
4. Responses tab → Sheets icon → **Create new spreadsheet** ("Growth Report Intake — Responses"). After creating it, paste the spreadsheet id (the long string in its URL) into `sheet_id` in `growth-lab/intake/faces-config.json`.

## Form title

```
Content Growth Report — Intake
```

## Form description

```
Nine questions, about seven minutes. No uploads, no prep — your answers are enough.

Within 48 hours of submitting, you get a free mini-read of your niche built from
real channel data: the videos beating their own channels' normal, where demand
concentrates right now, and one open lane nobody is crowding. It's yours either way.

If you want the full report after that, you'll know exactly what it covers.
```

## The nine questions (paste titles EXACTLY — they are the column contract)

**Q1 — Paragraph · Required**
```
What do you sell, and at what price?
```
Help text:
```
One or two sentences. E.g. "Performance supplements, hero product $54, subscription-first."
```

**Q2 — Paragraph · Required**
```
Describe your ideal buyer: the one person you most want more of
```
Help text:
```
A person, not a demographic. Someone real you've sold to counts double.
```

**Q3 — Short answer · Required**
```
If your content worked perfectly, what changes for you? (one sentence)
```

**Q4 — Paragraph · Required**
```
Top 3 problems your buyers bring you, in their words
```
Help text:
```
Their words, not yours. What do they say right before they buy — or right before they don't?
```

**Q5 — Paragraph · Required**
```
What can you honestly claim that almost nobody else in your space can?
```
Help text:
```
Experience, results, credentials, a story — anything most people in your space can't honestly say.
```

**Q6 — Paragraph · Required**
```
Where does your content live today, and what gets in the way?
```
Help text:
```
Platforms, posting rhythm, who makes it, and the real constraint (time, compliance, team, budget).
```

**Q7 — Paragraph · Required**
```
Which creators or competitors do you watch? (names or links, up to 5)
```
Help text:
```
Channel links or @handles are best — we use these to pull real data for your mini-read.
```

**Q8 — Multiple choice · Required**
```
What matters most right now?
```
Options (exact):
```
Reach - get discovered by new people
Trust - deepen the audience you have
Conversion - turn viewers into buyers
```

**Q9 — Multiple choice · Required**
```
Which report should we build first?
```
Options (exact — these are also the prefill values baked into the landing faces):
```
Positioning Dossier - your buyer, mapped in their own words
Whitespace Map - the lanes your niche is leaving open
Audience Bullseye - who to aim at, ring by ring
Topic Scan - the 50 videos your niche is voting on right now
Format Playbook - the shapes that carry winning ideas
Growth Blueprint - the full system in one plan
Not sure - read my answers and recommend one
```

## Confirmation message (Settings → Presentation → Confirmation message)

```
Got it — thank you.

Your free mini-read is now in the queue. It's built from real channel data
pulled for your niche, not a template, so it takes up to 48 hours.

It lands in the inbox you gave. Nothing else will — no sequence, no drip.
```

## After creating: wire the faces

1. Send button → link icon → copy the form URL → paste into `form_url` in `growth-lab/intake/faces-config.json`.
2. Form ⋮ menu → **Get pre-filled link** → pick any Q9 option → Get link → copy it. The URL contains `entry.NNNNNNNNN=` — paste that `entry.NNNNNNNNN` token into `prefill_entry` in the same config.
3. Re-bake the faces: `.venv/bin/python3 execution/build_intake_faces.py`

## The linked-Sheet column contract (what intake_bridge parses)

Google Forms writes question titles verbatim as the header row of "Form Responses 1".
Flat schema, Vibe-Tax style — one row per submission, expected header row EXACTLY:

```
Timestamp | Email Address | What do you sell, and at what price? | Describe your ideal buyer: the one person you most want more of | If your content worked perfectly, what changes for you? (one sentence) | Top 3 problems your buyers bring you, in their words | What can you honestly claim that almost nobody else in your space can? | Where does your content live today, and what gets in the way? | Which creators or competitors do you watch? (names or links, up to 5) | What matters most right now? | Which report should we build first?
```

- Machine truth: `QUESTION_TITLES` in `execution/intake_bridge.py`. Change a title in the
  form → change the tuple, or the parse fails loud (by design).
- Optional: add a `Status` column BY HAND in the Sheet (never in the form). Write anything
  ("sent 08-29") after handling a row — `status` then excludes it from the pending count.
- Read paths: `intake_bridge.py status --sheet <id>` (gws CLI) or File → Download → CSV
  then `--csv <path>` (always works).
