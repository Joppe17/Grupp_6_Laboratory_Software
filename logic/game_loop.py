import pygame
from ui.background import Background
from ui.hud import Hud
from ui.circle import Circle
from ui.mute_button import MuteButton
from logic.game_state import GameState
from ui.banana import flyingBanana

from ui.start_menu import StartMenu

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
    screen = pygame.display.set_mode((640, 640))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Monkey Clicker')

    state = GameState()
    objects = []

    background = Background(screen)
    hud = Hud(screen)
    my_circle = Circle(320, 320, 95, "ui/monkey_clicker.jpg", state)
    objects.append(my_circle)
    mute_button = MuteButton(40, 600, size=70)

    banana = flyingBanana(screen, state)
    objects.append(banana)

    pygame.mixer.music.load("ui/alec_koff-african-drums-tribal-492178.mp3")
    pygame.mixer.music.play(-1) 

    menu = StartMenu(screen)

    running = True
    while running:

        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if menu.run() == "exit":
                    running = False
            for obj in objects:
                obj.handle_event(event)
            mute_button.handle_event(event)

        screen.fill((0, 25, 150))
        background.draw(screen)
        hud.draw(screen, state.score)

        for obj in objects:
            obj.update(dt)
            obj.draw(screen)

        mute_button.draw(screen)
        pygame.display.flip()

    pygame.quit()
