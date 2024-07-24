#PLACEHOLDER NOT THE FINAL BUILD

import argparse

def main():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument('input_file', type=str, help='Input file for the initial configuration')
    parser.add_argument('output_file', type=str, help='Output file to save the final configuration')
    parser.add_argument('--steps', type=int, default=100, help='Number of steps to simulate')

    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    steps = args.steps

    # Call your game functions here, passing these arguments as needed
    # initialize_grid(input_file)
    # simulate_game(steps)
    # save_grid(output_file)

if __name__ == "__main__":
    main()