import pygame
import random

def run_minigame(screen, clock):

    monkeys = []
    score = 0
    time_left = 20.0
    spawn_timer = 0

    while time_left > 0:
        dt = clock.tick(60) / 1000
        time_left -= dt
        spawn_timer -= dt

        if spawn_timer <=0:
            spawn_timer = 1.0
            x = random.randint(100,540)
            y = random.randint(100,540)
            monkeys.append(pygame.Rect(x,y,60,60))





