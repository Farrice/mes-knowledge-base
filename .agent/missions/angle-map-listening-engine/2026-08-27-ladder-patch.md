# Angle Map Listening Engine — Social Ladder Patch (2026-08-27)

## Decision: Path A — Accept LIKELY, Document Manual URL Check

**Status:** Implemented  
**Timestamp:** 2026-08-27 (session continuation)  
**Change:** AUTOMATION_PROMPT.md lines 104–110 updated

### What Changed

**Before:**
- Rung 1: Apify (Reddit actors for verified buyer verbatim)
- Rung 2: research.py (Gemini Deep Research + Perplexity)
- Rung 3: Native $0 floor

**After:**
- Rung 1: research.py (Gemini Deep Research + Perplexity)
- Rung 2: Native $0 floor
- Manual URL-check step documented as standing workflow (≤30s per source, before any VERIFIED receipt ships)

### Why

Apify is already retired (BINDING 2026-08-27). The engine was falling back to research.py anyway, producing LIKELY-grade quotes. Rather than hold a broken ladder in code, we now:
1. Accept LIKELY as the engine output (honest)
2. Document the human review step explicitly (requirement, not hidden friction)
3. Keep the engine running (no stall)
4. Flag this as temporary (ladder needs redesign for longer-term scaling)

### Caveat

Every externally-facing receipt that claims buyer verbatim now carries the caveat: "Human URL verified for accuracy before use." This is a gate, not a problem — it ensures no invented quotes ship.

### Next: Ladder Redesign (Future Task)

Once the Reddit/social market stabilizes on a new tool (Apify replacement or alternative), revisit the ladder to pull the manual URL-check step back into automation. For now, it's the floor for data integrity.

---

**Approved by:** Implicit (Path A chosen via continuation instructions)  
**Documented by:** Session continuation 2026-08-27
