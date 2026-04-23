import sys
import os
import unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import pygame
from ui.banana import FlyingBanana
from logic.game_state import GameState

class TestGameState(unittest.TestCase):
    def test__initial_score(self):
        state = GameState()
        assert state.score == 0

    def test_initial_multiplier(self):
        state = GameState()
        assert state.click_multiplier == 1

    def test_bonus_activation(self):
        state = GameState()
        state.click_multiplier = 3
        state.score += 1 * state.click_multiplier
        assert state.score == 3


class TestBanana(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pygame.init()
        cls.screen = pygame.display.set_mode((800, 600))
    
    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def test_starts_inactive(self):
        state = GameState()
        banana = FlyingBanana(self.screen, state)
        assert banana.active == False

    def test_spawn(self):
        state = GameState()
        banana = FlyingBanana(self.screen, state)
        banana.spawn()
        assert banana.active == True
        assert 60 <= banana.x <= 740
        assert banana.y == -80

    def test_bonus_activation_on_click(self):
        state = GameState()
        banana = FlyingBanana(self.screen, state)
        banana.spawn()
        click_event = pygame.event.Event(
            pygame.MOUSEBUTTONDOWN, pos=(banana.x + 10, banana.y + 10))
        banana.handle_event(click_event)
        assert state.click_multiplier == 3
        assert banana.bonus_active == True

    def test_bonus_expires(self):
        state = GameState()
        banana = FlyingBanana(self.screen, state)
        banana.spawn()
        click_event = pygame.event.Event(
            pygame.MOUSEBUTTONDOWN, pos=(banana.x + 10, banana.y + 10))
        banana.handle_event(click_event)
        assert state.click_multiplier == 3
        assert banana.bonus_active == True

        # Simulerar tid för att bonusen ska gå ut
        dt = FlyingBanana.duration + 1
        banana.update(dt)
        assert state.click_multiplier == 1
        assert banana.bonus_active == False
