import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

from review_miner import score_trigger_event  # noqa: E402


def test_specific_intolerable_moment_scores_high():
    text = "At 2:00 one night I woke up because my dog was chewing his paws until they bled."
    score, reasons = score_trigger_event(text)
    assert score >= 45
    assert any("specific" in reason for reason in reasons)


def test_generic_benefit_is_not_a_trigger_event():
    text = "This food has great ingredients and gives dogs healthy skin."
    score, _ = score_trigger_event(text)
    assert score < 45
