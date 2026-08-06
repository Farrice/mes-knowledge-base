---
description: Daily morning zeitgeist brief delivered to Gmail — primes content creation by surfacing jackable angles, adjacent trends, build-in-public threads, crystal ball signals, format intelligence, client conversation gold, and personal-integration prompts. Pulls from external scan + prospect list cross-reference + conversation memory.
status: superseded
superseded_by: zeitgeist
superseded_date: 2026-08-05
superseded_reason: Never scheduled; last ran 2026-05-04. Replaced by the running /zeitgeist engine (deterministic Apify scrape on the pulse sub-budget + rendered research briefs on the asset board + Google Doc). The 11-phase email dossier ceremony is retired; jackable-angle synthesis now lives in the brief's decision layer.
---

# `/daily-zeitgeist-brief` — Parallax Morning Engine

The single artifact Farrice reads over coffee that decides today's content. **Decision document, not publication.** One pick → voice memo → `/jackpost` ships post by 11am LA.

Runs at 7:00am LA daily via `/schedule` cron. Delivered to farrice.cain@gmail.com via `gws` Gmail. Archived to `knowledge/zeitgeist-archive/[YYYY-MM-DD].md` for trend-pattern lookback.

---

## Inputs

| Input | Default | Override |
|---|---|---|
| Date | today (LA timezone) | `--date YYYY-MM-DD` |
| Domain scope | A=creative-strategy, B=AI-consulting | `--domain A` or `--domain B` |
| Adjacent mode | wide + personal-territory | `--adjacent wide` or `--adjacent personal` |
| Crystal Ball threshold | conservative (primary sources only) | `--speculative` to include weak signals |
| Delivery | Gmail draft + send to farrice.cain@gmail.com | `--no-send` for dry run |
| Prospect list | `_active/farrice-brand/leads/prospects_final.csv` (50 leads) | `--prospects path/to/csv` |

---

## Phase 1 — External Zeitgeist Scan (parallel research)

**Actor**: 1 deep-research subagent (single dispatch, parallel internal queries)

Pull 7 sections of dossier into `.tmp/zeitgeist/[date]-research-dossier.md`:

