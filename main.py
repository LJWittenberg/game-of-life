import argparse
import time
from gol_board import Board
from window_cell import Cell
from graphics import Window
from game_grid import Grid

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


def main():
    try:
        args = parse_args()

        input_file = args.input_file
    
        # Initialize the game board
        max_p_x = 1910
        max_p_y = 1000

        game = Board(382, 200)
        win = Window(max_p_x, max_p_y)

        # Load initial configuration into the board
        load_initial_configuration(game, input_file)

        game.run_game_logic(0, 0, win, 5, 5)  
        win.wait_for_close()
    except KeyboardInterrupt:
        print(f"\nGame-of-Life stopped at the {game.gen_check} Generation.")
     

if "__main__" == __name__:
    main()