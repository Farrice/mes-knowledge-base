# Growth Blueprint OS — Genius Context

Load this before producing any Tier-1 deliverable. It carries four things: the surpass doctrine (why this system exists), the adopted patterns (what we took from Kallaway, with attribution), the quality rubric (how output is judged), and the anti-patterns (what fails on sight).

Provenance: all Kallaway patterns below are written fresh from `extractions/kallaway-growth-system/extraction-report.md` (pattern IDs P1–P21, signature moves SM1–SM10, hidden knowledge H1–H18) and `extractions/kallaway/anatomy-cards.md`. No verbatim redistribution of his skill files; attribution notes mark what is his, what is upgraded, and what is entirely ours.

---

## 1. The Surpass Doctrine

Four commitments, each falsifiable, each aimed at a named gap in his system:

### 1.1 Receipts-first
Every competitive claim carries evidence a reader can click: specimen URL, views, outlier multiple, date. Kallaway's whitespace scores are Claude's impressions, and his evidence layer sits behind Sandcastles Pro ($39/mo annual, 100 credits — his own Topic Scanner spends up to 50 of them in one run); his fallback ships the same authoritative artifact "unvalidated by performance data" behind the same confident typography. Ours cannot: a score without ≥2 cited specimens does not ship, and where data is absent the artifact says INTERVIEW-ONLY at the top instead of dressing a guess as a map. The claim-label system (VERIFIED / LIKELY / UNCONFIRMED) is mandatory on every claim in every artifact — it is the factual-grounding standard applied to strategy work.

### 1.2 Identity depth
His avatar stops at demographics + psychographics ("believe, fear, have tried"). Ours goes to the identity layer: what the buyer would have to *believe about themselves* to buy, what resisting the purchase *protects*, and what admitting the problem *costs them socially* (the McRaney deep-canvass triad — belief / resistance / cost-of-admitting). Plus real language: ≥10 buyer verbatims mined from comments, reviews, and forums with URLs, on day one — the pain bank arrives pre-stocked, not as a "grow it forever" IOU. Demographic profiles produce demographic content; identity profiles produce content that recognizes.

