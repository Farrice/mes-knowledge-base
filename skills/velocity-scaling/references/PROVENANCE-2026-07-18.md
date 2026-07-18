# Provenance — velocity-scaling repair (Danny Yeung)

Ground truth: `extractions/danny-yeung/transcript.txt` (86,386 bytes, `wc -c`
confirmed). No `_archive/claude-export-2026-07-01.tar.gz` scan was needed —
local source was found and sufficient.

| Anchor (genius.md location) | Quote | Source file + how confirmed |
|---|---|---|
| Anti-Patterns item 1 | "we don't want to do anything short-term" / "these are minimum threeyear deals because if it's not it becomes too short term and you both sides doesn't benefit from it" | `extractions/danny-yeung/transcript.txt` — Python substring match (`quote in text`) confirmed True |
| Anti-Patterns item 2 | "the problem is once you do due diligence, it doesn't work" | `extractions/danny-yeung/transcript.txt` — substring match confirmed True |
| Anti-Patterns item 3 | "I never tell someone, hey, just do this blah blah blah" / "I always try to provide a lot of context" | `extractions/danny-yeung/transcript.txt` — substring match confirmed True |
| Anti-Patterns item 4 | "I think what if we put in retail into this now, it also loses focus" | `extractions/danny-yeung/transcript.txt` — substring match confirmed True |
| Anti-Patterns item 5 | "letting someone free as early as possible to find the next thing is way better than to keep them" / "on the ship" | `extractions/danny-yeung/transcript.txt` — substring match confirmed True |
| Anti-Patterns item 6 | "I don't care how great the formulation is, but it also needs to taste good" | `extractions/danny-yeung/transcript.txt` — substring match confirmed True |
| Anti-Patterns item 7 | "I'll text you at like 12:00 a.m., 2 a.m., 6:00 a.m., doesn't matter" | `extractions/danny-yeung/transcript.txt` — substring match confirmed True |
| "How to Use This Skill (Model Calibration)" section | Structure/phrasing modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 (read directly this session); content (Danny's operator-blunt texture, due-diligence-free posture) is original synthesis anchored to the Anti-Patterns quotes above | `skills/ben-watkins-storytelling/genius.md` (structural model) + `extractions/danny-yeung/transcript.txt` (content anchor) |

All 7 quotes verified by direct Python `in` substring match against the raw
transcript file this session (not read-then-paraphrased from memory) —
see command run and True/True/... output during repair.
