import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from logic.game_state import GameState
from logic.upgrades.auto_monkey_punch import MonkeyPunch


class TestMonkeyPunch(unittest.TestCase):
    def setUp(self):
        self.state = GameState()
        self.upgrade = MonkeyPunch(self.state)

    def test_apply_effect_increase_kps_by_5(self):
        start_kps = self.state.kps

        self.upgrade.apply_effect()

        self.assertEqual(self.state.kps, start_kps + 5)


    def test_apply_effect_twice_increases_kps_by_10(self):
        start_kps = self.state.kps

        self.upgrade.apply_effect()
        self.upgrade.apply_effect()

        self.assertEqual(self.state.kps, start_kps + 10)


if __name__ == "__main__":
    unittest.main()