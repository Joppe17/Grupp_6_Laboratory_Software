from logic.upgrades.base_upgrade import Upgrade

AUTO_CLICK_MULTIPLIER_CAP = 20

class AutoClicker(Upgrade):
    name = "Monkey Finger"
    description = "Auto-Click 1/s per level"
    base_cost = 500
    tab = "Auto Clicks"

    def apply_effect(self):
        self.state.kps += 1
