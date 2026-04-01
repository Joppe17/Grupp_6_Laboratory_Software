import pygame
"""
Min tanke är att detta är vår game loop till spelet.
Här har vi en array av objekt där alla kan lägga till egenskapade objekt.
Alla skapade objekt kommer ha GameObjects som bas klass.
GameObjects klassen kommer ha metoder bland annat update, draw med mera.

I vår game loop kommer dessa objekt konstant kallas på och ritas på skärmen eller lyssna på knapp tryckningar osv.

Vi kommer använda en teknik som kallas frame rate independence som i princip sätter samma framerate oavsett datorns hastighet.
"""
pygame.init()

screen = pygame.display.set_mode((640,640))

background_image_surface = pygame.image.load('background.jpg')
background_image_surface = pygame.transform.scale(background_image_surface, (1200, 640))

clock = pygame.time.Clock()

objects = []

running = True
        
while running:
        
    dt = clock.tick(60)/1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            
            running = False

    screen.fill((0,25,150))
    screen.blit(background_image_surface, background_image_surface.get_rect(center = screen.get_rect().center))

    for obj in objects:
        obj.update(dt)
        obj.draw(screen)

    pygame.display.flip()
