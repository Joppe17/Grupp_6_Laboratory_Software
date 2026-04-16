"""
This file will contain all UI elements for future upgrades
such as the one i've implemented below.
"""
import pygame
from ui.theme import (BORDER_COLOR, BUTTON_COLOR, BUTTON_HOVER, TEXT_COLOR, FONT_PATH_J)

CARD_HEIGHT = 90
CARD_GAP = 10
CARD_START_Y = 150


class UpgradePanel:
    def __init__(self, panel_width, target_x):
        self.panel_width = panel_width
        self.target_x = int(target_x)
        self.tab_font = pygame.font.Font(FONT_PATH_J, 28)
        self.small_font = pygame.font.Font(FONT_PATH_J, 22)
        self.upgrades = []
        self._buy_rects = []
    
    def set_upgrades(self, upgrades):
        self.upgrades = upgrades

    def handle_event(self, event, panel_x, target_x):
        if event.type == pygame.MOUSEBUTTONDOWN:
            offset_x = panel_x - target_x
            for upgrade, buy_rect in self._buy_rects:
                if buy_rect.move(offset_x, 0).collidepoint(event.pos):
                    upgrade.purchase()
                    return True
        return False
    
    def draw(self, screen, px, mouse_pos, current_tab_name):
        tab_upgrades = [u for u in self.upgrades if u.tab == current_tab_name]
        self._buy_rects = []

        if not tab_upgrades:
            return False
        
        card_w = self.panel_width - 40
        for i, upgrade in enumerate(tab_upgrades):
            card_y = CARD_START_Y + i * (CARD_HEIGHT + CARD_GAP)
            card_base = pygame.Rect(self.target_x + 20, card_y, card_w, CARD_HEIGHT)
            card_rect = card_base.move(px - self.target_x, 0)

            pygame.draw.rect(screen, (80, 35, 10), card_rect, border_radius=8)
            pygame.draw.rect(screen, BORDER_COLOR, card_rect, width=2, border_radius=8)

            name_surf = self.tab_font.render(upgrade.name, True, BORDER_COLOR)
            name_rect = name_surf.get_rect(topleft=(card_rect.x + 10, card_rect.y + 5))
            name_rect.y += 6
            screen.blit(name_surf, name_rect)

            desc_surf = self.small_font.render(upgrade.description, True, TEXT_COLOR)
            desc_rect = desc_surf.get_rect(topleft=(card_rect.x + 10, card_rect.y + 52))
            desc_rect.y += 6
            screen.blit(desc_surf, desc_rect)

            buy_rect_base = pygame.Rect(self.target_x + self.panel_width - 150,
                                        card_y + 10, 130, 40)
            self._buy_rects.append((upgrade, buy_rect_base))
            buy_rect = buy_rect_base.move(px - self.target_x, 0)

            can_buy = upgrade.can_buy()
            buy_hover = buy_rect.collidepoint(mouse_pos) and can_buy
            buy_color = BUTTON_HOVER if buy_hover else (BUTTON_COLOR if can_buy else (120, 120, 120))

            pygame.draw.rect(screen, buy_color, buy_rect, border_radius=6)
            pygame.draw.rect(screen, BORDER_COLOR, buy_rect, width=2, border_radius=6)

            cost_surf = self.small_font.render(f"{upgrade.get_cost()} Clicks", True, (0, 0, 0) if can_buy else TEXT_COLOR)
            cost_rect = cost_surf.get_rect(center=buy_rect.center)
            cost_rect.y += 6
            screen.blit(cost_surf, cost_rect)

            owned_surf = self.small_font.render(f"Owned {upgrade.times_bought}", True, TEXT_COLOR)
            owned_rect = owned_surf.get_rect(topleft=(buy_rect.x, buy_rect.bottom + 4))
            owned_rect.y += 6
            screen.blit(owned_surf, owned_rect)

        return True