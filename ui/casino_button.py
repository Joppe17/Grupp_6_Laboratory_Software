import pygame
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES = os.path.join(PROJECT_ROOT, "images")

class CasinoButton:
    def __init__(self, position, image, action=None, size=65):

        icon = pygame.image.load(os.path.join(IMAGES, image)).convert_alpha()
        self.image = pygame.transform.scale(icon, (size, size))

        self.rect = self.image.get_rect(center=position)

        self.action = action

        self.alpha_idle = 120
        self.alpha_hover = 255

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()

    def draw(self, surface):

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            alpha = self.alpha_hover
        else:
            alpha = self.alpha_idle

        img = self.image.copy()
        img.set_alpha(alpha)

        surface.blit(img, self.rect)