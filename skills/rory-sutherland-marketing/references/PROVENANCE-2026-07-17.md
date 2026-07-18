# PROVENANCE — rory-sutherland-marketing (Wave 3 Batch 2)

Anchor-by-anchor table for every quote/claim added or verified during this repair pass. Full narrative version (with LIKELY/UNCONFIRMED reasoning) lives in `references/source-ledger.md`; this file is the flat lookup table the adversarial verifier can check line-by-line.

## Convenience cache

`_source-extract/` in this output folder contains the raw `.md` conversation files I extracted from `_archive/claude-export-2026-07-01.tar.gz` this pass (via `tar -xzOf`), so the verifier does not need to unpack the 332MB archive to spot-check quotes. Canonical source path for citation purposes is always the archive path in the table below, not this cache.

| ID | Cache file | Canonical archive path |
|---|---|---|
| S2 | `_source-extract/how-human-behaviour-defies-logic.md` | `claude-export/normalized/conversations/af891b20-121c-4aa1-9ed7-856e5b23535f.md` |
| S3 | `_source-extract/22381-marketing-advice.md` | `claude-export/normalized/conversations/b48c2624-c6be-4b2f-b104-74325e915fc3.md` |
| S4 | `_source-extract/playbook-pt1-a.md` | `claude-export/normalized/conversations/cc8137fe-a600-4dec-8841-44c571bdd6be.md` |
| S5 | `_source-extract/playbook-pt1-b.md` | `claude-export/normalized/conversations/b25fb13a-bc76-4e1f-bbe2-ebaaee5088ad.md` |
| S6 | `_source-extract/luxury-brands.md` | `claude-export/normalized/conversations/aefce78d-4655-48fb-bc34-6088badeb260.md` |
| S7a/b/c | `_source-extract/playbook-pt2-a.md` / `-pt2-b.md` / `-pt3.md` | `6454e30a-...md` / `239d5849-...md` / `64042c51-...md` |
| S1 | `_source-extract/knowledge-project-interview.md` (copy) | `extractions/rory-sutherland/transcript.txt` (canonical) |

## Anti-Patterns in genius.md (all VERIFIED against S1)

| # | Anti-pattern title | Quote | Verified via |
|---|---|---|---|
| 1 | The Finance-Fetish Trap | "Finance people fetishize costsaving and automation." | `grep -qF` exact match in `extractions/rory-sutherland/transcript.txt` |
| 2 | The Transmission-Model Fallacy | "What they're not thinking about is what goes on behind the eyeball once that message is received." | `grep -qF` exact match, same file |
| 3 | Calibrating to the Angriest Person in the Room | "you cannot calibrate humor uh to the level of the angriest, most humorous person in the room." | `grep -qF` exact match, same file |
| 4 | Mistaking Cheap Signals for Real Demand | "cheap media enabled cheap signaling." | `grep -qF` exact match, same file |
| 5 | Chasing Efficiency Without Asking What Was Lost | "we got obsessed with the efficiency gains" / "what was it that old media did that new media doesn't do very well" | `grep -qF` exact match (both substrings), same file |
| 6 | Display-Over-Utility Feature Creep | "I don't really understand from a utility point of view why so much effort goes into the camera." | `grep -qF` exact match, same file |
| 7 | Killing Real Utility for Novelty | "I think the loss of the physical keyboard in your portable phone has actually been a productivity disaster." | `grep -qF` exact match, same file |
| 8 | Spending to Fix What Nobody Feels | "You could spend an awful lot of money trying to improve something that seems important but which nobody deep down ever cares about." | `grep -qF` exact match, same file (opening line of the transcript) |

All 8 quotes were verified with a scripted `grep -qF` pass (exact substring match, case-sensitive) against `extractions/rory-sutherland/transcript.txt` on 2026-07-17 before being written into `genius.md`. Full command + output is reproducible: `grep -F "<quote>" extractions/rory-sutherland/transcript.txt`.

## Key genius.md pattern claims spot-checked this pass (see source-ledger.md for the complete claim list)

