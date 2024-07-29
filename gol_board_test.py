import unittest
from gol_board import Board

class TestGameOfLife(unittest.TestCase):
    
    def setUp(self):
        self.test_game = Board(6, 6)
        
    def test_initialize_board(self):
        # testing if the requested dimensions have been created.
        self.test_game.current_cells[0][0] = 1
        self.test_game.current_cells[2][2] = 1
        self.test_game.current_cells[5][5] = 1
        
        self.assertEqual(self.test_game.current_cells[0][0], 1)
        self.assertEqual(self.test_game.current_cells[2][2], 1)
        self.assertEqual(self.test_game.current_cells[5][5], 1)

    def test_enforce_rules(self):
        self.test_game_neigh = Board(3, 3)
        
        # Initialize the specific test scenario
        self.test_game_neigh.current_cells[1][0] = 1
        self.test_game_neigh.current_cells[1][1] = 1
        self.test_game_neigh.current_cells[1][2] = 1
        
        self.test_game_neigh.enforce_rules()
        self.test_game_neigh.swap_cell_states()
        
        self.assertEqual(self.test_game_neigh.current_cells[0][1], 1)
        self.assertEqual(self.test_game_neigh.current_cells[1][1], 1)
        self.assertEqual(self.test_game_neigh.current_cells[2][1], 1)

    def test_check_dead_life(self):
        self.test_game_neigh = Board(3, 3)
        
        # Initialize the specific test scenario
        self.test_game_neigh.current_cells[1][0] = 1
        self.test_game_neigh.current_cells[1][1] = 1
        self.test_game_neigh.current_cells[1][2] = 1
        
        self.test_game_neigh.enforce_rules()
        self.test_game_neigh.swap_cell_states()
        
        result = self.test_game_neigh.check_dead_life()
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()