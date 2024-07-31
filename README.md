Conway's Game of Life implementation by Lennard Wittenberg in the language Python
=================================================================================
project task for [Bootdev-course-personal-project-1](https://www.boot.dev/tracks/backend)
My aim with this project is to complete my first implementation of the Game of Life C. At the time I wasn't able to finish the project in University and had leave in a incomplete state.
<!---
 maybe link to old project on github 
--->

## What is the Game of Life short explenation 
This is the describtion by the Cornell University  
The Game of Life (an example of a cellular automaton ) is played on an infinite two-dimensional rectangular grid of cells. Each cell can be either alive or dead. The status of each cell changes each turn of the game (also called a generation) depending on the statuses of that cell's 8 neighbors.

## How access and use the project.
1. **Clone the repository**: `git clone <repository-url>`
2. **Navigate to the project directory**: `cd <project-directory>`
3. **Open the Coordinates File**:
4. **Create your first Generation**: Enter the a series of coordinates for the two dimensional game grid. (x,y) These coordinates will become the first cell generation. Example for a coordinates pair:  
11 0 --> (x/row = 11; y/col = 0)
6. **Run the program**: Execute `python main.py` with either the coordinates you wrote as argument `coordinates.md` or the preset `presets.md` in your terminal.
**Example call**: ``python main.py presets.md`

## About the project
- In addition to the window and canvas representation the programm also has a console print which is enabled by default. This print is was used to ensure that the Logic and rules of the Game of Life were enforced accordingly. The print now serves as an additional way to represent the cells or as a debugging tool to check if a figure was set correctly.
- **Example for how a figure would look** The given coordinate pairs: (0,0);(1,0);(1,1);(0,1) would create the `Block` Pattern from the `Figure examples` picture in the top left corner.
<img src="https://blog.xojo.com/wp-content/uploads/2022/05/CleanShot-2022-05-02-at-14.25.12@2x-1024x924.png" alt="Figure examples" width="500"/>
- rules etc.
- presets.md 
- coordinates.md

## Note
- Check out the presets.md file before starting. A short explanation how to handle coordinates can be found there.
- When the window is manually closed via the close botton. Then the programm will terminate after the current generation has rendered completly. Therefore it can happen that the window will not instantly close when pressed.


## State of the project
- [x] rules
- [x] unit tests
- [x] visual representation
- [x] handeling and code combination 
- [x] Project base
- [x] improvements work in progress.

# Creators and Contributers
- Lennard J.W
- Bootdev Community 

# Scoures and Insparation
- [Geeks for Geeks](https://www.geeksforgeeks.org/program-for-conways-game-of-life/)
- [Game of Life Wiki](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [Window and Canvas Prototyp-BootDev](https://www.boot.dev/lessons/fb0967e1-a304-4110-8bf3-41071d99af0c)
- [Play John Conway's Game of Life](https://playgameoflife.com)
- [Game of Life figure Library](https://conwaylife.appspot.com/library/a)
- **Pictures**
- [example figures](https://blog.xojo.com/wp-content/uploads/2022/05/CleanShot-2022-05-02-at-14.25.12@2x-1024x924.png)
