# Wargame: Lindy Hop 8-Week Beginner Course — One-Page Landing Site

**Consequence horizon applied: 3rd order** (website build = XHIGH-effort mission class). 1st order = the page renders without errors. 2nd order = it works correctly for the actual visitor (mobile, arriving cold off an Instagram reel, low patience). 3rd order = it survives handoff to a non-technical studio owner who will edit copy directly in a text editor with no developer present — which is why every fabricated or placeholder fact below is tagged in-line rather than buried in a way a non-technical editor could accidentally publish as real.

**Model tier this drafting pass ran at: Sonnet 5** (current session tier; no escalation to a higher tier was dispatched for this paper pass — logged here rather than left silent, per the policy that any tier decision gets stated, not assumed).

---

## 1. Mission Spec

**Problem**: Build a one-page static landing site for an 8-week beginner lindy hop course in Chicago. Single conversion goal: get the visitor to reserve a spot.

**Audience**: 25–40yo working professionals, arriving cold off an Instagram reel — mobile device, skeptical, low patience, zero brand familiarity. They will not scroll past friction, will not tolerate a broken layout, and will not fill out a form that looks unfinished.

**CTA / Definition of Done**: One primary action — **"Reserve a spot"** — wired to the provided Mailchimp signup destination. Price: **$120 early bird**. Start date: **Sept 2**. Complete when:
- Static site exists at `./site` — `index.html`, `styles.css`, `script.js`, nothing else (no `assets/` unless real files were found — they weren't, see R2).
- All 6 required sections present, in this order: hero → why-lindy-hop → instructor bios → schedule/pricing → FAQ → reserve CTA.
- Zero horizontal scroll at 375px, 390px, 428px.
- Plain HTML/CSS/JS. No framework, no build step, no CDN dependency.
- All verification runs (Section 5) pass.

**Frozen design tokens** (pre-decided so the executor never chooses):

| Token | Frozen value |
|---|---|
| `--bg` | `#FAF7F0` (warm cream) |
| `--ink` | `#201C18` |
| `--accent` | `#B23A2E` (swing-red — CTA + interactive) |
| `--accent-gold` | `#C9971F` (dividers/secondary accents) |
| `--muted` | `#6B6259` |
| Display font | `Georgia, "Times New Roman", serif` — headlines only |
| Body font | `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` |
| Font loading | System stack only. Zero `@font-face`, zero external font requests. |
| Spacing scale | `8 / 16 / 24 / 32 / 48 / 64` (px, 8-base) |
| Breakpoints | Mobile-first unprefixed base → `@media (min-width: 600px)` → `@media (min-width: 900px)` |
| Test widths | 375, 390, 428 (must-pass no-scroll) + 600, 900, 1200 (sanity) |
| Container | `.wrap { max-width: 680px; margin-inline: auto; padding-inline: 16px; }`, `box-sizing: border-box` on `*` |
| CTA copy | Exactly **"Reserve a spot"** — same string, every instance, no synonyms |
| CTA touch target | Minimum 44×44px |
| Imagery | Zero `<img>` tags against real photography (none exists — R2). Inline SVG placeholders only, each tagged `<!-- DEMO CONTENT -->` |
| JS scope | Vanilla only — FAQ accordion toggle + smooth-scroll for in-page anchors. No library, no CDN script tag, ever |

---

## 2. RECON NEEDED (resolved against the assumed findings)

**R1 — existing site directory.**
Command: `ls -la ./site 2>&1`
- If found (any files listed): **ABORT A1** — do not overwrite, flag the conflict before any write.
- If not found: proceed to scaffold fresh at `./site/`.
- **RESOLVED**: no existing `site/` directory → not-found branch fires → fresh scaffold, no abort triggered.

**R2 — brand assets.**
Command: `find . -iname "*.png" -o -iname "*.svg" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.woff*" 2>/dev/null | grep -v node_modules`
- If found: copy into `site/assets/`, reference by relative path, use real files for hero/instructor imagery, real fonts if webfont files exist.
- If not found: inline SVG placeholders for every visual element (hero ornament, section icons, instructor headshots), zero `<img>` tags pointing at real photography, every placeholder tagged `<!-- DEMO CONTENT -->`, system font stack frozen (no `@font-face`).
- **RESOLVED**: no brand assets on disk → not-found branch fires → full inline-SVG-placeholder route active, system fonts frozen.

**R3 — course/instructor inputs.**
Command: `ls -la ./inputs/ 2>&1` and `find . -iname "*bio*" -o -iname "*instructor*" 2>/dev/null`
- If found: read real instructor names, credentials, studio address, and refund policy verbatim from `inputs/`. No fabrication needed.
- If not found: course logistics that ARE in the brief (8 weeks, beginner level, Chicago, $120 early bird, Sept 2 start) are usable as given. Instructor names/credentials/photos, exact studio address, and refund policy are **not** in the brief and **not** on disk — genuinely missing inputs. Do not invent real-sounding names or credentials. Ship instructor bios and the affected FAQ answers as explicitly labeled placeholder copy (e.g. `[Instructor Name — bio pending]`), each tagged `<!-- DEMO CONTENT: replace before real launch -->`.
- **RESOLVED**: `inputs/` does not exist → not-found branch fires → placeholder-and-flag route active. Mission status: **UNBLOCKED WITH FLAGGED GAPS** — the four missing facts (instructor names, credentials, studio address, refund policy) are BLOCKED pending real input from the studio; everything else proceeds.

**R4 — Mailchimp CTA destination.**
Settling question: does `https://example.us1.list-manage.com/subscribe` carry Mailchimp's real embed query params (`u=...&id=...`)?
- If it does: build a proper `<form action="...">` POST embed with Mailchimp's standard hidden-field pattern.
- If it doesn't (bare path, no `u`/`id`, explicitly marked "- demo"): do **not** build a fake form action — against a non-resolving demo domain it will silently fail. Wire the CTA as a plain `<a href="...">` anchor button instead, tagged `<!-- DEMO CTA: replace with real Mailchimp embed code before launch -->`.
- **RESOLVED**: URL given is bare, no params, explicitly marked demo → anchor-link branch fires. CTA is a link, not a form POST.

**R5 — framework/build tooling.**
Command: `find . -maxdepth 2 -iname "package.json" -o -iname "webpack.config*" -o -iname "vite.config*" 2>/dev/null`
- If found: a build pipeline exists elsewhere in the repo — still do not pull it into `./site`; the brief freezes plain HTML/CSS/JS.
- If not found: confirms from-scratch plain build is the only path.
- **RESOLVED**: no existing `site/` directory and no adjacent tooling surfaced → not-found branch fires → plain-build path confirmed. This also seeds Abort A2.

---

## 3. Moves

```
Move 1 — Scaffold.
Expect: three files exist — site/index.html, site/styles.css, site/script.js — and
  index.html contains six empty section skeletons with ids in document order:
  #hero, #why-lindy-hop, #instructor-bios, #schedule-pricing, #faq, #reserve.
Fail: a fourth file appears (e.g. package.json, a components/ folder) — signals the
  executor defaulted to a framework scaffold habit instead of reading R5's resolution.
Counter-move: delete the extra file/folder, confirm only the three named files exist.
Trigger: if `find site/ -type f | wc -l` returns anything other than 3 after this
  move, apply the counter-move before starting Move 2.
```

```
Move 2 — Global reset, tokens, viewport.
Expect: <head> contains `<meta name="viewport" content="width=device-width,
  initial-scale=1">`; styles.css opens with `*{box-sizing:border-box}` and the
  frozen CSS custom properties from the token table; base (unprefixed) rules are
  the mobile layout, with min-width media queries added, never max-width-first.
Fail: page renders at desktop width when emulated at 375px — signals the viewport
  meta tag is missing or malformed, the single most common cause of phantom
  horizontal scroll on mobile.
Counter-move: add the exact viewport meta tag above; re-check.
Trigger: if scrollWidth > clientWidth at 375px at any later move, return to this
  move first before patching the section that appeared to cause it — the viewport
  tag is the first thing to rule out, not the last.
```

```
Move 3 — Hero section.
Expect: full-bleed section with headline (display font), one-line subhead, the
  primary CTA anchor ("Reserve a spot" → the R4-resolved href), and one decorative
  inline SVG ornament (e.g. a swing-dance flourish) marked `aria-hidden="true"`
  with no accessible name, since it carries no information a screen reader user
  needs.
Fail: CTA button renders below 44px touch height at 375px — signals padding was
  set in the token scale's smaller unit (8px) instead of a combined value that
  clears 44px.
Counter-move: set explicit `min-height:44px; min-width:44px` on the CTA button
  class, independent of the padding token.
Trigger: if the rendered CTA box is under 44×44px at any tested width, apply the
  counter-move immediately — this is the only button most Instagram-referred
  visitors will ever tap.
```

```
Move 4 — Why Lindy Hop section.
Expect: 3–4 short benefit blocks (no partner needed, no experience needed, live
  music culture, welcoming beginner room), each with a small decorative inline SVG
  icon using the SAME markup pattern as Move 3's ornament — `aria-hidden="true"`,
  no accessible name. Section explicitly does NOT include a testimonials or
  social-proof subsection.
Fail: a "what people are saying" or quote-block subsection appears — signals the
  executor pattern-matched a generic landing-page template shape rather than the
  six sections actually named in the brief, and, with no real testimonials
  available, would have to fabricate a quote to fill it.
Counter-move: delete the subsection entirely. Scope is exactly the six named
  sections — no more.
Trigger: if any blockquote, star-rating, or attributed quote markup appears
  anywhere in the file, remove it and re-check against the six-section list
  before continuing.
```

```
Move 5 — Instructor bios section (anticipates the executor's own pattern-match
  from Move 3/4).
Expect: instructor cards render with a placeholder avatar (inline SVG silhouette)
  and placeholder name/credential text, each explicitly tagged
  `<!-- DEMO CONTENT: replace before real launch -->`; the avatar SVG is NOT
  marked aria-hidden, and the name text is present as real accessible content
  (even though its value is a placeholder string, its accessibility wiring is
  real).
Fail: the instructor avatar SVG inherits `aria-hidden="true"` copied wholesale
  from Move 3/4's decorative-icon markup — signals the executor treated this SVG
  as visually identical to the earlier ornaments and pattern-matched the code
  path instead of noticing this one is content-bearing (it stands in for a real
  person's photo, associated with a real name once the placeholder is replaced).
Counter-move: strip `aria-hidden` from every instructor avatar SVG; ensure the
  instructor's (placeholder) name sits in real text adjacent to the avatar, not
  inside an aria-hidden container.
Trigger: if any SVG inside #instructor-bios carries `aria-hidden="true"`, remove
  it before moving to Move 6 — decorative-icon markup and content-bearing
  placeholder markup must never share the same accessibility treatment just
  because they look the same inline.
```

```
Move 6 — Schedule / pricing section.
Expect: an 8-week schedule and single price ($120 early bird, class starts Sept 2)
  rendered as a responsive card or stacked-list layout — NOT an HTML `<table>` —
  so nothing needs a fixed column width that could force overflow.
Fail: the executor reaches for a `<table>` because "a schedule is tabular data" —
  signals a semantic-correctness instinct overriding the mobile-first constraint;
  a wide table at 375px either overflows the viewport or gets crushed unreadable.
Counter-move: rebuild as a card/list layout; if tabular semantics matter, use
  `role="table"`-equivalent ARIA on divs rather than a literal `<table>` element,
  or simply accept list semantics — the brief's hard constraint (no horizontal
  scroll at 375px) outranks table semantics here.
Trigger: if a `<table>` element exists inside #schedule-pricing at any point,
  replace it before Move 7. Also: do not invent a "regular price" to contrast
  against the $120 early-bird figure — no second price was given; state the
  early-bird price and the Sept 2 start date only.
```

```
Move 7 — FAQ section.
Expect: 4–6 questions (no partner needed, no experience needed, what to wear,
  cancellation/refund policy, exact studio address) as a JS-toggled accordion;
  every answer that depends on a fact NOT in the brief and NOT found in inputs/
  (studio address, refund policy — per R3) is rendered as placeholder text
  tagged `<!-- DEMO CONTENT: replace before real launch -->` rather than invented.
Fail: a specific studio street address or a specific refund window (e.g. "full
  refund within 7 days") appears without a DEMO CONTENT tag — signals the
  executor filled a factual gap with a plausible-sounding invented answer instead
  of flagging it, which is exactly the failure mode R3 exists to prevent.
Counter-move: replace the invented specific with an explicit placeholder string
  and the DEMO CONTENT tag; do not soften this into a vague non-answer either —
  the tag itself is the signal, not euphemism.
Trigger: grep the FAQ answers for any address- or policy-shaped specific claim;
  if it lacks an adjacent DEMO CONTENT comment, apply the counter-move before
  Move 8.
```

```
Move 8 — Reserve CTA section.
Expect: the final section repeats the CTA — exact string "Reserve a spot", exact
  href from R4's resolution — as an `<a>` anchor button, not a `<form
  action="...">`. Price and date restated verbatim: $120 early bird, Sept 2 start.
Fail: this CTA's copy drifts from Move 3's hero CTA (e.g. "Book Now" here vs.
  "Reserve a spot" there) — signals the two instances were written independently
  instead of from one frozen string, which reads as two different offers to a
  skimming mobile visitor.
Counter-move: replace with the exact frozen string, same case, same wording, in
  both places.
Trigger: if a grep for the CTA string returns more than one distinct variant
  across the file, normalize all instances to the frozen string before Move 9.
```

```
Move 9 — Cross-section consistency + no-framework check.
Expect: grep confirms (a) every CTA instance matches the frozen string and href
  exactly, (b) zero `<link>` or `<script src>` pointing at an external CDN
  (Bootstrap, Tailwind, jQuery, any framework) anywhere in index.html.
Fail: a CDN `<script src="https://cdn...">` tag appears — signals the executor
  reached for a familiar accordion/nav library out of habit rather than the
  vanilla-JS scope frozen in the token table.
Counter-move: remove the CDN reference; reimplement the behavior (FAQ toggle,
  smooth scroll) in script.js using plain `addEventListener` and no dependency.
Trigger: if any request in the rendered page's network activity would reach
  outside `./site` (other than the single CTA `<a href>` to the Mailchimp
  destination, which is a link the user clicks, not a page dependency), this is
  an automatic ABORT A2, not a patch-and-continue — rebuild the offending piece
  plain before re-attempting verification.
```

```
Move 10 — Full responsive + no-horizontal-scroll gate.
Expect: at 375px, 390px, and 428px viewport widths, `document.documentElement.
  scrollWidth <= document.documentElement.clientWidth` holds for the full page,
  section by section; the FAQ accordion opens/closes without introducing
  overflow; smooth-scroll anchors land on the correct section id.
Fail: overflow appears at exactly one breakpoint (e.g. 375px only, not 390/428)
  — signals a fixed-px width somewhere near the container's lower bound (a
  literal px value close to but under 375, or a margin/padding pair that only
  breaches at the narrowest tested width) rather than a viewport or box-sizing
  problem (already ruled out in Move 2).
Counter-move: search styles.css for any literal px width value between 300–380
  outside the token table; convert to a relative unit (%, max-width with
  min(), or the spacing scale) and re-test all three widths.
Trigger: if overflow persists after two counter-move attempts at the same
  breakpoint, this is ABORT A4 — stop and flag the specific selector for manual
  review rather than continuing to patch blind.
```

---

## 4. Abort Conditions

- **A1** — `ls site/` (R1) lists ANY existing files before Move 1 begins. Do not overwrite. Stop and flag the conflict.
- **A2** — any external CDN/framework reference (`<script src="https://cdn...">`, a Bootstrap/Tailwind class system, jQuery) appears anywhere in the output. Not a patch-and-continue — treat as an automatic stop, rebuild the offending piece plain, then resume.
- **A3** — the executor is about to fabricate a real-sounding instructor name, credential, studio address, or refund policy not present in the brief or `inputs/` (R3). Stop that specific block, substitute the tagged placeholder, and log the gap rather than inventing a fact.
- **A4** — horizontal overflow observed at 375/390/428px (Move 10) survives two counter-move attempts at the same breakpoint. Stop, flag the exact selector, do not keep guessing.
- **A5** — the Mailchimp URL appears to need modification (adding real-looking `u`/`id` params, guessing a real list ID) to "make the form work." Never guess real credentials for a marked-demo destination — R4's anchor-link fallback is the frozen answer; if that link itself won't render as a valid `<a href>`, stop and flag rather than substituting a fabricated working URL.

---

## 5. Verification Runs

| # | Run | Timing | Pass definition |
|---|---|---|---|
| V1 | File listing: `find site/ -type f` | After Move 1 | Exactly 3 files (`index.html`, `styles.css`, `script.js`); zero build-tooling files (`package.json`, config files) |
| V2 | Viewport emulation at 375, 390, 428px; check `scrollWidth <= clientWidth` | After Move 10, and re-run after any counter-move that touches CSS | True at all three widths, for the full page and every section individually |
| V3 | Section-id scan: grep for `#hero`, `#why-lindy-hop`, `#instructor-bios`, `#schedule-pricing`, `#faq`, `#reserve` | After Move 1 and again at final assembly | All 6 ids present exactly once each, in that document order |
| V4 | CTA-copy grep: every instance of the reserve CTA string and href | After Move 9 | 100% of CTA instances match the frozen string "Reserve a spot" and the frozen R4-resolved href, byte-for-byte |
| V5 | External-dependency scan: grep `<link` / `<script src` for `http` outside a same-origin path | After Move 9 | Zero results, except the single `<a href>` to the Mailchimp destination (a link, not a page dependency) |
| V6 | Placeholder-tag scan: grep `<!-- DEMO CONTENT` adjacent to every instructor bio, and adjacent to every FAQ answer touching address/refund policy | After Move 5 and Move 7 | A DEMO CONTENT (or DEMO CTA) tag sits directly beside every fabricated/placeholder fact — none presented as verified |
| V7 | Fact-string check: grep for "$120" and "Sept 2" / "September 2" verbatim; confirm no unexplained second price appears | After Move 6 | Both strings present exactly as given; no invented "regular price" contrast anywhere |
| V8 | FAQ accordion smoke test: toggle each item, check `aria-expanded` flips, check console for JS errors, re-check V2 immediately after toggling | After Move 7 and again after Move 10 | `aria-expanded` toggles true/false correctly, zero console errors, no overflow introduced by the open state |

Note on R4/A5: do not treat "the Mailchimp URL doesn't resolve" as a verification failure — it's explicitly marked demo and the pass condition for V4/V5 is string-match against the frozen href, never live network reachability of a placeholder domain.

---

## 6. Red-Team Log (survived contact)

**Attack 1 — broke an earlier draft of this wargame.** Before Move 5 carried an explicit counter-move and Move 10/A3 existed, the instructor-bios instruction was only "use placeholders, don't invent real names" as prose guidance with no machine-checkable trigger. Simulating the executor following that draft blind: nothing stops it from writing a plausible real-sounding name ("Sarah Chen — 8 years teaching experience") with no tag, because the instruction was a suggestion, not an observable check. **This attack succeeded** against the earlier draft. Patch: added Abort A3 (explicit stop condition) and Verification V6 (grep-based tag check) so the constraint is enforced by a runnable check, not executor discipline alone.

**Attack 2 — attempted against the current, patched draft; failed.** Argument: "the 8-week schedule is legitimately tabular data, so a real `<table>` element is the semantically correct choice — the no-horizontal-scroll rule shouldn't apply to a properly-marked-up table the same way it applies to a layout div." This attack tries to find an exemption the wargame doesn't grant. It fails here because Move 6 freezes the schedule as a card/list layout specifically to close that escape hatch, and V2's scroll check is unconditional across every section — there is no table-shaped carve-out anywhere in the document for the attack to exploit. The attack has nowhere to land.

---

## 7. Self-Grade (8-Point Standard)

| # | Point | Grade | Anchor named |
|---|---|---|---|
| 1 | Expected-observation specificity | Pass | Every move's Expect line is a yes/no check (file count, string match, scrollWidth comparison), not "should look good" |
| 2 | Failure causality (failure + cause + counter) | Pass | Move 2: "renders desktop-width at 375px → missing/malformed viewport meta → add exact tag" — matches the "overflow → missing flex-wrap → add flex-wrap" anchor shape |
| 3 | Fork determinism | Pass | Every RECON item and every Trigger is if-observe-X-then-route; A1's "if site/ lists ANY files, ABORT" is the exact anchor pattern |
| 4 | Recon groundedness | Pass | R1–R5, each with an exact command and both branches, resolved against the stated findings |
| 5 | Blind-executability | Pass | No move asks the executor to decide anything — every branch is observation-triggered |
| 6 | Honest blocking | Pass | R3 flags instructor names/credentials, studio address, and refund policy as BLOCKED pending real input; none invented |
| 7 | Survived contact | Pass | Section 6 — one attack that broke an earlier draft (instructor-name fabrication) plus the patch, one attack that failed against the current draft (table-exemption argument) |
| 8 | Anticipates executor's own mistakes | Pass | Move 5 explicitly predicts the aria-hidden inheritance from Move 3/4's decorative-icon pattern onto the instructor avatar — a mistake caused by this document's own earlier moves, not just the world |

All eight hold. Flagged as a self-grade pending an independent adversarial pass — the red-team log above is the drafting-time attack, not a substitute for a second reader attacking the finished document fresh.
