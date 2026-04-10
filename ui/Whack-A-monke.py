import pygame
import random

monkey_img = pygame.image.load(os.path.join(ASSETS, "monkey.png")).convert_alpha()
monkey_img = pygame.transform.scale(monkey_img, (60, 60))


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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                for monkey in monkeys[:]:
                    if monkey.collidepoint(event.pos):
                        monkeys.remove(monkey)
                        score += 100

        screen.fill((34, 139, 34))
        for monkey in monkeys:
            screen.blit(monkey_img, monkey.topleft)
        screen.blit(font.render(f'Time: {max(0, time_left):.1f}', True, (255, 255, 255)), (20, 20))
        screen.blit(font.render(f'Whacked: {score}', True, (255, 255, 255)), (20, 70))
        pygame.display.flip()






