"""
this file contains the base for current and future upgrades.
"""

class Upgrade:
    name = ""
    description = ""
    base_cost = 0
    tab = ""

    def __init__(self, state):
        self.state = state
        self.times_bought = 0

    def get_cost(self):
        return int(self.base_cost * (2 ** self.times_bought))
    
    def can_buy(self):
        return self.state.score >= self.get_cost()
    
    def purchase(self):
        if self.can_buy():
            self.state.score -= self.get_cost()
            self.times_bought += 1
            self.apply_effect()
    
    def apply_effect(self):
        raise NotImplementedError