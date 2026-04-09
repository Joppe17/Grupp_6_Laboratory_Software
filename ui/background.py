import os
import pygame

ASSETS = os.path.join(os.path.dirname(__file__))

class Background:
    def __init__(self, screen):
        img = pygame.image.load(os.path.join(ASSETS, "background.jpg"))
        self.surface = pygame.transform.scale(img, (1000, 700))

    def draw(self, screen):
        screen.blit(self.surface, self.surface.get_rect(center=screen.get_rect().center))
