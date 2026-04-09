import pygame
import os

class Hud:
    def __init__(self, screen):
        self.font = pygame.font.Font(os.path.join(os.path.dirname(__file__), "Jungle.otf"), 60)
        self.text_color = (1, 50, 32)
        self.shadow_color = (0, 0, 0)

    def draw(self, screen, counter):
        text = self.font.render(f'CLICKS : {counter}', True, self.text_color)
        shadow = self.font.render(f'CLICKS : {counter}', True, self.shadow_color)
        rect = text.get_rect(center=(320, 70))
        screen.blit(shadow, (rect.x + 3, rect.y + 3))
        screen.blit(text, rect)
