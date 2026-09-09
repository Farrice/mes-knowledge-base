# Intake Engine — Growth Blueprint OS pipeline front door

One form engine, six per-artifact faces, one bridge, one manual-fire workflow. A prospect
lands on a face → answers nine questions → the submission reaches the linked Sheet →
`intake_bridge.py` turns a row into a frozen-shape intake-pack → Farrice fires `/gb-intake` →
a free personalized mini-report goes out as a Gmail DRAFT within the 48-hour promise →
the paid full artifact is the upsell. Nothing sends itself. Nothing fires itself.

Locked decisions (Farrice, 2026-08-27): ONE form engine with per-artifact landing faces ·
free mini-report → paid full Blueprint upsell · 48-hour turnaround promise.
Boundary (binding): this tier collects **business answers only — no client file uploads**;
confidential inputs stay behind the manual READY/HOLD gate of a paid engagement.
Reader purity (binding): every prospect-facing surface (faces, form copy, mini-report,
draft email) carries zero operator language. Operator docs live here and in `operator/`.

## The nine questions → the frozen input-pack shape

The intake-pack contract is the FROZEN 9-section shape of
`extractions/kallaway/baseline-input-pack.md` (read-only, never edit). Seven questions fill
seven sections verbatim; two questions are routing metadata; two sections have no honest
form-sized question and are declared `NOT PROVIDED — interview fallback` (they are drafted
live in `/gb-interview`, never invented from form text).

| # | Form question (exact title = Sheet column header) | Type | Feeds section |
|---|---|---|---|
| Q1 | What do you sell, and at what price? | paragraph | 1 · The business behind the content |
| Q2 | Describe your ideal buyer: the one person you most want more of | paragraph | 2 · Ideal viewer/buyer avatar |
| Q3 | If your content worked perfectly, what changes for you? (one sentence) | short | 3 · Dream outcome (one sentence) |
| Q4 | Top 3 problems your buyers bring you, in their words | paragraph | 4 · Pain points bank (ranked, in their words) |
| Q5 | What can you honestly claim that almost nobody else in your space can? | paragraph | 5 · Unfair advantage / unique expertise inventory |
| Q6 | Where does your content live today, and what gets in the way? | paragraph | 7 · Platform reality |
| Q7 | Which creators or competitors do you watch? (names or links, up to 5) | paragraph | 8 · Known competitors/creators they watch — **doubles as radar niche seeds** |
| Q8 | What matters most right now? | multiple choice: Reach / Trust / Conversion | routing metadata (recorded under §7 + manifest); mirrors the mini-report's goal personalization |
| Q9 | Which report should we build first? | multiple choice, 7 options | routing metadata (manifest + chain selection); arrives pre-selected by the face's prefill URL |
| — | *(no form question)* | — | 6 · Target Authority Statement candidates → interview fallback |
| — | *(no form question)* | — | 9 · Delivery style → interview fallback |

Column contract, machine truth: `QUESTION_TITLES` in `execution/intake_bridge.py` —
update the kit and the tuple together or the parse fails loud.

## Routing table — Q9 answer → chain → face

