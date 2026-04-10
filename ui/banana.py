import pygame
import random
from logic.game_object import GameObject

class flyingBanana(GameObject):
    spawnInterval = 40
    duration = 10
    bonusMultiplier = 3

    def __init__(self, screen, state):
        self.state = state
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()

        self.image = pygame.image.load("images/banana.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (90, 50))
        self.active = False
        self.spawn_timer = 0
        self.bonus_timer = 0
        self.bonus_active = False

        self.x = 0
        self.y = 0
        self.speed = 180

    def spawn(self):
        self.x = random.randint(60, self.width - 60)
        self.y = -80 
        self.active = True

    def update(self, dt):      
        if not self.active:
            self.spawn_timer += dt
            if self.spawn_timer >= self.spawnInterval:
                self.spawn()
                self.spawn_timer = 0

        if self.active:
            self.y += self.speed * dt
            if self.y > self.height + 80:
                self.active = False

        if self.bonus_active:
            self.bonus_timer -= dt
            if self.bonus_timer <= 0:
                self.bonus_active = False
                self.state.click_multiplier = 1
    
    def draw(self, screen):
        if self.active:
            screen.blit(self.image, (self.x, self.y))

    def handle_event(self, event):
        if not self.active:
            return
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            rect = pygame.Rect(int(self.x), int(self.y), 80, 80)
            if rect.collidepoint(event.pos):
                self.active = False
                self.bonus_active = True
                self.bonus_timer = self.duration
                self.state.click_multiplier = self.bonusMultiplier


