import pygame
import os
from ui.theme import (
    PANEL_COLOR, BORDER_COLOR, BUTTON_COLOR, BUTTON_HOVER,
    TEXT_COLOR, OVERLAY_COLOR, FONT_PATH_B, FONT_PATH_J,
    TITLE_FONT_SIZE, BUTTON_FONT_SIZE
)
from ui.upgrades.upgrade_card import UpgradesPanel
PANEL_WIDTH_RATIO = 0.8
SLIDE_SPEED = 2000

TABS = ["Click Upgrades", "Auto Clicks", "Special"]

class UpgradeMenu:
    def __init__(self, screen):
        self.screen = screen
        self.sw = screen.get_width()
        self.sh = screen.get_height()
        self.panel_width = int(self.sw * PANEL_WIDTH_RATIO)
        self.panel_height = self.sh

        self.open = False
        self.panel_x = float(self.sw)
        self.target_x = float(self.sw - self.panel_width)

        self.current_tab = 0

        self.title_font = pygame.font.Font(FONT_PATH_J, TITLE_FONT_SIZE)
        self.button_font = pygame.font.Font(FONT_PATH_J, BUTTON_FONT_SIZE)
        self.tab_font = pygame.font.Font(FONT_PATH_J, 28)

        tab_w = self.panel_width // len(TABS)
        self.tab_rects = [
            pygame.Rect(int(self.target_x) + i * tab_w, 70, tab_w, 50)
            for i in range(len(TABS))
        ]

        self.close_rect = pygame.Rect(
            int(self.target_x) + self.panel_width - 50, 10, 40, 40)
        
        self.upgrades_panel = UpgradesPanel(self.panel_width, self.target_x)

    def toggle(self):
        self.open = not self.open

    def set_upgrades(self):
        self.upgrades_panel = UpgradesPanel(self.panel_width, self.target_x)

    def update(self, dt):
        if self.open:
            self.panel_x -= SLIDE_SPEED * dt
            if self.panel_x < self.sw - self.panel_width:
                self.panel_x = float(self.sw - self.panel_width)
        else:
            self.panel_x += SLIDE_SPEED * dt
            if self.panel_x > self.sw:
                self.panel_x = float(self.sw)

    def handle_event(self, event):
        if not self.open:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] < self.panel_x:
                self.toggle()
                return

            for i, rect in enumerate(self.tab_rects):
                shifted = rect.move(self.panel_x - self.target_x, 0)
                if shifted.collidepoint(event.pos):
                    self.current_tab = i

            shifted_close = self.close_rect.move(self.panel_x - self.target_x, 0)
            if shifted_close.collidepoint(event.pos):
                self.toggle()

            self.upgrades_panel.handle_event(event, self.panel_x, self.target_x)

    def _draw_panel(self, mouse_pos):
        px = int(self.panel_x)

        panel_rect = pygame.Rect(px, 0, self.panel_width, self.panel_height)
        pygame.draw.rect(self.screen, PANEL_COLOR, panel_rect)
        pygame.draw.rect(self.screen, BORDER_COLOR, panel_rect, width=4)

        # title
        title = self.title_font.render("UPGRADES", True, BORDER_COLOR)
        title_rect = title.get_rect(center=(px + self.panel_width // 2, 35))
        title_rect.y += 24
        self.screen.blit(title, title_rect)

        # close button
        shifted_close = self.close_rect.move(px - int(self.target_x), 0)
        pygame.draw.rect(self.screen, BUTTON_COLOR, shifted_close, border_radius=8)
        x_text = self.button_font.render("X", True, TEXT_COLOR)
        x_rect = x_text.get_rect(center=shifted_close.center)
        x_rect.y += 17
        self.screen.blit(x_text, x_rect)

        # tabs
        for i, (rect, label) in enumerate(zip(self.tab_rects, TABS)):
            shifted = rect.move(px - int(self.target_x), 0)
            active = (i == self.current_tab)
            hover = shifted.collidepoint(mouse_pos)
            color = BORDER_COLOR if active else (BUTTON_HOVER if hover else BUTTON_COLOR)
            pygame.draw.rect(self.screen, color, shifted, border_radius=8)
            pygame.draw.rect(self.screen, BORDER_COLOR, shifted, width=2, border_radius=8)
            text = self.tab_font.render(label, True, TEXT_COLOR)
            text_rect = text.get_rect(center=shifted.center)
            text_rect.y += 12
            self.screen.blit(text, text_rect)

        # content area
        content_rect = pygame.Rect(px + 10, 135, self.panel_width - 20, self.panel_height - 145)
        pygame.draw.rect(self.screen, BORDER_COLOR, content_rect, width=2, border_radius=8)

        # page label
        if not self.upgrades_panel.draw(self.screen, px, mouse_pos, TABS[self.current_tab]):
            page_label = self.tab_font.render(
                f"No {TABS[self.current_tab]} yet", True, BORDER_COLOR)
            page_rect = page_label.get_rect(
                center=(px + self.panel_width // 2, 145 + content_rect.height // 2))
            page_rect.y += 14
            self.screen.blit(page_label, page_rect)

    def draw(self):
        if self.panel_x >= self.sw:
            return
        mouse_pos = pygame.mouse.get_pos()
        self._draw_panel(mouse_pos)


class UpgradeButton:
    def __init__(self, screen, menu):
        self.screen = screen
        self.menu = menu
        self.font = pygame.font.Font(FONT_PATH_J, 28)
        self.rect = pygame.Rect(screen.get_width() - 160, screen.get_height() - 55, 150, 45)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.menu.toggle()

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        hover = self.rect.collidepoint(mouse_pos)
        color = BUTTON_HOVER if hover else BUTTON_COLOR
        pygame.draw.rect(self.screen, color, self.rect, border_radius=10)
        pygame.draw.rect(self.screen, BORDER_COLOR, self.rect, width=2, border_radius=10)
        text = self.font.render("UPGRADES", True, TEXT_COLOR)
        text_rect = text.get_rect(center=self.rect.center)
        text_rect.y += 12
        self.screen.blit(text, text_rect)