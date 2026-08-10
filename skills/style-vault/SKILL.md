---
name: style-vault
description: "The brand-image pipeline and the keyed style vault — many looks, switchable by brand x ICP x platform, compounding instead of restarting. Runs ICP psychographics into scene inventories (pain-scenes + desire-scenes), mines a decomposable style-probe sweep, AUDITIONS the winner across the whole scene set before any volume spend, banks it as a characterized card, then permutes the locked style into an image bank the content pipeline consumes. Use when: starting brand imagery for a new client or platform, you need on-brand images at volume, an existing look must be captured as a reusable entry, you are asking which banked style fits this post, or a style bank needs building/extending. Craft is DELEGATED, never restated — frame construction is nick-st-pierre, sweep and board-card discipline is rory-flynn, is-this-slop diagnosis is grace-liu. Trigger phrases: style vault, style bank, brand images, image bank, brand imagery, which style for this, bank this look, scene inventory, audition the style, batch the bank, on-brand images at volume. Ported from Luke Carter (YouTube sAMArYBpDmI, 2026-08-08) to a no-Midjourney stack."
---

# Style Vault — the brand-image pipeline

> **THE MISSION (Farrice, 2026-08-09, re-affirmed 2026-08-10).** ICP-avatar-grounded,
> situationally-aware, high-craft imagery for **whatever content is being made** — an image that
> resonates instantly with the specific buyer, the topic, and the moment, at the proven quality
> bar (`v6-03`, the plate he called "perfect"). The cover plate is the per-asset UNIT; the
> pipeline — ICP → scenes → style → bank → plate — is the PRODUCT. Every workflow below carries
> the same spine: the realism floor (`references/realism-floor.md`, layers 1–8 mechanical via
> `lint --strict`, 9/9a/9b judgment gates) and the four-variant zoom verdict. Content and decks
> are his; the imagery, end to end, is this system's job.

> **What this skill is for.** Deciding **what scene serves which buyer**, and **operating the
> vault**. It does not teach you to build a frame — the house already owns that layer and
> restating it would create a second, drifting copy.
>
> | Layer | Owner | Load when |
> |---|---|---|
> | Is this slop, and at which layer? | `grace-liu` | Before anything, on any foggy ask |
> | How is the frame constructed? | `nick-st-pierre` | Writing any actual prompt |
> | How is a style asset characterized and swept? | `rory-flynn` | Running the probe / writing a card |
> | **What scene, for whom, and where does it live?** | **this skill** | Always |
>
> **The one thing that is genuinely new here:** every skill above directs *how the frame looks*.
> None of them decides *what is happening in the frame and which buyer emotion it serves*. That
> bridge — ICP psychographics → scene inventory → banked style — is this pipeline.

---

## THE PREMISE

Carter's workflow locks **one** style for **one** brand. That is correct for a solo operator
with one audience and wrong for this house, which serves Farrice/Parallax, Proof-to-Market,
Jen's listings and My.BPM — plus per-platform registers inside each.

So the deliverable is not a locked look. It is a **vault**: many characterized entries, keyed
and retrievable, that compound. Farrice's own framing (2026-08-09):

> "There are going to be times where, even for client-facing work, I might have to make brand
> assets… I don't want to have to rework and retool everything every time I have a new client.
> Certain styles exceed and thrive on certain platforms. I want a vault I can go to, switch, and
> call upon… versus blanketing and using one style for everything, because that doesn't work."

**The rule that generates the rest:** *a style that cannot be described in words is not in the
vault — it is in a folder.* An entry earns its slot by being characterized (what it does, what
it refuses, where it belongs) and **verified by a dated run**. Description is not verification.

---

## THE PIPELINE

```
ICP profile ──▶ 01 seed-scenes ──▶ scene inventory (pain + desire)
                                          │
                          probe sweep ◀───┤
                                          ▼
                              02 mine-and-audition
                     (sweep → pick → AUDITION across ALL scenes)
                                          │
                                   card.md + verified
                                          ▼
                                 03 bank-and-batch
                        (permute → generate → curate → index)
                                          ▼
                          image bank the content pipeline consumes
```

