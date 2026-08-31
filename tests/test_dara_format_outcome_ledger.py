from __future__ import annotations

import argparse
import json
import tempfile
import unittest
from pathlib import Path

from execution import dara_format_outcome_ledger as ledger


def observation_args(**overrides):
    values = {
        "format_id": "founder-ad",
        "format_label": "Founder's Ad",
        "source_prior_tier": "S",
        "campaign_id": "hp-angle-map",
        "asset_id": "F01",
        "message_id": "unmade-belief",
        "category": "supplement",
        "persona": "translation-burdened founder",
        "channel": "linkedin",
        "funnel_stage": "recognition",
        "notes": "fixture",
        "spend": 100.0,
        "currency": "USD",
        "hook_rate": None,
        "hook_rate_definition": "three-second views / impressions",
        "hook_events": 300,
        "hook_opportunities": 1000,
        "conversion_event": "qualified-dm",
        "conversion_count": 2,
        "conversion_value": 0.0,
        "conversion_evidence_state": "directional",
        "attribution_window": "7d",
        "evidence": "fixtures/f01-receipt.json",
        "fatigue_state": "fresh",
        "fatigue_window": "days-1-3",
        "frequency": 1.2,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def decision_args(**overrides):
    values = {
        "format_id": "founder-ad",
        "format_label": "Founder's Ad",
        "source_prior_tier": "S",
        "campaign_id": "hp-angle-map",
        "asset_id": "F01",
        "message_id": "unmade-belief",
        "category": "supplement",
        "persona": "translation-burdened founder",
        "channel": "linkedin",
        "funnel_stage": "recognition",
        "notes": "fixture",
        "decision": "promote",
        "decision_reason": "Qualified replies plus stable hook rate cleared the precommitted gate.",
        "decision_evidence": "fixtures/f01-decision.md",
        "decided_by": "Farrice",
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class DaraFormatOutcomeLedgerTests(unittest.TestCase):
    def test_weighted_scoreboard_and_explicit_decision(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.jsonl"
            first = ledger.build_observation(observation_args())
            second = ledger.build_observation(
                observation_args(
                    spend=200,
                    hook_events=400,
                    hook_opportunities=2000,
                    conversion_count=1,
                    fatigue_state="watch",
                )
            )
            decision = ledger.build_decision(decision_args())
            for event in (first, second, decision):
                ledger.append_event(path, event)

            rows = ledger.summarize(ledger.read_events(path), "format-category-persona")
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["spend"], 300.0)
            self.assertEqual(rows[0]["spend_by_currency"], {"USD": 300.0})
            self.assertEqual(rows[0]["weighted_hook_rate"], round(700 / 3000, 6))
            self.assertEqual(rows[0]["conversion_count"], 3)
            self.assertEqual(rows[0]["latest_fatigue_state"], "watch")
            self.assertEqual(rows[0]["latest_decision"], "promote")

    def test_hook_rate_requires_denominator(self):
        with self.assertRaisesRegex(ledger.LedgerError, "hook_rate requires hook_opportunities"):
            ledger.build_observation(
                observation_args(hook_events=None, hook_opportunities=None, hook_rate=0.3)
            )

    def test_conversion_claim_requires_receipt(self):
        with self.assertRaisesRegex(ledger.LedgerError, "requires --evidence"):
            ledger.build_observation(observation_args(evidence=""))

    def test_high_hook_rate_does_not_auto_promote(self):
        event = ledger.build_observation(
            observation_args(hook_events=900, hook_opportunities=1000, conversion_count=0,
                             conversion_evidence_state="none", evidence="")
        )
        rows = ledger.summarize([event], "format")
        self.assertEqual(rows[0]["weighted_hook_rate"], 0.9)
        self.assertEqual(rows[0]["latest_decision"], "")

    def test_mixed_currency_spend_is_not_collapsed(self):
        usd = ledger.build_observation(observation_args(spend=100, currency="USD"))
        eur = ledger.build_observation(observation_args(spend=80, currency="EUR"))
        row = ledger.summarize([usd, eur], "format")[0]
        self.assertIsNone(row["spend"])
        self.assertEqual(row["currency"], "MIXED")
        self.assertEqual(row["spend_by_currency"], {"EUR": 80.0, "USD": 100.0})

    def test_verify_rejects_tampered_conversion_without_receipt(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.jsonl"
            event = ledger.build_observation(observation_args())
            event["evidence"] = ""
            path.write_text(json.dumps(event) + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ledger.LedgerError, "requires a receipt"):
                ledger.read_events(path)


if __name__ == "__main__":
    unittest.main()
