import pygame

class UpgradeMenu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.panel_width = 280
        self.closed_x = screen_width
        self.open_x = screen_width - self.panel_width
        self.current_x = float(self.closed_x)
        self.target_x = float(self.closed_x)
        self.slide_speed = 900
        self.is_open = False

        self.tab_width = 36
        self.tab_height = 90
        self.tab_bottom_margin = 20

        self.title_font = pygame.font.SysFont(None, 42)


    def toggle(self):
        self.is_open = not self.is_open
        if self.is_open:
            self.target_x = self.open_x
        else:
            self.target_x = self.closed_x

    
    def update(self, dt):
        pass

    def handle_event(self, event):
        return None
    
    def draw(self, screen):
        pass