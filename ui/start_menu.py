import pygame

def draw_start_menu(screen):
    panel_width = 500
    panel_height = 350

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    panel_x = (screen_width - panel_width) // 2
    panel_y = (screen_height - panel_height) // 2

    panel_rect = pygame.Rect(panel_x, panel_y, panel_width, panel_height)
    panel_color = (245, 222, 179)
    border_color = (139, 69, 19)

    pygame.draw.rect(screen, panel_color, panel_rect, border_radius=20)
    pygame.draw.rect(screen, border_color, panel_rect, width=4, border_radius=20)