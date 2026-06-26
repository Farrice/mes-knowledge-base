# Dan Wang Literary Analysis — Use Cases & Workflow Routing

> Specific deployment scenarios mapped to the matching workflow. Load on-demand
> when deciding *which* Wang workflow to fire for a given situation. Read
> `genius.md` first for the underlying patterns; this file is the routing layer.

---

## The Workflow Roster (what each one is for)

| Command | Produces | Fire when |
|---|---|---|
| `/wang-big-questions` | 2-3 live questions + staked answers + confidence note | **Before drafting anything.** You need to know what the piece is *for* — the tensions the audience is arguing about this period. |
| `/wang-friction-map` | Official-story vs. ground-truth matrix + 3-5 engine gaps + one insider-uncomfortable anchor insight | You have a topic but no *angle* yet. The gap between stated and observed is the engine. |
| `/wang-observation-engine` | A tagged note bank from meal-structured fieldwork; convergences ready for synthesis | You're going to gather primary observation (travel, site visit, customer fieldwork, immersion) and don't want to come home with photos instead of insight. |
| `/wang-xray-read` | A fire map of a book/report/dossier (skip column + fire column + key-phrase pull) | You must extract signal from dense source material fast — 80% of which is genre padding. |
| `/wang-texture-zoom` | A welded draft — every abstraction grounded, every detail elevated, oscillation tuned | You have a draft that's smart-but-dry (AN-1) or lush-but-inert (AN-2). A *welding* pass on existing prose. |
| `/wang-anchor-sentence` | A refined quotable anchor line + a backward-built structural spine | A great line drifted in and you want to build the piece around it (or you need to find the line the piece is missing). |
| `/wang-musical-pass` | A cadence-tuned draft + a read-aloud audit log | The argument is sound but the prose is flat on the ear. A music pass, not a rewrite. |
| `literary-cornerstone-sprint` | A polished annual letter / long-form essay | You have a note bank and need the full synthesis into reputation-grade cornerstone content. |
| `strategic-insight-synthesis` | A ground-truth intelligence audit | You need to extract non-obvious strategic insight from a mix of dense reading + raw field observation. |

> **The natural pipeline:** `/wang-big-questions` (why) → `/wang-xray-read` +
> `/wang-observation-engine` (gather) → `/wang-friction-map` (angle) →
> `literary-cornerstone-sprint` / `strategic-insight-synthesis` (synthesize) →
> `/wang-texture-zoom` → `/wang-anchor-sentence` → `/wang-musical-pass` (craft).
> Most single requests fire one or two of these, not the whole chain.

---

## Use Cases by Scenario

### A. "I need to write a long-form essay / annual letter from a year of notes"

**Scenario:** You've accumulated observations, fragments, and questions over months
and need to turn them into one cornerstone piece (Substack edition, founder annual
letter, flagship essay).

**Route:** `/wang-big-questions` (name the 2-3 live tensions, stake answers) →
`literary-cornerstone-sprint` (full synthesis) → `/wang-texture-zoom` (weld) →
`/wang-musical-pass` (cadence).

**Why this route:** the sprint is built for exactly this — radical infrequency ×
radical quality (Pattern 20), deadline-as-forcing-function (Tacit 2), the
qualm-collected-Canadian state to bypass perfectionism, and the zoom architecture.
Front-load `/wang-big-questions` so the piece has a reason to exist before you
draft. Close with the two craft passes.

---

### B. "This analysis is smart but dry / reads like a McKinsey memo"

**Scenario:** A whitepaper, report, or essay where the thinking is sound but it
floats free of any observed detail — generic, could be written by any AI (AN-1).

**Route:** `/wang-texture-zoom` (diagnose pole = DRY; install texture gateways) →
`/wang-anchor-sentence` (find the one quotable line) → `/wang-musical-pass`.

**Why this route:** texture-zoom is the dedicated *welding* pass — it grounds each
tectonic-plate claim in a specific observed gateway. **Critical gate:** it requires
a real observation bank. If you analyzed from a desk and have no real textures,
texture-zoom flags it honestly rather than fabricating a vendor — and you route to
`/wang-observation-engine` first to actually gather ground truth.

---

### C. "This travel/personal piece is beautiful but says nothing"

**Scenario:** Lush sensory writing — the ecstatic sunset, the charming market —
that never ladders up to an analytical point (AN-2, Wang's explicit indictment of
self-indulgent travel writing).

**Route:** `/wang-texture-zoom` (diagnose pole = INDULGENT; build the ladder up).

**Why this route:** the detail already exists; texture-zoom's Step 3 supplies the
cash-out — the one resonant lift sentence that names what the scene is secretly
evidence for, plus the friction it touches. Lift, don't explain.

