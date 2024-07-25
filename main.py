import argparse
import time
from gol_board import Board

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
    args = parse_args()

    input_file = args.input_file
    
    # Initialize the game board
    game = Board(40, 210)

    # Load initial configuration into the board
    load_initial_configuration(game, input_file)
    
    game_active = True
    while game_active:
        game.print_game()
        time.sleep(1)
        game.enforce_rules()
        game.swap_cell_states()
        game_active = game.check_dead_life()

if "__main__" == __name__:
    main()