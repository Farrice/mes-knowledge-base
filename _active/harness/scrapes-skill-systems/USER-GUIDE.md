# Scrapes Skill Systems — User's Guide (LIVING; update in place)

*For Farrice. How to use the 36 Scrapes skills through this harness without piloting them by hand. One page. Written 2026-09-03.*

## The one door
Type `/scrapes` and paste what you have. A topic. A URL. A draft. A video link. "Set up my templates." It classifies the job, locks the brand, and runs the matching pipeline. You never need the skill names. The six specific doors still exist if you want to go straight in: `/social-carousel`, `/social-post`, `/social-repurpose`, `/deck-build`, `/video-to-shorts`, `/video-to-ebook`.

You can also just say it in plain words in any session ("make Jen a carousel about still renting"). The router suggests the door with a `[SCRAPES engine]` tag; you tap or type it.

## Run it again (the way blind bar 01 was made, plus the review beat it skipped)
1. **Bring a concept, not a package.** One line with the brand and the idea: `/social-carousel farrice: teardown of <brand>, LinkedIn`. Drop in anything you already have: reference carousels you like, product or context images, a brand to name or spare. You never have to arrive with the angle, the research, or the copy. The brand word is the lock; leave it out and the system asks.
2. **Concept Room (your first tap).** The run comes back with ONE short page: the research that matters (tagged, with real screenshots already captured), three angle candidates with the fight each one picks, two or three hooks for the recommended angle, the photo plan, and the named-vs-composite call. You tap, edit, or redirect. Nothing is written until you do.
3. **Read the ledger, not the slides.** `VERIFICATION.md` in the run folder lists every claim, its tag, its source, and the crop it rides on. One read, sign off on accuracy. Nothing off the ledger ships.
4. **Edit the take file.** Caption plus seven-slide script comes to you as text. Word-level edits happen there. Copy locks before any machinery runs.
5. **Slides render at $0** on your approved pool. You get a contact sheet, and a blind judging surface whenever there is more than one take. Tap the verdict in your words; it goes into the ratchet.
6. **Post by hand.** Sends stay human. The run folder is under `projects/00-social-content/<date>/<slug>/`.
Full recipe with the dead ends: `docs/solutions/2026-09-03-teardown-carousel-copy-lock-evidence-crops.md`.

## Who is it for? (the brand lock)
Only the Scrapes doors care. Extractions, research, Parallax, Jen listings, harness work: nothing changes, no setting, no default to worry about.

- Say the brand in the sentence: "for me", "my brand", "for Jen", "for Andrea". One name → it runs.
- No name → it asks one question, "which brand?", and waits. It never assumes you.
- Two names → same question.
- Working inside a client folder (`_active/clients/<client>/…`) and naming nobody → that client.
- A new client → one file, `_active/clients/<client>/brand_context/BRAND.yaml` (copy Jen's and edit). Until it exists the door refuses by name. That refusal is the safety, not a bug.

Check any time: `python3 execution/scrapes_brand.py list` · `check <brand> --pool linkedin-carousel`.

## What is yours, what is theirs (the seams)
Their machinery runs the parts we could not build: scenario detection, slide planning with real logos and audits, template rendering, image generation, the review studios, clip scoring, face-aware reframe, caption burn. Our pens write every word: for you, VOICE-CARD dial + Luke Iha on the hook; for a client, Alyssa placement + Luke grip, one integrator, the brand-as-itself veto. Our receipts own the facts (`research.py`, `claim_audit`), our classifier is the gate, our budget guard is the wallet. Their pipeline receives finished copy and does the visuals ("Scenario A"). You will see this as: copy first for your read, then images.

## Before your first carousel: the template pool (once per brand)
Their carousel pipeline refuses to run without an approved template pool. Setup is `/scrapes set up my templates for my brand`. It reads 4–6 reference frames from `brand_context/visual_refs/` (yours are staged), builds one template per ref with GPT Image (≈ $0.17 per image, month cap $15), then opens the Template Studio in your browser. You compare ref vs render, edit, click Approve. Approved templates render carousels at $0 from then on. Jen's pool waits on her six inputs; until then her visuals go through her own renderer.

## Leaving notes in a Studio (verified)
Top bar → **Comment** pill (toggle) → click the slide → type in the small composer → press its **Comment** button (Return does not submit) → **Save**. Notes land in `comments.json` next to that template or slide. Say "read my Studio comments" and they drive the next pass. Or just tell me in chat, as you did; both work.

## Approvals that stay yours
Template Studio (templates), Content Studio (the finished slides), the outline in a deck, the human-review step in an ebook, every paid call above the guard's line, and every send. Nothing posts. Ever.

## Cost
Templates and template-rendered slides: $0. AI slides: GPT Image ≈ $0.04–0.19 each, Gemini path $0. Research: Gemini Deep Research ceiling $10, Perplexity fallback. Every paid call is stated before it runs and logged after.

## When something refuses
- "BRAND AMBIGUOUS" → name the brand.
- "render path: blocked" → no template pool for that brand and format → run the pool setup.
- "NOT READY … tokens.json" → run `/scrapes visual identity for <brand>` (Import mode from the brand's DESIGN.md).
- Budget DENIED → the month's cap is spent; raising it is your decision only.

## Where things land
Your runs: `projects/00-social-content/<date>/<slug>/`. A client's runs: under their folder, `04-deliverables/social-content/`. Templates: `<brand_context>/templates/<pool>/`. Lessons every run leaves behind: `context/learnings.md` (read automatically at the start of the next run).

## Do not
Edit anything inside `.claude/skills/` (hash-gated; updates would strand you). Use `tool-publisher`, `tool-zernio-social`, or `tool-linkedin-scraper` (sends stay human; Apify retired). Skip the brand lock because "it's obviously mine".

## Deeper
`ORCHESTRATION-DESIGN.md` (how it is wired, what is verified vs inferred) · `PRECEDENCE-MAP.md` (which side wins per skill, blind bars pending your taps) · `INTEGRATION.md` (install, keys, update procedure) · `RESUME-BRIEF.md` (state + kickoff prompt).
- **The proven carousel run, start to finish** (blind bar 01, his verdict "11 out of 10... this needs to be the floor"): `docs/solutions/2026-09-03-teardown-carousel-copy-lock-evidence-crops.md`. Same order every time; the door `/social-carousel` carries it under "Proven run shape".
