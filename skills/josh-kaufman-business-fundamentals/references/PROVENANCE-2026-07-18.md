# Provenance — josh-kaufman-business-fundamentals repair

Ground truth: two claude.ai export conversations preserving the full Merlin AI
transcript of "Entrepreneurship Expert: How To Build A $1m Business Without Hard
Work!" (Josh Kaufman, YouTube `kxLmeUIXXtU`). Both were absent from the live
filesystem (`.tmp/claude-export/` cleaned up, no `extractions/josh-kaufman*`) and
were recovered from the archive:

```
_archive/claude-export-2026-07-01.tar.gz  (332,779,255 bytes)
  → claude-export/normalized/conversations/531b46ea-2cf4-4726-ae10-86dd963118d5.md  (147,314 bytes, extracted)
  → claude-export/normalized/conversations/f8acd07a-a3a1-46f3-9ebd-8bd0c14aa31b.md  (154,769 bytes, extracted)
```

Recovery command: `tar -xzf _archive/claude-export-2026-07-01.tar.gz -C <scratch> claude-export/normalized/conversations/531b46ea-...md claude-export/normalized/conversations/f8acd07a-...md`. File index confirming these paths belong to this skill: `_active/claude-export/harvest/gap3-input.json` (entry `"skill": "josh-kaufman-business-fundamentals", "agent": "josh-kaufman"`).

## Anchor → source table (new Anti-Patterns section, genius.md)

| Anchor (bullet in genius.md § Anti-Patterns) | Source file | Location | Quote verified verbatim |
|---|---|---|---|
| Playing Business Before Doing Business | 531b46ea-...md | ~line 1020–1027 (transcript ~39:35–39:48) | "the first thing I need to do is pick a logo and buy my business cards... that's the signaling parts of business, it's playing a role" — yes |
| The Two-Year Launch-Day Gamble | 531b46ea-...md | ~line 1047–1051 (transcript ~40:32–40:47) | "the worst possible way to go about things is raise millions of dollars of venture capital and build up this whole thing only to have no one buy it at the end" — yes (minor connective words elided, marked by "..." per standard quotation practice; core clause verbatim) |
| Selling the Feature Instead of the Benefit | 531b46ea-...md | ~line 1718–1725 (transcript ~67:46–68:03) | "are making the mistake of focusing on the features of their product"; "an iPod has one gigabyte high drive hard drive and a thousand songs in your pocket" — yes |
| Reading Competition as a Stop Sign | 531b46ea-...md | ~line 1899–1905 (transcript ~74:57–75:20) | "discovered there is already someone solving that problem... and then they go no, there's no money to be made there" — yes |
| Mistaking Total Novelty for Safety | 531b46ea-...md | ~line 1927–1960 (transcript ~76:39–77:37) | "nobody's ever done this before can actually... be a bad sign"; "people didn't want to buy a $110,000 alternative to walking or riding a bike" — yes (dollar figure flagged UNCONFIRMED in source-ledger.md, see below) |
| Bolting On Features to Signal Value | 531b46ea-...md | ~line 2432–2443 (transcript ~96:42–97:06) | "we think because we've added more stuff people are going to value it more, therefore they're going to pay for it more... but that's not necessarily how the world works... you're going to screw up so many things by adding those features" — yes |
| Letting Management Become Bureaucracy | 531b46ea-...md | ~line 1827–1829 (transcript ~72:14–72:21) | "the flip side of some of the common failure cases of bureaucracy paperwork busy work" — yes |

## Anchor → source table (claim-by-claim verification underlying source-ledger.md)

See `source-ledger.md` for the full table (existing genius.md/SKILL.md patterns cross-checked against the same transcript, including the Lawrence & Nohria drive taxonomy at ~44:14–44:50, the Des Traynor credit-card quote at ~37:55–38:13, the Marc Andreessen Iron Law quote at ~75:33–75:46, the Pfeffer & Fong MBA study at ~12:12–13:53, and the two flagged gaps: the Segway dollar figure and the BrewDog reference in the pre-existing Counter-Signal pattern, neither of which appears anywhere in either transcript file).

## Recognition-test language

Added to `genius.md` § "How to Use This Skill (Model Calibration)": "would Kaufman recognize this as someone who actually reduced a business to its five moving, arithmetic-grade parts and validated it with real money — or as someone reciting Personal MBA vocabulary?" — original synthesis, not a sourced claim, written to satisfy the `recognition_test` heartbeat check against this expert's actual documented voice (plain-spoken, arithmetic-first, allergic to credential-signaling — all directly evidenced in the transcript, e.g. the MBA-as-purchased-interview and doing-vs-playing-business material above).
