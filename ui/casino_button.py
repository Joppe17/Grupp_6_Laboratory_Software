import pygame
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES = os.path.join(PROJECT_ROOT, "images")

class CasinoButton:
    def __init__(self, position, size = 65):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, surface):
        #standard
        surface.blit(self.image, self.rect)
