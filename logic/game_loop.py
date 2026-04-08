import os
import pygame
from ui.circle import Circle
#from ui.start_menu import draw_start_menu
ASSETS = os.path.join(os.path.dirname(__file__), "..", "ui")

"""
Min tanke är att detta är vår game loop till spelet.
Här har vi en array av objekt där alla kan lägga till egenskapade objekt.
Alla skapade objekt kommer ha GameObjects som bas klass.
GameObjects klassen kommer ha metoder bland annat update, draw med mera.

I vår game loop kommer dessa objekt konstant kallas på och ritas på skärmen eller lyssna på knapp tryckningar osv.

Vi kommer använda en teknik som kallas frame rate independence som i princip sätter samma framerate oavsett datorns hastighet.
"""
def run():
    pygame.init()

    Counter = 0



    screen = pygame.display.set_mode((640,640))

    background_image_surface = pygame.image.load(os.path.join(ASSETS, "background.jpg"))
    background_image_surface = pygame.transform.scale(background_image_surface, (1200, 640))

    clock = pygame.time.Clock()

    text_color = (255, 165, 0)

"""
Move some of this code to an appropiate place to adhere to a good structure.
"""
    objects = []

    my_circle = Circle(320, 320, 95, (0, 0, 0))
    objects.append(my_circle)

    pygame.display.set_caption('Not Cookie Clicker')

    font=pygame.font.SysFont('comicsansms', 60)
    #font = pygame.font.Font(None, 60)

    text = font.render('Clicks : ' + str(Counter), True, text_color)
    textrect = text.get_rect(center=(320, 50))

    shadow = font.render('Clicks : ' + str(Counter), True, (0,0,0))
    screen.blit(shadow, (textrect.x + 3, textrect.y + 3))

    running = True
        
    while running:
        
        text = font.render('Clicks : ' + str(Counter), True, text_color)
        textrect = text.get_rect(center=(320, 50))   

      

        dt = clock.tick(60)/1000

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
            
                running = False

            screen.fill((0,25,150))
            screen.blit(background_image_surface, background_image_surface.get_rect(center = screen.get_rect().center))
            screen.blit(text, textrect) 

        shadow = font.render('Clicks : ' + str(Counter), True, (0,0,0))
        screen.blit(shadow, (textrect.x + 3, textrect.y + 3))

        for obj in objects:
            obj.update(dt)
            obj.draw(screen)

        #draw_start_menu(screen)

        pygame.display.flip()
    pygame.quit()


