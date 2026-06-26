---
description: "/orlean-research-to-story — turn a deep-research dump, knowledge base, or report into narrative nonfiction that reads like fiction. Atomize the corpus into cards, cluster into themes (the structure layer), confirm the iceberg over-research, then lift the assemblage into a yarn with connective tissue — facts transformed into a story told across a dinner table, never a bullet-point information dump. The cross-domain pipeline that conducts orlean-card-structure → orlean-yarn-engine behind the three-phase walls."
---

# Research to Story — Turn a Deep-Research Dump Into Narrative Nonfiction (Susan Orlean)

Most research-to-content pipelines end where Orlean's *begins*. They gather the facts, then dump them — a report, a bulleted brief, a "here's everything we found" knowledge base. Orlean has a name for that output: "I'm just going to read you bullet points of information. That's a snoozefest." The chasm between a good researcher and a writer is one move — *the lift* — and almost nobody crosses it, because the lift can't happen until two prior walls are respected: the research has to be *done* (the iceberg, over-reported off the page so the visible tip floats), and the structure has to be decided *physically, before the prose* (the cards clustered into themes). This workflow is the whole pipeline that takes you from a corpus to a told story without skipping either wall. It does not gather new facts (deep-research / knowledge-alchemy own the iceberg) and it does not invent the spine inside the draft (the card layer owns that). It conducts two sub-engines in sequence — **orlean-card-structure** to build the movable, theme-clustered spine, then **orlean-yarn-engine** to lift the assemblage into a yarn with connective tissue — so what walks out is narrative nonfiction a skeptic stays at the dinner table for, not a fact sheet with paragraphs. The honesty spine runs the length of it: **the lift dramatizes true facts; it never invents a detail to make the yarn flow.**

## Pre-Flight

Read before executing — load these `genius.md` sections (do not paraphrase from memory; the method is precise, three-phase, and dies the instant it is run mechanically or collapsed into one undifferentiated "process the research" step):

