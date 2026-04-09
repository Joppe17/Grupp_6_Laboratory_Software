import pygame
import math
from logic.game_object import GameObject 

class Circle(GameObject):
    def __init__(self, x, y, radius, color, state):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.state = state

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            dx = event.pos[0] - self.x
            dy = event.pos[1] - self.y
            if math.sqrt(dx * dx + dy * dy) <= self.radius:
                self.state.score += 1

    def update(self, dt):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
