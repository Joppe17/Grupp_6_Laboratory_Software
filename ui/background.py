import os
import pygame

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES = os.path.join(PROJECT_ROOT, "images")

class Background:
    def __init__(self, screen):
        img = pygame.image.load(os.path.join(IMAGES, "background.jpg"))
        self.surface = pygame.transform.scale(img, (1000, 700))

    def draw(self, screen):
        screen.blit(self.surface, self.surface.get_rect(
            center=screen.get_rect().center))
