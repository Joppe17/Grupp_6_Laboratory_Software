from logic.upgrades.base_upgrade import Upgrade

class X2_Multiplier(Upgrade):
    name = "X2 Click Multiplier"
    description = "Every click is doubled"
    base_cost = 1000
    tab = "Click Upgrades"

    def apply_effect(self):
        self.state.permanent_click_multiplier *= 2 