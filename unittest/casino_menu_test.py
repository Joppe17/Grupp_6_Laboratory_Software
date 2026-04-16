import unittest
from unittest.mock import patch
import pygame

from ui.casino_start_menu import CasinoStartMenu


class TestCasinoStartMenu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        pygame.font.init()
        cls.screen = pygame.display.set_mode((800, 600))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def setUp(self):
        self.menu = CasinoStartMenu(self.screen)

    def test_menu_is_created(self):
        self.assertIsNotNone(self.menu)

    def test_panel_rect_exists(self):
        self.assertIsNotNone(self.menu.panel_rect)
        self.assertTrue(isinstance(self.menu.panel_rect, pygame.Rect))

    def test_three_buttons_exist(self):
        self.assertEqual(len(self.menu.buttons), 3)

    def test_button_labels_are_correct(self):
        labels = [button["label"] for button in self.menu.buttons]
        self.assertIn("Blackjack", labels)
        self.assertIn("Slots", labels)
        self.assertIn("Roulette", labels)

    def test_blackjack_button_click_calls_action(self):
        blackjack_button = self.menu.buttons[0]

        with patch.object(self.menu, "start_blackjack") as mock_action:
            blackjack_button["action"] = self.menu.start_blackjack

            event = pygame.event.Event(
                pygame.MOUSEBUTTONDOWN,
                {"pos": blackjack_button["rect"].center, "button": 1}
            )

            self.menu.handle_event(event)
            mock_action.assert_called_once()

    def test_slots_button_click_calls_action(self):
        slots_button = self.menu.buttons[1]

        with patch.object(self.menu, "start_slots") as mock_action:
            slots_button["action"] = self.menu.start_slots

            event = pygame.event.Event(
                pygame.MOUSEBUTTONDOWN,
                {"pos": slots_button["rect"].center, "button": 1}
            )

            self.menu.handle_event(event)
            mock_action.assert_called_once()

    def test_roulette_button_click_calls_action(self):
        roulette_button = self.menu.buttons[2]

        with patch.object(self.menu, "start_roulette") as mock_action:
            roulette_button["action"] = self.menu.start_roulette

            event = pygame.event.Event(
                pygame.MOUSEBUTTONDOWN,
                {"pos": roulette_button["rect"].center, "button": 1}
            )

            self.menu.handle_event(event)
            mock_action.assert_called_once()

    def test_click_outside_buttons_does_nothing(self):
        with patch.object(self.menu, "start_blackjack") as mock_blackjack, \
             patch.object(self.menu, "start_slots") as mock_slots, \
             patch.object(self.menu, "start_roulette") as mock_roulette:

            self.menu.buttons[0]["action"] = self.menu.start_blackjack
            self.menu.buttons[1]["action"] = self.menu.start_slots
            self.menu.buttons[2]["action"] = self.menu.start_roulette

            event = pygame.event.Event(
                pygame.MOUSEBUTTONDOWN,
                {"pos": (10, 10), "button": 1}
            )

            self.menu.handle_event(event)

            mock_blackjack.assert_not_called()
            mock_slots.assert_not_called()
            mock_roulette.assert_not_called()


if __name__ == "__main__":
    unittest.main()