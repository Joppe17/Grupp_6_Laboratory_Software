import pygame

pygame.init()

screen = pygame.display.set_mode((640,640))

running = True

screen.fill((128, 255, 255))
pygame.display.flip()

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    pygame.draw.circle(screen,(0,0,0),(320,320),150)
    pygame.display.update()

pygame.quit()

