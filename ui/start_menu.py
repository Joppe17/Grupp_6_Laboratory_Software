import pygame
import os

class StartMenu:
    def __init__(self, screen):
        self.screen = screen

        panel_width = 500
        panel_height = 350
        sw = screen.get_width()
        sh = screen.get_height()
        px = (sw - panel_width) // 2
        py = (sh - panel_height) // 2

        self.panel_rect = pygame.Rect(px, py, panel_width, panel_height)
        self.panel_color = (245, 222, 179)
        self.border_color = (139, 69, 19)

        btn_w, btn_h = 200, 55
        btn_x = (sw - btn_w) // 2
        self.start_rect = pygame.Rect(btn_x, py + 185, btn_w, btn_h)
        self.exit_rect  = pygame.Rect(btn_x, py + 265, btn_w, btn_h)

        font_path = os.path.join(os.path.dirname(__file__), "Jungle.otf")
        self.title_font  = pygame.font.Font(font_path, 52)
        self.button_font = pygame.font.Font(font_path, 36)

    def _draw(self, mouse_pos):
        # Dim the game behind the menu
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 140))
        self.screen.blit(overlay, (0, 0))

        # Panel
        pygame.draw.rect(self.screen, self.panel_color, self.panel_rect, border_radius=20)
        pygame.draw.rect(self.screen, self.border_color, self.panel_rect, width=4, border_radius=20)

        # Title
        title = self.title_font.render("PAUSED", True, self.border_color)
        self.screen.blit(title, title.get_rect(center=(self.screen.get_width() // 2,
                                                       self.panel_rect.y + 80)))

        # Buttons
        for rect, label in [(self.start_rect, "Start"), (self.exit_rect, "Exit")]:
            hover = rect.collidepoint(mouse_pos)
            btn_color = (180, 100, 30) if hover else (139, 69, 19)
            pygame.draw.rect(self.screen, btn_color, rect, border_radius=12)
            pygame.draw.rect(self.screen, self.border_color, rect, width=2, border_radius=12)
            text = self.button_font.render(label, True, (255, 255, 255))
            bounds = text.get_bounding_rect()
            self.screen.blit(text, (rect.centerx - bounds.centerx,
                                    rect.centery - bounds.centery))

    def run(self):
        """
        Blocks until the player picks an action.
        Returns 'start' to resume the game or 'exit' to quit.
        """
        clock = pygame.time.Clock()
        while True:
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "start"
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.start_rect.collidepoint(event.pos):
                        return "start"
                    if self.exit_rect.collidepoint(event.pos):
                        return "exit"

            self._draw(mouse_pos)
            pygame.display.flip()
            clock.tick(60)
