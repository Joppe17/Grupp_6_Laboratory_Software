import unittest
import sys

sys.path.insert(0, '..')


class TestGameLoop(unittest.TestCase):
    
    def test_run_function_exists(self):
        """Test that run function exists"""
        from logic.game_loop import run
        self.assertTrue(callable(run))
    
    def test_game_state_imports(self):
        """Test that GameState class can be imported"""
        from logic.game_state import GameState
        self.assertTrue(callable(GameState))
    
    def test_game_state_initialization(self):
        """Test that GameState initializes with default score of 0"""
        from logic.game_state import GameState
        state = GameState()
        self.assertEqual(state.score, 0)
    
    def test_circle_imports(self):
        """Test that Circle class can be imported"""
        from ui.circle import Circle
        self.assertTrue(callable(Circle))


if __name__ == '__main__':
    unittest.main()
