import pygame
import random
import os
import math

IMAGES = os.path.join(os.path.dirname(__file__), "..", "images")
FONTS  = os.path.join(os.path.dirname(__file__))

def run_minigame(screen, clock):
    imgs = [
        pygame.transform.scale(pygame.image.load(os.path.join(IMAGES, "monkey.png")).convert_alpha(), (120, 120)),
        pygame.transform.scale(pygame.image.load(os.path.join(IMAGES, "monkey2.png")).convert_alpha(), (120, 120)),
    ]
    bg   = pygame.transform.scale(pygame.image.load(os.path.join(IMAGES, "minigame_background.jpg")).convert(), (640, 640))
    font = pygame.font.Font(os.path.join(FONTS, "Jungle.otf"), 60)

    monkeys, score, time_left, spawn_timer = [], 0, 20.0, 0

    while time_left > 0:
        dt          = clock.tick(60) / 1000
        time_left  -= dt
        spawn_timer -= dt

        if spawn_timer <= 0:
            spawn_timer = 0.5
            monkeys.append({"pos": (random.randint(100, 540), random.randint(100, 540)), "img": random.choice(imgs), "age": 0.0})

        monkeys = [m for m in monkeys if m["age"] < 1.0]
        for m in monkeys:
            m["age"] += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                for m in monkeys[:]:
                    if pygame.Rect(*m["pos"], 120, 120).collidepoint(event.pos):
                        monkeys.remove(m)
                        score += 1

        screen.blit(bg, (0, 0))
        for m in monkeys:
            size = int(120 * (1 - m["age"]))
            if size > 0:
                img = pygame.transform.scale(m["img"], (size, size))
                screen.blit(img, (m["pos"][0] + math.sin(m["age"] * 30) * 5, m["pos"][1]))

        screen.blit(font.render(f'Time: {max(0, time_left):.1f}', True, (255, 255, 255)), (20, 20))
        screen.blit(font.render(f'Whacked: {score}', True, (255, 255, 255)), (20, 70))
        pygame.display.flip()
