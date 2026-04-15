import unittest
import sys

sys.path.insert(0, '..')


class TestGameLoop(unittest.TestCase):
    
    def test_run_function_exists(self):
        """Test that run function exists"""
        from logic.game_loop import run
        self.assertTrue(callable(run))


if __name__ == '__main__':
    unittest.main()
