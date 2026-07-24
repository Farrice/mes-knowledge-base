# Cross-Domain Patterns — Riley Brown

How Riley's marketing-ops patterns transfer beyond marketing. Grounded in the Cross-Domain Connections section of `extractions/riley-brown/mes-extraction.md`. Each entry: the pattern → the transferable principle → where it lands outside marketing.

---

## 1. Examples-Over-Instructions → any subjective, hard-to-verify output

**Principle:** where output quality is *subjective* (unlike code, which is verifiable), don't engineer a cleverer prompt — engineer *retrieval of verified exemplars* and describe plainly.

**Transfers to:**
- **Sales** — retrieve your best closed-won call transcripts as the exemplar set; the agent drafts objection handling in the voice that already won.
- **Recruiting** — retrieve your strongest past job descriptions / outreach that got replies; generate new ones against that corpus, not a blank template.
- **PR / comms** — retrieve statements that landed well; draft the next crisis note against proven cadence.
- **Design briefs** — retrieve briefs that produced work you loved; the agent writes new briefs to that standard.

The load-bearing move everywhere: **a scraped/curated library of "what good looks like" beats any amount of instruction-tuning the prompt.**

---

## 2. Longest-Running-Ad Heuristic → any "no internal data, but persistence is public" signal

**Principle:** when you can't see the private success metric, use *how long something has survived* as a free, public proxy — and label it as inference, not proof.

**Transfers to:**
- **SEO** — a page ranking for 2+ years is presumably converting/earning links; treat evergreen survivors as the template, freshly-published pages as unproven.
- **Sponsorships** — a brand that has sponsored the same creator for 6+ months is presumably getting ROI; repeat sponsorship = a durability signal.
- **Product features** — a feature that survived every roadmap cut for a year is load-bearing; a feature added last sprint is unproven.
- **Hiring / vendors** — tenure as a (weak, flagged) proxy for fit when performance data is opaque.

Always carry Riley's epistemic honesty: *durability suggests value; it does not prove it.*

---

## 3. Draft-Link / Approval Terminus → any high-stakes outbound action

**Principle:** remove all the *labor* before the send; keep the *judgment* human. The safety and taste live in the terminus (an editable draft behind approval), not in the prompt.

**Transfers to:**
- **Legal / contracts** — agent drafts the redline; a human signs.
- **Finance** — agent stages the transaction/invoice; a human approves the release.
- **Support** — agent drafts every reply; an agent-with-a-pulse sends the sensitive ones.
- **Publishing / posting** — agent stages the post; a human schedules. (Platforms increasingly enforce this — Gmail's AI-content banner, Buffer's pre-schedule checks.)

Generalized as an Antigravity primitive: **produce an editable artifact + a link, never auto-execute.** Aligns with existing client-content and posting gates.

---

## 4. "Turn It Into a Skill" → institutional-memory capture in any function

**Principle:** any successful one-off is a candidate for a named, reusable, self-updating asset. Corrections get written *into* the asset so they compound; the asset may be real code — open it and read it.

**Transfers to:**
- **Ops / RevOps** — a manual process done twice becomes a documented, callable runbook (echoes Ray Amjad: "anything done manually twice becomes a CLAUDE.md line").
- **Onboarding** — record-and-replay a task once; new hires (or agents) inherit the skill.
- **Research** — a good analysis pattern becomes a saved workflow, not a re-explained prompt.

The trigger-mindset ("would this be useful recurring or scheduled? — act in the future") is the reusable technique, independent of domain.

---

## 5. Three-Path Integration → any tool-integration decision

**Principle:** the integration surface is "does it have an API," not "does it have a plugin." Pick per tool: **MCP** (rich, when it exists) → **raw REST** (API key → "build a skill that controls it") → **computer-use / record-and-replay** (when neither exists).

**Transfers to:** any automation program deciding how to wire a tool — the same ladder applies to internal tools, legacy systems, and GUI-only SaaS with no API.

---

## 6. Cost-Routing Discipline → any metered-compute workflow

**Principle:** model choice is a per-task economic decision — cheap/open for mechanical work, high-effort for cross-data analysis — with explicit awareness of plan economics ($250 for nine frontier prompts; the $20 plan buys only a few high-effort runs).

**Transfers to:** maps directly onto Antigravity's model-routing / Opus-fallback policy — mechanical → cheap/open, analysis → high, always cost-aware. The mid-run effort escalation ("turn up soul... extra high") is a reusable move for any long-running agent task that turns out to need reasoning, not retrieval.

---

## Skill-Stacking Inside Antigravity

Riley's scraper-fed **exemplar retrieval + taste** is the missing *input layer* that orchestration skills assume already exists:
- **Nick Saraev / Mark Kashef / Nate B. Jones** (agentic workflows, orchestration) — Riley supplies the verified-exemplar retrieval those pipelines consume.
- **Rachel Woods** (AI operations) — Riley is the marketing-specific instance of the ops discipline.
- **Any voice expert** (Lara Acosta, Nicolas Cole, Diandra) — pair the creator-to-skill compiler to auto-source their exemplar sets.
- **The extraction pipeline itself** — scrape → corpus → skill is literally our own `/extract` loop, industrialized. Every scraped creator is an `/extract` candidate.
