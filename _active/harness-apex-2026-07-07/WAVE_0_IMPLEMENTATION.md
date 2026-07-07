# Wave 0 Implementation — COS Intelligence Brief

**Status:** SCAFFOLDED & INTEGRATED (2026-07-07)
**What's built:** Research loop infrastructure + question engine v2 + brief integration
**What's ready:** 3 architecture decisions for Farrice

---

## What Was Built

### 1. **Interests Registry** (`.agent/cos/interests.json`)
- 6 categories: marketing, copywriting, creative strategy, content strategy, AI, personal interests
- Each with 4 focus areas (e.g. "authority positioning for expertise businesses" under marketing)
- Used by research loop to filter what matters to Farrice's world
- **Status:** Live ✓

### 2. **Research Loop Script** (`execution/world_pulse_research.py`)
- `python3 execution/world_pulse_research.py run` → generates `.agent/cos/world/YYYY-MM-DD.md`
- Renders 5-8 items: title + what happened + why it matters + sources + optional action
- **Sourcing discipline:** No training-memory inference; every item must carry URL/quote
- **Honest Receipt:** logs which sources were consulted
- **Status:** Scaffolded (sample items) — awaiting sourcing strategy decision

### 3. **Question Engine v2** (`execution/cos_prep.py` - `generate_questions_v2()`)
- **Archetype rotation** (daily, deterministic via hash):
  1. **Decision-forcing:** pit two life threads against each other ("JJ vs. Jen — which deserves more focus?")
  2. **Connection-surfacing:** find non-obvious link between threads ("How are Health and Mindset actually connected?")
  3. **Life:** introspection tied to life section + world-item ("Health: what from today's pulse reframes this?")
- **Beats generic questions** ("Any updates?" is now a lint failure)
- **Status:** Live ✓

### 4. **Brief Integration** (`execution/cos_prep.py` - `render_brief()`)
- Morning brief now includes `## 🌍 World Pulse` section (top 5 items + link to full pulse)
- Calls world pulse research loop during prep
- Falls back gracefully if pulse file doesn't exist
- **Status:** Live ✓

### 5. **Test Run** (2026-07-07)
- Brief generation successful with sample world-pulse items
- Questions rotated to "decision-forcing" (JJ vs. Jen & Family) ✓
- World pulse section renders correctly with 3 sourced items
- Next: Farrice rates 3 consecutive mornings on "mind flow" (1-10 scale)

---

## Three Architecture Decisions Needed

### **Decision 1: Research Sourcing Strategy**

**Question:** How should the research loop gather items each night?

**Option A: Gemini Deep Research (Primary) + Perplexity (Fallback)**
- Gemini has structured research with citations
- Perplexity fallback if Gemini rate-limited
- Cost: Gemini $10/mo ceiling (part of existing budget), Perplexity $30/mo fallback
- Discipline: Extract sources from results; no hallucinations

**Option B: Perplexity Search Only (Simpler)**
- Single API, no fallback complexity
- Cost: $30/mo
- Risk: Less structured than Gemini; need manual filtering

**Option C: Hybrid — API + Manual Weekly Curation**
- Automated loop runs 3×/week; Farrice hand-curates 2×/week based on his own reading
- Combines machine + human signal
- Cost: $15/mo savings (fewer API calls)
- Downside: Requires discipline

**Recommendation:** Option A (Gemini primary). You've already got the budget; structured research produces better sourced items.

---

### **Decision 2: Research Cadence**

**Question:** How often should world pulse research run?

**Option A: Nightly (07:00, before cos_prep 06:45 + actual running 07:00)**
- Every morning has fresh items
- Cost: ~$0.50/day Gemini (rough)
- Requires: scheduled `launchd` job or manual `python3 execution/world_pulse_research.py run` in `/cos` workflow

**Option B: 3×/week (Mon/Wed/Fri)**
- Reduces API cost + decision fatigue
- Same items reused on off-days (fresher than the 2026-07-07 brief which reused generic examples)
- Cost: ~$10/mo Gemini
- Downside: Items are 24-48h stale

**Option C: Weekly (Sunday night, 1 comprehensive pulse for the week)**
- One deep research pass instead of 7 shallow ones
- Cost: Lowest (~$2/mo)
- Downside: Items are 3-6 days old by Friday

**Recommendation:** Option A (nightly). You want "tapped in and tuned into the world"; stale items defeat the purpose. The $15/mo is noise against your $5K incumbency goal.

---

### **Decision 3: Question Engine Archetype Rotation**

**Question:** Should the rotation be daily (what we built), or some other rhythm?

**Current (Daily Rotation):**
- Each day fires one archetype deterministically
- Day 1 = decision-forcing, Day 2 = connection-surfacing, Day 3 = life, Day 4 = repeat
- Pro: Maximum variety; prevents repetition
- Con: Might feel jarring if a thread needs repeated attention

**Alternative 1: Weekly Blocks**
- Mon-Tue-Wed = decision-forcing, Thu-Fri-Sat-Sun = life + connection (less forced decisions)
- Pro: Gives threads breathing room
- Con: Less variety within a week

**Alternative 2: Context-Aware (not yet built)**
- Detect high-urgency goals (revenue-5k-incumbency = 90d, very active)
- Automatically surface decision-forcing questions when deadlines loom
- Pro: Most responsive to life state
- Con: Requires more logic; maybe too much automation

**Recommendation:** Keep daily rotation (what we built). It's simple, deterministic, and forces creative variety in your thinking. If you hate it after 3 days, we switch to weekly blocks.

---

## Next Steps (In Order)

### **Immediate (This Week)**
1. **Pick the 3 architecture decisions** above (or tell me to go with recommendations)
2. **Build the real research loop** (swap out sample items for Gemini/Perplexity sourcing)
3. **Wire scheduled loop** (launchd `com.antigravity.world-pulse-nightly` at 07:00)

### **Verification (Week 2)**
- Run `/cos` each morning for 3 consecutive days
- Rate each brief on "mind flow" (1-10 scale) — Farrice's felt verdict
- Adjust question archetypes or sourcing if needed
- Update `.agent/session-state.md` with verdict

### **Finalize (Week 3)**
- Lock-in the research strategy + archetype rotation
- Move world-pulse research to the evolution_orchestrator.py daily auto run (so it's deterministic, not manual)
- Finalize Wave 0 verification

---

## Files Changed

| File | Change |
|------|--------|
| `.agent/cos/interests.json` | NEW: interests registry |
| `execution/world_pulse_research.py` | NEW: research loop script |
| `execution/cos_prep.py` | UPDATED: added world-pulse gathering, question engine v2, brief rendering |
| `.agent/cos/world/2026-07-07.md` | NEW: today's sample pulse file |

## Session Receipt

**Effort:** 1.5 sessions (scaffolding + integration)
**Cost:** $0 (no APIs called; sample data only)
**Blocker:** 3 architecture decisions + real sourcing implementation

## Running Manually

```bash
# Generate world pulse for today (currently sample data)
python3 execution/world_pulse_research.py run

# Generate this morning's brief with latest pulse
python3 execution/cos_prep.py prep

# View the brief
cat .agent/cos/briefs/2026-07-07.md

# Check pulse status
python3 execution/world_pulse_research.py status
```
