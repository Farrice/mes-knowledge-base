# Source Notes — Nick St. Pierre extraction (2026-08-02)

Every claim in `SKILL.md`, `genius.md`, and the workflows traces to a source below.
**Each entry carries its date.** Anything dated 2023–early-2024 that describes tool behaviour is
era-bound and lives in `references/era-bound-mechanics.md`, never in the durable craft layer.

---

## Who he is (verified from primary sources, 2026-08-02)

- **Nick St. Pierre** — @nickfloats on X, 175.2K followers, bio "Unofficial Midjourney shill.
  Playing with AI & sharing learnings." NYC. (X profile, read 2026-08-02.)
- **Creative Director, Original Creative Agency (OCA)**; client list Meta, Google, Ogilvy,
  McKinney, Adobe, Nike, Oliver Wyman, Shopify. "Generated tens of thousands of images, tested
  hundreds of techniques, and shared research and learnings with over 200 million people
  globally." (Maven course page, instructor bio — read 2026-08-02, course listed as no longer
  available.)
- **Executive producer** on a live-action/AI film premiering at Cannes — directed by Dustin
  Yellin, starring Paul Rudd and Chris Rock, produced by Darren Aronofsky. (X, 2026-05-14.)
- **Instagram AI camera effects** — "My team and I created some AI effects that accidentally
  melted instas GPUs." (X, 2026-04-22.)
- **Educator** — Maven "Midjourney for Creatives" (4.7/5, 159 ratings; 55+ async lessons, 24
  projects, 5 deep-dive live lessons) and a 2024 live-stream community (~80 sessions, $679/yr).
  Cohort #6 ran Jan 2024. Free public workshops through Mar 2025.

**Third-party corroboration of the method (verbatim, Maven testimonials page):**
- Matt Bornstein, Partner at a16z: *"There is an art to generating compelling images in AI tools.
  Many people think it's necessary to devise super complicated, over-engineered workflows. Nick's
  talent is to see through this & develop simple, powerful, & flexible strategies that generate
  amazing results. Nick has deeper intuition around how to control AI image models than anyone
  else."*
- Tony Parisi (co-creator VRML/X3D/glTF): *"Nick perfectly blends craft and creativity with his
  Additive prompting approach, and it's totally changed the way I work with Midjourney."*

---

## Sources actually read (with dates)

