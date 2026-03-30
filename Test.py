import pygame

pygame.init()

screen = pygame.display.set_mode((1920,1080))

pygame.display.set_caption("NOT CookieClicker")

running = true

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

pygame.quit()