- **Pattern 5 — The Three Separated Phases** — the walls this entire pipeline enforces: research, then digestion, then writing, never blended. This workflow assumes Phase 1 (research) is *complete* — it runs Phase 2 (the card layer) and Phase 3 (the lift). "I can't write yet. I don't know what I'm writing about" is the failure this prevents.
- **Pattern 6 — The Index-Card Architecture** — the structure layer (Step 2 of this pipeline; the full engine is orlean-card-structure): atomize the corpus into chunks-of-thought, physically move them until "the themes began having within them the story I was going to tell."
- **Pattern 7 — Connective Tissue** — the half everyone skips: a theme-cluster is not yet a story ("you can't just do, here's a story about arson, here's a story about this guy"); the craft is the seams. Mapped in the structure layer, drafted in the lift.
- **Pattern 8 — The Yarn, Not the Bullet Points** — the lift (the back half of this pipeline; the full engine is orlean-yarn-engine): spin mood, foreground characters, convey significance subtly, "the parts that then lead to the sum, but the sum is so much bigger than the parts."
- **Hidden Knowledge — The Iceberg Ratio** — the gate before drafting: "you're not going to go, boy, I bet that was eight weeks of research." The reader sees the tip; most of the corpus stays submerged. Confidence on the page comes from over-research off it — and the corollary, "every time I'm stuck, I just haven't reported enough."
- **Susan Orlean Would Never... (Anti-Patterns)** — especially **AN-4 (Drafting Before You Know What It's About)**, **AN-3 (Bullet-Point Information / the snoozefest)** — the exact two failures a research-to-story pipeline produces when run wrong — plus **AN-1 (Overwriting to impress)** and **AN-2 (Adjective/example stacking)**, the failure modes of the lift step.

> **🔒 Pre-Flight Gate**: run the **Decision Framework** in `genius.md § Decision Framework` before processing a single source. This pipeline is the one most tempting to start in the wrong place, so confirm in order:
> - **Q5 — is the research actually done?** This pipeline turns a *finished* corpus into a story. If the corpus is thin, or half the would-be cards are "??? need to find this," you are still in Phase 1 — stop and report more. The card layer organizes a story you already understand; it does not invent one (AN-4). The Iceberg Ratio is the test: is there far more under the corpus than will ever surface in the draft? If the corpus *is* the whole iceberg with no submerged mass, the tip will not float — over-research first.
> - **Q1/Q2/Q3 — is there a telling subject and theme in this corpus, and does it pass the prism test?** A research dump is raw material, not yet a subject. Before lifting, name the small specific thing the corpus carries and the universal underneath it. If the corpus is genuinely just an information set with no story in it (a price comparison, a spec table), this is the wrong workflow — it may want a clean report, not a yarn. Be honest: do not force a narrative onto material that has none.
> - **Q4 — proxy or superior?** You are about to retell what the research found. The stance is "I didn't think I needed to know this either, and then —," never "here is what the research shows." The former seduces a reader into a topic they didn't choose; the latter is the report you're trying to escape.
> - **Q6/Q7 — structure before prose, and pulling punches?** The spine gets decided in the card layer before a sentence is drafted; the prose stays plain and confident with reserved hits, not reaching to impress. If you find yourself drafting to "figure out the shape," you've collapsed the walls — go back to the cards.

## Input Required

- **The research corpus** — the actual deep-research output, knowledge base, report, brief, or document set. The *whole thing*, not a summary — we atomize the real material into cards, so we need the real particulars (the dates, the quotes, the anecdotes, the data, the source attributions), not an abstract of them. If it lives across multiple files or a database, point to where each piece lives (Orlean's cards were often pointers: "card 35: legal document → go fish it").
- **The source provenance** — where each fact came from, and its confidence label (VERIFIED / LIKELY / UNCONFIRMED, per the verification protocol). This rides *with* each fact through the whole pipeline so the lift never accidentally dramatizes an unconfirmed claim into a confident scene. The honesty spine depends on this travelling end-to-end.
- **The telling subject + theme (or the mandate to find it)** — the small specific thing the corpus is really about and the universal it carries. If you have it (from `orlean-telling-subject`), name it. If not, finding it is Step 1 — you cannot cluster a corpus into *story* themes without knowing what the story is about.
- **The format & scale** — narrative feature / longform essay / Substack edition / book chapter / brand story / report-turned-narrative / newsletter / series. Drives the card count, the number of themes, lead length, and how much the lift can afford to slow down.
- **The reader's starting heat** — what does the reader currently feel about this subject? (Usually, for research-driven pieces: indifference or "just give me the findings.") This calibrates how hard the lead and the proxy stance have to work to make a research subject feel like a story worth an hour.

## Workflow

The pipeline runs in three movements that map exactly to Orlean's three phases. Movement A (Steps 1–2) confirms the research wall is respected and finds the story inside the corpus. Movement B (Step 3) is the structure layer — it hands off to **orlean-card-structure**. Movement C (Steps 4–5) is the lift — it hands off to **orlean-yarn-engine**. Do not blend them. The walls between them are the method.

### Step 1 — Confirm the iceberg, then find the story inside the corpus (Phase 1 wall + telling-subject)

Before anything else, audit the corpus against the **Iceberg Ratio**. A research dump is not automatically a finished iceberg — it is often *the tip with no mass underneath*, which is exactly the corpus that produces a thin, brittle draft. Run the test:

| Iceberg check | What you're looking for | If it fails |
|---|---|---|
| **Depth ratio** | Is there far more *here* than could ever surface in the draft — multiple confirming sources per claim, texture you'll never use? | The corpus is too shallow. The visible tip won't float. Report more (Q5) before proceeding. |
| **The submergeable majority** | Can you name which 70–90% of the corpus will *stay off the page* — present only as the confidence under the visible facts? | If everything in the corpus "has to go in," you're writing a report, not a story. The lift requires the courage to submerge most of it. |
| **The stuck-test** | Is there any beat where you feel you'd have to *invent* a detail to make it vivid? | "Every time I'm stuck, I just haven't reported enough." That gap is a reporting hole, not a writing problem — and filling it with invention breaks the honesty spine. Report it or cut the beat. |

Only once the iceberg holds: find the **telling subject** inside the corpus. A research dump rarely arrives with its story labeled — it arrives as facts about a topic. Your job is to locate the small specific thing in the material that carries a universal (run `orlean-telling-subject` if you have not). Write it down:

```
TELLING SUBJECT (the small specific thing the corpus is really about): __________
SECRET THEME (the universal it carries — for the build file, NEVER the prose): __________
PRISM CHECK (4–6 facets the corpus opens onto, all one story): __________
```

If you cannot name a telling subject in the corpus — if it is genuinely just an information set — stop. Either the research needs reframing around a story, or this material wants a clean report and not a yarn. Do not staple a narrative onto facts that have none; that is the inauthenticity stench in pipeline form.

### Step 2 — Set the reader's starting heat and lock the proxy stance (Phase 2 entry, the demand audit)

Research-driven subjects run cold — the reader, if they wanted the findings, would read the report. So name the gap before you build the spine, because the colder the room, the more the structure has to front-load its most seductive material.

Write one line: *"The reader walks in __________ (heat — usually indifferent or 'just give me the data'), and by the end I need them to __________ (amazed they cared this much about it)."*

Then lock the stance for the whole pipeline. This is the single most important inversion in turning research into story: **you are not the researcher delivering findings; you are the proxy who didn't expect to care either.** Orlean doesn't even like Florida — she got fascinated, and now turns back over her shoulder: *keep coming, you're not going to believe what I found.* Install that register now so it governs both the structure (which beats lead) and the lift (the voice).

| Researcher register (kills the story — it's the report) | Proxy register (makes the corpus a yarn) |
|---|---|
| "The research found that…" / "Our analysis shows…" | "I went in thinking this was a dry subject. Then I found —" |
| "Key finding number three…" | "Here's the part I couldn't stop turning over —" |
| "According to the data…" | "What got me was a single number, buried on page forty —" |

The provenance still travels with every fact (it must, for the honesty spine and the verification gate) — but it travels in the *build file*, not as the prose's voice. The reader feels accompanied by a fascinated guide, not briefed by an analyst.

### Step 3 — Run the structure layer: atomize → cluster → sequence → map tissue (hand off to orlean-card-structure)

This is the heart of the pipeline and its non-negotiable middle wall: **the spine gets decided physically, before the prose.** Hand the corpus to `orlean-card-structure` and run its full method. The cross-domain adaptation for a *research corpus* specifically (versus original reporting) is in the table below — the engine is identical, but a research dump has properties you must handle deliberately.

| Card-layer step (orlean-card-structure) | What it does | Research-corpus-specific handling |
|---|---|---|
| **Atomize into chunks-of-thought** | Break the corpus into movable cards, each a single moment/idea/fact, tagged Type + Time-stamp | A research dump is already in *findings* form — resist transcribing findings 1:1 onto cards. Re-atomize into *story* units: a stat becomes a scene-able moment, a section becomes its constituent beats. Carry each card's **provenance + confidence label** as a fourth field. |
| **Cluster into themes** | Physically move cards until the strands of the story emerge (not pre-labeled topic bins) | The corpus's *report structure* (its headings, its sections) is almost never the *story* structure. Deliberately ignore the original outline and let the cards re-group by story-strand. The report said "Market, Technology, Risks"; the story might cluster as "the person who saw it first, the thing nobody believed, the cost." |
| **Sequence the spine** | Decide macro-order (theme order) and micro-order (cards within), chronological or not | Reports are logically ordered; stories are *seductively* ordered. Sequence so a person leads (proxy stance), so scene and fact alternate (no all-fact stretches = no snoozefest), and so the most jarring true particular sits where the lead will mine it. |
| **Map the connective tissue** | At every theme-to-theme seam and time-jump, name the hinge *now*, as a card note | This is where a research-to-story pipeline most often fails — the strands stay as discrete "findings sections" with no bridges, and the output reads as a report with prettier sentences. For each seam, name the shared image / recurring person / thematic echo that lets the reader turn the corner without feeling the joint. A seam whose honest hinge is "nothing, I just need to get from the market data to the founder story" is **not built** — find the hinge before drafting. |

The output of Step 3 is the artifact the rest of the pipeline depends on: a theme-clustered, sequenced spine with the seams mapped, decided in a layer where rearranging cost nothing. **Lock it.** From here, the spine governs order; drafting only fills it in. (Full method, granularity tests, chronological-vs-not decision, and the regrounding mechanic for non-chronological structure: `orlean-card-structure`.)

> **The "don't re-architect in the prose" rule (AN-4 guard):** if, during the lift, a card genuinely needs to move, move it *on the board first*, re-check its seams, then write. Never let the drafting silently re-decide what the cards decided — that is the slide back into discovering-the-story-while-writing, the exact failure the three-phase walls exist to prevent.

### Step 4 — Run the lift: transform the assemblage into a yarn (hand off to orlean-yarn-engine)

Now, and only now — research done, spine locked — cross the chasm a researcher never crosses. Hand the structured corpus to `orlean-yarn-engine` and lift it. The full engine builds the wait-what lead, plants the proxy stance, spins mood by selection, foregrounds characters, lets significance vibrate, and calibrates the pull-then-hit rhythm. The research-corpus-specific lifts — the moves that turn *findings* into *telling* — are these:

- **The lead is mined from the corpus's most jarring TRUE particular, not its headline finding.** A report leads with its conclusion; a yarn leads with the one detail that triggers "wait, what." Comb the corpus for the person rendered through a contradiction, or the specific that defies expectation, and lead on *that* — never on "the research reveals." (The Library Book doesn't open on "400,000 books burned"; it opens on the morning and the smell.)
- **Fact-clusters ride on the people the corpus contains.** For each thematic cluster, name *whose story carries it* — the source, the subject, the person the data is *about*. Facts delivered raw are the report; facts arriving through a person in action are the yarn. Where the corpus has only data and no human, find the human-adjacent (the analyst who found it, the person it happened to, the one who cared first).
- **Submerge the iceberg — most of the corpus stays off the page.** This is the move researchers resist hardest: the eight weeks of arson investigation become a paragraph. Lifting is *selection*, not inclusion. The submerged 70–90% is not wasted — it is the confidence that makes the visible tip float. A draft that tries to surface the whole corpus is a report wearing narrative clothes.
- **The significance vibrates; the findings are never stated as a thesis.** The corpus's "key takeaway" must become the *sum the reader assembles*, never a sentence that says "what this research teaches us is —." If the meaning only survives because you stated it, you stapled the moral on; cut it and choose particulars that make the reader feel it.
- **Plain prose with reserved hits — the data points that matter most are the hits, surrounded by quiet.** One devastating true number, placed inside calm narration, lands harder than ten findings in a row. Identify the 2–4 hits the whole telling is built toward; pull the punches everywhere else so they land.

(Full lift method, the lead candidates, the mood/character/significance discipline, and the rhythm calibration: `orlean-yarn-engine`.)

> **The honesty-spine seam (the load-bearing rule of this whole pipeline):** the lift dramatizes *true* facts — it makes a real detail seduce harder — but it never invents a detail to make the yarn flow. When a beat feels thin and the temptation is to add a vivid invented particular, that is the **stuck-test** from Step 1 firing: it is a reporting hole, not a writing license. Report the real detail or cut the beat. Every dramatized particular must trace back to a VERIFIED-or-LIKELY card in the corpus, with its provenance intact. A confident scene built on an UNCONFIRMED fact is the most dangerous failure mode here, because the better the telling, the more convincing the unverified claim.

### Step 5 — Read aloud, cut the crutches, run the dinner-table and fact-trace checks (the final pass)

The pipeline isn't finished until the draft survives two simultaneous tests — the *aloud* test (is it a story?) and the *trace* test (is it true?).

- **Read the whole draft aloud, cold.** Mark every place you get bored, stumble, or hear repetition. Boring-aloud is the verdict — those stretches are still *informing*, not *telling*; lift them or cut them. Hunt the habitual "would," the padding, the extra adjective (Pattern 12). The yarn must hold across the full dinner-table hour for a reader who didn't think they'd care.
- **Run the dinner-table test.** Imagine reading this to one skeptic across a table who came in wanting "just the findings." Do they stay for the hour? Where would they politely check their phone? Those spots are the seams that didn't get a hinge, or the beats that stayed bullet-points.
- **Run the fact-trace pass (the honesty gate).** Walk every vivid, dramatized particular in the draft back to its card and its provenance. Confirm: each is VERIFIED or LIKELY; none was invented to make the prose flow; no UNCONFIRMED fact has been promoted into a confident scene. This is the verification protocol applied to narrative — and it is where a research-to-story pipeline either keeps its integrity or quietly forfeits it.

If a beat fails *both* — boring aloud *and* untraceable — it was invented filler; cut it without mourning. If it's true but boring, lift it. If it's vivid but untraceable, that's the spine-breaking failure; report the real detail or cut the beat.

## Content Type Adaptations

| Format | Adaptation |
|---|---|
| **Social media** (LinkedIn / X / Substack note) | The corpus collapses to its single most jarring true particular — the lead *is* almost the whole budget. Open on the wait-what detail mined from the research, proxy stance in line one ("I went down a research rabbit hole I didn't expect to care about"), one character, one hit, the significance vibrating in a single closing beat. The card layer shrinks to a mini-spread (8–15 cards, 1–2 strands). Never post the findings list; post the one detail that makes someone stop. |
| **Marketing / brand story** | The "corpus" is the brand's proof, origin research, and operational findings. Find the small overlooked detail in it that opens onto the company's whole worldview (the prism), cluster the proof into the 2–4 strands the brand story braids, and lift it through a person — founder, maker, customer. The connective tissue is what stops it reading as a feature list. Honesty spine is strict here: every dramatized particular must be a real, substantiated fact; the lift makes a *true* claim seduce, it never manufactures one (that's copy-engine / luke-iha's claim-and-proof job, not the yarn's). |
| **Copy** (VSL / landing / email) | A research-backed offer's corpus (studies, mechanism evidence, results data) becomes a yarn: the wait-what lead does the work for a low-demand offer, the proxy stance ("I was skeptical of this research too, and then —") earns the read, and the proof rides through a character's story rather than a benefit-bullet list. Plain copy with reserved hits — one vivid true data point inside calm prose beats five. The pipeline supplies the *telling* layer over claims that copy-engine has already substantiated; the device layer (Ward) and the proof layer (Luke Iha) sit outside it. |
| **Ghostwriting** | The corpus is the client's research, interviews, and lived material. Cluster into *their* themes, lift through *their* characters, and write them as the slightly-ahead proxy — "I learned this the hard way too" — never the lecturing expert. Read the client's voice aloud to catch what's false or borrowed. Only build the yarn around findings the client is genuinely burning to share; audiences smell borrowed enthusiasm (the inauthenticity stench), and a ghostwritten research-recap with no felt curiosity is the deadest form of the snoozefest. |
| **Content** (feature / longform essay / series / newsletter) | The full pipeline, native habitat. A deep-research output becomes a narrative feature or a multi-part series: the card layer clusters the corpus into the strands, the connective tissue makes a series read as one show (stacks with `content-series` / `hawley-content-season`), and the lift carries the proxy stance across installments. The series-level significance vibrates across the run, surfacing only quietly, only late. Lead each installment on its own wait-what mined from the corpus; never let an episode become a findings recap. |

## Output Format

Deliver exactly this:

```
CORPUS: __________ (deep-research output / knowledge base / report / brief)   ·   FORMAT: __________
TELLING SUBJECT (the small specific thing the corpus is really about): __________
SECRET THEME (build file only, NEVER the prose): __________
READER WALKS IN: __________ (heat)  →  WALKS OUT: __________ (felt destination)

— MOVEMENT A · RESEARCH WALL + STORY-FINDING (Phase 1 confirmed, Phase 2 entry) —
ICEBERG CHECK: depth ratio holds · submergeable majority named · no stuck-test invention needed [confirmed]
PRISM (4–6 facets, all one story): __________
PROXY STANCE LOCKED: a fascinated guide, not an analyst [confirmed]

— MOVEMENT B · STRUCTURE LAYER (orlean-card-structure — decided before prose) —
THE DECK: ___ cards   ·   Type balance: __ scenes · __ anecdotes · __ facts · __ character · __ pointers
PROVENANCE CARRIED: every card tagged source + confidence (VERIFIED/LIKELY/UNCONFIRMED) [confirmed]
THEME CLUSTERS (emerged from moving cards — NOT the report's original sections):
  THEME 1: "__________"  — story-within: __________
  THEME 2: "__________"  — story-within: __________
  THEME 3: "__________"  — story-within: __________
SPINE: macro-order 1 → 2 → 3 …  (architecture: braid / nested / dominant-spine · chronological / not)
CONNECTIVE TISSUE: every theme-to-theme seam has a named hinge [confirmed — no "nothing, just need to get there"]

— MOVEMENT C · THE LIFT (orlean-yarn-engine — the assemblage becomes a yarn) —
THE LEAD (wait-what, one TRUE particular mined from the corpus, does all the work):
  "[the chosen lead]"   ·   true jarring detail: __________   ·   provenance: __________
THE TELLING (the full narrative draft):
  [lead → proxy-stanced narration → facts riding on foregrounded characters →
   mood by single concrete details → significance vibrating underneath →
   passive-stretch / earned-hit / return rhythm. Most of the corpus stays submerged.]
THE HITS (2–4, each surrounded by quiet, each a true data point or moment):
  1. "__________"
  2. "__________"
THE SUM (what the reader assembles — and you never stated): __________

— FINAL PASS —
READ-ALOUD: read cold, no boring stretches, "would"/crutches cut [confirmed]
DINNER-TABLE: a "just give me the findings" skeptic stays for the hour [confirmed]
FACT-TRACE (HONESTY GATE): every dramatized particular traces to a VERIFIED/LIKELY card;
  nothing invented to make the prose flow; no UNCONFIRMED fact promoted to a confident scene [confirmed]
ICEBERG: ~__% of the corpus deliberately submerged (off the page) [confirmed]
```

### Worked example A — A deep-research report on a logistics startup → a narrative feature

**Corpus (the deep-research dump, as handed over):** a 40-page report — market sizing for last-mile delivery; the company's routing-algorithm IP; a section on the founder (former emergency-room logistics coordinator); churn and retention data; three competitor profiles; a risk register. Confidence labels travel with each: the founder's ER background is VERIFIED (interview + LinkedIn), the "30% faster routes" claim is LIKELY (company-reported, one third-party confirmation), the TAM figure is UNCONFIRMED (single analyst estimate).

**Movement A — research wall + story-finding:**
> *Iceberg check:* the report is broad but the founder section has real depth — multiple interviews, texture about the ER. The market and competitor sections are surface; they'll mostly submerge. *Submergeable majority named:* the TAM math, two of three competitor profiles, and most of the risk register stay off the page. *Telling subject found:* not "the last-mile delivery market" (the report's framing) but **the founder who learned routing under fluorescent ER lights, deciding which gurney went where while people were dying.** *Secret theme (build file only):* the systems that move things fastest were learned where the stakes were life and death. *Prism:* the ER origin / the algorithm / the churn problem / the human cost of a late delivery — all one story about *urgency learned the hard way.*

**Movement B — structure layer (the report's sections ignored, story-strands emerged):**
> The report's outline was Market → Technology → Founder → Risks. The cards re-clustered into three *story* strands: **"the ER"** (the origin, scene + character) · **"the thing the algorithm actually does"** (the IP, lifted from spec to consequence) · **"the deliveries that fail"** (churn data, made human). Macro-spine: non-chronological braid, opening on the ER. Connective tissue: the *stopwatch* is the recurring hinge — the founder timed gurneys, then timed routes, then timed the deliveries that arrive too late; it lets every theme-to-theme seam pivot on a single true image. (The TAM figure, UNCONFIRMED, is flagged to stay out of any dramatized claim.)

**Movement C — the lift (lead mined from the corpus's most jarring true particular):**
> **The lead:** "Before she ever optimized a single delivery route, Dana Okafor spent six years deciding, in the time it takes to read this sentence, which dying person moved first." *(Wait-what: a delivery-software founder introduced through triage, not logistics. The true jarring detail — six years as an ER logistics coordinator — is VERIFIED.)*
> **The telling** rides the algorithm's facts through Dana ("she talks about a delivery van the way she used to talk about a trauma bay"), submerges the market math entirely, and lands its hit on a true, traceable number: the LIKELY "30% faster" claim, placed inside plain narration so it lands — *"The routes got thirty percent faster. In an ER, thirty percent is the difference between a name and a time of death."* The secret theme vibrates through that line; it is never stated as "this is a story about urgency."

*Why it works:* the report's logical order was discarded for a seductive one; the corpus's most human, most VERIFIED particular became the lead; ~75% of the corpus deliberately submerged; the one UNCONFIRMED fact (TAM) never entered a dramatized claim; and the meaning is the sum the reader assembles, not a thesis. A reader who came for "the last-mile delivery market" stays for Dana.

### Worked example B — A knowledge-base on sleep science → a Substack edition (the snoozefest, avoided)

**Corpus:** a knowledge base of ~60 atomized cards on sleep and athletic recovery — studies on sleep stages, cortisol data, a coach's protocols, anecdotes from three athletes, a debunked myth ("you can bank sleep"). All confidence-labeled.

**The failure this avoids (AN-3):** the default output is "5 things the research says about sleep and recovery" — a snoozefest. A reader gets the same value from the abstract.

**The lift (one strand shown):**
> **Researcher register (the report):** "Studies show that deep-sleep deprivation elevates cortisol, which impairs muscle recovery by up to 40%."
> **Lifted through a character, plain prose, one reserved hit:** "Marcus didn't believe the coach about sleep — he thought it was the soft part of training, the part you skipped to do more of the real part. Then they pulled his blood for six weeks. **The number that came back wasn't about how tired he felt. It was about how slowly he was healing, on the nights he was sure he was fine.**"

*Why it works:* the cortisol finding (LIKELY, one strong study) rides through Marcus's skepticism — which is also the *reader's* skepticism (proxy stance). The "40%" stat is submerged into "how slowly he was healing" rather than stated as a number, because the felt version lands and the precise figure was only LIKELY. The debunked "bank sleep" myth becomes a turn in the story ("the thing everyone believes that the blood work quietly disproved"), not a bullet. The significance — *the invisible work decides the visible result* — vibrates; it is never the headline.

## Quality Gate

> **🛡️ Anti-Pattern Check**: review against `genius.md § Susan Orlean Would Never... (Anti-Patterns)` and § Expert-Specific Quality Rubric (rows: **Structure-Before-Prose**, **Lift Into Story**, **Reader-as-Proxy Stance**, **Lead / Hook Seduction**). Flag and fix before delivering.

- **It tells, it doesn't inform (AN-3 — the cardinal test for this pipeline):** could a reader get the same value from the original report or a fact sheet? If yes, you stopped at assemblage — go back to the lift. The test is whether a "just give me the findings" skeptic stays at the dinner table, not whether the facts are all present. A report with prettier sentences is still a report.
- **The three walls were respected (Pattern 5, AN-4):** research was done before structure; structure was decided in the card layer before prose; the prose did not silently re-architect the spine. If you drafted to figure out the shape, you collapsed the walls — restart at the cards.
- **The iceberg floats (Hidden Knowledge):** most of the corpus (~70–90%) is deliberately submerged — present as confidence, absent from the page. If the draft tries to surface every finding, it's a report; cut to the tip. If a beat felt thin and tempted invention, that was a reporting hole, not a writing license (the stuck-test).
- **Themes emerged from the story, not the report (Pattern 6):** the clusters came from moving the cards by *story-strand*, not from transcribing the corpus's original section headings. The report said "Market / Tech / Risks"; the story found "the person / the thing nobody believed / the cost."
- **Connective tissue is built (Pattern 7):** every theme-to-theme seam has a named hinge — a shared image, person, or echo. No seam's bridge is "nothing, I just need to get from finding A to finding B." The piece reads as one telling, not a binder of findings-sections.
- **The lead does all the work on a TRUE particular (Pattern 4):** the opening triggers an involuntary "wait, what" mined from the corpus's most jarring *real* detail (usually a person) — not from the headline finding, and not from "the research reveals." Honesty spine: the jarring detail is literally true and traceable.
- **Proxy, not researcher (Pattern 3):** the voice is the fascinated guide who didn't expect to care — "I went in thinking this was dry, and then —" — never the analyst delivering findings. The reader feels accompanied into a subject they didn't choose, and trusts the telling *because* the skepticism was shared.
- **Significance vibrates, never stated (Pattern 8, AN-3):** the corpus's takeaway is the *sum the reader assembles*, not a "what this research teaches us is —" sentence. The theme lives in the build file; it vibrates in the prose.
- **Punches pulled, then hit (Pattern 9):** plain confident prose is the floor; 2–4 reserved hits (true data points or moments) land *because* of the quiet around them. No "boom boom boom boom" of finding-after-finding.
- **Honesty spine intact (the load-bearing gate):** every dramatized particular traces to a VERIFIED or LIKELY card; nothing was invented to make the yarn flow; no UNCONFIRMED fact was promoted into a confident scene. The better the telling, the stricter this check — a vivid scene on an unverified fact is the failure to kill on sight.

## Common Pitfalls

- **Drafting the story straight off the research dump, skipping the card layer (AN-4 — the pipeline's cardinal sin).** Reading the corpus and starting to write narrative immediately, "figuring out the shape" in the prose. This collapses the middle wall and produces a draft that's pretty but formless — mood with no architecture, seams showing, the report's logic leaking through. **Recovery:** stop drafting. Run Step 3 — hand the corpus to `orlean-card-structure`, atomize into cards, cluster into *story* themes (not the report's sections), sequence the spine, and map the seams. Only return to the lift once the spine is locked. The cards organize a story you understand; the prose does not invent one.
- **Surfacing the whole corpus — inclusion instead of selection (the report-in-disguise failure).** Feeling that because you *found* it, it has to go in — so the draft tries to honor every finding and becomes a comprehensive information dump with narrative pretensions. This is the snoozefest in its most seductive form, because it *feels* like thoroughness. **Recovery:** name the submergeable 70–90% explicitly (Step 1's iceberg check), and cut it from the page. It is not wasted — it's the confidence under the tip. The lift is the courage to leave most of the iceberg underwater. Ask of every paragraph: does this *tell*, or does it just *include*?
- **Inventing a vivid detail to make a thin beat flow (honesty-spine breach — the most dangerous failure).** A beat needs color, the corpus is dry there, and the temptation is to add an atmospheric particular that "feels right." The better the prose, the more convincing the fabrication. **Recovery:** that temptation is the stuck-test firing — it's a reporting hole, not a writing license ("every time I'm stuck, I just haven't reported enough"). Report the real detail and dramatize *that*, or cut the beat. Run the fact-trace pass (Step 5): every dramatized particular must walk back to a VERIFIED/LIKELY card. A yarn built on an invented detail has forfeited the only thing nonfiction has.
- **Letting the researcher's voice survive into the prose (Pattern 3 fail — the report register leaks).** The stance starts as the fascinated proxy but slips back into "the data shows" / "key finding three" partway through, because the source material is written that way and it's contagious. The reader stops feeling accompanied and starts feeling briefed. **Recovery:** run the researcher-register → proxy-register translation (Step 2) across the *whole* draft, not just the opening. Move all provenance into the build file. Reinstall the turn-back lines. The corpus's job was to be true; the prose's job is to seduce — they speak in different registers, and only one of them is the reader's.