---

### D. "I have a topic but no angle — what's the actual insight here?"

**Scenario:** You know the subject (an industry, a company, a policy, a trend) but
have nothing non-obvious to say. The risk is restating the press release as if it
were analysis (AN-3).

**Route:** `/wang-friction-map` (steelman the official story → map ground truth →
rank the 3-5 widest gaps → name the one insider-uncomfortable insight).

**Why this route:** friction-mapping IS the angle-finding engine. The output gate —
"would an insider find this uncomfortable AND accurate?" — is the deterministic
check against stenography. If the official and ground-truth columns say the same
thing, it tells you there's no piece yet and to go observe more.

---

### E. "I'm about to do fieldwork / travel / customer research and don't want to waste it"

**Scenario:** A trip, a site visit, customer-home shadowing, a conference floor,
competitor-store recon. The failure mode is coming home with photos and personal
ecstasy instead of observations tagged to questions.

**Route:** `/wang-observation-engine` (name live questions FIRST → design the
meal-structured day → capture raw texture → tag every note to a question → find
convergences across anchors).

**Why this route:** the engine turns Wang's meal-structured-travel method into a
repeatable protocol with a deterministic AN-2 trip-wire (the ECSTASY flag). It
generalizes fully off travel: for ICP fieldwork, anchors = moments in the
customer's real day, the walk = the in-between behaviors surveys miss, and the
said-vs-done friction IS the research payoff. Pairs with `mcraney-deep-canvass`
(the conversation layer) and `icp-research` (structures the gathered texture into
an avatar).

---

### F. "I have to read this 400-page book / dense report and pull the signal fast"

**Scenario:** You're synthesizing from dense source material where most of it is
genre padding (potted history, lit review, market-sizing boilerplate) and you need
the real claims without reading every word.

**Route:** `/wang-xray-read` (predict the genre's obligated sections → mark skip vs.
fire → pull the key analytical phrase per fire page → build a quote bank).

**Why this route:** Cowen-style x-ray vision as a procedure — read 3x the material
with equal-or-better comprehension by spending attention where the author spent
theirs. **Hard stop:** NOT for material you must master in full (exam study,
contract liability audit, reproducing a proof) — read every word there. Feeds
directly into `literary-cornerstone-sprint` or `strategic-insight-synthesis`.

---

### G. "I have a killer line and want to build something around it"

**Scenario:** A beautiful sentence drifted in — mid-walk, mid-conversation, mid-
reading — and you sense the whole piece could orbit it. Or: the inverse, your draft
is competent but nothing in it is quotable.

**Route:** `/wang-anchor-sentence` (triage: is it an anchor or just a nice note? →
refine for irony/music → build the essay *backward* so the arc earns the line).

**Why this route:** this is Pattern 6 made operational — the anchor is gravity, the
essay falls toward it. **Gate:** if there's no real line yet, it tells you NOT to
manufacture one; return to the notes until one arrives. The line must come from
within (AN-6) and carry a real payload (AN-2), not be a thesis statement in costume.

---

### H. "The argument is right but the prose is flat / lifeless on the ear"

**Scenario:** Analytically sound draft, but it reads in a monotone — four medium
sentences in a row, no flourishes, flat landings, every paragraph opening the same
way.

**Route:** `/wang-musical-pass` (read aloud cold → mark where the ear flags →
engineer sentence-length variation → place a *few* flourishes at intervals → layer
one irony for the re-reader → ship the audit log).

**Why this route:** a cadence pass, not a rewrite or a depth pass. **Hard stop:**
if the *argument* is thin, this is the wrong tool — route to `/wang-friction-map`
(find the gap) or `/deepen` first, because tuning a hollow paragraph just makes the
hollowness sing. Restraint is the whole calibration: clean lines, a *few*
flourishes — the plain sentences are the silence that makes the flourishes audible.

---

### I. "I need a strategic intelligence read on this domain/competitor/market"

**Scenario:** A mix of dense reading material (reports, dossiers, data) plus raw
field observations, and you need the hidden operating logic — the non-obvious
strategic insight, not a summary.

**Route:** `strategic-insight-synthesis` (X-ray scan the dossier for fire →
friction-mine official vs. ground truth → map the informal systems doing the real
work).

**Why this route:** this is the analytical (vs. literary-essay) front door — it
composes x-ray reading (Pattern 10), friction mining (Pattern 4), outsider error-
correction (Pattern 7), and informal-system mapping into a ground-truth intelligence
audit. Use `literary-cornerstone-sprint` instead when the deliverable needs to be
*published* (literary craft matters); use this when it needs to *inform a decision*.

---