### 1.3 Revenue wiring
His system optimizes reach proxies while claiming to optimize trust with a buyer — buckets get a "strategic job" but never touch offer economics, and his calibration tracker is a blank template with no dollar definition of "working." Ours wires every bucket to the offer it feeds: funnel role, estimated lead value, a dollar-defined "working =" threshold, and a kill/keep rule answerable by batch 3 (in Farrice's own runs: which buckets feed the $750 Angle Map, which feed the $2,500 Proof-to-Market Sprint). Calibration decides in dollars, not views. The Chain's question — "which bucket makes this business money, and how do you know?" — must have a written answer in the artifact.

### 1.4 Durable branded artifacts
His signature HTML outputs are chat-scoped: unbranded, unexportable, gone with the session — nothing a client could receive. Ours are files in a client-visible state folder (`growth-lab/<niche-slug>/`, 7 living artifacts + dated history) with a staleness manifest, rendered client-grade via `render_brief.py --client` under the Premium Minimal design contract (02-DESIGN-CONTRACT: Helvetica Neue, zero border-radius, one dark interruption), with an export row on every artifact. The artifact IS the deliverable; the flagship Content Growth Blueprint is the demo asset for the cash lane. His system has no sellable output at all — that absence is the whole commercial opening.

---

## 2. Adopted Kallaway Patterns (with attribution)

Seven patterns adopted because they are genuinely excellent. Each entry: the mechanism, why it earned adoption, and what we changed.

### 2.1 Constraint-relaxation rings
*(Adopted from extraction P4 — the highest-value non-obvious mechanic in his corpus; it exists only in his rendered artifact, never spoken.)*
Audience rings are not "broader circles" — each ring outward relaxes exactly ONE named constraint versus the ring inside (geography comes off, then purchase history, then intent…). This makes the ring set auditable: you can argue about *which* filter comes off first, which is a decision, where "go one ring broader" is a vibe. Ring 5's constraint column reads "everything" — which is precisely why it is a trap, not a tier. **Our change:** ring estimates (size / conversion proximity / competition) must be anchored with real proxies — channel counts per ring from the signal pack, search volume where fetchable — or labeled UNCONFIRMED. He acknowledged his estimates were directional and left them invented even where data was fetchable; we fetch.

### 2.2 The 3-2-1 mix + chaos reserve
*(Adopted from P5 + P6 — virality modeled as a budgeted risk, exploration modeled as designed experiment.)*
The 7-video batch: 2 narrow buckets (Rings 2–3, trust + conversion) × 2 videos, 1 broad bucket (Ring 4, reach) × 2, plus 1 chaos dart. Virality is deliberately a *minority* of the batch because an accidental Ring-5 hit poisons the algorithm's model of who the channel is for — reach is rationed and fenced. The chaos agent is not a random idea: each candidate is wild in a *different way*, and each carries an explicit "a win teaches you" payoff, so one rogue slot per week compounds into a designed experiment with orthogonal questions. Unused candidates bank in the reserve. **Our change:** chaos candidates are pre-screened against the whitespace map so the rogue slot doubles as a positioning probe, and every bucket — chaos included — carries the revenue wiring from §1.3.

### 2.3 The two-zone sourcing rule
*(Adopted from P7 — it resolves the standard creator contradiction and exists only inside his artifact.)*
Topics are altitude-bound: sourced only from the ring your bucket sits on. Craft — formats, hooks, storytelling, editing, pacing — is altitude-free: sourced from anywhere on the board, including Ring 5 and other niches entirely. Niche drift is thereby explained causally as a *sourcing failure with a specific point of entry* (sourcing topics from Ring 5), not a discipline failure. **Our change:** the format workflow operationalizes it — cross-niche specimen sourcing for mechanism cards carries receipts, per his own under-used doctrine.

### 2.4 Menu-not-verdict
*(Adopted from SM5 — he never presents a menu without a pick, and never a pick without the losers kept warm.)*
Every recommendation ships as: one starred pick with the reason, a visible bench of labeled alternates, and the standing rule that the operator's swap beats our ranking — they know their business and what they'd enjoy making. His Bullseye Builder is the exemplar: 8–10 candidate buckets drafted, a starting trio recommended (2 narrow + 1 broad), the rest held as a named bench, plus 4–5 chaos candidates with the unused ones banked as the reserve — "pick the three that fit. These are my recommendations — swap any of them." The bench gives the document a future: when calibration kills a bucket, the replacement is already scoped. **Our change:** bench entries carry the same receipts and revenue wiring as picks, so a swap never trades evidence for preference.

### 2.5 Credit-bill → cost transparency
*(Adopted from P8/SM2 — free stage first, paid stage quoted against balance, exclusions itemized and overrulable. Maps directly onto the house cost-gate doctrine and the binding cost-transparency rule.)*
Free triage always precedes paid depth; any run that costs money states the itemized bill before spending; exclusions are itemized by category with counts and shipped in the artifact so the human can overrule — the screen is a recommendation, not a filter; and zero-spend decisions are *reported as findings* ("nothing at that tier was worth buying"). **Our change:** the signal pack is $0 (yt-dlp, keyless), so the bill here is usually time and freshness, not credits — but the shape holds for any paid lane (research.py API calls, future data bridges): quote before spend, itemize, let the human trim.

### 2.6 Five-beat teaching panels
*(Adopted from extraction delta #29 / §6.2 — visualizations that teach, not decorate.)*
Every interactive wedge or slice explains itself in a fixed 5-beat order: (1) what this dimension even is, plain language, concrete contrast; (2) the total menu of options; (3) what we're seeing in your niche — a scoreboard, not a paragraph; (4) the white space, stated plainly; (5) what it means for *you*. A reader who has never heard the word "positioning" can use the artifact; a reader who has can audit it. The same five beats appear in the markdown form so the teaching survives outside the HTML. Full interaction canon: `references/artifact-design-language.md`. **Our change:** beat 3's scoreboard rows carry specimen receipts; beat 5's translation cites the interview evidence it leans on.

### 2.7 Folder-as-memory → schema'd state
*(Adopted from H11/P21 — durable state across ephemeral chats, every skill reads before it asks; upgraded to close his gap #4.)*
His pattern: named state files as the spine, artifacts pinned so they can be edited without re-running the pipeline, every file declaring its consumers ("Read by:") and its handoff (numbered step, manifest of contents, one-line English state, one-word continue trigger). **Our upgrade — the part he never built:** state is schema'd and dated (`growth-lab/<niche-slug>/` + `manifest.json` staleness ledger with TTLs and dependency edges), so the system can answer "what's now stale?" when positioning changes — his write-once markdown silently rots downstream and cannot tell. Plus a structured performance ledger (`ledger/performance-ledger.jsonl`) instead of prose coach-logs, so calibration compounds in numbers.

**Also carried (smaller, load-bearing):** reflect-back interviewing — mirror every answer in one tightened sentence, sharpen by guessing more specifically instead of stacking follow-ups (anatomy card adopt #2); hypothesis-then-falsification labeling — the self-report table is openly a guess until data crosses it (SM1); name-the-trap-inside-the-chart — every ranked visual carries an adjacent callout naming the wrong conclusion it invites, e.g. "a person winning, not a topic" (P9/SM3); `[NEED]` refusal markers on exactly the slots where a hallucinated number would be most damaging (H5); plain-English glossing of every term of art at first use (adopt #4); the honest ceiling — say what the machine cannot do and design the human's last mile around it (P14/SM8); the unclaimed-vs-graveyard test — zero videos means unclaimed, many low-outlier videos means graveyard; tell them apart with performance data before calling anything an opportunity (anatomy card #2); the 24-hour maturity rule — no verdict on a video at 24 hours (H9); the blind-spot declaration — every dashboard states what it cannot see and the wrong conclusion that gap invites, before its conclusion (H10).

---

## 3. Quality Rubric — how a Growth Blueprint artifact is judged

Adapted from extraction report §5 (his nine criteria, reconstructed from what he praises, enforces, and corrects) with our three hard additions folded in. Nine criteria, scored 1–5. **Any single 1 fails the artifact regardless of total.** Score ≥4 on a criterion requires the evidence named in its right-hand cell, not a feeling.

| # | Criterion | Fail (1) | Pass (3) | Blueprint-grade (5) |
|---|---|---|---|---|
| **Q1** | **Evidence provenance + claim labels** *(his R1 + our labeling addition)* | Assertions with no source; any unlabeled claim | Sources named; most claims labeled | Every row carries channel + outlier + views + a live link; **every claim labeled VERIFIED / LIKELY / UNCONFIRMED**; data tier (fresh/stale/absent) declared at the top; skipped evidence tiers reported with the reason |
| **Q2** | **Specimen floor** *(our addition — the anti-impression rule)* | Scores are the model's impressions | Some scores cite examples | **Every attribute score and every whitespace verdict cites ≥2 specimen videos** with URL, views, outlier, date — or is explicitly downgraded to UNCONFIRMED with the specimen gap named |
| **Q3** | **Revenue wiring** *(our addition — closes his gap #2)* | Buckets never touch money | Funnel roles asserted | **Every bucket wired to offer economics:** named offer it feeds, funnel role, estimated lead value with its basis, dollar-defined "working =", kill/keep rule answerable by batch 3 |
| **Q4** | **Falsifiability** *(his R2)* | Unfalsifiable synthesis | Claims checkable in principle | Hypotheses labeled as hypotheses until crossed with data; verdicts scored (confirmed / contested / redirect); exclusion rows carry reasons; the human can overrule any call and the artifact says so |
| **Q5** | **Named mechanism** *(his R3, widened)* | Descriptive labels only | Memorable names | Buckets, formats, and coined concepts carry a proposed name + an alternate + a human veto — the slot cannot be empty; *why-it-works* mechanisms named per bucket/format, not just stats |
| **Q6** | **Actionability at the decision level** *(his R4)* | "Post consistently" | Ordered structure | An operator can act without asking a question: decision-ready moves per whitespace entry, beat-level format recipes at the operator's real constraint level, recommended pick + bench everywhere |
| **Q7** | **Anti-misread guard** *(his R5)* | None | A caveat somewhere | The trap the visual invites is named inside the visual; a blind-spot section states what the data cannot see (coverage limits, conversion invisibility, one-channel dominance) and the wrong conclusion each gap invites |
| **Q8** | **Anti-hallucination discipline** *(his R7 + our absent-tier rule)* | Plausible numbers filled in | Uncertainty hedged | `[NEED]` markers on the exact slots refused, placeholder shown, why-the-slot-matters stated; ABSENT data tier renders interview-only with the banner — never an authoritative artifact on vibes |
| **Q9** | **Handoff contract + state hygiene** *(his R9 + our manifest)* | Ends with prose | Names a next step | Named state file with itemized manifest of contents; `manifest.json` updated (produced_at, data_tier, pack_ref, deps); prior version snapshotted to `history/`; one-line English state; next workflow named |

| **Q10** | **Register + insight floor** *(Farrice 2026-08-28 — the production-grade gate)* | Process narration as content; anything the ICP could have written themselves; jargon walls | Reads clean, some sections teach | Every section passes: "could the ICP have written this? If yes, cut or deepen." Coach-to-reader + strategist authority; every word earns its mark; verdicts first, receipts quiet behind them; immediately actionable. Process residue in a reader body ("proxy:", "(assumed base)", "on file", tool/tier names) = automatic 1 |

**THE REGISTER CONTRACT (Farrice verbatim, 2026-08-28 — binding on every reader-facing artifact):** Coach-to-reader Kallaway-grade base plus premium-strategist authority, "but with less jargon and less verbosity, and actual professional insights that show authority, knowledge, and expertise. It should be a display of our expertise, taste, and judgment… Every word needs to earn its mark… delivered with quiet confidence and casual nature, so that it's easily articulated, clear, understandable, and simple to understand. They could literally take action immediately after reading it or be more informed and educated, and have insight strike them because of the articulation." Exemplars of the standard: `.scratch/kallaway-sandcastles-forge/content-standard-exemplars.md`. Replication fidelity source: the on-screen artifact ledger, `extractions/kallaway-growth-system/extraction-report.md` §6 — match what his artifacts demonstrably contain before adding anything.

**Two override rules** (his, kept because they are correct):
- **Identity beats a neutral metric.** A metric that says "no effect" does not veto a positioning commitment; a metric that says 0.6× does. He kept a baseline-scoring self-demonstration rule because it was his positioning — that is a deliberate, legitimate override. Log it as one when you make it.
- **Maturity window before demotion.** No performance verdict inside 24 hours; no bucket demotion before 2–3 batches.

**House override on top:** verdict routing per `directives/quality_gate.md`; the factual veto (any Q1/Q8 fabrication) is hard. Everything else nudges — a rubric miss triggers one retry of the weakest section, never a stall.

---

## 4. Anti-Patterns — fails on sight

**His four system gaps (never reproduce them):**
1. **Receipts-free authority** — a claim about a competitor, format, or "what works" with no URL-as-evidence and no label. The exact failure his fallback ships; our ABSENT tier exists so we never do.
2. **Demographic-depth avatars** — an ICP that stops at "women 45–65, affluent" with psychographic bullets. No belief/resistance/cost-of-admitting mapping, no verbatims = not done.
3. **Gated or vanishing evidence** — analysis that only works if a third-party subscription is live, or evidence that lives in a session. The data spine is ungated and $0; the artifacts are files.
4. **Reach-proxy strategy** — picking buckets, topics, or formats on outlier scores alone with no conversion column and no offer linkage. Outlier ranks the pool; positioning and economics pick from it (he demonstrated this himself by picking the lowest-scoring bucket on the board because his unfair advantage supported it — the principle survives even where his tooling didn't).

**The recognition test (two-sided, both must pass):**
- **Would Kallaway recognize this as his?** Reading our rings, 3-2-1 mix, two-zone sourcing, or teaching panels, Kane Kallaway would recognize the mechanics as his own, faithfully understood at the level he built them — not a paraphrase that dropped the load-bearing details (the constraint column, the chaos payoff line, the bench). If he'd say "that's not how it works," the adoption failed.
- **Would Farrice recognize this as his standard?** The same artifact must read as Farrice's: receipts behind every score, the buyer's exact words, dollars behind every bucket, Premium Minimal on the page. If it could pass for a Sandcastles chat export, the elevation failed.

**House slop bans (the floor under everything):**
5. **Fabricated metrics** — any number without a source or a `[NEED]` marker. Includes repeating his growth claims as fact: "140K users" is self-reported; "75K followers / $100K attributable" conflicts with his own on-screen dashboard (UNCONFIRMED, extraction §7). Surpass claims reference only what we can show side-by-side.
6. **Ban-bank prose** — run `python3 execution/prose_classifier.py check <file>` before any artifact ships; `directives/ai-slop-ban-bank.md` is the sole canon. The ban bank is the floor; intent makes copy land.
7. **Comprehensive walls** — "comprehensive" output is system failure regardless of score. Every artifact finds the single truth and delivers it through the right mechanism; density over completeness; client docs lead with a ≤2-page executive verdict.
8. **Elevated paraphrase of buyer language** — the pain bank ships the buyer's researched words EXACTLY, sourced. Polishing verbatims kills the credibility they exist to provide.
9. **Blocking gates** — staleness, rubric misses, and drift are flags with quoted fix commands. Only the cost gate and the factual veto block (Compass Doctrine).
10. **Operator leakage in reader-facing forms** (Farrice 2026-08-27, BINDING) — any repo path, command, tier jargon, system name, or `[NEED]` marker inside a client/product artifact. The document serves the reader; operator material lives in the paired `operator/<artifact>-notes.md`. Tier states translate to reader language (see SKILL.md Reader-Purity Rule). Quoted-fix-command guidance in workflows applies to the OPERATOR side only.
