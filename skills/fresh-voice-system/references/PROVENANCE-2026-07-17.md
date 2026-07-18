# fresh-voice-system — Repair Provenance (Wave 3, Lane 3, 2026-07-17)

Anchor → source file + location, for everything added to `genius.md` in this pass.
Full labeled ledger: `references/source-ledger.md`.

| Anchor (in genius.md) | Source File | Location | Label |
|---|---|---|---|
| "Here are 5 ways to improve your decision-making..." / "In today's fast-paced business environment..." / "Leadership isn't about having all the answers..." | `_active/linkedin-launch/04-content-os/voice-captures/genspark-20-post-serial-arc.md` | Post 3 "The Expensive Mistake" (source lines ~59-61) | VERIFIED |
| "Just be authentic. Worst advice in the history of personal branding." | same file | Post 12 "The Voice Myth" (source lines 285-286) | VERIFIED |
| "Because that's too casual. I need to sound professional." | same file | Post 3 (source line 64) | VERIFIED |
| "I help entrepreneurs scale their businesses. DM me if you're interested." | same file | Post 7 "The Subtle Signal" (source line 158) | VERIFIED |
| "I tried it. Wrote like I actually talk. Posted it. Got 14 likes and one person saying it was 'unprofessional.'" | same file | Post 4 "The Part Nobody Sees" (source line 80) | VERIFIED |
| Primary source commit/date (2026-03-10, `4da54d14e`) | git history | `git log --follow -- _active/linkedin-launch/04-content-os/voice-captures/genspark-20-post-serial-arc.md` | VERIFIED |
| "Implement these tips and watch your engagement soar! ... Drop "LINKEDIN" in the comments for a free guide!" | `skills/fresh-voice-system/references/exemplars.md` | Anti-Exemplar section, line 58 | VERIFIED |
| "My work happens in the room, Farrice. It's too nuanced for a post." | same file | Exemplar 2 "The Coach Who Refused to Write", line 30 | VERIFIED |
| "Her depth was the problem. She couldn't simplify what she knew because she'd spent two decades learning it was never simple." | `skills/fresh-voice-system/genius.md` (pre-existing, untouched) | "The Paradox Reveal" worked example | VERIFIED (already in the skill; re-cited, not re-sourced externally) |
| exemplars.md commit/date (2026-04-02, `e7ae19898`) | git history | `git log --follow -- skills/fresh-voice-system/references/exemplars.md` | VERIFIED |
| exemplars.md line count (65 lines) | filesystem | `wc -l skills/fresh-voice-system/references/exemplars.md` | VERIFIED |
| quality-rubric.md score anchors (4/7/10) | `skills/fresh-voice-system/references/quality-rubric.md` | table header row | VERIFIED (file exists, header read directly; body has a pre-existing formatting corruption in one cell — not fixed, out of scope) |
| `agents/robert-mack/AGENT.md`, `skills/robert-mack-comedy-writing/` exist | filesystem | `ls agents/robert-mack/`, `ls skills/robert-mack-comedy-writing/` | VERIFIED (existence only — content not re-audited) |
| `.agent/workflows/voice-first-content.md` exists | filesystem | `ls .agent/workflows/voice-first-content.md` | VERIFIED |
| `_active/linkedin-launch/04-content-os/arcs/` exists | filesystem | `ls _active/linkedin-launch/04-content-os/arcs/` | VERIFIED |

## Note on the source file's quote formatting

`genspark-20-post-serial-arc.md` carries a formatting artifact throughout: quoted
dialogue opens with a literal `\"` and frequently closes with a bare `\` (no closing
quote mark) — apparent residue of an improperly unescaped JSON string when the file
was originally saved. Confirmed by a raw Python read (not the rendered Markdown view).
Every quote cited above is the exact English wording from the file with only that
stray backslash normalized away — no words added, removed, or reordered.
