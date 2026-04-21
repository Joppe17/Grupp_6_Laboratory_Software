import pygame
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(PROJECT_ROOT, "fonts")

class Hud:
    def __init__(self, screen):
        self.font = pygame.font.Font(os.path.join(FONTS, "Jungle.otf"), 60)
        self.small_font = pygame.font.Font(os.path.join(FONTS, "Jungle.otf"), 25)
        self.text_color = (1, 50, 32)
        self.shadow_color = (0, 0, 0)
        self.bonus_color = (255, 200, 0)

    def draw(self, screen, counter, state):
        text = self.font.render(f'CLICKS : {int(counter)}', True, self.text_color)
        shadow = self.font.render(
            f'CLICKS : {int(counter)}', True, self.shadow_color)
        rect = text.get_rect(center=(320, 70))
        screen.blit(shadow, (rect.x + 3, rect.y + 3))
        screen.blit(text, rect)

        if state.click_multiplier > 1:
            bonus_text = self.small_font.render(
                "3X MULTIPLIER!", True, self.bonus_color)
            bonus_shadow = self.small_font.render(
                "3X MULTIPLIER!", True, self.shadow_color)

            bonus_text = pygame.transform.rotate(bonus_text, -15)
            bonus_shadow = pygame.transform.rotate(bonus_shadow, -15)

            bonus_rect = bonus_text.get_rect(
                midleft=(rect.right + 10, rect.centery))
            screen.blit(bonus_shadow, (bonus_rect.x + 2, bonus_rect.y + 2))
            screen.blit(bonus_text, bonus_rect)