1. **Domain A Zeitgeist** (Creative Strategy, last 7-14 days) — Meta/Google ad platform changes, DTC brand moves, top creative-strategy LinkedIn posts, agency pivots
2. **Domain B Zeitgeist** (AI Consulting, last 7-14 days) — agent/AI launches, "manual work" memes, fractional-AI-COO content, tooling debates
3. **Adjacent Wide** — broad cultural moments (sports, music, science, geopolitics, viral memes) with structural bridge into A or B
4. **Adjacent Personal-Territory** — EDM/PLUR/festivals, NBA, S&C training, music industry, biracial/multicultural conversations, real estate (LA/Jen's territory) — bridged to A/B
5. **Crystal Ball (conservative)** — 30-day forward signals citing primary sources only (Meta dev blog, founder tweets, a16z posts, GitHub trending, named creator pivots). Plus 1-2 speculative-watch items flagged.
6. **Format & Packaging Intelligence** — 5-7 top-performing LinkedIn posts last 7-14 days in A and B niches. For each: CONTENT (the idea) × FORMAT (text/carousel/video/structure) × PACKAGING (hook, length, opening line, CTA, rhythm). Goal: instant "today I ship [format] using [packaging] on [angle]."
7. **Client Conversation Intel** — Reddit (r/PPC, r/marketing, r/AdvertisingAgency, r/DTCMarketing, r/Shopify, r/agency, r/automation, r/n8n), LinkedIn comment threads, podcast quotes (Foxwell, CTC, Operators). 8-12 distinct real conversations split A/B. Each item: actual problem (verbatim), dominant opinion, dissenting take getting traction, specific client language, under-discussed angle.

Verification standard: every item labeled VERIFIED / LIKELY / UNCONFIRMED. Primary sources cited inline. No "people are saying."

**Time-box**: 12-15 minutes max. Better 3 verified items than 7 invented.

---

## Phase 2 — Prospect-List Cross-Reference

**Actor**: Orchestrator + Apify (LinkedIn) or Playwright fallback

For the 50 prospects in `_active/farrice-brand/leads/prospects_final.csv`:

1. Pull last 24-48h LinkedIn activity (posts, top comments) — Apify if available, Playwright per `directives/browser-automation-routing.md` if rate-limited.
2. Detect cluster moves: which 2-3 angles are MULTIPLE prospects converging on right now?
3. Flag 1-2 boomerang targets — prospects whose recent post creates a high-leverage reciprocity opportunity if today's brief hits adjacent territory.

Output: `cluster_moves` + `boomerang_targets` block injected into Phase 8 synthesis.

---

## Phase 3 — Build-in-Public Compounding Layer

**Actor**: Orchestrator + memory + skill load

**Expert reference**: `skills/lara-acosta-content-system/genius.md` (build-in-public is structural in her LinkedIn engine). Secondary: Seena Rez (early-adopter influence), Daniel Priestley (Key Person of Influence stacking).

**Source material**:
- `MEMORY.md` and recent memory files for current builds, projects, frustrations, breakthroughs
- Last 7 days of session activity (`.agent/session-state.md`, recent finalize logs, recent extraction reports)
- Active projects: Parallax Substack, prospect outreach engine, AI consulting positioning, S&C niche, EDM/My.BPM brand, real estate work with Jen, NBA betting system, current Antigravity system builds

Surface 2-3 "you've been quietly building/learning this — it's POST-able as build-in-public" threads. Format each:

```
THREAD: [one-line description of what you've been working on]
ALPHA TO PROTECT: [what NOT to share — strategic moat]
PUBLIC ANGLE: [the 80% that's safe + magnetic to share]
SUGGESTED FORMAT: [thread / single post / annotated screenshot / "lessons after N days"]
COMPOUNDS WITH: [which earlier shared thread this builds on, if any — creates serial momentum]
```

**Discipline**: Never repeat the same build-in-public thread two days in a row. Rotate.

---

## Phase 4 — Synthesis: Pre-Brief Decision Tree

**Actor**: Orchestrator

Before drafting the email, score each candidate angle on:

| Dimension | Weight | Question |
|---|---|---|
| Specificity | 25% | Does it cite a real entity / quote / number? |
| Boomerang potential | 20% | Does the entity have LinkedIn presence likely to engage? |
| Voice fit | 20% | Does Farrice's lens (Parallax / multi-angle / S&C / EDM / biracial) genuinely sharpen this? |
| Prospect resonance | 15% | Are prospects from the 50-list talking about this RIGHT NOW? |
| Format readiness | 10% | Does Format Intelligence have a matching ready-to-deploy packaging? |
| Crystal-ball lead | 10% | Does this position him 2-4 weeks ahead? |

Top 3 from Domain A. Top 3 from Domain B. Top 2 from Adjacent (one wide, one personal-territory). Top 2 from Build-in-Public.

---

## Phase 5 — Personal Integration Prompt Generation

**Actor**: Orchestrator + memory

For the top 3-5 angles surfacing today, generate 3 voice-memo prompts that draw on a SPECIFIC personal thread Farrice has shared. Rotate threads — never repeat the same memory vein two days in a row. Memory rotation pool:

- S&C coaching past + niche (`niche-positioning-locked.md`)
- Parallax origin + "see from more than one angle" (`user_deep-suppression-wound.md`, `project_parallax-substack-live.md`)
- Brother dynamic + "don't outshine your brother" (sensitive — only when Farrice's mood signals readiness)
- HS bullying for being fast / suppression
- EDM / PLUR / My.BPM streetwear (`mybpm-streetwear-brand.md`)
- Biracial identity + cultural rejection from both sides
- Wife Jen / SFV real estate / first-time buyer empathy
- Friend Javier (HVC project) + music teacher world
- NBA betting friend + product-building from craft
- Current Antigravity system builds (meta — "I'm building this engine to ship content faster")

Format each prompt:

```
P[N] — [ONE-LINE MEMORY HOOK related to today's strongest angle]

Question: [open-ended question that requires Farrice to connect his lived experience
to today's angle — NOT generic "what do you think?"]

Why this prompt: [1-line on why this memory thread sharpens this angle specifically]

Voice memo target: 60-120 seconds
```

**Sensitivity gate**: never surface the brother / suppression vein unless prior 7-day check shows positive emotional context. Default to safer threads (S&C, EDM, real estate, current builds) on uncertain mornings.

---

## Phase 6 — Yesterday's Performance Pulse

**Actor**: Orchestrator

If a post shipped yesterday, pull:
- Engagement signals (likes, comments, reposts via LinkedIn API or manual lookup)
- DM volume / responses from outreach run
- Boomerang status — did the entity referenced engage?

If no post shipped, surface 1-line: "No post shipped yesterday. Today is the recovery day — pick the highest-conviction angle."

---

## Phase 7 — Calendar Context

**Actor**: Orchestrator + Google Calendar MCP

Pull today's calendar from `farrice.cain@gmail.com`. Flag:
- Posting window constraints (meetings 9-11am LA cuts the prime-window — recommend 7-9am ship)
- Themes from today's calendar that should not contradict the post (e.g., client call about creative strategy → don't ship a flippant AI-consulting hot take that morning)
- Anything that affects voice-memo recording windows (back-to-back meetings → record on commute)

---

## Phase 8 — Email Synthesis (FORMAT C — short HTML email + deep-dive Google Doc)

**Actor**: Orchestrator

**Format C principle**: the morning email is a **decision document**, not a publication. Reader skims in 90 seconds, picks one angle, replies. Depth lives in a linked Google Doc for when they want context.

Produce two artifacts:

### 8A — Short HTML email body (~250-350 lines of HTML, ~3-min skim)

Subject: `Parallax Daily — [3-word punch]` (3-word punch = the load-bearing thesis fragment).

Email contains, in order:
1. **Header card** — Parallax Daily branding, date, tagline (blue background `#1a4d8c`, white text)
2. **Thesis card** — 2 short paragraphs naming the load-bearing event and the Parallax-native opening
3. **Decision box** — 3 cards stacked vertically with badges:
   - `★ TOP PICK` (red border `#dc2626`, red badge, light red bg `#fef2f2`)
   - `SAFE BACKUP` (gray border, gray badge `#475569`)
   - `WEEK-LATER` (default border, teal badge `#0d9488`)
   Each card: angle ID, hook in bold, 1-line context, reply command in italics
4. **Domain A — 3 cards** (blue accent `#1a4d8c`, light blue section banner `#eff6ff`)
   Each card: jack-type/badge + hook (bold, larger) + 1-2 line context + format-match line + source link
5. **Domain B — 3 cards** (green accent `#065f46`, light green section banner `#ecfdf5`)
   Same structure. If a B angle is the TOP PICK, give it a red border accent.
6. **Adjacent — 2 cards** (purple accent `#6b21a8`, light purple banner `#faf5ff`)
   ADJ-W (wide), ADJ-P (personal-territory). Bridge must be structural.
7. **Personal Integration — 3 cards** (amber accent `#9a3412`, warm banner `#fff7ed`)
   Each card: prompt ID + the question (bolded core ask), no extra explanation in the email — full reasoning lives in the doc.
8. **Deep-dive doc CTA** (blue background `#1a4d8c`, white button)
   Link to today's Google Doc. 1 sentence saying "depth lives here."
9. **How to Reply footer** (light gray bg)
   Fast / Deep / Trust / Skip paths. Inline `<code>` for reply commands.
10. **Tagline footer** (centered, gray)

Inline CSS only (Gmail strips `<style>` tags). System font stack: `-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif`. Max-width 640px. Generous padding 16-20px between cards. Bold headings, regular body.

**Voice rules apply** — no AI structural tells, max 2 em-dashes per email, no "Here's what/why/how" openers anywhere.

### 8B — Plain-text fallback body (~10 lines, for non-HTML clients)

Short summary paragraph + deep-dive doc URL. Gmail uses this if the client can't render HTML. Don't try to mirror the full HTML — keep it minimal so the user knows to open the HTML version.

### 8C — Deep-Dive Google Doc HTML (~600-1000 lines, ~10-min deep read)

Full reasoning, all sources, all 8 sections from Phase 1 dossier expanded. This becomes a Google Doc via Phase 9. Sections in this order:

1. Today's Thesis (mirror of email card, expanded)
2. Crystal Ball — full reasoning, primary-source citations inline, action items
3. Format & Packaging Intelligence — full hierarchy table, all 5 ready-to-deploy triples with content × format × packaging triples
4. Client Conversation Gold — all 8-12 conversations split A/B with verbatim quotes, dominant/dissenting takes, client language, your under-discussed angle
5. Build-in-Public — full thread cards with public angle, alpha-protected, format, when to ship
6. Prospect Boomerang — full 7-target list with action verbs and DM script template
7. Personal Integration — full prompts with memory hook, why-this-prompt, use, voice-memo target
8. Yesterday + Calendar + Honest Gaps — full transparency
9. Verified Sources — all primary URLs with dates and authors

Standard HTML: `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<table>`, `<ul>`, `<ol>`, `<blockquote>`, `<a href>`. No inline styles needed (Google Docs renders semantic HTML well during import).

Save HTML to `.tmp/zeitgeist/[date]-deep-dive.html` for Phase 9 upload.

---

## Phase 8-LEGACY — (deprecated as of 2026-05-04, kept for reference)

Old Format A (plain text with ASCII separators, single-document) is deprecated. The original brief was 668 lines, hard to skim on Gmail mobile, ASCII separators rendered poorly. Format C replaced it after user feedback: "structured so poorly and so tight that it's hard to read."

Old reference fields below if needed for fallback:

```
🌍 PARALLAX DAILY — [DATE]

Subject: Parallax Daily — [3-word punch]

═══════════════════════════════════════════
⚡ TODAY'S DECISION
═══════════════════════════════════════════
Pick one angle. Reply to this email with the # + voice memo (or jump
into Claude Code). Posts ship by 11am LA.

Top recommendation today: [#] — [why in 1 sentence]

═══════════════════════════════════════════
DOMAIN A — Creative Strategy (3 angles)
═══════════════════════════════════════════

A1 [JACK TYPE] · [Entity / news / quote]
   Hook: "[1-line hook draft]"
   Source: [URL]
   Why now: [verified context, 1-2 lines]
   Format match: [pulled from Phase 1 Section 6]

A2 ...
A3 ...

═══════════════════════════════════════════
DOMAIN B — AI Consulting (3 angles)
═══════════════════════════════════════════

B1 ...
B2 ...
B3 ...

═══════════════════════════════════════════
🎭 ADJACENT — The Parallax Move (2 angles)
═══════════════════════════════════════════
One wide-aperture, one personal-territory. Bridge must be structural,
not metaphorical.

ADJ-W [wide cultural moment] → [bridge to A or B] → [hook]
ADJ-P [personal-territory: EDM / S&C / NBA / music / real estate]
       → [bridge] → [hook]

═══════════════════════════════════════════
🛠 BUILD-IN-PUBLIC (1-2 threads)
═══════════════════════════════════════════
What you've been quietly building/learning. Compounds with prior
shared threads — creates serial authority.

BIP-1 [thread] · Public angle: [...] · Alpha protected: [...] ·
       Format: [...] · Compounds with: [...]
BIP-2 ...

═══════════════════════════════════════════
🔮 CRYSTAL BALL — 30-Day Forward
═══════════════════════════════════════════
What to start positioning for NOW. Conservative threshold: primary
sources only.

CB-1 [Signal] · Source: [primary URL] · Why 30-day matters: [...]
     Draft angle: [a positioning sentence to start workshopping today]

CB-2 ...
CB-3 ...

🌫 SPECULATIVE WATCH (90-day, low-trust — DO NOT ACT, JUST WATCH)
SW-1 [weak signal] · why worth watching: [...]

═══════════════════════════════════════════
📊 FORMAT & PACKAGING INTEL
═══════════════════════════════════════════
Pre-built triples. Pick one and you instantly know what to ship and how.

FORMAT 1: [Content angle] × [format] × [packaging spec]
  Source winner: [creator name + post URL + engagement signal]
  Hook pattern: "[the literal hook structure]"
  Length: [word count range] | CTA type: [...]

FORMAT 2 ...
FORMAT 3 ...

═══════════════════════════════════════════
💎 CLIENT CONVERSATION GOLD
═══════════════════════════════════════════
Real conversations creative strategists / DTC founders / AI consultants
are having THIS WEEK. The nuance you're not yet in the room for.

CONV 1 — [Source: r/PPC thread / LinkedIn comment / podcast clip]
  Problem (verbatim): "[...]"
  Dominant opinion: [...]
  Dissenting take getting traction: [...]
  Specific client language to mirror: "[...]"
  Under-discussed angle Farrice could own: [...]

CONV 2 ...
[8-12 total split A/B]

═══════════════════════════════════════════
💭 PERSONAL INTEGRATION (3 voice-memo prompts)
═══════════════════════════════════════════
Each prompt connects today's strongest angles to a specific thread
from your story. Pick the one that sparks fastest.

P1 — [memory hook]
   Question: [...]
   Why this prompt: [...]

P2 ...
P3 ...

═══════════════════════════════════════════
🎯 PROSPECT BOOMERANG (1-2 today)
═══════════════════════════════════════════
Specific prospects whose recent activity makes them high-leverage
reciprocity targets if today's post hits adjacent territory.

  • [Name] · [their recent quote, dated] · [how today's angle reciprocates]

═══════════════════════════════════════════
📈 YESTERDAY + CALENDAR CONTEXT
═══════════════════════════════════════════
Yesterday's post: [stats or "no post shipped"]
Today's calendar: [posting-window constraint summary]

═══════════════════════════════════════════
HOW TO REPLY
═══════════════════════════════════════════
Fast path (recommended on busy days):
  Reply to this email with: "Go [#]" + voice memo attachment
  → I auto-trigger /jackpost and ship draft back within 30 minutes

Deep path (for high-conviction posts):
  Open Claude Code → "Run /jackpost on [#] with this raw take: [...]"

Skip path:
  No reply needed. Tomorrow's brief still ships at 7am.
```

---

## Phase 9 — Delivery (Format C: Google Doc + HTML email)

**Actor**: Orchestrator + `gws` (Drive + Gmail) + Gmail MCP fallback

### 9A — Upload deep-dive HTML as a Google Doc

```bash
# Drive create with auto-conversion (HTML → application/vnd.google-apps.document)
DOC_RESPONSE=$(gws drive files create \
  --upload .tmp/zeitgeist/[date]-deep-dive.html \
  --upload-content-type text/html \
  --json '{"name":"Parallax Daily Deep-Dive — [date]","mimeType":"application/vnd.google-apps.document"}')

# Extract doc ID
DOC_ID=$(echo "$DOC_RESPONSE" | python3 -c "import sys,json;print(json.load(sys.stdin)['id'])")
DOC_URL="https://docs.google.com/document/d/$DOC_ID/edit"
```

The doc is in Farrice's Drive. When he opens the link from his Gmail, he's already authenticated. No "anyone with link" sharing needed.

**Optional**: After creation, apply pageless format per Farrice's preference:
```bash
gws docs documents batchUpdate --documentId "$DOC_ID" --json '{
  "requests":[{"updateDocumentStyle":{
    "documentStyle":{"pageSize":{"width":{"magnitude":850,"unit":"PT"},"height":{"magnitude":1100,"unit":"PT"}}},
    "fields":"pageSize"
  }}]
}'
```

(Pageless mode is optional — the doc is readable either way. Skip if it complicates the run.)

### 9B — Send Gmail with HTML body + plain-text fallback + doc link

**Primary path — Gmail MCP** (works with current OAuth scope):
```python
# Pseudocode — actual call uses mcp__claude_ai_Gmail__create_draft
mcp__claude_ai_Gmail__create_draft(
  to=["farrice.cain@gmail.com"],
  subject="Parallax Daily — [3-word punch]",
  body=[plain-text fallback from 8B],
  htmlBody=[short HTML email from 8A — substitute DOC_URL into the deep-dive button href]
)
```

This produces a draft. The cron-runner can either:
- Leave as draft (Day-1 trust-building behavior — user reviews + sends)
- Auto-promote to send via Gmail API once user confirms format works (Day-N onward)

**Alternative — `gws gmail +send`** (requires re-auth with broader Gmail scope):
```bash
gws gmail +send \
  --to farrice.cain@gmail.com \
  --subject "Parallax Daily — [3-word punch]" \
  --body "$(cat .tmp/zeitgeist/[date]-email-fallback.txt)" \
  --html  # if body is HTML
  # Drop --draft when ready to auto-send
```

**Fallback chain**: Gmail MCP → gws (with re-auth) → write `.tmp/zeitgeist/[date]-FAILED-DELIVERY.md` and alert.

### 9C — Logging

Record the doc URL + draft/send ID in `.agent/zeitgeist-runs.jsonl` so Phase 11 reply-loop can reference both artifacts.

---

## Phase 10 — Archive + Log

**Actor**: Orchestrator

1. Copy `.tmp/zeitgeist/[date]-deep-dive.html` → `knowledge/zeitgeist-archive/[date]-deep-dive.html`
2. Save email-body HTML → `knowledge/zeitgeist-archive/[date]-email.html`
3. Append run record to `.agent/zeitgeist-runs.jsonl`:
   ```json
   {
     "date":"...",
     "subject":"...",
     "angles_count":N,
     "sent":true|false,
     "draft_id":"...",
     "doc_id":"...",
     "doc_url":"https://docs.google.com/document/d/.../edit",
     "delivery":"gmail_mcp_draft|gws_send",
     "format_version":"C",
     "gaps":[...],
     "failure_alert":null
   }
   ```
4. After 7am LA delivery, set 90-min watchdog: if Farrice hasn't replied or posted by 9am LA, no action (briefs are decision aids, not obligations).
5. Weekly Sunday: scan archive for trend-pattern lookback. Surface "you flagged X 3 weeks ago — it just hit LinkedIn mainstream" wins to reinforce Lag Advantage.

---

## Phase 11 — Reply-Loop Trigger (when Farrice replies)

**Actor**: Email-watcher cron (separate, every 30 min) + orchestrator

If Farrice replies to today's brief with format `Go [#]` + voice memo:

1. Parse angle # from reply
2. Transcribe voice memo (Whisper via Groq if `GROQ_API_KEY` set, else OpenAI Whisper)
3. Compose `/jackpost` invocation: `--entity [from angle metadata] --raw-take [transcript] --platform linkedin`
4. Run `/jackpost` workflow
5. Email draft post back to Farrice within 30 min
6. He reviews → posts → optionally replies "shipped" to log performance

---

## Failure Modes + Mitigations

| Failure | Mitigation |
|---|---|
| Research dossier returns thin / unverified | Skip thin sections in email — never invent. "Section X had no verified items today." |
| Gmail send fails | Fallback to Gmail MCP draft; alert via `.agent/session-state.md` |
| 2 days miss in a row | Auto-flag in next session-start: "Zeitgeist brief missed [N] days — reschedule or debug?" |
| Personal prompt picks suppression-vein on a heavy day | Sensitivity gate defaults to safe threads when uncertain |
| Crystal Ball drifts speculative | Pre-flight gate: every CB item must have primary URL or it's relabeled SPECULATIVE WATCH |
| Adjacent bridge feels forced | Drop the section for the day rather than ship try-hard pattern matching |
| Format Intel returns generic | Require named creator + post URL + verifiable engagement; otherwise omit |

---

## Output Files (Format C)

```
.tmp/zeitgeist/
  [date]-research-dossier.md     (raw research from Phase 1 — unchanged)
  [date]-deep-dive.html          (full HTML uploaded to Google Drive in Phase 9A)
  [date]-email.html              (short HTML email body sent in Phase 9B)
  [date]-email-fallback.txt      (plain-text fallback for non-HTML clients)

knowledge/zeitgeist-archive/
  [date]-deep-dive.html          (archived deep-dive)
  [date]-email.html              (archived email body)

.agent/
  zeitgeist-runs.jsonl           (run log with doc_id + draft_id + format_version)
```

---

## Quality Gate (run before Gmail send)

| Check | Pass condition |
|---|---|
| Verification | Every claim in email + doc is VERIFIED or labeled |
| Voice fit | Farrice's Parallax lens (multi-angle / S&C / EDM / biracial / build-in-public) is doing real work, not decoration |
| Specificity | Every angle cites a real entity / quote / number |
| Personal prompts | Draw on actual memory threads, not generic |
| Format Intel | Each triple cites named creator + URL + engagement signal |
| **Email skim time** | **HTML email body is < 3-min skim on phone.** If longer, move detail to deep-dive doc, not the email. |
| Deep-dive doc depth | Doc has full reasoning + sources + verbatim quotes. Doc is the *reference*, email is the *decision*. |
| Deep-dive doc accessibility | Doc URL works when clicked from Farrice's Gmail. (Owned by him → no extra sharing needed.) |
| Sensitivity | Personal prompts respect rotation + sensitivity gates |
| HTML email mobile rendering | Inline CSS only (Gmail strips `<style>`). Max-width 640px. System font stack. Cards with generous padding. |

If any check fails → fix or omit that section. Never ship low-quality fill.

---

## Format C Rationale (preserved for context)

**Why Format C** (adopted 2026-05-04 after Day-1 brief feedback):
- The original Format A was 668 lines of plain text with ASCII separators. Rendered as a wall of cramped paragraphs on Gmail mobile. Hard to skim, hard to make decisions from.
- Format C separates **decision** (email, ~3 min skim, HTML cards) from **depth** (Google Doc, ~10 min deep read, full reasoning).
- The morning email weighs almost nothing. Depth is one tap away when needed.
- Decision-fatigue stays low. The user can *commit to the daily habit* because the skim is fast.

**When NOT to use Format C** (rare):
- If Farrice ever reports the deep-dive link gets ignored or clicked too rarely to justify producing it, fall back to Format A (single self-contained email) but with cleaner HTML hierarchy.
- If Gmail MCP becomes unavailable AND gws scope re-auth blocks autonomous send, ship a Markdown file to project + alert.
