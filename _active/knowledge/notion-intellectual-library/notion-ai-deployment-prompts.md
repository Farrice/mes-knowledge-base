# Notion AI Deployment Pack — The Antigravity Intellectual Library

**What this is**: Copy-paste prompts that replicate Simon's (Systems Made Better) intellectual-library architecture inside YOUR Notion, tuned to the Antigravity system. Run them in **Notion AI personal-agent chat** with the strongest model available (Claude Opus-class). Run them IN ORDER, one chat each. Each prompt ends with verification steps — eyeball them before moving on.

**Why it's sequenced**: Simon's plan-lock principle — the AI proposes, you approve, THEN it builds. Don't paste all four at once.

**Source design**: `skills/simon-intellectual-library-os/references/notion-port-blueprint.md`

---

## Prompt 1 — Build the Library System (run first, ~one session)

```
You are my meta-agent for building a knowledge architecture called the Intellectual Library. I run a system of 100+ extracted expert methodologies (frameworks, psychological patterns, writing techniques) that currently live in messy prose logs. We are replacing that with a glanceable, contextually-organized library that both I and AI agents can use.

Before building anything, make a plan and confirm it with me. Then build exactly this:

1. A hub page called "🏛 Intellectual Library" — it will hold dashboard views of everything below.

2. Database "📚 Knowledge Entries" — the heart of the system. Properties:
   - Title (the one idea — one idea per entry, never two)
   - Type (select): Principle, Framework, Case Study, Example, Quote, Pattern, Study
   - Category (select): Content, Copywriting, Brand, Buyer Psychology, Storytelling, Systems & AI, Audience Growth, Offers & Pricing, Personal Voice
   - Key Insight (text — 1-2 sentences an agent can act on at a glance)
   - When to Apply (text — the trigger conditions for using this idea)
   - Confidence (select): Proven, Tested, Untested
   - Expert (relation → Experts database below)
   - Source (relation → Sources database below)
   - Linked Entries (self-relation — for cross-expert connections)
   - Status (select): Active, Needs Review, Deprecated
   - Date Added (date)
   Views: "By Category" (grouped), "By Confidence" (grouped), "Board by Type", "By Expert", "Recently Added" (sorted newest).

3. Database "🧠 Experts" — Name, Domain, Tier (A/B/C), One-line Genius (text), Entry Count (rollup counting related Knowledge Entries), Status.

4. Database "📖 Sources" — Title, Type (Book/Video/Course/Article/Podcast), Author or Creator, URL, Ingestion Status (Not Started/Mapped/In Progress/Complete), Date Ingested.

5. Database "⚙️ Skills & Playbooks" — Name, For Advisor (text), Trigger ("use when…"), Status. Page bodies will hold step-by-step playbooks I'll configure as AI skills.

6. Database "💬 Session Memory" — Title, Date, Advisor/Mode, Key Decisions (text), Pickup Prompt (text). This is our cross-session memory: at the end of important chats I'll ask you to log the session here and write me a prompt to resume in a new window.

7. On the hub page: linked views of all five databases — Knowledge Entries by Category and by Confidence at top, then Experts, Sources with ingestion status, recent Session Memory.

8. A page "🧭 Global Instructions" — an orchestration layer that lists advisor modes in a table (Mode, What it does, When to pick it, When NOT to pick it). Seed it with one row: "Librarian — maintains the Intellectual Library; pick for ingestion, organization, health checks; do NOT pick for domain advice."

9. A page "Who I Am — Context Map": leave headed sections for me to fill: who I am, my business, my voice, and a map of my key databases. Advisors must read this page plus their knowledge base before answering.

Rules going forward, written INTO the Global Instructions page:
- The AI is the librarian. I capture and curate; you organize, link, index, and audit. 
- Every entry is atomic: one idea, with Key Insight and When to Apply always filled, Confidence set (new material enters as Untested), and a Source.
- Any answer worth keeping gets saved back as a Knowledge Entry (Untested) or Session Memory row — each question makes the next answer better.

Propose your build plan first. After I approve, build it all, then give me a checklist to verify: all 5 databases exist with the exact properties, the views work, the hub shows everything, and the two pages exist.
```

**Verify before Prompt 2**: 5 DBs + hub + 2 pages exist; Knowledge Entries has all 11 properties; relations actually connect (create one dummy entry and link it to a dummy expert).

---

## Prompt 2 — Create Your First Grounded Advisor (repeat per advisor)