The Q9 choice labels are exact strings (they are simultaneously the form options, the
prefill values baked into each face's CTA, and the routing keys in `intake_bridge.py
ROUTES`). Because each face pre-selects its own artifact, the Q9 answer also names which
face sent the prospect.

| Q9 answer (exact) | Artifact | Paid chain (manual fire) | Came from face |
|---|---|---|---|
| Positioning Dossier - your buyer, mapped in their own words | positioning-dossier | /gb-interview | faces/face-positioning-dossier.html |
| Whitespace Map - the lanes your niche is leaving open | whitespace-map | /gb-interview → /gb-whitespace | faces/face-whitespace-map.html |
| Audience Bullseye - who to aim at, ring by ring | bullseye | /gb-interview → /gb-whitespace → /gb-bullseye | faces/face-bullseye.html |
| Topic Scan - the 50 videos your niche is voting on right now | topic-scan | /gb-topic-scan (pack required — radar refresh first) | faces/face-topic-scan.html |
| Format Playbook - the shapes that carry winning ideas | format-playbook | /gb-topic-scan → /gb-format-find | faces/face-format-playbook.html |
| Growth Blueprint - the full system in one plan | growth-blueprint | full chain: /gb-interview → /gb-whitespace → /gb-bullseye → /gb-topic-scan → /gb-format-find → /growth-blueprint | faces/face-growth-blueprint.html |
| Not sure - read my answers and recommend one | *(recommend)* | by Q8 goal: Reach → Topic Scan · Trust → Positioning Dossier · Conversion → Whitespace Map | any face / direct link |

The chain fires only when Farrice says paid. The free mini (below) is the default
deliverable for **every** submission regardless of Q9.

## The FREE-MINI recipe (end-to-end, $0 external)

Every submission gets a personalized mini-report inside the 48h promise. The clock starts
at the submission timestamp; `intake_bridge.py status` shows elapsed vs 48h on every row.

```bash
# 1 — see what came in (writes .agent/intake/pending.json for the Homebase count)
.venv/bin/python3 execution/intake_bridge.py status --sheet <id>     # or --csv <export.csv>

# 2 — pull one submission into an engagement (frozen-shape intake-pack + manifest block)
.venv/bin/python3 execution/intake_bridge.py pull --row N --csv <export.csv> --slug <client-slug>

# 3 — seed the radar from their Q7 answer (pull prints the parsed seeds)
.venv/bin/python3 execution/outlier_radar.py add-channels --niche <client-slug> @handle1 @handle2
.venv/bin/python3 execution/outlier_radar.py refresh --niche <client-slug>

# 4 — bake the personalized mini-report from their pack
.venv/bin/python3 execution/build_lead_magnet.py \
    --pack .agent/outlier-radar/packs/<client-slug>/latest.json \
    --niche-label "<their niche, in their words from Q2/Q7>" \
    --cta-url "<payment_url from faces-config.json; mailto fallback while unset>" \
    --out growth-lab/<client-slug>/exports/mini-report.html

# 5 — PDF of record
.venv/bin/python3 execution/export_growth_package.py pdf growth-lab/<client-slug>/exports/mini-report.html

# 6 — delivery surface: Drive upload (Doc/PDF link) via gws, then a Gmail DRAFT.
#     DRAFT, never send — Farrice reviews and sends himself, inside the 48h promise.
#     /gb-intake (the workflow) walks these two steps with the draft copy.
```

Degradation is honest at every step: a thin or failed radar refresh bakes the
interview-only mini variant (no fabricated numbers, "data refresh pending" line) —
that still ships inside 48h, because the promise is the turnaround, not the data tier.

## The paid-full upsell slot — `{{PAYMENT_URL}}` (single source)

There is exactly one payment placeholder in this system: the `payment_url` field of
`growth-lab/intake/faces-config.json`. Everything that mentions money reads it from there:

- the mini-report CTA (`--cta-url` in step 4 above),
- the upsell paragraph in the `/gb-intake` draft email,
- nothing else — faces never show prices; they sell the free mini first.

`payment_url` is **unset** until Farrice completes the open 15-minute Stripe task:
`_active/linkedin/05-lead-gen/2026-08-07-PAYMENT-SETUP-ACTION.md`. While unset, the
documented fallback CTA is `mailto:farrice.cain@gmail.com?subject=Full%20report` —
a reply-to-buy path that costs nothing and never dangles a dead link. When the Stripe
link exists: paste it into `payment_url`, re-run any bakes, done. No other file needs
editing (that is the point of the single source).

## Pieces of the machine

| Piece | Path | Job |
|---|---|---|
| Form kit | `growth-lab/intake/google-form-kit.md` | Copy-paste blocks: build the Google Form from a phone in 15 min |
| Wiring config | `growth-lab/intake/faces-config.json` | Single source: form_url, prefill_entry, payment_url, sheet_id |
| Face template | `templates/intake/face.html` | Premium Minimal static pitch surface (no JS, no network, no storage) |
| Face baker | `execution/build_intake_faces.py` | Bakes `growth-lab/intake/faces/face-<artifact>.html` ×6; graceful "opening soon" while unwired |
| Bridge | `execution/intake_bridge.py` | `status` (48h clock + pending.json) · `pull` (frozen-shape intake-pack + manifest) |
| Workflow | `skills/growth-blueprint-os/workflows/gb-intake.md` (`/gb-intake`) | Manual-fire: free-mini by default, chain when paid, Gmail DRAFT always |
| Homebase | `execution/homebase_board.py` `radar_freshness()` | Appends "intake: N pending" when `.agent/intake/pending.json` exists |
| Operator list | `growth-lab/intake/operator/FARRICE-WHEN-BACK.md` | The three tasks only Farrice can do |

Landmines honored: deterministic observability (`status` + Homebase count — never
"remembered"), Gmail DRAFT-never-send, extractions baseline read-only, Google Form
creation is manual (no Forms API dependency), no hosted-domain dependency in v1
(faces are files; send them as links or attachments, or host later).