## Cross-Domain Use Cases (applied)

### J. Social post that earns a save (LinkedIn / X)

**Scenario:** A daily/weekly post that should be the one people quote, not skim.

**Route:** `/wang-friction-map` (ONE gap, not five) → `/wang-anchor-sentence` →
`/wang-texture-zoom` (single oscillation). For zeitgeist-timed posts, lead with
`/wang-big-questions`.

**Discipline:** one oscillation, one gateway, one lift — more machinery shows the
scaffold at this length. Bring down the average (Pattern 20): one considered post
beats ten reactive takes.

---

### K. Brand positioning / campaign concept

**Scenario:** Replace category-cliché positioning with a real angle.

**Route:** `/wang-friction-map` (what the category SAYS vs. what customers
EXPERIENCE = the campaign) → `/wang-observation-engine` on *customer fieldwork* →
`/wang-anchor-sentence` (the line on the page).

**Discipline:** the ground-truth column must be *true of your product*, not
aspirational — if the matrix indicts your own product, fix the product before the
copy. Pairs with `godin-false-proxy-purge`.

---

### L. Conversion copy (VSL / landing / email)

**Scenario:** Copy that grounds benefits in lived moments and names the friction the
category won't admit.

**Route:** `/wang-texture-zoom` (copy variant — recognition anchoring, Pattern 16)
→ `/wang-friction-map` (the thing the last three vendors won't say) →
`/wang-anchor-sentence`.

**Discipline:** no fabricated texture; no literal "It's not X, it's Y" tell. Wang
supplies texture + friction; `luke-iha-copy-blocks` / `copy-engine` supply the
conversion architecture.

---

### M. Founder / operator authority piece

**Scenario:** A founder annual letter or origin piece that builds real authority
instead of survivorship-bias humblebrag.

**Route:** `/wang-big-questions` (what is my market arguing about) →
`/wang-observation-engine` (a year of operator fieldwork) →
`literary-cornerstone-sprint` → `/wang-musical-pass`.

**Discipline:** contingency over just-so stories (Pattern 19) — refuse the fated-
success narrative; reconstruct how it actually felt before anyone knew it would
work. Radical infrequency: don't dilute the cornerstone into weekly takes.

---

### N. Ghostwriting a client's thought-leadership

**Scenario:** Give a client a real, grounded position in their *own* coherent voice.

**Route:** `/wang-observation-engine` (client's immersion + outsider angle) →
`/wang-friction-map` (what the client's industry insiders have normalized) →
`/wang-texture-zoom` (ghostwriting variant — the two-author-seam fix is the whole
job) → `/wang-musical-pass` *in the client's register only*.

**Discipline:** the disappointment (Pattern 21) and the grounding details must be
the *client's*, in the client's language. Never insert your literary showpieces —
influence, not imitation. Pairs with `ghostwriting-voice`.

---

## Routing Decision Tree (quick)

```
Do I know what the piece is FOR (the live question)?
  NO  → /wang-big-questions
  YES ↓

Do I have an ANGLE (a non-obvious insight)?
  NO  → /wang-friction-map   (no observation yet? → /wang-observation-engine first)
  YES ↓

Do I have the SOURCE MATERIAL digested?
  Dense reading to mine fast?     → /wang-xray-read
  Primary observation to gather?  → /wang-observation-engine
  YES, ready to write ↓

Drafting the piece?
  Need full synthesis from notes?     → literary-cornerstone-sprint
  Need a strategic intelligence read? → strategic-insight-synthesis
  Draft exists ↓

What's wrong with the draft?
  Dry / abstract (AN-1) or lush / inert (AN-2)? → /wang-texture-zoom
  Missing a quotable spine / have a great line? → /wang-anchor-sentence
  Argument fine, prose flat on the ear?         → /wang-musical-pass
```

---

## Anti-Routing (when NOT to use Wang)

- **Tight business argument, short piece (memo, exec summary):** use
  `fareed-zakaria-writing-mastery` — Zakaria-tier argument architecture, not Wang's
  literary texture.
- **Memoir / personal-narrative literary prose:** use `lamott-craft` /
  `ocean-vuong` — Wang is *analytical*-essay literary, not confessional.
- **Pure depth problem (the idea itself is shallow):** use `/deepen` first; Wang's
  craft passes can't rescue a hollow argument.
- **The argument is thin and you reach for `/wang-musical-pass`:** stop — music
  cannot save a hollow paragraph. Fix the thinking (`/wang-friction-map` or
  `/deepen`) first.
- **Material you must master in full and you reach for `/wang-xray-read`:** stop —
  x-ray reading is for extracting signal from padding, not for exam study, contract
  audits, or reproducing proofs. Read every word.
