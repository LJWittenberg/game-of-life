import argparse
import time
from gol_board import Board
from window_cell import Cell
from graphics import Window

def parse_args():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument('input_file', type=str, help='Input file for the initial configuration')
    return parser.parse_args()

def load_initial_configuration(board, input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):  # Ignore comments
                row_idx, col_idx = map(int, line.split())
                board.current_cells[row_idx][col_idx] = 1  # Setting the cell as alive

def transfer_cell_to_canvas(cells, game, win):
    new_cells = cells.copy()
    for i in range(game.max_rows):
        for j in range(game.max_cols):
            if game.current_cells[i][j] == 1:
                    wc = Cell(i,j,i+5,j+5, win)
                    new_cells.append(wc)
    return new_cells


def main():
    args = parse_args()

    input_file = args.input_file
    
    # Initialize the game board
    max_p_x = 1910
    max_p_y = 1000
    # 5x5 game = Board(382, 200) work towoards that
    # 4x4 game = Board(477, 250) meh 
    game = Board(40, 210)
    win = Window(max_p_x, max_p_y)

    # Load initial configuration into the board
    load_initial_configuration(game, input_file)

    cells = []
    cells = transfer_cell_to_canvas(cells, game, win) # in spirit of pure functions
    for cell in cells:
        cell.draw()
    """
    c1 = Cell(0, 0, 5, 5,win)
    c1.draw()

    c2 = Cell(max_p_x-5, max_p_y-5, max_p_x, max_p_y,win)
    c2.draw()
    """
    win.wait_for_close()
    game.run_game_logic()    

if "__main__" == __name__:
    main()