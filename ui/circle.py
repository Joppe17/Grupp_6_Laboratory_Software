import pygame
import math
from logic.game_object import GameObject 

class Circle(GameObject):
    def __init__(self, x, y, radius, image_path, state):
        self.x = x
        self.y = y
        self.radius = radius
        self.base_radius = radius
        self.state = state
        self.image = self.make_circular_image(image_path,radius)
        self.scale_factor = 1.2
        self.max_radius = 500
        self.growth_speed = 600
        self.target_radius = radius
        self.image_path = image_path
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            dx = event.pos[0] - self.x
            dy = event.pos[1] - self.y
            if math.sqrt(dx * dx + dy * dy) <= self.radius:
                self.state.score += 1 * self.state.click_multiplier
                if self.target_radius < self.max_radius:
                    self.target_radius = int(self.target_radius * self.scale_factor)

    def make_circular_image(self, image_path, radius):
        diameter = radius*2
        original = pygame.image.load(image_path).convert_alpha()
        ow, oh = original.get_size()

        scale = 1.1*max(diameter / ow, diameter / oh)
        new_width = int(ow * scale)
        new_height = int(oh * scale)

        scaled = pygame.transform.smoothscale(original, (new_width, new_height))

        x = (scaled.get_width() - diameter) // 2
        y = (scaled.get_height() - diameter) // 2

        cropped = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        cropped.blit(scaled, (-x, -y))

        mask = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        pygame.draw.circle(mask, (255, 255, 255, 255), (radius, radius), radius)

        cropped.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        return cropped

    def update(self, dt):
        shrink_speed = 300
        if self.target_radius > self.base_radius:
            self.target_radius -= shrink_speed * dt
            if self.target_radius < self.base_radius:
                self.target_radius = self.base_radius

            if self.radius < self.target_radius:
                self.radius += self.growth_speed * dt
                if self.radius > self.target_radius:
                    self.radius = self.target_radius

            elif self.radius > self.target_radius:
                self.radius -= self.growth_speed * dt
                if self.radius < self.target_radius:
                    self.radius = self.target_radius



        self.image = self.make_circular_image(
            self.image_path,
            int(self.radius)
            )

    def draw(self, screen):
        rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, rect)

