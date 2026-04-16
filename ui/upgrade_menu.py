import pygame

class UpgradeMenu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        #sliding panel
        self.width = 280
        self.x = screen_width
        self.closed_x = screen_width
        self.open_x = screen_width - self.width
        self.target_x = self.closed_x

        self.is_open = False
        self.speed = 900
        self.scroll = 0

        # fonts
        self.title_font = pygame.font.SysFont(None, 42)
        self.item_font = pygame.font.SysFont(None, 28)
        self.small_font = pygame.font.SysFont(None, 22)


    def toggle(self):
        self.is_open = not self.is_open
        if self.is_open:
            self.target_x = self.open_x
        else:
            self.target_x = self.closed_x

    
    def update(self, dt):
        if self.x < self.target_x:
            self.x += self.speed * dt
            if self.x > self.target_x:
               self.x = self.target_x
        elif self.x > self.target_x:
            self.x -= self.speed * dt
            if self.x < self.target_x:
               self.x = self.target_x

        if self.scroll < 0:
           self.scroll = 0
        if self.scroll > 200:
            self.scroll = 200
    

    def contains_point(self, pos):
        tab_rect = pygame.Rect(self.screen_width - 36, self.screen_height - 110, 36, 90)
        panel_rect = pygame.Rect(int(self.x), 0, self.width, self.screen_height)

        return tab_rect.collidepoint(pos) or panel_rect.collidepoint(pos)
    

    def handle_event(self, event):
        tab_rect = pygame.Rect(self.screen_width - 36, self.screen_height - 110, 36, 90)
        upgrade_rect = pygame.Rect(int(self.x) + 18, 107 - self.scroll, self.width-36, 90)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if tab_rect.collidepoint(event.pos):
                    self.toggle()
                    return "toggle_menu"
                
                if self.is_open and upgrade_rect.collidepoint(event.pos):
                    return "money_per_click_upgrade"
                
                if self.is_open and pygame.Rect(int(self.x), 0, self.width, self.screen_height).collidepoint(event.pos):
                    return "menu_click" 
                    
            if self.is_open:
                if event.button == 4:
                    self.scroll -= 40
                elif event.button == 5:
                    self.scroll += 40
            
        if event.type == pygame.MOUSEWHEEL and self.is_open:
            self.scroll -= event.y * 40

        return None
    
    def draw(self, screen):
        panel_rect = pygame.Rect(int(self.x), 0, self.width, self.screen_height)
        tab_rect = pygame.Rect(self.screen_width - 36, self.screen_height - 110, 36, 90)

        #panel
        if self.x < self.screen_width:
            pygame.draw.rect(screen, (235, 220, 180), panel_rect)
            pygame.draw.line(screen, (90, 60, 30), (panel_rect.x, 0), (panel_rect.x, self.screen_height), 4)

            #title
            title = self.title_font.render("Monkey Shop", True, (60, 35, 15))
            screen.blit(title, (panel_rect.x + 40, 25))

            #upgrade box
            upgrade_rect = pygame.Rect(panel_rect.x + 18, 107- self.scroll, self.width - 36, 90)
            pygame.draw.rect(screen, (255, 248, 220), upgrade_rect, border_radius=12)
            pygame.draw.rect(screen, (90, 60, 30), upgrade_rect, 3, border_radius=12)

            text = self.item_font.render("+1 money per click", True, (30, 30, 30))
            text_rect = text.get_rect(center=(upgrade_rect.centerx, upgrade_rect.y +30))
            screen.blit(text, text_rect)

            subtext = self.small_font.render("UI only for now", True, (90, 90, 90))
            subtext_rect = subtext.get_rect(center=(upgrade_rect.centerx, upgrade_rect.y + 60))
            screen.blit(subtext, subtext_rect)


        #tab
        pygame.draw.rect(screen, (120, 75, 40), tab_rect, border_radius=8)
        pygame.draw.rect(screen, (70, 40, 20), tab_rect, 3, border_radius=8)


        #arrow
        if self.is_open:
            points = [
                (tab_rect.x + 12, tab_rect.y + 18),
                (tab_rect.x + 24, tab_rect.y + tab_rect.height // 2),
                (tab_rect.x + 12, tab_rect.y + tab_rect.height - 18)
            ]
        else:
            points = [
                (tab_rect.x + 24, tab_rect.y + 18),
                (tab_rect.x + 12, tab_rect.y + tab_rect.height // 2),
                (tab_rect.x + 24, tab_rect.y + tab_rect.height - 18)
            ]

        pygame.draw.lines(screen, (255, 255, 255), False, points, 4)