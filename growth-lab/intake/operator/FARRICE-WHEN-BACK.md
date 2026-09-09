# Intake engine — the three things only you can do (est. 30 min total)

Built 2026-08-27 while you were at Disneyland. Everything below is staged and verified;
these three tasks are the ones that need your hands (accounts, money, or an arming decision).

## 1 — Create the Google Form and wire the faces (~15 min, phone-doable)

1. Open `growth-lab/intake/google-form-kit.md` and paste the blocks into a new form at
   forms.google.com. Question titles must be pasted EXACTLY (they are the parse contract).
2. Turn email collection ON, link the responses Sheet (both in the kit's Settings block).
3. Paste three values into `growth-lab/intake/faces-config.json`:
   - `form_url` — the form's send link
   - `prefill_entry` — from ⋮ → "Get pre-filled link" (the `entry.NNNNNNNNN` token; steps in the kit)
   - `sheet_id` — the linked Sheet's id from its URL
4. Re-bake the faces (exact command):

   ```bash
   .venv/bin/python3 execution/build_intake_faces.py
   ```

   The six pages in `growth-lab/intake/faces/` flip from "Intake opens shortly" to a live
   CTA with each face's report pre-selected. Send a face as a link/attachment post-DM, or
   host them later — v1 assumes no domain.

## 2 — The 15-minute Stripe task → fill `payment_url`

The open task: `_active/linkedin/05-lead-gen/2026-08-07-PAYMENT-SETUP-ACTION.md`
(it also unblocks Day-1 sends — same link). When the payment link exists, paste it into
`payment_url` in `growth-lab/intake/faces-config.json`. That one field is the single
source for every money mention (mini-report CTA + /gb-intake draft email). Until then the
system uses the documented mailto fallback — nothing dangles, nothing waits on this.

## 3 — Decide: arm the radar auto-refresh, or keep it manual

The staged-but-UNARMED job: `.scratch/kallaway-sandcastles-forge/outlier-radar-refresh.UNARMED.md`
(launchd plist + arming steps inside). Armed = client packs stay fresh without you;
unarmed = you run `outlier_radar.py refresh --niche <slug>` per engagement (the /gb-intake
recipe includes it, so nothing breaks either way). Your call — nothing self-arms.

---

Daily rhythm once live: `.venv/bin/python3 execution/intake_bridge.py status --sheet <id>`
(or check the Homebase system line — "intake: N pending" appears automatically once a
status run has seen submissions). Then per submission: `pull --row N --slug <client>` →
`/gb-intake` → review the Gmail draft → YOU send it, inside the 48h promise. After
sending, write anything in that row's `Status` column in the Sheet to clear it from the
pending count.
