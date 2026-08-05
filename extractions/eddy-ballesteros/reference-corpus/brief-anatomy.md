# Eddy Ballesteros — Creator Brief Anatomy (verbatim frame teardown)

**Source**: "I Connected Claude to Monid AI. Now It Does My Research in 10 Minutes." (PmvqIaLC6AY, 2026-08-04, 14:43)
**Method**: watched via /watch — 37 scene-aware frames + full captions. Every observation below cites a frame timestamp. Inferred items are labeled INFERRED.

## What the artifact actually is

Two distinct HTML surfaces appear on screen, both Claude-generated with HIS personal design system ("my Claude design system that I built", t=05:13):

1. **The Creator Brief** (t=00:33–01:25) — daily/periodic niche-research brief, local file rendered in browser.
2. **The Research Report** (t=07:52–08:32) — on-demand topic deep-dive (AI SEO example), rendered as a claude.ai HTML artifact, downloadable.

He also renders his own **video scripts** as styled HTML docs (t=00:15, 01:52 — `monrod-video-script.html` with pull-quote callouts) — the design system is a whole personal document layer, not a one-off.

## Structural anatomy (section order, observed)

### Creator Brief (frames t=00:33, 01:25)
1. **Sticky pill-tab nav** by topic — `TL;DR · COHERE · CHATGPT WORK · MCP + CREATIVE · PEOPLE · VIDEO IDEAS` + a numbered "04" active state (t=01:25). Brief is navigable by subject lane, not a scroll blob.
2. **Cover block** (t=00:33): small outline chip `CREATOR BRIEF · X + WEB` → giant lowercase headline ("what's new in claude cowork & chatgpt *work*" — last word italic serif) → 2-line dek in quiet gray ("...pulled from x via monid, checked against anthropic and openai. built to turn into videos.") → **metadata row of 4 mono-label columns**: `WINDOW last 30 days · LENS marketing · creative · mcp · SOURCES ~120 posts + press · COMPILED jul 31, 2026`.
3. **Numbered sections**: italic serif number + lowercase bold heading (`01 the big picture`, `04 mcp + creative plays`) with optional right-aligned tag chip (`THE CONNECTIVE LAYER`).
4. **Kicker + summary panel** (t=01:25): mono caps kicker `WHAT'S FORMING` above a rounded soft panel holding a 3–4 line synthesis paragraph.
5. **Checklist evidence rows** (t=01:25): blue check square + **bold lowercase claim title** + 1–2 line dense description + tiny mono source id/handle underneath. Four rows visible: "beehiiv + zapier mcp + cowork = content engine" / "'stanley,' a purpose-built ai head of content" / "22 claude code skills grouped by job" / "a faceless-youtube folder system". Every row is *actionable and attributed*.

### Research Report (frames t=07:52–08:32)
6. **Dark inverted decision section** (t=07:52): kicker `THE OPENING` → huge headline "where the lane actually *is*." → dek "the topic is crowded at the top and thin in the middle. here is what the data supports doing, in order." → ranked checklist: `go after aeo, not ai seo` / `lead with claude, not with seo` / `build the audit, don't explain the concept` / `speak to the solo operator` / `skip llms.txt` — each with a dense evidence sentence citing the actual numbers (difficulty 74 vs 65, channel-size data). **Recommendations get maximum visual contrast** — the only dark section in a light document.
7. **Caveats section** (t=08:13–08:18): kicker `CAVEATS WORTH KEEPING` → headline "what this *isn't*." → epistemic paragraph ranking data reliability: "semrush volumes are a monthly estimate, not a count… the trend shapes and the community sizes are the most reliable things here. the conversion percentages and revenue claims are the least. build on the first, quote the second carefully or not at all." → single CTA button `OKAY, SO MAKE THE VIDEO`.
8. **Small-multiple charts** (t=08:32): per-keyword 12-month bar charts (ai seo / answer engine optimization / generative engine optimization), caption "same scale, very different shapes" — comparison honesty enforced by shared scale.
9. **Footer**: mono handle `@EDDYBALLZ` + page number, every page.

### Script docs (t=01:52, 02:02)
10. **Pull-quote callout**: full-width black rounded bar, italic serif white text ("the tool is called monid. it's not another chatbot…"). Closing aphorism same treatment (t=13:54): "it's not that claude got smarter. it's that you finally gave it hands."
11. **Step cards** (t=13:54 doc, "connect it in *two* minutes"): 4 numbered cards, mono `STEP 1..4` kickers, active step tinted blue.

## Design-language tells (his skin — treat as anti-reference, we restyle)
- Cream/paper background, near-black ink, **single blue accent** used for checks, links, italic accent words, active states.
- Modern grotesk body/headlines (Inter/Neue-Haas class), **italic serif as the accent voice** (one word per headline), mono caps for all labels/metadata.
- All-lowercase headline styling; generous whitespace; content column ~700px; zero decorative imagery — data and typography only.

## The moves worth stealing (function, not skin)
1. **Metadata row = trust header** — WINDOW/LENS/SOURCES/COMPILED answers "how fresh, through what filter, from how much data" before a single claim.
2. **Claim-first checklist rows** — every insight is a bold verdict with evidence sentence + source id. Scannable in 5 seconds, verifiable in one click.
3. **Decision layer gets the ink** — recommendations live in the sole dark section, ranked "in order." The brief tells you what to DO, not just what's happening.
4. **Built-in epistemics** — a whole section ranking which of its own numbers to trust. This is Farrice's VERIFIED/LIKELY/UNCONFIRMED standard, expressed editorially.
5. **Same-scale small multiples** — comparison charts share one scale so shape differences are real.
6. **One CTA per document** — the brief ends in a single action button, not a menu.
7. **Topic-lane tabs** — periodic briefs are navigable by lane (tools/people/ideas), making them a daily surface rather than a report to file.

## His workflow (observed end-to-end)
1. Prompt (verbatim, t=04:54–05:19, claude.ai + project context "cowork creator.md", Opus 5 Medium): *"Using monid AI, I want you to research this topic for me in depth. I want you to identify the tools we can use to conduct this research, such as Reddit, subreddits, X web search, and any social media platforms that make sense, like Instagram. And then I want you to turn that into a really good report using my Claude design system. The topic that we're going to research is AI SEO."*
2. Claude discovers Monid tools → pulls **Semrush keyword metrics, Reddit top posts + community sizes (time-windowed), X posts, YouTube last-30-days** (t=06:09–06:24). Cost: **$0.03** (t=06:04).
3. Report → conversational follow-ups on the report → **second artifact**: "Cited in 30 Days" challenge with 30 video ideas in 3 arcs (baseline-and-stakes / building-systems / money-proof-payoff), grounded in HIS channel's proven titles + anchor terms, with caveats (t=09:50–12:14).
4. Push to planner via other MCPs (Notion/Asana) — "not everything has to be stuck within Claude" (t=12:23).
