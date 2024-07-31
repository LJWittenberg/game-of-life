import time       # To replace time.h and parts of unistd.h (sleep function)
from game_grid import Grid

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
        self.gen_check = 1
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
    def __enforce_rules(self):
        for i in range(self.max_rows):
            for j in range(self.max_cols):
                neighbour_live_cell = self.__count_live_neighbours(i, j)
            
                # check if a live cell should stay alive
                if self.current_cells[i][j] == 1 and (neighbour_live_cell == 2 or neighbour_live_cell == 3):
                    self.updated_cells[i][j] = 1

                # check if a dead cell should become alive
                elif self.current_cells[i][j] == 0 and neighbour_live_cell == 3:
                    self.updated_cells[i][j] = 1

                # if none of the previous conditions apply, the cell should be dead
                else:
                    self.updated_cells[i][j] = 0

    """
    Function to print out the live cells of the grid to create the Game of Life simulation.
    likely replace later with Tkinter representation
    """
    def __print_game(self):
        for i in range(self.max_rows):
            for j in range(self.max_cols):
                if self.current_cells[i][j] == 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()  # for new line after each row
        print()  # additional new line after the entire board

    """
    transfering the data of updated_cells into current_cells and declaring all cells in updated cells as dead.
    public for now
    """
    def __swap_cell_states(self):
        for i in range(self.max_rows):
            for j in range(self.max_cols):
                self.current_cells[i][j] = self.updated_cells[i][j]
                self.updated_cells[i][j] = 0

    """
    Function to varify if any live cells are left withing the game.
    public for now
    """
    def __check_dead_life(self):
        dead = 0
        for i in range(self.max_rows):
            for j in range(self.max_cols):
                if self.current_cells[i][j] == 1:
                    dead = 1
                    break  # Once a living cell is found, no need to continue checking
            if dead == 1:
                break
        return dead

    def run_game_logic(self, grid_x1, grid_y1, window, cell_size_x, cell_size_y):
        # Create the Grid using the provided parameters
        grid = Grid(grid_x1, grid_y1, self.max_rows, self.max_cols, cell_size_x, cell_size_y, self, window)
        self.gen_check = 1
        self.game_active = True
        self.window = window

        def step():
            if self.game_active:
                grid.clear_grid()
                self.__print_game()
                self.__enforce_rules()
                self.__swap_cell_states()
                # Update the Grid's cells from the Board
                self.copy_board_to_grid(grid)
                
        
                # Draw the cells on the grid
                for i in range(self.max_rows):
                    for j in range(self.max_cols):
                        grid.grid_call_draw(i, j)
                

                self.game_active = self.__check_dead_life()
                print(f"{self.gen_check}")
                self.gen_check += 1

                # Schedule the next step
                time.sleep(1)
                self.window.after(500, step)
            else:
                pass
        # Start the first step
        step()
    
    def copy_board_to_grid(self, grid):
        for i in range(self.max_rows):
            for j in range(self.max_cols):
                if self.current_cells[i][j] == 1:
                    grid._cells[i][j].alive = True

    

    def __repr__(self):
        return f"Board({self.max_rows}, {self.max_cols})"