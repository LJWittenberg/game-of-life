from window_cell import Cell
import time

class Grid:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        # cell_size
        cell_size_x,
        cell_size_y,
        gol,
        win = None
        
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self.__create_cells(gol)

    def __create_cells(self, board):
        for i in range(self._num_rows):
            row_cells = []
            for i in range(self._num_cols):
                row_cells.append(Cell(self._win))
            self._cells.append(row_cells)
        board.copy_board_to_grid(self)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self.__draw_cell(i, j)

    """ prepare to delete
    def __copy_board_to_grid(self, board):
        if self._num_rows != board.max_rows or self._num_cols != board.max_cols:
            raise Exception("miss matching grid sizes!")
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                if board.current_cells[i][j] == 1:
                    self._cells[i][j].alive = True
    """

    def __draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1,y1,x2,y2)
        self.__animate()

    def __animate(self):
        if self._win is None:
            return
        self._win.redraw()
        #time.sleep(0.05)

    def update_grid_from_board(self):
        self.__copy_board_to_grid(self._game_board)
    
    def grid_call_draw(self, i,j):
        self.__draw_cell(i,j)
