import unittest
import sys
import os


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOUNDS = os.path.join(PROJECT_ROOT, "sounds")


class TestMuteButton(unittest.TestCase):

    def test_mute_button_imports(self):

        from ui.mute_button import MuteButton
        self.assertTrue(callable(MuteButton))

    def test_mute_button_initial_state(self):
        import pygame
        pygame.init()
        pygame.display.set_mode((1, 1))
        from ui.mute_button import MuteButton
        button = MuteButton(40, 600, size=70)
        self.assertFalse(button.muted)
        pygame.quit()

    def test_music_loads(self):
        import pygame
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(SOUNDS,'background_music.mp3'))
        self.assertTrue(True)
        pygame.quit()
