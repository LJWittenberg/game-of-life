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

    """ private function removed from tests
    def test_cell_in_grid(self):
        # testing cell in grid function.
        pos1 = self.test_game.__cell_in_grid(0, 0)
        pos2 = self.test_game.__cell_in_grid(5, 5)
        pos3 = self.test_game.__cell_in_grid(2, 2)
        pos4 = self.test_game.__cell_in_grid(-1, 3)
        pos5 = self.test_game.__cell_in_grid(8, 99)
        
        self.assertEqual(pos1, 1)
        self.assertEqual(pos2, 1)
        self.assertEqual(pos3, 1)
        self.assertEqual(pos4, 0)
        self.assertEqual(pos5, 0)
    """

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