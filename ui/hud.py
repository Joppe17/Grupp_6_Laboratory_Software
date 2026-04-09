import pygame

class Hud:
    def __init__(self, screen):
        self.font = pygame.font.SysFont('comicsansms', 60)
        self.text_color = (255, 165, 0)
        self.shadow_color = (0, 0, 0)

    def draw(self, screen, counter):
        text = self.font.render(f'Clicks : {counter}', True, self.text_color)
        shadow = self.font.render(f'Clicks : {counter}', True, self.shadow_color)
        rect = text.get_rect(center=(320, 50))
        screen.blit(shadow, (rect.x + 3, rect.y + 3))
        screen.blit(text, rect)
