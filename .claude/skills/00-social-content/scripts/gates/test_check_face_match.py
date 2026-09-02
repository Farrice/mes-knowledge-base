# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=10.0.0", "numpy>=1.26.0", "opencv-python-headless>=4.8.0"]
# ///
"""Unit tests for check_face_match.py — FACE-MATCH (resolved hero face must match the headshot).

Tests the contract gate (hero-face-with-headshot detection) + the deterministic similarity
score's separating power (a face matches itself, differs from a synthetic other). No hardcoded
slug. Run: uv run test_check_face_match.py
"""
import sys
import unittest
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from check_face_match import (  # noqa: E402
    hero_face_with_headshot,
    identity_score,
    cv2,
)

R_HEADSHOT_HERO = (
    "## ② Per-block breakdown\n"
    "**Hero portrait photo** · the hero face fills the frame\n"
    "  - hero_face_identity: brand-headshot (a headshot exists at .../simon-pic.jpg)\n")
R_INVENTED = (
    "## ② Per-block breakdown\n"
    "**Image / photo / hero block:**\n"
    "  - hero_face_identity: brand-headshot — ... The hero_face_identity for this template: "
    "invented — the scene is generated freely per post\n")
R_NO_FACE = (
    "## ② Per-block breakdown\n"
    "**Display word** · the dominant headline, HTML overlay\n"
    "  - no face, no portrait, no person in this layout\n")


class ContractGateTests(unittest.TestCase):
    def test_headshot_hero_triggers(self):
        self.assertTrue(hero_face_with_headshot(R_HEADSHOT_HERO))

    def test_invented_face_suppresses(self):  # overlay-cover editorial scene
        self.assertFalse(hero_face_with_headshot(R_INVENTED))

    def test_no_face_does_not_trigger(self):
        self.assertFalse(hero_face_with_headshot(R_NO_FACE))


@unittest.skipIf(cv2 is None, "opencv unavailable")
class IdentityScoreTests(unittest.TestCase):
    def _face(self, seed):
        rng = np.random.default_rng(seed)
        # A structured synthetic "face": gradients + two dark eye blobs + a mouth — enough
        # structure for the Sobel/correlation reads to separate identities deterministically.
        f = np.full((120, 120, 3), 180, np.uint8)
        f[35:50, 30:50] = 30
        f[35:50, 70:90] = 30
        f[85:95, 45:75] = 50
        f[:, :, 0] = (f[:, :, 0].astype(int) + int(rng.integers(0, 40))).clip(0, 255)
        return f

    def test_face_matches_itself(self):
        f = self._face(1)
        self.assertGreaterEqual(identity_score(f, f)["combined"], 0.95)

    def test_different_faces_score_lower(self):
        a = self._face(1)
        b = np.full((120, 120, 3), 180, np.uint8)  # a blank, featureless "invented" face
        self.assertLess(identity_score(a, b)["combined"], identity_score(a, a)["combined"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
