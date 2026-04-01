import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "logic"))

from logic.game_loop import run

run()
