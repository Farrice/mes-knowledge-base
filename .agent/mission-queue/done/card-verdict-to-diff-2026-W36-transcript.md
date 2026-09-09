The write guard blocked me — main is integration-only. This is the golden rule. The proposed diffs file needs to be written in a worktree lane.

I've completed the analysis and have 5 concrete proposals ready. To write them:

**What I found (5 repeating patterns):**

1. **System/harness work scored on Expert Standard** — "general" and "harness-architect" rows at 6.0. The rubric's Expert Standard question doesn't apply to control-plane work. Fix: add N/A rule.

2. **Dual-pen content logs fake skill strings** — "Luke Iha + Farrice VOICE-CARD" doesn't match a skill directory. Fix: document finalize hygiene (primary skill + layered notes).

3. **Client content missing ENGINE authority** — Jen rows under `jen-santulan-listing-conten` scored low; her ENGINE-V2.md realism gate, formats, and look aren't logged as the skill authority. Fix: log `skill_authority` in chain_runner.py.

4. **`skill: general` antipattern** — No such skill exists. Fix: call it an automatic 5 on Expert Standard.

5. **Client vetoes not loaded into Scrapes BRAND LOCK** — `feedback_jen-hands-off-photo-look.md` and `feedback_jen-visual-palette-no-orange.md` record her vetoes, but the designer phase doesn't see ENGINE-V2.md §§3,6,7. Fix: wire ENGINE into Step 0 load order.

**Next step:** Enter a worktree lane to write the file, or you can copy these proposals into your own session. The proposals are ready — just need a write surface.
