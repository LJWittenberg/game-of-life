import time       # To replace time.h and parts of unistd.h (sleep function)
import random     # To replace rand-related functions from stdlib.h
import os         # For any OS-level operations similar to unistd.h

# String handling and character type checks are built-in:
# No need to import anything extra for equivalents of ctype.h and string.h

class Board:
    def __init__(self, rows, cols):
        """
        Initialize the game grid in the form of a coordinate system.
        The top left corner has the coordinates x = 0; y = 0
        The top right corner has the coordinates x = cols - 1; y = 0
        The bottom left corner has the coordinates x = 0; y = rows - 1
        The bottom right corner has the coordinates x = cols - 1; y = rows - 1
        At the start of the game all cells are dead.
        :param rows: Number of rows in the grid.
        :param cols: Number of columns in the grid.
        """
        self.max_rows = rows
        self.max_cols = cols
        self.current_cells = [[0 for _ in range(cols)] for _ in range(rows)]
        self.updated_cells = [[0 for _ in range(cols)] for _ in range(rows)]

        # Initializing both grids with dead cells (0)
        self.initialize_board()

    def initialize_board(self):
        """
        Custom method to initialize or reset the game board.
        Sets all cells in current_cells and updated_cells to 0 (dead).
        """
        for i in range(self.max_rows):
            for j in range(self.max_cols):
                self.current_cells[i][j] = 0
                self.updated_cells[i][j] = 0

    def __cell_in_grid(self, cur_row, cur_col):
        return 0 <= cur_row < self.max_rows and 0 <= cur_col < self.max_cols

    def __repr__(self):
        return f"Board({self.max_rows}, {self.max_cols})"