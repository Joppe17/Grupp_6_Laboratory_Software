import pygame

class Circle:
    def __init__(self, x, y, radius, image_path):
        self.x = x
        self.y = y
        self.radius = radius
        self.image = self.make_circular_image(image_path, radius)

    def make_circular_image(self, image_path, radius):
        diameter = radius*2

        # load image
        original = pygame.image.load(image_path).convert_alpha()

        # get original size
        ow, oh = original.get_size()

        # scale image so it fits in the circle
        scale = 1.1*max(diameter / ow, diameter / oh)
        new_width = int(ow * scale)
        new_height = int(oh * scale)

        scaled = pygame.transform.smoothscale(original, (new_width, new_height))

        # crop
        x = (scaled.get_width() - diameter) // 2
        y = (scaled.get_height() - diameter) // 2

        cropped = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        cropped.blit(scaled, (-x, -y))

        #creates circular mask
        mask = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        pygame.draw.circle(mask, (255, 255, 255, 255), (radius, radius), radius)

        #apply mask
        cropped.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        return cropped

    def update(self, dt):
        pass

    def draw(self, screen):
        rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, rect)
