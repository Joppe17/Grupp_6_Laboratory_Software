import pytest
import pygame
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic.game_state import GameState

pygame.init()
pygame.display.set_mode((640, 640))

from ui.circle import Circle

IMAGE_PATH = "images/monkey_clicker.jpg"

@pytest.fixture
def setup():
    state = GameState()
    circle = Circle(320, 320, 95, IMAGE_PATH, state)
    return circle, state


def test_click_increases_score(setup):
    circle, state = setup
    click = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (320, 320), "button": 1})
    circle.handle_event(click)
    assert state.score > 0

def test_click_outside_does_not_increase_score(setup):
    circle, state = setup
    click = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (0, 0), "button": 1})
    circle.handle_event(click)
    assert state.score == 0

def test_multiplier_affects_score(setup):
    circle, state = setup
    state.click_multiplier = 2
    click = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (320, 320), "button": 1})
    circle.handle_event(click)
    assert state.score == 2 * state.permanent_x2_multiplier

def test_x2_multiplier_affects_score(setup):
    circle, state = setup
    state.permanent_x2_multiplier = 2
    click = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (320, 320), "button": 1})
    circle.handle_event(click)
    assert state.score == 2

def test_click_grows_radius(setup):
    circle, state = setup
    original_target = circle.target_radius
    click = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (320, 320), "button": 1})
    circle.handle_event(click)
    assert circle.target_radius > original_target

def test_radius_shrinks_back_over_time(setup):
    circle, state = setup
    click = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (320, 320), "button": 1})
    circle.handle_event(click)
    grown_target = circle.target_radius
    circle.update(2.0) 
    assert circle.target_radius < grown_target

def test_radius_never_goes_below_base(setup):
    circle, state = setup
    circle.update(999.0)
    assert circle.radius >= circle.base_radius