### A. Podcast — durable philosophy, thin on craft
- **"Probably Something" podcast, YouTube `W5-spIWNxJo`, 20:11** (fetched via
  `claude-video/watch` transcript, 2026-08-02). Undated on the page; internal evidence puts it
  ~late 2023 (he references MJ v4 as "December of last year," first MJ prompt "July of last
  year"). **Craft content: near zero.** Value: doctrine and stance —
  - "authoring at the speed of thought" [04:02]
  - the 10x creative and tool-stacking [08:28]
  - "if you're just writing a prompt that generates an output… that image isn't your art… it's
    about intent and it's about process" [10:14–10:35]
  - "what I share what I post is research, it's experimentation, it is not art" [12:06]
  - previs/concepting to close deals without a shoot budget [07:13–07:40]
  - open-sourcing prompts on principle [17:33]

### B. The Additive Prompting series — X, Feb 2023 (ERA-BOUND MECHANICS, durable *order*)
Compilation thread: `x.com/nickfloats/status/1631346749297106958` (2023-03-02, 734.8K views).
His own caveat, verbatim: *"PSA: Additive Prompting is by no means the 'correct' way of
prompting. It's a framework I developed to better understand the impact & interplay of variables
in my prompts on the overall composition of my images."*

| Guide | Date | Status ID | What it gives |
|---|---|---|---|
| Film types | 2023-02-04 | 1621974596093198336 | The control-prompt sweep method; base template `[Shot Type] photo of [Subject], shot on [Film Type]`; 8 film stocks with real-world descriptions |
| Lighting styles | 2023-02-05 | 1622218650517209089 | 8 lighting styles + combination lighting; same control prompt, one added slot |
| Shot types & camera position | 2023-02-06 | 1622729804402360322 | Compensating-token rules (medium shot needs body language; low/high angle needs from below/above; wide shot needs background context); emotion specificity |
| Fashion, color, textiles | 2023-02-07 | 1623211054317637632 | Lock-the-winner behaviour; designer/color/material sweep; seed discipline |
| Atmosphere & ambiance | 2023-02-10 | 1624156336874262530 | "Combo Commands" (his term); particle-size distinctions (misty vs steamy); 3 lighting approaches |
| Consistent characters | 2023-02-18 | 1627157305040027648 | Image-as-substrate character lock; casting language; distinct faces lock better |
| Set design & interiors | 2023-02-23 | 1628796348446253057 | The 1.3M-view slot schema and its ordering rules; "90%+ coherence" claim |
| Cinematics / image blending | 2023-02-26 | 1630016039755890689 | Character prompt + interior prompt = cinematic shot; "aspect ratio and lighting are the true drivers of cinematic looks" |

**Read them as ALT text.** He publishes exact prompts in image alt attributes ("Prompts in ALT if
you wanna test this out yourself") — that is where the verbatim specimens in this extraction come
from.

### C. The v6 era — X, Dec 2023–Mar 2024 (mostly durable, some era-bound)
- **`1741166489364025536` (2023-12-30, 987.8K views)** — "A guide to prompting --v 6." The
  four-step build (set the main scene → describe the details → describe the setting → explore
  styles & mediums), the troubleshooting list, and the two anti-patterns (style buzzwords;
  comma-separated keyword salad). **This is where he supersedes his own 2023 comma syntax.**
- **`1751731261872460198` (2024-01-28)** — 11 curated film-stock ↔ lighting-condition pairings,
  each with the full prompt. Durable photographic vocabulary.
- **`1752505154329251885` (2024-01-30)** — contrast doctrine + one fully-worked exemplar prompt.
- **`1749260418873163836` (2024-01-21)** — the basic-idea upgrade, before/after.
- **`1763371638395895953` (2024-02-29)** — X Article, "12 Midjourney Help Guides & Prompting
  Resources," with his own framing paragraph for each of the 12. Read in full.
- **`1770844219873075675` (2024-03-21)** — *"Text prompts really only need 3 things: {medium}
  {subject} {environment}"* + the expansion template + *"I don't use artist names in my prompts.
  Never have."* The hinge from text-heavy to reference-driven direction.

### D. 2025–2026 — the current layer (weighted heaviest per doctrine correction)
- **`1996694378476081267` (2025-12-04)** — "Text-first prompting is a terrible UX." Read in full;
  quoted at length in `genius.md`. The strongest statement of his current doctrine.
- **`1991531506397741156` (2025-11-20)** — a Nano Banana Pro prompt in his spine, on a
  non-Midjourney model. Proof the construction grammar is model-transferable.
- **`1937244488902053907` (2025-06-23)** — directing a sequence of six prompts across video
  extensions; **`1937957412373217473` (2025-06-25)** — "everything in this video was generated
  from a single frame, directing the character into different scenes over time with extensions."
- **`1939773992614682807` (2025-06-30)** — his own MJ parameter guide: *"This is where a lot of
  the MJ magic lives, and how you can start to really tune aesthetics and styles to your exact
  preferences."* (Era-bound content, durable intent.)
- **`1912220087232168092` (2025-04-15, pinned)** — v7 blending, "the idea of impressionism
  captured through a rain soaked windows" — concept-led blending.
- **X, 2026-01-29** — *"The delta between the AI content you typically see on X and what a true
  storyteller like Darren Aronofsky manages to produce with the same tools is truly insane."*
- **X, 2026-02-20** — on a v8-vs-Nano-Banana comparison: *"this is also a base model comparison,
  no style references, parameters, moodboards, etc, which all provide additional aesthetic
  control."*
- **X, 2026-02-14** — endorsing Paul Graham on taste: *"Maybe you nerds will listen now that Paul
  has said it."*
- **X, 2026-01-28** — *"We invented one of the most beautiful and expressive creative mediums to
  ever exist and you're using it to automate UGC campaigns with fake influencers on tiktok."*
- **X, 2026-06-25 (repost, Midjourney)** — big-batch draft mode with `--sref random`, "explore
  style space 24x faster." Sweep discipline, industrialised.

---

## Fidelity flags

1. **No 2025–2026 systematic teaching corpus exists.** His Articles tab ends 2024-03-14; the
   dense, step-by-step method threads are Feb 2023 – Mar 2024. 2025–2026 output is professional
   practice (Cannes EP credit, Instagram effects), model commentary, and doctrine — not
   tutorials. **Consequence:** the durable craft layer here is reconstructed from 2023–2024
   method threads and *validated* against his 2025–2026 statements and prompts, rather than being
   restated by him recently. Where a 2025–2026 statement confirms a 2023–2024 move, it is cited
   next to it.
2. **His method visibly evolved and partly contradicts itself.** The 2023 Additive Prompting
   syntax is comma-separated keyword slots. By 2023-12-30 he lists "prompts that are just
   comma-separated keywords" under *things to avoid*. The durable invariant is the **order of
   decisions and the sweep discipline**, not the punctuation. This extraction teaches the
   invariant and dates the syntax.
3. **Two claims are his, unverified by us:** "90%+ coherence to the prompt" for the interiors
   schema (2023-02-23) and "hundreds of tests" behind the character method (2023-02-18). Reported
   as his claims, not as house facts.
4. **DuckDuckGo search for 2025–2026 interviews/podcasts returned nothing usable** (run
   2026-08-02). WebFetch on x.com returns HTTP 402; all nitter/xcancel mirrors were bot-walled.
   **Everything from X in this extraction was read via Playwright on x.com directly** — the only
   route that worked.
5. **The Maven curriculum page is a marketing page, not a syllabus.** It gives module *themes*
   (remixing, parameters, image blending, style references, consistent characters, variations,
   inpainting, outpainting, multi-prompting, negative prompting, permutations, weights, seeds)
   and the course shape, not lesson content. Course now shows as unavailable. Treated as
   corroboration of scope, not as method.
6. **No video of him teaching was watched** (founding-failures rule: transcript-only caps
   confidence). The one podcast we have is audio-transcript only and is nearly craft-free. Craft
   confidence rests on his written threads, which carry verbatim prompts and side-by-side results
   — a stronger evidence class than a talking-head transcript, but not the same as watching him
   work.
7. **House conflict worth surfacing, not burying:** St. Pierre ran a sustained public campaign
   against Higgsfield in Feb 2026 (2026-02-03 through 2026-02-05: *"the most morally bankrupt and
   anti-creative tool in existence,"* allegations of a multi-level influencer scam, calls for
   model providers to cut API access). The house creative router currently routes photoreal
   people to Higgsfield Soul. This extraction takes no position on the allegations; it flags that
   loading St. Pierre and routing to Higgsfield in the same session is a values collision Farrice
   should decide on knowingly.
8. **Not extracted here (deliberately):** Midjourney business/company commentary, his AI-industry
   commentary, and the Higgsfield dispute. None of it is image-direction craft.
