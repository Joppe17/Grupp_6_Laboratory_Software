import pygame
import sys
from theme import *


pygame.init()
pygame.font.init()

#parameters
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monkeycasino")
title_font = pygame.font.Font(FONT_PATH_J, TITLE_FONT_SIZE)
button_font = pygame.font.Font(FONT_PATH_B, BUTTON_FONT_SIZE)


class CasinoStartMenu:
    
    def __init__(self,screen):
        self.screen = screen

        margin = 40  # distance from screen edges

        p_Width = screen.get_width() - margin * 2
        p_Height = screen.get_height() - margin * 2

        sw = screen.get_width()
        sh = screen.get_height()

        px = (sw - p_Width) // 2
        py = (sh - p_Height) // 2
        
        self.panel_rect = pygame.Rect(px, py, p_Width, p_Height)
        self.buttons = [
            {"rect": pygame.Rect(sw//2 - 100, py + 180, 200, 50),
            "label": "Blackjack", "action": self.start_blackjack},
            {"rect": pygame.Rect(sw//2 - 100, py + 250, 200, 50),
            "label": "Slots", "action": self.start_slots},
            {"rect": pygame.Rect(sw//2 - 100, py + 320, 200, 50),
            "label": "Roulette", "action": self.start_roulette},
        ]

    def start_blackjack(self):
        #blackjack logic here
        print("Starting Blackjack...")
    def start_slots(self):
        #same here but start slots
        print("Starting Slots...")
    def start_roulette(self):
        #roulette logic here
        print("Starting Roulette...")
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button["rect"].collidepoint(event.pos):
                    button["action"]()
                    
                
                
                

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()

        #panel
        pygame.draw.rect(self.screen, PANEL_COLOR, self.panel_rect, border_radius=20)
        pygame.draw.rect(self.screen, BORDER_COLOR, self.panel_rect, width=4, border_radius=20)

        #hover effect from start menu
        for button in self.buttons:
            color = BUTTON_HOVER if button["rect"].collidepoint(mouse_pos) else BUTTON_COLOR

            pygame.draw.rect(self.screen, color, button["rect"], border_radius=12)
            pygame.draw.rect(self.screen, BORDER_COLOR, button["rect"], width=2, border_radius=12)

            text = button_font.render(button["label"], True, TEXT_COLOR)
            text_rect = text.get_rect(center=button["rect"].center)
            self.screen.blit(text, text_rect)

        #title
        title = title_font.render("MONKEY CASINO", True, BORDER_COLOR)
        title_shadow = title_font.render("MONKEY CASINO", True, (0, 0, 0))

        title_rect = title.get_rect(center=(self.panel_rect.centerx, self.panel_rect.y + 70))

        self.screen.blit(title_shadow, (title_rect.x + 3, title_rect.y + 3))
        self.screen.blit(title, title_rect)
            
menu = CasinoStartMenu(screen) 

#simple game loop to keep menu running
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        menu.handle_event(event)
    menu.draw()
    pygame.display.flip()
pygame.quit()
sys.exit()