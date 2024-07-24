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