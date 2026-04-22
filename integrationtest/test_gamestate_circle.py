import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import pytest
import pygame
from logic.game_state import GameState
from ui.circle import Circle

def setup():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    state = GameState()
    circle = Circle(400, 300, 50, "images/monkey_clicker.jpg", state)
    yield circle, state, screen
    pygame.quit()

def test_circle_initial_state(setup):
    circle, state, screen = setup
    assert circle.active == False
    assert state.score == 0
    assert state.click_multiplier == 1

def test_circle_click_activation(setup):
    circle, state, screen = setup
    click_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(400, 300), button=1)
    circle.handle_event(click_event)
    assert state.score == 1
    assert state.click_multiplier == 1

