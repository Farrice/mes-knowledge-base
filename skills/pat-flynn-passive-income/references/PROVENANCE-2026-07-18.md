# Provenance — Pat Flynn: Passive Income Architecture repair

Anchor → source file + location. Every VERIFIED row was confirmed by `python3 tarfile` extraction of the named member from `_archive/claude-export-2026-07-01.tar.gz` into the session scratchpad, followed by `grep -n` against the raw text (not memory, not inference).

| Anchor (in `genius.md`) | Source file (archive member) | Size | Location |
|---|---|---|---|
| "the biggest mistake... what should I sell" | `fa99b805-bab2-48ca-909f-455969b0cd69.md` | 183,789 B | timestamp 7:45-7:52 |
| "high commission... not because it's actually helpful" | `fa99b805-bab2-48ca-909f-455969b0cd69.md` | 183,789 B | timestamp 12:29-12:41 |
| "kill all bugs... didn't sell at all" / "cockroach spray... ant spray" | `fa99b805-bab2-48ca-909f-455969b0cd69.md` | 183,789 B | timestamp 11:09-11:37 |
| "serves everybody... serving nobody" | `fa99b805-bab2-48ca-909f-455969b0cd69.md` | 183,789 B | timestamp 22:08-22:12 |
| "$7,908.55" / "FBI is going to come and knock on my door" | `fa99b805-bab2-48ca-909f-455969b0cd69.md` | 183,789 B | timestamp 5:19-5:59 |
| "this is an awesome life but it's not my awesome life" | `fa99b805-bab2-48ca-909f-455969b0cd69.md` | 183,789 B | timestamp 46:37-46:40 |
| "serve first... pays you back in one way or another over time" | `fa99b805-bab2-48ca-909f-455969b0cd69.md` | 183,789 B | timestamp 12:42-12:49 |
| "hurt people hurt people" | `fa99b805-bab2-48ca-909f-455969b0cd69.md` | 183,789 B | timestamp 20:10 (recurs `dfab4324...` timestamp 58:02-58:10) |
| "can't read the label when you're inside the bottle" | `fa99b805-bab2-48ca-909f-455969b0cd69.md` | 183,789 B | timestamp 31:25-31:27 |
| "consume just in case" / "shiny object syndrome" | `c2e8b7ad-2146-4f5e-962e-82e43d315220.md` | 99,713 B | timestamp 24:01-24:30 |
| "knowledge hoarding" (overlapping content-bloat theme) | `dfab4324-a28d-4ef2-b534-4ff89aa5257f.md` | 135,110 B | timestamp 22:02-22:08 |
| "a funnel is very soulless... remove the heart" | `90a84bdf-b478-4882-aba5-5ae3d471cbd5.md` | 74,958 B | timestamp 12:33-12:51 |
| "Hyatt he's like a leader of leaders" (supports mastermind claim, LIKELY not full verbatim of pre-existing sentence) | `fa99b805-bab2-48ca-909f-455969b0cd69.md` | 183,789 B | timestamp 30:09 |

Locating method (repeatable): `_active/claude-export/index.json` gives conversation `id` + `title` for all 21 Pat Flynn-titled entries; `python3 tarfile` opened `_archive/claude-export-2026-07-01.tar.gz`, matched `member.name.split('/')[-1] == f"{id}.md"`, and `tf.extractfile(m).read()` pulled the actual bytes (sizes above = `len(data)`, confirmed non-zero before any claim was made). No member was assumed absent without this direct check.

Full claim-by-claim table with VERIFIED/LIKELY/UNCONFIRMED labels: `references/source-ledger.md`.
