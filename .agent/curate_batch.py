#!/usr/bin/env python3
"""One-shot curation of the 2026-08-21 mass-approved distill batch (Farrice-directed).

41 proposals were approved in a scripted sub-second burst at 18:07:49Z — not the
human gate. Farrice directed this session to work the queue with judgment.
KEEP = specific + matches lived doctrine. DEMOTE = jargon blobs, paraphrases of
standing binding rules, dupe families, or new blocking gates (Compass violation).
Reversible per-item: `python3 execution/memory_review.py approve <fr_id>`.
"""
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

KEEP = {"fr_50a85ddb793eae82", "fr_3b405c4a25bab656", "fr_6eade214e8fb7a0b",
        "fr_5c36173e64c07cfe", "fr_f57414a4f802716f", "fr_0e6ba58324ae5b8a",
        "fr_19c908568d7771d8", "fr_f945d33a6789237f", "fr_a1853f26f96841e7",
        "fr_b897f1efda0b5633"}

REASONS = {
    "fr_fe3f71a3a246a916": "jargon, single-cluster artifact (SHADOW layer)",
    "fr_1dd8cae088c9abce": "dupe of fr_f57414a4 (authority-ledger theme)",
    "fr_defebd63d0da7e94": "paraphrase of standing five-input/proof-first doctrine",
    "fr_e5254df8617a928c": "workflow-local (trailer treatments) — belongs in that workflow doc",
    "fr_ef06734d45ab0f0b": "score-gaming meta-rule, no operational content",
    "fr_4869a91342dbce38": "over-specific cluster artifact (metabolic plateaus)",
    "fr_054d993f4d69cecf": "job-local (nightly mission-brief) — belongs in that job",
    "fr_81d2e18310d067cd": "covered by lane machinery + closeout spine docs",
    "fr_9d6fbd428070962d": "paraphrase of standing /park + finisher rule",
    "fr_e900437c4495e8b2": "vague (Constraint-First) — no operational content",
    "fr_a6da02ac25eceacd": "blob-era generic; dupe of fr_25aff573 + standing INTENT BRIEF rule",
    "fr_b40053c9e6e3490a": "paraphrase of standing two-rejected-takes/reground rule",
    "fr_48ffb353bde9ef32": "dupe of fr_0e6ba583 (kept: local-first is the actionable form)",
    "fr_3f39f74e15bc144f": "intent-alignment dupe family (kept fr_3b405c4a)",
    "fr_5f5d67f9ac6dcae9": "intent-alignment dupe family",
    "fr_25aff573c3c34837": "dupe of fr_a6da02ac / standing rules",
    "fr_99db08819f89e75f": "cluster artifact w/ project jargon (God Agent memory already standing)",
    "fr_3a9f7e71a88494da": "intent-alignment dupe family",
    "fr_7d3a14d9deb7c3a3": "covered by standing Blind Bar Protocol (binding)",
    "fr_758d058760b1471c": "dupe of fr_3b405c4a (kept)",
    "fr_625513cb3833a69e": "intent-alignment dupe family",
    "fr_e6dbc614374c5062": "routing bindings own this; not a memory",
    "fr_8d58c7d91a1a3546": "proposes a BLOCKING gate — Compass doctrine violation",
    "fr_27ed39257651b98e": "verification-spine paraphrase; 'mandate' framing",
    "fr_e960d5ed5b38d5d8": "the Chain already canon; paraphrase",
    "fr_6aa9375e4cd0fafb": "VOICE-CARD standing rule paraphrase",
    "fr_2feb18d09de6345a": "pipeline jargon; dupe of fr_e450dcae/fr_8b3b21df",
    "fr_e450dcae2f0dfd7b": "pipeline jargon dupe",
    "fr_7da1de58179d3533": "dupe of fr_0e6ba583 (kept)",
    "fr_8b3b21df16dfe6da": "pipeline jargon dupe",
    "fr_a00dd33e10659b5e": "intent-alignment dupe family; workflow-local",
}


def main() -> int:
    con = sqlite3.connect(str(ROOT / ".memory" / "sovereign.db"), timeout=10)
    con.row_factory = sqlite3.Row
    rows = con.execute(
        "SELECT id, judge_score, promoted_memory_id, proposed_content FROM flagged_review "
        "WHERE status='approved' AND reviewed_at >= '2026-08-21T18:07'"
    ).fetchall()
    now = datetime.now(timezone.utc).isoformat()
    receipt = [
        "# Memory curation receipt — 2026-08-21 (Farrice-directed review of mass-approved batch)",
        "",
        "Context: 41 distill proposals were mass-approved by a scripted burst at 18:07:49Z "
        "(NOT the human gate). Farrice directed this session to work the review queue with "
        "judgment. Verdicts below; every DEMOTE is reversible: "
        "`python3 execution/memory_review.py approve <fr_id>`.",
        "",
    ]
    kept = demoted = 0
    for r in rows:
        fid, mem_id = r["id"], r["promoted_memory_id"]
        head = " ".join((r["proposed_content"] or "").split())[:110]
        if fid in KEEP:
            kept += 1
            receipt.append(f"- KEEP  {fid} [{r['judge_score']}] mem={mem_id} — {head}")
        else:
            reason = REASONS.get(fid, "generic auto-distill; no operational content")
            con.execute("UPDATE flagged_review SET status='rejected', reviewed_at=? WHERE id=?", (now, fid))
            if mem_id:
                con.execute("DELETE FROM memories WHERE id=?", (mem_id,))
            demoted += 1
            receipt.append(f"- DEMOTE {fid} [{r['judge_score']}] mem={mem_id} — {reason} — {head}")
    con.commit()
    sem = con.execute("SELECT COUNT(*) FROM memories WHERE tier='semantic'").fetchone()[0]
    pend = con.execute("SELECT COUNT(*) FROM flagged_review WHERE status='pending'").fetchone()[0]
    con.close()
    receipt += ["", f"Result: kept {kept}, demoted {demoted}. Semantic tier now {sem} rows. Pending queue: {pend}."]
    (ROOT / ".agent" / "memory-curation-2026-08-21.md").write_text("\n".join(receipt), encoding="utf-8")
    print(f"kept={kept} demoted={demoted} semantic_now={sem} pending={pend}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