| Pattern/Item | Anchor | Status |
|---|---|---|
| Doorman Fallacy (mechanism) | S1: "Finance people fetishize costsaving and automation"; S4/S5: assistant-generated prompt titles reference the term (not confirmed as Sutherland's own words in the checked portion) | LIKELY |
| Human Proxy Heuristic | S4/S5: "the vendor and the door is answered... by, for example, a female vicar" | VERIFIED (mechanism; S1 has an independent secondhand-car version) |
| Transaction Utility Lens (beach beer) | S4/S5: "you and your best friend are lying on a beach somewhere... your friend says to you, 'I'm off to [blank] to buy a beer...'" | VERIFIED |
| Brand Quake Recognition | S1: "...create a what there's one American agency calls it a brand quake" | VERIFIED |
| Fat-Tail Opportunity Spotter | S4/S5: "it's Jeff Bezos's point about in business... in baseball you can only score four, in business you can score a thousand" | VERIFIED |
| Reverse Benchmarking (mechanism) | S2, timestamp 80:44: "reverse benchmarking. Okay, which is if the whole of the market goes in one direction... Dove was a beautiful example" | VERIFIED (mechanism); Guidara/Eleven Madison Park case study = UNCONFIRMED, zero hits across S1-S7 |
| The Paceometer (term) | S2: "Paceometer" ×3 occurrences | VERIFIED |
| Two-Way Door (Bezos framing) | Not located in S1-S7; the one confirmed Bezos quote (S4/S5) is the fat-tail baseball line, unrelated to reversibility | UNCONFIRMED |
| The Overground Effect | "Overground," "Silverlink," "Tube map" — zero hits across S1-S7 | UNCONFIRMED |
| Churchill Reframe | S2: "Churchill" ×4, clustered at timestamps 62:xx-63:xx | VERIFIED (presence + placement; not re-quoted character-for-character this pass) |
| The Horsepower Move | S2: "horsepower" ×5 at timestamps 36:09-36:28; "Watt" ×3 | VERIFIED |
| The Scout Bee Ratio | S2, timestamp 59:38: "reaction is to get rid of the scout bees" | VERIFIED |
| Too-Good-To-Be-True (Nespresso/biryani) | S3, timestamp 28:29 "Nespresso launched the virtuo machine"; timestamp 32:28 "Indian food biryanis" | VERIFIED |
| Bargain-or-Treat (KFC) | S3, timestamps 4:37/5:08: "overheard some people at a KFC" / "people go to KFC for two reasons" | VERIFIED |
| Oblique Delivery (Reagan) | S2, timestamps 51:55-53:07: "Reagan second term. He's 78 years..." | VERIFIED |
| Behavioral Detective (John Lewis Tunbridge Wells) | S3 ×5 mentions incl. timestamp 48:43 "the John Lewis tumbridge Wells story" | VERIFIED |

## Workflow files — Output Schema additions

All 10 Output Schema sections added this pass (`addictive-perception-content.md`, `consumer-perception-alchemy.md`, `insight-perception-sprint.md`, `perception-dominance-campaign.md`, `perception-dopamine-engine.md`, `perception-metric-reframe.md`, `positioning-perception-siege.md`, `price-frame-architect.md`, `reverse-benchmarking-audit.md`, `sin-of-omission-audit.md`) are original synthesis work by this repair pass, not sourced from Sutherland material — they formalize each workflow's ALREADY-STATED deliverable (see each file's pre-existing "**Output**:" line or Phase 4 table) into the house `## Output Schema` + Quality Checklist format. No new Sutherland claims were introduced; each schema is bespoke to its own workflow's phases (verified non-boilerplate: no two schemas share more than the section headers).

## Note on live-tree drift during this pass

At dispatch, `audit-rory-sutherland-marketing.txt` reported 15/20 workflow files missing Output Schema. Mid-repair, `git log` showed a concurrent commit (`3942d10c1`, 2026-07-17 19:37:42, "chore(session): end-session commit gate") had already landed fixes for 5 of those 15 files directly on `main` (a different conductor/worker touched the same skill). Re-running the auditor against the live tree at that point showed only 10 files still failing. Per the envelope's read-only-git instruction, this drift was not investigated further or blocked on — this repair pass fixed the 10 that were still actually failing at time of writing, using the current (already-partially-repaired) file content as the base for the unaffected files. The conductor should reconcile; no destructive action was taken on the other 5.
