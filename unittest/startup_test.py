import unittest
from unittest.mock import patch
 
 
class TestGameLoop(unittest.TestCase):
    
    @patch('main.pygame')
    @patch('main.GameState')
    @patch('main.Background')
    @patch('main.Hud')
    @patch('main.Circle')
    @patch('main.MuteButton')
    @patch('main.flyingBanana')
    @patch('main.StartMenu')
    def test_pygame_init(self, *mocks):
        """Test that pygame.init() is called"""
        from main import run
        
        mocks[0].display.set_mode.return_value = None
        mocks[0].time.Clock.return_value.tick.return_value = 16
        mocks[0].event.get.return_value = [type('Event', (), {'type': 12})()]  # QUIT event
        
        run()
        
        mocks[0].init.assert_called_once()
 
 
if __name__ == '__main__':
    unittest.main()
