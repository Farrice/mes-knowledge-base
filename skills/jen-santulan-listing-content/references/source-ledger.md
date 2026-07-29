# Jen Santulan Listing Content — Source Ledger

> This is a **client skill**, not a public-expert extraction. There is no `extractions/` file for Jen Santulan — confirmed via `ls extractions/ | grep -i santulan` (zero matches) and a repo-wide `grep -ril santulan` (2026-07-17), which surfaces only `_active/jen-listings/`, `_active/jen-santulan/`, and the skill's own files. Ground truth for this skill is the client project directory, not the extraction pipeline. Every claim below traces to a file actually opened and read during this repair pass (2026-07-17), or is flagged UNCONFIRMED where it isn't.

---

## Sources Consulted (file-level)

| Source | Label | Note |
|---|---|---|
| `skills/jen-santulan-listing-content/SKILL.md` | VERIFIED | Skill package's own frontmatter/routing file; read directly, unchanged this pass |
| `skills/jen-santulan-listing-content/genius.md` | VERIFIED | Voice DNA file; read directly, repaired this pass (see PROVENANCE.md) |
| `skills/jen-santulan-listing-content/PROMPT.md` | VERIFIED | Original master prompt, superseded by workflow 01 per SKILL.md; not modified |
| `skills/jen-santulan-listing-content/workflows/01-03-*.md` | VERIFIED | Passing `workflow_contracts` check already — not modified this pass |
| `_active/jen-listings/CLAUDE.md` | VERIFIED | Client project CLAUDE.md; git-tracked since 2026-05-28; read directly |
| `_active/jen-listings/6853-willis-van-nuys/6853-willis-briefing.md` | VERIFIED | Dated 2026-07-02 in-file; hardened via "multi-lens generation + adversarial clarity verification" per its own header; read directly |
| `_active/jen-listings/6853-willis-van-nuys/6853-willis-SHOOT-SHEET.md` | VERIFIED | Companion shoot sheet to the briefing, same 2026-07-02 session; read directly |
| `_active/jen-listings/6853-willis-van-nuys/proof-claims-ledger.md` | VERIFIED | Dated 2026-07-02 in-file; itself a claim-by-claim VERIFIED/LIKELY/UNCONFIRMED ledger sourced from Zillow/CRMLS, Highrises, Freddie Mac PMMS, Redfin/Zillow/Movoto, walkscore.com, Metro/NBC LA, GreatSchools via read-only Playwright + WebSearch ($0, no paid API calls per its own header) |
| `_active/jen-listings/04-deliverables/6853-willis-persuasive-reels-v2.metadata.json` | VERIFIED | Git-committed 2026-07-07; contains a verbatim user-feedback note quoted in genius.md §7 |
| `_active/jen-listings/5421-bothwell-tarzana/listing-package.md` | VERIFIED | Read directly; carries its own internal MLS-sourced spec table labeled VERIFIED at file end |
| `strategy_briefs/Strategy_Brief_First_Time_Home_Buyers_in_SoCal.md` | VERIFIED | 266-line dossier dated "February 5, 2026" in-file; cites US Census, CA Dept of Finance, ACS 2024, NAR Buyer Survey, Comstock's Magazine, r/FirstTimeHomeBuyer — read directly (in full, not excerpted) |
| `_active/jen-listings/deliverables/sfv-fthb-lead-copy/proof-claims-ledger.md` | VERIFIED | FTHB program names (HOP80/HOP120/LIPA/Greenline/CalHFA) each individually labeled VERIFIED via LAHD/LACDA/LA County DCBA program data, Gemini Search-grounding dated 2026-06-02 in-file |

---

## Claims and Labels (claim-by-claim)

