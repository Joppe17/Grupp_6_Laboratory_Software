import pygame
import sys

pygame.init()
pygame.font.init()

#parameters
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monkeycasino")
font = pygame.font.SysFont(None, 36)

class CasinoStartMenu:
    
    def __init__(self,screen):
        self.screen = screen
        self.blackjack_button = pygame.Rect(300, 200, 200, 50)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.blackjack_button.collidepoint(event.pos):
                print("Blackjack button clicked")
                #logic for buttonclick, could add more buttons and stuff similar to this under
                
                

    def draw(self):
        self.screen.fill((255,255,255))
        pygame.draw.rect(self.screen, (0, 0, 255), self.blackjack_button)
                
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