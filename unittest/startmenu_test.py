import unittest
from unittest.mock import patch
import pygame

from ui.start_menu import StartMenu


class TestStartMenu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        pygame.font.init()
        cls.screen = pygame.display.set_mode((800, 600))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def setUp(self):
        self.menu = StartMenu(self.screen)

    def test_menu_is_created(self):
        self.assertIsNotNone(self.menu)

    def test_panel_rect_exists(self):
        self.assertIsNotNone(self.menu.panel_rect)
        self.assertTrue(isinstance(self.menu.panel_rect, pygame.Rect))

    def test_start_and_exit_rects_exist(self):
        self.assertTrue(isinstance(self.menu.start_rect, pygame.Rect))
        self.assertTrue(isinstance(self.menu.exit_rect, pygame.Rect))

    def test_fonts_are_loaded(self):
        self.assertIsNotNone(self.menu.title_font)
        self.assertIsNotNone(self.menu.button_font)

    def test_panel_is_centered_on_screen(self):
        sw = self.screen.get_width()
        sh = self.screen.get_height()
        self.assertEqual(self.menu.panel_rect.centerx, sw // 2)
        self.assertAlmostEqual(self.menu.panel_rect.centery, sh // 2, delta=1)

    def test_start_and_exit_buttons_do_not_overlap(self):
        self.assertFalse(self.menu.start_rect.colliderect(self.menu.exit_rect))

    def test_draw_runs_without_error(self):
        try:
            self.menu._draw((0, 0))
        except Exception as e:
            self.fail(f"_draw raised an exception: {e}")

    def test_quit_event_returns_exit(self):
        quit_event = pygame.event.Event(pygame.QUIT)

        with patch("pygame.event.get", return_value=[quit_event]), \
             patch("pygame.display.flip"), \
             patch("pygame.mouse.get_pos", return_value=(0, 0)):
            result = self.menu.run()

        self.assertEqual(result, "exit")

    def test_escape_key_returns_start(self):
        escape_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_ESCAPE})

        with patch("pygame.event.get", return_value=[escape_event]), \
             patch("pygame.display.flip"), \
             patch("pygame.mouse.get_pos", return_value=(0, 0)):
            result = self.menu.run()

        self.assertEqual(result, "start")

    def test_click_start_button_returns_start(self):
        click_event = pygame.event.Event(
            pygame.MOUSEBUTTONDOWN,
            {"pos": self.menu.start_rect.center, "button": 1},
        )

        with patch("pygame.event.get", return_value=[click_event]), \
             patch("pygame.display.flip"), \
             patch("pygame.mouse.get_pos", return_value=self.menu.start_rect.center):
            result = self.menu.run()

        self.assertEqual(result, "start")

    def test_click_exit_button_returns_exit(self):
        click_event = pygame.event.Event(
            pygame.MOUSEBUTTONDOWN,
            {"pos": self.menu.exit_rect.center, "button": 1},
        )

        with patch("pygame.event.get", return_value=[click_event]), \
             patch("pygame.display.flip"), \
             patch("pygame.mouse.get_pos", return_value=self.menu.exit_rect.center):
            result = self.menu.run()

        self.assertEqual(result, "exit")

    def test_click_outside_buttons_does_not_return(self):
        outside_click = pygame.event.Event(
            pygame.MOUSEBUTTONDOWN,
            {"pos": (0, 0), "button": 1},
        )
        quit_event = pygame.event.Event(pygame.QUIT)

        with patch("pygame.event.get", side_effect=[[outside_click], [quit_event]]), \
             patch("pygame.display.flip"), \
             patch("pygame.mouse.get_pos", return_value=(0, 0)):
            result = self.menu.run()

        self.assertEqual(result, "exit")

    def test_right_click_on_start_button_is_ignored(self):
        right_click = pygame.event.Event(
            pygame.MOUSEBUTTONDOWN,
            {"pos": self.menu.start_rect.center, "button": 3},
        )
        quit_event = pygame.event.Event(pygame.QUIT)

        with patch("pygame.event.get", side_effect=[[right_click], [quit_event]]), \
             patch("pygame.display.flip"), \
             patch("pygame.mouse.get_pos", return_value=self.menu.start_rect.center):
            result = self.menu.run()

        self.assertEqual(result, "exit")


if __name__ == "__main__":
    unittest.main()