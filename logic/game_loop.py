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
    counter = 0  # lowercase, Python convention
    screen = pygame.display.set_mode((640, 640))
    clock = pygame.time.Clock()
    objects = []

    # --- move all setup into their own modules ---
    from ui.background import Background
    from ui.hud import Hud
    from ui.circle import Circle

    background = Background(screen)
    hud = Hud(screen)
    my_circle = Circle(320, 320, 95, (0, 0, 0))
    objects.append(my_circle)

    pygame.display.set_caption('Not Cookie Clicker')
    running = True

    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # these three always run every frame, outside event loop
        screen.fill((0, 25, 150))
        background.draw(screen)
        hud.draw(screen, counter)

        for obj in objects:
            obj.update(dt)
            obj.draw(screen)

        pygame.display.flip()

    pygame.quit()
