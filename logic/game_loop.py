import pygame
from ui.background import Background
from ui.hud import Hud
from ui.circle import Circle
from ui.mute_button import MuteButton
from logic.game_state import GameState
from ui.banana import FlyingBanana
from ui.upgrade_menu import UpgradeMenu, UpgradeButton
from ui.start_menu import StartMenu

from ui.whack_a_monkey import run_minigame


def run():

    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Monkey Clicker')

    state = GameState()
    objects = []

    background = Background(screen)
    hud = Hud(screen)
    my_circle = Circle(320, 320, 95, "images/monkey_clicker.jpg", state)
    objects.append(my_circle)
    mute_button = MuteButton(40, 600, size=70)

    banana = FlyingBanana(screen, state)
    objects.append(banana)

    pygame.mixer.music.load("sounds/background_music.mp3")
    upgrade_menu = UpgradeMenu(screen)
    upgrade_button = UpgradeButton(screen, upgrade_menu)
    pygame.mixer.music.play(-1)

    menu = StartMenu(screen)

    # run_minigame(screen, clock)

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
            upgrade_menu.handle_event(event)
            upgrade_button.handle_event(event)

        screen.fill((0, 25, 150))
        background.draw(screen)
        hud.draw(screen, state.score, state)

        for obj in objects:
            obj.update(dt)
            obj.draw(screen)

        upgrade_menu.update(dt)
        upgrade_menu.draw()
        upgrade_button.draw()
        mute_button.draw(screen)
        pygame.display.flip()

    pygame.quit()
