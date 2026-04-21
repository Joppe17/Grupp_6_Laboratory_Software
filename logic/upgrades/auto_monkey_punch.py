from logic.upgrades.base_upgrade import Upgrade

class MonkeyPunch(Upgrade):
    name = "Monkey Punch"
    description = "Auto-Click 5/s per level"
    base_cost = 3000
    tab = "Auto Clicks"

    def apply_effect(self):
        self.state.kps += 5