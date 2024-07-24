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

    """
    Support function to test if a specific cell in inside of the grid.
    used for the count_live_neighbours function and indirectly for the enforce_rules function.
    """
    def __cell_in_grid(self, cur_row, cur_col):
        return 0 <= cur_row < self.max_rows and 0 <= cur_col < self.max_cols
    
    """
    Support function that counts all surrounding live neighbours of a inspected cell.
    @param cur_row and cur_col represent the x and y coordinates of the inspected cell.
    """
    def __count_live_neighbours(self, cur_row, cur_col):
        count = 0
        for i in range(cur_row - 1, cur_row + 2):
            for j in range(cur_col - 1, cur_col + 2):
                proceed_check = self.__cell_in_grid(i,j)
                if i == cur_row and j == cur_col:
                    continue
                if self.__cell_in_grid(i, j) and self.current_cells[i][j] == 1:
                    count += 1
        return count
    
    def clear_board(self):
        """Clears the board by setting all cells to None or empty lists."""
        self.current_cells = None
        self.updated_cells = None
        print("Board has been cleared.")

    """
    Function to apply the rules of Conways game of Life.
    public for now
    """
    def enforce_rules(self):
        pass

    """
    Function to print out the live cells of the grid to create the Game of Life simulation.
    likely replace later with Tkinter representation
    """
    def print_game(self):
        pass

    """
    transfering the data of updated_cells into current_cells and declaring all cells in updated cells as dead.
    public for now
    """
    def swap_cell_states(self):
        pass

    """
    Function to varify if any live cells are left withing the game.
    public for now
    """
    def check_dead_life(self):
        pass
    def __repr__(self):
        return f"Board({self.max_rows}, {self.max_cols})"