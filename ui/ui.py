import pygame

class circle: 
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def update(self, dt):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
pygame.init()

screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption('Not Cookie Clicker')

pygame.quit()