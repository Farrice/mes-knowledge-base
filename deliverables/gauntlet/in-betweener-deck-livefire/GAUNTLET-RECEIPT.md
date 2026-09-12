# GAUNTLET RECEIPT — in-betweener-deck-livefire

- artifact: deliverables/IN-BETWEENER_pitch_deck.html
- mode: Precision Polish
- bar: self (no external comparison deck supplied for this live-fire drill — judged against production-grade floor per CLAUDE.md craft gate: no overflow/cutoff, readable type at 375, sufficient contrast)
- preserve: —
- never: —
- opened: 2026-09-11T21:41:07-07:00

## Round 1 — VISUAL VERIFIED
- desktop: /Users/farricecain/Google Antigravity/.claude/worktrees/job-visibility-fix/deliverables/gauntlet/in-betweener-deck-livefire/round-1/desktop.png
- tablet: /Users/farricecain/Google Antigravity/.claude/worktrees/job-visibility-fix/deliverables/gauntlet/in-betweener-deck-livefire/round-1/tablet.png
- mobile: /Users/farricecain/Google Antigravity/.claude/worktrees/job-visibility-fix/deliverables/gauntlet/in-betweener-deck-livefire/round-1/mobile.png
- verdict: INCOMPARABLE · gap: No external comparison deck was supplied for this live-fire drill (bar=self); judged against production floor instead of blind A/B
- evidence: Real-scroll screenshots at desktop/tablet/mobile (hero, mid-content, close) show no horizontal overflow (scrollWidth==clientWidth at 375 and 768), readable serif/sans/mono type and good contrast at all 3 breakpoints, no cut-off content. One tooling finding: the attached fullPage:true PNGs duplicate the hero/logline block (verified false-positive — DOM has exactly 1 hero, 1 logline via querySelectorAll; a real-scroll screenshot at the same scrollY shows correct distinct content), so the attached round-1 PNGs are not a faithful single-frame representation of the page even though VISUAL VERIFIED; future rounds on 100vh-section pages should sample real scroll positions, not rely on fullPage capture. Minor cosmetic: gold scrollbar thumb (::-webkit-scrollbar-thumb) renders as a thin gold sliver at the right edge in every shot — intentional brand styling, not a defect.
- preserve: cinematic dark/gold palette, serif display type, generous negative space

## Close
- verdict: PASS
- surviving risks: (1) Attached round-1 fullPage PNGs contain a screenshot-capture artifact — hero/logline block renders twice in the stitched full-page image despite the DOM holding each section once (verified via querySelectorAll + a real-scroll cross-check at the same scrollY); treat this deck's fullPage captures as unreliable for future rounds, use real-scroll viewport shots instead. (2) 20/59 .reveal IntersectionObserver elements did not flip to .visible under a fast synthetic scroll pass — low-confidence, likely a test-harness artifact (scroll too fast for the observer to fire) rather than a live hazard, but worth a human confirming with normal mouse-wheel scroll speed. (3) Gold scrollbar thumb (::-webkit-scrollbar-thumb) shows as a thin vertical sliver at the frame edge in every screenshot — intentional brand styling, cosmetic only, not a defect. No overflow, cutoff, or contrast failures found at 1440/768/375 (scrollWidth==clientWidth confirmed at 768 and 375; hero, mid-content, and closing sections all read cleanly at all three breakpoints).
- repairs used: 0/2
- closed: 2026-09-11T21:51:01-07:00
