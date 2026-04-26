import pygame
from ui.theme import *


class StartMenu:
    def __init__(self, screen):
        self.screen = screen

        sw = screen.get_width()
        sh = screen.get_height()
        px = (sw - PANEL_WIDTH) // 2
        py = (sh - PANEL_HEIGHT) // 2

        self.panel_rect = pygame.Rect(px, py, PANEL_WIDTH, PANEL_HEIGHT)
        

        btn_w, btn_h = 200, 42
        btn_x = (sw - btn_w) // 2

        self.start_rect = pygame.Rect(btn_x, py + 110, btn_w, btn_h)
        self.save_rect = pygame.Rect(btn_x, py + 165, btn_w, btn_h)
        self.load_rect = pygame.Rect(btn_x, py + 220, btn_w, btn_h)
        self.exit_rect = pygame.Rect(btn_x, py + 275, btn_w, btn_h)

        self.title_font = pygame.font.Font(FONT_PATH_B, 52)
        self.button_font = pygame.font.Font(FONT_PATH_B, 30)

    def _draw(self, mouse_pos):
        # Dim the game behind the menu
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill(OVERLAY_COLOR)
        self.screen.blit(overlay, (0, 0))

        # Panel
        pygame.draw.rect(self.screen, PANEL_COLOR,
                         self.panel_rect, border_radius=20)
        pygame.draw.rect(self.screen, BORDER_COLOR,
                         self.panel_rect, width=4, border_radius=20)

        # Title
        title_shadow = self.title_font.render("PAUSED", True, SHADOW_COLOR)
        title = self.title_font.render("PAUSED", True, BORDER_COLOR)
        title_rect = title.get_rect(center=(self.screen.get_width() // 2,
                                            self.panel_rect.y + 60))
        self.screen.blit(title_shadow, (title_rect.x + SHADOW_OFFSET, title_rect.y + SHADOW_OFFSET))
        self.screen.blit(title, title_rect)

        # Buttons
        for rect, label in [(self.start_rect, "Start"), (self.save_rect, "Save"), (self.load_rect, "Load"), (self.exit_rect, "Exit")]:
            hover = rect.collidepoint(mouse_pos)
            btn_color = BUTTON_HOVER if hover else BUTTON_COLOR
            pygame.draw.rect(self.screen, btn_color, rect, border_radius=12)
            pygame.draw.rect(self.screen, BORDER_COLOR,
                             rect, width=2, border_radius=12)
            text = self.button_font.render(label, True, TEXT_COLOR)
            text_shadow = self.button_font.render(label, True, SHADOW_COLOR)
            bounds = text.get_bounding_rect()
            self.screen.blit(text_shadow, (rect.centerx - bounds.centerx + SHADOW_OFFSET,
                                           rect.centery - bounds.centery + SHADOW_OFFSET))
            self.screen.blit(text, (rect.centerx - bounds.centerx,
                                    rect.centery - bounds.centery))

    def run(self):
        """
        Blocks until the player picks an action.
        Returns 'start' to resume the game or 'exit' to quit,
                'save' to save game, 'load' to load previous game
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
                    if self.save_rect.collidepoint(event.pos):
                        return "save"
                    if self.load_rect.collidepoint(event.pos):
                        return "load"
                    if self.exit_rect.collidepoint(event.pos):
                        return "exit"

            self._draw(mouse_pos)
            pygame.display.flip()
            clock.tick(60)