| Workflow | Deliverable |
|---|---|
| **`workflows/04-cover-plate.md`** | **THE imagery run — one verified cover plate at the proven v6-03 standard (~120 credits). The default front door: brief in, image out.** |
| `workflows/01-seed-scenes.md` | A scene inventory: 3+ pain-state and 3+ desire-state scenes drawn from a real ICP profile, plus the fixed probe subject |
| `workflows/02-mine-and-audition.md` | A decided style, proven to replicate across the whole scene inventory, written to a `card.md` with `verified` set |
| `workflows/03-bank-and-batch.md` | A permuted, curated, indexed image bank keyed to brand × ICP × platform |

**Scope ruling (Farrice, 2026-08-10):** this skill's product is the IMAGERY — the *whole
pipeline of it*, not only covers. `04` is the per-asset run; `01→03` are the compounding spine
that makes each run land for the right buyer in the right moment. Decks, captions and content
are his; the deck pipeline (workflow 03 § deck doctrine) stays wired but is optional and only
runs on his ask.

## THE VAULT

Store: `skills/generate/styles/<slug>/` — `prompt.md` (untouched; the assets board reads it) plus
a sibling `card.md` carrying the keying and characterization.

```bash
python3 execution/style_vault.py list --brand jen-listings --platform instagram
python3 execution/style_vault.py show turrell-light-gallery
python3 execution/style_vault.py probe --n 24 --subject "<fixed probe subject>"
python3 execution/style_vault.py permute "{a, b} scene at {dawn, dusk}"
python3 execution/style_vault.py validate --strict     # exit 1 if any card has gaps
python3 execution/style_vault.py index                 # regenerate VAULT.md
```

**Tiers** (Flynn's, and they decide the entry's *job*):

| Tier | Signature | Job |
|---|---|---|
| `tight` | overrides the probe almost entirely | reproduce a look |
| `broad` | several aesthetics coexist | a house style with room |
| `micro` | one isolated effect | **stack fuel** — composes with others |

A vault with no `micro` tier is a finding, not a preference: it means nothing in the bank
composes, so every new need starts from zero.

## THE VERIFICATION CONTRACT

`gaps()` in `style_vault.py` refuses to mark a card shippable until **`verified: YYYY-MM-DD`**
is set by an actual run. This exists because characterization fields can be filled by reading a
prompt string, and that is inference, not evidence — exactly the green-from-nothing failure the
verification spine was built to kill (2026-08-08). If a card reads OK, someone ran it.

## COST

Stated per the cost-transparency binding:

- **This pipeline itself: $0** — local Python, no API.
- **A probe sweep:** `nano-banana-2` at **$0.0062/image**. 24 candidates × 4 = 96 images ≈ **$0.60**.
- **A 140-image bank:** ≈ **$0.87**.
- Cost gate fires on every paid invocation; a denial surfaces to Farrice and is never retried.
- ⚠️ `flux-2` is a **deferred stub** — endpoint and price UNCONFIRMED, refuses to run. Do not
  plan an escalation lane through it until its recipe is filled.

## HANDOFFS (options, never a pipeline)

Generation itself goes through `/generate` (`creative_router.py` lanes are binding). Styled and
poster families are `fantastic-posters`. Character identity is a *different kind of entry* — it
answers "who is in the frame," never "what does the frame look like" — and combines with a style
card rather than replacing one.

## SOURCE AND FIDELITY

Ported from Luke Carter, *"Stop Posting AI Slop (Build Your Own Style Instead)"* (`sAMArYBpDmI`,
2026-08-08, 18:27). **Fidelity: HIGH on the pipeline shape, and deliberately partial on craft** —
roughly 70% of the video's technique was already extracted here in `nick-st-pierre` (including
`--sref random` and the `--sw`/`--stylize` dials) and `rory-flynn` (null run → probe → tier →
weight sweep → named recipes). Re-extracting it would have produced a second drifting copy.

What was taken: the ICP→scene bridge, the audition gate, permutation batching, and bank-as-
infrastructure. Every Midjourney-specific move and its honest stack translation — including the
two that **do not port** — is in `references/midjourney-port.md`.

**On his taste, plainly:** his demonstrated output is a flat pastel-blue editorial illustration
world. Coherent and genuinely not slop — but competent, not world-class. The method buys
consistency; the ceiling is the operator's. Take the mechanism, not the look.