```
Using the Intellectual Library system you can see in my workspace (hub: "🏛 Intellectual Library"), create a specialist advisor as a new instruction page. Advisor: [NAME — e.g., "Content Psychology Advisor"], covering the Knowledge Entries categories: [e.g., Content, Buyer Psychology].

The instruction page must be ONE page, in this order:
1. Purpose & north star — who this advisor is and its mission, written like a job description for a new hire.
2. MANDATORY ENTRY GATE, stated imperatively: "Before answering anything, read the 'Who I Am — Context Map' page AND your linked Knowledge Entries view below, filtered to your categories. Weight entries: Proven over Tested over Untested. If the knowledge base has little or nothing on the question, say so plainly and label any fallback opinion as ungrounded, with a confidence level."
3. A linked view of the Knowledge Entries database filtered to this advisor's categories.
4. Boundaries & handoffs — what this advisor does NOT cover and which other mode to use instead.
5. Working method: classify the question → read the knowledge base → apply relevant entries by name → validate against When-to-Apply conditions → answer in my context, citing entries.
6. Anti-drift rules, compressed bullets.

Then: review the whole page for token efficiency — reduce length, keep every step (target meaningfully shorter, same behavior). Then register the advisor as a new row/section in the "🧭 Global Instructions" page (what it does, when to pick, when not to pick).

Finally, run the acceptance test WITH me: I will ask it a real question now. The correct behavior, since its filtered view is empty or thin, is to tell me the knowledge base can't support an answer yet and recommend ingestion — NOT to give me generic advice. Confirm you understand, then prompt me for the test question.
```

**Verify**: the refusal test passes. If the advisor answers generically with an empty view, tell it: "Your entry gate failed. Move it earlier, make it imperative, and re-test."

---

## Prompt 3 — Ingest a Source (book, video set, or one of my extractions)

```
Act as the Librarian mode from my Global Instructions. We're ingesting a source into the Knowledge Entries database: [SOURCE TITLE + what it is].

Process — follow exactly:
1. First, here is the chapter/section list of the source. Build yourself a brief working plan mapping every section, candidate Categories per section, and likely entry Types. We will work through it in order and you will track progress against it. [PASTE CHAPTER LIST / SECTION LIST]
2. Register the source as a row in the 📖 Sources database (Ingestion Status: Mapped).
3. I will paste the source in chunks (pasted text, not PDFs — tell me if a chunk seems cut off). For each chunk:
   - EXTRACT every distinct idea, framework, case study, and strong quote.
   - ATOMIZE: one idea per entry. If an "and" joins two ideas, split them.
   - NORMALIZE: create Knowledge Entries with ALL properties filled — Key Insight (1-2 actionable sentences), When to Apply (trigger conditions), Confidence (Untested unless the source itself provides validation), Type, Category, Source relation. Entry body: What it is / Why it works / How to apply / Examples / Connections.
   - LINK: connect new entries to existing entries, including from OTHER experts where ideas rhyme ("X says something similar").
4. After each chunk, report: entries created (by type), sections completed on the map, anything skipped.
5. When the source is done: mark Ingestion Status Complete, give me a coverage summary, and flag anything that needs my judgment.

Confirm the plan, then ask me for the first chunk.
```

**Tip from the source videos**: paste text rather than uploading PDFs (AI reads long PDFs poorly); use the strongest model for ingestion; don't paste more than a few chapters per message.

---

## Prompt 4 — The Monthly Health Check (save as a Skill page, then trigger monthly)

```
Create a page in ⚙️ Skills & Playbooks called "Library Health Check (Monthly)" containing this playbook, then run it now as a demonstration in report-only mode (change nothing yet):

PHASE 1 — AUDIT the Knowledge Entries database and report findings per stage:
1. Contradictions — entries asserting incompatible claims (name both).
2. Orphans — entries with no Linked Entries relations and no Expert/Source relation.
3. Provenance — entries with empty Source, or attribution that looks wrong.
4. Coverage — Sources rows stuck in Mapped/In Progress; experts in 🧠 Experts with zero entries.
5. Staleness — Active entries older than 90 days: still true, still relevant?
6. Writing quality — entries violating plain-writing rules (AI-sounding filler, vague Key Insights that can't be acted on at a glance).
7. GROWTH (most important) — based on gaps versus my categories and my Context Map: suggest new entries worth adding (with reputable source candidates) and connections between existing entries I haven't drawn yet.

PHASE 2 — ACTION MENU: present every actionable finding as a numbered menu and ask which to action. Safe fixes (links, wording, registry updates) can be batched; judgment calls (contradiction resolution, deprecations, new entries) need my explicit yes. New entries you draft enter as Confidence: Untested.

End every run by logging a Session Memory row: date, findings count, actions taken, and a pickup prompt.
```

**Cost note (Simon's economic routing)**: run this manually in personal-agent chat once a month rather than as a scheduled custom agent — scheduled agents burn credits; a chat-triggered skill is nearly free on the plan. If you have multiple libraries later, stagger them across different days.

---

## Seeding plan (so the library isn't born empty)

A library launched empty is a bookmark graveyard. Before or right after Prompt 2, ask me (Claude, in Antigravity) to run `/library-extraction-bridge` on 2-3 extractions — I'll produce ready-to-paste atomized entries (e.g., Meg Heckman's 16 buyer-trigger patterns, Noah Hawley's storytelling architecture, Simon's own 15 patterns). Paste those via Prompt 3's loop with "here are pre-atomized entries — normalize and create them."

## The three acceptance tests (after everything is live)

1. **Glance test**: open the hub — can you state library size, strongest lanes, weakest-confidence areas in 30 seconds?
2. **Filter test**: ask an advisor a question — does it cite entries by name, filtered by its categories?
3. **Refusal test**: ask an advisor something its lanes don't cover — does it say so instead of going generic?