| Claim | Label | Source / Reasoning |
|---|---|---|
| Voice test: "Would Jen say this to her best friend over coffee?" | VERIFIED | `_active/jen-listings/CLAUDE.md` §Voice Test — exact phrase |
| "Let's [action]" is Jen's signature closer, never "DM me"/"Link in bio" | VERIFIED | `CLAUDE.md` Anti-Patterns + `6853-willis-briefing.md` (2026-07-02): "spoken closer stays "let's go see it"", "the DM ask lives only in caption/Story" |
| Golden reference: objection named in ≤8 words, ADU as bonus not the pitch | VERIFIED | `6853-willis-van-nuys/6853-willis-SHOOT-SHEET.md` line 2, exact phrase, 2026-07-02 |
| "No stairs" answers the aging-parent + young-kid objection in line one | VERIFIED | `6853-willis-briefing.md` §2, Hook 4 rationale, exact phrase |
| "We make good money but still can't afford. It's humiliating." (pain script, genius.md §3) | VERIFIED | `strategy_briefs/Strategy_Brief_First_Time_Home_Buyers_in_SoCal.md` line 73, exact verbatim quote (there attributed "Common sentiment pattern") |
| "Hoping my lottery number comes up... feels defeating when funds run out in 11 days" (pain script, genius.md §3) | VERIFIED | Same brief, line 71, exact verbatim quote (there attributed to a buyer quoted in Comstock's Magazine) |
| "Stuck renting into retirement" (pain script, genius.md §3) | VERIFIED | Same brief, line 65 — appears as "Missing the window entirely; stuck renting into retirement" (Primary Fear row) |
| "I'll never own in LA at this rate" (pain script, genius.md §3) | **UNCONFIRMED** | Searched the full 266-line strategy brief for this phrase and near-variants ("never own," "priced out," "LA at this rate") — not found verbatim. The brief's closest line is "Frustrated, hopeless, feel 'priced out forever'" (line 64), which is a different sentence. This line in genius.md §3 predates this repair pass and was NOT added by this repair — flagging here per the "no quote you cannot find gets an anchor" rule rather than silently leaving it uncited. Recommend Farrice/Jen confirm or swap for the verified "priced out forever" phrasing in a future pass. |
| FTHB Permission Mechanic structure (NAME → FLIP → INVITE) | LIKELY | House-authored framework (genius.md §8) applied TO Jen's actual hooks — not a quote FROM Jen or a third-party source. The underlying moves it describes (naming a hesitation, then flipping it with one proof point) are directly confirmed in `6853-willis-briefing.md`'s 5 final hooks; the three-beat NAME/FLIP/INVITE label itself is skill-authored structure, not verbatim Jen language. |
| Instagram handle @realestatewithjing | **UNCONFIRMED** | Appears in `SKILL.md` frontmatter and `CLAUDE.md`. No file in `_active/jen-listings/` or elsewhere in this repair pass independently confirms the exact handle against a live Instagram fetch — no browser check was run this pass (out of scope for a heartbeat repair). Flag before any public-facing claim leans on the handle string. |
| Show-Not-Tell table pairs (genius.md §5, e.g. "26 homes behind the gate, almost zero turnover in three years") | LIKELY | Illustrative craft examples authored for the skill in Jen's register; do not trace to one verbatim source file. Read as house-authored pattern demonstrations, not direct quotes from a real listing. |
| FTHB programs: HOP80, HOP120, LIPA, Greenline, CalHFA, MyHome | VERIFIED | `_active/jen-listings/deliverables/sfv-fthb-lead-copy/proof-claims-ledger.md` — each individually VERIFIED via LACDA/LAHD/LA County DCBA program data, Gemini Search-grounding dated 2026-06-02 |
| "$200K price cut" is a real caught overclaim (anti-pattern example) | VERIFIED (as CONTRADICTED claim) | `6853-willis-van-nuys/proof-claims-ledger.md` (2026-07-02): "No reduction in public record — do NOT claim unless CRMLS shows a real price-change event" |
| Metro G Line Van Nuys station closed, do not claim as operational (anti-pattern example) | VERIFIED | Same ledger: "Metro G Line Van Nuys station CLOSED for reconstruction until ~Dec 2027" / "do not film/claim as operational" |
| Kester Ave Elementary 9/10 likely not the assigned school (anti-pattern example) | VERIFIED | Same ledger: "Kester Ave Elementary 9/10 | VERIFIED (rating) — likely NOT assigned to this address; do not claim" |
| "V1 was too safe, tame, price-history-led, and not persuasive enough" (anti-pattern example) | VERIFIED | `6853-willis-persuasive-reels-v2.metadata.json` "notes" field, exact verbatim quote, git-committed 2026-07-07 |
| SFV sub-neighborhood list (Canoga Park, Sherman Oaks, Encino, Lake Balboa, Tarzana, Van Nuys, Reseda, West Hills, Woodland Hills) | VERIFIED | Cross-referenced against live project files: Van Nuys (`6853-willis-briefing.md`), Tarzana (`5421-bothwell-tarzana/listing-package.md`); all are real, named San Fernando Valley sub-neighborhoods |
| "Pencils out around $850 per square foot" (anti-pattern example, replacing "stunning"/"gorgeous" with a number) | VERIFIED | `5421-bothwell-tarzana/listing-package.md` line 205, exact verbatim quote |

---

## Explicitly Absent Sources

- **No `extractions/` file for Jen Santulan.** Verified via `ls extractions/ | grep -i santulan` (zero results) and a repo-wide `grep -ril santulan` (2026-07-17) that surfaces only client-project and skill-package paths. This is expected and correct: per the skill's own frontmatter, Jen is Farrice's wife's real-estate practice, not a public-expert extraction subject.
- **No independent third-party (Instagram, press, MLS live-fetch) verification was run this pass.** All labels above are file-to-file (repo-internal) verification only. Where the skill content makes a claim that would require an external fetch to confirm (the handle, live MLS status), it is labeled UNCONFIRMED rather than silently assumed.
