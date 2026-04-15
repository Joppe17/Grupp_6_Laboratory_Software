import pygame
import os

class MuteButton:
    def __init__(self, x, y, size=50):
        self.x = x
        self.y = y
        self.size = size
        self.muted = False
        icon = pygame.image.load(os.path.join(os.path.dirname(__file__), "mute.png")).convert_alpha()
        self.icon = pygame.transform.scale(icon, (size, size))
        self.rect = pygame.Rect(x - size//2, y - size//2, size, size)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.muted = not self.muted
                if self.muted:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()



    def draw(self, screen):
        screen.blit(self.icon, self.rect)
        if self.muted:
            start = (self.rect.left + 10, self.rect.top + 10)
            end = (self.rect.right - 10, self.rect.bottom - 10)
            pygame.draw.line(screen, (220, 50, 50), start, end, 4)

