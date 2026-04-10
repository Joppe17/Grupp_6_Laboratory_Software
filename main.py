"""
This is the main file which the game will run from.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "logic"))

#from logic.game_loop import run

#run()

from ui.whack_a_monkey import run_minigame

run_minigame(screen, clock)
