"""Verification checks 1, 3, 4, 5 for execution/outlier_radar.py (spec section 'Verification')."""
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "execution"))

RADAR_DIR = ROOT / ".agent" / "outlier-radar"
RECEIPTS = sorted((RADAR_DIR / "receipts").glob("shortform-marketing-*.json"))
PACK = RADAR_DIR / "packs" / "shortform-marketing" / "latest.json"
TRANSCRIPTS = sorted((RADAR_DIR / "transcripts").glob("*.txt"))

results = []


def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))


# --- Check 1: 3-channel niche, two runs, TTL skip, receipts, snapshots grow ---
receipts = [json.loads(p.read_text()) for p in RECEIPTS]
check("1a: >=2 run receipts exist", len(receipts) >= 2, f"{len(receipts)} receipts")
run1, run2 = receipts[0], receipts[1]
check("1b: run1 fetched 3 channels, 0 skipped",
      run1["channels_fetched"] == 3 and run1["channels_skipped_ttl"] == 0,
      f"fetched={run1['channels_fetched']} skipped={run1['channels_skipped_ttl']}")
check("1c: run2 TTL-skipped all 3 fresh channels",
      run2["channels_skipped_ttl"] == 3 and run2["channels_fetched"] == 0,
      f"fetched={run2['channels_fetched']} skipped={run2['channels_skipped_ttl']}")
conn = sqlite3.connect(RADAR_DIR / "radar.db")
snap_count = conn.execute("SELECT COUNT(*) FROM snapshots").fetchone()[0]
runs_in_db = conn.execute("SELECT COUNT(*) FROM runs WHERE status != 'running'").fetchone()[0]
video_count = conn.execute("SELECT COUNT(*) FROM videos").fetchone()[0]
multi_snap = conn.execute(
    "SELECT COUNT(*) FROM (SELECT video_id FROM snapshots GROUP BY video_id HAVING COUNT(*) >= 2)"
).fetchone()[0]
check("1d: snapshots grow across runs", snap_count > run1["snapshots_added"],
      f"total={snap_count} vs run1={run1['snapshots_added']}; {multi_snap} videos have 2+ snapshots")
check("1e: runs table recorded all finished runs", runs_in_db == len(receipts), f"db={runs_in_db}")

# --- Check 3: transcripts only for flagged outliers, per-run count <= cap ---
pack = json.loads(PACK.read_text())
transcript_ids = {p.stem for p in TRANSCRIPTS}
db_video_ids = {row[0] for row in conn.execute("SELECT video_id FROM videos").fetchall()}
per_run = [r["transcripts_written"] for r in receipts]
check("3a: every per-run transcript count <= cap 10", all(n <= 10 for n in per_run), f"per-run={per_run}")
check("3b: transcript file total == sum of per-run writes (no other writer)",
      len(TRANSCRIPTS) == sum(per_run), f"files={len(TRANSCRIPTS)} sum={sum(per_run)}")
check("3c: all transcript ids are known sampled videos", transcript_ids <= db_video_ids)
check("3d: current watchlist (flagged) all have transcripts",
      set(pack["watchlist_adds"]) <= transcript_ids,
      f"watchlist={len(pack['watchlist_adds'])}")
flagged_now = {r["video_id"] for r in pack["ranked_videos"] if r["winner_line_status"] == "above_winner_line"}
check("3e: transcript_path set only on flagged records in pack",
      all((r["transcript_path"] is None) or (r["video_id"] in set(pack["watchlist_adds"]))
          for r in pack["ranked_videos"]))

# --- Check 4: pack validates against the contract ---
import outlier_radar  # noqa: E402
problems = outlier_radar.validate_pack(pack)
check("4a: validate_pack(latest) has no problems", not problems, "; ".join(problems) or "clean")
# sabotage both directions: a broken pack must fail
bad = dict(pack)
bad.pop("leaderboard")
bad["status"] = "wat"
check("4b: validate_pack flags a sabotaged pack", len(outlier_radar.validate_pack(bad)) >= 2,
      f"{len(outlier_radar.validate_pack(bad))} problems flagged")

# --- Check 5: no apify on any network path ---
src = (ROOT / "execution" / "outlier_radar.py").read_text()
import_hits = re.findall(r"^\s*(?:import|from)\s+\S*apify\S*", src, re.MULTILINE)
check("5a: no apify import statements in outlier_radar.py", not import_hits, str(import_hits))
check("5b: importing outlier_radar loads no apify module",
      not any("apify" in name for name in sys.modules),
      f"{[m for m in sys.modules if 'apify' in m]}")
usage_hits = re.findall(r"apify_client\s*[.(]", src)
check("5c: no apify_client usage in outlier_radar.py", not usage_hits, str(usage_hits))

# --- Bonus sanity on pack content ---
records = pack["ranked_videos"]
enriched = [r for r in records if r["transcript_path"]]
check("sanity: velocity_vpd_7d non-null after 2+ snapshots",
      any(r["velocity_vpd_7d"] is not None for r in records),
      f"{sum(1 for r in records if r['velocity_vpd_7d'] is not None)}/{len(records)} non-null")
check("sanity: enriched records carry likes/comments",
      any(r["likes"] is not None for r in enriched))
check("sanity: enriched hook_text comes from transcript (differs from title)",
      any(r["hook_text"] != r["title"] for r in enriched))
check("sanity: confidence present on all records",
      all(r["confidence"] in ("high", "medium", "low") for r in records))

conn.close()
failed = [r for r in results if not r[1]]
for name, ok, detail in results:
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
print(f"\n{len(results) - len(failed)}/{len(results)} passed")
sys.exit(1 if failed else 0)
