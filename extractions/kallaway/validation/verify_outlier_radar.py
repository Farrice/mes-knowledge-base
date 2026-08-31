#!/usr/bin/env python3
"""Offline contract and sabotage tests for the reconciled Outlier Radar."""

import copy
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "execution"))

import outlier_radar  # noqa: E402

SNAPSHOT = Path(__file__).parent / "live" / "latest.json"
results = []


def check(name, condition, detail=""):
    results.append((name, bool(condition), detail))


def upgraded_snapshot():
    """Lift the preserved v1 live receipt into v2 without rewriting history."""
    pack = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    pack.update(
        pack_version=outlier_radar.PACK_VERSION,
        evidence_class="PUBLIC_PROXY",
        owned_corpus_size=12,
        data_maturity_state="HYBRID",
    )
    for record in pack["ranked_videos"]:
        record.update(
            evidence_class="PUBLIC_PROXY",
            cohort_role="UNCLASSIFIED",
            engagement_rate=None,
            signal_hygiene="REVIEW",
            rejection_reasons=["engagement_unavailable"],
        )
        outlier_radar.apply_signal_hygiene(record)
    return pack


pack = upgraded_snapshot()
problems = outlier_radar.validate_pack(pack)
check("v2 upgraded live snapshot validates", not problems, "; ".join(problems))
check("public producer never upgrades evidence", pack["evidence_class"] == "PUBLIC_PROXY")
check(
    "producer leaves cohort judgment unclassified",
    all(row["cohort_role"] == "UNCLASSIFIED" for row in pack["ranked_videos"]),
)

check("maturity: undeclared", outlier_radar.data_maturity_state(None) == "UNDECLARED")
check("maturity: cold start", outlier_radar.data_maturity_state(9) == "COLD_START")
check("maturity: hybrid", outlier_radar.data_maturity_state(12) == "HYBRID")
check("maturity: owned learning", outlier_radar.data_maturity_state(20) == "OWNED_LEARNING")

low = {"views": 1000, "likes": 10, "comments": 0}
outlier_radar.apply_signal_hygiene(low)
check(
    "2 percent floor rejects low engagement",
    low["signal_hygiene"] == "REJECT"
    and low["rejection_reasons"] == ["engagement_below_2_percent"],
)

high = {"views": 1000, "likes": 25, "comments": 0}
outlier_radar.apply_signal_hygiene(high)
check(
    "2 percent floor passes high engagement",
    high["signal_hygiene"] == "PASS" and high["rejection_reasons"] == [],
)

missing = {"views": 1000, "likes": None, "comments": None}
outlier_radar.apply_signal_hygiene(missing)
check(
    "missing engagement stays reviewable",
    missing["signal_hygiene"] == "REVIEW"
    and missing["rejection_reasons"] == ["engagement_unavailable"],
)

bad = copy.deepcopy(pack)
bad.pop("leaderboard")
bad["ranked_videos"][0]["cohort_role"] = "INVENTED"
bad_problems = outlier_radar.validate_pack(bad)
check("sabotage: missing leaderboard rejected", any("leaderboard" in item for item in bad_problems))
check("sabotage: invented cohort rejected", any("cohort_role" in item for item in bad_problems))

source = (ROOT / "execution" / "outlier_radar.py").read_text(encoding="utf-8")
check(
    "no Apify import path",
    not re.findall(r"^\s*(?:import|from)\s+\S*apify\S*", source, re.MULTILINE),
)
check(
    "interop preserves evidence fields",
    all(
        token in source
        for token in (
            '\"evidence_class\": record[\"evidence_class\"]',
            '\"cohort_role\": record[\"cohort_role\"]',
            '\"signal_hygiene\": record[\"signal_hygiene\"]',
        )
    ),
)

failed = [row for row in results if not row[1]]
for name, ok, detail in results:
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))
print(f"\n{len(results) - len(failed)}/{len(results)} passed")
raise SystemExit(1 if failed else 0)
